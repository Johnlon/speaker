# Driver Combination Spreadsheet

Exhaustive record of mid + tweeter pairings evaluated against the locked subwoofer (Tang Band W5-1138SMF). One entry per combination. Records crossover window, centre spacing, PSU voltage, visual notes, ruling, and trade-offs. Curated scenario recommendations are in [solutions.md](solutions.md).

---

## System Reference

- Sub at 40W RMS → **98 dB @1m** (continuous reference)
- Sub burst at 80W → **101 dB @1m** (transient ceiling)
- JAB5 amp output (η = 0.85, full H-bridge class D): 24V → 31W/8Ω, 61W/4Ω | 29V → 45W/8Ω, 90W/4Ω
- Crossover targets: sub LP 150 Hz (LR24) · mid BP 150–2,800 Hz · tweeter HP 2,800 Hz (LR48)

### Power needed per driver at reference levels

| Driver | Role | Imp | Sensitivity | Needed @ 98 dB | Needed @ 101 dB | Available @ 24V | PSU |
|--------|------|-----|-------------|----------------|-----------------|-----------------|-----|
| TB W5-1138SMF | Sub | 4Ω | 85 dB | 40W RMS | 80W | ~61W | 24V |
| SIG120-4 | Mid | 4Ω | 89.7 dB | 13.5W | 27W | ~61W | 24V |
| DS115-8 | Mid | 8Ω | 85.3 dB | 18.6W | 37.2W | ~31W | 24V |
| HiVi B4N | Mid | 8Ω | 85 dB | 20.0W | 40W | ~31W | 24V |
| DSA90-8 | Mid | 8Ω | 84.7 dB | 21.4W | 42.8W | ~31W | 24V (burst: 29V) |
| TCP115-8 | Mid | 8Ω | 81.9 dB | 40.7W | 81.4W | ~31W | **29V required** |
| SB19ST | Tweeter | 4Ω | 88.5 dB | 17.8W | 35.5W | ~61W | 24V |

Total DC draw at matched 98 dB (RMS): ~78–90W from PSU (~3.5–4A at 24V). At sub burst (80W): ~120W peak (~5A at 24V) — within LRS-150-24 (6.5A) for music content. Capacitor bank absorbs transient peaks.

---

## Beaming Limits — Maximum Useful Mid/Tweeter Crossover

| Mid | Beams above |
|-----|-------------|
| DSA90-8 | **3,260 Hz** |
| SB12PFCR/MNRX2-25-4 (4") | **2,730 Hz** |
| DS115-8 / HiVi B4N | ~2,636 Hz |
| SPM-116/8 / Beyma 4FR40 / DA115-8 | ~2,600 Hz |
| TCP115-8 / SIG120-4 | ~2,570 Hz |
| HiVi M5N (5") | ~2,185 Hz |
| SB13PFC25-8 / SDS-P830656 | ~2,080 Hz |
| SIG150-4 (5.25") | **1,990 Hz** |

---

## Tweeter Minimum Crossover (2× Fs)

| Tweeter | Min xover |
|---------|-----------|
| XT25TG30-04 | **880 Hz** |
| DX25TG59-04 | 1,180 Hz |
| SB29SDAC / SB29RDNC | 1,200 Hz |
| XT25SC90-04 | 1,650 Hz |
| **SB19ST** | **1,960 Hz** ← reference tweeter |
| DT-28N | 2,400 Hz |
| ND25FA-4 | 2,700 Hz |
| HiVi TN25 | 3,000 Hz |
| Markaudio TW 6 | **3,400 Hz** — most constrained |

---

## All Pairings — Quick Reference

| ID | Mid | Tweeter | Xover | Price | PSU | Character | Key reason for rank |
|----|-----|---------|-------|-------|-----|-----------|-------------------|
| S1 | DS115-8 | SB19ST | 2,500 Hz | ~£50 | 24V | Warm | Reference pairing; paper warmth + 19mm dome; 4 left |
| S2 | SB12PFCR25-4 | SB19ST | 2,700 Hz | ~£41 | 24V | Warm, natural | Best value; natural fibre; 10+ stock |
| S3 | SB12MNRX2-25-4 | SB29SDAC | 1,200–2,700 Hz | ~£92 | 24V | Warm-neutral | Ring dome; wide xover window; engineering showcase |
| A1 | HiVi B4N | SB19ST | 2,500 Hz | ~£38 | 24V | Warm | Sensitivity-matched; simplest DSP |
| A2 | SB12MNRX2-25-4 | SB19ST | 2,700 Hz | ~£72 | 24V | Warm, dynamic | Natural fibre; controlled transients |
| A3 | DSA90-8 | SB19ST | 2,800 Hz | ~£49 | 24V | Detailed | Tightest round spacing (90mm); narrowest baffle |
| A4 | DS115-8 | DX25TG59-04 | 1,800–2,500 Hz | ~£60 | 24V | Warm, flexible | Paper warmth + widest crossover window (standard dome) |
| A5 | SB12PFCR25-4 | DX25TG59-04 | 1,800–2,700 Hz | ~£51 | 24V | Warm, flexible | A4 concept; cheaper |
| A6 | Beyma 4FR40 | SB19ST | 2,500 Hz | ~£45 | 24V | Warm | Paper+Santoprene; confirm Fs before ordering |
| A7 | SPM-116/8 | SB19ST | 2,500 Hz | ~£37 | 24V | Warm | Cheapest paper mid |
| A8 | SIG120-4 | SB19ST | 2,500 Hz | ~£48 | 24V | Clear, dynamic | 4Ω mid; excellent amp headroom; Audiophonics FR |
| B1 | TCP115-8 | SB19ST | 2,500 Hz | ~£31+PSU | **29V** | Warmest | Cheapest drivers; warmest character |
| B2 | ND91-4 | SB19ST | 2,700 Hz | ~£48 | **29V** | Detailed | Xmax 4.6mm; compact 3.5" |
| B3 | HiVi M5N | DX25TG59-04 | 1,200–2,100 Hz | ~£54 | 24V | Warm | 5"; Fs 3.0×; needs DX25 |
| B4 | SB13PFC25-8 | DX25TG59-04 | 1,200–2,080 Hz | ~£53 | 24V | Warm | Best Fs margin (3.33×); natural fibre 5" |
| B5 | DA115-8 | SB19ST | 2,500 Hz | ~£44 | 24V | Detailed | Near-perfect sensitivity match |
| B6 | DSA90-8 | HiVi TN25 | 3,000 Hz | ~£52 | 24V | Detailed | Tightest spacing (73mm); square tweeter |
| B7 | SDS-P830656 | DX25TG59-04 | 1,500–2,000 Hz | ~£54 | 24V | Natural | Xmax 10mm |
| B8 | SIG150-4 | DX25TG59-04 | 1,500–1,990 Hz | ~£60 | 24V | Neutral | Large mid; low xover; wide baffle |
| B9 | SB12PACR25-4-COAX | built-in | 2,800 Hz | ~£59 | 24V | Clear | Point source; 94 dB ceiling |
| B10 | DSA90-8 | ND25FA-4 | 2,700 Hz | ~£44 | 24V | Detailed | Minimum round spacing (79mm) |
| B11 | DSA90-8 | DT-28N | 2,500 Hz | ~£65 | 24V | Detailed | Compact waveguide tweeter; tight spacing |
| B12 | SLS-85S25CP04-04 | DT-28N | 2,500 Hz | ~£61 | **29V** | Warm | Oval mid; Xmax 10.2mm |
| RR1 | DS115-8 | XT25TG30-04 | 880–2,636 Hz | ~£62 | 24V | Warm + wide | Best ring radiator; widest xover window |
| RR2 | SB12PFCR25-4 | XT25TG30-04 | 880–2,730 Hz | ~£52 | 24V | Warm + wide | Best value ring radiator |
| RR3 | SB12MNRX2-25-4 | XT25TG30-04 | 880–2,730 Hz | ~£83 | 24V | Warm + wide | Ring radiator + natural fibre |
| RR4 | DSA90-8 | XT25SC90-04 | 2,800 Hz | ~£37 | 24V | Detailed + wide | Cheapest ring radiator; single Falcon order |
| RR5 | SIG150-4 | XT25TG30-04 | 1,000–1,990 Hz | ~£67 | 24V | Neutral | Only tweeter compatible with SIG150-4 |
| RR6 | DS115-8 | SB29SDAC | 1,200–2,636 Hz | ~£71 | 24V | Warm + ring dome | Ring dome + paper warmth |
| C1 | RS100-8 | SB19ST | 2,500 Hz | ~£60 | 24V | Detailed | Fs 1.63× — marginal |
| C2 | PA130-8 | SB19ST | 2,000 Hz | ~£47 | 24V | Natural | Xmax 2mm; Fs 1.8× |
| C3 | TF0510 | SB19ST | 2,200 Hz | ~£45 | 24V | Natural | Weakest Fs + Xmax |
| C4 | DSA90-8 | TW 6 | 3,200–3,400 Hz | ~£69 | 24V | Detailed | Xover above beaming limit; poor 60° performance |

---

## Detailed Pairing Entries

### Tier S — Outstanding all-rounders

**S1 · DS115-8 + SB19ST**
- Xover: 2,500 Hz | Spacing: 102 mm | Price: ~£50 (SI) / ~£41 (Falcon tweeter) | PSU: **24V / ~3.8A**
- Fs: 55.2 Hz → 2.72× at 150 Hz — best of any paper-cone mid
- **Why S1:** Confirmed dark coated-paper cone (datasheet-verified). Warm, musical character matching the GHM-inspired tonal goal. SB19ST 19 mm dome = widest HF dispersion of any tweeter candidate — directly addresses the 60° off-axis kitchen position. Best Fs margin in the field. Note: 4 units left at SoundImports.

---

**S2 · SB12PFCR25-4 + SB19ST**
- Xover: 2,700 Hz | Spacing: 105 mm | Price: ~£41 | PSU: **24V / ~3.8A**
- Fs: 58 Hz → 2.59× at 150 Hz — excellent. 10+ stock both drivers.
- **Why S2:** Natural fibre paper cone — warm, organic character. Best value in the catalogue. Default choice if DS115-8 sells out, and arguably the better value pick regardless.

---

**S3 · SB12MNRX2-25-4 + SB29SDAC-C000-4** ← premium pick
- Xover: 1,200–2,700 Hz (1,500 Hz tuning window) | Spacing: ~107 mm | Price: ~£92 | PSU: **24V / ~4A**
- **Why S3:** Engineering showcase under £100. SDAC ring dome construction (stabilising ring reduces distortion vs standard dome) gives wider off-axis dispersion. MNRX2's Qts 0.27 = very controlled midrange transients. Natural fibre + ring dome = warm-to-neutral character. Wide crossover tuning window is useful during EQ optimisation.

---

### Tier A — Very good; specific strengths

**A1 · HiVi B4N + SB19ST**
- Xover: 2,500 Hz | Spacing: 102 mm | Price: ~£38 | PSU: **24V / ~3.9A**
- Fs: 56 Hz → 2.68× at 150 Hz. 10+ stock both.
- **Best for:** Sensitivity naturally matched to sub — minimal DSP correction needed on the mid channel. Reliable, good value, always in stock. Al/Mg cone (copper-tone anodising — noted). Best choice when you want a working system quickly.

---

**A2 · SB12MNRX2-25-4 + SB19ST**
- Xover: 2,700 Hz | Spacing: 105 mm | Price: ~£72 | PSU: **24V / ~3.9A**
- **Best for:** MNRX2's Qts 0.27 gives very well-controlled midrange transients. Natural fibre cone, warm character. Best dynamic capability under £100 with conventional tweeter.

---

**A3 · DSA90-8 + SB19ST**
- Xover: 2,800 Hz | Spacing: **90 mm** (tightest round pairing) | Price: ~£49 | PSU: **24V / ~3.9A**
- Beaming 3,260 Hz — 2,800 Hz crossover comfortably below limit.
- **Best for:** Smallest mid footprint (OD 92 mm) → narrowest baffle, tightest centre spacing. 90 mm at 2,800 Hz = excellent lobing geometry. Black anodised aluminium cone. Consider raising sub/mid crossover to 165 Hz (Fs 66.6 Hz → 2.48×).

---

**A4 · DS115-8 + DX25TG59-04**
- Xover: 1,800–2,500 Hz | Spacing: 110 mm | Price: ~£60 | PSU: **24V / ~3.8A**
- **Best for:** Paper warmth + most flexible crossover point of any standard-dome tweeter (Fs 590 Hz → min 1,180 Hz). If EQ tuning suggests moving the crossover, this pair accommodates it without new hardware. DX25TG59-04's ferrofluid cooling gives thermal safety margin.

---

**A5 · SB12PFCR25-4 + DX25TG59-04**
- Xover: 1,800–2,700 Hz | Spacing: 110 mm | Price: ~£51 | PSU: **24V / ~3.8A**
- Same concept as A4: natural fibre warmth + flexible crossover. Better stock and lower price than A4. Choose this if DS115-8 sells out.

---

**A6 · Beyma 4FR40 + SB19ST**
- Xover: 2,500 Hz | Spacing: 103 mm | Price: ~£45 | PSU: **24V / ~3.8A**
- **Best for:** Paper + Santoprene surround = warm, punchy character. Beyma build quality. Full-range design extends cleanly above 2,500 Hz crossover.
- **Note:** Fs not explicitly published; likely ~80–100 Hz. If Fs is 100 Hz, 150 Hz crossover = 1.5× — marginal. Confirm Fs from datasheet before ordering.

---

**A7 · SPM-116/8 + SB19ST**
- Xover: 2,500 Hz | Spacing: 102 mm | Price: ~£37 | PSU: **24V / ~3.7A**
- **Best for:** Cheapest paper-cone pairing in the catalogue. Monacor construction.
- **Note:** Fs 75 Hz → 2.0× at 150 Hz — tightest of the paper-cone mids. Consider raising sub/mid crossover to 165 Hz.

---

**A8 · SIG120-4 + SB19ST** ← in stock at Audiophonics FR; ships to UK
- Xover: 2,500 Hz | Spacing: 105 mm | Price: ~£48 | PSU: **24V / ~3.6A**
- Beaming 2,570 Hz — 2,500 Hz crossover is below limit.
- **Best for:** 4Ω load gives excellent amp headroom on the mid channel at 24V. Black single-piece anodised dish. Single order at Audiophonics FR.

---

### Tier B — Good; notable trade-offs

**B1 · TCP115-8 + SB19ST** — warmest character; requires 29V
- Xover: 2,500 Hz | Spacing: 102 mm | Price: ~£31 (drivers) + ~£25 (PSU) | PSU: **29V / ~4A required**
- Fs: 59.2 Hz → 2.53× at 150 Hz. Xmax 4.0 mm. Warmest, punchiest character of any mid evaluated.
- **Trade-off:** Does not work at 24V — requires LRS-200-29 (~£25). Factor into build budget.

---

**B2 · ND91-4 + SB19ST** — compact, high Xmax
- Xover: 2,700 Hz | Spacing: 97 mm | Price: ~£48 | PSU: **29V / ~4A**
- Xmax 4.6 mm — highest of any small mid candidate. 3.5" driver = compact footprint.
- **Note:** Fs unconfirmed (response starts 65 Hz; likely ~70–80 Hz). Confirm from datasheet before ordering.

---

**B3 · HiVi M5N + DX25TG59-04** — 5" driver, exceptional Fs margin
- Xover: 1,200–2,100 Hz | Spacing: ~103 mm | Price: ~£54 | PSU: **24V / ~3.9A**
- Fs 50 Hz → 3.0× at 150 Hz — best Fs margin of any new candidate. 5" driver beams above 2,185 Hz.
- **Why DX25TG59-04 not SB19ST:** SB19ST min xover 1,960 Hz leaves only a 225 Hz window below M5N's beaming limit. DX25TG59-04 opens this to 1,200–2,100 Hz.

---

**B4 · SB13PFC25-8 + DX25TG59-04** — 5" natural fibre, outstanding Fs
- Xover: 1,200–2,080 Hz | Spacing: ~110 mm | Price: ~£53 | PSU: **24V / ~3.9A**
- Fs 45 Hz → 3.33× at 150 Hz — best Fs margin of all drivers. Natural fibre paper cone — warm.
- **Why DX25TG59-04:** Same reason as B3 — SB19ST leaves insufficient window below 2,080 Hz beaming limit.

---

**B5 · DA115-8 + SB19ST** — budget aluminium, near-perfect sensitivity match
- Xover: 2,500 Hz | Spacing: 102 mm | Price: ~£44 | PSU: **24V / ~3.9A**
- Fs 60 Hz → 2.5×. Sensitivity almost identical to sub. Only 3 in stock.
- **Best for:** Near-perfect sensitivity match at lower cost than DSA90-8. Aluminium cone — analytical character.

---

**B6 · DSA90-8 + HiVi TN25** — tightest spacing of any pairing; square tweeter
- Xover: 3,000 Hz | Spacing: **73 mm** | Price: ~£52 | PSU: **24V / ~3.8A**
- TN25: 54×54 mm square faceplate, Fs 1,500 Hz → min xover 3,000 Hz.
- **Best for:** Absolute minimum acoustic centre separation — 73 mm at 3,000 Hz is excellent lobing geometry. Square tweeter face above round mid creates strong visual contrast. TN25 depth 63.5 mm — check enclosure clearance.

---

**B7 · SDS-P830656 + DX25TG59-04** — Xmax 10 mm, truncated frame
- Xover: 1,500–2,000 Hz | Spacing: ~105 mm | Price: ~£54 | PSU: **24V / ~3.8A**
- Xmax 10 mm — highest of any mid. Fs 65 Hz → 2.3×. Truncated 152×134 mm frame (noted). Beams above 2,080 Hz.
- **Best for:** Outstanding mechanical headroom — cannot be over-excursed at any realistic kitchen SPL. 60W RMS power rating.

---

**B8 · SIG150-4 + DX25TG59-04** — large mid, low crossover
- Xover: 1,500–1,990 Hz | Spacing: 128 mm | Price: ~£60 | PSU: **24V / ~3.8A**
- Beams above 1,990 Hz. Frame OD 152 mm — very wide baffle.
- **Best for:** Allows a crossover below 2,000 Hz that no other tweeter (except XT25TG30-04) can match. Best suited when speaker is aimed directly at the listener.
- **Trade-off:** 152 mm OD leaves only 19 mm each side on a 190 mm baffle. Off-axis 40–50° is audibly coloured above 2 kHz.

---

**B9 · SB12PACR25-4-COAX** — point source; SPL ceiling ~94 dB
- Xover (internal): 2,800 Hz | Spacing: **0 mm** | Price: ~£59 | PSU: **24V / ~3.5A**
- **Best for:** True acoustic point source — zero time offset, no lobing at any angle. Coherent imaging at any position. Adequate for background and moderate kitchen SPL. Uses JAB5's fourth amp channel for the built-in tweeter.
- **Trade-off:** Max system SPL limited to ~94 dB @1m — sub must be DSP-limited to match.

---

**B10 · DSA90-8 + ND25FA-4** — minimum round spacing
- Xover: 2,700 Hz | Spacing: **79 mm** | Price: ~£44 | PSU: **24V / ~3.9A**
- ND25FA-4: 66 mm OD — smallest round tweeter faceplate evaluated.
- **Best for:** Absolute minimum centre spacing for an all-round pairing. Best lobing geometry of any round/round pair. Choose when baffle width is tightly constrained.

---

**B11 · DSA90-8 + DT-28N** — compact tweeter, very tight spacing
- Xover: 2,500 Hz | Spacing: **~82 mm** | Price: ~£65 | PSU: **24V / ~3.8A**
- DT-28N: 50 mm cutout, 21 mm depth, ~72 mm OD estimated. Fs 1,200 Hz → min xover 2,400 Hz. 50W rated.
- **Best for:** DT-28N is one of the most compact tweeters in the catalogue. Paired with DSA90-8 (92 mm OD) gives ~82 mm centre spacing. Both 8Ω → 24V adequate for both channels.

---

**B12 · SLS-85S25CP04-04 + DT-28N** — oval mid; non-standard shapes
- Xover: 2,500 Hz | Spacing: **~82 mm** | Price: ~£61 | PSU: **29V / ~4A required**
- SLS: 105×91 mm oval frame, Xmax 10.2 mm, paper cone, Fs 73 Hz → 2.05×.
- **Best for:** SLS's oval frame and DT-28N's small waveguide give a distinctive non-round visual. Xmax 10.2 mm = outstanding mechanical headroom. Paper cone for warm character.
- **Trade-off:** Requires 29V PSU (LRS-200-29 ~£25).

---

### Ring Radiator Pairings

Ring radiators produce inherently wide, controlled dispersion through their annular diaphragm — directly benefiting the 60° off-axis kitchen position.

**RR1 · DS115-8 + XT25TG30-04** — paper warmth + widest crossover window
- Xover: 880–2,636 Hz (any point in this range) | Spacing: 113 mm | Price: ~£62 | PSU: **24V / ~3.8A**
- **Best for:** Paper warmth + ring radiator off-axis dispersion + widest crossover tuning window of any pairing.

---

**RR2 · SB12PFCR25-4 + XT25TG30-04** — natural fibre + ring radiator
- Xover: 880–2,730 Hz | Spacing: 116 mm | Price: ~£52 | PSU: **24V / ~3.8A**
- Same concept as RR1 at lower cost. Natural fibre warmth + ring radiator dispersion. 10+ stock mid.
- **Best value ring radiator pairing.**

---

**RR3 · SB12MNRX2-25-4 + XT25TG30-04** — ring radiator + max headroom
- Xover: 880–2,730 Hz | Spacing: 116 mm | Price: ~£83 | PSU: **24V / ~4A**
- **Best for:** Engineering-first ring radiator build. Natural fibre + ring radiator off-axis advantage.

---

**RR4 · DSA90-8 + XT25SC90-04** — budget UK ring radiator; single Falcon order
- Xover: 2,800 Hz | Spacing: 91 mm | Price: ~£37 | PSU: **24V / ~3.8A**
- **Best for:** Cheapest ring radiator pairing. Both drivers at Falcon Acoustics UK — single order, no import. Compact 91 mm spacing.

---

**RR5 · SIG150-4 + XT25TG30-04** — only tweeter that works with SIG150-4
- Xover: 1,000–1,990 Hz | Spacing: 140 mm | Price: ~£67 | PSU: **24V / ~3.9A**
- SB19ST min xover 1,960 Hz leaves only 30 Hz margin below SIG150-4's 1,990 Hz beaming limit. XT25TG30-04 (min 880 Hz) gives the full 1,000–1,990 Hz range.
- **Trade-off:** SIG150-4 OD 152 mm requires very wide baffle. Off-axis 40–50° is coloured above 2 kHz.

---

**RR6 · DS115-8 + SB29SDAC-C000-4** — ring dome + paper warmth
- Xover: 1,200–2,636 Hz | Spacing: ~110 mm | Price: ~£71 | PSU: **24V / ~3.8A**
- **Best for:** Paper cone warmth + SB29 ring dome construction. SDAC's stabilising ring reduces distortion at the crossover region. 1,400 Hz of crossover tuning flexibility.

---

### Tier C — Weaker specs; consider only if priorities demand

**C1 · RS100-8 + SB19ST** — Fs margin too tight
- ~£60. Fs 92 Hz → 1.63× at 150 Hz — tightest Fs margin of any mid.

**C2 · PA130-8 + SB19ST** — Xmax 2 mm, marginal Fs
- ~£47. Xmax 2 mm + Fs 1.8× at 150 Hz + OD 132 mm = three weaknesses.

**C3 · Celestion TF0510 + SB19ST** — weakest Fs and Xmax
- ~£45. Fs 106 Hz (1.42× at 150 Hz). Xmax 1.1 mm. Paper-Kevlar character is interesting but specs are weakest of the field.

**C4 · DSA90-8 + Markaudio TW 6** — crossover above beaming limit
- ~£69. TW 6 Fs 1,700 Hz → min xover 3,400 Hz. DSA90-8 beams at 3,260 Hz — required crossover sits above the mid's beaming limit. Off-axis 40–50° shows a mid-frequency dip. Only consider if speaker is aimed directly at the listener.

---

## Supplier Notes (June 2026)

- **SoundImports** (EU) — primary source for most drivers
- **Falcon Acoustics** (UK) — SB19ST £14.30, XT25TG30-04 £29.90, XT25SC90-04 £18.20, DX25TG59-04 £20.85
- **Audiophonics** (France) — SIG120-4 in stock, ships to UK
