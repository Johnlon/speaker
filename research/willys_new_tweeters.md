# Willys-Hifi New Tweeter Candidates — June 2026 Sweep

Drivers not yet in `si_tweeter_index.md`. Fetched from willys-hifi.com June 2026.
To merge: add rows to si_tweeter_index.md candidate table and create drivers.md entries for any passing initial screen.

**Exchange rate reference:** €1 ≈ £0.85 (June 2026)

---

## New Candidates (not in current index)

### SB Acoustics SB21RDCN-C000-4 — STAR: compact ring dome neodymium
- Type: Ring radiator (inverted centre phase plug free design) | Dome: 21 mm | Impedance: 4Ω | Re: 3.1Ω
- Sensitivity: **89.5 dB @ 2.83V/1m** | Power: **40W RMS** | Fs: **850 Hz** | Ferrofluid: Yes
- Faceplate OD: **58 mm** | Cutout: 40 mm | Neodymium magnet | CCAW voice coil | Copper cap
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/sb-acoustics-sb21rdcn-c000-4-tweeter) | Price: **£41.60** | Stock: UK in stock June 2026
- **Min xover:** 2× Fs = **1,700 Hz** — comfortable margin below 2,800 Hz target.
- **DSP correction vs TB sub (85 dB ref):** −4.5 dB pad.
- **Power at reference:** 98 dB → 5.3W (13% of 40W ✓). Burst 101 dB → 10.6W (26.5% ✓).
- **Centre spacing (FP OD 58mm):** DSA90-8 (92mm) → 75mm | DS115-8 (116mm) → 87mm | SB12PFCR25-4 (122mm) → 90mm
- **Why star:** 58mm FP is the most compact RING dome in the field — smaller than even CF18N-4 (58mm, dome). Ring radiator = wide off-axis dispersion at 60° kitchen position. 40W power rating. Neodymium motor. SB Acoustics quality.
- **vs SB21RDC-C000-4 (ferrite, £36.55):** Ferrite version has 92mm FP (much larger), 60W, Fs 760 Hz — less compact but higher power and £5 cheaper. For spacing, RDCN wins decisively at 58mm vs 92mm.
- **Datasheet:** Fetch from SB Acoustics website — doc.soundimports.nl pattern may have it.
- **Depth:** Not confirmed from page — verify before ordering.
- **Pairings enabled:** new XCR1 (DSA90-8 + SB21RDCN, 75mm spacing, 1,700–3,260 Hz window); XCR2 (DS115-8 + SB21RDCN, 87mm, 1,700–2,636 Hz); XCR3 (SB12PFCR25-4 + SB21RDCN, 90mm, 1,700–2,730 Hz)

---

### SB Acoustics SB21RDC-C000-4 — ring dome ferrite
- Type: Ring radiator (inverted centre phase plug free design) | Dome: 21 mm | Impedance: 4Ω | Re: 3.0Ω
- Sensitivity: **90 dB @ 2.83V/1m** | Power: **60W RMS** | Fs: **760 Hz** | Ferrofluid: Yes
- Faceplate OD: **92 mm** | Cutout: 64 mm | Ferrite magnet
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/sb-acoustics-sb21rdc-c000-4-tweeter) | Price: **£36.55** | Stock: UK in stock June 2026
- **Min xover:** 2× Fs = **1,520 Hz** — good margin.
- **DSP correction vs TB sub:** −5.0 dB pad.
- **Power at reference:** 98 dB → 5.0W (8.3% of 60W ✓). Burst 101 dB → 10.0W (16.7% ✓).
- **Centre spacing (FP OD 92mm):** DSA90-8 (92mm) → 92mm | DS115-8 (116mm) → 104mm | SB12PFCR25-4 (122mm) → 107mm
- **Why considered:** Same ring dome construction as RDCN but ferrite magnet and 92mm FP. At 92mm FP it's in the same spacing class as SB19ST (88mm). 60W is higher power than RDCN (40W). Cheaper at £36.55 vs £41.60.
- **vs SB21RDCN:** RDCN is the clear winner for spacing (58mm vs 92mm). Only prefer RDC if you need the 60W rating and spacing doesn't matter.

---

### Morel MDT22T — upgrade over MDT12, better Fs margin
- Type: Soft dome | Dome: 28 mm textile | Faceplate: **54 mm square** | Cutout: 44 mm | Impedance: 8Ω | Re: 5.2Ω
- Sensitivity: **89 dB @ 2.83V/1m** | Power: **80W RMS / 200W max** | Fs: **650 Hz** | Ferrofluid: Yes, ferrofluid-cooled copper VC
- Neodymium motor | Gold-plated input tags
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/morel-mdt22-soft-dome-tweeter) | Price: **£47.55** | Stock: UK in stock June 2026
- **Min xover:** 2× Fs = **1,300 Hz** — excellent; 1,500 Hz better margin than MDT12's 2,000 Hz.
- **DSP correction vs TB sub (85 dB ref):** −4.0 dB pad.
- **Power at 8Ω:** Available ~31W at 24V. Reference 98 dB → 7.9W (10% of 80W ✓). Burst 101 dB → 15.9W (20% ✓).
- **vs Morel MDT12 (already in index, £39.50):** MDT12: Fs 1,000 Hz (min xover 2,000 Hz), 28mm dome, 54mm sq FP, 80W, 19mm deep. MDT22T: Fs 650 Hz (min xover 1,300 Hz) — **700 Hz more crossover flexibility**. Same FP, same power, same dome. MDT22T costs £8 more. The MDT22T strictly supersedes MDT12 for builds where crossover is below 2,000 Hz; MDT12 is acceptable only when 2,000 Hz+ crossover is confirmed.
- **Depth:** Not confirmed from page — Morel MDT12 is 19mm deep; MDT22T likely similar, but verify.
- **Concern:** 28mm dome = narrower off-axis dispersion above ~6 kHz than 19mm dome. Same concern as RST28F-4.
- **Concern:** Square 54mm FP. Same geometry as TN25 (B6 pairing, 73mm spacing with DSA90-8). Spacing calc: (92+54)/2 = 73mm with DSA90-8.

---

### SB Acoustics SB29RDAC-C000-4 — ring dome ferrite, cheaper SB29RDNC alternative
- Type: Ring dome (inverted centre phase plug free design) | Dome: 29 mm | Impedance: 4Ω | Re: 3.0Ω
- Sensitivity: **93 dB @ 2.83V/1m** | Power: **100W RMS** | Fs: **600 Hz** | Ferrofluid: Yes
- Faceplate OD: **104 mm** | Cutout: 74 mm | CCAW voice coil, long life silver lead wires | Ferrite magnet
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/sb-acoustics-sb29rdac-c000-4-tweeter) | Price: **£44.39** | Stock: UK in stock June 2026
- **Min xover:** 2× Fs = **1,200 Hz**.
- **DSP correction vs TB sub:** −8.0 dB pad.
- **Power at reference:** 98 dB → 6.3W (6.3% of 100W ✓). Burst 101 dB → 12.6W (12.6% ✓). Indestructible.
- **vs SB29RDNC-C000-4 (£54.31 Willys, in index):** RDAC = ferrite magnet; RDNC = neodymium. Both ring dome 29mm 104mm FP. RDAC saves £9.92. Performance difference: neodymium version likely has stronger motor (better transient response) but both have 100W rating. For this application, ferrite version is perfectly adequate.
- **Concern:** 104mm FP — large. Same spacing class as DX25TG59-04, DX25TG59-04, SB29RDNC.

---

### Scanspeak D2604/833000 — Discovery Range, lower Fs than D2604/830000
- Type: Textile dome | Dome: 26 mm | Impedance: 4Ω | Re: 2.8Ω
- Sensitivity: **93 dB @ 2.83V/1m** | Power: **100W RMS** | Fs: **475 Hz** | Ferrofluid: No
- Faceplate OD: **104 mm** | Cutout: 72 mm | "Tuned rear chamber" | "Wide surround"
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/scanspeak-d2604-833000-tweeter) | Price: **£41.88** | Stock: UK in stock June 2026
- **Min xover:** 2× Fs = **950 Hz** — lowest of any dome tweeter candidate in the entire field.
- **DSP correction vs TB sub:** −8.0 dB pad.
- **Power at reference:** 98 dB → 5.0W (5% of 100W). Burst 101 dB → 10.0W (10%). Indestructible.
- **vs D2604/830000 (£35.65 Willys, in index):** 830000 has Fs ~630 Hz (min xover ~1,260 Hz), 92 dB, 104mm FP, 100W. 833000 has Fs 475 Hz (min xover **950 Hz**) — 310 Hz lower minimum crossover, 1 dB more sensitive. Costs £6.23 more. The 833000 is the better performer for any pairing needing sub-1,200 Hz crossover to tweeter — opens up compatibility with large 5"+ mids.
- **Dome colour:** Not confirmed. "Textile" dome — likely dark.
- **Depth:** Not specified — need datasheet.

---

### Scanspeak D2008/852100 — Classic Range, 20mm dome, 8Ω (PENDING verification)
- Type: Coated textile dome | Dome: 20 mm | Impedance: 8Ω | Re: 5.9Ω | Qts: 0.49 | Vas: 0.01 L
- Sensitivity: **89 dB @ 2.83V/1m** | Power: **90W RMS** | Fs: **550 Hz** | Sd: 3.8 cm² | BL: 2.4 Tm
- Faceplate OD: **92 mm** | Cutout: 68 mm | Neodymium | Dual rear chambers | Wide dispersion, vented pole piece
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/scanspeak-d2008-852100-classic-range) | [Scan-Speak](https://www.scan-speak.dk/product/d2008-852100/) | Price: **£57.88** | Stock: UK in stock June 2026
- **Min xover:** 2× Fs = **1,100 Hz** — very good margin.
- **DSP correction vs TB sub:** −4.0 dB pad.
- **Power at 8Ω:** Available ~31W at 24V. Reference 98 dB → 7.9W (8.8% of 90W ✓). Burst 101 dB → 15.9W (17.7% ✓).
- **⚠️ Critical concern:** Willys page recommends 4 kHz / 12 dB crossover. If the FR rolls off significantly below 4 kHz, crossing at 2,800 Hz would introduce a dip. **MUST verify FR curve from Scanspeak datasheet before ordering.** If FR is flat to 2.8 kHz, this is an excellent candidate. If it rolls off below 4 kHz, it is rejected.
- **Why interesting:** 20mm dome (one step above 19mm ≤ideal) with 90W and Fs 550 Hz. Classic-range Scanspeak build quality. 92mm FP = compact footprint matching SB21RDC.
- **Action required:** Download Scanspeak datasheet PDF; confirm FR ≥ −3 dB at 2,800 Hz before adding to main index.

---

### SB Acoustics SB26STAC-C000-4 — now in stock at Willys (was OOS at SI)
- Type: Soft dome | Dome: 26 mm fine weave soft fabric | Impedance: 4Ω | Re: 3.2Ω
- Sensitivity: **91.5 dB @ 2.83V/1m** | Power: **120W RMS** | Fs: **750 Hz** | Ferrofluid: Yes
- Faceplate OD: **100 mm** | Cutout: 74 mm | Copper cap | CCAW VC
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/sb-acoustics-sb26stac-c000-4-tweeter) | Price: **£37.64** | Stock: UK in stock June 2026 (was OOS at SoundImports exp Aug 2026)
- **Min xover:** 2× Fs = **1,500 Hz**.
- **DSP correction vs TB sub:** −6.5 dB pad.
- **Power at reference:** 98 dB → 4.4W. Burst 101 dB → 8.8W. Indestructible at 120W.
- **vs SB26STCN-C000-4 (£28.92 Willys, confirmed in index):** STCN has 92 dB, 120W, 72mm FP, Fs 950 Hz. STAC has 91.5 dB, 120W, 100mm FP, Fs 750 Hz. STAC gives better Fs margin (1,500 Hz min xover vs 1,900 Hz) but STCN is smaller (72 vs 100mm FP → tighter spacing) and £8.72 cheaper. STCN wins on spacing and price. STAC only preferred if Fs margin below 1,900 Hz is specifically needed.

---

## Rejected

| Model | Willys price | Reason |
|-------|-------------|--------|
| BC25SC08-04 | £24.64 (stock unclear) | Fs 1,663 Hz → min xover 3,326 Hz — exceeds 2,800 Hz project target |
| Monacor DT-99 | £26.30 | Fs 1,500 Hz → min xover 3,000 Hz marginal; 100mm FP not compact; 8Ω |
| Monacor DT-100 | £28.27 | Fs 1,500 Hz → 3,000 Hz marginal; 115×80mm rectangular FP incompatible |
| Monacor DT-105 | £26.90 | Specs unknown — assumed similar to DT-99; skip pending datasheet |
| SB14ST-C000-4 | £22.56 | Power only 10W RMS; cylindrical KEF-replacement capsule, not flat-baffle mount |
| SB21SDCN-C000-4 | £31.02 | IN STOCK at Willys (was OOS at SI exp Aug 2026). Neodymium version of SB21SDC (already in index). Specs likely similar to SB21SDC (Fs 720 Hz, 92mm FP, 40W) but verify. Add to index candidates with Willys £31.02 price. |

Note on SB21SDCN: the last row above is NOT a full rejection — re-evaluate this one. It was excluded from SI index only for OOS status. Now that Willys has it in stock, it should be screened against SB21SDC specs. Likely very similar to SB21SDC with neodymium motor (lighter, slightly different BL curve).

---

## Price / Stock Corrections for Indexed Drivers

| Model | SI price | Willys price | Saving | Notes |
|-------|---------|-------------|--------|-------|
| D27TG35-06 | €39.95 (≈£34.0) | **£27.52** | £6.5 | Update drivers.md price; Willys is preferred source |
| SB29SDAC-C000-4 | €44.95 (≈£38.2) | **£34.30** | £3.9 | Update drivers.md / si_tweeter_index.md |
| SB26STCN-C000-4 | €36.45 (≈£31.0) | **£28.92** | £2.1 | Update index |
| D2604/830000 | €44.95 (≈£38.2) | **£35.65** | £2.6 | Update index |
| SB26ST-C000-5 | €30.95 (≈£26.3) | **£25.30** | £1.0 | Update index |
| D2606/920000 | €39.95 (≈£34.0) | **£31.02** | £3.0 | Update index |
| SB19ST-C000-4 | €21.45 (≈£18.2) | £20.14 | — | SI is slightly cheaper at current rate |
| NE25VTS-04 | €39.95 (≈£34.0) | £36.44 | — | SI is cheaper |
| SB26ADC-C000-4 | €52.45 (≈£44.6) | £41.60 | £3.0 | Update index |
| SB29RDNC-C000-4 | €68.45 (≈£58.2) | **£54.31** | £3.9 | Update index |
| XT25BG60-04 | €41.28 (≈£35.1) | £37.14 | — | Similar; SI slightly cheaper |
| SB21SDC-C000-4 | €39.95 (≈£34.0) | **£28.51** | £5.5 | Update index — Willys notably cheaper |

---

## Willys-Hifi Notable Out of Stock

| Model | Status |
|-------|--------|
| XT19TD00-04 | Sold Out at Willys (and OOS at SI) |
| SB26STC-C000-4 | Sold Out at Willys |
| BC20SC15-04 | £10.76 at Willys — specs not fetched; possibly very budget tweeter |

*Sources: willys-hifi.com product pages fetched June 2026*
