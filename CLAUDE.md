# Kitchen Counter Monitor — AI Assistant Instructions

Project and file structure, requirements, evaluation policy, and fixed system constants are all in **REQUIREMENTS.md**. This file contains only operational rules for the AI assistant.

---

## HARD RULE — Verified Facts Only (read this first; overrides everything below)

Every fact, number, spec, ranking, opinion, and recommendation — in files **and** in chat — MUST be backed by a source you have actually read this session: a datasheet, a published measurement, or a manufacturer/dealer page. Substantiate every claim with the source inline.

- **NEVER present an AI guess, assumption, inference, or "typically / usually / should be" claim as fact.** A plausible-sounding inference is not a fact. If it isn't measured or sourced, it is not true yet.
- **If something is not verified, say so explicitly** ("not verified", "unknown — needs datasheet") and do NOT build a recommendation, ranking, or design decision on it. Stop and fetch the source, or flag the gap to the owner and wait.
- **Never silently fill a gap.** "I don't know / not yet verified" is the correct answer when you don't have the source. It is always better than a confident guess.
- **Derived numbers** (power, beaming, crossover, volume) must show the formula AND the sourced input values they were computed from.
- **Clearly separate** sourced fact from anything provisional. No unlabelled provisional content anywhere.
- This rule overrides speed, convenience, and the urge to be helpful or decisive.

**Why this exists:** an earlier unverified "ring radiator off-axis advantage" — a pure AI hallucination — led the owner to buy £160 of unusable tweeters. Unverified assumptions have a real, expensive cost. This must never happen again.

---

## Autonomous Operation

Only work fully autonomously when the owner has explicitly instructed you to do so in the current session. In normal operation, ask for clarification or confirmation when needed.

When operating autonomously: make decisions independently, record choices in commit messages, and push to GitHub at least every 10 minutes. **NEVER run git commands in the background; always set WaitMsBeforeAsync to its maximum value (10000ms) to run git commands synchronously in the foreground.**

---

## Persistent Memory

Project notes are stored in `memory/` inside this repository. Read `memory/MEMORY.md` at the start of each session to get context. Write new memories to `memory/` as markdown files and add a pointer to `memory/MEMORY.md`. Keep memory files current — update rather than append when facts change.

---

## Write Analysis to Files

The owner cannot track console output across sessions. Write all findings to the appropriate file. File roles and placement rules are defined in REQUIREMENTS.md — read that section before writing to any file.

**Quick routing:**
- Raw scraped specs → `research/`
- Fact about one driver (power needed, DSP correction, crossover margin, PSU minimum) → `drivers.md`
- Fact about two drivers paired together (combo crossover, centre spacing, combo PSU) → `combos.md`
- Recommendation for a scenario → `solutions.html`
- Amp/PSU/DSP electronics → `amp.md`
- Supplier info → `suppliers.md`
- Calculations and formatting automation scripts → `scripts/`
- Scraping pipeline (URL list, download cache, extractor) → see `scripts/SCRIPTS.md`

**Never put per-driver data in combos.md.** If a fact is true regardless of which driver the mid or tweeter is paired with, it belongs in drivers.md.

When performing a supplier stock check, record findings in the relevant driver entry in drivers.md (stock and date) and update combos.md/solutions.html if a previously available driver is now out of stock.

---

## Tweeter Off-Axis Gate — Mandatory Before Any Recommendation

Before writing any tweeter recommendation to any file, AND before describing any tweeter as a "good candidate", "promising", or using any positive language about its off-axis performance in chat:

1. **Read the actual 60° off-axis curve in the datasheet** — open the local PDF, find the FR plot showing the 60° curve, and state the measured dB difference between on-axis and 60° at 13 kHz. If no local PDF exists, fetch it before proceeding.
2. **Calculate beaming frequency** from Sd: D = 2√(Sd/π), f_beam = 344 / (π × D/2). This is context only — it does NOT establish suitability. A low beaming frequency predicts poor off-axis, but a high beaming frequency does NOT confirm good off-axis. Only measured data does.
3. **Check measured polar data** if available — RAW-CAt Ultimate Tweeter Shootout Part 6 (Nov 2025) has measured 30° data for 40+ tweeters. Note: RAW-CAt measures at 30° only, not 60°. A good 30° score does not imply good 60° performance.

**The gate blocks any positive statement about a tweeter's off-axis performance until step 1 is complete and the dB figure at 13 kHz / 60° is recorded.** Theoretical calculations alone never satisfy this gate. No exceptions.

---

## Source URL Requirements

Every specification quoted in project files must have a traceable source:
1. **Manufacturer datasheet PDF** — download to `research/` and link the local path AND original URL. SoundImports product pages attach datasheets at `doc.soundimports.nl/pdf/...` — always fetch these as they contain full T/S parameters the product page omits.
2. **Manufacturer product page**
3. **SoundImports product page**
4. **Parts Express, loudspeakerdatabase.com, or other reputable dealer**

Never quote a specification without noting where it came from.

Never record a spec without checking it's actually real and not a hallucination.

---

## Working with the Owner

- **The owner has a strong technical grasp** — comfortable with T/S parameters, crossover math, power calculations, and PSU design. Go straight to the numbers; no need to explain fundamentals.

- **The owner enjoys the engineering process.** When there's a choice between a pragmatic fix and an equally realistic but more interesting solution, surface BOTH. A custom capacitor bank is more satisfying than "just buy a bigger PSU". Always present the creative angle alongside the practical one.

- **Be substantive — real numbers, real calculations.** Vague suggestions are not enough. Give specific, actionable options with component values and cost estimates.

- **Power budget must always cover both RMS and burst.** The sub's 80W max defines the burst ceiling. Always derive amplifier power from actual supply voltage using P = V²/(2R) × 0.85, not the board's rated power.
