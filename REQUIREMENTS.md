# Kitchen Counter Monitor — Explicit Requirements

This file records requirements explicitly stated by the owner, plus fixed system constants, file structure conventions, and evaluation policy. It is the authoritative reference for all decisions about what to build and how to evaluate options.

---

## Project File Structure

Each file has a single responsibility. Do not write content into the wrong file.

| File | Role | What does NOT go here |
|------|------|----------------------|
| `REQUIREMENTS.md` | Owner requirements, fixed constants, evaluation policy, file structure. | Analysis, opinions, rankings |
| `research/si_tweeter_index.md` | Raw tweeter specs from SoundImports — scraped data only. | Any derived figures or analysis |
| `research/si_woofer_index.md` | Raw woofer/mid specs from SoundImports — scraped data only. | Any derived figures or analysis |
| `research/*.pdf` | Downloaded datasheets for offline reference. | — |
| `drivers.md` | Per-driver analysis: DSP correction, power check vs sub reference SPL, crossover margin, ranking, decisions, why liked/disliked, minimum PSU voltage. No raw spec duplication — refer to research/ for raw specs. | Anything that doesn't change based on which driver you pick |
| `combos.md` | Exhaustive spreadsheet of mid+tweeter pairings. Records only combo-specific data: crossover window, centre spacing, PSU voltage for the combination, visual notes on the pair together, ruling and reason, combo trade-offs. | Per-driver data (power needed, sensitivity, Fs etc.) — those belong in drivers.md even when displayed in a combo context |
| `solutions.md` | Curated final report. Small number of recommended pairings per scenario (off-axis, on-axis, compact, budget, visual). Justified and actionable. | Exhaustive lists, marginal options, runner-ups beyond 5th place |
| `amp.md` | JAB5 specs, PSU specs and options, DSP crossover and loudness configuration. | Per-driver analysis, driver names, model-specific recommendations |
| `suppliers.md` | Supplier list with notes on UK shipping, range, and findings. | Driver evaluations |
| `CLAUDE.md` | Narrow operational instructions for the AI assistant only. | Requirements, evaluation criteria, project context |

### No data duplication

Each fact is recorded in exactly one place. Do not summarise or re-list data that already exists in another file — reference it instead.

- **combos.md** is a single table (one row per pairing). There is no separate "detailed entries" section that repeats the same pairings in prose form.
- **drivers.md** is the source of truth for per-driver specs. combos.md never repeats sensitivity, Fs, Xmax, or any other per-driver figure — it records only what changes per combination.
- **solutions.md** references pairings by ID (e.g., RR2, S1) — it does not duplicate the spec data from combos.md or drivers.md.

### File placement test — ask before writing

Before writing any analysis, run through this test:
- **Is this fact true for a single driver regardless of what it's paired with?** → `drivers.md`
- **Is this fact only true when two specific drivers are paired together?** → `combos.md`
- **Is this a recommendation for a specific use case?** → `solutions.md`
- **Is this about the amplifier or PSU electronics?** → `amp.md`
- **Is this a raw spec scraped from a product page?** → `research/`

Examples of correct placement:
- "DS115-8 needs 18.6W to reach 98 dB" → **drivers.md** (true regardless of what tweeter pairs with it)
- "S1 crossover is 2,500 Hz" → **combos.md** (combo-specific)
- "RR2 is the best pick for 60° off-axis" → **solutions.md** (recommendation)
- "JAB5 delivers 31W into 8Ω at 24V" → **amp.md** (amp spec)

---

## Fixed System Constants

These components are locked. They define the engineering envelope for all other evaluations.

### Subwoofer — Tang Band W5-1138SMF (LOCKED)

| Parameter | Value |
|-----------|-------|
| Frame OD | 133.3 mm |
| Impedance | 4Ω |
| Sensitivity | **85 dB @ 2.83V/1m** |
| Power | 40W RMS / 80W peak |
| Fs | 45 Hz |
| Xmax | 9.25 mm |
| Qts | 0.49 |
| Sd | 94 cm² |
| Vas | 4.81 L |

**System SPL reference:**
- Sub at 40W RMS → **98 dB @ 1m** (continuous)
- Sub at 80W peak → **101 dB @ 1m** (burst ceiling)

Source: [SoundImports](https://www.soundimports.eu/en/tang-band-w5-1138smf.html) | Datasheet: [research/tang_band_w5-1138smf.pdf](research/tang_band_w5-1138smf.pdf)

---

### Passive Radiator — SB Acoustics SB15SFCR-00 5×8" Racetrack (LOCKED)

| Parameter | Value |
|-----------|-------|
| Shape | Oval racetrack |
| Sd | ≈ 178 cm² (~1.89× sub Sd) |
| Tuning method | Added mass to rear M6 bolt to reach 38 Hz target |
| Mounting | Side or rear panel only |

The racetrack shape eliminates Option C (dual round PRs). The active layout is Option A (sub on side panel, PR on opposite side) or Option B (sub on front baffle, PR on side or rear panel).

Source: [SoundImports](https://www.soundimports.eu/en/sb-acoustics-sb15sfcr-00.html)

---

### Amplifier — Sure Electronics JAB5 (AA-AB32184) (LOCKED)

| Parameter | Value |
|-----------|-------|
| Channels | 4 (3 used: sub / mid / tweeter; 1 spare) |
| Rated power | 4 × 100W @ 6Ω at ~36V supply |
| Supply voltage range | 10–39V DC |
| DSP | ADAU1701 (Analog Devices) — programmed in SigmaStudio |
| Bluetooth | BT5.0, aptX HD |
| THD | 0.07% (rated) |
| Idle current | ~0.5A |

**Available power per channel (Class D H-bridge: P = V²/2R × 0.85):**

| PSU voltage | 4Ω (sub, tweeter) | 8Ω (mid) | 6Ω |
|-------------|-------------------|-----------|-----|
| 24V | ~61W | ~31W | ~41W |
| 29V | ~89W | ~45W | ~60W |
| 36V | ~138W | ~69W | ~92W |

The official datasheet specifies only 100W/ch at 36V into 6Ω. All other figures are derived from the formula above.

> **Warning:** At 29V and above, the 4Ω channels (sub and tweeter) can deliver more than the sub's 80W maximum and far more than most tweeter power ratings. DSP channel-level limiters are mandatory at any supply voltage above 24V.

Datasheet: [research/jab5_datasheet.pdf](research/jab5_datasheet.pdf)

---

### Enclosure

| Dimension | Target |
|-----------|--------|
| Width | ~190 mm (baffle) |
| Depth | ~130–140 mm (Google Home Max reference) |
| Height | Up to GHM height + ~5 cm (~270 mm maximum) |
| Electronics vault (base) | 26 mm height allocated for PSU and wiring |

- All drivers surface-mounted proud of the baffle — no flush-recessing
- Layout: Option A or Option B (see Passive Radiator above — racetrack shape constrains this)
- No wiring or connectors visible on front or top face

---

## Listening Context

- Kitchen counter placement, 5–6 feet from listener
- Listener frequently at 60° off-axis (at the cooker)
- Use spans quiet background listening to full volume (party, classical)

---

## Frequency Response

- Flat, natural response from the low 30s Hz upward
- 38 Hz native tuning via passive radiator — no digital bass boost to reach this target

---

## DSP / Loudness

- GHM-style loudness compensation: gentle bass shelf boost at low volumes, flattening as volume rises

---

## Power — SPL Balance Across All Three Drivers

The subwoofer defines the SPL ceiling. The mid and tweeter must match it at every volume level — not just at moderate levels, but at full rated sub output (40W RMS) and at transient bursts (80W peak).

### Reference levels

| Condition | Sub power | SPL @ 1m |
|-----------|-----------|-----------|
| RMS continuous | 40W into 4Ω | **98 dB** |
| Burst / transient | 80W into 4Ω | **101 dB** |

### How to calculate required driver power

```
P_needed = (2.83² / R_driver) × 10^((SPL_target − sensitivity_dB) / 10)
```

Where `SPL_target` is 98 dB (RMS) or 101 dB (burst), and `sensitivity_dB` is the driver's 2.83V/1m rating.

After DSP level correction brings all three channels to matched SPL:
- The power delivered to each driver must remain within its continuous rating
- A DSP channel limiter is the safety margin for burst peaks above the driver's rating

### PSU specification per pairing

Every recommended pairing must state the minimum PSU and the current draw at both reference levels:

| Quantity | How to calculate |
|----------|-----------------|
| PSU voltage | Minimum V where amp delivers P_needed at that impedance |
| RMS current | (P_sub + P_mid + P_tweet) / V_supply + 0.5A idle |
| Burst current | (P_sub_burst + P_mid + P_tweet) / V_supply + 0.5A idle |

The Mean Well LRS-150-24 supplies 6.5A / 156W at 24V. At standard 24V combos with an 8Ω mid, RMS current is ~3.5–4A and burst approaches 5–6A — within spec for music content, but a capacitor bank (see amp.md) absorbs transient peaks cleanly.

---

## Off-Axis Stability

- Tonal balance must remain stable across the full 60° horizontal sweep
- Tweeter dome ≤19 mm preferred (wider HF dispersion above crossover)
- Mild toe-in (10–15°) is possible but the design must not depend on it

---

## Crossover — Integration and Listening Quality

- All three drivers must sum flat and in-phase at the crossover points — no audible suck-outs or brightness peaks at the transitions
- Crossover targets: sub LP 150 Hz (LR24) · mid BP 150–2,800 Hz · tweeter HP 2,800 Hz (LR48)
- Per-pairing crossover must be checked: the mid's beaming frequency sets the upper limit; the tweeter's Fs (×2) sets the lower limit — these must not conflict
- Both crossover points should be well away from driver resonances — Fs margin of ≥2× is the minimum for the sub/mid crossover; ≥2× for the mid/tweeter crossover
- The goal is a system that sounds seamless: no listener awareness of individual drivers, natural and uncoloured across the full range at any volume level

---

## Driver Evaluation Policy

### No Visual Exclusions

Visual constraints removed by owner instruction (June 2026). Do not exclude any driver based on cone colour, frame shape, dome material colour, phase plug colour, or any other visual attribute. Record appearance as a note and move on.

Automatic exclusions only for:
- Drivers designed exclusively for rear mounting with no provision for front mounting
- Drivers with ratings that make them technically unusable (e.g., power handling far below what the amp delivers at matched SPL)

### Evaluation criteria (in order)

1. **Acoustic fit** — Fs margin above sub/mid crossover (≥2×), Xmax, sensitivity match to sub
2. **Engineering compatibility** — power rating vs power delivered after DSP correction, PSU voltage requirement
3. **Practical fit** — frame OD vs baffle width, depth vs enclosure clearance, stock availability

Appearance notes are recorded in drivers.md but do not affect ranking.

### Power rating check

The only question that matters: can the driver handle the power the amp actually delivers to it when all three are playing at matched SPL? The DSP sets the level balance; high-sensitivity drivers get a large pad and receive very little power.

- Evaluate power in terms of what reaches the driver, not an absolute minimum rating
- A high-sensitivity tweeter rated 15W that only receives 6W is fine
- A lower-sensitivity driver that receives 40W needs a 40W+ rating

---

## Recommendations by Scenario

Recommendations must cover best pairings for the scenarios defined in this file, including (at minimum):
- Best for visual interest
  - by shape class — round, square/non-round, mixed
- Best overall for kitchen 60° off-axis listening
- Best for on-axis listening (direct, centred)
- Best for compact baffle / minimum width
- Best value (under £50 and under £100 tiers)

---

## Recommendation Tables

Minimum required columns in every recommendation table:

| Column | Notes |
|--------|-------|
| ID | Reference code |
| Mid | Driver model |
| Tweeter | Driver model |
| Crossover | Frequency or range |
| Price | Combined £ estimate |
| PSU | Voltage and RMS current, e.g. "24V / 4A" |
| Character | Tonal signature (warm / detailed / neutral etc.) |
| Why | Key reason for inclusion or rank |

Additional columns permitted only where the value has direct and significant bearing on a decision. Centre spacing is one example — include it only when notably tight or wide enough to affect performance or baffle design. Do not add columns for their own sake.

---

## Physical

- All drivers surface-mounted — proud of the baffle, not flush-recessed
- No wiring or connectors visible on front or top face
- Compact — Google Home Max footprint is the size reference; up to ~5 cm taller is acceptable
- Classic look — I like B&W DM4 and similar wooden speaker designs, but I also like the idea of an ultra compact speaker with great bass and lovely mids and highs
