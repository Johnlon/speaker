# Enclosure Design — DS115-8 + R2604/833000 + W5-1138SMF + SB15SFCR-00 PR

GHM-inspired active 3-way kitchen counter monitor. Side-firing sub and PR free up the front baffle for mid + tweeter only — circles on a slim black column. JAB5 + PSU in sealed base below.

---

## Drivers

| Role | Driver | Frame mm | Cutout mm | Depth mm | Fires |
|------|--------|----------|-----------|----------|-------|
| Sub | Tang Band W5-1138SMF | 155 OD | 120 | 81 (from back of flange) | LEFT side |
| PR | SB Acoustics SB15SFCR-00 | 253 × 168.75 racetrack | 220 × 119.1 | 49.7 | RIGHT side (portrait) |
| Mid | Dayton DS115-8 | 115.6 OD | 93.6 | 54.7 | Front |
| Tweeter | Scan-Speak R2604/833000 | ~104 OD | ~74 | ~55 | Front |

---

## Overall Cabinet

```
╔══════════════════╗  ─┐
║                  ║   │
║  TWEETER  (front)║   │  Acoustic section
║  MID      (front)║   │  190 × 215 × 270 mm external
║                  ║   │  18 mm MDF front baffle
║  ◎ sub   ◎ PR  ║   │  12 mm MDF all other panels
║  (L side)(R side)║   │
╠══════════════════╣  ─┤  12 mm divider (acoustic floor)
║  JAB5 + PSU      ║   │  Electronics base
╚══════════════════╝  ─┘  190 × 215 × 80 mm external
                           ──────────────────
                           Total: 190 × 215 × 350 mm
```

| Dimension | External mm | Internal mm |
|-----------|-------------|-------------|
| Width | 190 | 166 |
| Depth | 215 | 185 (18 mm front + 12 mm rear) |
| Acoustic height | 270 | 246 |
| Base height | 80 | 56 |
| **Total height** | **350** | — |

Width increase from 175→190 mm is driven by sub basket depth (81 mm confirmed) + SB15SFCR-00 mounting depth (49.7 mm) + clearance. At 166 mm internal width the two drivers clear each other by **35 mm** — comfortable.

---

## Acoustic Volume

Single acoustic volume — no internal shelves. Sub and PR share the full interior. Mid is isolated by a small sealed inner box (see below).

**Gross internal volume:** 166 × 185 × 246 = **7.54 L**

| Deduction | Volume |
|-----------|--------|
| Mid inner box walls + cavity | −1.13 L |
| Sub basket protrusion | −0.51 L |
| Tweeter body | −0.05 L |
| **Net sub volume** | **~5.8 L** |

5.8 L net is above the W5-1138SMF's Vas (4.81 L) — correct operating range for a PR-loaded alignment.

---

## Side Panel Drivers

### Left side — W5-1138SMF (sub)

Side panel face: 215 mm deep × 270 mm tall.

- Centre: **135 mm from acoustic floor** (external measurement)
- OD span: 135 ± 77.5 mm → **57.5–212.5 mm** — fully within 270 mm ✓
- Cutout: 120 mm on 215 mm depth → 47.5 mm margin each side ✓

### Right side — SB15SFCR-00 (passive radiator, portrait)

The racetrack frame (253 × 168.75 mm) mounts portrait — long axis vertical.

- Centre: **135 mm from acoustic floor** — symmetric with sub ✓
- Frame long axis (253 mm) in height: 135 ± 126.5 mm → **8.5–261.5 mm** — 8.5 mm margin top and bottom ⚠ tight (see construction note)
- Frame short axis (168.75 mm) in depth: 215 mm available → 23 mm margin each side ✓
- Cutout 220 × 119.1 mm — fully within panel face ✓
- Mounting depth 49.7 mm + sub basket 81 mm = 130.7 mm < 166 mm internal width → **35 mm clearance** ✓

**Construction note:** 8.5 mm frame-to-panel-edge margin means the top/bottom panels must attach via **dado or rabbet joints** cut into the side panels, not butt-jointed onto the outer face. This keeps the side panel outer face clear for the full 270 mm so the PR flange has unobstructed bearing. Do not run glue blocks or screws within 10 mm of the side panel top/bottom edges in the PR zone.

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

Calculated at Vb = 5.8 L net. M_total = (ρ₀c² × Sd²) / (4π² × Fb² × Vb).

| Target Fb | Mms total | Added mass |
|-----------|-----------|------------|
| 35 Hz | 183 g | **121 g** |
| 38 Hz | 156 g | **94 g** |
| 40 Hz | 141 g | **79 g** |
| 42 Hz | 128 g | **66 g** |
| 45 Hz | 112 g | **50 g** |

**Recommendation: 40 Hz tuning (79 g added)** — gives F3 ≈ 35 Hz, well-matched to W5-1138SMF characteristics. Mass: 79 g via M6 stud + steel washer stack on rear boss. Verify by measuring free-air Fs of loaded PR before installation.

**Sd ratio:** SB15SFCR-00 178 cm² / W5-1138SMF 94 cm² = **1.89×** — well above the 1.5× minimum; PR displacement per unit sub displacement is comfortably lower than Xmax allows.

---

## Mid Inner Box

The mid's rear wave must be isolated from the sub chamber. Build a small sealed box from 9 mm MDF, glued to the front baffle inner face, surrounding the DS115-8 basket.

```
Front baffle (inner face)
    │
    ├──── 9 mm MDF cap ────────────┐
    │     9 mm MDF side (×4)       │  Inner box
    │     110 mm × 110 mm × 70 mm  │  (fits DS115-8 basket 54.7 mm + 15 mm clearance)
    └──────────────────────────────┘
         Open face sealed to baffle around cutout by gasket + silicone
```

| Dimension | Value |
|-----------|-------|
| Inner cavity (W × D × H) | 110 × 110 × 70 mm |
| Inner air volume | 0.85 L |
| Wall material | 9 mm MDF |
| Outer footprint in sub chamber | ~128 × 128 × 79 mm |
| Volume displaced from sub | ~1.13 L |

0.85 L rear chamber for a mid crossing at 150–1,500 Hz is adequate. No tuning required.

The tweeter mounts above the mid through the same baffle. The R2604/833000 has its own tuned factory rear chamber; no isolation needed in the main cavity.

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

190 × 215 × 80 mm external (56 mm internal height).

LRS-150-24 (159 × 97 × 30 mm) + JAB5 board (~100 × 75 × 20 mm) — stacked (50 mm combined) fits in 56 mm with 6 mm to spare. Tight; use low-profile connectors and route cables along base walls.

Alternatively use a compact 24 V SMPS brick (e.g., Mean Well GST90A24-P1M, 155 × 50 × 30 mm) to free up more clearance.

Rear panel of base: removable (screwed). IEC inlet, RCA/XLR input, binding posts all rear-mounted. 25 mm cable grommet through acoustic floor to acoustic section.

---

## Volume Summary

| Space | Gross L | Net L | Note |
|-------|---------|-------|------|
| Sub / PR chamber | 7.54 | ~5.8 | Single volume; sub + PR share it |
| Mid inner box | 0.85 | 0.85 | Isolated rear chamber for DS115-8 |
| Base | ~1.9 | — | JAB5 + PSU |

---

## Cut List (12 mm MDF unless noted)

| Panel | Count | Dimensions mm | Material |
|-------|-------|---------------|----------|
| Front baffle | 1 | 190 × 270 | 18 mm MDF |
| Rear panel | 1 | 190 × 270 | 12 mm MDF |
| Side panel (sub, left) | 1 | 215 × 270 | 12 mm MDF |
| Side panel (PR, right) | 1 | 215 × 270 | 12 mm MDF — dado/rabbet top+bottom edges |
| Top panel | 1 | 166 × 215 | 12 mm MDF |
| Acoustic floor (= base ceiling) | 1 | 166 × 215 | 12 mm MDF |
| Mid inner box sides (×4) + cap | 5 | various | 9 mm MDF |
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
