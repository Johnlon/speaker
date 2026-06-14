# Driver Combination Spreadsheet

Exhaustive record of every evaluated mid+tweeter pairing. One row per combination. Per-driver data (sensitivity, power, Fs, etc.) is in [drivers.md](drivers.md). Curated recommendations are in [solutions.md](solutions.md).

---

## System Reference

- Sub at 40W RMS → **98 dB @1m** (continuous) | Sub at 80W → **101 dB @1m** (burst)
- JAB5: 24V → 31W/8Ω, 61W/4Ω | 29V → 45W/8Ω, 90W/4Ω (η = 0.85)
- Crossover targets: sub LP 150 Hz (LR24) · mid BP 150–2,800 Hz · tweeter HP 2,800 Hz (LR48)

Per-driver power requirements are in [drivers.md](drivers.md).

---

## Beaming Limits — Max Useful Mid/Tweeter Crossover

| Mid | Beams above |
|-----|-------------|
| DSA90-8 | 3,260 Hz |
| SB12PFCR/MNRX2-25-4 (4") | 2,730 Hz |
| DS115-8 / HiVi B4N | ~2,636 Hz |
| SPM-116/8 / Beyma 4FR40 / DA115-8 | ~2,600 Hz |
| TCP115-8 / SIG120-4 | ~2,570 Hz |
| HiVi M5N (5") | ~2,185 Hz |
| SB13PFC25-8 / SDS-P830656 | ~2,080 Hz |
| SIG150-4 (5.25") | 1,990 Hz |

---

## Tweeter Minimum Crossover (2× Fs)

| Tweeter | Min xover | FP OD mm | Sens dB | Power W |
|---------|-----------|----------|---------|---------|
| XT25TG30-04 | 880 Hz | 104 | 91.9 | 15 |
| XT25BG60-04 | 1,140 Hz | 104.5 | 92.6 | 15 |
| DX25TG59-04 | 1,180 Hz | 104 | 93.4 | 15 |
| SB29SDAC / SB29RDNC | 1,200 Hz | ~104 | ~91 | ~30 |
| NE25VTS-04 | 1,460 Hz | 66.3 | 91.1 | 15 |
| SB21SDC-C000-4 | 1,440 Hz | 92 | 91 | 40 |
| DA25BG08-06 | 1,420 Hz | 104 | 91.6 | 15 |
| XT25SC40-04 (ring rad) | 2,036 Hz | **43.9** | 94 | 100 |
| XT25SC90-04 | 1,650 Hz | ~90 | 90.1 | 100 |
| SB19ST | 1,960 Hz | 88 | 88.5 | 30 |
| SB26STCN-C000-4 | 1,900 Hz | 72 | 92 | 120 |
| DT-28N | 2,400 Hz | ~72 | ~92 | 50 |
| HiVi TN28-B | 2,600 Hz | **47.6** | 90 | 15 |
| ND25FA-4 | 2,700 Hz | 66 | 90 | 20 |
| HiVi TN25 | 3,000 Hz | 54×54sq | 91 | 20 |
| Markaudio TW 6 | 3,400 Hz | ~90 | — | — |

---

## All Pairings

| ID | Mid | Tweeter | Xover Hz | Spacing mm | Price £ | PSU | Character | Flags / Notes |
|----|-----|---------|----------|-----------|---------|-----|-----------|---------------|
| S1 | DS115-8 | SB19ST | 2,500 | 102 | ~50 | 24V | Warm | 4 units left |
| S2 | SB12PFCR25-4 | SB19ST | 2,700 | 105 | ~41 | 24V | Warm, natural | Best value; 10+ stock |
| S3 | SB12MNRX2-25-4 | SB29SDAC | 1,200–2,700 | ~107 | ~92 | 24V | Warm-neutral | Ring dome; wide xover window |
| A1 | HiVi B4N | SB19ST | 2,500 | 102 | ~38 | 24V | Warm | Zero DSP correction; 10+ stock |
| A2 | SB12MNRX2-25-4 | SB19ST | 2,700 | 105 | ~72 | 24V | Warm, dynamic | Controlled transients |
| A3 | DSA90-8 | SB19ST | 2,800 | 90 | ~49 | 24V | Detailed | Tightest round spacing |
| A4 | DS115-8 | DX25TG59-04 | 1,800–2,500 | 110 | ~60 | 24V | Warm, flexible | Widest xover window (std dome) |
| A5 | SB12PFCR25-4 | DX25TG59-04 | 1,800–2,700 | 110 | ~51 | 24V | Warm, flexible | A4 at lower cost |
| A6 | Beyma 4FR40 | SB19ST | 2,500 | 103 | ~45 | 24V | Warm | Confirm Fs before ordering |
| A7 | SPM-116/8 | SB19ST | 2,500 | 102 | ~37 | 24V | Warm | Cheapest paper mid |
| A8 | SIG120-4 | SB19ST | 2,500 | 105 | ~48 | 24V | Clear, dynamic | 4Ω; Audiophonics FR only |
| B1 | TCP115-8 | SB19ST | 2,500 | 102 | ~31 + PSU | **29V** | Warmest | Cheapest drivers; 29V required |
| B2 | ND91-4 | SB19ST | 2,700 | 97 | ~48 | **29V** | Detailed | Confirm Fs before ordering |
| B3 | HiVi M5N | DX25TG59-04 | 1,200–2,100 | ~103 | ~54 | 24V | Warm | 5"; DX25 needed (not SB19ST) |
| B4 | SB13PFC25-8 | DX25TG59-04 | 1,200–2,080 | ~110 | ~53 | 24V | Warm | Best Fs margin; 5" natural fibre |
| B5 | DA115-8 | SB19ST | 2,500 | 102 | ~44 | 24V | Detailed | Near-perfect sensitivity match; 3 left |
| B6 | DSA90-8 | HiVi TN25 | 3,000 | 73 | ~52 | 24V | Detailed | Tightest spacing; square tweeter; TN25 depth 63.5mm — check clearance |
| B7 | SDS-P830656 | DX25TG59-04 | 1,500–2,000 | ~105 | ~54 | 24V | Natural | Xmax 10mm; truncated frame |
| B8 | SIG150-4 | DX25TG59-04 | 1,500–1,990 | 128 | ~60 | 24V | Neutral | 152mm OD — wide baffle; poor 60° off-axis |
| B9 | SB12PACR25-4-COAX | (built-in) | 2,800 | 0 | ~59 | 24V | Clear | Point source; max SPL ~94 dB — sub must be limited |
| B10 | DSA90-8 | ND25FA-4 | 2,700 | 79 | ~44 | 24V | Detailed | Minimum round spacing |
| B11 | DSA90-8 | DT-28N | 2,500 | ~82 | ~65 | 24V | Detailed | Compact waveguide |
| B12 | SLS-85S25CP04-04 | DT-28N | 2,500 | ~82 | ~61 | **29V** | Warm | Oval mid; 29V required |
| RR1 | DS115-8 | XT25TG30-04 | 880–2,636 | 113 | ~62 | 24V | Warm + wide | Best ring radiator; widest xover window |
| RR2 | SB12PFCR25-4 | XT25TG30-04 | 880–2,730 | 116 | ~52 | 24V | Warm + wide | Best value ring radiator |
| RR3 | SB12MNRX2-25-4 | XT25TG30-04 | 880–2,730 | 116 | ~83 | 24V | Warm + wide | Ring radiator + highest headroom |
| RR4 | DSA90-8 | XT25SC90-04 | 2,800 | 91 | ~37 | 24V | Detailed + wide | Cheapest ring radiator; single Falcon order |
| RR5 | SIG150-4 | XT25TG30-04 | 1,000–1,990 | 140 | ~67 | 24V | Neutral | Only tweeter that works with SIG150-4 |
| RR6 | DS115-8 | SB29SDAC | 1,200–2,636 | ~110 | ~71 | 24V | Warm + ring dome | Ring dome + paper warmth |
| C1 | RS100-8 | SB19ST | 2,500 | — | ~60 | 24V | Detailed | Fs 1.63× at 150 Hz — marginal |
| C2 | PA130-8 | SB19ST | 2,000 | — | ~47 | 24V | Natural | Xmax 2mm; Fs 1.8×; OD 132mm |
| C3 | TF0510 | SB19ST | 2,200 | — | ~45 | 24V | Natural | Weakest Fs (1.42×) + Xmax (1.1mm) |
| C4 | DSA90-8 | Markaudio TW 6 | 3,200–3,400 | — | ~69 | 24V | Detailed | Xover above mid beaming limit; poor 60° |
| NR1 | DSA90-8 | NE25VTS-04 | 1,460–3,260 | 79 | ~44 | 24V | Detailed | Same spacing as B10; much lower min xover (1,460 vs 2,700 Hz) |
| NR2 | DS115-8 | NE25VTS-04 | 1,460–2,636 | 91 | ~51 | 24V | Warm | Wide xover window vs SB19ST equivalent |
| NR3 | SB12PFCR25-4 | NE25VTS-04 | 1,460–2,730 | ~94 | ~43 | 24V | Warm, natural | NR2 at lower cost with nat. fibre mid |
| RD1 | DS115-8 | SB21SDC-C000-4 | 1,440–2,636 | 104 | ~49 | 24V | Warm + ring dome | Cheaper ring dome alt to RR6; saves ~£20 |
| RD2 | SB12PFCR25-4 | SB21SDC-C000-4 | 1,440–2,730 | 107 | ~40 | 24V | Warm + ring dome | Cheapest ring dome pairing; 92mm FP vs 104mm SB29 |
| RD3 | SB12MNRX2-25-4 | SB21SDC-C000-4 | 1,440–2,730 | 107 | ~73 | 24V | Warm + ring dome | Engineering: smaller ring dome; saves £5 vs S3 |
| XC1 | DSA90-8 | XT25SC40-04 | 2,036–3,260 | **68** | ~47 | 24V | Detailed + wide | ABSOLUTE MINIMUM spacing (68 mm); ring rad dispersion |
| XC2 | DS115-8 | XT25SC40-04 | 2,036–2,636 | 80 | ~55 | 24V | Warm + wide | Paper warmth + ultra-compact ring rad; ~600 Hz xover window |
| XC3 | SB12PFCR25-4 | XT25SC40-04 | 2,036–2,730 | 83 | ~44 | 24V | Warm + wide | Best value ultra-compact ring rad; nat. fibre + 43.9mm ring rad |
| TN1 | DSA90-8 | HiVi TN28-B | 2,600–3,260 | 70 | ~40 | 24V | Detailed | 2nd tightest round spacing (70mm); narrow xover window |
| TN2 | DS115-8 | HiVi TN28-B | 2,600–2,636 | 82 | ~45 | 24V | Warm | Only 36 Hz xover window — risky; confirm Fs |
| DA1 | DS115-8 | DA25BG08-06 | 1,420–2,636 | 110 | ~52 | 24V | Warm, flexible | Peerless dome; same FP as DX25; wide xover window |
| DA2 | SB12PFCR25-4 | DA25BG08-06 | 1,420–2,730 | 113 | ~43 | 24V | Warm, flexible | Best value wide-window pairing; cheaper than A5 (DX25) |
| R1 | RS125-4 | DX25TG59-04 | 1,180–2,184 | 115 | ~78 | 24V | Neutral-bright | Premium 5" Al; 4Ω; needs DX25 (beams above 2184 Hz) |
| R2 | RS125-4 | XT25TG30-04 | 880–2,184 | 115 | ~85 | 24V | Neutral + wide | Premium 5" + ring rad; widest window possible for 5" |
| R3 | SB13PFCR25-4 | DX25TG59-04 | 1,180–2,080 | 117 | ~42 | 24V | Warm, nat. fibre | Cheaper 5" option vs R1 at same crossover constraint |
| COAX2 | SB12PFC25-4-COAX | (built-in) | ~2,800 | 0 | ~46 | 24V | Warm | Nat. fibre coaxial; cheaper than B9; same SPL ceiling ~94 dB |

---

## Supplier Notes (June 2026)

- **SoundImports** (EU) — primary source for most drivers
- **Falcon Acoustics** (UK) — SB19ST £14.30, XT25TG30-04 £29.90, XT25SC90-04 £18.20, DX25TG59-04 £20.85
- **Audiophonics** (France) — SIG120-4 in stock, ships to UK
