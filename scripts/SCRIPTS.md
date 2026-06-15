# Scripts — Driver Data Pipeline

Three-stage pipeline: **seed → crawl → extract**. Each stage is independent and
idempotent. Re-run any stage any time without clobbering earlier work.

---

## Pipeline Overview

```
extract_urls.py          crawl_cache.py           extract_drivers.py
      |                        |                          |
  drivers.json   -->   research/source_urls.md -->   research/cache/   -->  drivers_extracted.json
  drivers.md                  (seeds)               manifest.json
  *_index.md         + BFS discovers PDFs
                       from HTML pages
                       + appends to source_urls.md
```

---

## Stage 1 — `extract_urls.py`

**Purpose:** Produce `research/source_urls.md` — the seed URL list.

**Sources scanned:**
- `drivers.json` — every `prices[].url` and `datasheets[].url`
- `drivers.md` — every line containing a URL
- `research/*_index.md` — all markdown links and bare URLs
- **Constructed URLs** — SI product-page URLs and loudspeakerdatabase.com URLs
  auto-generated from every brand+model in `drivers.json` (404s are silently
  skipped by the crawler)

**Run when:** New drivers are added to `drivers.json` or `drivers.md`, or when
index files are updated.

```
python scripts/extract_urls.py
```

Output: `research/source_urls.md` (overwritten each run — hand-edits survive
because `crawl_cache.py` appends to it rather than regenerating it).

---

## Stage 2 — `crawl_cache.py`

**Purpose:** BFS crawler — fetches every uncached URL and discovers new ones.

**How it works:**
1. Reads `research/source_urls.md` as seeds
2. Skips URLs already in `research/cache/manifest.json`
3. Fetches in parallel (50 workers, no rate-limiting by default)
4. Caches everything: HTML, PDF, JSON, etc.
5. After fetching each HTML page, extracts discovered URLs:
   - `.pdf` links anywhere
   - `doc.soundimports.nl/pdf/` datasheet links (the most important)
   - Manufacturer PDF links (sbacoustics.com, seas.no, scan-speak.dk, etc.)
6. Discovered URLs are added to the live queue AND appended to `source_urls.md`

**Cache filename:** `SHA-256(url).{html|pdf|json}` — deterministic, collision-free.

**Manifest:** `research/cache/manifest.json` — maps URL → `{file, content_type,
status, size_bytes, fetched_at, final_url}`.

**Run when:** After `extract_urls.py`, or whenever you want to fetch new URLs.

```
python scripts/crawl_cache.py [--workers 200] [--timeout 20]
python scripts/crawl_cache.py --force      # re-fetch everything
```

**Re-run safety:** Already-cached URLs are always skipped unless `--force`.

---

## Stage 3 — `extract_drivers.py`

**Purpose:** Parse every cached file and produce `drivers_extracted.json`.

**How it works:**
1. Reads `research/cache/manifest.json`
2. For each cached file (HTML or PDF):
   - Determines site type from the source URL
   - Extracts specs using a site-specific parser (SI, LDB, Willys, HFC, Falcon, LSS, Dayton)
   - **Driver type** (high/mid/sub/pr/full_range) is detected from page content
     (product title, description, spec fields) — never from filename or index
   - **`manu:manucode`** identity key extracted from content:
     - Primary: JSON-LD `schema.org/Product` → `brand.name` + `name`
     - Fallback: OpenGraph `og:title`
     - Fallback: `<h1>` text
     - Fallback: `<title>` text
     - Last resort: URL slug parsing
3. Groups data by `manu:manucode` — same driver from multiple sources is merged
4. Merge priority: soundimports > datasheet_si > datasheet > loudspeakerdatabase >
   dayton > hfc > falcon > willys > lss > other

**Run when:** After `crawl_cache.py` completes, or any time you want fresh extraction.

```
python scripts/extract_drivers.py [--output drivers_extracted.json]
```

PDF parsing requires pypdf: `pip install pypdf`

---

## manu:manucode Key

Format: `brand:model` — all lowercase, brand has punctuation stripped, model has
spaces replaced with hyphens.

Examples:
- `dayton:nd91-4`
- `sbacoustics:sb12pfcr25-4`
- `seas:27tdfc-h1189-06`
- `scanspeak:r2604-833000`

This key is the same regardless of which site the data came from, enabling
deduplication and cross-source merging in `drivers_extracted.json`.

---

## Full Re-run

```
python scripts/extract_urls.py      # rebuild seed list
python scripts/crawl_cache.py       # fetch uncached URLs (skips existing)
python scripts/extract_drivers.py   # parse all cached files
```

To wipe the cache and start fresh:

```
rm -rf research/cache/
python scripts/crawl_cache.py --workers 50
python scripts/extract_drivers.py
```

---

## Other Scripts

| Script | Purpose |
|--------|---------|
| `build_drivers_json.py` | Builds `drivers.json` from `drivers.md` + index files |
| `refetch_drivers.py` | Legacy: parallel fetch into `drivers_refetched.json` (superseded by this pipeline) |
| `scratch.py` | One-off investigations — always use this, never create new `_*.py` temp files |
