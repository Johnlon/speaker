# Driver Combination Spreadsheet

Exhaustive record of every evaluated mid+tweeter pairing. One row per combination. Per-driver data (sensitivity, power, Fs, etc.) is in [drivers.md](drivers.md). Curated recommendations are in [solutions.html](solutions.html).

---

## System Reference

- Sub at 40W RMS → **98 dB @1m** (continuous) | Sub at 80W → **101 dB @1m** (burst)
- JAB5: P = V²/(2R) × 0.85 | 24V → 31W/8Ω, 61W/4Ω | 28V → 42W/8Ω, 84W/4Ω | 29V → 45W/8Ω, 89W/4Ω
- Sub/mid crossover: ~150 Hz (LR24). Mid/tweeter crossover: no fixed target — set by the chosen drivers (mid beaming limit upper, 2× tweeter Fs lower). Per-pairing window recorded in the Xover Hz column.

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
| H1189-06 | 1,100 Hz | 103.8 | 90 | **90** |
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
| SEAS H1211-06 | 1,800 Hz | 103.8 | 91 | 90 |
| SEAS H1318-06 | 1,900 Hz | 103.8 | 92 | 90 |
| Morel CAT-298 | 1,800 Hz | 104 | 89 | 80 |
| D3004/602010 | 850 Hz | 62 | 89.6 | 50 |

---

## All Pairings

PSU = "RMS min / Burst min". `*` = mid reaches ~100.3 dB max even at 36V (JAB5 ceiling) — 1 dB short of sub burst.

| ID | Mid | Tweeter | Xover Window (Hz) | Best Cross (Hz) | Spacing mm | Price £ | PSU V/A/W (RMS/Burst) | Character | Flags / Notes |
|----|-----|---------|-------------------|-----------------|------------|---------|-----------------|-----------|---------------|
| S1 | DS115-8 | SB19ST | 1,960–2,636 | 2,500 | 102 | £46 | 24V/3.7A/88W / 28V/4.7A/130W | Warm | DS115-8 £31.41 (SI €36.95); SB19ST £14.30 (Falcon); 4 units left |
| S2 | SB12PFCR25-4 | SB19ST | 1,960–2,730 | 2,700 | 105 | £35 | 24V/3.8A/92W / 28V/4.8A/134W | Warm, natural | Best value; SB12PFCR £20.58 + SB19ST £20.14 Willys (both UK stock) |
| S3 | SB12MNRX2-25-4 | SB29SDAC | 1,200–2,700 | 2,500 | ~107 | £82 | 24V/2.8A/68W / 28V/3.9A/110W | Warm-neutral | Ring dome; wide xover window; MNRX2 £48.10 + SB29SDAC £34.30 Willys |
| A1 | HiVi B4N | SB19ST | 1,960–2,636 | 2,500 | 102 | £33 | 24V/3.7A/90W / 28V/4.7A/132W | Warm | HiVi B4N £19.08 (SI €22.45); SB19ST £14.30 (Falcon); Zero DSP correction; 10+ stock; Fs 66.3 Hz (2.26× margin) |
| A2 | SB12MNRX2-25-4 | SB19ST | 1,960–2,730 | 2,700 | 105 | £62 | 24V/3.3A/80W / 28V/4.4A/122W | Warm, dynamic | Controlled transients; MNRX2 £48.10 + SB19ST £20.14 Willys |
| A3 | DSA90-8 | SB19ST | 1,960–3,260 | 2,500 | 90 | £44 | 24V/3.8A/91W / 29V/4.6A/134W | Detailed | DSA90-8 £29.71 (SI €34.95); SB19ST £14.30 (Falcon); Tightest round spacing |
| A4 | DS115-8 | DX25TG59-04 | 1,800–2,500 | 2,500 | 110 | £50 | 24V/3.2A/76W / 28V/4.2A/118W | Warm, flexible | Widest xover window (std dome); DX25 £18.44 Willys (was ~£28 SI) |
| A5 | SB12PFCR25-4 | DX25TG59-04 | 1,800–2,700 | 2,500 | 110 | £39 | 24V/3.3A/80W / 28V/4.4A/122W | Warm, flexible | A4 at lower cost; DX25 £18.44 + SB12PFCR £20.58 both Willys |
| A6 | Beyma 4FR40 | SB19ST | 1,960–2,600 | 2,500 | 103 | £41 | 24V/3.4A/82W / 28V/4.4A/124W | Warm | Beyma 4FR40 £26.31 (SI €30.95); SB19ST £14.30 (Falcon); Confirm Fs before ordering |
| A7 | SPM-116/8 | SB19ST | 1,960–2,600 | 2,500 | 102 | £33 | 24V/3.4A/82W / 32V/4.0A/126W | Warm | SPM-116/8 £18.23 (SI €21.45); SB19ST £14.30 (Falcon); Cheapest paper mid; 84 dB sens → mid-limited at burst |
| A8 | SIG120-4 | SB19ST | 1,960–2,570 | 2,500 | 105 | ~48 | 24V/3.5A/83W / 28V/4.5A/125W | Clear, dynamic | 4Ω; Audiophonics FR only |
| B1 | TCP115-8 | SB19ST | 1,960–2,570 | 2,500 | 102 | £29 | 28V/4.0A/113W / 36V/4.3A/157W* | Warmest | TCP115-8 £14.41 (SI €16.95); SB19ST £14.30 (Falcon); Cheapest drivers; mid maxes at ~100.3 dB at 36V |
| B2 | ND91-4 | SB19ST | 1,960–3,000 | 2,700 | 97 | £43 | 24V/4.4A/105W / 28V/5.2A/147W | Detailed | ND91-4 £28.86 (SI €33.95); SB19ST £14.30 (Falcon); Confirm Fs before ordering |
| B3 | HiVi M5N | DX25TG59-04 | 1,200–2,100 | 1,650 | ~103 | £44 | 24V/2.9A/70W / 28V/4.0A/112W | Warm | 5"; DX25 needed (not SB19ST); DX25 £18.44 Willys |
| B4 | SB13PFC25-8 | DX25TG59-04 | 1,200–2,080 | 1,640 | ~110 | ~43 | 24V/2.9A/70W / 28V/4.0A/112W | Warm | Best Fs margin; 5" natural fibre; DX25 £18.44 Willys |
| B5 | DA115-8 | SB19ST | 1,960–2,600 | 2,500 | 102 | £35 | 24V/3.8A/90W / 28V/4.7A/132W | Detailed | DA115-8 £21.04 (SI €24.75); SB19ST £14.30 (Falcon); Near-perfect sensitivity match; 3 left; DA115 on sale €24.75 (Jun 2026) |
| B6 | DSA90-8 | HiVi TN25 | 3,000–3,260 | 3,000 | 73 | £51 | 24V/3.4A/81W / 29V/4.3A/124W | Detailed | DSA90-8 £29.71 (SI €34.95); HiVi TN25 £21.63 (SI €25.45); Tightest spacing; square tweeter; TN25 depth 63.5mm — check clearance |
| B7 | SDS-P830656 | DX25TG59-04 | 1,500–2,000 | 1,750 | ~105 | £44 | 24V/3.1A/73W / 28V/4.1A/115W | Natural | Xmax 10mm; truncated frame; DX25 £18.44 Willys |
| B8 | SIG150-4 | DX25TG59-04 | 1,500–1,990 | 1,745 | 128 | £57 | 24V/2.8A/68W / 28V/3.9A/110W | Neutral | 152mm OD — wide baffle; poor 60° off-axis; DX25 £18.44 Willys |
| B9 | SB12PACR25-4-COAX | (built-in) | 2,600–2,730 | 2,665 | 0 | £53 | 24V/4.2A/100W / 28V/5.1A/142W | Clear | SB12PACR25-4-COAX £52.53 (Willys); Point source; max SPL ~94 dB — sub must be limited |
| B10 | DSA90-8 | ND25FA-4 | 2,700–3,260 | 2,700 | 79 | £48 | 24V/3.6A/86W / 29V/4.4A/128W | Detailed | DSA90-8 £29.71 (SI €34.95); ND25FA-4 £18.23 (SI €21.45); Minimum round spacing |
| B11 | DSA90-8 | DT-28N | 2,400–3,260 | 2,500 | ~82 | £65 | 24V/3.2A/76W / 29V/4.1A/118W | Detailed | DSA90-8 £29.71 (SI €34.95); DT-28N £34.81 (SI €40.95); Compact waveguide |
| B12 | SLS-85S25CP04-04 | DT-28N | 2,400–3,000 | 2,500 | ~82 | £60 | 24V/3.6A/86W / 28V/4.6A/128W | Warm | SLS-85S25CP04-04 £25.46 (SI €29.95); DT-28N £34.81 (SI €40.95); Oval mid; 86 dB → sub-limited at burst |
| RR1 | DS115-8 | XT25TG30-04 | 880–2,636 | 2,500 | 113 | £61 | 24V/3.3A/79W / 28V/4.3A/121W | Warm + wide | DS115-8 £31.41 (SI €36.95); XT25TG30-04 £29.90 (Falcon); Best ring radiator; widest xover window |
| RR2 | SB12PFCR25-4 | XT25TG30-04 | 880–2,730 | 2,500 | 116 | £50 | 24V/3.4A/83W / 28V/4.4A/125W | Warm + wide | Best value ring radiator; SB12PFCR £20.58 Willys + XT25TG30 £29.90 Falcon |
| RR3 | SB12MNRX2-25-4 | XT25TG30-04 | 880–2,730 | 2,500 | 116 | £78 | 24V/2.9A/70W / 28V/4.0A/112W | Warm + wide | Ring radiator + highest headroom; MNRX2 £48.10 Willys; XT25TG30 £29.90 Falcon |
| RR4 | DSA90-8 | XT25SC90-04 | 1,650–3,260 | 2,500 | 91 | £48 | 24V/3.6A/86W / 29V/4.4A/128W | Detailed + wide | Cheapest ring radiator; XT25SC90 £18.20 Falcon / £19.52 Willys |
| RR4B | SB12PFCR25-4 | XT25SC90-04 | 1,650–2,730 | 2,500 | 106 | £39 | 24V/3.6A/87W / 28V/4.6A/129W | Warm + wide | Cheapest ring rad + nat. fibre; SB12PFCR £20.58 + XT25SC90 £19.52 Willys |
| RR4C | DS115-8 | XT25SC90-04 | 1,650–2,636 | 2,500 | 103 | £50 | 24V/3.5A/83W / 28V/4.5A/125W | Warm + wide | Paper warmth + ring rad; XT25SC90 £18.20 Falcon / £19.52 Willys |
| RR5 | SIG150-4 | XT25TG30-04 | 1,000–1,990 | 1,495 | 140 | £68 | 24V/2.9A/70W / 28V/4.0A/112W | Neutral | SIG150-4 £38.21 (SI €44.95); XT25TG30-04 £29.90 (Falcon); Only tweeter that works with SIG150-4 |
| RR6 | DS115-8 | SB29SDAC | 1,200–2,636 | 2,500 | ~110 | £66 | 24V/3.2A/77W / 28V/4.2A/119W | Warm + ring dome | DS115-8 £31.41 (SI €36.95); SB29SDAC £34.30 (Willys); Ring dome + paper warmth |
| C1 | RS100-8 | SB19ST | 1,960–2,900 | 2,500 | — | £56 | 24V/3.8A/92W / 29V/4.6A/134W | Detailed | RS100-8 £41.61 (SI €48.95); SB19ST £14.30 (Falcon); Fs 1.63× at 150 Hz — marginal; 84.6 dB → mid-limited at burst |
| C2 | PA130-8 | SB19ST | 1,960–2,000 | 2,000 | — | £43 | 24V/3.3A/79W / 28V/4.3A/121W | Natural | PA130-8 £28.43 (SI €33.45); SB19ST £14.30 (Falcon); Xmax 2mm; Fs 1.8×; OD 132mm |
| C3 | TF0510 | SB19ST | 1,960–2,200 | 2,200 | — | ~45 | 24V/3.1A/75W / 28V/4.2A/117W | Natural | Weakest Fs (1.42×) + Xmax (1.1mm) |
| C4 | DSA90-8 | Markaudio TW 6 | 3,200–3,400 | 3,300 | — | £68 | 24V/3.1A/75W / 29V/4.1A/118W | Detailed | DSA90-8 £29.71 (SI €34.95); Markaudio TW 6 £38.21 (SI €44.95); Xover above mid beaming limit; poor 60° |
| NR1 | DSA90-8 | NE25VTS-04 | 1,460–3,260 | 2,500 | 79 | £64 | 24V/3.5A/83W / 29V/4.3A/126W | Detailed | DSA90-8 £29.71 (SI €34.95); NE25VTS-04 £33.96 (SI €39.95); Same spacing as B10; much lower min xover (1,460 vs 2,700 Hz) |
| NR2 | DS115-8 | NE25VTS-04 | 1,460–2,636 | 2,500 | 91 | £65 | 24V/3.4A/80W / 28V/4.4A/122W | Warm | DS115-8 £31.41 (SI €36.95); NE25VTS-04 £33.96 (SI €39.95); Wide xover window; paper warmth + compact tweeter |
| NR3 | SB12PFCR25-4 | NE25VTS-04 | 1,460–2,730 | 2,500 | ~94 | £55 | 24V/3.5A/84W / 28V/4.5A/126W | Warm, natural | SB12PFCR25-4 £20.58 (Willys); NE25VTS-04 £33.96 (SI €39.95); NR2 at lower cost with nat. fibre mid |
| RD0 | DSA90-8 | SB21SDC-C000-4 | 1,440–3,260 | 2,500 | 92 | £58 | 24V/3.5A/83W / 29V/4.3A/126W* | Detailed + ring dome | DSA90-8 £29.71 (SI €34.95); SB21SDC-C000-4 £28.51 (Willys); Widest ring dome window (1,820Hz!); 92mm spacing; compact detailed mid + ring dome; 29V for burst |
| RD1 | DS115-8 | SB21SDC-C000-4 | 1,440–2,636 | 2,500 | 104 | £60 | 24V/3.4A/81W / 28V/4.4A/123W | Warm + ring dome | DS115-8 £31.41 (SI €36.95); SB21SDC-C000-4 £28.51 (Willys); Ring dome alt to RR6; saves ~£6; 92mm FP tighter than SB29 |
| RD2 | SB12PFCR25-4 | SB21SDC-C000-4 | 1,440–2,730 | 2,500 | 107 | £49 | 24V/3.5A/84W / 28V/4.5A/126W | Warm + ring dome | SB12PFCR25-4 £20.58 (Willys); SB21SDC-C000-4 £28.51 (Willys); Cheapest ring dome pairing; nat. fibre + smaller SB21 ring dome |
| RD3 | SB12MNRX2-25-4 | SB21SDC-C000-4 | 1,440–2,730 | 2,500 | 107 | £77 | 24V/3.0A/72W / 28V/4.1A/114W | Warm + ring dome | Engineering ring dome; MNRX2 £48.10 + SB21SDC £28.51 Willys |
| TN1 | DSA90-8 | HiVi TN28-B | 2,600–3,260 | 2,930 | 70 | £55 | 24V/3.4A/82W / 29V/4.3A/124W | Detailed | DSA90-8 £29.71 (SI €34.95); HiVi TN28-B £25.46 (SI €29.95); 2nd tightest round spacing (70mm); narrow xover window |
| TN2 | DS115-8 | HiVi TN28-B | 2,600–2,636 | 2,618 | 82 | £57 | 24V/3.3A/79W / 28V/4.3A/121W | Warm | DS115-8 £31.41 (SI €36.95); HiVi TN28-B £25.46 (SI €29.95); Only 36 Hz xover window — risky; likely unusable |
| DA1 | DS115-8 | DA25BG08-06 | 1,420–2,636 | 2,500 | 110 | £65 | 24V/3.2A/76W / 28V/4.2A/118W | Warm, flexible | DS115-8 £31.41 (SI €36.95); DA25BG08-06 £33.96 (SI €39.95); Peerless dome; same FP as DX25; wide xover window |
| DA2 | SB12PFCR25-4 | DA25BG08-06 | 1,420–2,730 | 2,500 | 113 | £55 | 24V/3.3A/80W / 28V/4.4A/122W | Warm, flexible | SB12PFCR25-4 £20.58 (Willys); DA25BG08-06 £33.96 (SI €39.95); Wide-window pairing; ~£5 cheaper than A5 (DX25) |
| R1 | RS125-4 | DX25TG59-04 | 1,180–2,184 | 1,682 | 115 | £75 | 24V/2.9A/71W / 28V/4.0A/113W | Neutral-bright | Premium 5" Al; 4Ω; needs DX25 (beams above 2184 Hz); DX25 £18.44 Willys |
| R2 | RS125-4 | XT25TG30-04 | 880–2,184 | 1,532 | 115 | £87 | 24V/3.0A/73W / 28V/4.1A/115W | Neutral + wide | RS125-4 £56.91 (SI €66.95); XT25TG30-04 £29.90 (Falcon); Premium 5" + ring rad; widest window possible for 5" |
| R3 | SB13PFCR25-4 | DX25TG59-04 | 1,180–2,080 | 1,630 | 117 | £43 | 24V/3.1A/74W / 28V/4.1A/116W | Warm, nat. fibre | Cheaper 5" option vs R1; DX25 £18.44 + SB13PFCR £24.50 both Willys |
| COAX2 | SB12PFC25-4-COAX | (built-in) | 2,600–2,730 | 2,665 | 0 | £48 | 24V/4.0A/97W / 28V/5.0A/139W | Warm | SB12PFC25-4-COAX £48.41 (SI €56.95); Nat. fibre coaxial; cheaper than B9 (£59); same SPL ceiling ~94 dB |
| ST1 | DS115-8 | SB26ST-C000-5 | 1,740–2,636 | 2,500 | 94 | £57 | 24V/3.3A/79W / 28V/4.3A/121W | Warm | DS115-8 £31.41 (SI €36.95); SB26ST-C000-5 £25.30 (Willys); 80W tweeter; ~72mm FP (assume); wide window; robust power handling |
| ST2 | SB12PFCR25-4 | SB26ST-C000-5 | 1,740–2,730 | 2,500 | 97 | £46 | 24V/3.4A/82W / 28V/4.4A/124W | Warm, nat. | SB12PFCR25-4 £20.58 (Willys); SB26ST-C000-5 £25.30 (Willys); Cheapest 80W tweeter pairing; nat. fibre + indestructible tweeter |
| ST3 | DSA90-8 | SB26ST-C000-5 | 1,740–3,260 | 2,500 | 82 | £55 | 24V/3.4A/81W / 28V/4.4A/123W | Detailed | DSA90-8 £29.71 (SI €34.95); SB26ST-C000-5 £25.30 (Willys); 82mm spacing; 80W tweeter; widest xover window of any DSA90-8 pairing |
| NX1 | SB12NRX25-4 | SB19ST | 1,960–2,730 | 2,500 | ~105 | £60 | 24V/3.8A/92W / 28V/4.8A/134W | Warm, nat. | SB12NRX25-4 £45.75 (Willys); SB19ST £14.30 (Falcon); Premium paper NRX; acoustically identical to S2 (SB12PFCR25-4) — choose S2 on value |
| NX2 | SB12NRX25-4 | XT25TG30-04 | 880–2,730 | 2,500 | ~116 | £76 | 24V/3.4A/83W / 28V/4.4A/125W | Warm + wide | SB12NRX25-4 £45.75 (Willys); XT25TG30-04 £29.90 (Falcon); Premium NRX + ring rad; acoustically identical to RR2 — choose RR2 on value |
| PL1 | PLUVIA-7HD Gold | SB19ST | 1,960–~2,900 | 1960–~2900 | ~105 | £59 | 24V/3.6A/87W / 28V/4.6A/129W | Warm, zero-pad | PLUVIA-7HD Gold £44.58 (SI €52.45); SB19ST £14.30 (Falcon); Unique zero-correction mid; system SPL capped 97 dB (DSP at 18W); Mg/Al cone |
| DC1 | DS115-8 | D2604/830000 | 1,260–2,636 | 2,500 | 110 | £64 | 24V/3.3A/79W / 28V/4.3A/121W | Warm, 100W | Scan-Speak 100W dome; **Falcon £33.05** (vs SI €44.95); same spacing as DA1 but wider window + indestructible tweeter |
| DC2 | SB12PFCR25-4 | D2604/830000 | 1,260–2,730 | 2,500 | 113 | £54 | 24V/3.4A/82W / 28V/4.4A/124W | Warm, nat. 100W | Cheapest 100W wide-window pairing; nat. fibre + Scan-Speak 100W; **Falcon £33.05** |
| SE1 | DSA90-8 | SEAS H1406-04 | 2,340–3,260 | 2,500 | ~75 | £63 | 24V/3.5A/83W / 28V/4.5A/125W | Detailed | DSA90-8 £29.71 (SI €34.95); SEAS H1406-04 £33.66 (HFC); **⚠ H1406-04 OOS (Jun 2026)** — pre-order only. 80W oval tweeter; 73mm portrait spacing; on sale €40.45 |
| SE2 | DS115-8 | SEAS H1406-04 | 2,340–2,636 | 2,500 | ~85 | £65 | 24V/3.4A/81W / 28V/4.4A/123W | Warm | DS115-8 £31.41 (SI €36.95); SEAS H1406-04 £33.66 (HFC); **⚠ H1406-04 OOS** — pre-order only. SEAS 80W; only 296Hz window — very tight; not recommended even if restocked |
| CF1 | DSA90-8 | CF18N-4 | 2,200–3,260 | 2,500 | **75** | £61 | 24V/3.6A/86W / 28V/4.6A/128W | Detailed, CF | DSA90-8 £29.71 (SI €34.95); CF18N-4 £31.41 (SI €36.95); **⚠ CF18N-4 OOS (Jun 2026)** — pre-order only. 18mm CF dome; on sale €30.54; monitor for restock |
| CF2 | DS115-8 | CF18N-4 | 2,200–2,636 | 2,500 | 87 | £63 | 24V/3.5A/83W / 28V/4.5A/125W | Warm, CF | DS115-8 £31.41 (SI €36.95); CF18N-4 £31.41 (SI €36.95); **⚠ CF18N-4 OOS** — pre-order only. Carbon fibre dome; 40W; paper warmth + CF detail |
| CF3 | SB12PFCR25-4 | CF18N-4 | 2,200–2,730 | 2,500 | 90 | £52 | 24V/3.6A/87W / 28V/4.6A/129W | Warm nat., CF | SB12PFCR25-4 £20.58 (Willys); CF18N-4 £31.41 (SI €36.95); **⚠ CF18N-4 OOS** — pre-order only. Best value CF dome; 40W; monitor for restock |
| TD1 | DSA90-8 | TD25F-4 | 1,800–3,260 | 2,500 | 93 | £55 | 24V/3.5A/83W / 28V/4.5A/125W | Detailed | DSA90-8 £29.71 (SI €34.95); TD25F-4 £25.46 (SI €29.95); Semi-horn 93.5mm FP; wide xover window; note semi-horn narrows HF off-axis |
| TD2 | DS115-8 | TD25F-4 | 1,800–2,636 | 2,500 | 105 | £57 | 24V/3.4A/81W / 28V/4.4A/123W | Warm | DS115-8 £31.41 (SI €36.95); TD25F-4 £25.46 (SI €29.95); Semi-horn + paper warmth; wide window (836Hz) but semi-horn off-axis concern |
| DT1 | DS115-8 | D27TG35-06 | 1,800–2,636 | 2,500 | 110 | £59 | 24V/3.2A/76W / 28V/4.2A/118W | Warm, 6Ω | DS115-8 £31.41 (SI €36.95); D27TG35-06 £27.52 (Willys); 6Ω tweeter; 104mm FP; same spacing as DA1; 15W (adequate at 10.5W burst) |
| DT2 | SB12PFCR25-4 | D27TG35-06 | 1,800–2,730 | 2,500 | 113 | £48 | 24V/3.3A/80W / 28V/4.4A/122W | Warm nat., 6Ω | SB12PFCR25-4 £20.58 (Willys); D27TG35-06 £27.52 (Willys); 6Ω; same class as DA2 at same price; DA25 wins on Fs (710 vs 900Hz) |
| BC1 | DSA90-8 | BC25SC06-04 | 2,700–3,260 | 2,980 | 81 | £46 | 24V/3.2A/77W / 29V/4.1A/120W | Detailed | DSA90-8 £29.71 (SI €34.95); BC25SC06-04 £16.78 (Willys); 50W tweeter; 95.4dB → only 1.8W at ref / 3.6W burst; FP ~70mm (est); 81mm spacing |
| BC2 | DS115-8 | BC25SC06-04 | 2700 (Fixed) | 2,700 | 93 | £48 | 24V/3.1A/74W / 28V/4.2A/116W | Warm | DS115-8 £31.41 (SI €36.95); BC25SC06-04 £16.78 (Willys); Xover at DS115 beaming limit (2636Hz) — marginally tight; on-axis only |
| BC3 | SB12PFCR25-4 | BC25SC06-04 | 2,700–2,730 | 2,715 | 96 | £37 | 24V/3.3A/78W / 28V/4.3A/120W | Warm, nat. | SB12PFCR25-4 £20.58 (Willys); BC25SC06-04 £16.78 (Willys); 30Hz xover window only — fixed at ~2,715Hz; cheapest 50W nat. fibre pairing |
| STC1 | DSA90-8 | SB26STCN-C000-4 | 1,900–3,260 | 2,500 | 82 | £59 | 24V/3.4A/81W / 29V/4.3A/124W | Detailed | DSA90-8 £29.71 (SI €34.95); SB26STCN-C000-4 £28.92 (Willys); 120W indestructible; 82mm spacing; 1360Hz DSP window; burnout impossible at 29V |
| STC2 | DS115-8 | SB26STCN-C000-4 | 1,900–2,636 | 2,500 | 94 | £60 | 24V/3.3A/79W / 28V/4.3A/121W | Warm | DS115-8 £31.41 (SI €36.95); SB26STCN-C000-4 £28.92 (Willys); 120W + paper warmth; 736Hz window; best power safety for DS115 pairing |
| STC3 | SB12PFCR25-4 | SB26STCN-C000-4 | 1,900–2,730 | 2,500 | 97 | £50 | 24V/3.4A/82W / 28V/4.4A/124W | Warm, nat. | SB12PFCR25-4 £20.58 (Willys); SB26STCN-C000-4 £28.92 (Willys); Best value 120W pairing; nat. fibre + indestructible tweeter; 830Hz window |
| AL1 | DS115-8 | SB26ADC-C000-4 | 1,360–2,636 | 2,500 | 110 | £73 | 24V/3.5A/83W / 28V/4.5A/125W | Warm + bright Al | DS115-8 £31.41 (SI €36.95); SB26ADC-C000-4 £41.60 (Willys); 120W Al dome; same FP class as D2604; wider window (1360 vs 1260Hz min); €7 more |
| AL2 | SB12PFCR25-4 | SB26ADC-C000-4 | 1,360–2,730 | 2,500 | 113 | £62 | 24V/3.6A/87W / 28V/4.6A/129W | Warm nat. + Al | SB12PFCR25-4 £20.58 (Willys); SB26ADC-C000-4 £41.60 (Willys); 120W Al dome + nat. fibre; warm-bright hybrid |
| RPN1 | DS115-8 | SB29RDNC-C000-4 | 1,160–2,636 | 2,500 | 110 | £86 | 24V/3.2A/76W / 28V/4.2A/118W | Warm + ring dome 100W | DS115-8 £31.41 (SI €36.95); SB29RDNC-C000-4 £54.31 (Willys); Premium ring dome; 1,476Hz DSP window; 94dB → only 5W at burst; 100W = burnout impossible |
| RPN2 | SB12PFCR25-4 | SB29RDNC-C000-4 | 1,160–2,730 | 2,500 | 113 | £75 | 24V/3.3A/79W / 28V/4.3A/121W | Warm nat. + ring dome 100W | SB12PFCR25-4 £20.58 (Willys); SB29RDNC-C000-4 £54.31 (Willys); Widest ring dome window in catalogue (1,570Hz); nat. fibre + premium ring dome |
| RPN3 | SB12MNRX2-25-4 | SB29RDNC-C000-4 | 1,160–2,730 | 2,500 | 113 | £102 | 24V/2.8A/67W / 28V/3.9A/109W | Warm + ring dome 100W | Engineering flagship; MNRX2 £48.10 + SB29RDNC £54.31 Willys |
| RPN4 | DSA90-8 | SB29RDNC-C000-4 | 1,160–3,260 | 2,500 | 98 | £84 | 24V/3.3A/78W / 29V/4.2A/121W | Detailed + ring dome 100W | DSA90-8 £29.71 (SI €34.95); SB29RDNC-C000-4 £54.31 (Willys); Widest window of any DSA90-8 pairing (2,100Hz); 98mm spacing; premium compact option |
| RST1 | DS115-8 | RST28F-4 | 1,420–2,636 | 2,500 | 110 | £71 | 24V/3.2A/76W / 28V/4.2A/118W | Warm + 80W | DS115-8 £31.41 (SI €36.95); RST28F-4 £39.91 (SI €46.95); 80W; 93.5dB → 5.6W at burst; same spacing as DC1; +£7 over D2604 (Falcon) |
| RST2 | SB12PFCR25-4 | RST28F-4 | 1,420–2,730 | 2,500 | 113 | £60 | 24V/3.3A/80W / 28V/4.4A/122W | Warm nat. + 80W | SB12PFCR25-4 £20.58 (Willys); RST28F-4 £39.91 (SI €46.95); 80W; wider window than STC3 (SB26STCN); lower sensitivity match (+6dB vs +7dB DSP pad) |
| RST3 | DSA90-8 | RST28F-4 | 1,420–3,260 | 2,500 | 98 | £70 | 24V/3.3A/79W / 29V/4.2A/122W | Detailed + 80W | DSA90-8 £29.71 (SI €34.95); RST28F-4 £39.91 (SI €46.95); 1,840Hz window; 98mm spacing; 80W insurance at 29V |
| D26_1 | DSA90-8 | D2606/920000 | 2,200–3,260 | 2,500 | 98 | £59 | 24V/3.3A/79W / 29V/4.2A/122W | Detailed + 100W 6Ω | 1,060Hz window; 6Ω; 100W; **Falcon £29.35**; compact 98mm spacing |
| D26_2 | DS115-8 | D2606/920000 | 2,200–2,636 | 2,500 | 110 | £61 | 24V/3.2A/77W / 28V/4.2A/119W | Warm + 100W 6Ω | 436Hz window — tight; **Falcon £29.35**; cross at DS115 beaming limit; 6Ω |
| D26_3 | SB12PFCR25-4 | D2606/920000 | 2,200–2,730 | 2,500 | 113 | £50 | 24V/3.4A/81W / 28V/4.4A/123W | Warm nat. + 100W 6Ω | 530Hz window; **Falcon £29.35** = cheapest 100W tweeter in catalogue |
| SB13_TG | SB13PFCR25-4 | XT25TG30-04 | 880–2,080 | 1,480 | 117 | £54 | 24V/3.2A/76W / 28V/4.2A/118W | Warm, nat. + wide | 5"; Fs=44Hz (3.4× margin); 1,200Hz ring rad window; SB13PFCR £24.50 Willys + XT25TG30 £29.90 Falcon |
| SB13_DC | SB13PFCR25-4 | D2604/830000 | 1,260–2,080 | 1,670 | 117 | £58 | 24V/3.2A/76W / 28V/4.2A/118W | Warm, nat. + 100W | 5" + Scan-Speak 100W; SB13PFCR £24.50 Willys + D2604 £35.65 Willys |
| SB13_RPN | SB13PFCR25-4 | SB29RDNC-C000-4 | 1,160–2,080 | 1,620 | 117 | £79 | 24V/3.0A/73W / 28V/4.1A/115W | Warm nat. + ring dome | 5"; 920Hz window; 100W ring dome; SB13PFCR £24.50 + SB29RDNC £54.31 Willys |
| M_TG | HiVi M5N | XT25TG30-04 | 880–2,185 | 1,532 | 115 | £55 | 24V/3.0A/73W / 28V/4.1A/115W | Warm + wide | HiVi M5N £25.46 (SI €29.95); XT25TG30-04 £29.90 (Falcon); 5"; best Fs margin (50Hz); 1,305Hz window; widest M5N option; 190mm baffle OK |
| M_RPN | HiVi M5N | SB29RDNC-C000-4 | 1,160–2,185 | 1,672 | 115 | £80 | 24V/2.9A/70W / 28V/4.0A/112W | Warm + ring dome | HiVi M5N £25.46 (SI €29.95); SB29RDNC-C000-4 £54.31 (Willys); 5"; 1,025Hz window; 100W ring dome; 190mm baffle OK |
| B_TG | HiVi B4N | XT25TG30-04 | 880–2,636 | 2,500 | 110 | £49 | 24V/3.3A/80W / 28V/4.4A/122W | Warm gold + wide | HiVi B4N £19.08 (SI €22.45); XT25TG30-04 £29.90 (Falcon); Perfect sub sens match (85dB); widest B4N window (1,756Hz); ring rad; single order Falcon+SI |
| B_STC | HiVi B4N | SB26STCN-C000-4 | 1,900–2,636 | 2,500 | 94 | £48 | 24V/3.3A/80W / 28V/4.4A/122W | Warm gold + 120W | HiVi B4N £19.08 (SI €22.45); SB26STCN-C000-4 £28.92 (Willys); Cheapest 120W pairing (~£50); 94mm spacing; zero DSP correction needed at 85dB |
| B_DC | HiVi B4N | D2604/830000 | 1,260–2,636 | 2,500 | 110 | £52 | 24V/3.3A/80W / 28V/4.4A/122W | Warm gold + 100W | HiVi B4N £19.08 (SI €22.45); D2604/830000 £33.05 (Falcon); Scan-Speak 100W; widest window for B4N standard dome (1,376Hz); DS115 replacement |
| DA_TG | DA115-8 | XT25TG30-04 | 880–2,636 | 2,500 | 110 | £51 | 24V/3.4A/81W / 28V/4.4A/123W | Al + ring rad | DA115-8 £21.04 (SI €24.75); XT25TG30-04 £29.90 (Falcon); Ring rad + Al; 3 left — order now; widest Al-mid window (1,756Hz); DA115 sale €24.75 |
| DA_STC | DA115-8 | SB26STCN-C000-4 | 1,900–2,636 | 2,500 | 94 | £50 | 24V/3.3A/80W / 28V/4.4A/122W | Al + 120W | DA115-8 £21.04 (SI €24.75); SB26STCN-C000-4 £28.92 (Willys); 120W + Al cone; 3 left; 94mm spacing; DA115 sale → ~£52 now |
| DMA1 | DMA105-8 | SB19ST | 1,960–2,900 | 2,500 | 96 | £37 | 24V/3.8A/91W / 28V/4.7A/133W | Al neodymium | DMA105-8 £22.48 (SI €26.45); SB19ST £14.30 (Falcon); 4" dual-neo Al cone; beaming 2,900Hz (better than DS115 at 2,636); **min LP 200Hz recommended** (Fs 72Hz → 2×Fs=144Hz marginal at 150); 35W rated (better than DA115 at 20W); 940Hz window |
| DMA2 | DMA105-8 | XT25TG30-04 | 880–2,900 | 2,500 | 107 | £52 | 24V/3.4A/81W / 28V/4.4A/123W | Al + ring rad | 2,020Hz DSP window (widest DMA105 pairing); ring rad off-axis; 107mm spacing; Falcon £29.90 for twt saves ~£13; **min LP 200Hz** |
| DMA3 | DMA105-8 | SB29RDNC-C000-4 | 1,160–2,900 | 2,500 | 104 | £77 | 24V/3.2A/78W / 28V/4.3A/120W | Al + ring dome 100W | DMA105-8 £22.48 (SI €26.45); SB29RDNC-C000-4 £54.31 (Willys); 1,740Hz window; premium 100W ring dome; 104mm spacing; compact pairing; **min LP 200Hz** |
| RP1 | DSA90-8 | R2604/833000 | 880–3,260 | 2,500 | 98 | £76 | 24V/3.4A/81W / 29V/4.3A/124W | Detailed + ring rad 100W | **Absolute window champion: 2,380Hz**; **Falcon £45.95**; same Fs as XT25TG30 + 100W; 98mm spacing |
| RP2 | DS115-8 | R2604/833000 | 880–2,636 | 2,500 | 110 | £77 | 24V/3.3A/79W / 28V/4.3A/121W | Warm + ring rad 100W | 1,756Hz window; **Falcon £45.95**; 100W vs XT25TG30 15W; +£16 over RR1 for burnout immunity |
| RP3 | SB12PFCR25-4 | R2604/833000 | 880–2,730 | 2,500 | 113 | £67 | 24V/3.4A/82W / 28V/4.4A/124W | Warm nat. + ring rad 100W | 1,850Hz window; **Falcon £45.95**; nat. fibre + Discovery ring rad; +£16 over RR2 |
| RP4 | DSA90-8 | R2604/832000 | 1,000–3,260 | 2,500 | 98 | £69 | 24V/3.6A/86W / 29V/4.4A/128W | Detailed + ring rad 100W | 2,260Hz window; **Falcon £38.95** (+£9 over XT25TG30); 100W; 120Hz narrower than RP1 |
| RP5 | DS115-8 | R2604/832000 | 1,000–2,636 | 2,500 | 110 | £70 | 24V/3.5A/83W / 28V/4.5A/125W | Warm + ring rad 100W | 1,636Hz window; **Falcon £38.95** (+£9 over XT25TG30); 100W for £9 premium |
| RP6 | SB12PFCR25-4 | R2604/832000 | 1,000–2,730 | 2,500 | 113 | £60 | 24V/3.6A/87W / 28V/4.6A/129W | Warm nat. + ring rad 100W | 1,730Hz window; **Falcon £38.95**; cheapest 100W ring rad + nat. fibre |
| TF1 | DSA90-8 | H1189-06 | 1,100–3,260 | 2,500 | 98 | £87 | 24V/3.4A/82W / 29V/4.3A/124W | Detailed + dome 90W | **2,160Hz window — widest of any standard dome pairing**; **HFC £56.92** (SI €71.86); 98mm spacing; cloth dome character |
| TF2 | DS115-8 | H1189-06 | 1,100–2,636 | 2,500 | 110 | £88 | 24V/3.3A/79W / 28V/4.3A/121W | Warm + dome 90W | 1,536Hz window; wider than DC1 (1,376Hz); **best dome window for DS115 pairing**; HFC £56.92 |
| TF3 | SB12PFCR25-4 | H1189-06 | 1,100–2,730 | 2,500 | 113 | £78 | 24V/3.5A/83W / 28V/4.5A/125W | Warm nat. + dome 90W | 1,630Hz window; 113mm spacing; SEAS cloth dome + nat. fibre; HFC £56.92 |
| D6R1 | DSA90-8 | D2604/833000 | 950–3,260 | 2,500 | 98 | £72 | 24V/3.3A/80W / 29V/4.2A/122W | Detailed + dome 100W | DSA90-8 £29.71 (SI €34.95); D2604/833000 £41.88 (Willys); 2,310Hz window; widest dome window for DSA90; Scan-Speak 100W |
| D6R2 | DS115-8 | D2604/833000 | 950–2,636 | 2,500 | 110 | £73 | 24V/3.2A/77W / 28V/4.2A/119W | Warm + dome 100W | DS115-8 £31.41 (SI €36.95); D2604/833000 £41.88 (Willys); 1,686Hz window; widest dome window for DS115; Scan-Speak 100W |
| D6R3 | SB12PFCR25-4 | D2604/833000 | 950–2,730 | 2,500 | 113 | £62 | 24V/3.4A/81W / 28V/4.4A/123W | Warm nat. + dome 100W | SB12PFCR25-4 £20.58 (Willys); D2604/833000 £41.88 (Willys); 1,780Hz window; widest dome window for SB12; Scan-Speak 100W |
| MDT22_1 | DSA90-8 | MDT22T | 1,300–3,260 | 2,500 | 73 | £77 | 24V/3.4A/81W / 29V/4.3A/124W | Detailed + sq dome | DSA90-8 £29.71 (SI €34.95); MDT22T £47.55 (Willys); 1,960Hz window; 73mm spacing; Morel square dome upgrade |
| MDT22_2 | DS115-8 | MDT22T | 1,300–2,636 | 2,500 | 85 | £79 | 24V/3.3A/79W / 28V/4.3A/121W | Warm + sq dome | DS115-8 £31.41 (SI €36.95); MDT22T £47.55 (Willys); 1,336Hz window; 85mm spacing; Morel sq dome; check 55mm depth |
| MDT22_3 | SB12PFCR25-4 | MDT22T | 1,300–2,730 | 2,500 | 88 | £68 | 24V/3.4A/82W / 28V/4.4A/124W | Warm nat. + sq dome | SB12PFCR25-4 £20.58 (Willys); MDT22T £47.55 (Willys); 1,430Hz window; 88mm spacing; best value square dome upgrade |
| XBG1 | DS115-8 | XT25BG60-04 | 1,140–2,636 | 2,500 | 110 | £69 | 24V/3.2A/78W / 28V/4.3A/120W | Warm + wide | DS115-8 £31.41 (SI €36.95); XT25BG60-04 £37.14 (Willys); Ring rad; SI-stocked (vs XT25TG30 pre-order); widest window std-stock ring rad |
| XBG2 | SB12PFCR25-4 | XT25BG60-04 | 1,140–2,730 | 2,500 | ~110 | £58 | 24V/3.4A/81W / 28V/4.4A/123W | Warm nat. + wide | SB12PFCR25-4 £20.58 (Willys); XT25BG60-04 £37.14 (Willys); SI-stocked ring rad alt to RR2 (XT25TG30 pre-order only at SI); nat. fibre warmth |
| XBG3 | DSA90-8 | XT25BG60-04 | 1,140–3,260 | 2,500 | 98 | £67 | 24V/3.3A/80W / 29V/4.2A/123W | Detailed + wide | DSA90-8 £29.71 (SI €34.95); XT25BG60-04 £37.14 (Willys); Widest xover window of any DSA90-8 pairing; ring rad off-axis |
| XC1 | DSA90-8 | XT25SC40-04 | 2,036–3,260 | 2,500 | 68 | £55 | 24V/3.3A/78W / 29V/4.2A/121W | Detailed + wide | DSA90-8 £29.71 (SI €34.95); XT25SC40-04 £25.46 (SI €29.95); Absolute minimum spacing (68 mm); ring rad dispersion; 100W |
| XC2 | DS115-8 | XT25SC40-04 | 2,036–2,636 | 2,500 | 80 | £57 | 24V/3.2A/76W / 28V/4.2A/118W | Warm + wide | DS115-8 £31.41 (SI €36.95); XT25SC40-04 £25.46 (SI €29.95); Paper warmth + ultra-compact ring rad; ~600 Hz xover window |
| XC3 | SB12PFCR25-4 | XT25SC40-04 | 2,036–2,730 | 2,500 | 83 | £46 | 24V/3.3A/79W / 28V/4.3A/121W | Warm + wide | SB12PFCR25-4 £20.58 (Willys); XT25SC40-04 £25.46 (SI €29.95); Best value ultra-compact ring rad; nat. fibre + 43.9mm ring rad |
| XCR1 | DSA90-8 | SB21RDCN-C000-4 | 1,700–3,260 | 2,500 | 75 | £71 | 24V/3.6A/88W / 29V/4.5A/130W | Detailed + ring dome | DSA90-8 £29.71 (SI €34.95); SB21RDCN-C000-4 £41.60 (Willys); 1,560Hz window; 75mm spacing; most compact ring dome |
| XCR2 | DS115-8 | SB21RDCN-C000-4 | 1,700–2,636 | 2,500 | 87 | £73 | 24V/3.5A/85W / 28V/4.5A/127W | Warm + ring dome | DS115-8 £31.41 (SI €36.95); SB21RDCN-C000-4 £41.60 (Willys); 936Hz window; 87mm spacing; premium compact ring dome |
| XCR3 | SB12PFCR25-4 | SB21RDCN-C000-4 | 1,700–2,730 | 2,500 | 90 | £62 | 24V/3.7A/89W / 28V/4.7A/131W | Warm nat. + ring dome | SB12PFCR25-4 £20.58 (Willys); SB21RDCN-C000-4 £41.60 (Willys); 1,030Hz window; 90mm spacing; best value compact ring dome |
| XT19_1 | DSA90-8 | XT19TD00-04 | 1,640–3,260 | 2,500 | 93 | £59 | 24V/3.7A/90W / 29V/4.6A/132W* | Detailed + ring | DSA90-8 £29.71 (SI €34.95); XT19TD00-04 £29.71 (SI €34.95); 19mm ring rad; 93mm spacing; burst needs 32.4W (4Ω correction) vs 20W rated — DSP limiter at 18W caps tweeter to 98.9dB (2.1dB gap to sub burst — audible HF compression) |
| XT19_2 | SB12PFCR25-4 | XT19TD00-04 | 1,640–2,730 | 2,500 | 108 | £50 | 24V/3.8A/91W / 28V/4.7A/133W* | Warm + ring | SB12PFCR25-4 £20.58 (Willys); XT19TD00-04 £29.71 (SI €34.95); 19mm ring; 1090Hz window; same 2.1dB HF ceiling at burst; DSP limiter essential |
| XT19_3 | DS115-8 | XT19TD00-04 | 1,640–2,636 | 2,500 | 105 | £61 | 24V/3.6A/87W / 28V/4.6A/129W* | Warm + ring | DS115-8 £31.41 (SI €36.95); XT19TD00-04 £29.71 (SI €34.95); 19mm ring + paper warmth; 996Hz window; burst ceiling 98.9dB; SB19ST (100dB cap) or XT25TG30 preferred |
| TF4 | DSA90-8 | SEAS H1211-06 | 1,800–3,260 | 2,500 | 98 | £76 | 24V/3.3A/79W / 29V/4.2A/121W | Detailed + dome 90W | **⚠ H1211 OOS (Jun 2026)** — HFC £46.70 no other UK source; DSA90-8 £29.71 (SI €34.95); 1,460Hz window; 27mm SEAS cloth 6Ω |
| TF5 | DS115-8 | SEAS H1211-06 | 1,800–2,636 | 2,500 | 110 | £78 | 24V/3.2A/76W / 28V/4.2A/118W | Warm + dome 90W | **⚠ H1211 OOS** — HFC £46.70; DS115-8 £31.41 (SI €36.95); 836Hz window |
| TF6 | SB12PFCR25-4 | SEAS H1211-06 | 1,800–2,730 | 2,500 | 113 | £67 | 24V/3.3A/79W / 28V/4.3A/122W | Warm nat. + dome 90W | **⚠ H1211 OOS** — HFC £46.70; SB12PFCR £20.58 (Willys); 930Hz window |
| TF7 | DSA90-8 | SEAS H1318-06 | 1,900–3,260 | 2,500 | 98 | £80 | 24V/3.2A/77W / 29V/4.1A/120W | Detailed + dome 90W | H1318 £49.95 (Falcon); DSA90-8 £29.71 (SI €34.95); 1,360Hz window; 29mm cloth dome 6Ω; 98mm |
| TF8 | DS115-8 | SEAS H1318-06 | 1,900–2,636 | 2,500 | 110 | £81 | 24V/3.1A/75W / 28V/4.2A/117W | Warm + dome 90W | H1318 £49.95 (Falcon); DS115-8 £31.41 (SI €36.95); 736Hz window — tight; 29mm cloth 6Ω |
| TF9 | SB12PFCR25-4 | SEAS H1318-06 | 1,900–2,730 | 2,500 | 113 | £71 | 24V/3.3A/79W / 28V/4.3A/120W | Warm nat. + dome 90W | H1318 £49.95 (Falcon); SB12PFCR £20.58 (Willys); 830Hz window; nat. fibre + 29mm SEAS |
| CAT1 | DSA90-8 | Morel CAT-298 | 1,800–3,260 | 2,500 | 98 | £86 | 24V/3.4A/81W / 29V/4.3A/124W | Detailed + dome 80W | CAT-298 £55.95 (Falcon); DSA90-8 £29.71 (SI €34.95); 1,460Hz window; 28mm Acuflex replaceable dome 8Ω; 98mm |
| CAT2 | DS115-8 | Morel CAT-298 | 1,800–2,636 | 2,500 | 110 | £87 | 24V/3.3A/79W / 28V/4.3A/121W | Warm + dome 80W | CAT-298 £55.95 (Falcon); DS115-8 £31.41 (SI €36.95); 836Hz window; Acuflex 8Ω |
| CAT3 | SB12PFCR25-4 | Morel CAT-298 | 1,800–2,730 | 2,500 | 113 | £77 | 24V/3.4A/82W / 28V/4.4A/124W | Warm nat. + dome 80W | CAT-298 £55.95 (Falcon); SB12PFCR £20.58 (Willys); 930Hz window; nat. fibre + Acuflex |
| ILL1 | DSA90-8 | D3004/602010 | 850–3,260 | 2,500 | 77 | £145 | 24V/3.6A/87W / 29V/4.5A/130W | Detailed + Illuminator | **⚠ DISC** — D3004 £115.05 (Willys, last stock); DSA90-8 £29.71 (SI €34.95); 2,410Hz window; 77mm spacing; Fs=425Hz widest xover floor |
| ILL2 | DS115-8 | D3004/602010 | 850–2,636 | 2,500 | 89 | £146 | 24V/3.5A/84W / 28V/4.5A/126W | Warm + Illuminator | **⚠ DISC** — D3004 £115.05 (Willys); DS115-8 £31.41 (SI €36.95); 1,786Hz window |
| ILL3 | SB12PFCR25-4 | D3004/602010 | 850–2,730 | 2,500 | 92 | £136 | 24V/3.7A/88W / 28V/4.7A/130W | Warm nat. + Illuminator | **⚠ DISC** — D3004 £115.05 (Willys); SB12PFCR £20.58 (Willys); 1,880Hz window; nat. fibre + Illuminator |
| X1 | DSA90-8 | XT25TG | 880–3260 | 2500 | 98 | £60 | 24V/3.4A/82W / 28V/4.4A/124W | Aluminium detail + Ring rad detail | DSA90-8 £29.71 (SI €34.95); XT25TG £29.90 (Falcon); Wide xover window |
| X2 | DSA90-8 | XT25BG | 1140–3260 | 2500 | 98 | £67 | 24V/3.3A/80W / 28V/4.4A/122W | Aluminium detail + Ring rad detail | DSA90-8 £29.71 (SI €34.95); XT25BG £37.14 (Willys); Wide xover window |
| X3 | DSA90-8 | SB26ADC | 1360–3260 | 2500 | 98 | £71 | 24V/3.6A/86W / 28V/4.6A/128W | Aluminium detail + Dome warmth | DSA90-8 £29.71 (SI €34.95); SB26ADC £41.60 (Willys); Wide xover window |
| X4 | DSA90-8 | TN25 | 3000–3260 | 3130 | 73 | £51 | 24V/3.4A/81W / 28V/4.4A/123W | Aluminium detail + Dome warmth | DSA90-8 £29.71 (SI €34.95); TN25 £21.63 (SI €25.45); Tight window (distortion risk) |
| X5 | DSA90-8 | TN28B | 2600–3260 | 2930 | 69 | £55 | 24V/3.4A/82W / 28V/4.4A/124W | Aluminium detail + Dome warmth | DSA90-8 £29.71 (SI €34.95); TN28B £25.46 (SI €29.95) |
| X6 | DSA90-8 | SB26ST | 1740–3260 | 2500 | 82 | £55 | 24V/3.4A/81W / 28V/4.4A/123W | Aluminium detail + Dome warmth | DSA90-8 £29.71 (SI €34.95); SB26ST £25.30 (Willys); Wide xover window |
| X7 | DSA90-8 | DX25TG | 1180–3260 | 2500 | 98 | £48 | 24V/3.3A/79W / 28V/4.3A/121W | Aluminium detail + Dome warmth | DSA90-8 £29.71 (SI €34.95); DX25TG £18.44 (Willys); Wide xover window |
| X8 | DSA90-8 | D2604/833 | 950–3260 | 2500 | 98 | £72 | 24V/3.3A/80W / 28V/4.3A/122W | Aluminium detail + Dome warmth | DSA90-8 £29.71 (SI €34.95); D2604/833 £41.88 (Willys); Wide xover window |
| X9 | DSA90-8 | D2604/830 | 1260–3260 | 2500 | 98 | £63 | 24V/3.4A/81W / 28V/4.4A/123W | Aluminium detail + Dome warmth | DSA90-8 £29.71 (SI €34.95); D2604/830 £33.05 (Falcon); Wide xover window |
| X10 | DSA90-8 | R2604/833 | 880–3260 | 2500 | 98 | £76 | 24V/3.4A/81W / 28V/4.4A/123W | Aluminium detail + Ring rad detail | DSA90-8 £29.71 (SI €34.95); R2604/833 £45.95 (Falcon); Wide xover window |
| X11 | DSA90-8 | R2604/832 | 1000–3260 | 2500 | 98 | £69 | 24V/3.6A/86W / 28V/4.6A/128W | Aluminium detail + Ring rad detail | DSA90-8 £29.71 (SI €34.95); R2604/832 £38.95 (Falcon); Wide xover window |
| X12 | DSA90-8 | SB29SDAC | 1200–3260 | 2500 | 98 | £64 | 24V/3.3A/80W / 28V/4.3A/122W | Aluminium detail + Dome warmth | DSA90-8 £29.71 (SI €34.95); SB29SDAC £34.30 (Willys); Wide xover window |
| X13 | DSA90-8 | MDT12 | 2000–3260 | 2500 | 73 | £69 | 24V/3.4A/81W / 28V/4.4A/123W | Aluminium detail + Dome warmth | DSA90-8 £29.71 (SI €34.95); MDT12 £39.50 (Willys) |
| X14 | DSA90-8 | NE19VTS | 1540–3260 | 2500 | 72 | £55 | 24V/3.5A/85W / 28V/4.5A/127W | Aluminium detail + Wide dispersion | DSA90-8 £29.71 (SI €34.95); NE19VTS £25.20 (Willys); Wide xover window |
| X15 | DSA90-8 | D27TG35 | 1800–3260 | 2500 | 98 | £57 | 24V/3.3A/79W / 28V/4.3A/121W | Aluminium detail + Dome warmth | DSA90-8 £29.71 (SI €34.95); D27TG35 £27.52 (Willys) |
| X16 | TCP115-8 | XT25TG | 880–2570 | 2500 | 110 | £44 | 24V/4.2A/101W / 36V/4.1A/147W* | Natural warmth + Ring rad detail | TCP115-8 £14.41 (SI €16.95); XT25TG £29.90 (Falcon); Wide xover window |
| X17 | TCP115-8 | XT25BG | 1140–2570 | 2500 | 110 | £52 | 24V/4.2A/100W / 36V/4.0A/146W* | Natural warmth + Ring rad detail | TCP115-8 £14.41 (SI €16.95); XT25BG £37.14 (Willys) |
| X18 | TCP115-8 | XT25SC90 | 1650–2570 | 2500 | 103 | £33 | 24V/4.4A/105W / 36V/4.2A/151W* | Natural warmth + Ring rad detail | TCP115-8 £14.41 (SI €16.95); XT25SC90 £18.20 (Falcon) |
| X19 | TCP115-8 | XT25SC40 | 2036–2570 | 2500 | 79 | £40 | 24V/4.1A/98W / 36V/4.0A/144W* | Natural warmth + Ring rad detail | TCP115-8 £14.41 (SI €16.95); XT25SC40 £25.46 (SI €29.95) |
| X20 | TCP115-8 | XT19TD | 1640–2570 | 2500 | 105 | £44 | 24V/4.5A/109W / 36V/4.3A/155W* | Natural warmth + Ring rad detail | TCP115-8 £14.41 (SI €16.95); XT19TD £29.71 (SI €34.95) |
| X21 | TCP115-8 | SB26ADC | 1360–2570 | 2500 | 110 | £56 | 24V/4.4A/105W / 36V/4.2A/151W* | Natural warmth + Dome warmth | TCP115-8 £14.41 (SI €16.95); SB26ADC £41.60 (Willys) |
| X22 | TCP115-8 | SB26STCN | 1900–2570 | 2500 | 94 | £43 | 24V/4.2A/101W / 36V/4.1A/147W* | Natural warmth + Dome warmth | TCP115-8 £14.41 (SI €16.95); SB26STCN £28.92 (Willys) |
| X23 | TCP115-8 | SB26ST | 1740–2570 | 2500 | 94 | £40 | 24V/4.2A/101W / 36V/4.1A/147W* | Natural warmth + Dome warmth | TCP115-8 £14.41 (SI €16.95); SB26ST £25.30 (Willys) |
| X24 | TCP115-8 | RST28F | 1420–2570 | 2500 | 110 | £54 | 24V/4.1A/98W / 36V/4.0A/144W* | Natural warmth + Dome warmth | TCP115-8 £14.41 (SI €16.95); RST28F £39.91 (SI €46.95) |
| X25 | TCP115-8 | DX25TG | 1180–2570 | 2500 | 110 | £33 | 24V/4.1A/99W / 36V/4.0A/145W* | Natural warmth + Dome warmth | TCP115-8 £14.41 (SI €16.95); DX25TG £18.44 (Willys) |
| X26 | TCP115-8 | D2606 | 2200–2570 | 2500 | 110 | £44 | 24V/4.1A/99W / 36V/4.0A/145W* | Natural warmth + Dome warmth | TCP115-8 £14.41 (SI €16.95); D2606 £29.35 (Falcon); Narrow window |
| X27 | TCP115-8 | D2604/833 | 950–2570 | 2500 | 110 | £56 | 24V/4.1A/99W / 36V/4.0A/145W* | Natural warmth + Dome warmth | TCP115-8 £14.41 (SI €16.95); D2604/833 £41.88 (Willys); Wide xover window |
| X28 | TCP115-8 | D2604/830 | 1260–2570 | 2500 | 110 | £47 | 24V/4.2A/101W / 36V/4.1A/147W* | Natural warmth + Dome warmth | TCP115-8 £14.41 (SI €16.95); D2604/830 £33.05 (Falcon) |
| X29 | TCP115-8 | R2604/833 | 880–2570 | 2500 | 110 | £60 | 24V/4.2A/101W / 36V/4.1A/147W* | Natural warmth + Ring rad detail | TCP115-8 £14.41 (SI €16.95); R2604/833 £45.95 (Falcon); Wide xover window |
| X30 | TCP115-8 | R2604/832 | 1000–2570 | 2500 | 110 | £53 | 24V/4.4A/105W / 36V/4.2A/151W* | Natural warmth + Ring rad detail | TCP115-8 £14.41 (SI €16.95); R2604/832 £38.95 (Falcon); Wide xover window |
| X31 | TCP115-8 | H1189 | 1100–2570 | 2500 | 109 | £71 | 24V/4.2A/101W / 36V/4.1A/147W* | Natural warmth + Dome warmth | TCP115-8 £14.41 (SI €16.95); H1189 £56.92 (Falcon) |
| X32 | TCP115-8 | SB21RDCN | 1700–2570 | 2500 | 87 | £56 | 24V/4.5A/107W / 36V/4.2A/153W* | Natural warmth + Ring rad detail | TCP115-8 £14.41 (SI €16.95); SB21RDCN £41.60 (Willys) |
| X33 | TCP115-8 | SB21SDC | 1440–2570 | 2500 | 104 | £43 | 24V/4.3A/103W / 36V/4.1A/149W* | Natural warmth + Dome warmth | TCP115-8 £14.41 (SI €16.95); SB21SDC £28.51 (Willys) |
| X34 | TCP115-8 | SB29RDNC | 1160–2570 | 2500 | 110 | £69 | 24V/4.1A/98W / 36V/4.0A/144W* | Natural warmth + Ring rad detail | TCP115-8 £14.41 (SI €16.95); SB29RDNC £54.31 (Willys) |
| X35 | TCP115-8 | SB29SDAC | 1200–2570 | 2500 | 110 | £49 | 24V/4.1A/99W / 36V/4.0A/145W* | Natural warmth + Dome warmth | TCP115-8 £14.41 (SI €16.95); SB29SDAC £34.30 (Willys) |
| X36 | TCP115-8 | MDT22T | 1300–2570 | 2500 | 85 | £62 | 24V/4.2A/101W / 36V/4.1A/147W* | Natural warmth + Dome warmth | TCP115-8 £14.41 (SI €16.95); MDT22T £47.55 (Willys) |
| X37 | TCP115-8 | MDT12 | 2000–2570 | 2500 | 85 | £54 | 24V/4.2A/101W / 36V/4.1A/147W* | Natural warmth + Dome warmth | TCP115-8 £14.41 (SI €16.95); MDT12 £39.50 (Willys) |
| X38 | TCP115-8 | NE19VTS | 1540–2570 | 2500 | 84 | £40 | 24V/4.3A/104W / 36V/4.2A/150W* | Natural warmth + Wide dispersion | TCP115-8 £14.41 (SI €16.95); NE19VTS £25.20 (Willys) |
| X39 | TCP115-8 | NE25VTS | 1460–2570 | 2500 | 91 | £48 | 24V/4.3A/103W / 36V/4.1A/149W* | Natural warmth + Wide dispersion | TCP115-8 £14.41 (SI €16.95); NE25VTS £33.96 (SI €39.95) |
| X40 | TCP115-8 | TD25F | 1800–2570 | 2500 | 104 | £40 | 24V/4.3A/103W / 36V/4.1A/149W* | Natural warmth + Dome warmth | TCP115-8 £14.41 (SI €16.95); TD25F £25.46 (SI €29.95) |
| X41 | TCP115-8 | D27TG35 | 1800–2570 | 2500 | 110 | £42 | 24V/4.1A/98W / 36V/4.0A/144W* | Natural warmth + Dome warmth | TCP115-8 £14.41 (SI €16.95); D27TG35 £27.52 (Willys) |
| X42 | DS115-8 | XT25TG | 880–2636 | 2500 | 109 | £61 | 24V/3.3A/79W / 28V/4.3A/121W | Natural warmth + Ring rad detail | DS115-8 £31.41 (SI €36.95); XT25TG £29.90 (Falcon); Wide xover window |
| X43 | DS115-8 | XT25BG | 1140–2636 | 2500 | 110 | £69 | 24V/3.2A/78W / 28V/4.3A/120W | Natural warmth + Ring rad detail | DS115-8 £31.41 (SI €36.95); XT25BG £37.14 (Willys) |
| X44 | DS115-8 | TN28B | 2600–2636 | 2618 | 81 | £57 | 24V/3.3A/79W / 28V/4.3A/121W | Natural warmth + Dome warmth | DS115-8 £31.41 (SI €36.95); TN28B £25.46 (SI €29.95); Tight window (distortion risk) |
| X45 | DS115-8 | SB26ST | 1740–2636 | 2500 | 93 | £57 | 24V/3.3A/79W / 28V/4.3A/121W | Natural warmth + Dome warmth | DS115-8 £31.41 (SI €36.95); SB26ST £25.30 (Willys) |
| X46 | DS115-8 | DX25TG | 1180–2636 | 2500 | 109 | £50 | 24V/3.2A/76W / 28V/4.2A/118W | Natural warmth + Dome warmth | DS115-8 £31.41 (SI €36.95); DX25TG £18.44 (Willys) |
| X47 | DS115-8 | D2604/833 | 950–2636 | 2500 | 109 | £73 | 24V/3.2A/77W / 28V/4.2A/119W | Natural warmth + Dome warmth | DS115-8 £31.41 (SI €36.95); D2604/833 £41.88 (Willys); Wide xover window |
| X48 | DS115-8 | D2604/830 | 1260–2636 | 2500 | 109 | £64 | 24V/3.3A/79W / 28V/4.3A/121W | Natural warmth + Dome warmth | DS115-8 £31.41 (SI €36.95); D2604/830 £33.05 (Falcon) |
| X49 | DS115-8 | R2604/833 | 880–2636 | 2500 | 109 | £77 | 24V/3.3A/79W / 28V/4.3A/121W | Natural warmth + Ring rad detail | DS115-8 £31.41 (SI €36.95); R2604/833 £45.95 (Falcon); Wide xover window |
| X50 | DS115-8 | R2604/832 | 1000–2636 | 2500 | 109 | £70 | 24V/3.5A/83W / 28V/4.5A/125W | Natural warmth + Ring rad detail | DS115-8 £31.41 (SI €36.95); R2604/832 £38.95 (Falcon); Wide xover window |
| X51 | DS115-8 | MDT12 | 2000–2636 | 2500 | 84 | £71 | 24V/3.3A/79W / 28V/4.3A/121W | Natural warmth + Dome warmth | DS115-8 £31.41 (SI €36.95); MDT12 £39.50 (Willys) |
| X52 | DS115-8 | NE19VTS | 1540–2636 | 2500 | 83 | £57 | 24V/3.4A/82W / 28V/4.4A/124W | Natural warmth + Wide dispersion | DS115-8 £31.41 (SI €36.95); NE19VTS £25.20 (Willys) |
| X53 | HiVi B4N | XT25TG | 880–2636 | 2500 | 110 | £49 | 24V/3.3A/80W / 28V/4.4A/122W | Natural warmth + Ring rad detail | HiVi B4N £19.08 (SI €22.45); XT25TG £29.90 (Falcon); Wide xover window |
| X54 | HiVi B4N | XT25BG | 1140–2636 | 2500 | 110 | £56 | 24V/3.3A/79W / 28V/4.3A/121W | Natural warmth + Ring rad detail | HiVi B4N £19.08 (SI €22.45); XT25BG £37.14 (Willys) |
| X55 | HiVi B4N | XT25SC90 | 1650–2636 | 2500 | 103 | £37 | 24V/3.5A/84W / 28V/4.5A/126W | Natural warmth + Ring rad detail | HiVi B4N £19.08 (SI €22.45); XT25SC90 £18.20 (Falcon) |
| X56 | HiVi B4N | XT25SC40 | 2036–2636 | 2500 | 80 | £45 | 24V/3.2A/77W / 28V/4.2A/119W | Natural warmth + Ring rad detail | HiVi B4N £19.08 (SI €22.45); XT25SC40 £25.46 (SI €29.95) |
| X57 | HiVi B4N | XT19TD | 1640–2636 | 2500 | 105 | £49 | 24V/3.7A/88W / 28V/4.7A/130W | Natural warmth + Ring rad detail | HiVi B4N £19.08 (SI €22.45); XT19TD £29.71 (SI €34.95) |
| X58 | HiVi B4N | SB26ADC | 1360–2636 | 2500 | 110 | £61 | 24V/3.5A/85W / 28V/4.5A/127W | Natural warmth + Dome warmth | HiVi B4N £19.08 (SI €22.45); SB26ADC £41.60 (Willys) |
| X59 | HiVi B4N | TN28B | 2600–2636 | 2618 | 82 | £45 | 24V/3.3A/80W / 28V/4.4A/122W | Natural warmth + Dome warmth | HiVi B4N £19.08 (SI €22.45); TN28B £25.46 (SI €29.95); Tight window (distortion risk) |
| X60 | HiVi B4N | SB26ST | 1740–2636 | 2500 | 94 | £44 | 24V/3.3A/80W / 28V/4.4A/122W | Natural warmth + Dome warmth | HiVi B4N £19.08 (SI €22.45); SB26ST £25.30 (Willys) |
| X61 | HiVi B4N | RST28F | 1420–2636 | 2500 | 110 | £59 | 24V/3.2A/78W / 28V/4.3A/120W | Natural warmth + Dome warmth | HiVi B4N £19.08 (SI €22.45); RST28F £39.91 (SI €46.95) |
| X62 | HiVi B4N | DX25TG | 1180–2636 | 2500 | 110 | £38 | 24V/3.2A/78W / 28V/4.3A/120W | Natural warmth + Dome warmth | HiVi B4N £19.08 (SI €22.45); DX25TG £18.44 (Willys) |
| X63 | HiVi B4N | D2606 | 2200–2636 | 2500 | 110 | £48 | 24V/3.3A/78W / 28V/4.3A/120W | Natural warmth + Dome warmth | HiVi B4N £19.08 (SI €22.45); D2606 £29.35 (Falcon); Narrow window |
| X64 | HiVi B4N | D2604/833 | 950–2636 | 2500 | 110 | £61 | 24V/3.3A/78W / 28V/4.3A/120W | Natural warmth + Dome warmth | HiVi B4N £19.08 (SI €22.45); D2604/833 £41.88 (Willys); Wide xover window |
| X65 | HiVi B4N | D2604/830 | 1260–2636 | 2500 | 110 | £52 | 24V/3.3A/80W / 28V/4.4A/122W | Natural warmth + Dome warmth | HiVi B4N £19.08 (SI €22.45); D2604/830 £33.05 (Falcon) |
| X66 | HiVi B4N | R2604/833 | 880–2636 | 2500 | 110 | £65 | 24V/3.3A/80W / 28V/4.4A/122W | Natural warmth + Ring rad detail | HiVi B4N £19.08 (SI €22.45); R2604/833 £45.95 (Falcon); Wide xover window |
| X67 | HiVi B4N | R2604/832 | 1000–2636 | 2500 | 110 | £58 | 24V/3.5A/85W / 28V/4.5A/127W | Natural warmth + Ring rad detail | HiVi B4N £19.08 (SI €22.45); R2604/832 £38.95 (Falcon); Wide xover window |
| X68 | HiVi B4N | H1189 | 1100–2636 | 2500 | 110 | £76 | 24V/3.3A/80W / 28V/4.4A/122W | Natural warmth + Dome warmth | HiVi B4N £19.08 (SI €22.45); H1189 £56.92 (Falcon); Wide xover window |
| X69 | HiVi B4N | SB21RDCN | 1700–2636 | 2500 | 87 | £61 | 24V/3.6A/86W / 28V/4.6A/128W | Natural warmth + Ring rad detail | HiVi B4N £19.08 (SI €22.45); SB21RDCN £41.60 (Willys) |
| X70 | HiVi B4N | SB21SDC | 1440–2636 | 2500 | 104 | £48 | 24V/3.4A/82W / 28V/4.4A/124W | Natural warmth + Dome warmth | HiVi B4N £19.08 (SI €22.45); SB21SDC £28.51 (Willys) |
| X71 | HiVi B4N | SB29RDNC | 1160–2636 | 2500 | 110 | £73 | 24V/3.2A/77W / 28V/4.2A/119W | Natural warmth + Ring rad detail | HiVi B4N £19.08 (SI €22.45); SB29RDNC £54.31 (Willys) |
| X72 | HiVi B4N | SB29SDAC | 1200–2636 | 2500 | 110 | £53 | 24V/3.3A/78W / 28V/4.3A/120W | Natural warmth + Dome warmth | HiVi B4N £19.08 (SI €22.45); SB29SDAC £34.30 (Willys) |
| X73 | HiVi B4N | MDT22T | 1300–2636 | 2500 | 85 | £67 | 24V/3.3A/80W / 28V/4.4A/122W | Natural warmth + Dome warmth | HiVi B4N £19.08 (SI €22.45); MDT22T £47.55 (Willys) |
| X74 | HiVi B4N | MDT12 | 2000–2636 | 2500 | 85 | £59 | 24V/3.3A/80W / 28V/4.4A/122W | Natural warmth + Dome warmth | HiVi B4N £19.08 (SI €22.45); MDT12 £39.50 (Willys) |
| X75 | HiVi B4N | NE19VTS | 1540–2636 | 2500 | 84 | £44 | 24V/3.5A/83W / 28V/4.5A/125W | Natural warmth + Wide dispersion | HiVi B4N £19.08 (SI €22.45); NE19VTS £25.20 (Willys) |
| X76 | HiVi B4N | NE25VTS | 1460–2636 | 2500 | 91 | £53 | 24V/3.4A/82W / 28V/4.4A/124W | Natural warmth + Wide dispersion | HiVi B4N £19.08 (SI €22.45); NE25VTS £33.96 (SI €39.95) |
| X77 | HiVi B4N | TD25F | 1800–2636 | 2500 | 105 | £45 | 24V/3.4A/82W / 28V/4.4A/124W | Natural warmth + Dome warmth | HiVi B4N £19.08 (SI €22.45); TD25F £25.46 (SI €29.95) |
| X78 | HiVi B4N | D27TG35 | 1800–2636 | 2500 | 110 | £47 | 24V/3.2A/78W / 28V/4.3A/120W | Natural warmth + Dome warmth | HiVi B4N £19.08 (SI €22.45); D27TG35 £27.52 (Willys) |
| X79 | SB12PACR | SB19ST | 1960–2730 | 2500 | 105 | £38 | 24V/4.0A/95W / 28V/4.9A/137W | Aluminium detail + Wide dispersion | SB12PACR £23.76 (Willys); SB19ST £14.30 (Falcon) |
| X80 | SB12PACR | XT25TG | 880–2730 | 2500 | 113 | £54 | 24V/3.6A/85W / 28V/4.5A/127W | Aluminium detail + Ring rad detail | SB12PACR £23.76 (Willys); XT25TG £29.90 (Falcon); Wide xover window |
| X81 | SB12PACR | XT25BG | 1140–2730 | 2500 | 113 | £61 | 24V/3.5A/84W / 28V/4.5A/126W | Aluminium detail + Ring rad detail | SB12PACR £23.76 (Willys); XT25BG £37.14 (Willys); Wide xover window |
| X82 | SB12PACR | XT25SC90 | 1650–2730 | 2500 | 106 | £42 | 24V/3.7A/90W / 28V/4.7A/132W | Aluminium detail + Ring rad detail | SB12PACR £23.76 (Willys); XT25SC90 £18.20 (Falcon) |
| X83 | SB12PACR | XT25SC40 | 2036–2730 | 2500 | 82 | £49 | 24V/3.4A/82W / 28V/4.4A/124W | Aluminium detail + Ring rad detail | SB12PACR £23.76 (Willys); XT25SC40 £25.46 (SI €29.95) |
| X84 | SB12PACR | XT19TD | 1640–2730 | 2500 | 108 | £53 | 24V/3.9A/93W / 28V/4.8A/135W | Aluminium detail + Ring rad detail | SB12PACR £23.76 (Willys); XT19TD £29.71 (SI €34.95) |
| X85 | SB12PACR | SB26ADC | 1360–2730 | 2500 | 113 | £65 | 24V/3.7A/90W / 28V/4.7A/132W | Aluminium detail + Dome warmth | SB12PACR £23.76 (Willys); SB26ADC £41.60 (Willys) |
| X86 | SB12PACR | TN28B | 2600–2730 | 2665 | 84 | £49 | 24V/3.6A/86W / 28V/4.6A/128W | Aluminium detail + Dome warmth | SB12PACR £23.76 (Willys); TN28B £25.46 (SI €29.95); Tight window (distortion risk) |
| X87 | SB12PACR | ND25FA | 2700–2730 | 2715 | 94 | £42 | 24V/3.7A/90W / 28V/4.7A/132W | Aluminium detail + Dome warmth | SB12PACR £23.76 (Willys); ND25FA £18.23 (SI €21.45); Tight window (distortion risk) |
| X88 | SB12PACR | BC25SC06 | 2700–2730 | 2715 | 96 | £41 | 24V/3.4A/81W / 28V/4.4A/123W | Aluminium detail + Dome warmth | SB12PACR £23.76 (Willys); BC25SC06 £16.78 (Willys); Tight window (distortion risk) |
| X89 | SB12PACR | SB26STCN | 1900–2730 | 2500 | 97 | £53 | 24V/3.5A/85W / 28V/4.5A/127W | Aluminium detail + Dome warmth | SB12PACR £23.76 (Willys); SB26STCN £28.92 (Willys) |
| X90 | SB12PACR | SB26ST | 1740–2730 | 2500 | 97 | £49 | 24V/3.5A/85W / 28V/4.5A/127W | Aluminium detail + Dome warmth | SB12PACR £23.76 (Willys); SB26ST £25.30 (Willys) |
| X91 | SB12PACR | RST28F | 1420–2730 | 2500 | 113 | £64 | 24V/3.5A/83W / 28V/4.5A/125W | Aluminium detail + Dome warmth | SB12PACR £23.76 (Willys); RST28F £39.91 (SI €46.95) |
| X92 | SB12PACR | DX25TG | 1180–2730 | 2500 | 113 | £42 | 24V/3.5A/83W / 28V/4.5A/125W | Aluminium detail + Dome warmth | SB12PACR £23.76 (Willys); DX25TG £18.44 (Willys); Wide xover window |
| X93 | SB12PACR | D2606 | 2200–2730 | 2500 | 113 | £53 | 24V/3.5A/83W / 28V/4.5A/125W | Aluminium detail + Dome warmth | SB12PACR £23.76 (Willys); D2606 £29.35 (Falcon) |
| X94 | SB12PACR | D2604/833 | 950–2730 | 2500 | 113 | £66 | 24V/3.5A/84W / 28V/4.5A/126W | Aluminium detail + Dome warmth | SB12PACR £23.76 (Willys); D2604/833 £41.88 (Willys); Wide xover window |
| X95 | SB12PACR | D2604/830 | 1260–2730 | 2500 | 113 | £57 | 24V/3.5A/85W / 28V/4.5A/127W | Aluminium detail + Dome warmth | SB12PACR £23.76 (Willys); D2604/830 £33.05 (Falcon) |
| X96 | SB12PACR | R2604/833 | 880–2730 | 2500 | 113 | £70 | 24V/3.5A/85W / 28V/4.5A/127W | Aluminium detail + Ring rad detail | SB12PACR £23.76 (Willys); R2604/833 £45.95 (Falcon); Wide xover window |
| X97 | SB12PACR | R2604/832 | 1000–2730 | 2500 | 113 | £63 | 24V/3.7A/90W / 28V/4.7A/132W | Aluminium detail + Ring rad detail | SB12PACR £23.76 (Willys); R2604/832 £38.95 (Falcon); Wide xover window |
| X98 | SB12PACR | H1189 | 1100–2730 | 2500 | 112 | £81 | 24V/3.6A/86W / 28V/4.6A/128W | Aluminium detail + Dome warmth | SB12PACR £23.76 (Willys); H1189 £56.92 (Falcon); Wide xover window |
| X99 | SB12PACR | SB21RDCN | 1700–2730 | 2500 | 90 | £65 | 24V/3.8A/91W / 28V/4.8A/133W | Aluminium detail + Ring rad detail | SB12PACR £23.76 (Willys); SB21RDCN £41.60 (Willys) |
| X100 | SB12PACR | SB21SDC | 1440–2730 | 2500 | 107 | £52 | 24V/3.6A/87W / 28V/4.6A/129W | Aluminium detail + Dome warmth | SB12PACR £23.76 (Willys); SB21SDC £28.51 (Willys) |
| X101 | SB12PACR | SB29RDNC | 1160–2730 | 2500 | 113 | £78 | 24V/3.4A/82W / 28V/4.4A/124W | Aluminium detail + Ring rad detail | SB12PACR £23.76 (Willys); SB29RDNC £54.31 (Willys); Wide xover window |
| X102 | SB12PACR | SB29SDAC | 1200–2730 | 2500 | 113 | £58 | 24V/3.5A/84W / 28V/4.5A/126W | Aluminium detail + Dome warmth | SB12PACR £23.76 (Willys); SB29SDAC £34.30 (Willys); Wide xover window |
| X103 | SB12PACR | MDT22T | 1300–2730 | 2500 | 88 | £71 | 24V/3.5A/85W / 28V/4.5A/127W | Aluminium detail + Dome warmth | SB12PACR £23.76 (Willys); MDT22T £47.55 (Willys) |
| X104 | SB12PACR | MDT12 | 2000–2730 | 2500 | 88 | £63 | 24V/3.5A/85W / 28V/4.5A/127W | Aluminium detail + Dome warmth | SB12PACR £23.76 (Willys); MDT12 £39.50 (Willys) |
| X105 | SB12PACR | NE19VTS | 1540–2730 | 2500 | 87 | £49 | 24V/3.7A/89W / 28V/4.7A/131W | Aluminium detail + Wide dispersion | SB12PACR £23.76 (Willys); NE19VTS £25.20 (Willys) |
| X106 | SB12PACR | NE25VTS | 1460–2730 | 2500 | 94 | £58 | 24V/3.6A/87W / 28V/4.6A/129W | Aluminium detail + Wide dispersion | SB12PACR £23.76 (Willys); NE25VTS £33.96 (SI €39.95) |
| X107 | SB12PACR | TD25F | 1800–2730 | 2500 | 107 | £49 | 24V/3.6A/87W / 28V/4.6A/129W | Aluminium detail + Dome warmth | SB12PACR £23.76 (Willys); TD25F £25.46 (SI €29.95) |
| X108 | SB12PACR | D27TG35 | 1800–2730 | 2500 | 113 | £51 | 24V/3.4A/83W / 28V/4.5A/125W | Aluminium detail + Dome warmth | SB12PACR £23.76 (Willys); D27TG35 £27.52 (Willys) |
| X109 | SB12NRX | XT25TG | 880–2730 | 2500 | 113 | £76 | 24V/3.4A/83W / 28V/4.4A/125W | Natural warmth + Ring rad detail | SB12NRX £45.75 (Willys); XT25TG £29.90 (Falcon); Wide xover window |
| X110 | SB12NRX | XT25BG | 1140–2730 | 2500 | 113 | £83 | 24V/3.4A/81W / 28V/4.4A/123W | Natural warmth + Ring rad detail | SB12NRX £45.75 (Willys); XT25BG £37.14 (Willys); Wide xover window |
| X111 | SB12NRX | XT25SC90 | 1650–2730 | 2500 | 106 | £64 | 24V/3.6A/87W / 28V/4.6A/129W | Natural warmth + Ring rad detail | SB12NRX £45.75 (Willys); XT25SC90 £18.20 (Falcon) |
| X112 | SB12NRX | XT25SC40 | 2036–2730 | 2500 | 82 | £71 | 24V/3.3A/79W / 28V/4.3A/121W | Natural warmth + Ring rad detail | SB12NRX £45.75 (Willys); XT25SC40 £25.46 (SI €29.95) |
| X113 | SB12NRX | XT19TD | 1640–2730 | 2500 | 108 | £75 | 24V/3.8A/91W / 28V/4.7A/133W | Natural warmth + Ring rad detail | SB12NRX £45.75 (Willys); XT19TD £29.71 (SI €34.95) |
| X114 | SB12NRX | SB26ADC | 1360–2730 | 2500 | 113 | £87 | 24V/3.6A/87W / 28V/4.6A/129W | Natural warmth + Dome warmth | SB12NRX £45.75 (Willys); SB26ADC £41.60 (Willys) |
| X115 | SB12NRX | TN28B | 2600–2730 | 2665 | 84 | £71 | 24V/3.5A/83W / 28V/4.5A/125W | Natural warmth + Dome warmth | SB12NRX £45.75 (Willys); TN28B £25.46 (SI €29.95); Tight window (distortion risk) |
| X116 | SB12NRX | ND25FA | 2700–2730 | 2715 | 94 | £64 | 24V/3.6A/87W / 28V/4.6A/129W | Natural warmth + Dome warmth | SB12NRX £45.75 (Willys); ND25FA £18.23 (SI €21.45); Tight window (distortion risk) |
| X117 | SB12NRX | BC25SC06 | 2700–2730 | 2715 | 96 | £63 | 24V/3.3A/78W / 28V/4.3A/120W | Natural warmth + Dome warmth | SB12NRX £45.75 (Willys); BC25SC06 £16.78 (Willys); Tight window (distortion risk) |
| X118 | SB12NRX | SB26STCN | 1900–2730 | 2500 | 97 | £75 | 24V/3.4A/82W / 28V/4.4A/124W | Natural warmth + Dome warmth | SB12NRX £45.75 (Willys); SB26STCN £28.92 (Willys) |
| X119 | SB12NRX | SB26ST | 1740–2730 | 2500 | 97 | £71 | 24V/3.4A/82W / 28V/4.4A/124W | Natural warmth + Dome warmth | SB12NRX £45.75 (Willys); SB26ST £25.30 (Willys) |
| X120 | SB12NRX | RST28F | 1420–2730 | 2500 | 113 | £86 | 24V/3.3A/80W / 28V/4.4A/122W | Natural warmth + Dome warmth | SB12NRX £45.75 (Willys); RST28F £39.91 (SI €46.95) |
| X121 | SB12NRX | DX25TG | 1180–2730 | 2500 | 113 | £64 | 24V/3.3A/80W / 28V/4.4A/122W | Natural warmth + Dome warmth | SB12NRX £45.75 (Willys); DX25TG £18.44 (Willys); Wide xover window |
| X122 | SB12NRX | D2606 | 2200–2730 | 2500 | 113 | £75 | 24V/3.4A/81W / 28V/4.4A/123W | Natural warmth + Dome warmth | SB12NRX £45.75 (Willys); D2606 £29.35 (Falcon) |
| X123 | SB12NRX | D2604/833 | 950–2730 | 2500 | 113 | £88 | 24V/3.4A/81W / 28V/4.4A/123W | Natural warmth + Dome warmth | SB12NRX £45.75 (Willys); D2604/833 £41.88 (Willys); Wide xover window |
| X124 | SB12NRX | D2604/830 | 1260–2730 | 2500 | 113 | £79 | 24V/3.4A/82W / 28V/4.4A/124W | Natural warmth + Dome warmth | SB12NRX £45.75 (Willys); D2604/830 £33.05 (Falcon) |
| X125 | SB12NRX | R2604/833 | 880–2730 | 2500 | 113 | £92 | 24V/3.4A/82W / 28V/4.4A/124W | Natural warmth + Ring rad detail | SB12NRX £45.75 (Willys); R2604/833 £45.95 (Falcon); Wide xover window |
| X126 | SB12NRX | R2604/832 | 1000–2730 | 2500 | 113 | £85 | 24V/3.6A/87W / 28V/4.6A/129W | Natural warmth + Ring rad detail | SB12NRX £45.75 (Willys); R2604/832 £38.95 (Falcon); Wide xover window |
| X127 | SB12NRX | H1189 | 1100–2730 | 2500 | 112 | £103 | 24V/3.5A/83W / 28V/4.5A/125W | Natural warmth + Dome warmth | SB12NRX £45.75 (Willys); H1189 £56.92 (Falcon); Wide xover window |
| X128 | SB12NRX | SB21RDCN | 1700–2730 | 2500 | 90 | £87 | 24V/3.7A/89W / 28V/4.7A/131W | Natural warmth + Ring rad detail | SB12NRX £45.75 (Willys); SB21RDCN £41.60 (Willys) |
| X129 | SB12NRX | SB21SDC | 1440–2730 | 2500 | 107 | £74 | 24V/3.5A/84W / 28V/4.5A/126W | Natural warmth + Dome warmth | SB12NRX £45.75 (Willys); SB21SDC £28.51 (Willys) |
| X130 | SB12NRX | SB29RDNC | 1160–2730 | 2500 | 113 | £100 | 24V/3.3A/79W / 28V/4.3A/121W | Natural warmth + Ring rad detail | SB12NRX £45.75 (Willys); SB29RDNC £54.31 (Willys); Wide xover window |
| X131 | SB12NRX | SB29SDAC | 1200–2730 | 2500 | 113 | £80 | 24V/3.4A/81W / 28V/4.4A/123W | Natural warmth + Dome warmth | SB12NRX £45.75 (Willys); SB29SDAC £34.30 (Willys); Wide xover window |
| X132 | SB12NRX | MDT22T | 1300–2730 | 2500 | 88 | £93 | 24V/3.4A/82W / 28V/4.4A/124W | Natural warmth + Dome warmth | SB12NRX £45.75 (Willys); MDT22T £47.55 (Willys) |
| X133 | SB12NRX | MDT12 | 2000–2730 | 2500 | 88 | £85 | 24V/3.4A/82W / 28V/4.4A/124W | Natural warmth + Dome warmth | SB12NRX £45.75 (Willys); MDT12 £39.50 (Willys) |
| X134 | SB12NRX | NE19VTS | 1540–2730 | 2500 | 87 | £71 | 24V/3.6A/86W / 28V/4.6A/128W | Natural warmth + Wide dispersion | SB12NRX £45.75 (Willys); NE19VTS £25.20 (Willys) |
| X135 | SB12NRX | NE25VTS | 1460–2730 | 2500 | 94 | £80 | 24V/3.5A/84W / 28V/4.5A/126W | Natural warmth + Wide dispersion | SB12NRX £45.75 (Willys); NE25VTS £33.96 (SI €39.95) |
| X136 | SB12NRX | TD25F | 1800–2730 | 2500 | 107 | £71 | 24V/3.5A/84W / 28V/4.5A/126W | Natural warmth + Dome warmth | SB12NRX £45.75 (Willys); TD25F £25.46 (SI €29.95) |
| X137 | SB12NRX | D27TG35 | 1800–2730 | 2500 | 113 | £73 | 24V/3.3A/80W / 28V/4.4A/122W | Natural warmth + Dome warmth | SB12NRX £45.75 (Willys); D27TG35 £27.52 (Willys) |
| X138 | SB12PFCR | XT25TG | 880–2730 | 2500 | 113 | £50 | 24V/3.4A/83W / 28V/4.4A/125W | Natural warmth + Ring rad detail | SB12PFCR £20.58 (Willys); XT25TG £29.90 (Falcon); Wide xover window |
| X139 | SB12PFCR | XT25BG | 1140–2730 | 2500 | 113 | £58 | 24V/3.4A/81W / 28V/4.4A/123W | Natural warmth + Ring rad detail | SB12PFCR £20.58 (Willys); XT25BG £37.14 (Willys); Wide xover window |
| X140 | SB12PFCR | TN28B | 2600–2730 | 2665 | 84 | £46 | 24V/3.5A/83W / 28V/4.5A/125W | Natural warmth + Dome warmth | SB12PFCR £20.58 (Willys); TN28B £25.46 (SI €29.95); Tight window (distortion risk) |
| X141 | SB12PFCR | ND25FA | 2700–2730 | 2715 | 94 | £39 | 24V/3.6A/87W / 28V/4.6A/129W | Natural warmth + Dome warmth | SB12PFCR £20.58 (Willys); ND25FA £18.23 (SI €21.45); Tight window (distortion risk) |
| X142 | SB12PFCR | SB26ST | 1740–2730 | 2500 | 97 | £46 | 24V/3.4A/82W / 28V/4.4A/124W | Natural warmth + Dome warmth | SB12PFCR £20.58 (Willys); SB26ST £25.30 (Willys) |
| X143 | SB12PFCR | DX25TG | 1180–2730 | 2500 | 113 | £39 | 24V/3.3A/80W / 28V/4.4A/122W | Natural warmth + Dome warmth | SB12PFCR £20.58 (Willys); DX25TG £18.44 (Willys); Wide xover window |
| X144 | SB12PFCR | D2604/833 | 950–2730 | 2500 | 113 | £62 | 24V/3.4A/81W / 28V/4.4A/123W | Natural warmth + Dome warmth | SB12PFCR £20.58 (Willys); D2604/833 £41.88 (Willys); Wide xover window |
| X145 | SB12PFCR | D2604/830 | 1260–2730 | 2500 | 113 | £54 | 24V/3.4A/82W / 28V/4.4A/124W | Natural warmth + Dome warmth | SB12PFCR £20.58 (Willys); D2604/830 £33.05 (Falcon) |
| X146 | SB12PFCR | R2604/833 | 880–2730 | 2500 | 113 | £67 | 24V/3.4A/82W / 28V/4.4A/124W | Natural warmth + Ring rad detail | SB12PFCR £20.58 (Willys); R2604/833 £45.95 (Falcon); Wide xover window |
| X147 | SB12PFCR | R2604/832 | 1000–2730 | 2500 | 113 | £60 | 24V/3.6A/87W / 28V/4.6A/129W | Natural warmth + Ring rad detail | SB12PFCR £20.58 (Willys); R2604/832 £38.95 (Falcon); Wide xover window |
| X148 | SB12PFCR | SB29SDAC | 1200–2730 | 2500 | 113 | £55 | 24V/3.4A/81W / 28V/4.4A/123W | Natural warmth + Dome warmth | SB12PFCR £20.58 (Willys); SB29SDAC £34.30 (Willys); Wide xover window |
| X149 | SB12PFCR | MDT12 | 2000–2730 | 2500 | 88 | £60 | 24V/3.4A/82W / 28V/4.4A/124W | Natural warmth + Dome warmth | SB12PFCR £20.58 (Willys); MDT12 £39.50 (Willys) |
| X150 | SB12PFCR | NE19VTS | 1540–2730 | 2500 | 87 | £46 | 24V/3.6A/86W / 28V/4.6A/128W | Natural warmth + Wide dispersion | SB12PFCR £20.58 (Willys); NE19VTS £25.20 (Willys) |
| X151 | SB12PFCR | TD25F | 1800–2730 | 2500 | 107 | £46 | 24V/3.5A/84W / 28V/4.5A/126W | Natural warmth + Dome warmth | SB12PFCR £20.58 (Willys); TD25F £25.46 (SI €29.95) |
| X152 | SB12MNRX2 | XT25TG | 880–2730 | 2500 | 113 | £78 | 24V/3.2A/78W / 28V/4.3A/120W | Natural warmth + Ring rad detail | SB12MNRX2 £48.10 (Willys); XT25TG £29.90 (Falcon); Wide xover window |
| X153 | SB12MNRX2 | XT25BG | 1140–2730 | 2500 | 113 | £85 | 24V/3.2A/77W / 28V/4.2A/119W | Natural warmth + Ring rad detail | SB12MNRX2 £48.10 (Willys); XT25BG £37.14 (Willys); Wide xover window |
| X154 | SB12MNRX2 | XT25SC90 | 1650–2730 | 2500 | 106 | £66 | 24V/3.4A/82W / 28V/4.4A/124W | Natural warmth + Ring rad detail | SB12MNRX2 £48.10 (Willys); XT25SC90 £18.20 (Falcon) |
| X155 | SB12MNRX2 | XT25SC40 | 2036–2730 | 2500 | 83 | £74 | 24V/3.1A/75W / 28V/4.2A/117W | Natural warmth + Ring rad detail | SB12MNRX2 £48.10 (Willys); XT25SC40 £25.46 (SI €29.95) |
| X156 | SB12MNRX2 | XT19TD | 1640–2730 | 2500 | 108 | £78 | 24V/3.6A/86W / 28V/4.6A/128W | Natural warmth + Ring rad detail | SB12MNRX2 £48.10 (Willys); XT19TD £29.71 (SI €34.95) |
| X157 | SB12MNRX2 | SB26ADC | 1360–2730 | 2500 | 113 | £90 | 24V/3.4A/82W / 28V/4.4A/124W | Natural warmth + Dome warmth | SB12MNRX2 £48.10 (Willys); SB26ADC £41.60 (Willys) |
| X158 | SB12MNRX2 | TN28B | 2600–2730 | 2665 | 85 | £74 | 24V/3.3A/78W / 28V/4.3A/120W | Natural warmth + Dome warmth | SB12MNRX2 £48.10 (Willys); TN28B £25.46 (SI €29.95); Tight window (distortion risk) |
| X159 | SB12MNRX2 | ND25FA | 2700–2730 | 2715 | 94 | £66 | 24V/3.4A/82W / 28V/4.4A/124W | Natural warmth + Dome warmth | SB12MNRX2 £48.10 (Willys); ND25FA £18.23 (SI €21.45); Tight window (distortion risk) |
| X160 | SB12MNRX2 | BC25SC06 | 2700–2730 | 2715 | 96 | £65 | 24V/3.1A/73W / 28V/4.1A/115W | Natural warmth + Dome warmth | SB12MNRX2 £48.10 (Willys); BC25SC06 £16.78 (Willys); Tight window (distortion risk) |
| X161 | SB12MNRX2 | SB26STCN | 1900–2730 | 2500 | 97 | £77 | 24V/3.2A/78W / 28V/4.3A/120W | Natural warmth + Dome warmth | SB12MNRX2 £48.10 (Willys); SB26STCN £28.92 (Willys) |
| X162 | SB12MNRX2 | SB26ST | 1740–2730 | 2500 | 97 | £73 | 24V/3.2A/78W / 28V/4.3A/120W | Natural warmth + Dome warmth | SB12MNRX2 £48.10 (Willys); SB26ST £25.30 (Willys) |
| X163 | SB12MNRX2 | RST28F | 1420–2730 | 2500 | 114 | £88 | 24V/3.1A/75W / 28V/4.2A/117W | Natural warmth + Dome warmth | SB12MNRX2 £48.10 (Willys); RST28F £39.91 (SI €46.95) |
| X164 | SB12MNRX2 | DX25TG | 1180–2730 | 2500 | 113 | £67 | 24V/3.1A/76W / 28V/4.2A/118W | Natural warmth + Dome warmth | SB12MNRX2 £48.10 (Willys); DX25TG £18.44 (Willys); Wide xover window |
| X165 | SB12MNRX2 | D2606 | 2200–2730 | 2500 | 113 | £77 | 24V/3.2A/76W / 28V/4.2A/118W | Natural warmth + Dome warmth | SB12MNRX2 £48.10 (Willys); D2606 £29.35 (Falcon) |
| X166 | SB12MNRX2 | D2604/833 | 950–2730 | 2500 | 113 | £90 | 24V/3.2A/76W / 28V/4.2A/118W | Natural warmth + Dome warmth | SB12MNRX2 £48.10 (Willys); D2604/833 £41.88 (Willys); Wide xover window |
| X167 | SB12MNRX2 | D2604/830 | 1260–2730 | 2500 | 113 | £81 | 24V/3.2A/78W / 28V/4.3A/120W | Natural warmth + Dome warmth | SB12MNRX2 £48.10 (Willys); D2604/830 £33.05 (Falcon) |
| X168 | SB12MNRX2 | R2604/833 | 880–2730 | 2500 | 113 | £94 | 24V/3.2A/78W / 28V/4.3A/120W | Natural warmth + Ring rad detail | SB12MNRX2 £48.10 (Willys); R2604/833 £45.95 (Falcon); Wide xover window |
| X169 | SB12MNRX2 | R2604/832 | 1000–2730 | 2500 | 113 | £87 | 24V/3.4A/82W / 28V/4.4A/124W | Natural warmth + Ring rad detail | SB12MNRX2 £48.10 (Willys); R2604/832 £38.95 (Falcon); Wide xover window |
| X170 | SB12MNRX2 | H1189 | 1100–2730 | 2500 | 113 | £105 | 24V/3.3A/78W / 28V/4.3A/120W | Natural warmth + Dome warmth | SB12MNRX2 £48.10 (Willys); H1189 £56.92 (Falcon); Wide xover window |
| X171 | SB12MNRX2 | SB21RDCN | 1700–2730 | 2500 | 90 | £90 | 24V/3.5A/84W / 28V/4.5A/126W | Natural warmth + Ring rad detail | SB12MNRX2 £48.10 (Willys); SB21RDCN £41.60 (Willys) |
| X172 | SB12MNRX2 | MDT22T | 1300–2730 | 2500 | 88 | £96 | 24V/3.2A/78W / 28V/4.3A/120W | Natural warmth + Dome warmth | SB12MNRX2 £48.10 (Willys); MDT22T £47.55 (Willys) |
| X173 | SB12MNRX2 | MDT12 | 2000–2730 | 2500 | 88 | £88 | 24V/3.2A/78W / 28V/4.3A/120W | Natural warmth + Dome warmth | SB12MNRX2 £48.10 (Willys); MDT12 £39.50 (Willys) |
| X174 | SB12MNRX2 | NE19VTS | 1540–2730 | 2500 | 87 | £73 | 24V/3.4A/81W / 28V/4.4A/123W | Natural warmth + Wide dispersion | SB12MNRX2 £48.10 (Willys); NE19VTS £25.20 (Willys) |
| X175 | SB12MNRX2 | NE25VTS | 1460–2730 | 2500 | 94 | £82 | 24V/3.3A/80W / 28V/4.3A/122W | Natural warmth + Wide dispersion | SB12MNRX2 £48.10 (Willys); NE25VTS £33.96 (SI €39.95) |
| X176 | SB12MNRX2 | TD25F | 1800–2730 | 2500 | 108 | £74 | 24V/3.3A/80W / 28V/4.4A/122W | Natural warmth + Dome warmth | SB12MNRX2 £48.10 (Willys); TD25F £25.46 (SI €29.95) |
| X177 | SB12MNRX2 | D27TG35 | 1800–2730 | 2500 | 113 | £76 | 24V/3.1A/75W / 28V/4.2A/117W | Natural warmth + Dome warmth | SB12MNRX2 £48.10 (Willys); D27TG35 £27.52 (Willys) |
| X178 | SIG150-4 | SB19ST | 1960–1990 | 1975 | 120 | £53 | 24V/3.3A/80W / 28V/4.3A/122W | Aluminium detail + Wide dispersion | SIG150-4 £38.21 (SI €44.95); SB19ST £14.30 (Falcon); Tight window (distortion risk) |
| X179 | SIG150-4 | XT25TG | 880–1990 | 1435 | 128 | £68 | 24V/2.9A/70W / 28V/4.0A/112W | Aluminium detail + Ring rad detail | SIG150-4 £38.21 (SI €44.95); XT25TG £29.90 (Falcon) |
| X180 | SIG150-4 | XT25BG | 1140–1990 | 1565 | 128 | £75 | 24V/2.9A/69W / 28V/4.0A/111W | Aluminium detail + Ring rad detail | SIG150-4 £38.21 (SI €44.95); XT25BG £37.14 (Willys) |
| X181 | SIG150-4 | XT25SC90 | 1650–1990 | 1820 | 121 | £56 | 24V/3.1A/74W / 28V/4.1A/116W | Aluminium detail + Ring rad detail | SIG150-4 £38.21 (SI €44.95); XT25SC90 £18.20 (Falcon); Narrow window |
| X182 | SIG150-4 | XT19TD | 1640–1990 | 1815 | 123 | £68 | 24V/3.3A/78W / 28V/4.3A/120W | Aluminium detail + Ring rad detail | SIG150-4 £38.21 (SI €44.95); XT19TD £29.71 (SI €34.95); Narrow window |
| X183 | SIG150-4 | SB26ADC | 1360–1990 | 1675 | 128 | £80 | 24V/3.1A/74W / 28V/4.2A/116W | Aluminium detail + Dome warmth | SIG150-4 £38.21 (SI €44.95); SB26ADC £41.60 (Willys) |
| X184 | SIG150-4 | SB26STCN | 1900–1990 | 1945 | 112 | £67 | 24V/2.9A/70W / 28V/4.0A/112W | Aluminium detail + Dome warmth | SIG150-4 £38.21 (SI €44.95); SB26STCN £28.92 (Willys); Tight window (distortion risk) |
| X185 | SIG150-4 | SB26ST | 1740–1990 | 1865 | 112 | £64 | 24V/2.9A/70W / 28V/4.0A/112W | Aluminium detail + Dome warmth | SIG150-4 £38.21 (SI €44.95); SB26ST £25.30 (Willys); Tight window (distortion risk) |
| X186 | SIG150-4 | RST28F | 1420–1990 | 1705 | 128 | £78 | 24V/2.8A/67W / 28V/3.9A/109W | Aluminium detail + Dome warmth | SIG150-4 £38.21 (SI €44.95); RST28F £39.91 (SI €46.95) |
| X187 | SIG150-4 | DX25TG | 1180–1990 | 1585 | 128 | £57 | 24V/2.8A/68W / 28V/3.9A/110W | Aluminium detail + Dome warmth | SIG150-4 £38.21 (SI €44.95); DX25TG £18.44 (Willys) |
| X188 | SIG150-4 | D2604/833 | 950–1990 | 1470 | 128 | £80 | 24V/2.8A/68W / 28V/3.9A/110W | Aluminium detail + Dome warmth | SIG150-4 £38.21 (SI €44.95); D2604/833 £41.88 (Willys) |
| X189 | SIG150-4 | D2604/830 | 1260–1990 | 1625 | 128 | £71 | 24V/2.9A/70W / 28V/4.0A/112W | Aluminium detail + Dome warmth | SIG150-4 £38.21 (SI €44.95); D2604/830 £33.05 (Falcon) |
| X190 | SIG150-4 | R2604/833 | 880–1990 | 1435 | 128 | £84 | 24V/2.9A/70W / 28V/4.0A/112W | Aluminium detail + Ring rad detail | SIG150-4 £38.21 (SI €44.95); R2604/833 £45.95 (Falcon) |
| X191 | SIG150-4 | R2604/832 | 1000–1990 | 1495 | 128 | £77 | 24V/3.1A/74W / 28V/4.2A/116W | Aluminium detail + Ring rad detail | SIG150-4 £38.21 (SI €44.95); R2604/832 £38.95 (Falcon) |
| X192 | SIG150-4 | H1189 | 1100–1990 | 1545 | 127 | £95 | 24V/2.9A/70W / 28V/4.0A/112W | Aluminium detail + Dome warmth | SIG150-4 £38.21 (SI €44.95); H1189 £56.92 (Falcon) |
| X193 | SIG150-4 | SB21RDCN | 1700–1990 | 1845 | 105 | £80 | 24V/3.2A/76W / 28V/4.2A/118W | Aluminium detail + Ring rad detail | SIG150-4 £38.21 (SI €44.95); SB21RDCN £41.60 (Willys); Tight window (distortion risk) |
| X194 | SIG150-4 | SB21SDC | 1440–1990 | 1715 | 122 | £67 | 24V/3.0A/72W / 28V/4.1A/114W | Aluminium detail + Dome warmth | SIG150-4 £38.21 (SI €44.95); SB21SDC £28.51 (Willys) |
| X195 | SIG150-4 | SB29RDNC | 1160–1990 | 1575 | 128 | £93 | 24V/2.8A/67W / 28V/3.9A/109W | Aluminium detail + Ring rad detail | SIG150-4 £38.21 (SI €44.95); SB29RDNC £54.31 (Willys) |
| X196 | SIG150-4 | SB29SDAC | 1200–1990 | 1595 | 128 | £73 | 24V/2.8A/68W / 28V/3.9A/110W | Aluminium detail + Dome warmth | SIG150-4 £38.21 (SI €44.95); SB29SDAC £34.30 (Willys) |
| X197 | SIG150-4 | MDT22T | 1300–1990 | 1645 | 103 | £86 | 24V/2.9A/70W / 28V/4.0A/112W | Aluminium detail + Dome warmth | SIG150-4 £38.21 (SI €44.95); MDT22T £47.55 (Willys) |
| X198 | SIG150-4 | NE19VTS | 1540–1990 | 1765 | 102 | £63 | 24V/3.1A/73W / 28V/4.1A/115W | Aluminium detail + Wide dispersion | SIG150-4 £38.21 (SI €44.95); NE19VTS £25.20 (Willys); Narrow window |
| X199 | SIG150-4 | NE25VTS | 1460–1990 | 1725 | 109 | £72 | 24V/3.0A/72W / 28V/4.1A/114W | Aluminium detail + Wide dispersion | SIG150-4 £38.21 (SI €44.95); NE25VTS £33.96 (SI €39.95) |
| X200 | SIG150-4 | TD25F | 1800–1990 | 1895 | 122 | £64 | 24V/3.0A/72W / 28V/4.1A/114W | Aluminium detail + Dome warmth | SIG150-4 £38.21 (SI €44.95); TD25F £25.46 (SI €29.95); Tight window (distortion risk) |
| X201 | SIG150-4 | D27TG35 | 1800–1990 | 1895 | 128 | £66 | 24V/2.8A/67W / 28V/3.9A/109W | Aluminium detail + Dome warmth | SIG150-4 £38.21 (SI €44.95); D27TG35 £27.52 (Willys); Tight window (distortion risk) |
| X202 | SB13PFCR | SB19ST | 1960–2080 | 2020 | 109 | £39 | 24V/3.6A/86W / 28V/4.6A/128W | Natural warmth + Wide dispersion | SB13PFCR £24.50 (Willys); SB19ST £14.30 (Falcon); Tight window (distortion risk) |
| X203 | SB13PFCR | XT25TG | 880–2080 | 1480 | 117 | £54 | 24V/3.2A/76W / 28V/4.2A/118W | Natural warmth + Ring rad detail | SB13PFCR £24.50 (Willys); XT25TG £29.90 (Falcon) |
| X204 | SB13PFCR | XT25BG | 1140–2080 | 1610 | 117 | £62 | 24V/3.1A/75W / 28V/4.2A/117W | Natural warmth + Ring rad detail | SB13PFCR £24.50 (Willys); XT25BG £37.14 (Willys) |
| X205 | SB13PFCR | XT25SC90 | 1650–2080 | 1865 | 110 | £43 | 24V/3.3A/80W / 28V/4.4A/122W | Natural warmth + Ring rad detail | SB13PFCR £24.50 (Willys); XT25SC90 £18.20 (Falcon); Narrow window |
| X206 | SB13PFCR | XT25SC40 | 2036–2080 | 2058 | 86 | £50 | 24V/3.0A/73W / 28V/4.1A/115W | Natural warmth + Ring rad detail | SB13PFCR £24.50 (Willys); XT25SC40 £25.46 (SI €29.95); Tight window (distortion risk) |
| X207 | SB13PFCR | XT19TD | 1640–2080 | 1860 | 112 | £54 | 24V/3.5A/84W / 28V/4.5A/126W | Natural warmth + Ring rad detail | SB13PFCR £24.50 (Willys); XT19TD £29.71 (SI €34.95); Narrow window |
| X208 | SB13PFCR | SB26ADC | 1360–2080 | 1720 | 117 | £66 | 24V/3.4A/81W / 28V/4.4A/123W | Natural warmth + Dome warmth | SB13PFCR £24.50 (Willys); SB26ADC £41.60 (Willys) |
| X209 | SB13PFCR | SB26STCN | 1900–2080 | 1990 | 101 | £53 | 24V/3.2A/76W / 28V/4.2A/118W | Natural warmth + Dome warmth | SB13PFCR £24.50 (Willys); SB26STCN £28.92 (Willys); Tight window (distortion risk) |
| X210 | SB13PFCR | SB26ST | 1740–2080 | 1910 | 101 | £50 | 24V/3.2A/76W / 28V/4.2A/118W | Natural warmth + Dome warmth | SB13PFCR £24.50 (Willys); SB26ST £25.30 (Willys); Narrow window |
| X211 | SB13PFCR | RST28F | 1420–2080 | 1750 | 117 | £64 | 24V/3.1A/74W / 28V/4.1A/116W | Natural warmth + Dome warmth | SB13PFCR £24.50 (Willys); RST28F £39.91 (SI €46.95) |
| X212 | SB13PFCR | DX25TG | 1180–2080 | 1630 | 117 | £43 | 24V/3.1A/74W / 28V/4.1A/116W | Natural warmth + Dome warmth | SB13PFCR £24.50 (Willys); DX25TG £18.44 (Willys) |
| X213 | SB13PFCR | D2604/833 | 950–2080 | 1515 | 117 | £66 | 24V/3.1A/74W / 28V/4.2A/116W | Natural warmth + Dome warmth | SB13PFCR £24.50 (Willys); D2604/833 £41.88 (Willys) |
| X214 | SB13PFCR | D2604/830 | 1260–2080 | 1670 | 117 | £58 | 24V/3.2A/76W / 28V/4.2A/118W | Natural warmth + Dome warmth | SB13PFCR £24.50 (Willys); D2604/830 £33.05 (Falcon) |
| X215 | SB13PFCR | R2604/833 | 880–2080 | 1480 | 117 | £70 | 24V/3.2A/76W / 28V/4.2A/118W | Natural warmth + Ring rad detail | SB13PFCR £24.50 (Willys); R2604/833 £45.95 (Falcon) |
| X216 | SB13PFCR | R2604/832 | 1000–2080 | 1540 | 117 | £63 | 24V/3.4A/81W / 28V/4.4A/123W | Natural warmth + Ring rad detail | SB13PFCR £24.50 (Willys); R2604/832 £38.95 (Falcon) |
| X217 | SB13PFCR | H1189 | 1100–2080 | 1590 | 116 | £81 | 24V/3.2A/76W / 28V/4.2A/118W | Natural warmth + Dome warmth | SB13PFCR £24.50 (Willys); H1189 £56.92 (Falcon) |
| X218 | SB13PFCR | SB21RDCN | 1700–2080 | 1890 | 94 | £66 | 24V/3.4A/82W / 28V/4.4A/124W | Natural warmth + Ring rad detail | SB13PFCR £24.50 (Willys); SB21RDCN £41.60 (Willys); Narrow window |
| X219 | SB13PFCR | SB21SDC | 1440–2080 | 1760 | 111 | £53 | 24V/3.2A/78W / 28V/4.3A/120W | Natural warmth + Dome warmth | SB13PFCR £24.50 (Willys); SB21SDC £28.51 (Willys) |
| X220 | SB13PFCR | SB29SDAC | 1200–2080 | 1640 | 117 | £59 | 24V/3.1A/74W / 28V/4.2A/116W | Natural warmth + Dome warmth | SB13PFCR £24.50 (Willys); SB29SDAC £34.30 (Willys) |
| X221 | SB13PFCR | MDT22T | 1300–2080 | 1690 | 92 | £72 | 24V/3.2A/76W / 28V/4.2A/118W | Natural warmth + Dome warmth | SB13PFCR £24.50 (Willys); MDT22T £47.55 (Willys) |
| X222 | SB13PFCR | MDT12 | 2000–2080 | 2040 | 92 | £64 | 24V/3.2A/76W / 28V/4.2A/118W | Natural warmth + Dome warmth | SB13PFCR £24.50 (Willys); MDT12 £39.50 (Willys); Tight window (distortion risk) |
| X223 | SB13PFCR | NE19VTS | 1540–2080 | 1810 | 91 | £50 | 24V/3.3A/79W / 28V/4.3A/121W | Natural warmth + Wide dispersion | SB13PFCR £24.50 (Willys); NE19VTS £25.20 (Willys) |
| X224 | SB13PFCR | NE25VTS | 1460–2080 | 1770 | 98 | £58 | 24V/3.2A/78W / 28V/4.3A/120W | Natural warmth + Wide dispersion | SB13PFCR £24.50 (Willys); NE25VTS £33.96 (SI €39.95) |
| X225 | SB13PFCR | TD25F | 1800–2080 | 1940 | 111 | £50 | 24V/3.2A/78W / 28V/4.3A/120W | Natural warmth + Dome warmth | SB13PFCR £24.50 (Willys); TD25F £25.46 (SI €29.95); Tight window (distortion risk) |
| X226 | SB13PFCR | D27TG35 | 1800–2080 | 1940 | 117 | £52 | 24V/3.1A/73W / 28V/4.1A/115W | Natural warmth + Dome warmth | SB13PFCR £24.50 (Willys); D27TG35 £27.52 (Willys); Tight window (distortion risk) |
| X227 | SLS-85 | SB19ST | 1960–3000 | 2500 | 89 | £40 | 24V/4.2A/102W / 28V/5.1A/144W | Natural warmth + Wide dispersion | SLS-85 £25.46 (SI €29.95); SB19ST £14.30 (Falcon) |
| X228 | SLS-85 | XT25TG | 880–3000 | 2500 | 97 | £55 | 24V/3.8A/92W / 28V/4.8A/134W | Natural warmth + Ring rad detail | SLS-85 £25.46 (SI €29.95); XT25TG £29.90 (Falcon); Wide xover window |
| X229 | SLS-85 | XT25BG | 1140–3000 | 2500 | 97 | £63 | 24V/3.8A/91W / 28V/4.7A/133W | Natural warmth + Ring rad detail | SLS-85 £25.46 (SI €29.95); XT25BG £37.14 (Willys); Wide xover window |
| X230 | SLS-85 | XT25SC90 | 1650–3000 | 2500 | 90 | £44 | 24V/4.0A/96W / 28V/4.9A/138W | Natural warmth + Ring rad detail | SLS-85 £25.46 (SI €29.95); XT25SC90 £18.20 (Falcon) |
| X231 | SLS-85 | XT25SC40 | 2036–3000 | 2500 | 67 | £51 | 24V/3.7A/89W / 28V/4.7A/131W | Natural warmth + Ring rad detail | SLS-85 £25.46 (SI €29.95); XT25SC40 £25.46 (SI €29.95) |
| X232 | SLS-85 | XT19TD | 1640–3000 | 2500 | 92 | £55 | 24V/4.2A/100W / 28V/5.1A/142W | Natural warmth + Ring rad detail | SLS-85 £25.46 (SI €29.95); XT19TD £29.71 (SI €34.95) |
| X233 | SLS-85 | SB26ADC | 1360–3000 | 2500 | 97 | £67 | 24V/4.0A/96W / 28V/4.9A/138W | Natural warmth + Dome warmth | SLS-85 £25.46 (SI €29.95); SB26ADC £41.60 (Willys); Wide xover window |
| X234 | SLS-85 | TN25 | 3000–3000 | 3000 | 72 | £47 | 24V/3.8A/92W / 28V/4.8A/134W | Natural warmth + Dome warmth | SLS-85 £25.46 (SI €29.95); TN25 £21.63 (SI €25.45); Tight window (distortion risk) |
| X235 | SLS-85 | TN28B | 2600–3000 | 2800 | 69 | £51 | 24V/3.8A/92W / 28V/4.8A/134W | Natural warmth + Dome warmth | SLS-85 £25.46 (SI €29.95); TN28B £25.46 (SI €29.95); Narrow window |
| X236 | SLS-85 | ND25FA | 2700–3000 | 2850 | 78 | £44 | 24V/4.0A/96W / 28V/4.9A/138W | Natural warmth + Dome warmth | SLS-85 £25.46 (SI €29.95); ND25FA £18.23 (SI €21.45); Narrow window |
| X237 | SLS-85 | BC25SC06 | 2700–3000 | 2850 | 80 | £42 | 24V/3.6A/87W / 28V/4.6A/129W | Natural warmth + Dome warmth | SLS-85 £25.46 (SI €29.95); BC25SC06 £16.78 (Willys); Narrow window |
| X238 | SLS-85 | SB26STCN | 1900–3000 | 2500 | 81 | £54 | 24V/3.8A/92W / 28V/4.8A/134W | Natural warmth + Dome warmth | SLS-85 £25.46 (SI €29.95); SB26STCN £28.92 (Willys) |
| X239 | SLS-85 | SB26ST | 1740–3000 | 2500 | 81 | £51 | 24V/3.8A/92W / 28V/4.8A/134W | Natural warmth + Dome warmth | SLS-85 £25.46 (SI €29.95); SB26ST £25.30 (Willys) |
| X240 | SLS-85 | RST28F | 1420–3000 | 2500 | 98 | £65 | 24V/3.7A/89W / 28V/4.7A/131W | Natural warmth + Dome warmth | SLS-85 £25.46 (SI €29.95); RST28F £39.91 (SI €46.95); Wide xover window |
| X241 | SLS-85 | DX25TG | 1180–3000 | 2500 | 97 | £44 | 24V/3.7A/89W / 28V/4.7A/131W | Natural warmth + Dome warmth | SLS-85 £25.46 (SI €29.95); DX25TG £18.44 (Willys); Wide xover window |
| X242 | SLS-85 | D2606 | 2200–3000 | 2500 | 97 | £55 | 24V/3.7A/90W / 28V/4.7A/132W | Natural warmth + Dome warmth | SLS-85 £25.46 (SI €29.95); D2606 £29.35 (Falcon) |
| X243 | SLS-85 | D2604/833 | 950–3000 | 2500 | 97 | £67 | 24V/3.8A/90W / 28V/4.7A/132W | Natural warmth + Dome warmth | SLS-85 £25.46 (SI €29.95); D2604/833 £41.88 (Willys); Wide xover window |
| X244 | SLS-85 | D2604/830 | 1260–3000 | 2500 | 97 | £59 | 24V/3.8A/92W / 28V/4.8A/134W | Natural warmth + Dome warmth | SLS-85 £25.46 (SI €29.95); D2604/830 £33.05 (Falcon); Wide xover window |
| X245 | SLS-85 | R2604/833 | 880–3000 | 2500 | 97 | £71 | 24V/3.8A/92W / 28V/4.8A/134W | Natural warmth + Ring rad detail | SLS-85 £25.46 (SI €29.95); R2604/833 £45.95 (Falcon); Wide xover window |
| X246 | SLS-85 | R2604/832 | 1000–3000 | 2500 | 97 | £64 | 24V/4.0A/96W / 28V/4.9A/138W | Natural warmth + Ring rad detail | SLS-85 £25.46 (SI €29.95); R2604/832 £38.95 (Falcon); Wide xover window |
| X247 | SLS-85 | H1189 | 1100–3000 | 2500 | 97 | £82 | 24V/3.8A/92W / 28V/4.8A/134W | Natural warmth + Dome warmth | SLS-85 £25.46 (SI €29.95); H1189 £56.92 (Falcon); Wide xover window |
| X248 | SLS-85 | SB21RDCN | 1700–3000 | 2500 | 74 | £67 | 24V/4.1A/98W / 28V/5.0A/140W | Natural warmth + Ring rad detail | SLS-85 £25.46 (SI €29.95); SB21RDCN £41.60 (Willys) |
| X249 | SLS-85 | SB21SDC | 1440–3000 | 2500 | 91 | £54 | 24V/3.9A/94W / 28V/4.8A/136W | Natural warmth + Dome warmth | SLS-85 £25.46 (SI €29.95); SB21SDC £28.51 (Willys); Wide xover window |
| X250 | SLS-85 | SB29RDNC | 1160–3000 | 2500 | 97 | £80 | 24V/3.7A/89W / 28V/4.7A/131W | Natural warmth + Ring rad detail | SLS-85 £25.46 (SI €29.95); SB29RDNC £54.31 (Willys); Wide xover window |
| X251 | SLS-85 | SB29SDAC | 1200–3000 | 2500 | 97 | £60 | 24V/3.8A/90W / 28V/4.7A/132W | Natural warmth + Dome warmth | SLS-85 £25.46 (SI €29.95); SB29SDAC £34.30 (Willys); Wide xover window |
| X252 | SLS-85 | MDT22T | 1300–3000 | 2500 | 72 | £73 | 24V/3.8A/92W / 28V/4.8A/134W | Natural warmth + Dome warmth | SLS-85 £25.46 (SI €29.95); MDT22T £47.55 (Willys); Wide xover window |
| X253 | SLS-85 | MDT12 | 2000–3000 | 2500 | 72 | £65 | 24V/3.8A/92W / 28V/4.8A/134W | Natural warmth + Dome warmth | SLS-85 £25.46 (SI €29.95); MDT12 £39.50 (Willys) |
| X254 | SLS-85 | NE19VTS | 1540–3000 | 2500 | 71 | £51 | 24V/4.0A/95W / 28V/4.9A/137W | Natural warmth + Wide dispersion | SLS-85 £25.46 (SI €29.95); NE19VTS £25.20 (Willys) |
| X255 | SLS-85 | NE25VTS | 1460–3000 | 2500 | 78 | £59 | 24V/3.9A/93W / 28V/4.8A/135W | Natural warmth + Wide dispersion | SLS-85 £25.46 (SI €29.95); NE25VTS £33.96 (SI €39.95); Wide xover window |
| X256 | SLS-85 | TD25F | 1800–3000 | 2500 | 92 | £51 | 24V/3.9A/94W / 28V/4.8A/136W | Natural warmth + Dome warmth | SLS-85 £25.46 (SI €29.95); TD25F £25.46 (SI €29.95) |
| X257 | SLS-85 | D27TG35 | 1800–3000 | 2500 | 97 | £53 | 24V/3.7A/89W / 28V/4.7A/131W | Natural warmth + Dome warmth | SLS-85 £25.46 (SI €29.95); D27TG35 £27.52 (Willys) |
| X258 | RS125-4 | SB19ST | 1960–2184 | 2072 | 106 | £71 | 24V/3.4A/83W / 28V/4.5A/125W | Aluminium detail + Wide dispersion | RS125-4 £56.91 (SI €66.95); SB19ST £14.30 (Falcon); Tight window (distortion risk) |
| X259 | RS125-4 | XT25TG | 880–2184 | 1532 | 114 | £87 | 24V/3.0A/73W / 28V/4.1A/115W | Aluminium detail + Ring rad detail | RS125-4 £56.91 (SI €66.95); XT25TG £29.90 (Falcon) |
| X260 | RS125-4 | XT25BG | 1140–2184 | 1662 | 114 | £94 | 24V/3.0A/72W / 28V/4.1A/114W | Aluminium detail + Ring rad detail | RS125-4 £56.91 (SI €66.95); XT25BG £37.14 (Willys) |
| X261 | RS125-4 | XT25SC90 | 1650–2184 | 1917 | 107 | £75 | 24V/3.2A/77W / 28V/4.3A/119W | Aluminium detail + Ring rad detail | RS125-4 £56.91 (SI €66.95); XT25SC90 £18.20 (Falcon) |
| X262 | RS125-4 | XT25SC40 | 2036–2184 | 2110 | 84 | £82 | 24V/2.9A/70W / 28V/4.0A/112W | Aluminium detail + Ring rad detail | RS125-4 £56.91 (SI €66.95); XT25SC40 £25.46 (SI €29.95); Tight window (distortion risk) |
| X263 | RS125-4 | XT19TD | 1640–2184 | 1912 | 109 | £87 | 24V/3.4A/81W / 28V/4.4A/123W | Aluminium detail + Ring rad detail | RS125-4 £56.91 (SI €66.95); XT19TD £29.71 (SI €34.95) |
| X264 | RS125-4 | SB26ADC | 1360–2184 | 1772 | 114 | £99 | 24V/3.2A/78W / 28V/4.3A/120W | Aluminium detail + Dome warmth | RS125-4 £56.91 (SI €66.95); SB26ADC £41.60 (Willys) |
| X265 | RS125-4 | SB26STCN | 1900–2184 | 2042 | 98 | £86 | 24V/3.0A/73W / 28V/4.1A/115W | Aluminium detail + Dome warmth | RS125-4 £56.91 (SI €66.95); SB26STCN £28.92 (Willys); Tight window (distortion risk) |
| X266 | RS125-4 | SB26ST | 1740–2184 | 1962 | 98 | £82 | 24V/3.0A/73W / 28V/4.1A/115W | Aluminium detail + Dome warmth | RS125-4 £56.91 (SI €66.95); SB26ST £25.30 (Willys); Narrow window |
| X267 | RS125-4 | RST28F | 1420–2184 | 1802 | 115 | £97 | 24V/2.9A/71W / 28V/4.0A/113W | Aluminium detail + Dome warmth | RS125-4 £56.91 (SI €66.95); RST28F £39.91 (SI €46.95) |
| X268 | RS125-4 | DX25TG | 1180–2184 | 1682 | 114 | £75 | 24V/2.9A/71W / 28V/4.0A/113W | Aluminium detail + Dome warmth | RS125-4 £56.91 (SI €66.95); DX25TG £18.44 (Willys) |
| X269 | RS125-4 | D2604/833 | 950–2184 | 1567 | 114 | £99 | 24V/3.0A/71W / 28V/4.0A/113W | Aluminium detail + Dome warmth | RS125-4 £56.91 (SI €66.95); D2604/833 £41.88 (Willys) |
| X270 | RS125-4 | D2604/830 | 1260–2184 | 1722 | 114 | £90 | 24V/3.0A/73W / 28V/4.1A/115W | Aluminium detail + Dome warmth | RS125-4 £56.91 (SI €66.95); D2604/830 £33.05 (Falcon) |
| X271 | RS125-4 | R2604/833 | 880–2184 | 1532 | 114 | £103 | 24V/3.0A/73W / 28V/4.1A/115W | Aluminium detail + Ring rad detail | RS125-4 £56.91 (SI €66.95); R2604/833 £45.95 (Falcon) |
| X272 | RS125-4 | R2604/832 | 1000–2184 | 1592 | 114 | £96 | 24V/3.2A/78W / 28V/4.3A/120W | Aluminium detail + Ring rad detail | RS125-4 £56.91 (SI €66.95); R2604/832 £38.95 (Falcon) |
| X273 | RS125-4 | H1189 | 1100–2184 | 1642 | 114 | £114 | 24V/3.1A/73W / 28V/4.1A/115W | Aluminium detail + Dome warmth | RS125-4 £56.91 (SI €66.95); H1189 £56.92 (Falcon) |
| X274 | RS125-4 | SB21RDCN | 1700–2184 | 1942 | 91 | £99 | 24V/3.3A/79W / 28V/4.3A/121W | Aluminium detail + Ring rad detail | RS125-4 £56.91 (SI €66.95); SB21RDCN £41.60 (Willys); Narrow window |
| X275 | RS125-4 | SB21SDC | 1440–2184 | 1812 | 108 | £85 | 24V/3.1A/75W / 28V/4.2A/117W | Aluminium detail + Dome warmth | RS125-4 £56.91 (SI €66.95); SB21SDC £28.51 (Willys) |
| X276 | RS125-4 | SB29RDNC | 1160–2184 | 1672 | 114 | £111 | 24V/2.9A/70W / 28V/4.0A/112W | Aluminium detail + Ring rad detail | RS125-4 £56.91 (SI €66.95); SB29RDNC £54.31 (Willys) |
| X277 | RS125-4 | SB29SDAC | 1200–2184 | 1692 | 114 | £91 | 24V/3.0A/71W / 28V/4.0A/113W | Aluminium detail + Dome warmth | RS125-4 £56.91 (SI €66.95); SB29SDAC £34.30 (Willys) |
| X278 | RS125-4 | MDT22T | 1300–2184 | 1742 | 89 | £104 | 24V/3.0A/73W / 28V/4.1A/115W | Aluminium detail + Dome warmth | RS125-4 £56.91 (SI €66.95); MDT22T £47.55 (Willys) |
| X279 | RS125-4 | MDT12 | 2000–2184 | 2092 | 89 | £96 | 24V/3.0A/73W / 28V/4.1A/115W | Aluminium detail + Dome warmth | RS125-4 £56.91 (SI €66.95); MDT12 £39.50 (Willys); Tight window (distortion risk) |
| X280 | RS125-4 | NE19VTS | 1540–2184 | 1862 | 88 | £82 | 24V/3.2A/76W / 28V/4.2A/118W | Aluminium detail + Wide dispersion | RS125-4 £56.91 (SI €66.95); NE19VTS £25.20 (Willys) |
| X281 | RS125-4 | NE25VTS | 1460–2184 | 1822 | 95 | £91 | 24V/3.1A/75W / 28V/4.2A/117W | Aluminium detail + Wide dispersion | RS125-4 £56.91 (SI €66.95); NE25VTS £33.96 (SI €39.95) |
| X282 | RS125-4 | TD25F | 1800–2184 | 1992 | 109 | £82 | 24V/3.1A/75W / 28V/4.2A/117W | Aluminium detail + Dome warmth | RS125-4 £56.91 (SI €66.95); TD25F £25.46 (SI €29.95); Narrow window |
| X283 | RS125-4 | D27TG35 | 1800–2184 | 1992 | 114 | £84 | 24V/2.9A/70W / 28V/4.0A/112W | Aluminium detail + Dome warmth | RS125-4 £56.91 (SI €66.95); D27TG35 £27.52 (Willys); Narrow window |
| X284 | RS125P | SB19ST | 1960–2184 | 2072 | 106 | £70 | 24V/3.4A/82W / 28V/4.4A/124W | Natural warmth + Wide dispersion | RS125P £55.21 (SI €64.95); SB19ST £14.30 (Falcon); Tight window (distortion risk) |
| X285 | RS125P | XT25TG | 880–2184 | 1532 | 114 | £85 | 24V/3.0A/73W / 28V/4.1A/115W | Natural warmth + Ring rad detail | RS125P £55.21 (SI €64.95); XT25TG £29.90 (Falcon) |
| X286 | RS125P | XT25BG | 1140–2184 | 1662 | 114 | £92 | 24V/3.0A/72W / 28V/4.1A/114W | Natural warmth + Ring rad detail | RS125P £55.21 (SI €64.95); XT25BG £37.14 (Willys) |
| X287 | RS125P | XT25SC90 | 1650–2184 | 1917 | 107 | £73 | 24V/3.2A/77W / 28V/4.2A/119W | Natural warmth + Ring rad detail | RS125P £55.21 (SI €64.95); XT25SC90 £18.20 (Falcon) |
| X288 | RS125P | XT25SC40 | 2036–2184 | 2110 | 84 | £81 | 24V/2.9A/70W / 28V/4.0A/112W | Natural warmth + Ring rad detail | RS125P £55.21 (SI €64.95); XT25SC40 £25.46 (SI €29.95); Tight window (distortion risk) |
| X289 | RS125P | XT19TD | 1640–2184 | 1912 | 109 | £85 | 24V/3.4A/81W / 28V/4.4A/123W | Natural warmth + Ring rad detail | RS125P £55.21 (SI €64.95); XT19TD £29.71 (SI €34.95) |
| X290 | RS125P | SB26ADC | 1360–2184 | 1772 | 114 | £97 | 24V/3.2A/77W / 28V/4.3A/119W | Natural warmth + Dome warmth | RS125P £55.21 (SI €64.95); SB26ADC £41.60 (Willys) |
| X291 | RS125P | SB26STCN | 1900–2184 | 2042 | 98 | £84 | 24V/3.0A/73W / 28V/4.1A/115W | Natural warmth + Dome warmth | RS125P £55.21 (SI €64.95); SB26STCN £28.92 (Willys); Tight window (distortion risk) |
| X292 | RS125P | SB26ST | 1740–2184 | 1962 | 98 | £81 | 24V/3.0A/73W / 28V/4.1A/115W | Natural warmth + Dome warmth | RS125P £55.21 (SI €64.95); SB26ST £25.30 (Willys); Narrow window |
| X293 | RS125P | RST28F | 1420–2184 | 1802 | 115 | £95 | 24V/2.9A/70W / 28V/4.0A/112W | Natural warmth + Dome warmth | RS125P £55.21 (SI €64.95); RST28F £39.91 (SI €46.95) |
| X294 | RS125P | DX25TG | 1180–2184 | 1682 | 114 | £74 | 24V/2.9A/70W / 28V/4.0A/112W | Natural warmth + Dome warmth | RS125P £55.21 (SI €64.95); DX25TG £18.44 (Willys) |
| X295 | RS125P | D2604/833 | 950–2184 | 1567 | 114 | £97 | 24V/3.0A/71W / 28V/4.0A/113W | Natural warmth + Dome warmth | RS125P £55.21 (SI €64.95); D2604/833 £41.88 (Willys) |
| X296 | RS125P | D2604/830 | 1260–2184 | 1722 | 114 | £88 | 24V/3.0A/73W / 28V/4.1A/115W | Natural warmth + Dome warmth | RS125P £55.21 (SI €64.95); D2604/830 £33.05 (Falcon) |
| X297 | RS125P | R2604/833 | 880–2184 | 1532 | 114 | £101 | 24V/3.0A/73W / 28V/4.1A/115W | Natural warmth + Ring rad detail | RS125P £55.21 (SI €64.95); R2604/833 £45.95 (Falcon) |
| X298 | RS125P | R2604/832 | 1000–2184 | 1592 | 114 | £94 | 24V/3.2A/77W / 28V/4.3A/119W | Natural warmth + Ring rad detail | RS125P £55.21 (SI €64.95); R2604/832 £38.95 (Falcon) |
| X299 | RS125P | H1189 | 1100–2184 | 1642 | 114 | £112 | 24V/3.0A/73W / 28V/4.1A/115W | Natural warmth + Dome warmth | RS125P £55.21 (SI €64.95); H1189 £56.92 (Falcon) |
| X300 | RS125P | SB21RDCN | 1700–2184 | 1942 | 91 | £97 | 24V/3.3A/79W / 28V/4.3A/121W | Natural warmth + Ring rad detail | RS125P £55.21 (SI €64.95); SB21RDCN £41.60 (Willys); Narrow window |
| X301 | RS125P | SB21SDC | 1440–2184 | 1812 | 108 | £84 | 24V/3.1A/75W / 28V/4.2A/117W | Natural warmth + Dome warmth | RS125P £55.21 (SI €64.95); SB21SDC £28.51 (Willys) |
| X302 | RS125P | SB29RDNC | 1160–2184 | 1672 | 114 | £110 | 24V/2.9A/70W / 28V/4.0A/112W | Natural warmth + Ring rad detail | RS125P £55.21 (SI €64.95); SB29RDNC £54.31 (Willys) |
| X303 | RS125P | SB29SDAC | 1200–2184 | 1692 | 114 | £90 | 24V/3.0A/71W / 28V/4.0A/113W | Natural warmth + Dome warmth | RS125P £55.21 (SI €64.95); SB29SDAC £34.30 (Willys) |
| X304 | RS125P | MDT22T | 1300–2184 | 1742 | 89 | £103 | 24V/3.0A/73W / 28V/4.1A/115W | Natural warmth + Dome warmth | RS125P £55.21 (SI €64.95); MDT22T £47.55 (Willys) |
| X305 | RS125P | MDT12 | 2000–2184 | 2092 | 89 | £95 | 24V/3.0A/73W / 28V/4.1A/115W | Natural warmth + Dome warmth | RS125P £55.21 (SI €64.95); MDT12 £39.50 (Willys); Tight window (distortion risk) |
| X306 | RS125P | NE19VTS | 1540–2184 | 1862 | 88 | £80 | 24V/3.2A/76W / 28V/4.2A/118W | Natural warmth + Wide dispersion | RS125P £55.21 (SI €64.95); NE19VTS £25.20 (Willys) |
| X307 | RS125P | NE25VTS | 1460–2184 | 1822 | 95 | £89 | 24V/3.1A/74W / 28V/4.2A/116W | Natural warmth + Wide dispersion | RS125P £55.21 (SI €64.95); NE25VTS £33.96 (SI €39.95) |
| X308 | RS125P | TD25F | 1800–2184 | 1992 | 109 | £81 | 24V/3.1A/75W / 28V/4.2A/117W | Natural warmth + Dome warmth | RS125P £55.21 (SI €64.95); TD25F £25.46 (SI €29.95); Narrow window |
| X309 | RS125P | D27TG35 | 1800–2184 | 1992 | 114 | £83 | 24V/2.9A/70W / 28V/4.0A/112W | Natural warmth + Dome warmth | RS125P £55.21 (SI €64.95); D27TG35 £27.52 (Willys); Narrow window |
| X310 | HiVi M5N | SB19ST | 1960–2185 | 2072 | 109 | £40 | 24V/3.4A/82W / 28V/4.4A/124W | Natural warmth + Wide dispersion | HiVi M5N £25.46 (SI €29.95); SB19ST £14.30 (Falcon); Tight window (distortion risk) |
| X311 | HiVi M5N | XT25TG | 880–2185 | 1532 | 117 | £55 | 24V/3.0A/73W / 28V/4.1A/115W | Natural warmth + Ring rad detail | HiVi M5N £25.46 (SI €29.95); XT25TG £29.90 (Falcon) |
| X312 | HiVi M5N | XT25BG | 1140–2185 | 1662 | 117 | £63 | 24V/3.0A/72W / 28V/4.1A/114W | Natural warmth + Ring rad detail | HiVi M5N £25.46 (SI €29.95); XT25BG £37.14 (Willys) |
| X313 | HiVi M5N | XT25SC90 | 1650–2185 | 1917 | 110 | £44 | 24V/3.2A/77W / 28V/4.2A/119W | Natural warmth + Ring rad detail | HiVi M5N £25.46 (SI €29.95); XT25SC90 £18.20 (Falcon) |
| X314 | HiVi M5N | XT25SC40 | 2036–2185 | 2110 | 86 | £51 | 24V/2.9A/70W / 28V/4.0A/112W | Natural warmth + Ring rad detail | HiVi M5N £25.46 (SI €29.95); XT25SC40 £25.46 (SI €29.95); Tight window (distortion risk) |
| X315 | HiVi M5N | XT19TD | 1640–2185 | 1912 | 112 | £55 | 24V/3.4A/81W / 28V/4.4A/123W | Natural warmth + Ring rad detail | HiVi M5N £25.46 (SI €29.95); XT19TD £29.71 (SI €34.95) |
| X316 | HiVi M5N | SB26ADC | 1360–2185 | 1772 | 117 | £67 | 24V/3.2A/77W / 28V/4.3A/119W | Natural warmth + Dome warmth | HiVi M5N £25.46 (SI €29.95); SB26ADC £41.60 (Willys) |
| X317 | HiVi M5N | SB26STCN | 1900–2185 | 2042 | 101 | £54 | 24V/3.0A/73W / 28V/4.1A/115W | Natural warmth + Dome warmth | HiVi M5N £25.46 (SI €29.95); SB26STCN £28.92 (Willys); Tight window (distortion risk) |
| X318 | HiVi M5N | SB26ST | 1740–2185 | 1962 | 101 | £51 | 24V/3.0A/73W / 28V/4.1A/115W | Natural warmth + Dome warmth | HiVi M5N £25.46 (SI €29.95); SB26ST £25.30 (Willys); Narrow window |
| X319 | HiVi M5N | RST28F | 1420–2185 | 1802 | 117 | £65 | 24V/2.9A/70W / 28V/4.0A/112W | Natural warmth + Dome warmth | HiVi M5N £25.46 (SI €29.95); RST28F £39.91 (SI €46.95) |


---

## Supplier Notes (June 2026)

- **SoundImports** (EU) — primary source for most drivers
- **Falcon Acoustics** (UK) — SB19ST £14.30, XT25TG30-04 £29.90 (**in stock**), XT25SC90-04 £18.20, DX25TG59-04 £20.85; **Scan-Speak Discovery:** D2604/830000 £33.05, D2606/920000 £29.35, R2604/832000 £38.95, R2604/833000 £45.95 — all cheaper than SI by £4–8
- **Willys-Hifi** (UK) — full catalogue scraped Jun 2026. Key prices: DX25TG59-04 £18.44, SB12PFCR25-4 £20.58, SB12MNRX2-25-4 £48.10, SB13PFCR25-4 £24.50, SB12PACR25-4 £23.76, SB12NRXF25-4 £43.11, SB12NRX25-4 £45.75, SB19ST £20.14, SB26STCN-C000-4 £28.92, SB29SDAC £34.30, SB29RDNC £54.31, D2604/830000 £35.65, BC25SC06-04 £16.78, XT25SC90-04 £19.52, XT25TG30-04 £31.95, MDT12 £39.50, H26TG45-06 £31.80, SB29SDNC £56.64, NE19VTS-04 £25.20, NE25VTS-04 £36.44, SB26ADC £41.60, SB26ST-C000-5 £25.30, XT25BG60-04 £37.14, DC25T-8 £15.10, DT-25N £26.91, D27TG35-06 £27.52
- **Note (Jun 2026):** XT25TG30-04 now also in stock at SI (€49.95, 10+). Falcon £29.90 cheapest; Willys £31.95; SI most expensive. XT25SC90-04: Falcon £18.20 < Willys £19.52. DX25TG59-04: Willys £18.44 < Falcon £20.85 — **Willys is cheapest source for DX25**. **For Scan-Speak Discovery tweeters: Falcon is cheapest UK source.**
- **Audiophonics** (France) — SIG120-4 in stock; CF120-4 in stock (€49.92 sale); ships to UK
