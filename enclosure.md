# Enclosure Design — DS115-8 + R2604/833000 + W5-1138SMF + SB15SFCR-00 PR

GHM-inspired active 3-way kitchen counter monitor. Slim dark column, circles only on the front baffle, JAB5 + PSU in a sealed base below the acoustic section.

---

## Drivers

| Role | Driver | OD mm | Cutout mm | Depth mm | Notes |
|------|--------|-------|-----------|----------|-------|
| Sub | Tang Band W5-1138SMF | 133.3 | ~108 | ~95 | Surround protrudes 8.5 mm proud of baffle |
| Mid | Dayton DS115-8 | 115.6 | 93.6 | 54.7 | Surface mount; no countersink |
| Tweeter | Scan-Speak R2604/833000 | ~104 | ~74 | ~55 | Tuned rear chamber fixed — cannot shorten |
| PR | SB Acoustics SB15SFCR-00 | — | — | — | 5×8" racetrack, Sd 178 cm² |

---

## Overall Cabinet

Two-box stack. Acoustic section sits on top of the electronics base. Both have identical footprint.

```
╔══════════════════╗  ─┐
║                  ║   │
║  TWEETER         ║   │  Acoustic section
║                  ║   │  175 × 220 × 460 mm external
║  MID             ║   │  18 mm MDF front baffle
║                  ║   │  12 mm MDF all other panels
║  SUB             ║   │
╠══════════════════╣  ─┤  12 mm divider (acoustic floor)
║  JAB5 + PSU      ║   │  Electronics base
╚══════════════════╝  ─┘  175 × 220 × 130 mm external
```

| | External mm | Internal mm |
|---|---|---|
| Width | 175 | 151 |
| Depth | 220 | 190 (18 mm front + 12 mm rear) |
| Acoustic height | 460 | 436 |
| Base height | 130 | 106 |
| **Total height** | **602** | — |

---

## Internal Chamber Layout

Three isolated chambers separated by 12 mm MDF shelves with driver cutouts only where needed.

```
  436 mm ┬─────────────────────────────
         │  Tweeter space    82 mm
  354 mm ├── shelf ──────────────────── 
         │  Mid chamber     110 mm      3.15 L gross / ~2.8 L net
  232 mm ├── shelf ────────────────────
         │  Sub chamber     220 mm      6.31 L gross / ~6.1 L net (see below)
    0 mm ┴─────────────────────────────  (acoustic floor)
```

### Sub chamber — 6.1 L net

- Gross: 151 × 190 × 220 mm = **6.31 L**
- Minus sub basket volume (est. 0.4 L): **5.91 L**
- Plus surround recess recovery (8.5 mm protrusion × ~19 cm² annulus ≈ 160 mL): **+0.16 L**
- **Net: ~6.1 L**

PR (SB15SFCR-00) mounts on the rear panel within this chamber (see PR section).

### Mid chamber — ~2.8 L net

DS115-8 basket (54.7 mm deep) extends through the shelf into this space. Volume is over-sized relative to mid requirements — for a sealed mid above 150 Hz, any volume above 0.5 L is adequate. No tuning needed.

### Tweeter space — clearance only

R2604/833000 has its own factory-tuned rear chamber inside the driver (~50 mm deep). This space provides the mandatory ≥50 mm clearance behind the baffle inner face. Not acoustically tuned.

---

## Front Baffle — Driver Positions

All heights measured from the **external bottom face of the acoustic section**.

```
   ┌──────────────────────┐  460 mm top
   │      38 mm margin    │
   │   ┌──────────────┐   │  422 mm  tweeter top edge
   │   │  R2604/833000│   │
   │   │   ⊙  104 mm  │   │  370 mm  TWEETER CENTRE   ←── 115 mm c-t-c
   │   └──────────────┘   │  318 mm  tweeter bottom edge
   │      5 mm gap        │
   │   ┌──────────────┐   │  313 mm  mid top edge
   │   │   DS115-8    │   │
   │   │  ⊙  115.6 mm │   │  255 mm  MID CENTRE        ←── 155 mm c-t-c
   │   └──────────────┘   │  197 mm  mid bottom edge
   │      30 mm gap       │
   │  ┌────────────────┐  │  167 mm  sub top edge
   │  │  W5-1138SMF    │  │
   │  │  ⊙  133.3 mm   │  │  100 mm  SUB CENTRE
   │  └────────────────┘  │   33 mm  sub bottom edge
   │      33 mm margin    │
   └──────────────────────┘    0 mm  acoustic floor
```

| Gap | Distance | c-t-c | Flange gap |
|-----|----------|-------|------------|
| Sub bottom to baffle edge | 33 mm | — | — |
| Sub → Mid | 30 mm between flanges | 155 mm | 30 mm |
| Mid → Tweeter | 5 mm between flanges | 115 mm | 5 mm |
| Tweeter top to baffle edge | 38 mm | — | — |

Baffle width 175 mm accommodates sub (133.3 mm OD) with 21 mm margin each side.

---

## Passive Radiator

**Position:** Rear panel, centred horizontally, within the sub chamber section.

The SB15SFCR-00 racetrack (5"×8" ≈ 127 mm × 203 mm) mounts portrait on the rear panel:
- Long axis (203 mm) vertical — fits within 220 mm sub chamber height with 17 mm margin
- Short axis (127 mm) horizontal — fits within 175 mm panel width with 24 mm margin
- Centre: 110 mm from acoustic floor

### PR mass for tuning

Target Fb = 38 Hz (F3 ≈ 40 Hz, well-suited to music content above 35 Hz on a counter):

```
Mms_total = ρ₀c² × Sd_PR² / (Vb × (2π × Fb)²)
          = 142,356 × 0.0178² / (0.0061 × (2π × 38)²)
          = 45.1 / 346.6
          = 130 g total moving mass
```

SB15SFCR-00 stock Mms not confirmed — fetch datasheet. Assuming ~40–50 g stock:
- **Added mass required: ~80–90 g** via M6-threaded rear bolt
- Easily achieved with steel or brass M6 washers + nuts

For F3 = 35 Hz (Fb ≈ 33 Hz): Mms_total ≈ 175 g → ~125–135 g added mass (also feasible, heavier bolt stack).

| Target F3 | Mms total | Estimated Madd |
|-----------|-----------|----------------|
| 40 Hz | 130 g | ~80–90 g |
| 35 Hz | 175 g | ~125–135 g |

Sd ratio: PR 178 cm² / Sub 94 cm² = **1.89×** — slightly below the ideal ≥2× but within workable range given the PR's larger excursion capability.

---

## Crossover

| Boundary | Frequency | Filter | Window |
|----------|-----------|--------|--------|
| Sub / Mid | 150 Hz | LR4 (24 dB/oct) | Fs ratio: 150/55.2 = 2.72× mid, 150/45 = 3.3× sub ✓ |
| Mid / Tweeter | **1,500 Hz** | LR4 or LR8 | Window: 880–2,636 Hz (1,756 Hz wide); ideal √(880×2636) = 1,523 Hz |

Tweeter is over-engineered for this application (100W, needs ~8W burst). No power concern whatsoever.

### Acoustic timing

At 1,500 Hz crossover (λ = 229 mm), physical centre offset mid→tweeter = 115 mm = 0.50λ. This creates a natural 180° acoustic path difference at the crossover frequency. Compensate in JAB5 DSP by:

1. **Digital delay on tweeter channel:** 115 mm ÷ 343,000 mm/s = **0.335 ms** — advance tweeter relative to mid, or equivalently add delay to mid.
2. Alternatively use LR8 (48 dB/oct) slopes which may self-correct through their steeper phase rotation — verify by impulse measurement after build.

Sub → Mid physical offset = 155 mm at 150 Hz (λ = 2,287 mm) → 0.068λ → 24° — negligible; DSP delay not required.

---

## Electronics Base

JAB5 (Sure TDA7498E, 3-channel) + PSU in a separate sealed bay below the acoustic section.

### Recommended PSU candidates

| PSU | Voltage | Dimensions mm | Notes |
|-----|---------|---------------|-------|
| Mean Well LRS-150-24 | 24V / 6.3A | 159×97×30 | Confirmed in project |
| Mean Well LRS-200-27 | 27V / 7.4A | 175×99×30 | Closer to 29V target; wider |
| Custom linear 29V | 29V / 5A | ~150×100×60 | Toroid + rectifier; quietest; overkill |

At 24V/8Ω: JAB5 delivers ~31W per channel. At 27V: ~41W per channel into 8Ω. DS115-8 needs 37.2W burst — 27V PSU covers it cleanly; 24V is marginal at peak.

**Recommendation: LRS-200-27** (27V) gives headroom for DS115-8 burst without custom PSU. Size 175×99 mm fits in the 175×220 mm base footprint (just — PSU oriented with 175 mm axis across the 175 mm cabinet width, 99 mm along the depth).

JAB5 + LRS-200-27 stacked height estimate:
- PSU: 30 mm
- JAB5 + heatsink: ~50 mm
- Clearance + wiring: 20 mm
- Total: ~100 mm → fits in 106 mm internal base height ✓

### Base access

Rear panel of base: removable (screwed, no glue) for PSU access. Speaker binding posts, XLR/RCA input, and IEC power inlet mounted on rear panel of base. Wire loom from base to acoustic section through a 25 mm hole in the divider shelf.

---

## Construction Notes

### Baffle (front panel)
- **18 mm MDF** — sub excursion and mass demand stiff baffle
- All three drivers surface-mount (no rebate); DS115-8 explicitly designed for front mount
- R2604/833000 uses 5× M4 mounting holes on 92 mm PCD at 72° spacing — use template
- Sub: 4× M5 screws into T-nuts on basket flange (or 4× M4 per Dayton spec)

### Internal shelves
- Sub/mid shelf: 12 mm MDF with DS115-8 cutout (93.6 mm) and cable pass-through
- Mid/tweeter shelf: 12 mm MDF with R2604/833000 cutout (74 mm) and cable pass-through
- Both shelves glued and screwed to side panels with 18×18 mm triangular glue blocks

### Bracing
- Single cross-brace (12 mm MDF dowel or 25×25 mm rectangular batten) at mid-height of sub chamber connecting front baffle to rear panel — prevents panel resonance at sub frequencies

### Damping
- Sub chamber: 25 mm acoustic foam on all four side walls (NOT rear — PR must be unobstructed)
- Mid chamber: 25 mm acoustic foam on rear and side walls; leave front clear
- Tweeter space: small piece of acoustic wool tucked at rear corners — prevents standing waves

### Finish
- Baffle: 120-grit sand, prime, 3× satin black spray (enamel); drivers protrude through paint
- Sides/top: 0.6 mm satin black vinyl wrap or spray; matching colour to baffle
- Base: same wrap; cable entry with small rubber grommet

---

## Volume Summary

| Chamber | Gross L | Net L | Driver |
|---------|---------|-------|--------|
| Sub | 6.31 | ~6.1 | W5-1138SMF |
| Mid | 3.15 | ~2.8 | DS115-8 |
| Tweeter | 2.07 | clearance | R2604/833000 |
| Base | 3.43 | — | JAB5 + PSU |

---

## Cut List (12 mm MDF unless noted)

| Panel | Count | Dimensions mm | Material |
|-------|-------|---------------|----------|
| Front baffle | 1 | 175 × 460 | 18 mm MDF |
| Rear panel | 1 | 175 × 460 | 12 mm MDF |
| Side panels | 2 | 220 × 460 | 12 mm MDF |
| Top panel | 1 | 151 × 220 | 12 mm MDF |
| Acoustic floor (= base ceiling) | 1 | 151 × 220 | 12 mm MDF |
| Sub/mid shelf | 1 | 151 × 190 | 12 mm MDF |
| Mid/tweet shelf | 1 | 151 × 190 | 12 mm MDF |
| Base rear (removable) | 1 | 175 × 130 | 12 mm MDF |
| Base sides | 2 | 220 × 130 | 12 mm MDF |
| Base front | 1 | 175 × 130 | 12 mm MDF |

Total MDF (estimate): ~0.5 m² of 18 mm + ~1.5 m² of 12 mm.
