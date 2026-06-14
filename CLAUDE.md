# Kitchen Counter Monitor — Project Instructions

This is a DIY active 3-way desktop speaker project. The subwoofer (Tang Band W5-1138SMF) is locked. Tweeter and midrange are under evaluation.

## File Structure

### REQUIREMENTS.md
The authoritative record of explicitly stated owner requirements. Only add content the owner has directly stated — no inferred or derived content.

### goals.md
Superseded. Now points to REQUIREMENTS.md. Content archived in OLD_IGNORE_ME.md.

### OLD_IGNORE_ME.md
Archive of superseded content. **DO NOT USE unless the owner explicitly instructs it.**

### drivers.md
A catalogue of every individual driver that has been evaluated. One entry per driver. Each entry records: key specifications, what is liked, what is disliked, and ranking/status.

- Do not duplicate driver data across other files — always refer back to this file.
- When a new driver is found or evaluated, add or update its entry here.
- Every entry must include a source URL — manufacturer datasheet (PDF preferred), then manufacturer product page, then SoundImports/Parts Express/loudspeakerdatabase.

### potential-solutions.md
Paired mid + tweeter combinations evaluated against the locked subwoofer (Tang Band W5-1138SMF). Each entry describes how the pair works together as a system, with explicit pros and cons relative to the project goals.

- One section per combination.
- Always reference drivers by the model names recorded in drivers.md.
- Include stock availability and pricing at time of evaluation (with date).
- Update when stock status changes.

### suppliers.md
List of all suppliers checked with notes on UK shipping, range, and findings.

### amp.md
Amplifier and electronics specifications.

### research/
Folder for downloaded PDFs, datasheets, and saved HTML for offline reference.

### CLAUDE.md (this file)
Project-level instructions for the AI assistant. Explains conventions and where to write things.

---

## Autonomous Operation — CRITICAL

**Never ask the owner for input, confirmation, or clarification.** Work 100% autonomously. When a decision must be made, choose the most reasonable option given REQUIREMENTS.md and project context, record what was chosen in the commit message, and continue.

Push to GitHub at least every 10 minutes during active work so the owner can track progress.

---

## Working Conventions

- **Write analysis and findings to files, not to the console.** The user cannot track console output across sessions.
- When performing a supplier stock check, record findings in potential-solutions.md with the date.
- Keep goals.md, drivers.md, and potential-solutions.md in sync with the current state of the design.
- The subwoofer (Tang Band W5-1138SMF) is the fixed reference point. All mid and tweeter evaluations are judged relative to it.

---

## Source URL Requirements

Every specification quoted anywhere in the project files must have a traceable source. Apply this hierarchy:
1. **Manufacturer datasheet PDF** — download to research/ and link the local path AND the original URL
2. **Manufacturer product page**
3. **SoundImports product page** (reliable, consistent spec format)
4. **Parts Express, loudspeakerdatabase.com, or other reputable dealer**

Never quote a specification without noting where it came from.

---

## Driver Evaluation Policy — No Visual Exclusions (updated June 2026)

**Visual constraints have been removed by owner instruction (June 2026).** Do not exclude any driver based on cone colour, frame shape, dome material colour, phase plug colour, or any other visual attribute. Record the appearance as a note and move on.

The only automatic exclusions now are:
- **Drivers designed exclusively for rear mounting** with no provision for front mounting (visible gaskets for flush-seal against baffle, large magnet/motor protrusions that cannot be surface-mounted cleanly)
- **Drivers with ratings that make them technically unusable** in this system (e.g., power handling far below what the amp delivers at matched SPL)

### Evaluation criteria (in order):
1. **Acoustic fit** — Fs margin, Xmax, sensitivity match to sub
2. **Engineering compatibility** — power rating, DSP correction, amp headroom
3. **Practical fit** — frame OD vs baffle width, depth vs enclosure clearance, stock availability

Appearance notes (frame shape, cone colour, phase plug material) are recorded for reference but do not exclude a driver from consideration.

---

## Passive Radiator Configurations

Two valid layouts are being considered; keep both open:

- **Option A (side-mount sub):** Sub on left side panel, single racetrack PR (SB15SFCR or similar) on right side panel. Front baffle has tweeter + mid only.
- **Option B (front-mount sub):** Sub on front baffle below mid. PR(s) on rear or sides. All visible drivers in a vertical column on front.
- **Option C (dual round PR, sides):** Sub on front baffle, two matched round PRs (e.g., ND140-PR) one on each side. Aesthetically consistent with circular driver theme. Requires total PR Sd ≥ sub Sd×Xmax ratio.

The choice of sub placement affects baffle width requirements — record this when evaluating mid driver frame sizes.

---

## Working with the Owner

- **The owner enjoys the engineering process as much as the end product.** When there's a choice between a pragmatic fix and an equally realistic but more interesting solution, surface the interesting one. A custom capacitor bank is more satisfying than "just buy a bigger PSU". A dual-supply voltage design is more interesting than a single-rail one. Always present the creative angle alongside the practical one.

- **When giving options, be substantive — real numbers, real voltages, real calculations.** Vague suggestions like "consider a better PSU" are not enough. Give 3–5 specific, actionable options with component values and cost estimates.

- **Power budget analysis must always cover both:**
  1. **RMS continuous power** — can the amp sustain the matched reference SPL indefinitely?
  2. **Burst/transient headroom** — can the amp match the sub's peak SPL when the sub is at its rated maximum (80W)? Transients 10–20 dB above average are normal music content.
  
  Present both figures for every amp/driver combination. The sub's 80W max defines the burst ceiling.

- **Always derive amplifier power from actual supply voltage, not the board's rated power.** The JAB5 is rated 100W into 6Ω at ~37–38V. At 24V into 8Ω it delivers ~31W. Formula: P = V² / (2R) × η (class D full H-bridge, η ≈ 0.85).

- **Driver evaluation priority order:** (1) Acoustic fit — Fs margin, Xmax, sensitivity match to sub. (2) Engineering compatibility — power rating, DSP correction, amp headroom. (3) Practical fit — frame OD, depth, stock. Visual attributes are notes only, not evaluation criteria.

- **Power rating — the only question that matters:** Can the driver handle the power the amp actually delivers to it when all three are playing at matched SPL? The DSP sets the level balance; high-sensitivity drivers get a big pad and receive very little power. Evaluate power in terms of what reaches the driver, not an absolute minimum rating. A high-sensitivity tweeter rated 15W that only receives 6W is fine. A lower-sensitivity driver that receives 40W needs a 40W+ rating.

- **Write all analysis to files.** The owner cannot track console output across sessions. Findings go to the appropriate file (potential-solutions.md for pairings, drivers.md for individual driver facts, amp.md for electronics analysis). Summarise the key findings in the reply but the full working belongs in the file.
