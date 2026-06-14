Resume engineering for "Kitchen Counter Monitor" — paste-ready AI prompt
---------------------------------------------------------------

Resume engineering for "Kitchen Counter Monitor" Option C: deliver a finalized `Option C` design (side-firing low-profile monitor) that meets these measurable goals: 98 dB SPL peak at 6 ft, stable tonal balance across 60° horizontal sweep, and native sub extension to 38 Hz. Fixed decisions: tweeter SB19ST-C000-4, sub Tang Band W5-1138SMF, PR SB15SFCR racetrack, Mean Well LRS-150-24 PSU, target sealed mid chamber 1.5 L and sub chamber 7.5 L. Open decision: midrange — compare Dayton DSA90-8 vs TCP115-8 and recommend with quantitative trade-offs (sensitivity, required amp power, baffle interaction, DSP gain).


Constraints and decisions extracted from `desktop-idea.md` (include these in all resumed sessions):

- Visual constraint: all front-facing plates, driver plates, and routing cuts must be 100% circular (no rectangular/truncated frames); all drivers are surface-mounted.
- Driver selections (locked):
  - Tweeter: SB Acoustics SB19ST-C000-4 (19 mm textile dome, 88 mm round faceplate).
  - Subwoofer: Tang Band W5-1138SMF (5.25", heavy round frame, 9.25 mm Xmax).
  - Passive radiator: SB Acoustics SB15SFCR-00 5x8" racetrack (mounted vertically on rear centerline); additional mass required to achieve 38 Hz.
- Midrange candidates: Dayton DSA90-8 (3" aluminium, 92.3 mm circular frame) and Dayton TCP115-8 (4" treated paper, 116 mm circular frame). DSA90-8 = higher sensitivity (~84.7 dB); TCP115-8 = warmer low-mids, lower sensitivity (~81.9 dB).
- Enclosure target net volumes (sealed): Midrange chamber 1.5 L net; Subwoofer chamber 7.5 L net. Enclosure materials: 12 mm moisture-resistant MDF exterior, 9 mm plywood internal partition for midrange.
- Option C mechanical layout (accepted): Side-firing low-profile desktop monitor with external dimensions 26.5 cm H × 19.0 cm W × 25.2 cm D. Tweeter center 4.0 cm down, mid center 11.0 cm down (or 11.5 cm for larger mid), sub and PR mounted on opposite side panels centered vertically to cancel forces.
- Electronics & DSP (specified): Mean Well LRS-150-24 (24 V, 6.5 A), JAB5 amp with ADAU1701 DSP, crossover targets: LP @120 Hz, mid band 120–2800 Hz, HP @2800 Hz for tweeter, Linkwitz-Riley 24 dB/oct for LP and BP, 48 dB/oct HP for tweeter; tweeter digital pad -9.5 dB before DAC 2.
- Power/headroom note: Calculated peak electrical draw ~164.8 W DC; projected peak acoustic output ~98.4 dB SPL at 6 ft when drivers driven to physical limits.
- Mechanical notes: Surface-mounted sub surround sits proud of baffle (~8.5 mm), reclaiming ~160 mL internal volume; account for driver displacements and protrusions in final net volumes.
- Manufacturing notes: Base isolates PSU and electronics into a sealed drawer; verify ventilation or relocate PSU if thermal limits exceeded.
- Optional modes: Option A (wired master-slave with umbilical), Option B (wireless single-board active TWS) — wireless adds latency and sync complexity; prefer wired for deterministic performance unless user requires wireless.

- Passive radiator SB15SFCR: Sd ≈ 178 cm² (~2.05× active driver displacement); mount vertical on rear centerline and add mass to the rear M6-threaded bolt assembly to lower native tuning to 38 Hz.
- Tang Band sub surround sits ~8.5 mm proud of the baffle, reclaiming ≈160 mL — include this in final net-volume math.
- volume calcs should take account of the fact the speakers are surface mounted and thereofre the thickness of the walls may subtract from the overal depth of the driver

---
End of prompt.
