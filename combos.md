# Driver Combination Spreadsheet

Exhaustive record of every evaluated mid+tweeter pairing. One row per combination. Per-driver data (sensitivity, power, Fs, etc.) is in [drivers.md](drivers.md). Curated recommendations are in [solutions.md](solutions.md).

---

## System Reference

- Sub at 40W RMS → **98 dB @1m** (continuous) | Sub at 80W → **101 dB @1m** (burst)
- JAB5: P = V²/(2R) × 0.85 | 24V → 31W/8Ω, 61W/4Ω | 28V → 42W/8Ω, 84W/4Ω | 29V → 45W/8Ω, 89W/4Ω
- Crossover targets: sub LP 150 Hz (LR24) · mid BP 150–2,800 Hz · tweeter HP 2,800 Hz (LR48)

**PSU column** shows "RMS min / Burst min":
- **RMS min** = lowest voltage where all three drivers match at 98 dB. Sub (40W/4Ω) needs 19.4V → 24V covers every combo at RMS except TCP115-8 (28V).
- **Burst min** = lowest voltage for 101 dB parity. Sub (80W/4Ω) sets a 27.4V → **28V floor**. 8Ω mids with sensitivity below ~85 dB push higher. All within JAB5's 10–39V unless flagged with *.

**Power correction for 4Ω drivers:** Sensitivity specs are at 2.83V/1m. For 4Ω drivers, 2.83V delivers 2W — so the 1W sensitivity = Sens_2.83V − 3.01 dB. Correct burst power: P = 10^((101 − (Sens_2.83V − 3.01)) / 10). Example: SB19ST (4Ω, 88.5 dB) → P_burst = 10^((101−85.49)/10) = 35.5W vs 30W rated (18% over — brief transients only, DSP limiter caps at 100 dB). For 8Ω drivers, 2.83V = 1W, no correction needed.

Per-driver power requirements are in [drivers.md](drivers.md).

---

## Beaming Limits — Max Useful Mid/Tweeter Crossover

Beaming limit: f = 34400 / (π × √(Sd/π)) Hz, where Sd in cm².

| Mid | Size | Sd cm² | Beams above |
|-----|------|--------|-------------|
| DSA90-8 | 3" | ~26 | 3,260 Hz |
| SB12PFCR/MNRX2-25-4 | 4" | ~50 | 2,730 Hz |
| DS115-8 / HiVi B4N | 4" | ~48 | ~2,636 Hz |
| DMA105-8 | 4" (105mm OD) | ~40 | ~2,900 Hz |
| SPM-116/8 / Beyma 4FR40 / DA115-8 | 4" | ~46 | ~2,600 Hz |
| TCP115-8 / SIG120-4 | 4" | ~45 | ~2,570 Hz |
| Tang Band W4-655F | 4" (125mm OD) | ~50 | ~2,636 Hz |
| Dayton RS125-4 | 5" | ~79 | ~2,184 Hz |
| HiVi M5N | 5" | ~79 | ~2,185 Hz |
| SB13PFC25-4/8 / SDS-P830656 | 5" | ~87 | ~2,080 Hz |
| SIG150-4 (5.25") | 5.25" | ~99 | 1,990 Hz |

---

## Tweeter Minimum Crossover (2× Fs)

| Tweeter | Min xover | FP OD mm | Sens dB | Power W |
|---------|-----------|----------|---------|---------|
| R2604/833000 | 880 Hz | ~104 | 92 | **100** |
| XT25TG30-04 | 880 Hz | 104 | 91.9 | 15 |
| R2604/832000 | 1,000 Hz | ~104 | 90 | **100** |
| XT25BG60-04 | 1,140 Hz | 104.5 | 92.6 | 15 |
| DX25TG59-04 | 1,180 Hz | 104 | 93.4 | 15 |
| SB29SDAC | 1,200 Hz | ~104 | ~91 | ~30 |
| SB29RDNC-C000-4 | 1,160 Hz | ~104 | 94 | 100 |
| RST28F-4 | 1,420 Hz | 104.8 | 93.5 | 80 |
| D2606/920000 | 2,200 Hz | ~104 | 91.4 | 100 |
| NE25VTS-04 | 1,460 Hz | 66.3 | 91.1 | 15 |
| SB21SDC-C000-4 | 1,440 Hz | 92 | 91 | 40 |
| SB26ST-C000-5 | 1,740 Hz | ~72 | 91 | 80 |
| SEAS H1406-04 | 2,340 Hz | 69.7×54oval | 91 | 80 |
| CF18N-4 | 2,200 Hz | 58 | 90 | 40 |
| TD25F-4 | 1,800 Hz | 93.5 | 91 | 20 |
| DA25BG08-06 | 1,420 Hz | 104 | 91.6 | 15 |
| XT25SC90-04 | 1,650 Hz | ~90 | 90.1 | 100 |
| XT19TD00-04 | 1,640 Hz | 94 | 88.9 | 20 |
| SB19ST | 1,960 Hz | 88 | 88.5 | 30 |
| SB26STCN-C000-4 | 1,900 Hz | 72 | 92 | 120 |
| DT-28N | 2,400 Hz | ~72 | ~92 | 50 |
| HiVi TN28-B | 2,600 Hz | 47.6 | 90 | 15 |
| ND25FA-4 | 2,700 Hz | 66 | 90 | 20 |
| HiVi TN25 | 3,000 Hz | 54×54sq | 91 | 20 |
| XT25SC40-04 (ring rad) | 2,036 Hz | 43.9 | 94 | 100 |
| Markaudio TW 6 | 3,400 Hz | ~90 | — | — |
| BC25SC06-04 | 2,700 Hz | ~70 | 95.4 | 50 |

---

## All Pairings

PSU = "RMS min / Burst min". `*` = mid reaches ~100.3 dB max even at 36V (JAB5 ceiling) — 1 dB short of sub burst.

| ID | Mid | Tweeter | Xover Hz | Spacing mm | Price £ | PSU (RMS/Burst) | Character | Flags / Notes |
|----|-----|---------|----------|-----------|---------|-----------------|-----------|---------------|
| S1 | DS115-8 | SB19ST | 2,500 | 102 | ~50 | 24V / 28V | Warm | 4 units left |
| S2 | SB12PFCR25-4 | SB19ST | 2,700 | 105 | ~41 | 24V / 28V | Warm, natural | Best value; 10+ stock |
| S3 | SB12MNRX2-25-4 | SB29SDAC | 1,200–2,700 | ~107 | ~92 | 24V / 28V | Warm-neutral | Ring dome; wide xover window |
| A1 | HiVi B4N | SB19ST | 2,500 | 102 | ~38 | 24V / 28V | Warm | Zero DSP correction; 10+ stock; Fs 66.3 Hz (2.26× margin) |
| A2 | SB12MNRX2-25-4 | SB19ST | 2,700 | 105 | ~72 | 24V / 28V | Warm, dynamic | Controlled transients |
| A3 | DSA90-8 | SB19ST | 2,800 | 90 | ~49 | 24V / 29V | Detailed | Tightest round spacing |
| A4 | DS115-8 | DX25TG59-04 | 1,800–2,500 | 110 | ~60 | 24V / 28V | Warm, flexible | Widest xover window (std dome) |
| A5 | SB12PFCR25-4 | DX25TG59-04 | 1,800–2,700 | 110 | ~51 | 24V / 28V | Warm, flexible | A4 at lower cost |
| A6 | Beyma 4FR40 | SB19ST | 2,500 | 103 | ~45 | 24V / 28V | Warm | Confirm Fs before ordering |
| A7 | SPM-116/8 | SB19ST | 2,500 | 102 | ~37 | 24V / 32V | Warm | Cheapest paper mid; 84 dB sens → mid-limited at burst |
| A8 | SIG120-4 | SB19ST | 2,500 | 105 | ~48 | 24V / 28V | Clear, dynamic | 4Ω; Audiophonics FR only |
| B1 | TCP115-8 | SB19ST | 2,500 | 102 | ~31 + PSU | 28V / 36V* | Warmest | Cheapest drivers; mid maxes at ~100.3 dB at 36V |
| B2 | ND91-4 | SB19ST | 2,700 | 97 | ~48 | 24V / 28V | Detailed | Confirm Fs before ordering |
| B3 | HiVi M5N | DX25TG59-04 | 1,200–2,100 | ~103 | ~54 | 24V / 28V | Warm | 5"; DX25 needed (not SB19ST) |
| B4 | SB13PFC25-8 | DX25TG59-04 | 1,200–2,080 | ~110 | ~53 | 24V / 28V | Warm | Best Fs margin; 5" natural fibre |
| B5 | DA115-8 | SB19ST | 2,500 | 102 | ~40 | 24V / 28V | Detailed | Near-perfect sensitivity match; 3 left; DA115 on sale €24.75 (Jun 2026) |
| B6 | DSA90-8 | HiVi TN25 | 3,000 | 73 | ~52 | 24V / 29V | Detailed | Tightest spacing; square tweeter; TN25 depth 63.5mm — check clearance |
| B7 | SDS-P830656 | DX25TG59-04 | 1,500–2,000 | ~105 | ~54 | 24V / 28V | Natural | Xmax 10mm; truncated frame |
| B8 | SIG150-4 | DX25TG59-04 | 1,500–1,990 | 128 | ~60 | 24V / 28V | Neutral | 152mm OD — wide baffle; poor 60° off-axis |
| B9 | SB12PACR25-4-COAX | (built-in) | 2,800 | 0 | ~59 | 24V / 28V | Clear | Point source; max SPL ~94 dB — sub must be limited |
| B10 | DSA90-8 | ND25FA-4 | 2,700 | 79 | ~44 | 24V / 29V | Detailed | Minimum round spacing |
| B11 | DSA90-8 | DT-28N | 2,500 | ~82 | ~65 | 24V / 29V | Detailed | Compact waveguide |
| B12 | SLS-85S25CP04-04 | DT-28N | 2,500 | ~82 | ~61 | 24V / 28V | Warm | Oval mid; 86 dB → sub-limited at burst |
| RR1 | DS115-8 | XT25TG30-04 | 880–2,636 | 113 | ~62 | 24V / 28V | Warm + wide | Best ring radiator; widest xover window |
| RR2 | SB12PFCR25-4 | XT25TG30-04 | 880–2,730 | 116 | ~52 | 24V / 28V | Warm + wide | Best value ring radiator |
| RR3 | SB12MNRX2-25-4 | XT25TG30-04 | 880–2,730 | 116 | ~83 | 24V / 28V | Warm + wide | Ring radiator + highest headroom |
| RR4 | DSA90-8 | XT25SC90-04 | 2,800 | 91 | ~37 | 24V / 29V | Detailed + wide | Cheapest ring radiator; single Falcon order |
| RR4B | SB12PFCR25-4 | XT25SC90-04 | 1,650–2,730 | 106 | ~39 | 24V / 28V | Warm + wide | Cheapest ring rad + nat. fibre; 1080Hz DSP window; £8 under RR2 |
| RR4C | DS115-8 | XT25SC90-04 | 1,650–2,636 | 103 | ~49 | 24V / 28V | Warm + wide | Paper warmth + ring rad; cheaper than RR1 (XT25TG30) by ~£13 |
| RR5 | SIG150-4 | XT25TG30-04 | 1,000–1,990 | 140 | ~67 | 24V / 28V | Neutral | Only tweeter that works with SIG150-4 |
| RR6 | DS115-8 | SB29SDAC | 1,200–2,636 | ~110 | ~71 | 24V / 28V | Warm + ring dome | Ring dome + paper warmth |
| C1 | RS100-8 | SB19ST | 2,500 | — | ~60 | 24V / 29V | Detailed | Fs 1.63× at 150 Hz — marginal; 84.6 dB → mid-limited at burst |
| C2 | PA130-8 | SB19ST | 2,000 | — | ~47 | 24V / 28V | Natural | Xmax 2mm; Fs 1.8×; OD 132mm |
| C3 | TF0510 | SB19ST | 2,200 | — | ~45 | 24V / 28V | Natural | Weakest Fs (1.42×) + Xmax (1.1mm) |
| C4 | DSA90-8 | Markaudio TW 6 | 3,200–3,400 | — | ~69 | 24V / 29V | Detailed | Xover above mid beaming limit; poor 60° |
| NR1 | DSA90-8 | NE25VTS-04 | 1,460–3,260 | 79 | ~64 | 24V / 29V | Detailed | Same spacing as B10; much lower min xover (1,460 vs 2,700 Hz) |
| NR2 | DS115-8 | NE25VTS-04 | 1,460–2,636 | 91 | ~65 | 24V / 28V | Warm | Wide xover window; paper warmth + compact tweeter |
| NR3 | SB12PFCR25-4 | NE25VTS-04 | 1,460–2,730 | ~94 | ~56 | 24V / 28V | Warm, natural | NR2 at lower cost with nat. fibre mid |
| RD0 | DSA90-8 | SB21SDC-C000-4 | 1,440–3,260 | 92 | ~64 | 24V / 29V* | Detailed + ring dome | Widest ring dome window (1,820Hz!); 92mm spacing; compact detailed mid + ring dome; 29V for burst |
| RD1 | DS115-8 | SB21SDC-C000-4 | 1,440–2,636 | 104 | ~65 | 24V / 28V | Warm + ring dome | Ring dome alt to RR6; saves ~£6; 92mm FP tighter than SB29 |
| RD2 | SB12PFCR25-4 | SB21SDC-C000-4 | 1,440–2,730 | 107 | ~56 | 24V / 28V | Warm + ring dome | Cheapest ring dome pairing; nat. fibre + smaller SB21 ring dome |
| RD3 | SB12MNRX2-25-4 | SB21SDC-C000-4 | 1,440–2,730 | 107 | ~86 | 24V / 28V | Warm + ring dome | Engineering ring dome; saves ~£6 vs S3 |
| XC1 | DSA90-8 | XT25SC40-04 | 2,036–3,260 | 68 | ~55 | 24V / 29V | Detailed + wide | Absolute minimum spacing (68 mm); ring rad dispersion; 100W |
| XC2 | DS115-8 | XT25SC40-04 | 2,036–2,636 | 80 | ~56 | 24V / 28V | Warm + wide | Paper warmth + ultra-compact ring rad; ~600 Hz xover window |
| XC3 | SB12PFCR25-4 | XT25SC40-04 | 2,036–2,730 | 83 | ~47 | 24V / 28V | Warm + wide | Best value ultra-compact ring rad; nat. fibre + 43.9mm ring rad |
| TN1 | DSA90-8 | HiVi TN28-B | 2,600–3,260 | 70 | ~55 | 24V / 29V | Detailed | 2nd tightest round spacing (70mm); narrow xover window |
| TN2 | DS115-8 | HiVi TN28-B | 2,600–2,636 | 82 | ~56 | 24V / 28V | Warm | Only 36 Hz xover window — risky; likely unusable |
| DA1 | DS115-8 | DA25BG08-06 | 1,420–2,636 | 110 | ~65 | 24V / 28V | Warm, flexible | Peerless dome; same FP as DX25; wide xover window |
| DA2 | SB12PFCR25-4 | DA25BG08-06 | 1,420–2,730 | 113 | ~56 | 24V / 28V | Warm, flexible | Wide-window pairing; ~£5 cheaper than A5 (DX25) |
| R1 | RS125-4 | DX25TG59-04 | 1,180–2,184 | 115 | ~78 | 24V / 28V | Neutral-bright | Premium 5" Al; 4Ω; needs DX25 (beams above 2184 Hz) |
| R2 | RS125-4 | XT25TG30-04 | 880–2,184 | 115 | ~87 | 24V / 28V | Neutral + wide | Premium 5" + ring rad; widest window possible for 5" |
| R3 | SB13PFCR25-4 | DX25TG59-04 | 1,180–2,080 | 117 | ~45 | 24V / 28V | Warm, nat. fibre | Cheaper 5" option vs R1 at same crossover constraint |
| COAX2 | SB12PFC25-4-COAX | (built-in) | ~2,800 | 0 | ~48 | 24V / 28V | Warm | Nat. fibre coaxial; cheaper than B9 (£59); same SPL ceiling ~94 dB |
| ST1 | DS115-8 | SB26ST-C000-5 | 1,740–2,636 | 94 | ~58 | 24V | Warm | 80W tweeter; ~72mm FP (assume); wide window; robust power handling |
| ST2 | SB12PFCR25-4 | SB26ST-C000-5 | 1,740–2,730 | 97 | ~48 | 24V | Warm, nat. | Cheapest 80W tweeter pairing; nat. fibre + indestructible tweeter |
| ST3 | DSA90-8 | SB26ST-C000-5 | 1,740–3,260 | 82 | ~56 | 24V | Detailed | 82mm spacing; 80W tweeter; widest xover window of any DSA90-8 pairing |
| NX1 | SB12NRX25-4 | SB19ST | 1,960–2,730 | ~105 | ~65 | 24V | Warm, nat. | Premium paper NRX; acoustically identical to S2 (SB12PFCR25-4) — choose S2 on value |
| NX2 | SB12NRX25-4 | XT25TG30-04 | 880–2,730 | ~116 | ~81 | 24V | Warm + wide | Premium NRX + ring rad; acoustically identical to RR2 — choose RR2 on value |
| PL1 | PLUVIA-7HD Gold | SB19ST | 1,960–~2,900 | ~105 | ~58 | 24V | Warm, zero-pad | Unique zero-correction mid; system SPL capped 97 dB (DSP at 18W); Mg/Al cone |
| DC1 | DS115-8 | D2604/830000 | 1,260–2,636 | 110 | ~70 | 24V | Warm, 100W | Scan-Speak 100W dome; same spacing as DA1 but wider window + indestructible tweeter |
| DC2 | SB12PFCR25-4 | D2604/830000 | 1,260–2,730 | 113 | ~60 | 24V | Warm, nat. 100W | Cheapest 100W wide-window pairing; nat. fibre + Scan-Speak 100W at €45 |
| SE1 | DSA90-8 | SEAS H1406-04 | 2,340–3,260 | ~75 | ~74 | 24V | Detailed | **⚠ H1406-04 OOS (Jun 2026)** — pre-order only. 80W oval tweeter; 73mm portrait spacing; on sale €40.45 |
| SE2 | DS115-8 | SEAS H1406-04 | 2,340–2,636 | ~85 | ~76 | 24V | Warm | **⚠ H1406-04 OOS** — pre-order only. SEAS 80W; only 296Hz window — very tight; not recommended even if restocked |
| CF1 | DSA90-8 | CF18N-4 | 2,200–3,260 | **75** | ~61 | 24V | Detailed, CF | **⚠ CF18N-4 OOS (Jun 2026)** — pre-order only. 18mm CF dome; on sale €30.54; monitor for restock |
| CF2 | DS115-8 | CF18N-4 | 2,200–2,636 | 87 | ~63 | 24V | Warm, CF | **⚠ CF18N-4 OOS** — pre-order only. Carbon fibre dome; 40W; paper warmth + CF detail |
| CF3 | SB12PFCR25-4 | CF18N-4 | 2,200–2,730 | 90 | ~53 | 24V | Warm nat., CF | **⚠ CF18N-4 OOS** — pre-order only. Best value CF dome; 40W; monitor for restock |
| TD1 | DSA90-8 | TD25F-4 | 1,800–3,260 | 93 | ~55 | 24V | Detailed | Semi-horn 93.5mm FP; wide xover window; note semi-horn narrows HF off-axis |
| TD2 | DS115-8 | TD25F-4 | 1,800–2,636 | 105 | ~58 | 24V | Warm | Semi-horn + paper warmth; wide window (836Hz) but semi-horn off-axis concern |
| DT1 | DS115-8 | D27TG35-06 | 1,800–2,636 | 110 | ~65 | 24V | Warm, 6Ω | 6Ω tweeter; 104mm FP; same spacing as DA1; 15W (adequate at 10.5W burst) |
| DT2 | SB12PFCR25-4 | D27TG35-06 | 1,800–2,730 | 113 | ~56 | 24V | Warm nat., 6Ω | 6Ω; same class as DA2 at same price; DA25 wins on Fs (710 vs 900Hz) |
| BC1 | DSA90-8 | BC25SC06-04 | 2,700–3,260 | 81 | ~55 | 24V / 29V | Detailed | 50W tweeter; 95.4dB → only 1.8W at ref / 3.6W burst; FP ~70mm (est); 81mm spacing |
| BC2 | DS115-8 | BC25SC06-04 | 2,700 | 93 | ~55 | 24V / 28V | Warm | Xover at DS115 beaming limit (2636Hz) — marginally tight; on-axis only |
| BC3 | SB12PFCR25-4 | BC25SC06-04 | 2,700–2,730 | 96 | ~47 | 24V / 28V | Warm, nat. | 30Hz xover window only — fixed at ~2,715Hz; cheapest 50W nat. fibre pairing |
| STC1 | DSA90-8 | SB26STCN-C000-4 | 1,900–3,260 | 82 | ~63 | 24V / 29V | Detailed | 120W indestructible; 82mm spacing; 1360Hz DSP window; burnout impossible at 29V |
| STC2 | DS115-8 | SB26STCN-C000-4 | 1,900–2,636 | 94 | ~65 | 24V / 28V | Warm | 120W + paper warmth; 736Hz window; best power safety for DS115 pairing |
| STC3 | SB12PFCR25-4 | SB26STCN-C000-4 | 1,900–2,730 | 97 | ~55 | 24V / 28V | Warm, nat. | Best value 120W pairing; nat. fibre + indestructible tweeter; 830Hz window |
| AL1 | DS115-8 | SB26ADC-C000-4 | 1,360–2,636 | 110 | ~79 | 24V / 28V | Warm + bright Al | 120W Al dome; same FP class as D2604; wider window (1360 vs 1260Hz min); €7 more |
| AL2 | SB12PFCR25-4 | SB26ADC-C000-4 | 1,360–2,730 | 113 | ~69 | 24V / 28V | Warm nat. + Al | 120W Al dome + nat. fibre; warm-bright hybrid |
| XBG1 | DS115-8 | XT25BG60-04 | 1,140–2,636 | 110 | ~76 | 24V / 28V | Warm + wide | Ring rad; SI-stocked (vs XT25TG30 pre-order); widest window std-stock ring rad |
| XBG2 | SB12PFCR25-4 | XT25BG60-04 | 1,140–2,730 | ~110 | ~66 | 24V / 28V | Warm nat. + wide | SI-stocked ring rad alt to RR2 (XT25TG30 pre-order only at SI); nat. fibre warmth |
| XBG3 | DSA90-8 | XT25BG60-04 | 1,140–3,260 | 98 | ~67 | 24V / 29V | Detailed + wide | Widest xover window of any DSA90-8 pairing; ring rad off-axis |
| RPN1 | DS115-8 | SB29RDNC-C000-4 | 1,160–2,636 | 110 | ~87 | 24V / 28V | Warm + ring dome 100W | Premium ring dome; 1,476Hz DSP window; 94dB → only 5W at burst; 100W = burnout impossible |
| RPN2 | SB12PFCR25-4 | SB29RDNC-C000-4 | 1,160–2,730 | 113 | ~79 | 24V / 28V | Warm nat. + ring dome 100W | Widest ring dome window in catalogue (1,570Hz); nat. fibre + premium ring dome |
| RPN3 | SB12MNRX2-25-4 | SB29RDNC-C000-4 | 1,160–2,730 | 113 | ~109 | 24V / 28V | Warm + ring dome 100W | Engineering flagship; Qts 0.27 mid + 100W ring dome; cost ceiling option |
| RPN4 | DSA90-8 | SB29RDNC-C000-4 | 1,160–3,260 | 98 | ~86 | 24V / 29V | Detailed + ring dome 100W | Widest window of any DSA90-8 pairing (2,100Hz); 98mm spacing; premium compact option |
| RST1 | DS115-8 | RST28F-4 | 1,420–2,636 | 110 | ~70 | 24V / 28V | Warm + 80W | 80W; 93.5dB → 5.6W at burst; same spacing as DC1; £0 premium over D2604 |
| RST2 | SB12PFCR25-4 | RST28F-4 | 1,420–2,730 | 113 | ~60 | 24V / 28V | Warm nat. + 80W | 80W; wider window than STC3 (SB26STCN); lower sensitivity match (+6dB vs +7dB DSP pad) |
| RST3 | DSA90-8 | RST28F-4 | 1,420–3,260 | 98 | ~68 | 24V / 29V | Detailed + 80W | 1,840Hz window; 98mm spacing; 80W insurance at 29V |
| D26_1 | DSA90-8 | D2606/920000 | 2,200–3,260 | 98 | ~63 | 24V / 29V | Detailed + 100W 6Ω | 1,060Hz window; 6Ω; 100W; compact 98mm spacing |
| D26_2 | DS115-8 | D2606/920000 | 2,200–2,636 | 110 | ~64 | 24V / 28V | Warm + 100W 6Ω | 436Hz window — tight; cross at DS115 beaming limit; 6Ω; 100W |
| D26_3 | SB12PFCR25-4 | D2606/920000 | 2,200–2,730 | 113 | ~55 | 24V / 28V | Warm nat. + 100W 6Ω | 530Hz window; cheapest 100W 6Ω pairing; €5 under D2604 equivalent |
| SB13_TG | SB13PFCR25-4 | XT25TG30-04 | 880–2,080 | 117 | ~67 | 24V / 28V | Warm, nat. + wide | 5"; Fs=44Hz (3.4× margin); 1,200Hz ring rad window; deepest low-end DSP flexibility; 190mm baffle OK (vertical layout) |
| SB13_DC | SB13PFCR25-4 | D2604/830000 | 1,260–2,080 | 117 | ~63 | 24V / 28V | Warm, nat. + 100W | 5" + Scan-Speak 100W; 820Hz window; 190mm baffle OK |
| SB13_RPN | SB13PFCR25-4 | SB29RDNC-C000-4 | 1,160–2,080 | 117 | ~81 | 24V / 28V | Warm nat. + ring dome | 5"; 920Hz window; 100W ring dome; engineering peak for 5" mid; 190mm baffle OK |
| M_TG | HiVi M5N | XT25TG30-04 | 880–2,185 | 115 | ~68 | 24V / 28V | Warm + wide | 5"; best Fs margin (50Hz); 1,305Hz window; widest M5N option; 190mm baffle OK |
| M_RPN | HiVi M5N | SB29RDNC-C000-4 | 1,160–2,185 | 115 | ~83 | 24V / 28V | Warm + ring dome | 5"; 1,025Hz window; 100W ring dome; 190mm baffle OK |
| B_TG | HiVi B4N | XT25TG30-04 | 880–2,636 | 110 | ~62 | 24V / 28V | Warm gold + wide | Perfect sub sens match (85dB); widest B4N window (1,756Hz); ring rad; single order Falcon+SI |
| B_STC | HiVi B4N | SB26STCN-C000-4 | 1,900–2,636 | 94 | ~50 | 24V / 28V | Warm gold + 120W | Cheapest 120W pairing (~£50); 94mm spacing; zero DSP correction needed at 85dB |
| B_DC | HiVi B4N | D2604/830000 | 1,260–2,636 | 110 | ~63 | 24V / 28V | Warm gold + 100W | Scan-Speak 100W; widest window for B4N standard dome (1,376Hz); DS115 replacement |
| DA_TG | DA115-8 | XT25TG30-04 | 880–2,636 | 110 | ~64 | 24V / 28V | Al + ring rad | Ring rad + Al; 3 left — order now; widest Al-mid window (1,756Hz); DA115 sale €24.75 |
| DA_STC | DA115-8 | SB26STCN-C000-4 | 1,900–2,636 | 94 | ~52 | 24V / 28V | Al + 120W | 120W + Al cone; 3 left; 94mm spacing; DA115 sale → ~£52 now |
| XT19_1 | DSA90-8 | XT19TD00-04 | 1,640–3,260 | 93 | ~61 | 24V / 29V* | Detailed + ring | 19mm ring rad; 93mm spacing; burst needs 32.4W (4Ω correction) vs 20W rated — DSP limiter at 18W caps tweeter to 98.9dB (2.1dB gap to sub burst — audible HF compression) |
| XT19_2 | SB12PFCR25-4 | XT19TD00-04 | 1,640–2,730 | 108 | ~52 | 24V / 28V* | Warm + ring | 19mm ring; 1090Hz window; same 2.1dB HF ceiling at burst; DSP limiter essential |
| XT19_3 | DS115-8 | XT19TD00-04 | 1,640–2,636 | 105 | ~62 | 24V / 28V* | Warm + ring | 19mm ring + paper warmth; 996Hz window; burst ceiling 98.9dB; SB19ST (100dB cap) or XT25TG30 preferred |
| DMA1 | DMA105-8 | SB19ST | 1,960–2,900 | 96 | ~44 | 24V / 28V | Al neodymium | 4" dual-neo Al cone; beaming 2,900Hz (better than DS115 at 2,636); **min LP 200Hz recommended** (Fs 72Hz → 2×Fs=144Hz marginal at 150); 35W rated (better than DA115 at 20W); 940Hz window |
| DMA2 | DMA105-8 | XT25TG30-04 | 880–2,900 | 107 | ~52 | 24V / 28V | Al + ring rad | 2,020Hz DSP window (widest DMA105 pairing); ring rad off-axis; 107mm spacing; Falcon £29.90 for twt saves ~£13; **min LP 200Hz** |
| DMA3 | DMA105-8 | SB29RDNC-C000-4 | 1,160–2,900 | 104 | ~80 | 24V / 28V | Al + ring dome 100W | 1,740Hz window; premium 100W ring dome; 104mm spacing; compact pairing; **min LP 200Hz** |
| RP1 | DSA90-8 | R2604/833000 | 880–3,260 | 98 | ~75 | 24V / 29V | Detailed + ring rad 100W | **Absolute window champion: 2,380Hz** (widest in catalogue); same Fs as XT25TG30 + 100W; 98mm spacing; Scan-Speak Discovery ring rad |
| RP2 | DS115-8 | R2604/833000 | 880–2,636 | 110 | ~80 | 24V / 28V | Warm + ring rad 100W | 1,756Hz window (tied with RR1); 100W vs XT25TG30 15W; same price class (+€12.50); indestructible tweeter |
| RP3 | SB12PFCR25-4 | R2604/833000 | 880–2,730 | 113 | ~70 | 24V / 28V | Warm nat. + ring rad 100W | 1,850Hz window (wider than RR2); 100W; nat. fibre + Discovery ring rad; €12.50 over RR2 |
| RP4 | DSA90-8 | R2604/832000 | 1,000–3,260 | 98 | ~63 | 24V / 29V | Detailed + ring rad 100W | 2,260Hz window; cheaper (€52.95 vs €62.45); 2dB less sens than RP1; 120Hz narrower than RP1 |
| RP5 | DS115-8 | R2604/832000 | 1,000–2,636 | 110 | ~66 | 24V / 28V | Warm + ring rad 100W | 1,636Hz window; budget Discovery 100W ring rad; ~£3 premium over XT25TG30 |
| RP6 | SB12PFCR25-4 | R2604/832000 | 1,000–2,730 | 113 | ~56 | 24V / 28V | Warm nat. + ring rad 100W | 1,730Hz window; cheapest 100W ring rad + nat. fibre; best value in RP series |

---

## Supplier Notes (June 2026)

- **SoundImports** (EU) — primary source for most drivers
- **Falcon Acoustics** (UK) — SB19ST £14.30, XT25TG30-04 £29.90 (**in stock**), XT25SC90-04 £18.20, DX25TG59-04 £20.85
- **Note (Jun 2026):** XT25TG30-04 now also in stock at SI (€49.95, 10+). Falcon £29.90 is ~£13 cheaper; use SI only if combining with other SI order. XT25SC90-04 also at SI (€26.95) vs Falcon (£18.20 ≈ £5 cheaper).
- **Audiophonics** (France) — SIG120-4 in stock, ships to UK
