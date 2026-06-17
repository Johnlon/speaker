# Enclosure Design — DS115-8 + R2604/833000 + W5-1138SMF + SB15SFCR-00 PR

GHM-inspired active 3-way kitchen counter monitor. Side-firing sub and PR free up the front baffle for mid + tweeter only — circles on a slim black column. JAB5 + PSU in sealed base below.

---

## Drivers

| Role | Driver | Frame mm | Cutout mm | Depth mm | Fires |
|------|--------|----------|-----------|----------|-------|
| PR | SB Acoustics SB15SFCR-00 | 253 × 168.75 racetrack | 220 × 119.1 | 49.7 | LEFT side (portrait) |
| Sub | Tang Band W5-1138SMF | 155 OD | 120 | 81 (from back of flange) | RIGHT side |
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
║  ◎ PR    ◎ sub ║   │  12 mm MDF all other panels
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
| Soil pipe outer volume (π×55²×70 mm) | −0.67 L |
| Sub basket protrusion | −0.51 L |
| Tweeter body | −0.05 L |
| **Net sub volume** | **~6.33 L** |

6.33 L net is well above the W5-1138SMF's Vas (4.81 L) — correct operating range for a PR-loaded alignment. The soil pipe mid box displaces 0.46 L less than the old MDF box (1.13 L), which is why the net volume increased.

---

## Side Panel Drivers

### Left side — SB15SFCR-00 (passive radiator, portrait)

The racetrack frame (253 × 168.75 mm) mounts portrait — long axis vertical.

- Centre: **135 mm from acoustic floor** (external measurement)
- Frame long axis (253 mm) in height: 135 ± 126.5 mm → **8.5–261.5 mm** — 8.5 mm margin top and bottom ⚠ tight (see construction note)
- Frame short axis (168.75 mm) in depth: 215 mm available → 23 mm margin each side ✓
- Cutout 220 × 119.1 mm — fully within panel face ✓
- Mounting depth 49.7 mm + sub basket 81 mm = 130.7 mm < 166 mm internal width → **35 mm clearance** ✓

**Construction note:** 8.5 mm frame-to-panel-edge margin means the top/bottom panels must attach via **dado or rabbet joints** cut into the side panels, not butt-jointed onto the outer face. This keeps the side panel outer face clear for the full 270 mm so the PR flange has unobstructed bearing. Do not run glue blocks or screws within 10 mm of the side panel top/bottom edges in the PR zone.

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

Calculated at Vb = 6.33 L net (soil pipe mid box). M_total = (Kms + Kair) / (2πFb)².

| Target Fb | Mms total | Added mass |
|-----------|-----------|------------|
| 35 Hz | 170 g | **108 g** |
| 38 Hz | 144 g | **82 g** |
| 40 Hz | 130 g | **68 g** |
| 42 Hz | 118 g | **56 g** |
| 45 Hz | 103 g | **41 g** |

**Recommendation: 40 Hz tuning (68 g added)** — gives F3 ≈ 35 Hz. Mass: 68 g via M6 stud + steel washer stack on rear boss. Verify by measuring free-air Fs of loaded PR before installation.

**Sd ratio:** SB15SFCR-00 178 cm² / W5-1138SMF 94 cm² = **1.89×** — well above the 1.5× minimum; PR displacement per unit sub displacement is comfortably lower than Xmax allows.

---

## Mid Inner Box — 110 mm Soil Pipe

The mid's rear wave must be isolated from the sub chamber. A length of standard 110 mm OD soil pipe (PVC-U, BS EN 1329) glued to the rear of the front baffle makes a simple, airtight rear chamber.

```
Front baffle (rear face)
    │
    ├── silicone bead ──────────────────┐
    │   110 mm OD soil pipe             │  Sealed rear chamber
    │   ID ~103.6 mm                    │  for DS115-8
    │   length ~70 mm                   │
    └── 12 mm MDF disc cap ─────────────┘
        (sealed with silicone, retained by 3 mm screw tabs or push-fit cap)
```

| Dimension | Value |
|-----------|-------|
| Pipe OD / ID | 110 mm / 103.6 mm (3.2 mm wall, PVC-U) |
| Length (cut to) | 70 mm (basket 54.7 mm + 15 mm clearance) |
| Internal air volume | ~0.59 L |
| Volume displaced from sub | ~0.66 L (including pipe wall) |
| Clearance: basket in pipe | 5 mm each side (93.6 mm cutout vs 103.6 mm ID) |

0.59 L is adequate for a mid crossed at 150–1,500 Hz. No tuning required; rear chamber compliance is negligible at these frequencies.

Mount: press pipe end against baffle rear face, centred on the 93.6 mm cutout. Run a bead of silicone around the joint. Cap the far end with a 12 mm MDF disc (110 mm OD) glued and siliconed. Allow 24 h cure before closing the cabinet.

**Clearance to PR body:** soil pipe left edge is ~28 mm from left inner panel; PR body protrudes ~49.7 mm from left panel at flange depth, but at the soil pipe's height (70 mm centre) the PR protrusion is only ~10–15 mm (end-cap region). Nominal gap ~13–18 mm. Verify physically when PR arrives — do not glue mid pipe until trial-fitted.

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

| Panel | Count | Dimensions mm | Material |
|-------|-------|---------------|----------|
| Front baffle | 1 | 190 × 270 | 18 mm MDF |
| Rear panel | 1 | 190 × 270 | 12 mm MDF |
| Side panel (sub, left) | 1 | 215 × 270 | 12 mm MDF |
| Side panel (PR, right) | 1 | 215 × 270 | 12 mm MDF — dado/rabbet top+bottom edges |
| Top panel | 1 | 166 × 215 | 12 mm MDF |
| Acoustic floor (= base ceiling) | 1 | 166 × 215 | 12 mm MDF |
| Mid rear pipe | 1 | 110 mm OD × 70 mm long | 110 mm soil pipe (PVC-U) |
| Mid pipe end cap | 1 | 110 mm OD disc | 12 mm MDF |
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
