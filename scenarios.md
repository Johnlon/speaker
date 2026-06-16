# Driver Pairing Scenarios

Derived from `drivers.json` (146 entries) and `REQUIREMENTS.md` only.
Generated 2026-06-16.

**System constants:** Sub = Tang Band W5-1138SMF, 4Ω, 85 dB, 40W RMS / 80W burst peak.
Target SPL: 98 dB RMS, 101 dB burst. Amp: JAB5 @ 0.85 η. All impedances measured.

**PSU floor:** Sub burst (80W/4Ω) sets minimum supply at 28V. All combos below use **29V** (standard Mean Well LRS/LRS-series) — delivers 89W/4Ω, 45W/8Ω.

**Crossover window grades:**
- Comfortable ≥ 1.0 oct | Moderate 0.5–1.0 oct | Tight 0.25–0.5 oct | Very tight < 0.25 oct
- Lower bound = 3× tweeter Fs; upper bound = mid beam-80% (0.8 × 34400 / (π × √(Sd/π)))
- Ideal crossover = geometric mean of bounds

**Datasheet links** (local path first where downloaded):

| Driver | Local | Source URL |
|--------|-------|-----------|
| DS115-8 | [research/dayton_ds115-8.pdf](research/dayton_ds115-8.pdf) | https://www.parts-express.com/pedocs/specs/295-424--dayton-audio-ds115-8-specifications.pdf |
| D2604/833000 | [research/scan_speak_d2604-833000.pdf](research/scan_speak_d2604-833000.pdf) | https://www.scan-speak.dk/datasheet/pdf/d2604-833000.pdf |
| DX25TG59-04 | [research/peerless_dx25tg59-04.pdf](research/peerless_dx25tg59-04.pdf) | https://doc.soundimports.nl/pdf/brands/Peerless%20by%20Tymphany/DX25TG59-04/DX25TG59-04.pdf |
| MDT22T | [research/morel_mdt22t.pdf](research/morel_mdt22t.pdf) | https://cdn.shopify.com/s/files/1/0809/2387/files/MOREL_MDT22_DATASHEET.pdf?v=1686654880 |
| XT25TG30-04 | no local | https://doc.soundimports.nl/pdf/brands/Peerless%20by%20Tymphany/XT25TG30-04/XT25TG30-04.pdf |

---

## Scenario 1 — Visual Interest (by shape class)

Three shape classes, one best pick each.

| ID | Mid | Tweeter | Crossover | Price | PSU | Character | Why |
|----|-----|---------|-----------|-------|-----|-----------|-----|
| **V-RR** | DS115-8 · 8Ω · 85.3 dB · 116mm OD | XT25TG30-04 · 4Ω · 91.9 dB · ring rad · 104mm OD | 1,670 Hz · moderate · 0.68 oct · **ROUND** | £32 + £43 = **£75** | 29V / 4.6A burst | Warm + airy | Both round frames — clean matched aesthetic. Ring rad gives wide throw. Limiter needed (16.3W vs 15W rated — 0.35 dB at burst, set in ADAU1701). |
| **V-SQ** | DS115-8 · 8Ω · 85.3 dB · 116mm OD | MDT22T · 8Ω · 89 dB · square 54×54mm | 1,949 Hz · **tight** · 0.23 oct · **SQUARE ACCENT** | £32 + ? = TBD | 29V / 4.1A burst | Warm + punchy | Only viable square-face tweeter. Striking contrast: large round cone vs small square dome. **Tight window — measure and iterate; datasheet FR floor 1,800 Hz gives 0.23 oct.** 80W MDT22T demand is 15.9W, comfortable. 85mm centre spacing. |
| **V-MX** | DS115-8 · 8Ω · 85.3 dB · 116mm OD | SB29SDNC · 4Ω · 95.5 dB · 72mm ring dome | 1,969 Hz · tight · 0.11 oct · **MIXED** | £32 + ? = TBD | 29V / 4.1A burst | Warm + extended | Noticeably small tweeter face vs large round cone — industrial minimalist look. 95.5 dB sens means only 7.1W at burst (zero stress). Very tight window same as V-SQ — needs precise DSP. |

> **Note on V-SQ and V-MX:** both have sub-0.25-oct windows. ADAU1701 DSP with Linkwitz-Riley 4th order handles this, but leave headroom for measurement correction — you won't hit the ideal frequency exactly first time.

---

## Scenario 2 — Best for 60° off-axis (kitchen / cooker)

Ring radiator mandatory. Ranked by: off-axis dispersion → crossover window → headroom.

| ID | Mid | Tweeter | Crossover | Price | PSU | Character | Why |
|----|-----|---------|-----------|-------|-----|-----------|-----|
| **OA-1** | DS115-8 · 8Ω · 85.3 dB · 116mm OD | **R2604/833000** · 4Ω · 92 dB · ring rad · 100W | 1,670 Hz · **moderate** · 0.68 oct | £32 + £48 (Willys) = **£80** | 29V / 4.6A burst | Warm + airy | Top pick. Ring rad with 100W rating — **no DSP limiter ever needed** (15.9W burst demand). Widest crossover window of any ring rad combo. Paper cone warmth + Scan-Speak ring rad detail. Moderate window = most DSP-forgiving alignment. Willys £47.79; SI £62. |
| **OA-2** | DS115-8 · 8Ω · 85.3 dB · 116mm OD | **XT25TG30-04** · 4Ω · 91.9 dB · ring rad · 15W | 1,670 Hz · moderate · 0.68 oct | £32 + £43 = **£75** | 29V / 4.6A burst | Warm + airy | Same crossover window as OA-1, £19 cheaper. 16.3W burst demand vs 15W rated — set DSP limiter at 100.6 dB (0.4 dB below burst ceiling, inaudible in practice). Same wide dispersion character. |
| **OA-3** | SB12PFCR25-4 · 4Ω · 87.5 dB · 122mm OD | **XT25BG60-04** · 4Ω · 92.6 dB · ring rad · 15W | 1,938 Hz · tight · 0.36 oct | ? + ? = TBD | 29V / 4.8A burst | Natural + open | **Only ring rad pair that is fully safe at burst without any limiter** (13.9W vs 15W rated). Natural fibre cone. Tighter crossover window than OA-1/2 — precision DSP needed, but ADAU1701 is adequate. Mid burst demand (44.8W vs 30W rated) is transient-only; SPL limiter covers it. |

---

## Scenario 3 — Best for on-axis listening (direct, centred)

Dome tweeter preferred — dispersion less critical, quality focus.

| ID | Mid | Tweeter | Crossover | Price | PSU | Character | Why |
|----|-----|---------|-----------|-------|-----|-----------|-----|
| **OX-1** | DS115-8 · 8Ω · 85.3 dB · 116mm OD | **D2604/833000** · 4Ω · 93 dB · dome · 100W | 1,735 Hz · **moderate** · 0.57 oct | £32 + ? = TBD | 29V / 4.5A burst | Warm + detailed | Best overall on-axis pair. 100W dome — zero tweeter stress (12.6W burst). Paper warmth + Scan-Speak treble resolution. Moderate window = relaxed DSP alignment. Widest appeal for critical listening. |
| **OX-2** | SEAS CA12RCY · 8Ω · 86 dB · 124mm OD | **D2604/833000** · 4Ω · 93 dB · dome · 100W | 1,727 Hz · moderate · 0.55 oct | ? + ? = TBD | 29V / 4.3A burst | Natural + refined | Premium SEAS mid paired with Scan-Speak dome — both in the same quality tier. 60W mid rating at 31.6W burst = comfortable 2× headroom. Near-identical crossover point to OX-1, slightly tighter window. |
| **OX-3** | 12MU/4731T00 · 4Ω · 90 dB · 101mm OD | **D2604/833000** · 4Ω · 93 dB · dome · 100W | 1,705 Hz · moderate · 0.52 oct | ? + ? = TBD | 29V / 4.0A burst | Transparent + detailed | All Scan-Speak. Illuminator mid has lowest colouration in the candidate set — if you want maximum resolution on-axis, this is it. Most compact OD (101mm). 25.2W burst vs 80W rated = 3× headroom. Slightly tighter window than OX-1 but still moderate. |

---

## Scenario 4 — Compact baffle / minimum width

Ranked by centre-to-centre spacing (mid OD + tweeter OD) / 2. Smaller = less required baffle height.

| ID | Mid (OD) | Tweeter (OD) | Spacing | Crossover | Price | PSU | Character | Why |
|----|----------|--------------|---------|-----------|-------|-----|-----------|-----|
| **CP-1** | DS115-8 · 116mm | MDT22T · 54mm sq | **85mm** | 1,949 Hz · tight · 0.23 oct | £32 + ? | 29V / 4.1A burst | Warm + punchy | Tightest possible spacing of any viable pair. 85mm vertical centre gap. Square MDT22T adds visual interest. Tight window — measure and iterate. 80W MDT22T at 15.9W burst = comfortable. |
| **CP-2** | 12MU/4731T00 · 101mm | D2604/833000 · 104mm | **103mm** | 1,705 Hz · moderate · 0.52 oct | ? + ? | 29V / 4.0A burst | Transparent + detailed | Second-tightest spacing but with a **moderate crossover window** — much easier to align. Smallest eligible mid (101mm OD). All Scan-Speak quality. Best compact pick if you don't want a narrow DSP window. |
| **CP-3** | 12MU/4731T00 · 101mm | DX25TG59-04 · 104mm | **103mm** | ? + £28 | 29V / 3.9A burst | Transparent + open | Same spacing as CP-2, tweeter safe at burst (11.5W vs 15W — no limiter). DX25TG59-04 is a 93.4 dB dome with confirmed GBP price. Tighter window (0.20 oct) than CP-2 — precise DSP needed, but tweeter headroom is better. |

---

## Scenario 5 — Best value

Only pairs with at least one confirmed GBP price are ranked. No confirmed pair achieves under £50 combined.

### Under £100

| ID | Mid | Tweeter | Crossover | Price | PSU | Character | Why |
|----|-----|---------|-----------|-------|-----|-----------|-----|
| **BV-1** | DS115-8 · 8Ω · 85.3 dB | DX25TG59-04 · 4Ω · 93.4 dB · dome · 15W | 1,933 Hz · tight · 0.25 oct | £32 + £28 = **£60** | 29V / 4.6A burst | Warm | **Cheapest viable pair with both prices confirmed.** Dome is safe at burst (11.5W vs 15W — no limiter). Tight crossover window — set DSP carefully. Good starting point for the build. |
| **BV-2** | DS115-8 · 8Ω · 85.3 dB | XT25TG30-04 · 4Ω · 91.9 dB · ring rad · 15W | 1,670 Hz · **moderate** · 0.68 oct | £32 + £43 = **£75** | 29V / 4.6A burst | Warm + airy | Ring rad for £15 more than BV-1. Moderate window = far more DSP-forgiving. Limiter needed at burst (0.4 dB margin) — trivial in ADAU1701. Big upgrade in off-axis performance. |
| **BV-3** | DS115-8 · 8Ω · 85.3 dB | **R2604/833000** · 4Ω · 92 dB · ring rad · 100W | 1,670 Hz · **moderate** · 0.68 oct | £32 + £48 (Willys) = **£80** | 29V / 4.6A burst | Warm + airy | Ring rad, 100W — **no limiter, ever.** Now confirmed £47.79 at Willys — only £5 above BV-2. Wider window (0.68 oct) and higher sensitivity than the 832000 version. Beats the 832000 on every metric for nearly the same price. |

### Under £50 — not achievable

Cheapest verified pairs with both drivers having GBP prices: £60 (BV-1). The SB12PFCR25-4 (mid candidate) has no GBP price in `drivers.json`; if sourced at ~£21 (Willys, unverified), BV-1 equivalent drops to ~£49 — but this cannot be confirmed from the database.

---

## Summary — one-line per scenario

| Scenario | Best pick | Price | Key metric |
|----------|-----------|-------|------------|
| Visual — round | DS115-8 + XT25TG30-04 | £75 | Both round, moderate window |
| Visual — square | DS115-8 + MDT22T | TBD | 85mm spacing, square accent |
| Visual — mixed | DS115-8 + SB29SDNC | TBD | Small ring dome contrast |
| 60° off-axis | DS115-8 + R2604/833000 | £80 (Willys) | Ring rad, 100W, moderate window |
| On-axis quality | DS115-8 + D2604/833000 | TBD | 100W dome, moderate window, warm |
| Compact | DS115-8 + MDT22T | TBD | 85mm spacing (tightest) |
| Value best | DS115-8 + DX25TG59-04 | £60 | Cheapest confirmed pair |
| Value ring rad | DS115-8 + R2604/833000 | £80 | Ring rad, no limiter, only £5 over XT25TG30-04 |
