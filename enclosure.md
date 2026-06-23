# Enclosure Design — W5-1138SMF + SB15SFCR-00 PR + SB12MNRX2-25-4 + SB19ST-C000-4

> **⚠ UPDATED June 2026 — design in transition.** Driver set changed: mid **DS115-8 → SB12MNRX2-25-4**, tweeter **R2604/833000 → SB19ST-C000-4** (see drivers.md "SELECTED SYSTEM"). Cabinet changed to **220 × 180 × 360 mm single section, side-firing sub + PR, rear electronics pocket** (visualised in `enclosure_3d.html`). The **Drivers**, **Overall Cabinet** and **PR Tuning** sections below are updated. The detailed geometry sections further down (acoustic volume, side-panel positions, mid box, front baffle, cut list) **still reference the OLD design and need re-deriving** for the new drivers/dims — treat them as superseded until revised.

GHM-inspired active 3-way kitchen counter monitor. Side-firing sub (left) and PR (right) keep the front baffle for mid + tweeter; electronics in a sealed rear pocket (no separate base).

---

## Drivers

| Role | Driver | Frame OD mm | Cutout mm | Depth mm | Fires |
|------|--------|----------|-----------|----------|-------|
| Sub | Tang Band W5-1138SMF | 155 | 120 | 81 (from back of flange) | LEFT side |
| PR | SB Acoustics SB15SFCR-00 | 252 × 153 racetrack | 220 × 119 | 49.7 | RIGHT side (portrait) |
| Mid | SB Acoustics **SB12MNRX2-25-4** | 123 | ~102 (confirm) | ~70 (confirm) | Front |
| Tweeter | SB Acoustics **SB19ST-C000-4** | 88 | 60 | 21 | Front |

⚠ Mid changed to SB12MNRX2-25-4 (OD 123 mm vs DS115's 115.6) — its **sealed rear chamber must be resized**: the old 110 mm soil pipe (ID 103.6) only just clears a ~102 mm cutout; verify the MNRX2 basket fits or step up to 125 mm pipe.

---

## Overall Cabinet — 220 × 180 × 360 mm (single section)

```
   ┌──────────────┐  360 mm
   │   ⊙ tweeter   │   SB19ST  (front)
   │   ◎ mid       │   SB12MNRX2 (front)
 sub│              │PR    sub = LEFT side, PR = RIGHT side
 ◎  │              │ ▭    electronics pocket on REAR (upper)
   └──────────────┘  0 mm   (20 mm bottom margin so side cutouts clear)
   220 W × 180 D
```

| Dimension | External mm | Internal mm |
|-----------|-------------|-------------|
| Width | 220 | 196 |
| Depth | 180 | 150 (18 mm front + 12 mm rear) |
| Height | **360** | 336 |

Single unified box — no separate electronics base (JAB5 + PSU sit flat in a sealed rear pocket, ~175 × 127 × 46 mm, with ventilation holes). Sub (left, basket ~63 mm into box) and PR (right, ~38 mm in) clear each other across the 196 mm internal width by ~95 mm. Gross internal ≈ **9.9 L**.

---

## Acoustic Volume

Single acoustic volume — no internal shelves. Sub and PR share the full interior. Mid is isolated by a small sealed inner box (see below).

**Gross internal volume:** 166 × 185 × 246 = **7.54 L**

| Deduction | Volume |
|-----------|--------|
| Soil pipe outer volume (π×55²×70 mm) | −0.67 L |
| Sub basket protrusion | −0.51 L |
| Tweeter body | −0.05 L |
| **Net sub volume** | **~6.33 L** |

6.33 L net is well above the W5-1138SMF's Vas (4.81 L) — correct operating range for a PR-loaded alignment. The soil pipe mid box displaces 0.46 L less than the old MDF box (1.13 L), which is why the net volume increased.

---

## Side Panel Drivers

### Left side — SB15SFCR-00 (passive radiator, portrait)

The racetrack frame (253 × 153 mm) mounts portrait — long axis vertical.

- Centre: **135 mm from acoustic floor** (external measurement)
- Frame long axis (253 mm) in height: 135 ± 126.5 mm → **8.5–261.5 mm** — 8.5 mm margin top and bottom ⚠ tight (see construction note)
- Frame short axis (153 mm) in depth: 215 mm available → 23 mm margin each side ✓
- Cutout 220 × 119 mm — fully within panel face ✓
- Mounting depth 49.7 mm + sub basket 81 mm = 130.7 mm < 166 mm internal width → **35 mm clearance** ✓

**Construction note:** standard **butt joints** throughout (no dado/rabbet — there never was one). ⚠ These side-panel positions are from the OLD 270 mm-tall panel; re-derive for the new 360 mm side panels (the 20 mm bottom margin lets the PR/sub cutouts clear the floor).

### Right side — W5-1138SMF (sub)

Side panel face: 215 mm deep × 270 mm tall.

- Centre: **135 mm from acoustic floor** — symmetric with PR ✓
- OD span: 135 ± 77.5 mm → **57.5–212.5 mm** — fully within 270 mm ✓
- Cutout: 120 mm on 215 mm depth → 47.5 mm margin each side ✓

---

## PR Tuning (SB15SFCR-00)

Specs from drivers.json (SB Acoustics datasheet): Sd = 178 cm², Mms_stock = 62 g, Fs_stock = 21 Hz, Xmax = 11 mm. Mass adjust boss: M6 bolt on rear.

Suspension stiffness:
```
Kms = Mms_stock × (2π × Fs_stock)² = 0.062 × (131.9)² = 1,079 N/m
```

Air spring in 6.0 L net box:
```
Kair = ρ₀c² × Sd² / Vb = 142,356 × (0.0178)² / 0.006 = 7,517 N/m
```

Total (Kms not negligible at Fs = 21 Hz):
```
Fb = (1/2π) × √((Kms + Kair) / Mms_total)
```

**RE-TUNED for the new box.** New cabinet net volume ≈ **7.3 L** (gross 9.9 L minus mid box ~0.7, sub basket ~0.5, PR basket ~0.3, electronics pocket ~1.0, tweeter ~0.05). Larger than the old 6.33 L → softer air spring → **less added mass** for the same Fb.

```
Kms  = 0.062 × (2π×21)²            = 1,078 N/m
Kair = 142,356 × 0.0178² / 0.0073  = 6,180 N/m   (at 7.3 L)
Ktot = 7,258 N/m
Mms_total = Ktot / (2π·Fb)²,  added = Mms_total − 62 g
```

| Target Fb | Mms total | Added mass (new ~7.3 L) |
|-----------|-----------|--------------------------|
| 38 Hz | 127 g | **65 g** |
| **40 Hz** | **115 g** | **~53 g** |
| 42 Hz | 104 g | **42 g** |
| 45 Hz | 91 g | **29 g** |

**Recommendation: 40 Hz tuning (~53 g added)** (was 68 g in the old 6.33 L box). F3 ≈ 38–42 Hz. ⚠ Net volume is estimated — recompute/measure once the final box + mid chamber + electronics pocket are built, and verify by measuring the loaded PR's free-air Fs before gluing.

**Sd ratio:** SB15SFCR-00 178 cm² / W5-1138SMF 94 cm² = **1.89×** — well above the 1.5× minimum; PR displacement per unit sub displacement is comfortably lower than Xmax allows.

---

## Mid Inner Box — sealed rear chamber for SB12MNRX2-25-4 (~1.2 L)

The mid's rear wave must be isolated from the sub/PR chamber. **The MNRX2 needs a bigger chamber than the old DS115 0.59 L pipe** — its Vas is 5.3 L, so a tiny chamber pushes its sealed resonance up into the passband.

Sealed-box math (Fc = Fs·√(1+Vas/Vb), Qtc = Qts·√(1+Vas/Vb); MNRX2: Fs 63.5, Vas 5.3, Qts 0.32):

| Chamber Vb | Fc | Qtc | verdict |
|------------|-----|-----|---------|
| 0.59 L (old DS115 pipe) | ~200 Hz | ~1.0 | ❌ humps ~200 Hz in the passband |
| 1.0 L | 159 Hz | 0.80 | OK |
| **~1.2 L (target)** | **148 Hz** | **0.74** | ✅ Fc at the crossover, benign Q |
| 1.5 L | 135 Hz | 0.68 | ✅ cleaner, more low-mid output |

**Target ≈ 1.2 L** (fit the largest the depth allows, ~1.2–1.5 L — more chamber = more clean output at 150–200 Hz, which helps the W5 output match). In the active-DSP system any residual hump is flattened, so ~0.8–1.5 L all works; don't over-engineer.

**Form: rectangular MDF box (chosen — easiest to build/seal/fit).**
- **Internal ≈ 130 × 130 × 85 mm** → gross ~1.44 L, minus MNRX2 basket (~0.3 L) → **~1.15 L net → Fc 151 Hz, Qtc 0.76** ✓. Scale to ~140 × 130 × 90 (~1.3 L net, Fc 142 / Qtc 0.72) for a touch more low-mid output if depth allows.
- **Construction:** 5-sided 12 mm MDF box (top, bottom, 2 sides, back) **butt-glued onto the rear of the front baffle** around the mid cutout — the baffle is the box's front face. Silicone all seams airtight. Optional light wadding.
- **Basket clearance:** MNRX2 basket ~100 mm dia, ~52 mm into the box → ~15 mm around it (130 mm internal), ~33 mm behind it (85 mm depth). Fine.

⚠ **Depth watch-point:** box is ~85 mm internal + 12 mm back = **~97 mm from the baffle**; the rear electronics pocket protrudes **46 mm** → only ~7 mm clearance in the 150 mm internal depth **if mid and pocket share a height**. Fix in geometry step by offsetting them vertically (mid lower-front, pocket upper-rear).
(110 mm/125 mm soil-pipe alternative dropped — box is simpler and packs better.)

The tweeter (SB19ST-C000-4) has its own sealed factory rear chamber — no isolation needed in the main cavity.

---

## Front Baffle — Driver Positions

All heights measured from the **external bottom of the acoustic section** (top of base).

```
   ┌────────────────────┐  270 mm top
   │     27 mm margin   │
   │  ┌─────────────┐   │  243 mm  tweeter top edge
   │  │ R2604/833000│   │
   │  │  ⊙  104 mm  │   │  185 mm  TWEETER CENTRE   ←── 115 mm c-t-c
   │  └─────────────┘   │  133 mm  tweeter bottom edge
   │     5 mm gap       │
   │  ┌─────────────┐   │  128 mm  mid top edge
   │  │   DS115-8   │   │
   │  │  ⊙ 115.6 mm │   │   70 mm  MID CENTRE        ←── 115 mm c-t-c (same as original)
   │  └─────────────┘   │   12 mm  mid bottom edge
   │     12 mm margin   │
   └────────────────────┘    0 mm  acoustic floor
```

| Gap | Distance | Flange gap |
|-----|----------|------------|
| Mid bottom to baffle edge | 12 mm | — |
| Mid → Tweeter | 5 mm | 5 mm |
| Tweeter top to baffle edge | 27 mm | — |

Baffle width 190 mm vs mid OD 115.6 mm: 37 mm margin each side.

---

## Crossover and Timing

Identical to prior design — DSP unchanged.

| Boundary | Frequency | Notes |
|----------|-----------|-------|
| Sub / Mid | 150 Hz | LR4; λ = 2,287 mm; side offset negligible |
| Mid / Tweet | 1,500 Hz | LR4; ideal √(880 × 2,636) = 1,523 Hz |

### Side-firing sub timing

At 150 Hz (λ = 2,287 mm), the sub radiates from the side panel at the listening position rather than from the front. The path difference depends on room geometry but is small (≤ 100 mm ≈ 0.04λ = 15°). Compensate with a short digital delay on the sub channel in JAB5 — measure and dial in after build.

### Mid/tweet timing

Physical offset mid→tweet = 115 mm = 0.5λ at 1,500 Hz → 0.335 ms delay on tweeter channel. Same as original design.

---

## Electronics Base

190 × 215 × 80 mm external (56 mm internal height, 12 mm top + bottom MDF).

JAB5 (121.92 × 91.44 × 45.1 mm) and PSU mounted **side by side in depth**, JAB5 at front, PSU behind with a 10 mm wiring gap.

| PSU candidate | Dimensions | Depth needed | Depth available | Fits? |
|---------------|-----------|-------------|-----------------|-------|
| Mean Well LRS-150-36 (closest available) | 159 × 97 × 30 mm | 198.4 mm | 191 mm | **NO** — 7.4 mm short (all LRS-150 variants same footprint; no 27V/29V variant exists) |
| AliExpress SMPS (pending spec confirm) | 127 × 83 × 38 mm | 184.4 mm | 191 mm | **YES** — 6.6 mm spare |

The AliExpress unit at 127 × 83 × 38 mm is the candidate PSU. **Specs to confirm before ordering:** output voltage ≥ 27.4 V (29 V target), current rating ≥ 5.1 A (or ≥ 3.0 A with cap bank — see amp.md). Both PSU height (38 mm) and JAB5 height (45.1 mm) clear the 56 mm internal height.

If the AliExpress unit proves inadequate, any LRS-150 variant (no 27V/29V exists — nearest is LRS-150-36 at 36V) requires increasing cabinet depth to 225 mm external. At 36V, DSP channel limiters are mandatory (138W available vs 80W sub limit).

Rear panel of base: removable (screwed). IEC inlet, RCA/XLR input, binding posts all rear-mounted. 25 mm cable grommet through acoustic floor to acoustic section.

---

## Volume Summary

| Space | Gross L | Net L | Note |
|-------|---------|-------|------|
| Sub / PR chamber | 7.54 | ~6.33 | Single volume; sub + PR share it |
| Mid rear pipe | 0.59 | 0.59 | Isolated rear chamber — 110 mm soil pipe, 70 mm long |
| Base | ~1.9 | — | JAB5 + PSU |

---

## Cut List (12 mm MDF unless noted)

⚠ **OLD-design cut list** (190×215×350 two-section). Superseded by the 220×180×360 single-section box — panels and the base section need re-deriving; only the mid-chamber line is updated below.

| Panel | Count | Dimensions mm | Material |
|-------|-------|---------------|----------|
| Front baffle | 1 | 190 × 270 | 18 mm MDF |
| Rear panel | 1 | 190 × 270 | 12 mm MDF |
| Side panel (sub, left) | 1 | 215 × 270 | 12 mm MDF |
| Side panel (PR, right) | 1 | 215 × 270 | 12 mm MDF — butt joints (OLD dims; revise to 180 × 360) |
| Top panel | 1 | 166 × 215 | 12 mm MDF |
| Acoustic floor (= base ceiling) | 1 | 166 × 215 | 12 mm MDF |
| Mid box — sides | 2 | 85 × 130 (internal depth × height) | 12 mm MDF |
| Mid box — top/bottom | 2 | 85 × 130 | 12 mm MDF |
| Mid box — back | 1 | 130 × 130 (+ wall overlap) | 12 mm MDF |
| (box glues to baffle rear around mid cutout; internal ≈130×130×85 → ~1.15 L net) | | | |
| Base rear (removable) | 1 | 190 × 80 | 12 mm MDF |
| Base sides | 2 | 215 × 80 | 12 mm MDF |
| Base front | 1 | 190 × 80 | 12 mm MDF |

Mid inner box panels:
- 2 sides: 110 × 70 mm
- 2 sides: 128 × 70 mm (includes 9 mm wall overlap)
- 1 cap: 128 × 128 mm

---

## Damping

- Acoustic chamber walls (all except side panels where sub/PR mount): 25 mm acoustic foam
- Leave the two side panels bare — foam would reduce effective box volume and block driver travel
- Mid inner box: no lining needed at 0.85 L
