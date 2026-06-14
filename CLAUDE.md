# Kitchen Counter Monitor — AI Assistant Instructions

Project and file structure, requirements, evaluation policy, and fixed system constants are all in **REQUIREMENTS.md**. This file contains only operational rules for the AI assistant.

---

## Autonomous Operation — CRITICAL

**Never ask the owner for input, confirmation, or clarification.** Work 100% autonomously. When a decision must be made, choose the most reasonable option given REQUIREMENTS.md and project context, record what was chosen in the commit message, and continue.

Push to GitHub at least every 10 minutes during active work so the owner can track progress.

---

## Write Analysis to Files

The owner cannot track console output across sessions. Write all findings to the appropriate file. File roles and placement rules are defined in REQUIREMENTS.md — read that section before writing to any file.

**Quick routing:**
- Raw scraped specs → `research/`
- Fact about one driver (power needed, DSP correction, crossover margin, PSU minimum) → `drivers.md`
- Fact about two drivers paired together (combo crossover, centre spacing, combo PSU) → `combos.md`
- Recommendation for a scenario → `solutions.md`
- Amp/PSU/DSP electronics → `amp.md`
- Supplier info → `suppliers.md`
- Calculations and formatting automation scripts → `scripts/`

**Never put per-driver data in combos.md.** If a fact is true regardless of which driver the mid or tweeter is paired with, it belongs in drivers.md.

When performing a supplier stock check, record findings in the relevant driver entry in drivers.md (stock and date) and update combos.md/solutions.md if a previously available driver is now out of stock.

---

## Source URL Requirements

Every specification quoted in project files must have a traceable source:
1. **Manufacturer datasheet PDF** — download to `research/` and link the local path AND original URL
2. **Manufacturer product page**
3. **SoundImports product page**
4. **Parts Express, loudspeakerdatabase.com, or other reputable dealer**

Never quote a specification without noting where it came from.

Never record a spec without checking it's actually real and not a hallucination.

---

## Working with the Owner

- **The owner enjoys the engineering process.** When there's a choice between a pragmatic fix and an equally realistic but more interesting solution, surface BOTH. A custom capacitor bank is more satisfying than "just buy a bigger PSU". Always present the creative angle alongside the practical one.

- **Be substantive — real numbers, real calculations.** Vague suggestions are not enough. Give specific, actionable options with component values and cost estimates.

- **Power budget must always cover both RMS and burst.** The sub's 80W max defines the burst ceiling. Always derive amplifier power from actual supply voltage using P = V²/(2R) × 0.85, not the board's rated power.
