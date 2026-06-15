# Willys-Hifi New Tweeter Candidates — June 2026 Sweep

Drivers not yet in `si_tweeter_index.md`. All specs confirmed from manufacturer datasheets unless marked ?.
Datasheets stored in `research/` where obtained.
To merge: add rows to si_tweeter_index.md candidate table; create drivers.md entries for any passing initial screen.

**Exchange rate reference:** €1 ≈ £0.85 (June 2026)

---

## Index Table (si_tweeter_index.md format)

| Model | Type | Imp | Price | Stock | Fs Hz | Sens dB | Pwr W | FP OD mm | FP Shape | Dome mm | Dome Col | Min Xover Hz | Status |
|-------|------|-----|-------|-------|-------|---------|-------|----------|----------|---------|----------|--------------|--------|
| SB21RDCN-C000-4 | Ring Rad | 4Ω | £41.60 Willys | UK stock | 850 | 89.5 | 40 | 58 | Round | 21 | Dark | 1,700 | ★ most compact ring dome; 38mm cutout; 22.7mm deep |
| SB21RDC-C000-4 | Ring Rad | 4Ω | £36.55 Willys | UK stock | 760 | 90 | 40 | 92 | Round | 21 | Dark | 1,520 | ~ ferrite; same FP class as SB19ST; 40W (Willys says 60W — wrong); 30.6mm deep |
| Morel MDT22T | Dome | 8Ω | £47.55 Willys | UK stock | 650 | 89 | 80 | 54×54 | Square | 28 | Dark | 1,300 | ~ upgrade over MDT12 on Fs; same FP; but 55mm deep (vs MDT12 19mm) |
| SB29RDAC-C000-4 | Ring Rad | 4Ω | £44.39 Willys | UK stock | 600 | 93 | 100 | 103.8 | Round | 29 | Dark | 1,200 | ~ ferrite alt to SB29RDNC (£54.31); 70mm cutout (not 74 as Willys says); 37.25mm deep |
| SS D2604/833000 | Dome | 4Ω | £41.88 Willys | UK stock | 475 | 93 | 100 | 104.2 | Round | 26 | Dark | 950 | ★ lowest Fs dome in field; 74mm cutout; 55mm deep (tuned chamber); min xover 2.5kHz per SS |
| SS D2008/852100 | Dome | 8Ω | £57.88 Willys | UK stock | 550 | 89 | 90 | 92 | Round | 20 | Dark | 1,100 | ? FR at 2.8kHz unverified — Willys recommends 4kHz xover; datasheet needed |
| SB26STAC-C000-4 | Dome | 4Ω | £37.64 Willys | UK stock | 750 | 91.5 | 120 | 100 | Round | 26 | Dark | 1,500 | ~ in stock at Willys (OOS at SI); inferior to SB26STCN (72mm FP £28.92) on spacing |

SS = Scan-Speak

---

## Full Entries — Confirmed from Datasheets

### SB Acoustics SB21RDCN-C000-4 ★ — compact ring dome neodymium
- Type: Ring radiator | Dome: 21 mm fabric | Impedance: 4Ω | Re: 3.1Ω | Le: 0.04 mH
- Sd: 4.6 cm² | VC diameter: 20.4 mm | VC height: 1.5 mm | Air gap: 2.0 mm | Xlin (p-p): 0.5 mm
- Mms: 0.25 g | BL: 1.3 Tm | Qms: 2.71 | Qes: 2.45 | Qts: 1.28 | Flux density: 0.9 T
- Sensitivity: **89.5 dB @ 2.83V/1m** | Power: **40W** (IEC HP Butterworth 2600 Hz 12dB/oct) | Fs: **850 Hz**
- Faceplate OD: **58.0 mm** (+0.1/-0.2) round | Cutout: **38.25 mm** | Total depth: **22.7 mm** | Protrusion: **3.2 mm**
- Below-baffle depth: **~19.5 mm** | Net weight: **0.06 kg** (neodymium — very light)
- Dome colour: **Dark** (black ring fabric, confirmed from datasheet photo)
- Magnetically shielded: No (neodymium compact motor)
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/sb-acoustics-sb21rdcn-c000-4-tweeter) | **Datasheet:** [research/sb_acoustics_sb21rdcn-c000-4.pdf](sb_acoustics_sb21rdcn-c000-4.pdf) | [original URL](https://sbacoustics.com/wp-content/uploads/2020/04/SB21RDCN-C000-4.pdf)
- Price: **£41.60** | Stock: UK in stock June 2026
- **Min xover:** 2× Fs = **1,700 Hz**
- **DSP correction vs TB sub (85 dB ref):** −4.5 dB pad
- **Power at reference:** 98 dB → 5.3W (13% of 40W ✓). Burst 101 dB → 10.6W (26.5% ✓)
- **Centre spacing (FP OD 58mm):** DSA90-8 (92mm) → 75mm | DS115-8 (116mm) → 87mm | SB12PFCR25-4 (122mm) → 90mm
- **FR at 60°:** On-axis flat ~1kHz–15kHz; 30° tracks to ~5kHz; 60° (red) tracks to ~3kHz then diverges. At 2,800 Hz the 60° response is close to on-axis — excellent for kitchen position.
- **Why star:** Most compact ring dome in the project field. Ring radiator = wide off-axis. SB quality. Very shallow (22.7mm). Lightweight (60g). Neodymium.
- **Concern:** Qts 1.28 is high — typical for high-Fs tweeters, not a concern in use above 1,700 Hz.
- **Pairings enabled:** XCR1 (DSA90-8 + SB21RDCN: 75mm, 1700–3260 Hz); XCR2 (DS115-8 + SB21RDCN: 87mm, 1700–2636 Hz); XCR3 (SB12PFCR: 90mm, 1700–2730 Hz)

---

### SB Acoustics SB21RDC-C000-4 — ring dome ferrite
- Type: Ring radiator | Dome: 21 mm fabric | Impedance: 4Ω | Re: 3.1Ω | Le: 0.04 mH
- Sd: 4.6 cm² | VC diameter: 20.4 mm | VC height: 1.5 mm | Air gap: 2.5 mm | Xlin (p-p): 1.0 mm
- Mms: 0.25 g | BL: 1.5 Tm | Qms: 2.54 | Qes: 1.64 | Qts: 1.0 | Flux density: 1.02 T
- Sensitivity: **90 dB @ 2.83V/1m** | Power: **40W** (IEC HP Butterworth 2600 Hz 12dB/oct) | Fs: **760 Hz**
- ⚠️ Willys product page incorrectly states 60W — **manufacturer datasheet confirms 40W**
- Faceplate OD: **92.0 mm** (+0/-0.2) round | Cutout: **62.5 mm** | Total depth: **30.6 mm** | Protrusion: **3.3 mm**
- Below-baffle depth: **26.5 mm** | Net weight: **0.33 kg** (ferrite — heavy vs 0.06kg RDCN)
- Dome colour: **Dark** (dark ring fabric, confirmed from datasheet photo)
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/sb-acoustics-sb21rdc-c000-4-tweeter) | **Datasheet:** [research/sb_acoustics_sb21rdc-c000-4.pdf](sb_acoustics_sb21rdc-c000-4.pdf) | [original URL](https://sbacoustics.com/wp-content/uploads/2020/02/SB21RDC-C000-4.pdf)
- Price: **£36.55** | Stock: UK in stock June 2026
- **Min xover:** 2× Fs = **1,520 Hz**
- **DSP correction vs TB sub:** −5.0 dB pad
- **Power at reference:** 98 dB → 5.0W (12.5% of 40W ✓). Burst 101 dB → 10.0W (25% ✓)
- **Centre spacing (FP OD 92mm):** DSA90-8 → 92mm | DS115-8 → 104mm | SB12PFCR → 107mm
- **vs SB21RDCN:** Same ring dome diaphragm (Sd, VC identical), similar power (40W both), but: RDC has 92mm FP (vs 58mm for RDCN) → much less compact; RDC costs £5.05 less; RDC has lower Fs (760 vs 850 Hz → 1,520 vs 1,700 Hz min xover); RDC weighs 5.5× more (0.33 vs 0.06 kg, ferrite motor). For spacing, RDCN wins decisively. Only prefer RDC if you need marginally lower min xover and 92mm FP spacing is acceptable.

---

### Morel MDT22T — soft dome, upgrade over MDT12 on Fs but much deeper
- Type: Soft dome | Dome: 28 mm selected soft fabric | Impedance: 8Ω | Re: 5.2Ω | Le: 0.05 mH @ 1kHz
- VC diameter: 28 mm (1.125") | VC height: 2.5 mm | VC former: Aluminum | VC wire: Copper | 2 layers
- Mms: 0.47 g | BL: 2.8 N·A | Flux density (B): 1.4 T | Magnetic gap height: 2.5 mm | Sd: 6.0 cm²
- Q factors: **not published by Morel** (blank in datasheet)
- Sensitivity: **89 dB @ 1W/1m** | Power: **80W RMS** (nominal) / **500W** (transient 10ms) | Fs: **650 Hz**
- Frequency Response: **1,800–25,000 Hz** | Recommended crossover: 2.5 kHz / 12 dB
- Faceplate: **54.0 × 54.0 mm SQUARE** (R5.5mm corner radii) | Cutout: **Ø44.0 mm** (chassis OD)
- Total depth: **55 mm** (2.17") | Protrusion: **3 mm** (0.118") | Below-baffle depth: **52 mm**
- Mounting: Ø3.5mm holes on Ø43.5mm pitch circle (4 holes in corners of square faceplate)
- Dome colour: **Dark** (black soft fabric, confirmed from datasheet photo)
- Net weight: 0.09 kg | Magnetically shielded: Yes ("magnetically shielded for A/V systems")
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/morel-mdt22-soft-dome-tweeter) | **Datasheet:** [research/morel_mdt22t.pdf](morel_mdt22t.pdf) | [original URL](https://cdn.shopify.com/s/files/1/0809/2387/files/MOREL_MDT22_DATASHEET.pdf?v=1686654880)
- Price: **£47.55** | Stock: UK in stock June 2026
- **Min xover:** 2× Fs = **1,300 Hz**
- **DSP correction vs TB sub (85 dB ref):** −4.0 dB pad
- **Power at 8Ω:** Available ~31W at 24V. Reference 98 dB → 7.9W (10% ✓). Burst 101 dB → 15.9W (20% ✓)
- **Centre spacing (FP 54mm sq):** DSA90-8 (92mm) → 73mm | DS115-8 (116mm) → 85mm
- **vs Morel MDT12 (£39.50, in index):**
  - MDT12: Fs 1,000 Hz → 2,000 Hz min xover; total depth **19mm** (chamberless design)
  - MDT22T: Fs 650 Hz → 1,300 Hz min xover; total depth **55mm** (vented motor)
  - Same: 54mm sq FP, 28mm dome, 80W, dark fabric, ~89 dB sensitivity
  - MDT22T gives 700 Hz more crossover flexibility (very useful for large-cone mids) but is **36mm deeper** — a significant installation constraint
  - Choose MDT12 when depth is critical (<25mm behind baffle) and 2,000 Hz min xover is acceptable
  - Choose MDT22T when crossover must be below 2,000 Hz (e.g. pairing with a 5" mid that beams early), and 52mm behind-baffle depth is workable

---

### SB Acoustics SB29RDAC-C000-4 — ring dome ferrite, cheaper SB29RDNC alternative
- Type: Ring dome | Dome: 29 mm fabric | Impedance: 4Ω | Re: 3.0Ω | Le: 0.05 mH
- Sd: 9.6 cm² | VC diameter: 29.0 mm | VC height: 2.0 mm | Air gap: 2.5 mm | Xlin (p-p): 0.5 mm
- Mms: 0.45 g | BL: 2.4 Tm | Qms: 2.2 | Qes: 0.9 | Qts: 0.64 | Flux density: 1.1 T
- Sensitivity: **93 dB @ 2.83V/1m** | Power: **100W** (IEC HP Butterworth 2600 Hz 12dB/oct) | Fs: **600 Hz**
- Faceplate OD: **103.8 mm** (±0.15) round | Cutout: **70.0 mm** | Total depth: **37.25 mm** | Protrusion: **4.0 mm**
- ⚠️ Willys product page states cutout 74mm — **datasheet confirms 70mm**
- Below-baffle depth: **33.25 mm** | Net weight: **0.54 kg** | Mounting: 7× Ø4.2mm holes
- Cast aluminium faceplate
- Dome colour: **Dark** (dark ring fabric, confirmed from datasheet photo and features list "cast aluminium faceplate" implies separate dark dome ring)
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/sb-acoustics-sb29rdac-c000-4-tweeter) | **Datasheet:** [research/sb_acoustics_sb29rdac-c000-4.pdf](sb_acoustics_sb29rdac-c000-4.pdf) | [original URL](https://sbacoustics.com/wp-content/uploads/2025/03/SB29RDAC-C000-4.pdf)
- Price: **£44.39** | Stock: UK in stock June 2026
- **Min xover:** 2× Fs = **1,200 Hz**
- **DSP correction vs TB sub:** −8.0 dB pad
- **Power at reference:** 98 dB → 6.3W (6.3% of 100W ✓). Burst 101 dB → 12.6W (12.6% ✓). Indestructible.
- **vs SB29RDNC-C000-4 (£54.31 Willys, in index):** RDAC = ferrite; RDNC = neodymium. Both 100W, ~104mm FP, 29mm ring dome, Fs ~580–600 Hz. RDAC saves £9.92. Performance difference is motor topology only — both well within power limits for this project. RDAC weighs 0.54kg vs (expect) 0.3kg for RDNC.
- **Concern:** 104mm FP — large. Same spacing class as DX25TG59-04 etc.

---

### Scan-Speak Discovery D2604/833000 ★ — lowest Fs dome in field
- Type: Textile dome | Dome: 26 mm textile, wide surround | Impedance: 4Ω | Re: 2.8Ω | Le: 0.04 mH
- Sd: 8 cm² | Effective diaphragm diameter: 32 mm | Mms: 0.42 g | Cms: 0.27 mm/N | Rms: 0.49 kg/s
- BL: 2.2 Tm | Qms: 2.55 | Qes: 0.71 | Qts: 0.55 | Flux density: not stated | Vas: 0.02 L
- Sensitivity: **93 dB @ 2.83V/1m** | Power: **100W** (IEC 18.4) / **240W** (IEC 18.2) | Fs: **475 Hz**
- Operating frequency: **2,500–20,000 Hz** | Minimum crossover: **2.5 kHz / 2nd order Butterworth** (Scanspeak confirmed)
- Faceplate OD: **104.2 mm** (±0.20) round | Cutout: **74 mm** (r=37) | Total depth: **~55 mm** | Protrusion: **~5 mm**
- Below-baffle depth: **~50 mm** ("tuned rear chamber" for low Fs — significantly deeper than D2604/830000's 25.4mm)
- Mounting: 5× Ø4.2mm holes on 92mm pitch circle at 72° spacing
- Dome colour: **Dark** (dark textile, confirmed from product photo)
- Net weight: 0.8 kg
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/scanspeak-d2604-833000-tweeter) | **Datasheet:** [research/scanspeak_d2604-833000.pdf](scanspeak_d2604-833000.pdf) | [original URL](https://www.scan-speak.dk/datasheet/pdf/d2604-833000.pdf)
- Price: **£41.88** | Stock: UK in stock June 2026
- **Min xover:** 2× Fs = **950 Hz** — lowest of any dome candidate in the entire project field
- **DSP correction vs TB sub:** −8.0 dB pad
- **Power at reference:** 98 dB → 5.0W (5% of 100W). Burst 101 dB → 10.0W (10%). Indestructible.
- **FR notes:** On-axis rises from ~90dB at 2.5kHz to 93dB at 3–5kHz (typical dome rising response). At 2,800 Hz: ~91dB on-axis (1–2 dB below rated, rising to flat). 60° off-axis tracks well to ~5kHz. At 2,800 Hz the 60° response is close to on-axis. Scanspeak confirms operating from 2,500 Hz — our 2,800 Hz crossover is within spec.
- **vs D2604/830000 (£35.65 Willys, in index):** 830000 has Fs ~630 Hz (min xover ~1,260 Hz), 92 dB, 25.4mm depth. 833000 has Fs **475 Hz** (min xover **950 Hz**), 93 dB, **~55mm depth**. The 833000 gives 310 Hz more crossover window (opens up 5"+ mid pairings) for £6.23 more, but requires ~25mm more behind-baffle clearance. Choose 833000 when pairing with a 5" mid requiring sub-1,200 Hz tweeter crossover; choose 830000 for standard 4" mids where 1,260 Hz min xover is sufficient.

---

### Scan-Speak Classic D2008/852100 — PENDING FR verification
- Type: Coated textile dome | Dome: **20 mm** (3/4") | Impedance: 8Ω | Re: 5.9Ω
- Qt: 0.49 | Vas: 0.01 L | Sd: 3.8 cm² | BL: 2.4 Tm | Mms: not confirmed
- Sensitivity: **89 dB @ 2.83V/1m** | Power: **90W RMS** | Fs: **550 Hz**
- Neodymium | Dual rear chambers | Vented pole piece | Wide dispersion
- Faceplate OD: **92 mm** | Cutout: **68 mm** | Depth: not confirmed
- Dome colour: not confirmed from available sources
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/scanspeak-d2008-852100-classic-range) | [Scan-Speak](https://www.scan-speak.dk/product/d2008-852100/) | Price: **£57.88** | Stock: UK in stock June 2026
- **⚠️ Critical unresolved:** Willys page recommends 4 kHz crossover. Scan-Speak product page confirms Fs 550 Hz but does not state minimum operating frequency. Min xover (2× Fs) = 1,100 Hz but actual usable lower limit from FR curve unknown.
- **Action required before indexing:** Download Scanspeak D2008/852100 datasheet; confirm FR is not significantly rolled off at 2,800 Hz. If flat to 2.8 kHz → excellent candidate. If rolled: reject.
- **If verified:** DSP correction −4.0 dB; 8Ω available ~31W; ref 98dB→7.9W (8.8% of 90W); burst→15.9W (17.7%). Compact 92mm FP (same class as SB21RDC). 20mm dome = good off-axis. Deepest candidate by power rating at 90W/8Ω.

---

### SB Acoustics SB26STAC-C000-4 — now in stock at Willys
- Type: Soft dome | Dome: 26 mm fine weave soft fabric | Impedance: 4Ω | Re: 3.2Ω
- Sensitivity: **91.5 dB @ 2.83V/1m** | Power: **120W RMS** | Fs: **750 Hz** | Ferrofluid: Yes
- Faceplate OD: **100 mm** | Cutout: 74 mm | Copper cap | CCAW VC
- Dome colour: Dark (assumed from SB26 family — not explicitly confirmed for STAC)
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/sb-acoustics-sb26stac-c000-4-tweeter) | Price: **£37.64** | Stock: UK in stock June 2026 (was OOS at SoundImports exp Aug 2026)
- **Min xover:** 2× Fs = **1,500 Hz**
- **vs SB26STCN-C000-4 (£28.92 Willys, confirmed in index):** STCN: 92 dB, 120W, **72mm FP**, Fs 950 Hz (→1900 Hz). STAC: 91.5 dB, 120W, 100mm FP, Fs 750 Hz (→1500 Hz). STAC gives 400 Hz better Fs margin but is 28mm wider (tighter spacing lost) and £8.72 more. SB26STCN remains the better buy for most pairings. STAC only preferred if Fs below 1,900 Hz is specifically needed AND wider FP is not a concern.

---

## Rejected at Willys

| Model | Willys price | Reason |
|-------|-------------|--------|
| BC25SC08-04 | £24.64 (stock unclear) | Fs 1,663 Hz → min xover 3,326 Hz — exceeds 2,800 Hz project target |
| Monacor DT-99 | £26.30 | Fs 1,500 Hz → 3,000 Hz min xover (marginal); 100mm FP; 8Ω |
| Monacor DT-100 | £28.27 | Fs 1,500 Hz → 3,000 Hz; 115×80mm rectangular FP |
| Monacor DT-105 | £26.90 | Specs not confirmed; assumed similar to DT-99; skip |
| SB14ST-C000-4 | £22.56 | Power only 10W; cylindrical KEF-replacement capsule — not flat-baffle mount |

---

## Price / Stock Corrections for Already-Indexed Drivers

⚠️ **Willys product pages contain errors** — always verify against manufacturer datasheet.
Known Willys errors found during this sweep:
- SB21RDC-C000-4: Willys says 60W → datasheet says **40W**
- SB29RDAC-C000-4: Willys says 74mm cutout → datasheet says **70mm**

| Model | SI price | Willys price | Saving vs SI | Notes |
|-------|---------|-------------|------|-------|
| D27TG35-06 | €39.95 (≈£34.0) | **£27.52** | £6.5 | Best Willys price saving |
| SB29SDAC-C000-4 | €44.95 (≈£38.2) | **£34.30** | £3.9 | |
| D2606/920000 | €39.95 (≈£34.0) | **£31.02** | £3.0 | |
| SB29RDNC-C000-4 | €68.45 (≈£58.2) | **£54.31** | £3.9 | |
| SB26ADC-C000-4 | €52.45 (≈£44.6) | **£41.60** | £3.0 | |
| SB26STCN-C000-4 | €36.45 (≈£31.0) | **£28.92** | £2.1 | |
| D2604/830000 | €44.95 (≈£38.2) | **£35.65** | £2.6 | |
| SB26ST-C000-5 | €30.95 (≈£26.3) | **£25.30** | £1.0 | |
| SB21SDC-C000-4 | €39.95 (≈£34.0) | **£28.51** | £5.5 | Notable saving |
| SB19ST-C000-4 | €21.45 (≈£18.2) | £20.14 | — | SI cheaper |
| NE25VTS-04 | €39.95 (≈£34.0) | £36.44 | — | SI cheaper |
| XT25BG60-04 | €41.28 (≈£35.1) | £37.14 | — | Similar |

---

## Datasheets Saved to research/

| File | Driver | Source URL |
|------|--------|-----------|
| sb_acoustics_sb21rdcn-c000-4.pdf | SB21RDCN-C000-4 | sbacoustics.com/wp-content/uploads/2020/04/SB21RDCN-C000-4.pdf |
| sb_acoustics_sb21rdc-c000-4.pdf | SB21RDC-C000-4 | sbacoustics.com/wp-content/uploads/2020/02/SB21RDC-C000-4.pdf |
| sb_acoustics_sb29rdac-c000-4.pdf | SB29RDAC-C000-4 | sbacoustics.com/wp-content/uploads/2025/03/SB29RDAC-C000-4.pdf |
| scanspeak_d2604-833000.pdf | D2604/833000 | scan-speak.dk/datasheet/pdf/d2604-833000.pdf |
| morel_mdt22t.pdf | MDT22T | cdn.shopify.com/…/MOREL_MDT22_DATASHEET.pdf |

*Sources: willys-hifi.com + manufacturer datasheets, fetched June 2026*

---

## Seller Purchase Links & Pricing Reference

Direct links to purchase recommended drivers featured in this catalog:

### SB Acoustics SB21RDCN
- **SoundImports (EU):** [€59.95](https://www.soundimports.eu/en/sb-acoustics-sb21rdcn-c000-4.html)
- **Willys-Hifi (UK):** [£45.60](https://willys-hifi.com/products/sb-acoustics-sb21rdcn-c000-4-tweeter)

### Morel MDT22T
- **SoundImports (EU):** [€63.95](https://www.soundimports.eu/en/morel-mdt-22.html)
- **Willys-Hifi (UK):** [£48.00](https://willys-hifi.com/products/morel-mdt-22-tweeter)

### Scan-Speak R2604/833000
- **SoundImports (EU):** [€62.45 (~£53)](https://www.soundimports.eu/en/scan-speak-r2604-833000.html)
- **Willys-Hifi (UK):** [£46.00](https://willys-hifi.com/products/scan-speak-discovery-r2604-833000-dual-ring-tweeter)
- **Falcon Acoustics (UK):** [£45.95](https://www.falconacoustics.co.uk/scanspeak-r2604-833000-tweeter-discovery-range.html)

### SB Acoustics SB26STCN-C000-4
- **SoundImports (EU):** [€39.95](https://www.soundimports.eu/en/sb-acoustics-sb26stcn-c000-4.html)
- **Willys-Hifi (UK):** [£29.40](https://willys-hifi.com/products/sb-acoustics-sb26stcn-c000-4-tweeter)

