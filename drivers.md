# Driver Catalogue

Per-driver analysis: derived figures, power checks, DSP correction, decisions. Raw specs are in `research/si_tweeter_index.md` and `research/si_woofer_index.md`.

One entry per driver. Status: **Locked** / **Candidate** / **Rejected**.

---

## ✅ SELECTED SYSTEM (June 2026)

| Role | Driver | Key specs | Why |
|------|--------|-----------|-----|
| **Sub** | Tang Band **W5-1138SMF** | 85 dB, 40 W→98 dB / 80 W→101 dB, Fs 45, Xmax 9.25 mm, 4Ω | Locked anchor; sets the system output ceiling |
| **PR** | SB Acoustics **SB15SFCR-00** | racetrack, Sd 178 cm² (1.9× sub) | Tunes the sealed sub box; side/rear mount |
| **Mid** | SB Acoustics **SB12MNRX2-25-4** | **90.5 dB, 50 W, Fs 63.5, Xmax ±2.2 mm, Sd 50, 4Ω** | **Only 4" mid that matches the W5 burst** (max 104.5 dB) |
| **Tweeter** | SB Acoustics **SB19ST-C000-4** | **88.5 dB, 30 W, Fs 980, 4Ω, Ø88/Ø60** | Best-reputation 19 mm dome; adequate 60°; cheap |

**Crossovers (DSP, JAB5/ADAU1701):** sub→mid **150 Hz LR**; mid→tweeter **~2 kHz LR4 (24 dB/oct)**. Electronics: Sure JAB5 on 36 V PSU.

### Justification

**Governing requirement — match the W5 output** (98 dB @40 W RMS / 101 dB @80 W burst):
- **Mid:** Max SPL = sens + 10·log₁₀(P/P_ref). SB12MNRX2-25-4 = 90.5 + 10·log₁₀(50/2) = **104.5 dB** → covers the 101 dB burst by +3.5 dB. It is the **only 4" mid that reaches burst**; SB12PFCR25-4 / SB12NRX25-4 (87.5 dB/30 W) are power-limited at **99.3 dB (−1.7 dB)**, HiVi B4N (85/25) at 99.0. MNRX2 matches via sensitivity+power; its modest ±2.2 mm Xmax is still excursion-OK at the 150 Hz crossover (~105 dB at 150 Hz).
- **Tweeter:** SB19ST = 88.5 + 10·log₁₀(30/2) = **100.3 dB** (0.7 dB under burst — treble burst energy trivial → effectively matched).

**Crossover integrity:** mid Fs 63.5 → 150 Hz = **2.36×** (≥2× safe); mid beams ~2,730 Hz, tweeter safe min 2×Fs = 1,960 Hz → clean **~2 kHz LR4** window (1,960–2,180 Hz).

**Tweeter choice (SB19ST) — why over the alternatives:**
- Eliminated: **ring radiators** (R2604/XT25/etc.) ineligible — horn-like 60° off-axis (RAW-CAt Part 6); **NE19VTS-04** out — conflicting datasheets (88.3 vs 90.4 dB, 100 vs 20 W); **SB29RDNC** out — massive 60° top-octave dropout (owner-confirmed); **SB29SDAC** cliffs at 12 kHz; **ND13/16/20FA, PTMini** crossover-blocked (Fs too high → 4+ kHz min xover above any mid's beam); **Monacor DT-100/DT-28N** no off-axis data.
- Survivors were SB19ST / SB21SDCN / DC28FT (all fine off-axis per Zaph: 3/4" domes droop little; top-octave-at-60° is low priority). SB19ST chosen for **reputation + value** (Parts-Express test "near perfect to 30°"; "bargain"; £14–18) and owner preference; SB21SDCN is the compact runner-up (has independent HiFiCompass data).

### Evidence
- Off-axis / shootout / opinion analysis: [research/tweeter_offaxis_evidence.md](research/tweeter_offaxis_evidence.md) (UTS shootout, Zaph, HiFiCompass, datasheet polars read at 400 DPI).
- Datasheets: `research/speakers/` (SB19ST, SB21SDCN, SB12MNRX2, W5, etc.).
- FRD data store: `research/speakers/datafiles/` (Dayton official; SB19ST/SB21SDCN digitised).
- Datasheet-trust caveats: SB sheets read ~15° optimistic on angle; Dayton sheets over-smoothed — see evidence file.

---

## Power at Reference SPL — All Candidates

Sub at 40W → 98 dB @1m (RMS reference). Sub at 80W → 101 dB @1m (burst ceiling).
Formula: P_needed = (2.83² / R) × 10^((SPL_target − sensitivity) / 10)

| Driver | Role | Imp | Sensitivity | Needed @ 98 dB | Needed @ 101 dB | Available @ 24V | PSU (RMS / Burst) |
|--------|------|-----|-------------|----------------|-----------------|-----------------|-------------------|
| TB W5-1138SMF | Sub | 4Ω | 85 dB | 40W | 80W | ~61W | 20V / 28V |
| SIG120-4 | Mid | 4Ω | 89.7 dB | 13.5W | 27W | ~61W | 24V / 28V |
| DS115-8 | Mid | 8Ω | 85.3 dB | 18.6W | 37.2W | ~31W | 24V / 28V |
| HiVi B4N | Mid | 8Ω | 85 dB | 20.0W | 40W | ~31W | 24V / 28V |
| DSA90-8 | Mid | 8Ω | 84.7 dB | 21.4W | 42.8W | ~31W | 24V / 29V |
| TCP115-8 | Mid | 8Ω | 81.9 dB | 40.7W | 81.4W | ~31W | 28V / 36V* |
| SB19ST | Tweeter | 4Ω | 88.5 dB | 17.8W | 35.5W | ~61W | 24V / 28V |
| NE19VTS-04 | Tweeter | 4Ω | 90.4 dB | 11.5W | 23W (>20W rated) | ~61W | 24V / 28V |
| SB29SDNC | Tweeter | 4Ω | 95.5 dB | 3.6W | 7.1W | ~61W | 24V / 28V |
| Morel MDT12 | Tweeter | 8Ω | 89 dB | 7.9W | 15.9W | ~31W | 24V / 28V |

Total DC draw at matched 98 dB (RMS): ~78–90W from PSU (~3.5–4A at 24V). At sub burst (80W): ~120W peak (~5A at 24V) — within LRS-150-24 (6.5A) for music content. Capacitor bank absorbs transient peaks.

---

## Subwoofer

### Tang Band W5-1138SMF — LOCKED
- Role: **SUB** | Size: 5.25" | Frame OD: **155.8 mm** (datasheet drawing; cutout Ø120 mm) | Impedance: 4Ω
- Sensitivity: **85 dB @ 2.83V/1m** | Xmax: 9.25 mm | Power: 40W RMS / 80W max
- Fs: 45 Hz | Qts: 0.49 | Vas: 0.17 ft³ (4.81 L) | Sd: 94 cm² | Re: 3.4Ω
- Frequency range: 45–1,500 Hz | Sealed F3: 73 Hz | Vented F3: 35 Hz
- Surround sits ~8.5 mm proud of baffle when surface-mounted → reclaims ~160 mL internal volume
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/tang-band-w5-1138smf.html) (specs fetched June 2026)
- **Datasheet:** [research/tang_band_w5-1138smf.pdf](research/tang_band_w5-1138smf.pdf) | [original URL](https://www.tb-speaker.com/uploads/files/cadcecac0ea8af7e07014e520d4ea00d.pdf)
- **Manufacturer spec (confirmed):** Sensitivity **82 dB @ 1W/1m (= ~85.2 dB @ 2.83V/1m at 4Ω)**; Vas 4.85 L; Fs 45 Hz; Qts 0.49 (Qms 3.56, Qes 0.57); Mms 28.81 g; Cms 368.72 µm/N; Sd 0.0094 m²; Bl 7.17 Tm; Re 3.4Ω; Le 0.34 mH; Xmax 9.25 mm; 40W RMS / 80W max; VC 32 mm; range 45 Hz–1.5 kHz.
- **Measured data (FRD/ZMA/.sdrv, in-repo):** [research/measured/w5-1138smf/](research/measured/w5-1138smf/) — free-air response + impedance (single Z peak ~48 Hz confirms free-air). In the **6.33 L net PR box @ Fb 40 Hz, modelled F3 ≈ 42 Hz** (not 35 Hz — see [enclosure.md](enclosure.md)).
- SoundImports price: €54.95 | Stock (June 2026): 10+
- **Why locked:** Class-leading excursion for its size; round frame; dark/stealth motor. This is the performance anchor — all other driver choices are judged against its output capability.

---

## Passive Radiator

### SB Acoustics SB15SFCR-00 5×8" Racetrack — Candidate
- Role: **PR** | Shape: Oval racetrack | Sd ≈ 178 cm² (~2.05× the TB sub's Sd)
- Mounts vertically on side or rear panel
- Requires added mass to rear M6-threaded bolt to lower native tuning to 38 Hz
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/sb-acoustics-sb15sfcr-00.html) — fetch for confirmed Sd and mass range
- **Why liked:** Narrow profile fits on a slim cabinet side wall while providing sufficient Sd to couple correctly with the TB sub's 9.25 mm Xmax. Preferred for Option A (side-sub) layout.
- **Limitation:** Oval shape only suits Option A (side panels). Not an aesthetic fit for front-baffle layouts where circles are the theme.

### Dayton Audio ND140-PR — Candidate (dual-side configuration only)
- Role: **PR** | Shape: Round | Nominal diameter: 5.25" | **Confirmed Sd: 86.6 cm²** (single unit)
- Fs: 44.2 Hz | Mms: 16.4 g | Cms: 0.79 mm/N | Rms: 1.13 kg/s | Qms: 4.02 | Vas: 8.4 L | Xmax: 9 mm
- Added mass: **Includes two 18.5 g disc weights** with adjustable threaded rod — each can be fitted independently or combined (18.5 g or 37 g total per unit)
- Supplier: [SoundImports](https://www.soundimports.eu/en/dayton-audio-nd140-pr.html) | Price: **€16.49** (sale; regular €19.95) | Stock (June 2026): 10+
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/dayton-audio-nd140-pr.html) (specs fetched June 2026)
- **Single-unit rejection reason:** One ND140-PR has confirmed Sd = 86.6 cm², only ~0.92× the TB sub's Sd (94 cm²). This is actually less than the sub's piston area — a single PR would be seriously underspecified and prone to over-excursion.
- **Dual-unit reconsideration:** Two ND140-PRs mounted one on each side panel give combined Sd = 173.2 cm² — close to the SB15SFCR racetrack (178 cm²) and 1.84× the sub's 94 cm² Sd. This is acoustically workable given the sub's 9.25 mm Xmax.
- **Why this is interesting:** If the sub is front-mounted (Option B/C layout), two matching round PRs on the side panels are visually harmonious with the all-circles design language. The ND140-PR's round shape is a better aesthetic fit than the racetrack SB15SFCR on the sides, which would look asymmetric against a circular front baffle.
- **Requirements for dual configuration:** Both PRs must be loaded with the same added mass (calculated to tune the combined system to 38 Hz), and both must be mechanically free to move (not obstructed by internal bracing). With Mms 16.4 g stock and 18.5 g / 37 g available added mass, tuning calculation needed before committing.

---

## Tweeters

> **Ring radiators are INELIGIBLE.** Measured 60° off-axis dispersion is poor — comparable to horns, with large deviation already at 30° and severe HF rolloff by 60° (RAW-CAt Ultimate Tweeter Shootout Part 6, Nov 2025). For the 60° kitchen listening geometry this is disqualifying. Small-diaphragm soft-dome tweeters give the widest measured off-axis dispersion and are preferred. This applies to every driver whose type is "ring radiator" (Peerless XT25/XT19 family, Scan-Speak R-series, SB Acoustics SB21RDC/RDCN). "Ring dome" devices are a separate construction and remain candidates, but carry no off-axis advantage.

### Peerless by Tymphany XT25BG60-04 — INELIGIBLE (ring radiator — poor 60° off-axis)
- Role: **HIGH** | Type: **Ring radiator**, fabric diaphragm | VC: 25 mm | Faceplate OD: **104.5 mm** | Cutout: 73 mm | Depth: 67 mm | Impedance: 4Ω
- Sensitivity: **92.6 dB @ 2.83V/1m** | Power: **15W RMS** | Fs: **570 Hz** | Frequency response: flat well beyond 20 kHz
- Ferrite magnet | Rear chamber | Patented dual concentric diaphragm with waveguide
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/peerless-by-tymphany-xt25bg60-04.html) (fetched June 2026)
- **Datasheet:** download to research/ on order (doc.soundimports.nl pattern)
- SoundImports price: **€41.28** (10+ in stock) | June 2026
- **DSP correction vs TB sub (85 dB ref):** −7.6 dB pad needed.
- **Power at reference:** 98 dB from 92.6 dB → needs **6.9W** RMS (46% of 15W ✓) | burst 101 dB → **13.8W** (92% of 15W — within rating, just) | DSP limiter at 14W gives small margin.
- **Ineligible — off-axis:** Ring radiator. Measured 60° off-axis dispersion is horn-like — severe HF rolloff by 60° (RAW-CAt Tweeter Shootout Part 6, Nov 2025). Disqualifying for the 60° kitchen geometry regardless of its otherwise good power match (13.8W at burst vs 15W rating).

### Peerless by Tymphany XT19TD00-04 — INELIGIBLE (ring radiator — poor 60° off-axis)
- Role: **HIGH** | Type: **Ring radiator**, dual concentric diaphragm + waveguide | VC: 19 mm | Faceplate OD: **94 mm** | Cutout: 68 mm | Depth: 44 mm | Impedance: 4Ω
- Sensitivity: **88.9 dB @ 2.83V/1m** | Power: **20W RMS** | Fs: **730 Hz** | Re: 2.9Ω | Qms: 3.1 | Qes: 0.888 | Qts: 0.69 | Le: 0.014 mH | Fabric diaphragm | Frequency response: 800–20,000 Hz
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/peerless-by-tymphany-xt19td00-04.html) (fetched June 2026)
- SoundImports price: **€28.88** (10+ in stock) | June 2026
- **⚠ Datasheet note:** `research/peerless_xt19td00-04.pdf` is a mislabeled file for a different driver (small conventional dome, 43mm OD). Correct datasheet not yet obtained.
- **DSP correction vs TB sub (85 dB ref):** −3.9 dB pad needed.
- **Power at reference:** 98 dB from 88.9 dB → needs **16.2W** RMS (81% of 20W ✓) | burst 101 dB → **32.3W** (exceeds 20W — DSP limiter mandatory at ≤19W, max tweeter SPL 98.9 dB)
- **Ineligible — off-axis:** Ring radiators measure poorly at 60° — comparable to horns, severe HF rolloff (RAW-CAt Tweeter Shootout Part 6, Nov 2025). Disqualifying for the 60° kitchen geometry.

### Peerless by Tymphany XT25TG30-04 — INELIGIBLE (ring radiator — poor 60° off-axis)
- Role: **HIGH** | Type: **Ring radiator** (dual concentric diaphragm, central waveguide) | VC: 25 mm | Faceplate OD: **104 mm** | Cutout: 73 mm | Depth: 51.7 mm | Impedance: 4Ω
- Sensitivity: **91.9 dB @ 2.83V/1m** | Power: **15W RMS** | Fs: **440 Hz** | Re: 3.1Ω | Frequency response: 800–20,000 Hz
- Qts: 0.44 | Le: 0.009 mH | Ferrite magnet | Rear chamber | No ferrofluid
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/peerless-by-tymphany-xt25tg30-04.html) (specs fetched June 2026)
- **Datasheet:** [original URL](https://doc.soundimports.nl/pdf/brands/Peerless%20by%20Tymphany/XT25TG30-04/XT25TG30-04.pdf) — download to research/ on order
- SoundImports price: €49.95 (**10+ in stock**, Jun 2026) | Falcon Acoustics price: **£29.90** (in stock, UK) | Falcon is cheaper
- **DSP correction vs TB sub (85 dB ref):** −6.9 dB pad needed.
- **Power at reference:** 98 dB from 91.9 dB driver → needs 8.2W RMS (54% of 15W rating ✓) | burst 101 dB → 16.3W (exceeds rating — see below)
- **DSP limiter:** Set tweeter channel at 13W → maximum tweeter SPL = 91.9 + 10×log(13/2) = **100.0 dB**. Sub peaks at 101 dB. 1 dB gap at burst, irrelevant in practice (bass transients, not treble).
- **Ineligible — off-axis:** Ring radiator. Despite the lowest Fs of any tweeter in the field (440 Hz → 880 Hz min crossover, compatible with every mid including 5"+ beamers), its 60° off-axis dispersion is horn-like (RAW-CAt Tweeter Shootout Part 6, Nov 2025) — disqualifying for the 60° kitchen geometry.
- **Concern — power:** 15W rating is the same as DX25TG59-04 but sensitivity is 1.5 dB lower, so it needs more power for the same SPL. DSP limiter at 13W is essential. DX25TG59-04 has more headroom at the same rating because of its higher sensitivity.
- **Concern — faceplate size:** 104 mm OD is the widest tweeter in the candidate field. Same as DX25TG59-04 and D27TG35-06. Cabinet baffle must be at least 190 mm wide to fit alongside any standard 4" mid.

### Peerless by Tymphany XT25SC90-04 — INELIGIBLE (ring radiator — poor 60° off-axis)
- Role: **HIGH** | Type: **Ring radiator** (dual concentric diaphragm, central waveguide) | VC: 25 mm | Faceplate OD: ? (unconfirmed — fetch datasheet) | Impedance: 4Ω
- Sensitivity: **90.1 dB @ 2.83V/1m** | Power: **100W RMS** | Fs: **825 Hz** | Re: 3.2Ω
- Qts: 0.93 | Qes: 1.007 | Qms: 7.2 | No ferrofluid | Rear chamber
- **Source:** Falcon Acoustics product page (fetched June 2026)
- Falcon Acoustics price: **£18.20** (in stock, UK) | SoundImports: not confirmed | June 2026
- **DSP correction vs TB sub (85 dB ref):** −5.1 dB pad needed.
- **Power at reference:** 98 dB → 12.3W (12.3% of 100W ✓) | burst 101 dB → 24.5W (24.5% ✓). Large power headroom.
- **Ineligible — off-axis:** Ring radiator. Strong on paper (Fs 825 Hz, 100W, cheapest-but-one at £18.20), but its 60° off-axis dispersion is horn-like (RAW-CAt Tweeter Shootout Part 6, Nov 2025) — disqualifying for the 60° kitchen geometry.

### SB Acoustics SB19ST-C000-4 — ✅ SELECTED (tweeter) — see Selected System at top
- Role: **HIGH** | Dome: 19 mm fine weave soft fabric | Faceplate OD: **88 mm** | Cutout: **60 mm** | Depth: **21 mm** | Bolt circle: 78 mm | 4× M4 holes | Impedance: 4Ω
- Sensitivity: 88.5 dB @ 2.83V/1m | Power: **30W RMS** | Fs: **980 Hz** | Re: 3.4Ω | Le: 0.07 mH | Sd: 3.8 cm² | Qts: 1.22 | Qes: 1.50 | Qms: 6.45 | Bl: 1.75 Tm | Mms: 0.22 g | B: 1.24 T
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/sb-acoustics-sb19st-c000-4.html) (specs fetched June 2026)
- **Datasheet:** [research/sb_acoustics_sb19st-c000-4.pdf](research/sb_acoustics_sb19st-c000-4.pdf) | [Falcon Acoustics PDF](https://www.falconacoustics.co.uk/downloads/SBA/SB19ST-C000-4.pdf) (downloaded June 2026)
- SoundImports price: €21.45 | Stock (June 2026): 10+
- **DSP correction vs TB sub (85 dB ref):** −3.5 dB pad needed.
- **Off-axis gate — SATISFIED:** Datasheet (Falcon Acoustics, REV.2 2014) shows Blue=on-axis, Green=30°, Red=60°. At 13 kHz, 60° (red) curve is **5–6 dB below on-axis** — confirmed by owner reading (June 2026). Similar to SB21SDCN at 6 dB. Acceptable for 60° kitchen use.
- **Crossover constraint — Fs 980 Hz:** 3×Fs = 2,940 Hz (preferred floor). Most 4" mids beam by ~2,500 Hz → 3×Fs exceeds mid ceiling → **INCOMPATIBLE with 4" mids at preferred crossover**. Marginal at 2×Fs (1,960 Hz) with a 3" mid or high-f_beam 4" mid only. Crossover window per pairing must be calculated in combos.md.
- **Why liked:** 19mm dome, smallest Sd (3.8 cm²) of all confirmed candidates — widest dispersion. Warm fabric character. 21mm depth is the shallowest tweeter in the field. 30W power rating comfortable. 88mm round faceplate.

### SB Acoustics SB26ADC-C000-4 — Candidate
- Role: **HIGH** | Dome: 26 mm aluminium (copper cap) | Faceplate OD: ? (unconfirmed — fetch datasheet) | Impedance: 4Ω
- Sensitivity: 90 dB @ 2.83V/1m | Power: 120W RMS | Fs: 680 Hz | Re: 3.2Ω | Xmax: 0.6 mm | Sd: 6.2 cm²
- Qts: 1.20 | Qes: 2.0 | Qms: 2.9 | Mms: 0.38 g
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/sb-acoustics-sb26adc-c000-4.html) (specs fetched June 2026)
- SoundImports price: €52.45 | Stock (June 2026): 10+
- **DSP correction vs TB sub (85 dB ref):** −5.0 dB pad needed
- **What's good:** 120W RMS — effectively indestructible. Fs 680 Hz → min crossover 1,360 Hz.
- **Concern:** Aluminium dome sounds brighter/harder than the warm fabric character this project targets. At €52.45 it takes most of the £75 budget, leaving little for the mid.

### HiVi TN25 — Candidate (owner-accepted visual)
- Role: **HIGH** | Dome: 25 mm fabric | Faceplate: 54.1 × 54.1 mm square (2.13") | Impedance: 5Ω | Re: 4.6Ω
- Sensitivity: 91 dB @ 2.83V/1m | Power: 20W RMS | Fs: 1,500 Hz | Frequency response: 2,500–22,000 Hz
- Cutout: 42.9 mm (1.69") | Depth: 63.5 mm (2.50")
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/hivi-tn25.html) (specs fetched June 2026)
- **Datasheet:** [research/hivi_tn25.pdf](research/hivi_tn25.pdf) | [original URL](https://doc.soundimports.nl/pdf/brands/HiVi/TN25/pdf_HiVi_TN25_1.pdf) (image-based PDF, downloaded June 2026)
- SoundImports price: €25.45 | Stock (June 2026): 5
- **Note:** Square 54.1×54.1mm faceplate; non-standard shape.
- **DSP correction vs TB sub (85 dB ref):** −6.0 dB pad needed.
- **Impedance note:** 5Ω — at 24V the JAB5 delivers ≈49W into 5Ω; 8W needed to match reference level. Ample headroom.
- **Acoustic concern — Fs/crossover ratio:** Fs 1500 Hz vs a typical 2500–3000 Hz crossover = ~1.8× margin. This is the tightest of all active tweeter candidates. The TN25's specified response starts at 2500 Hz. The LR48 48 dB/oct HP filter provides mechanical protection, but the comfort margin here is smaller than ideal. The Monacor DT-25N was rejected on similar grounds (Fs 1600 Hz, 1.75× ratio, response start 1600 Hz). TN25 is marginally better but the same concern applies.
- **Depth note:** 63.5 mm depth is roughly double the SB19ST (≈35 mm). Verify against tweeter chamber depth in the enclosure layout before ordering.

### Dayton Audio ND25FA-4 — Candidate
- Role: **HIGH** | Dome: 25 mm soft dome (neodymium) | Faceplate OD: 66 mm (2.60") round | Impedance: 4Ω
- Sensitivity: 90 dB | Power: 20W RMS | Fs: 1350 Hz | Qts: 1.56 | Qes: 2.61 | Qms: 3.87
- Re: 3.20Ω | Le: 0.48 mH | Cutout: 45 mm | Depth: 25 mm
- Supplier: [SoundImports](https://www.soundimports.eu/en/dayton-audio-nd25fa-4.html) | Price: €15.95 | Stock: 10+
- **Why liked:** Compact round faceplate (66 mm OD) — smallest footprint of any candidate tweeter. 90 dB sensitivity exceeds the 85 dB sub reference and is only 1.5 dB below the SB19ST. Neodymium motor for tight, efficient operation. Budget-friendly at €15.95. Fs 1350 Hz gives comfortable room below target crossovers.
- **Concern:** Dome colour not confirmed from product page text — likely dark/black based on neodymium compact design. Power at 20W RMS is modest (same as SB19ST-C000-4). Qts 1.56 is high; needs to be used above its Fs by a comfortable margin, which is met at target crossovers. **Recommend confirming dome colour before ordering.**
- **Note:** Dome colour could not be confirmed from web content; manufacturer datasheet confirms it as a black soft dome. Sensitivity at 2.83V/1m is 90 dB.
- **Source:** https://www.soundimports.eu/en/dayton-audio-nd25fa-4.html (fetched June 2026)

### Peerless by Tymphany BC25SC06-04 — Candidate
- Role: **HIGH** | Dome: 25 mm textile | Faceplate OD: ? (unconfirmed — fetch datasheet) | Impedance: 4Ω
- Sensitivity: 95.4 dB | Power: 50W RMS | Fs: 1350 Hz | Qts: 1.26
- Cutout: ~43 mm | Depth: ~32 mm
- Supplier: [SoundImports](https://www.soundimports.eu/en/peerless-by-tymphany-bc25sc06-04.html) | Price: €24.95 | Stock: 10+
- **Why liked:** 50W RMS power — highest power handling of any candidate tweeter in budget. Circular faceplate confirmed. 95.4 dB sensitivity is very high — means significant DSP attenuation (~7–10 dB) would be needed to match the 85 dB sub, which is straightforward with the JAB5. Includes finned heat sink for thermal management.
- **Concern:** 95.4 dB sensitivity requires large DSP attenuation vs the 85 dB sub. Dome colour not confirmed from page text.
- **Source:** https://www.soundimports.eu/en/peerless-by-tymphany-bc25sc06-04.html (fetched June 2026)

### SB Acoustics SB26STCN-C000-4 — ❌ REJECTED (too much offset — owner)
- Role: **HIGH** | Dome: 25 mm fine weave soft fabric | Faceplate OD: 72 mm round | Impedance: 4Ω
- Sensitivity: 92 dB | Power: 120W RMS | Fs: 950 Hz | Re: 3.2Ω | Le: 0.04 mH
- Supplier: [SoundImports](https://www.soundimports.eu/en/sb-acoustics-sb26stcn-c000-4.html) | Price: €36.45 | Stock: 10+
- **Why liked:** Massive 120W RMS power handling — effectively indestructible in this application. Fs 950 Hz gives good margin below target crossovers. Soft fabric dome offers warm character similar to SB19ST. Neodymium magnet. Internal pressure equalisation. 72 mm faceplate is compact and confirmed circular.
- **Concern:** At €36.45 it leaves less budget for the midrange. Dome colour not confirmed from page text — likely dark fabric. Sensitivity at 92 dB is 7 dB above sub; needs DSP attenuation.
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb26stcn-c000-4.html (fetched June 2026)

### Dayton Audio RST28F-4 — ❌ REJECTED (60° off-axis)
- Role: **HIGH** | Dome: 28 mm (1-1/8") silk | Faceplate OD: **104.5 mm** | Cutout: **72 mm** | Bolt circle: Ø90mm, 4×Ø4.5mm | Depth: **57 mm total** (4mm protrusion, ~53mm behind baffle) | Impedance: 4Ω
- Sensitivity: 93.5 dB @ 2.83V/1m | Power: 80W RMS | Frequency response: 1,400–20,000 Hz
- Fs: 710 Hz | Re: 3.0Ω | Le: 0.03 mH | Qts: 0.92 | Qes: 1.46 | Qms: 2.52 | Sd: 6.6 cm²
- **Off-axis gate result:** No 60° data in datasheet or Dayton data files (max angle = 45°). At 45°: −6.4 dB at 10 kHz, **−10.1 dB at 13 kHz** (confirmed from data files). At 60°: ≥12–13 dB predicted. Sd = 6.6 cm² → effective diameter 29 mm → f_beam = 7.6 kHz. **REJECTED for 60° kitchen position.**
- **Datasheet:** [research/dayton_rst28f-4.pdf](research/dayton_rst28f-4.pdf) | [research/dayton_rst28f-4_fre.pdf](research/dayton_rst28f-4_fre.pdf) (FR graph from data zip)
- **Source:** [Dayton Audio product page](https://www.daytonaudio.com/product/1566/rst28f-4-1-1-8-reference-series-fabric-dome-tweeter-4-ohm) | [SoundImports](https://www.soundimports.eu/en/dayton-audio-rst28f-4.html) (€46.95, 10+ stock)

### Peerless by Tymphany DX25TG59-04 — ❌ REJECTED (60° off-axis — owner)
- Role: **HIGH** | Dome: 25 mm silk (damped, ferrofluid-cooled VC) | Faceplate OD: 104 mm | Cutout: 74 mm | Depth: 33 mm | Impedance: 4Ω
- Sensitivity: 93.4 dB @ 2.83V/1m | Power: 15W RMS | Frequency response: 800–20,000 Hz
- Fs: 590 Hz | Re: 3Ω | Le: 0.035 mH | Qts: 0.48 | Qes: 0.609 | Qms: 2.16
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/peerless-by-tymphany-dx25tg59-04.html) (specs fetched June 2026)
- **Datasheet:** [research/peerless_dx25tg59-04.pdf](research/peerless_dx25tg59-04.pdf) | [original URL](https://doc.soundimports.nl/pdf/brands/Peerless%20by%20Tymphany/DX25TG59-04/DX25TG59-04.pdf) (downloaded June 2026)
- SoundImports price: €32.95 | Stock (June 2026): 10+
- **Power at reference:** 5.8W RMS and 11.5W at burst — both well within 15W rating. DSP limiter set at 12W protects the driver with 25% margin.
- **Why liked:** Fs 590 Hz → ~4.7× margin at typical crossovers — best of all tweeter candidates by a wide margin. Qts 0.48 is the lowest (best behaved) of any candidate. Ferrofluid cooling adds thermal safety at the limits. Circular faceplate. 10+ in stock.
- **DSP correction vs TB sub (85 dB ref):** −8.4 dB pad needed. Large attenuation — verify noise floor with the JAB5 at idle before committing.
- **Concern — dome colour:** "Damped silk diaphragm" material confirmed; colour not explicitly stated on page. Likely dark (standard hi-fi silk), but verify from datasheet images or product photo before ordering.
- **Concern — faceplate size:** 104 mm OD is large — same footprint as SB26ADC. Front baffle width impact the same as those drivers.

### Monacor DT-25N — Candidate
- Role: **HIGH** | Dome: 25 mm silk | Faceplate OD: 66 mm (integral waveguide) | Impedance: 8Ω
- Sensitivity: 95 dB @ 2.83V/1m | Power: 40W RMS / 80W max | Fs: 1600 Hz | Frequency response: 1,600–20,000 Hz
- Supplier: [SoundImports](https://www.soundimports.eu/en/monacor-dt-25n.html) | Price: €29.95 | Stock: 10+
- **DSP correction vs TB sub (85 dB ref):** −10 dB pad needed.
- **Note:** Fs 1600 Hz means crossover should be at least 3,200 Hz (2× Fs). Response starts at 1,600 Hz. Waveguide narrows dispersion — affects 60° off-axis position. Needs high-Fs-tolerant crossover point. 8Ω on JAB5 tweeter channel: ~31W available at 24V; needs ~3.2W at reference — no power concern.

### Peerless by Tymphany D27TG35-06 — Candidate (reinstated)
- Role: **HIGH** | Dome: 25 mm silk | Faceplate OD: 104 mm | Impedance: 6Ω
- Sensitivity: 91.8 dB | Power: 15W RMS | Fs: 900 Hz
- Supplier: [SoundImports](https://www.soundimports.eu/en/peerless-by-tymphany-d27tg35-06.html) | Price: €39.95 | Stock: 10+
- **Power at reference:** At woofer max (80W), tweeter needs 11.1W — within 15W rating with 35% headroom.
- **DSP correction vs TB sub (85 dB ref):** −6.8 dB pad needed.
- **Note:** 6Ω impedance — JAB5 is rated into 6Ω (its specified load), so this is fine. ~41W available at 24V, well above the 11.1W needed.
- **Concern:** Dome colour unconfirmed. Faceplate 104 mm is large (same as DX25TG59-04). Fetch datasheet to confirm colour before ordering.

### Peerless by Tymphany NE25VTS-04 — Candidate (compact faceplate)
- Role: **HIGH** | Dome: 25 mm silk (neodymium, copper cap) | Faceplate OD: **66.3 mm** | Impedance: 4Ω
- Sensitivity: 91.1 dB @ 2.83V/1m | Power: 15W RMS | Fs: 730 Hz | Frequency response: 700–20,000 Hz
- Rear aluminium chamber (heat dissipator)
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/ne25vts-04.html) (fetched June 2026)
- SoundImports price: **€39.95** | Stock (June 2026): 10+
- **DSP correction vs TB sub (85 dB ref):** −6.1 dB pad needed.
- **Fs check:** 730 Hz → min crossover 1,460 Hz.
- **Power at reference (98 dB):** 4.7W (31% of 15W ✓). At burst (101 dB): 9.3W (62% ✓). Headroom adequate; no DSP limiter required at project SPL levels.
- **Why interesting:** 66.3 mm faceplate is the same compact class as ND25FA-4 (66 mm) — significantly smaller than the 88 mm SB19ST and the 104 mm DX25TG59-04 family. Compact footprint means tighter centre spacing with any mid driver. Sensitivity at 91.1 dB is 2.6 dB higher than ND25FA-4 (90 dB) — needs a little more DSP attenuation but draws less power. Neodymium motor.
- **vs ND25FA-4 (B10 pairing):** Near-identical faceplate OD. NE25VTS-04 is 1.1 dB higher sensitivity, €24 more expensive. Both 25 mm domes — same dispersion characteristic. Use NE25VTS-04 if ND25FA-4 is out of stock; otherwise ND25FA-4 is better value.
- **Concern:** 15W power rating — lowest alongside XT25TG30-04 and XT25BG60-04. Fine at project SPL (9.3W at burst), but driver cannot be pushed harder.

### Peerless by Tymphany NE19VTS-04 — Candidate (compact 19mm, UK stock Willys-Hifi)
- Role: **HIGH** | Dome: 19 mm silk (neodymium, copper cap) | Faceplate OD: **52 mm** | Cutout: 38 mm | Depth: 35.5 mm | Impedance: 4Ω
- Sensitivity: **90.4 dB @ 2.83V/1m** | Power: **20W RMS** | Fs: **770 Hz** | Frequency response: 700–20,000 Hz
- Rear aluminium chamber (heat sink) | No ferrofluid | Silk dome, dark
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/vifa-peerless-ne19vts-04-tweeter) | [SoundImports](https://www.soundimports.eu/en/peerless-by-tymphany-ne19vts-04.html) (OOS Dec 2026)
- Willys-Hifi price: **£25.20** (UK, in stock June 2026) | SoundImports: €29.95 (OOS Dec 2026)
- **DSP correction vs TB sub (85 dB ref):** −5.4 dB pad needed.
- **Power at reference:** 98 dB → 11.5W (57% of 20W ✓) | burst 101 dB → 23W — exceeds 20W rating. **DSP limiter mandatory at ≤20W.** Max tweeter SPL = 90.4 + 10×log(20/2) = **100.4 dB** (0.6 dB below sub burst ceiling — inaudible at transients).
- **PSU:** 24V RMS / 28V burst (sub-limited; tweeter DSP-capped at 20W).
- **Centre spacing (FP OD 52mm):** DSA90-8 (92mm OD) → 72mm | DS115-8 (115.6mm) → 83.8mm | SB12PFCR25-4 (~122mm) → 87mm
- **Why considered:** 52mm FP is the 2nd most compact dome tweeter in the field (after XT25SC40-04 ring rad at 43.9mm). 19mm dome = same off-axis dispersion class as SB19ST. Warm silk character. UK stock now.
- **Vs SB19ST-C000-4:** FP 52mm vs 88mm — significantly more compact. Same 19mm dome. SB19ST has 1.9 dB higher sensitivity (less power needed), 30W vs 20W rating, cheaper (€21.45 / £18 Falcon). NE19VTS-04 wins only on faceplate compactness.

### SB Acoustics SB29SDNC-C000-4 — Candidate (compact 29mm cloth dome, Willys-Hifi)
- Role: **HIGH** | Dome: 29 mm cloth (textile, dark) | Faceplate OD: **72 mm** | Impedance: 4Ω
- Sensitivity: **95.5 dB @ 2.83V/1m** | Power: **80W RMS** | Fs: **630 Hz** | Sd: 9.6 cm²
- Neodymium motor | Re: 3.0Ω | VC diameter: 29 mm
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/sb-acoustics-sb29sdnc-c000-4-tweeter) | [SB Acoustics product page](https://sbacoustics.com/product/sb29sdnc-c000-4-fabric/)
- Willys-Hifi price: **£56.64** (UK, in stock June 2026)
- **DSP correction vs TB sub (85 dB ref):** −10.5 dB pad needed.
- **Power at reference:** 98 dB → 3.6W (4.5% of 80W) | burst 101 dB → 7.1W (8.9% ✓). Effectively indestructible at project SPL levels.
- **PSU:** 24V / 28V (sub-limited; tweeter barely loaded).
- **Why considered:** 72mm FP is compact (same as SB26STCN). Fs 630 Hz → min xover 1,260 Hz — second widest crossover window of any cloth dome candidate. 80W rating gives enormous headroom. Cloth dome = warm character.
- **Vs SB26STCN-C000-4:** Both 72mm FP. SB29SDNC: 95.5 dB (3.5 dB more sensitive), 80W vs 120W, Fs 630 vs 950 Hz (better margin), 29mm dome vs 25mm (narrower dispersion), £56.64 vs €36.45 at SI (significantly more expensive). Use SB29SDNC only if the lower Fs crossover flexibility justifies the cost.
- **Concern:** 29mm dome is wider than the ≤19mm ideal for off-axis dispersion. At 60° kitchen position, output above 8–10 kHz is slightly lower than a 19–25mm dome. Same concern as RST28F-4.

### Morel MDT12 — ❌ REJECTED (60° off-axis) | Retain for on-axis / compact scenarios
- Role: **HIGH** | Dome: **28 mm selected soft fabric (dark)** | Faceplate: **54×54 mm SQUARE** (R5.5mm corners) | Cutout: **Ø44.0 mm** | Depth: **19 mm** | Impedance: 8Ω
- Sensitivity: **89 dB @ 1W/1m** | Power: **80W RMS / 500W transient (10ms)** | Fs: **1,000 Hz** | Frequency response: 1,800–25,000 Hz
- Re: 5.2Ω | Le: 0.05 mH @ 1kHz | VC diameter: 28mm | VC former: Aluminum | BL: 2.8 NA | B flux: 1.4T | Mms: 0.47g | **Sd: 6.0 cm²**
- Neodymium motor | Chamberless (no rear volume needed) | Ferrofluid | Magnetically shielded
- **Datasheet:** [research/morel_mdt12.pdf](research/morel_mdt12.pdf) | [Madisound URL](https://madisound.com/loudspeaker_specifications/mdt%2012.pdf)
- **Source:** [SoundImports](https://www.soundimports.eu/en/morel-mdt-12.html) (€49.95, 5 in stock June 2026) | [Willys-Hifi](https://willys-hifi.com/products/morel-mdt12-soft-dome-tweeter) (£39.50, in stock)
- **Off-axis gate result:** Datasheet shows 0°, 30°, 45° only — **no 60° data**. Sd = 6.0 cm² → effective diameter 27.6mm → f_beam = 7.9 kHz — same class as RST28F-4 (6.6 cm², 7.6 kHz) which measured −10.1 dB at 45° at 13 kHz. At 60°: ≥12 dB predicted. **REJECTED for 60° kitchen position.** Retain for on-axis and compact/square visual scenarios only.
- **DSP correction vs TB sub (85 dB ref):** −4.0 dB pad needed.
- **Power at reference (8Ω):** 98 dB → 7.9W (10% of 80W ✓) | burst 101 dB → 15.9W (20% ✓).
- **Available @ 24V into 8Ω:** ~31W >> 15.9W ✓ | PSU: 24V / 28V (sub-limited).
- **Why retain:** Unique 54mm square faceplate + 19mm depth = most compact square tweeter, zero rear-chamber concern. Fs 1,000 Hz → min xover 2,000 Hz.

### Dayton Audio ND13FA-4 — Candidate (high-xover, wide dispersion) | needs a high-beaming mid OR on-axis-leaning use
- Role: **HIGH** | Dome: 1/2" (13 mm) soft dome | **Mount: front pressfit, compact faceplate** | Impedance: 4Ω | Re: 3.07Ω | Le: 0.02 mH | Qts: 0.84 | VC: 12.7 mm
- Sensitivity: **88.5 dB @ 2.83V/1m** | Power: **20W RMS** | **Fs: 2,832 Hz** | Usable: 4,500–20,000 Hz
- **Source:** [Dayton datasheet (doc.soundimports.nl)](https://doc.soundimports.nl/pdf/brands/Dayton%20Audio/ND13FA-4/pdf_Dayton%20Audio_ND13FA-4_1.pdf) (owner-supplied params, June 2026)
- **Off-axis:** Datasheet polar shows **0°/15°/30°/45° only — no 60° curve.** Owner reads it as very even dispersion; verified even to 45° (smallest 13 mm dome → widest dispersion, as expected). 60° not on the datasheet → unverified for our 60° gate.
- **Power check (4Ω, p_ref = 2W):** 98 dB needs **17.8W (89% of 20W — no headroom)**; burst 101 dB needs **35.6W — far exceeds 20W** → hard DSP limiter, tweeter SPL-capped. Power-marginal even before the crossover problem.
- **Crossover:** Fs 2,832 Hz → wants a ~4.5–5 kHz crossover (datasheet usable from 4,500 Hz). That is above where a 4" mid beams, so it is only a problem for a **60°-flat-power** target — NOT on-axis.
- **Real-world data point (DIY, [FB DIY Loudspeaker group](https://www.facebook.com/groups/DIYLoudspeakerProjecPad/posts/1871934119829083/), June 2026):** **SB12PFCR25-4 + ND13FA-4, first-order at 5 kHz, no L-pad — reported to work brilliantly.** This is an on-axis listening verdict and is consistent with the physics: the 4" is flat on-axis to 5 kHz; only the wide-angle response softens.
- **60° off-axis status — UNVERIFIED (no measured polar; datasheet shows 0/15/30/45° only).** Rigid-piston *estimate* for the SB12PFCR25-4 mid at 60°: ~−4 dB @ 3 k, −8 dB @ 4 k, −14 dB @ 5 k — a sloping droop, not a void, and real paper cones disperse wider than the piston model (breakup decouples the cone), so true droop is likely less. Confirm with a measured 60° polar before treating the combo as 60°-validated.
- **Net:** earlier "incompatible" label was wrong — it assumed a 60°-flat-power target. Viable and builder-proven on-axis; the open question is solely the degree of 3–5 kHz softening at a true 60°.
- **Crossover point / slope (DSP):** datasheet "usable from 4,500 Hz" is a gentle-slope guideline; the real limit is drive at Fs (2,832 Hz). Filter math: 1st-order @ 5 kHz leaves −6 dB at Fs; 1st-order @ 4 kHz −4.8 dB; **LR4 (24 dB/oct) @ 4 kHz ≈ −13 dB; LR4 @ 4.5 kHz ≈ −16 dB.** With the JAB5/ADAU1701, an **LR4 high-pass at ~4–4.5 kHz** protects the tweeter better than the FB build's 5 kHz first-order AND keeps the mid less beamed. Do not copy the passive first-order. Filter figures are math, not a THD measurement — confirm the safe floor with a distortion sweep at level before locking.

### Dayton Audio ND16FA-4 — ⚠ INCOMPATIBLE (crossover) | Best measured 45° off-axis of all candidates
- Role: **HIGH** | Dome: 5/8" (16mm) soft dome | Faceplate OD: **~45mm** | Cutout: **37mm pressfit** | Depth: **14.5mm total** (2.5mm protrusion, 12mm behind baffle) | Impedance: 4Ω | Re: 3.17Ω | Le: 0.03 mH
- Sensitivity: **93 dB @ 2.83V/1m** | Power: **30W RMS** | **Fs: 2,246 Hz** | Qms: 3.71 | Qes: 3.46 | Qts: 1.79 | Sd: N/A | Usable: 4,000–20,000 Hz
- Pressfit front mount — no bolt holes
- **Datasheet:** [research/dayton_nd16fa-4.pdf](research/dayton_nd16fa-4.pdf) | [research/dayton_nd16fa-4_fre.pdf](research/dayton_nd16fa-4_fre.pdf) (FR graph from Dayton data zip)
- **Off-axis (45° measured from data files, June 2026):** −3.1 dB at 10 kHz, **−4.4 dB at 13 kHz** — best 45° off-axis performance of any tweeter measured in this project. No 60° data in files (max angle = 45°). At 60° likely 6–7 dB at 13 kHz based on trajectory — competitive with SB19ST.
- **⚠ INCOMPATIBLE — crossover:** Fs 2,246 Hz → 2×Fs = **4,492 Hz minimum crossover**. All mids in catalogue beam before this: DSA90-8 beams at 3,260 Hz, DS115-8 at 2,636 Hz. Gap of 1.2 kHz+ where mid is beaming and tweeter isn't playing — directivity hole at 60° exactly where needed. **Cannot be used in this 3-way design.**
- **Power check:** 30W RMS. At 98 dB: 6.3W (21% ✓). At burst 101 dB: 12.6W (42% ✓) — marginal but OK.

### Dayton Audio ND16FA-6 — ⚠ INCOMPATIBLE (crossover) | 6Ω sibling of ND16FA-4, strictly weaker
- Role: **HIGH** | Dome: 5/8" (16 mm) soft dome | **Mount: front pressfit flush-mount, NO bolt holes** | Faceplate OD: **32.5 mm (1.28")** | Cutout: **25.4 mm (1") pressfit** | Depth: **14.5 mm (0.57")** | Impedance: 6Ω | Re: 5.0Ω | Le: 0.05 mH | Qts: 2.20
- Sensitivity: **90.5 dB @ 2.83V/1m** (≈89.3 dB @ 1W, 6Ω) | Power: **10W RMS** | **Fs: 2,283 Hz** | Usable: 3,500–27,000 Hz
- **Source:** [Dayton datasheet PDF](https://www.daytonaudio.com/images/resources/275-025-dayton-audio-nd16fa-6-specifications-46192.pdf) | [SoundImports](https://www.soundimports.eu/en/dayton-audio-nd16fa-6.html) (specs fetched June 2026)
- **Mounting:** drill 25.4 mm hole, press in from front, retain with silicone/glue (no screw provision); c-t-c as tight as ~35 mm.
- **Power check (6Ω):** 98 dB needs **7.5W** (75% of 10W); burst 101 dB needs **15.0W — exceeds the 10W rating** → DSP limiter mandatory, tweeter SPL-capped ~99.2 dB.
- **⚠ INCOMPATIBLE — crossover:** Fs 2,283 Hz → 2×Fs = **4,566 Hz minimum crossover**, above every mid's beam limit (DS115-8 2,636 Hz, DSA90-8 3,475 Hz). Same directivity-hole block as ND16FA-4. Versus ND16FA-4 (30W, 93 dB, same dome) it is strictly weaker — no reason to choose -6.

### Dayton Audio ND20FA-6 — ⚠ INCOMPATIBLE (crossover)
- Role: **HIGH** | Dome: 19 mm soft dome | Faceplate OD: 45 mm | Cutout: 33mm | Depth: 15mm | Impedance: 6Ω | Re: 5.2Ω | Le: 0.05 mH
- Sensitivity: 90 dB @ 1W/1m | Power: 15W RMS / 30W max | Fs: 2,005 Hz | Qms: 1.5 | Qes: 2.88 | Qts: 0.99 | Sd: 2.8 cm²
- Supplier: [SoundImports](https://www.soundimports.eu/en/dayton-audio-nd20fa-6.html) | Price: €14.95 | Stock: 10+
- **Off-axis (45° measured from data files, June 2026):** −5.5 dB at 10 kHz, −8.0 dB at 13 kHz. No 60° data.
- **⚠ INCOMPATIBLE — crossover:** Fs 2,005 Hz → 2×Fs = 4,010 Hz minimum crossover. All mids beam below this. Same incompatibility as ND16FA-4.

### Dayton Audio ND20FB-4 — ⚠ INCOMPATIBLE (crossover)
- Role: **HIGH** | Dome: 3/4" (19/20 mm) soft textile, rear-mount | Impedance: 4Ω | Re: 3.20Ω | Le: 0.03 mH | Ferrofluid-cooled
- Sensitivity: **90 dB @ 2.83V/1m** | Power: **15W RMS** | **Fs: 2,072 Hz** | Usable: 3,500–25,000 Hz
- **Source:** [Dayton datasheet PDF](https://www.daytonaudio.com/images/resources/275-035-dayton-audio-nd20fb-4-specifications-46117.pdf) | [SoundImports](https://www.soundimports.eu/en/dayton-audio-nd20fb-4.html) (specs fetched June 2026)
- **Off-axis:** Owner reports good wide dispersion / low directivity (small 19 mm dome — physically plausible). **Not yet verified — no measured 60° polar curve obtained.** Fetch measured directivity before any off-axis claim.
- **⚠ INCOMPATIBLE — crossover:** Fs 2,072 Hz → 2×Fs = **4,144 Hz minimum crossover**. DS115-8 beams at 2,636 Hz, DSA90-8 at ~3,475 Hz — both below this, leaving a 2.6–4.1 kHz directivity hole at 60°. Same incompatibility as ND16FA-4 (4,492 Hz) and ND20FA-6 (4,010 Hz). Usable only with a mid/wideband that stays pistonic to ~4.2 kHz.

### Dayton Audio PTMini-6 — ⚠ INCOMPATIBLE (crossover) | planar
- Role: **HIGH** | Type: **Planar magnetic** (Kapton ribbon membrane, etched aluminium conductor) | Impedance: 6Ω
- Sensitivity: **90 dB @ 2.83V/1m** | Power: **15W RMS** | **Fs: 4,461 Hz** | Usable: 2,900–25,000 Hz | **Mfr recommended crossover: ≥4,000 Hz, 12 dB/oct**
- **Source:** [Dayton datasheet PDF](https://www.daytonaudio.com/images/resources/275-083--dayton-audio-ptmini-6-specifications.pdf) | [SoundImports](https://www.soundimports.eu/en/dayton-audio-ptmini-6.html) (specs fetched June 2026)
- **Off-axis:** Owner reports planar gives very consistent horizontal off-axis (physically expected — narrow vertical strip radiates wide horizontally) **but narrow/lobing vertical dispersion** (tall element). Horizontal consistency suits the 60° kitchen geometry; vertical narrowness matters if listening height varies. **Not yet verified — no measured polar obtained.**
- **⚠ INCOMPATIBLE — crossover:** manufacturer recommends ≥4,000 Hz crossover (Fs 4,461 Hz). DS115-8 beams at 2,636 Hz, DSA90-8 at ~3,475 Hz — both well below 4,000 Hz, so the mid is already beaming before the planar can take over: directivity hole at 60° across ~2.6–4 kHz. Same wall as the small domes (ND16FA-4 / ND20FA-6 / ND20FB-4). Usable only with a mid/wideband pistonic to ~4 kHz.

### Peerless by Tymphany NE19VTS-04 — ❌ OUT (conflicting datasheets, unremarkable 60°)
- **Withdrawn (June 2026):** the official Tymphany datasheet ([cdn.shopify NE19VTS-04.pdf](https://cdn.shopify.com/s/files/1/0809/2387/files/NE19VTS-04.pdf), local `research/speakers/NE19VTS-04_tymphany.pdf`) gives **88.29 dB @ 2.83V / 85.1 @ 1W, Fs 742, 100 W** — conflicting badly with the SoundImports sheet (90.4 dB, 20 W, Fs 770). Two manufacturer sheets disagreeing by 2 dB and 5× power = untrustworthy data. Real sensitivity (~88 dB) is no better than SB19ST, and the 60° off-axis is ordinary (top-octave droop + deep notch ~28–30 kHz). Loses both its claimed edges → out.
- Role: **HIGH** | Type: 19 mm fabric dome, neodymium, cast aluminium frame | Faceplate: **Ø52 mm round, 3-bolt** | Impedance: 4Ω | Re: 2.8Ω | Zmin 3.4Ω | Le: 0.014 mH | Sd: 4.91 cm²
- Sensitivity: **90.4 dB @ 2.83V/1m** (87.4 dB/1W) | Power: **20W (IEC 268-5)** | **Fs: 770 Hz** | Range: 700–20,000 Hz | Mms 0.197 g | Xmax 0.7 mm
- **Source:** [Tymphany datasheet, July 2025](https://doc.soundimports.nl/pdf/brands/Peerless%20by%20Tymphany/NE19VTS-04/NE19VTS.pdf) — local copy `research/speakers/Peerless_NE19VTS-04_datasheet.pdf`
- **Off-axis (datasheet plots 0/30/60°):** 60° tracks on-axis to ~5 kHz, then ~**−5 dB** through the top octave (ripple/notch ~12–16 kHz). Critical 2.8–10 kHz holds within a few dB at 60°. **Tymphany datasheet — NOT subject to the SB Acoustics "60° = real 45°" mislabel** (see research/tweeter_offaxis_evidence.md), so this 60° figure is the most credible of the dome shortlist.
- **Crossover:** Fs 770 → min ~1,540 Hz; cross ~1.5–2 kHz (DSP LR4), comfortably below any mid's beam onset → cleanest window of the shortlist.
- **Power:** max SPL ≈ **100.4 dB/1m** at 20 W (87.4 dB/1W + 13 dB). Covers 98 dB ref; 0.6 dB under the 101 dB burst → DSP limiter caps inaudibly. Non-issue. −5.4 dB DSP pad vs 85 dB sub.
- **vs SB19ST / SB21SDCN:** lowest Fs (best crossover), most compact faceplate (Ø52 vs Ø88/Ø58), highest sensitivity (90.4), and the only one with a 60° curve from a datasheet we don't know to be mislabelled. **Current front-runner.** Confirm with an independent polar (HiFiCompass/Erin) to make it bulletproof.

### Dayton Audio TD20F-4 — Candidate (3/4" silk dome, neo) | 60° UNVERIFIED, crosses high
- Role: **HIGH** | Type: 3/4" (20 mm) silk soft dome, neodymium | Faceplate: **Ø65 mm round** | Mounting depth: 15 mm | Impedance: 4Ω | Re: 3.4Ω | Le: 0.03 mH | Ferrofluid | Qts: 1.38
- Sensitivity: **90 dB @ 2.83V/1m** | Power: **20W RMS** | **Fs: 1,696 Hz** | Usable: 3,000–20,000 Hz
- **Source:** [Dayton datasheet (doc.soundimports.nl)](https://doc.soundimports.nl/pdf/brands/Dayton%20Audio/TD20F-4/pdf_Dayton%20Audio_TD20F-4_1.pdf) (read June 2026)
- **Off-axis:** datasheet polar is **0/15/30/45° only — no 60°.** At 45°: ~−3–4 dB @ 10 kHz, ~−8 dB @ 15 kHz (decent for a 20 mm dome). 60° unverified for the kitchen gate.
- **Crossover:** Fs 1,696 → min ~3.0–3.4 kHz. Above a 4" mid's beam onset (SB12PFCR25-4 2,730, DS115-8 2,636) → small directivity gap with a 4"; pairs cleanly with DSA90-8 (beams 3,475). SB19ST (Fs 980) crosses lower with no gap.
- **Power (4Ω):** 12.6 W @ 98 dB (63% of 20 W); **25 W @ 101 dB burst — over the 20 W rating** → DSP limiter, capped ~99.5 dB.
- **⚠ Datasheet error:** lists Sd 31.4 cm² — impossible for a 20 mm dome (≈ a 3" cone's area; likely faceplate area mis-entered). Immaterial for a tweeter; do not use that figure.
- **vs SB19ST:** SB19ST has a confirmed 60° curve, crosses lower (Fs 980), and is 30 W. TD20F-4 is higher-Fs, 60°-unmeasured, 20 W. Behind SB19ST on evidence; competitive only if paired with DSA90-8 and a measured 60° beats it.

### Monacor DT-100 — Candidate (25 mm soft dome, low Fs — crosses cleanly; dispersion UNVERIFIED)
- Role: **HIGH** | Type: Soft dome | VC/dome: **25 mm** | Faceplate: **116×80×26 mm rectangular** (ferrite, 0.525 kg) | Cutout: **Ø72 mm round** | Mounting depth: 26 mm | Impedance: 8Ω | Ferrofluid
- Sensitivity: **92 dB/W/m** | Power: **30W RMS / 60W max** | Fs: **1,500 Hz** | Mfr recommended crossover: **2,500 Hz / 12 dB/oct**
- **Source:** [Monacor datasheet](https://doc.soundimports.nl/pdf/brands/Monacor/DT-100/pdf_monacor_DT-100_1.pdf) (Order 10.0040) | [SoundImports](https://www.soundimports.eu/en/) €43.95 | **[Willys-Hifi](https://willys-hifi.com/products/monacor-dt-100-tweeter) £28.27 (cheapest)** | Drop-in for Peerless KO10DT / DT115
- **Crossover — clean match:** Fs 1,500 → cross ~2.5–3 kHz (DSP LR4). Lands at the mid's beam onset (SB12PFCR25-4 2,730 Hz, DS115-8 2,636 Hz) → conventional well-integrated 3-way crossover, **no directivity hole** (unlike the high-Fs micro-domes ND13/16/20, PTMini).
- **Power (8Ω):** 4.0W @ 98 dB, 7.9W @ burst — trivial; −7 dB DSP pad; large headroom.
- **⚠ Dispersion UNVERIFIED:** the Monacor datasheet has **no polar/off-axis plot** — the "wide dispersion" wording was the *Willys listing*, not Monacor (Monacor claims only "good linearity, brilliant, detail"). A 25 mm dome is *larger* than the 13–19 mm domes, so physically beams *earlier* at the top, not later. **No 60° data exists.** Do not credit dispersion without a measured plot — cf. Scan-Speak's "Wide Dispersion" D2604/830000, contradicted by its own 60° datasheet and rejected.
- **vs SB19ST:** SB19ST is smaller (19 mm → physically wider 60°), crosses lower (1,960 Hz), and **has a confirmed 60° curve** (−5–6 dB @ 13 kHz). DT-100 is hotter (92 vs 88.5 dB) but larger-dome, higher-crossover, dispersion unverified. SB19ST is the stronger 60° bet on current data.

### Monacor DT-28N — Candidate (28 mm silk cone, neo, tiny faceplate — best low-xover Monacor) | dispersion UNVERIFIED
- Role: **HIGH** | Type: **28 mm silk cone** (neodymium) | Faceplate: **55×55×20 mm square** | Cutout: **Ø50 mm** | Mounting depth: 16.7 mm | Magnet: Ø46 mm neo | Weight: 0.074 kg | Impedance: 8Ω
- Sensitivity: **94 dB/W/m** | Power: **50W RMS / 100W max** | Fs: **1,200 Hz** | Mfr recommended crossover: **2,000 Hz / 12 dB/oct**
- **Source:** [Monacor datasheet](https://doc.soundimports.nl/pdf/brands/Monacor/DT-28N/pdf_monacor_DT-28N_1.pdf) (Order 10.4020) | [SoundImports](https://www.soundimports.eu/en/) €40.95
- **Crossover — best of the Monacor pair:** Fs 1,200 → cross ~2,000–2,400 Hz (DSP LR4), **below** the mid's beam onset (SB12PFCR25-4 2,730 Hz) → clean window, no hole, and the lowest crossover of any conventional dome here except SB19ST.
- **Spacing:** 55×55 mm plate is far smaller than DT-100 (116×80) → much tighter mid-tweeter centre spacing. Neodymium, 74 g (light).
- **Power (8Ω):** 2.5W @ 98 dB, 5.0W @ burst — trivial; −9 dB DSP pad; huge headroom.
- **⚠ Dispersion UNVERIFIED:** Monacor datasheet has **no polar plot.** 28 mm cone is the *largest* diaphragm of the DT-100/DT-28N/SB19ST set → by physics the narrowest top-octave dispersion, though cone (vs dome) behaviour differs. **No 60° data.** Must be measured before treating as 60°-suitable.
- **Beats DT-100 on the measurable specs** (lower Fs/crossover, +2 dB sensitivity, +20W, far smaller plate). Already referenced in combos B11/B12. For a true 60° priority, SB19ST still leads on evidence (confirmed curve); DT-28N is the better choice if you'll measure dispersion at build.

### Scan-Speak Discovery D2606/920000 — Candidate
- Role: **HIGH** | Dome: 25 mm coated textile | Faceplate OD: not confirmed | Impedance: 6Ω
- Sensitivity: 91.4 dB @ 2.83V/1m | Power: 100W RMS / 200W max | Fs: 1100 Hz
- Supplier: [SoundImports](https://www.soundimports.eu/en/scan-speak-d2606-920000.html) | Price: €39.95 | Stock: 10+
- **DSP correction vs TB sub (85 dB ref):** −6.4 dB pad needed.
- **Note:** Scan-Speak quality — likely excellent. 6Ω: JAB5 at 24V delivers ~41W; needs ~5.6W at reference. €39.95 is the most expensive tweeter candidate — constrains mid budget if £75 total. Faceplate OD not confirmed — fetch before ordering.

### Dayton Audio DC25T-8 — Catalogue (visual constraints removed June 2026)
- Role: **HIGH** | Dome: 25 mm titanium | Impedance: 8Ω | Sensitivity: 93 dB | Power: 50W RMS | Fs: 1,468 Hz | Response: 3,000–20,000 Hz
- Supplier: [SoundImports](https://www.soundimports.eu/en/dayton-audio-dc25t-8.html) | Price: €18.97 | Stock: 10+
- Note: Titanium dome (silver metallic appearance). Precision phase lens. Previously visual-excluded — visual constraints removed June 2026. Remaining concern: Fs 1,468 Hz → min crossover 2,936 Hz is high; response starts at 3,000 Hz. €18.97 — budget-friendly.

### Peerless by Tymphany XT25SC40-04 — INELIGIBLE (ring radiator — poor 60° off-axis)
- Role: **HIGH** | Type: **Ring radiator** | VC: 25 mm | Faceplate OD: **43.9 mm** (smallest ring rad in field) | Impedance: 4Ω
- Sensitivity: **94 dB @ 2.83V/1m** | Power: **100W RMS** | Fs: **1,018 Hz** | Frequency response: to 20,000+ Hz
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/xt25sc40-04.html) (fetched June 2026)
- SoundImports price: **€29.95** | Stock (June 2026): 10+
- **Min crossover:** 2× Fs = **2,036 Hz**.
- **DSP correction vs TB sub (85 dB ref):** −9.0 dB pad needed (tweeter is 9 dB hotter than sub reference).
- **Power at reference (98 dB):** 10^((98−94)/10) = **2.5W** (2.5% of 100W — minimal draw). At burst (101 dB): **5.0W** (5% of 100W). 100W power rating is effectively indestructible in this application.
- **Ineligible — off-axis:** Ring radiator. Its 43.9 mm faceplate is the smallest tweeter OD in the field (would have given a 68 mm centre spacing with DSA90-8 — the project minimum), but ring radiators measure horn-like at 60° off-axis (RAW-CAt Tweeter Shootout Part 6, Nov 2025), which is disqualifying for the 60° kitchen geometry. The spacing advantage cannot redeem it.

### SB Acoustics SB21SDC-C000-4 — Candidate (compact soft dome)
- Role: **HIGH** | Type: **Soft dome** (21 mm fabric — SB "SD" = soft dome, distinct from the "RD" ring-radiator series) | Dome: 21 mm | Faceplate OD: **92 mm** | Impedance: 4Ω
- Sensitivity: **91 dB @ 2.83V/1m** | Power: **40W RMS** | Fs: **720 Hz** | Frequency response: to 20,000+ Hz
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/sb21sdc-c000-4.html) (fetched June 2026)
- SoundImports price: **€39.95** | Stock (June 2026): 1 unit + 7 expected 3-Jul-2026
- **Min crossover:** 2× Fs = **1,440 Hz** — excellent; same range as SB29SDAC's 1,200 Hz.
- **DSP correction vs TB sub (85 dB ref):** −6.0 dB pad needed.
- **Power at reference (98 dB):** 10^((98−91)/10) = **5.0W** (12.5% of 40W ✓). At burst (101 dB): **10.0W** (25% ✓). Excellent headroom.
- **Off-axis gate — provisional PASS for the critical band, with caveats** ([HiFiCompass SB21SDCN/RDCN review](https://hificompass.com/en/reviews/sb-acoustics-sb21sdcn-c000-4-sb21rdcn-c000-4); local copy [research/speakers/SB Acoustics SB21SDCN-C000-4, SB21RDCN-C000-4 _ HiFiCompass.pdf](research/speakers/SB%20Acoustics%20SB21SDCN-C000-4%2C%20SB21RDCN-C000-4%20_%20HiFiCompass.pdf), Kozhushko, Dec 2020):
  - Both dome and ring "radiate well on the sides **up to ~6 kHz**, after which the pattern narrows," and **the dome disperses wider than the ring radiator** ("a principal difference between dome and annular membranes") — direct measured confirmation of why ring radiators are out.
  - ⚠ **The review measures the neodymium 58 mm SB21SDCN, not this ferrite 92 mm SB21SDC.** Same 21 mm fabric dome family, but the flange differs (and the reviewer notes the flange bead shapes off-axis), so the curves transfer only roughly.
  - ⚠ **Datasheet 60° is optimistic:** the reviewer found the datasheet's 60° curve actually matches the *measured 45°*, and 30° matches measured 20°. So a "−5–6 dB at 13 kHz at 60°" read off the datasheet is really ~45° behaviour; true 60° above ~10 kHz is worse.
  - ⚠ Even the dome's **upper-octave dispersion is only "not very good"** for such a small tweeter (reviewer's words).
  - **Net:** clears the kitchen-critical 2.8–10 kHz band at wide angles (good to ~6 kHz, gentle narrowing above), loses top-octave air at 60° — broadly SB19ST-class, not better. Eligible, but get a real SB21SDC (92 mm) 60° curve before locking it as the tweeter.
- **Why interesting — compact soft dome:** SB29SDAC costs €44.95; SB21SDC costs €39.95 — €5 cheaper. SB21SDC's 92 mm faceplate vs SB29SDAC's ~104 mm → tighter spacing. Fs 720 Hz vs SB29's 600 Hz → min xover 1,440 Hz vs 1,200 Hz — slightly tighter but still excellent.
- **New pairings enabled:** RD1 (DS115-8 + SB21SDC = 104 mm spacing, 1,440–2,636 Hz window), RD2 (SB12PFCR25-4 + SB21SDC = 107 mm spacing).
- **vs SB29SDAC:** SB21 is €5 cheaper, 92 mm vs 104 mm FP (tighter spacing), 21 mm vs 29 mm dome (slightly less diaphragm area). Both are eligible soft domes; SB29SDAC has the lower Fs / wider window.
- **Stock caveat:** Only 1 available now; 7 expected July 3.

### Scan-Speak Discovery D2604/830000 — ❌ REJECTED (60° off-axis)
- Role: **HIGH** | Dome: 26 mm textile, wide surround | Faceplate OD: **104.2 mm** | Cutout: **75 mm** | Depth: **25.4 mm** (5mm protrusion, 20.4mm behind baffle) | Bolt circle: Ø92mm, 5×Ø4.2mm holes | Impedance: 4Ω | Re: 2.8Ω | Le: 0.04 mH
- Sensitivity: **92 dB @ 2.83V/1m** | Power: **100W RMS (IEC 18.4) / 240W (IEC 18.2)** | Fs: **630 Hz** | Qts: 0.79 | Qms: 3.46 | Qes: 1.02 | BL: 2.2 Tm | Rms: 0.48 kg/s | Mms: 0.42g | Cms: 0.15 mm/N | **Sd: 8 cm²** | Effective diameter D: **32 mm** | Vas: 0.01 L
- VC dia: 26mm | VC height: 2mm | 2 layers | Gap: 2.5mm | Xmax: ±0.3mm linear / ±1.6mm max
- **Datasheet:** [research/scanspeakd2604-830000.pdf](research/scanspeakd2604-830000.pdf) | [Scan-Speak URL](https://www.scan-speak.dk/datasheet/pdf/d2604-830000.pdf) (May 2020)
- **Source:** [SoundImports](https://www.soundimports.eu/en/scan-speak-d2604830000.html) | [Scan-Speak](https://www.scan-speak.dk/product/d2604-830000/) | Price: €44.95 | Stock: 10+ (pre-order)
- **Off-axis gate result:** 60° curve present in datasheet. At 13 kHz: on-axis ~87 dB, 60° ~75–77 dB → **−10 to −12 dB at 60° at 13 kHz**, with heavy jagged peaks and dips in the 60° response above 10 kHz. Effective diameter D = 32mm → f_beam = 6.8 kHz — beams harder than any other dome candidate. Scan-Speak markets "Wide Dispersion" — datasheet 60° plot contradicts this. **REJECTED for 60° kitchen position.**
- **Source:** [SoundImports](https://www.soundimports.eu/en/scan-speak-d2604830000.html) (fetched June 2026; URL confirmed) | [Scan-Speak](https://www.scan-speak.dk/product/d2604-830000/)
- SoundImports price: **€44.95** | Stock (June 2026): 10+ (listed as pre-order at SI but in stock)
- **Min crossover:** 2× Fs ≈ **1,260 Hz** — excellent; same window class as SB29SDAC (1,200 Hz). Only XT25TG30-04 (880 Hz) goes lower among domes.
- **DSP correction vs TB sub (85 dB ref):** −7.0 dB pad needed.
- **Power at reference (98 dB):** 4.0W (4% of 100W). At burst (101 dB): 8.0W (8%). Effectively indestructible at 100W/240W rating.
- **Why interesting:** Scan-Speak Discovery class engineering in a 104mm faceplate with 100W power handling, Fs ~630 Hz, and widest crossover window of any dome in the candidate field. €44.95 mid-range price. 104mm OD — same footprint class as DX25TG59-04, SB29SDAC. Depth only 25.4mm (shallowest large-FP tweeter in the field).
- **Pairing note:** At 104.2mm FP, spacing with DS115-8 (116mm OD) ≈ 110mm; with SB12PFCR25-4 (~122mm OD) ≈ 113mm — same as DA1/DA2. Centre spacing with DSA90-8 ≈ 98mm.

### Scan-Speak Discovery R2604/833000 — INELIGIBLE (ring radiator — poor 60° off-axis)
- Role: **HIGH** | Type: **26 mm dome / dual ring radiator**, fabric diaphragm | VC: 26 mm (2 layers) | **Faceplate OD: 104 ±0.2 mm (datasheet confirmed)** | Pitch dia: 92 mm | Depth: 55 mm | 5× Ø4.2 mm bolts at 72° | Impedance: 4Ω (Zmin 3.6Ω) | Re: 2.9Ω | Le: 0.02 mH
- Sensitivity: **92 dB @ 2.83V/1m** | Power: **100W RMS** (IEC 268-5) | Fs: **440 Hz** | Qts: 0.38 | Qms: 2.18 | Qes: 0.46 | Mms: 0.3 g | Cms: 0.44 mm/N | Sd: 5.4 cm² | Vas: 0.02 L | Xmax: ±0.2 mm linear (±1.6 mm max mech) | Cabinet displacement: 0.18 L | Extended response to >40 kHz
- **Source:** [SoundImports](https://www.soundimports.eu/en/scan-speak-r2604-833000.html) | **Datasheet (confirmed):** [research/scanspeak_r2604-833000_datasheet.pdf](research/scanspeak_r2604-833000_datasheet.pdf) | [original URL](https://www.scan-speak.dk/datasheet/pdf/r2604-833000.pdf) (downloaded June 2026) | Price: **€62.45** | Stock (Jun 2026): **10+**
- **Min crossover:** 2× Fs = **880 Hz** — the widest crossover window of any tweeter in the field (Fs 440 Hz), 100W rated.
- **DSP correction vs TB sub (85 dB ref):** −7.0 dB pad needed (same as D2604/830000).
- **Power at reference (98 dB):** 4.0W (4% of 100W). At burst (101 dB): 8.0W (8%). Indestructible.
- **Ineligible — off-axis:** Dual ring radiator. Its 880 Hz min crossover was the widest window in the catalogue, but ring radiators measure horn-like at 60° off-axis — large deviation by 30°, severe rolloff by 60° (RAW-CAt Tweeter Shootout Part 6, Nov 2025), confirmed on this driver's own datasheet. Disqualifying for the 60° kitchen geometry. The window advantage cannot redeem it.
- **Pairing note:** At ~104mm FP, spacing with DS115-8 ≈ 110mm; with SB12PFCR25-4 ≈ 113mm; with DSA90-8 ≈ 98mm. Same physical footprint as D2604/830000 and SB29RDNC-C000-4.

### Scan-Speak Discovery R2604/832000 — INELIGIBLE (ring radiator — poor 60° off-axis)
- Role: **HIGH** | Type: **Dual Ring Radiator**, fabric diaphragm | VC: 25 mm | Faceplate OD: **? (unconfirmed — fetch datasheet)** | Impedance: 4Ω | Re: 2.9Ω | Xmax: 0.2 mm
- Sensitivity: **90 dB @ 2.83V/1m** | Power: **100W RMS** | Fs: **500 Hz** | Extended response to 40 kHz+
- **Source:** [SoundImports](https://www.soundimports.eu/en/scan-speak-r2604-832000.html) (fetched June 2026) | Price: **€52.95** | Stock (Jun 2026): **10+**
- **Min crossover:** 2× Fs = **1,000 Hz** — slightly higher than R2604/833000 (880 Hz) but still wider window than D2604/830000 (1,260 Hz).
- **DSP correction vs TB sub (85 dB ref):** −5.0 dB pad needed.
- **Power at reference (98 dB):** 6.3W (6.3% of 100W). At burst (101 dB): 12.6W (12.6%). Indestructible.
- **Ineligible — off-axis:** Dual ring radiator. Same disqualifying horn-like 60° off-axis dispersion as all ring radiators (RAW-CAt Tweeter Shootout Part 6, Nov 2025), regardless of its budget 100W spec and wide window.
- **Pairing note:** At ~104mm FP, spacing with DS115-8 ≈ 110mm; with SB12PFCR25-4 ≈ 113mm; with DSA90-8 ≈ 98mm.

### SEAS 27TDFC H1189-06 — Candidate (90W dome, Fs 550 Hz — widest-window standard dome)
- Role: **HIGH** | Dome: 27 mm soft textile | Rear chamber | Faceplate OD: **103.8 mm** | Cutout: 73 mm | Depth: **39 mm** | Impedance: 6Ω
- Sensitivity: **90 dB @ 2.83V/1m** | Power: **90W RMS / 220W max** | Fs: **550 Hz** | Frequency response: specified from 1,500 Hz
- **Source:** [SoundImports](https://www.soundimports.eu/en/seas-27tdfc.html) (fetched June 2026) | Price: **€71.86** (sale from €86.95) | Stock (Jun 2026): **10+**
- **Also at HiFi Collective:** £56.92 (stock status unknown; verify before ordering)
- **Min crossover:** 2× Fs = **1,100 Hz** — widest-window standard dome in the catalogue. Better than SB29RDNC-C000-4 (1,160 Hz), SB29SDNC-C000-4 (1,260 Hz), D2604/830000 (1,260 Hz).
- **DSP correction vs TB sub (85 dB ref):** −5.0 dB pad needed.
- **Power at reference (6Ω, 98 dB):** 2.83²/6 × 10^((98−90)/10) = 1.334 × 6.31 = **8.4W** (9.4% of 90W ✓). At burst (101 dB): **16.8W** (18.7%). Completely safe.
- **Available @ 24V into 6Ω:** ~41W >> 16.8W needed ✓. No PSU concern.
- **Centre spacing (FP 103.8 mm):** DSA90-8 (92mm OD) → **98mm** | DS115-8 (~116mm OD) → **110mm** | SB12PFCR25-4 (~122mm OD) → **113mm** — same as R2604/833000 at identical FP OD.
- **Why interesting:** SEAS Prestige-quality standard dome with the lowest Fs of any dome candidate (550 Hz). Rear chamber lowers compliance resonance further than chamberless designs. Cloth dome character is smooth and warm vs ring-radiator brightness. At 103.8mm FP it physically matches SB29RDNC-C000-4, R2604/833000, R2604/832000 — interchangeable bolt-on without baffle change.
- **vs R2604/833000:** R2604/833000 wins on window width (880 Hz vs 1,100 Hz), sensitivity (92 vs 90 dB), power (100W vs 90W), and price (Falcon £45.95 vs £56.92). H1189-06 wins if cloth dome character is preferred. For kitchen-monitor DSP system, R2604/833000 is the stronger choice; H1189-06 is the best dome alternative for buyers who specifically want a dome at this FP size.
- **Depth note:** 39mm depth requires ≥40mm clearance behind baffle inner face. Plan for recessed tweeter rebate or a deeper baffle section at tweeter location.

### Dayton Audio CF18N-4 — Candidate (compact carbon fiber 18mm dome)
- Role: **HIGH** | Dome: **18 mm woven carbon fiber** | Faceplate OD: **58 mm** | Cutout: 36.9 mm | Depth: 38.3 mm | Impedance: 4Ω | Re: 3.54Ω
- Sensitivity: **90 dB @ 2.83V/1m** | Power: **40W RMS** | Fs: **1,100 Hz** | Frequency response: 2,500–20,000 Hz
- Qts: 1.2 | Qms: 2.0 | Qes: 3.1 | Neodymium motor | Ferrofluid VC cooling
- **Source:** [SoundImports](https://www.soundimports.eu/en/dayton-audio-cf18n-4.html) (fetched June 2026) | Price: **€30.54** (sale, was €36.95) | Stock (Jun 2026): **pre-order / OOS** (was 6 units; gone OOS)
- **Min crossover:** 2× Fs = **2,200 Hz**. Response starts 2,500 Hz — crossover must be placed above this; LR48 slope provides ample mechanical protection below it.
- **DSP correction vs TB sub (85 dB ref):** −5.0 dB pad needed.
- **Power at reference (98 dB):** 6.3W (15.8% of 40W). At burst (101 dB): 12.6W (31.5%). Well within 40W rating.
- **Why this stands out — spacing:** 58mm FP OD is the 3rd smallest in the entire candidate field, after XT25SC40-04 (43.9mm) and HiVi TN28-B (47.6mm). With DSA90-8 (92mm OD): spacing = (92+58)/2 = **75mm** — between TN1 (70mm) and B6 (73mm). With SB12PFCR25-4 (~122mm): **90mm spacing**.
- **Why this stands out — off-axis:** 18mm dome = widest off-axis dispersion of any dome candidate except ND20FA-6 (45mm FP, 19mm dome, but Fs=2,005 Hz min xover 4,010 Hz). Carbon fiber dome = detailed, low-colouration character. At 60° kitchen geometry the 18mm dome maintains output well into HF.
- **Why this stands out — power:** 40W RMS is double the typical 15-20W fabric/silk dome at this FP size. CF3 pairing (SB12PFCR25-4 + CF18N-4, €25.95 + €30.54 = €56.49 total) gives 90mm spacing with both 30W mid and 40W tweeter — very robust.
- **Concern — HF rolloff at 30° off-axis:** Reviewer noted "rolloff above 12 kHz beyond 30°." At 60° kitchen position HF above 12 kHz will be attenuated. This is less audible than mid-treble rolloff; the critical 2.8–10 kHz range may still be fine.
- **Concern — depth:** 38.3mm depth requires adequate tweeter chamber depth.
- **Carbon fiber visual note:** Woven CF dome has a distinctive dark-weave appearance — different from fabric or silk domes. Owner has removed all visual exclusions; CF appearance is noted as distinctive, not a concern.

### SEAS Prestige 27TFFNC/CG H1406-04 — Candidate (80W, low-profile, oval faceplate)
- Role: **HIGH** | Dome: 26 mm Sonolex precoated fabric | Faceplate: **69.7 × 54 mm oval** | Cutout: 46 mm | Depth: **21.5 mm** | Impedance: 4Ω | Re: 2.7Ω
- Sensitivity: **91 dB @ 2.83V/1m** | Power: **80W RMS / 200W max** | Fs: **1,170 Hz** | Frequency response: 2,500–30,000 Hz
- Double chamber magnet system | Sonolex precoated lightweight fabric
- **Source:** [SoundImports](https://www.soundimports.eu/en/seas-27tffnc-cg.html) (fetched June 2026) | Price: **€40.45** (sale, was €48.95) | Stock (Jun 2026): **pre-order / OOS** (was 4 units; gone OOS)
- **Min crossover:** 2× Fs = **2,340 Hz**. Response specified from 2,500 Hz — crossover must be placed above this; LR48 slope provides ample mechanical protection below it.
- **DSP correction vs TB sub (85 dB ref):** −6.0 dB pad needed.
- **Power at reference (98 dB):** 5.0W (6.25% of 80W). At burst (101 dB): **10.0W** (12.5%). Well within 80W/200W rating.
- **Why interesting — spacing:** Oval 69.7×54mm faceplate. Mounted portrait (54mm axis vertical): effective vertical dimension = 54mm → centre spacing with DSA90-8 (92mm OD) = (92+54)/2 = **73mm** — matching B6 (TN25 at 73mm) as joint tightest spacing, but this is a 80W tweeter. If mounted landscape (69.7mm vertical), spacing becomes (92+69.7)/2 = 81mm.
- **Why interesting — power:** 80W RMS in a non-round compact faceplate with a quality SEAS pedigree. RST28F-4 is the only competitor at 80W (104mm FP, 80W, €46.95). SEAS H1406 is smaller (69.7×54mm vs 104mm round) and €2 more.
- **Depth advantage:** 21.5mm depth is the shallowest of any tweeter candidate (even shallower than D2604/830000 at 25.4mm). Very easy to fit in any enclosure.
- **Concern — oval faceplate:** Non-round OD. Visual note only (not an exclusion). The 54mm narrow dimension is what drives tight spacing in portrait orientation. This is an aesthetically distinct look — oval tweeter above round mid above round sub.
- **Concern — narrow window SE2:** With DS115-8 (beams at 2,636 Hz), only a 296 Hz window (2,340–2,636 Hz) for the crossover. Very tight; SE1 (DSA90-8, beams 3,260 Hz) gives a much better 920 Hz window.

### SB Acoustics SB26ST-C000-5 — Candidate (high-power compact tweeter)
- Role: **HIGH** | Dome: 26 mm fine weave soft fabric | Faceplate OD: **? (unconfirmed — fetch datasheet)** | Impedance: 5Ω | Re: 4.4Ω
- Sensitivity: **91 dB @ 2.83V/1m** | Power: **80W RMS** | Fs: **870 Hz** | Xmax: 0.6 mm | Sd: 6.2 cm²
- CCAW voice coil (0.33 g moving mass) | Saturation-controlled motor | Internal pressure equalisation
- **Source:** [SoundImports](https://www.soundimports.eu/en/sb-acoustics-sb26st-c000-5.html) | [SB Acoustics](https://sbacoustics.com/product/sb26st-c000-5/) | Price: **€30.95** | Stock (June 2026): 10+
- **Min crossover:** 2× Fs = **1,740 Hz**.
- **DSP correction vs TB sub (85 dB ref):** −6.0 dB pad needed.
- **Power at reference (98 dB):** 5.0W (6.3% of 80W). At burst (101 dB): **10.0W** (12.5%). Effectively indestructible in this application.
- **5Ω note:** JAB5 at 24V → ~49W into 5Ω. Massively above the 10W needed at burst.
- **Why this matters:** 80W RMS in a ~72mm compact faceplate is the standout combination. The SB26STCN-C000-4 (same SB26 family, 72mm FP, 120W) costs €36.45; the SB26ST at €30.95 is €6 cheaper and still far exceeds any power requirement. Combines compact spacing (ST series = SB26 small-ish faceplate vs 104mm large-FP tweeters) with very high thermal robustness.
- **FP OD caveat:** SB26STCN-C000-4 (confirmed 72mm FP) is from the same SB26 chassis family. FP OD for SB26ST-C000-5 is unconfirmed — fetch datasheet before ordering. If FP = 72mm (as SB26 family standard): spacing with DSA90-8 (92mm OD) = **82mm**; with DS115-8 (116mm OD) = 94mm; with SB12PFCR25-4 (~122mm OD) = 97mm.
- **vs SB26STCN-C000-4:** SB26ST costs €6 less but has 80W vs 120W and 5Ω vs 4Ω. At the power levels in this project (10W max at burst), 80W vs 120W is irrelevant. Choose SB26ST for the €6 saving.
- **Pairings enabled:** ST1 (DS115-8 + SB26ST: 94mm spacing, 1,740–2,636 Hz window); ST2 (SB12PFCR25-4 + SB26ST: 97mm, 1,740–2,730 Hz); ST3 (DSA90-8 + SB26ST: 82mm, 1,740–3,260 Hz).

### Dayton Audio ND25FN-4 — Rejected (no faceplate — unmountable on standard baffle)
- Role: **HIGH** | Dome: 25 mm treated silk | Impedance: 4Ω | Sensitivity: 90 dB | Power: 20W RMS | Fs: 1,350 Hz
- Supplier: [SoundImports](https://www.soundimports.eu/en/dayton-audio-nd25fn-4.html) | Price: €12.36 | Stock: 10+
- **Reason:** Designed as a bare element for waveguide or custom mounting — explicitly has no faceplate. Cannot be conventionally front-baffle mounted without fabricating a custom mounting ring. Power at reference (98 dB) needs 12.6W vs 20W rated — power is fine. Excluded solely on mounting practicality grounds.

### Peerless by Tymphany BC25TG15-04 — Rejected
- Role: **HIGH** | Dome: 25 mm silk | Faceplate OD: 104 mm | Impedance: 4Ω
- Sensitivity: 93.9 dB | Power: 7W RMS | Fs: 1100 Hz
- Supplier: [SoundImports](https://www.soundimports.eu/en/peerless-by-tymphany-bc25tg15-04.html) | Price: €29.95 | Stock: 10+
- **Reason for rejection:** Power at only 7W RMS is catastrophically below the 20W minimum requirement. Would be destroyed at moderate volumes on this system.

### Peerless by Tymphany OC25SC65-04 — Rejected
- Role: **HIGH** | Dome: 25 mm coated textile | Faceplate OD: 41 mm body (faceplate-less design) | Impedance: 4Ω
- Sensitivity: 92.3 dB | Power: 12W RMS | Fs: 1400 Hz
- Supplier: [SoundImports](https://www.soundimports.eu/en/peerless-by-tymphany-oc25sc65-04.html) | Price: €26.95 | Stock: 10+
- **Reason for rejection:** Faceplate-less twist-lock design — cannot be surface-mounted to a flat baffle without custom hardware. Power at 12W RMS fails the 20W minimum requirement.

### Dayton Audio ND25FW-4 — Candidate (in stock Amazon UK)
- Role: **HIGH** | Dome: 1" (25 mm) treated silk | Round waveguide faceplate OD: 104 mm | Impedance: 4Ω
- Sensitivity: **94 dB @ 2.83V/1m** (spec sheet: 91 dB @ 1W/1m; +3 dB for 4Ω correction) | Power: 20W RMS | Fs: 1,350 Hz
- Re: 3.2Ω | Le: 0.04 mH | VC diameter: 1" | Cutout: 44.3 mm | Depth: 40 mm | Ferrofluid cooling
- Usable frequency range: 2,500–20,000 Hz
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/dayton-audio-nd25fw-4.html) (fetched June 2026); SoundImports OOS — backordered
- **Datasheet:** [research/dayton_audio_nd25fw-4.pdf](research/dayton_audio_nd25fw-4.pdf) | [original URL](https://doc.soundimports.nl/pdf/brands/Dayton%20Audio/ND25FW-4/pdf_Dayton%20Audio_ND25FW-4_1.pdf) (downloaded June 2026)
- SoundImports price: €17.95 (OOS) | **Amazon UK: in stock** (price not confirmed — Amazon page returned error June 2026)
- **DSP correction vs TB sub (85 dB ref):** −9.0 dB pad needed. Largest attenuation of any tweeter candidate.
- **Power check:** At reference (98 dB): 5.0W needed. At woofer max (101 dB): 10.0W needed. Both within 20W rating. ✓
- **Crossover minimum:** Fs 1350 Hz. Dayton's datasheet states crossover "as low as 2,500 Hz" is safe. Standard 2× rule gives 2,700 Hz minimum crossover.
- **Dome colour:** Not explicitly stated. "Treated silk dome" material. Likely grey/natural silk — confirm from product photo before ordering.
- **Faceplate:** 104 mm round — same as DX25TG59-04, D27TG35-06, RST28F-4. Widest footprint class; baffle width impact same as those drivers.
- **Key concern — off-axis dispersion:** The waveguide concentrates HF output on-axis. From the datasheet FR plot, 30° off-axis (green) begins rolling off above ~7 kHz; 45° (blue) rolls off above ~5 kHz. At the project's 60° off-axis kitchen listening position, high-frequency output above 4–5 kHz will be noticeably attenuated. The SB19ST (no waveguide, 19 mm dome) has significantly better off-axis response. **If the speaker is aimed directly at the listener this concern is reduced; if it points straight ahead on the counter, HF at 60° will sound dull.**
- **Upside of waveguide:** Reduces early reflections from kitchen surfaces directly behind and beside the listening position — can improve midrange clarity in a reflective kitchen. A trade-off, not a pure negative.
- **Vs SB19ST:** Cheaper (if similar Amazon price), higher sensitivity (needs less power), but: larger faceplate (104 vs 88 mm), narrower HF dispersion, higher Fs (min crossover 2,700 Hz vs SB19ST's 1,960 Hz). SB19ST remains better choice for off-axis listening unless speaker can be aimed.

### SB Acoustics SB21RDCN-C000-4 — INELIGIBLE (ring radiator — poor 60° off-axis)
- Role: **HIGH** | Type: Ring radiator | Dome: **21 mm fabric ring** | Faceplate OD: **58.0 mm** round | Cutout: **38.25 mm** | Depth: **22.7 mm total** (3.2 mm protrusion, ~19.5 mm behind baffle) | Impedance: 4Ω | Re: 3.1Ω | Le: 0.04 mH
- Sensitivity: **89.5 dB @ 2.83V/1m** | Power: **40W RMS** (IEC HP Butterworth 2600 Hz 12dB/oct) | Fs: **850 Hz**
- Sd: 4.6 cm² | VC dia: 20.4 mm | VC height: 1.5 mm | Air gap: 2.0 mm | Xlin (p-p): 0.5 mm | Mms: 0.25 g | BL: 1.3 Tm | Qms: 2.71 | Qes: 2.45 | Qts: 1.28 | Flux density: 0.9 T
- Dome colour: **Dark** (black ring fabric, confirmed from SB Acoustics datasheet photo)
- Net weight: **0.06 kg** (neodymium — lightest tweeter candidate)
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/sb-acoustics-sb21rdcn-c000-4-tweeter) | **Datasheet:** [research/sb_acoustics_sb21rdcn-c000-4.pdf](research/sb_acoustics_sb21rdcn-c000-4.pdf) | [SB Acoustics URL](https://sbacoustics.com/wp-content/uploads/2020/04/SB21RDCN-C000-4.pdf) | Price: **£41.60** | Stock (Jun 2026): UK in stock
- **Min crossover:** 2× Fs = **1,700 Hz** — comfortable 1,100 Hz margin below project target.
- **DSP correction vs TB sub (85 dB ref):** −4.5 dB attenuation.
- **Power at reference (4Ω, 98 dB):** 10^((98−89.5)/10) = **7.1W** (17.7% of 40W ✓). At burst (101 dB): **14.1W** (35.3% of 40W ✓). Well within rating.
- **Available @ 24V into 4Ω:** ~61W >> 14.1W ✓.
- **Centre spacing (FP OD 58 mm):** DSA90-8 (92mm OD) → **75mm** | DS115-8 (115.6mm OD) → **87mm** | SB12PFCR25-4 (~122mm OD) → **90mm**
- **Ineligible — off-axis:** Ring radiator. Its 58 mm faceplate (≤90 mm spacing with any mid ≤122 mm) and 22.7 mm depth were attractive, but ring radiators measure horn-like at 60° off-axis (RAW-CAt Tweeter Shootout Part 6, Nov 2025) — disqualifying for the 60° kitchen geometry. The compactness advantage cannot redeem it. Pairings XCR1/XCR2/XCR3 are withdrawn.

### Scan-Speak Discovery D2604/833000 ★ — lowest Fs dome in field, tuned rear chamber (Willys-Hifi)
- Role: **HIGH** | Type: Textile dome | Dome: **26 mm dark textile, wide surround** | Faceplate OD: **104.2 mm** round | Cutout: **74 mm** | Depth: **~55 mm total** (~5 mm protrusion, ~50 mm behind baffle; tuned rear chamber — much deeper than D2604/830000's 25.4 mm) | Impedance: 4Ω | Re: 2.8Ω | Le: 0.04 mH
- Sensitivity: **93 dB @ 2.83V/1m** | Power: **100W** (IEC 18.4) / **240W** (IEC 18.2) | Fs: **475 Hz**
- Sd: 8 cm² | Mms: 0.42 g | Cms: 0.27 mm/N | Rms: 0.49 kg/s | BL: 2.2 Tm | Qms: 2.55 | Qes: 0.71 | Qts: 0.55 | Vas: 0.02 L
- Operating frequency: **2,500–20,000 Hz** | Scan-Speak recommended crossover: **2nd order HP Butterworth 2.5 kHz** (our 2,800 Hz LR48 is within specification)
- Dome colour: **Dark** (dark textile, confirmed from Scan-Speak datasheet photo)
- Net weight: 0.8 kg | 5× Ø4.2mm mounting holes on 92mm pitch circle at 72° spacing
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/scanspeak-d2604-833000-tweeter) | **Datasheet:** [research/scanspeak_d2604-833000.pdf](research/scanspeak_d2604-833000.pdf) | [Scan-Speak URL](https://www.scan-speak.dk/datasheet/pdf/d2604-833000.pdf) | Price: **£41.88** | Stock (Jun 2026): UK in stock
- **Min crossover:** 2× Fs = **950 Hz** — lowest of any dome candidate in the project field. Scan-Speak confirms operating from 2,500 Hz; our 2,800 Hz LR48 crossover is within spec.
- **DSP correction vs TB sub (85 dB ref):** −8.0 dB attenuation.
- **Power at reference (4Ω, 98 dB):** 10^((98−93)/10) = **3.2W** (3.2% of 100W). At burst (101 dB): **6.3W** (6.3%). Effectively indestructible.
- **Available @ 24V into 4Ω:** ~61W >> 6.3W ✓.
- **Centre spacing (FP OD 104.2 mm):** DSA90-8 (92mm) → **98mm** | DS115-8 (115.6mm) → **110mm** | SB12PFCR25-4 (~122mm) → **113mm**
- **Why this stands out:** Lowest Fs dome enables widest crossover window. If a 5" mid (beaming ~2,200 Hz) is considered, D2604/833000 is the only dome compatible. At 104mm FP it bolt-interchanges with SB29RDNC, R2604/833000, SEAS H1189-06 without baffle changes.
- **Critical depth concern:** ~55mm total depth (50mm behind baffle). The tuned rear chamber is structural — cannot be shortened. Plan for dedicated tweeter chamber ≥55mm deep or recessed tweeter rebate.
- **vs D2604/830000 (£35.65 Willys, in index):** 830000 = Fs ~630 Hz (min xover ~1,260 Hz), 92 dB, 25.4mm depth. 833000 = Fs 475 Hz (min xover 950 Hz), 93 dB, ~55mm depth. Choose 833000 when pairing with 5"+ mids or sub-1,200 Hz crossover flexibility is needed.
- **Pairings enabled (new combo IDs):**
  - **D6R1:** DSA90-8 + D2604/833000 → 98mm spacing, window 950–3,260 Hz (2,310 Hz wide — widest combo window in the project)
  - **D6R2:** DS115-8 + D2604/833000 → 110mm spacing, window 950–2,636 Hz (1,686 Hz wide)
  - **D6R3:** SB12PFCR25-4 + D2604/833000 → 113mm spacing, window 950–2,730 Hz (1,780 Hz wide)

### Morel MDT22T — ❌ REJECTED (60° off-axis) | Retain for on-axis / compact scenarios
- Role: **HIGH** | Type: Soft dome | Dome: **28 mm selected soft fabric (dark)** | Faceplate: **54 × 54 mm SQUARE** (R5.5mm corner radii) | Cutout: **Ø44.0 mm** (chassis) | Depth: **~55 mm total** (3 mm protrusion, ~52 mm behind baffle) | Impedance: 8Ω | Re: 5.2Ω | Le: 0.05 mH @ 1kHz
- Sensitivity: **89 dB @ 1W/1m** | Power: **80W RMS** / **500W transient** (10ms) | Fs: **650 Hz** | Frequency response: **1,800–25,000 Hz** | Morel recommended crossover: 2.5 kHz / 12dB
- VC dia: 28 mm | VC height: 2.5 mm | VC former: Aluminum | BL: 2.8 N·A | Flux density (B): 1.4 T | Mms: 0.47 g | Sd: 6.0 cm² | Magnetic gap: 2.5 mm | Mounting: Ø3.5mm holes on Ø43.5mm pitch circle (4 corner holes in square faceplate)
- Q factors: **not published by Morel** (blank in datasheet) | Magnetically shielded: Yes | Net weight: 0.09 kg
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/morel-mdt22-soft-dome-tweeter) | **Datasheet:** [research/morel_mdt22t.pdf](research/morel_mdt22t.pdf) | [Willys CDN URL](https://cdn.shopify.com/s/files/1/0809/2387/files/MOREL_MDT22_DATASHEET.pdf?v=1686654880) | Price: **£47.55** | Stock (Jun 2026): UK in stock
- **Min crossover:** 2× Fs = **1,300 Hz** — 700 Hz better margin than MDT12 (min xover 2,000 Hz).
- **DSP correction vs TB sub (85 dB ref):** −4.0 dB attenuation.
- **Power at reference (8Ω, 98 dB):** 10^((98−89)/10) = **7.9W** (9.9% of 80W ✓). At burst (101 dB): **15.9W** (19.9% ✓).
- **Available @ 24V into 8Ω:** ~31W >> 15.9W ✓.
- **Centre spacing (FP 54mm sq):** DSA90-8 (92mm) → **73mm** | DS115-8 (115.6mm) → **85mm** | SB12PFCR25-4 (~122mm) → **88mm**
- **Why considered:** Same 54mm square faceplate as MDT12 → same tight spacing. Fs 650 Hz → min xover 1,300 Hz is 700 Hz lower than MDT12's 2,000 Hz.
- **Critical depth concern:** ~55mm total depth (52mm behind baffle). Morel uses a vented motor system unlike the MDT12's chamberless design. **MDT22T is 36mm deeper than MDT12.** Must accommodate ≥52mm behind baffle at tweeter location.
- **vs Morel MDT12 (£39.50 Willys, in index):** MDT12: Fs 1,000 Hz (min xover 2,000 Hz), 19mm deep, £39.50. MDT22T: Fs 650 Hz (min xover 1,300 Hz), 55mm deep, £47.55. Same: 54mm sq FP, 28mm dome, 80W, dark fabric, ~89 dB. Choose MDT12 when depth is critical. Choose MDT22T when crossover must be below 2,000 Hz and 52mm depth is achievable.

### SB Acoustics SB29RDAC-C000-4 — Candidate (ferrite ring dome, cheaper SB29RDNC alternative; Willys-Hifi)
- Role: **HIGH** | Type: Ring dome | Dome: **29 mm fabric ring** | Faceplate OD: **103.8 mm** round | Cutout: **70.0 mm** | Depth: **37.25 mm total** (4.0 mm protrusion, 33.25 mm behind baffle) | Impedance: 4Ω | Re: 3.0Ω | Le: 0.05 mH | Net weight: 0.54 kg | Cast aluminium faceplate
- Sensitivity: **93 dB @ 2.83V/1m** | Power: **100W** | Fs: **600 Hz** | Sd: 9.6 cm² | VC dia: 29mm | Air gap: 2.5mm | Xlin (p-p): 0.5mm | Mms: 0.45g | BL: 2.4 Tm | Qms: 2.2 | Qes: 0.9 | Qts: 0.64 | Flux density: 1.1T | Mounting: 7× Ø4.2mm holes
- ⚠️ Willys product page states cutout 74mm — **SB Acoustics datasheet confirms 70.0mm**
- Dome colour: **Dark** (dark ring fabric, confirmed from SB Acoustics datasheet photo)
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/sb-acoustics-sb29rdac-c000-4-tweeter) | **Datasheet:** [research/sb_acoustics_sb29rdac-c000-4.pdf](research/sb_acoustics_sb29rdac-c000-4.pdf) | [SB Acoustics URL](https://sbacoustics.com/wp-content/uploads/2025/03/SB29RDAC-C000-4.pdf) | Price: **£44.39** | Stock (Jun 2026): UK in stock
- **Min crossover:** 2× Fs = **1,200 Hz**. | **DSP correction:** −8.0 dB. | **Power at reference:** 3.2W (3.2% of 100W); burst 6.3W (6.3%). Indestructible.
- **Centre spacing (FP OD 103.8 mm):** DSA90-8 → 98mm | DS115-8 → 110mm | SB12PFCR25-4 → 113mm
- **vs SB29RDNC-C000-4 (£54.31 Willys, confirmed in index):** RDAC = ferrite, RDNC = neodymium. Both 100W, ~104mm FP, 29mm ring dome, Fs ~580–600 Hz. RDAC saves **£9.92** (18%). Both within limits. RDAC is the value choice; prefer RDNC only for reduced mounting weight.

### SB Acoustics SB21RDC-C000-4 — INELIGIBLE (ring radiator — poor 60° off-axis)
- Role: **HIGH** | Type: Ring radiator | Dome: **21 mm fabric ring** | Faceplate OD: **92.0 mm** round | Cutout: **62.5 mm** | Depth: **30.6 mm total** (3.3 mm protrusion, 26.5 mm behind baffle) | Impedance: 4Ω | Re: 3.1Ω | Le: 0.04 mH | Net weight: 0.33 kg
- Sensitivity: **90 dB @ 2.83V/1m** | Power: **40W RMS** (IEC HP Butterworth 2600 Hz 12dB/oct) | Fs: **760 Hz**
- Sd: 4.6 cm² | VC dia: 20.4mm | VC height: 1.5mm | Air gap: 2.5mm | Xlin (p-p): 1.0mm | Mms: 0.25g | BL: 1.5 Tm | Qms: 2.54 | Qes: 1.64 | Qts: 1.0 | Flux density: 1.02T
- ⚠️ Willys product page states 60W power — **SB Acoustics datasheet confirms 40W**
- Dome colour: **Dark** (dark ring fabric, confirmed from SB Acoustics datasheet photo)
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/sb-acoustics-sb21rdc-c000-4-tweeter) | **Datasheet:** [research/sb_acoustics_sb21rdc-c000-4.pdf](research/sb_acoustics_sb21rdc-c000-4.pdf) | [SB Acoustics URL](https://sbacoustics.com/wp-content/uploads/2020/02/SB21RDC-C000-4.pdf) | Price: **£36.55** | Stock (Jun 2026): UK in stock
- **Min crossover:** 2× Fs = **1,520 Hz**. | **DSP correction:** −5.0 dB. | **Power at reference:** 6.3W (15.8% of 40W ✓); burst 12.6W (31.5% ✓).
- **Centre spacing (FP OD 92 mm):** DSA90-8 (92mm) → 92mm | DS115-8 → 104mm | SB12PFCR25-4 → 107mm
- **Ineligible — off-axis:** Ring radiator (the "ring dome" label on the Willys page is a misnomer — SB Acoustics classes it as a ring radiator). Same disqualifying horn-like 60° off-axis dispersion as all ring radiators (RAW-CAt Tweeter Shootout Part 6, Nov 2025).

### Scan-Speak Illuminator D3004/602010 ★★ — Candidate (ultra-low Fs dome, 850 Hz min xover; lautsprechershop.de)
- Role: **HIGH** | Type: Soft dome (textile) + rear chamber | Dome: **26 mm** | Faceplate OD: **61.9 mm** round | Impedance: 4Ω | Power: **50W RMS / 130W max**
- Sensitivity: **89.6 dB @ 2.83V/1m** | Fs: **425 Hz**
- ⚠ Full T/S (Re, Qts, cutout, depth) not confirmed from LSS page — fetch Scan-Speak Illuminator D3004 datasheet for complete mechanical dimensions
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS tweeter index, June 2026) | LSS price: **€142.20 inc VAT / €119.50 exc VAT** | Stock (Jun 2026): **in stock at LSS** | Previously listed ⚠ DISC at Willys (last stock £115.05) — LSS confirms available
- **Min crossover:** 2× Fs = **850 Hz** — lowest of any dome in the entire catalogue. Enables mid/tweeter crossover below 1 kHz.
- **DSP correction vs TB sub (85 dB ref):** −4.6 dB attenuation (4Ω: 1W sens = 89.6 − 3.01 = 86.59 dB).
- **Power at reference (4Ω, 98 dB):** 10^((98−86.59)/10) = **13.8W** (27.6% of 50W ✓). At burst (101 dB): **27.6W** (55.2% of 50W ✓; 21.2% of 130W ✓).
- **Centre spacing (FP OD 61.9 mm):** DSA90-8 (92.3mm) → **77mm** | DS115-8 (115.6mm) → **89mm** | SB12PFCR25-4 (~122mm) → **92mm** | 12W/4524G00 (~125mm) → **93mm** | 15W/4434G00 (114mm) → **88mm** | WF118WA07 (118mm) → **90mm** | Morel 428 (118.5mm) → **90mm**
- **Why this stands out:** 850 Hz minimum crossover is 90 Hz lower than any ring radiator and 250 Hz lower than any dome in the catalogue. The compact 61.9mm FP creates the tightest achievable centre-spacing — 77–92mm depending on mid — minimising vertical lobe smearing. With a 4" mid (beaming ~2,600–2,900 Hz), crossover window is 850–2,600+ Hz (over 1,700 Hz of freedom). With a 5.25" mid (beaming ~2,390 Hz), window is 850–2,390 Hz — still excellent. Scan-Speak Illuminator-grade transient response and low distortion at 850 Hz crossover point.
- **Pairings:** ILL1/ILL2/ILL3 (existing combos) updated to remove DISC flag; LS-series in combos.md covers new LSS mids.

### Scan-Speak Illuminator R3004/602010 — INELIGIBLE (ring radiator — poor 60° off-axis)
- Role: **HIGH** | Type: Ring radiator | FP OD: **61.9 mm** round | Impedance: 4Ω | Power: not confirmed from page
- Fs: **420 Hz** | Sensitivity: not confirmed from LSS page
- ⚠ Full T/S (Re, Qts, sensitivity, power, cutout, depth) not confirmed — fetch Scan-Speak R3004/602010 datasheet from scan-speak.dk before ordering
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS tweeter index, June 2026) | LSS price: **€179.10 inc VAT / €150.50 exc VAT** | Stock (Jun 2026): in stock at LSS
- **Min crossover:** 2× Fs = **840 Hz** — 10 Hz lower than D3004/602010 (850 Hz). Narrowly the most flexible crossover window of any tweeter in this catalogue.
- **Centre spacing (FP OD 61.9 mm):** DSA90-8 → **77mm** | DS115-8 → **89mm** | 12W/4524G00 (~125mm) → **93mm** | 15W/4434G00 (114mm) → **88mm** | WF118WA07 (118mm) → **90mm** | Morel 428 (118.5mm) → **90mm**
- **Ineligible — off-axis:** Ring radiator. Same compact 61.9 mm Illuminator chassis and ultra-low Fs (420 Hz) as the D3004/602010 dome, but ring radiators measure horn-like at 60° off-axis (RAW-CAt Tweeter Shootout Part 6, Nov 2025) — disqualifying for the 60° kitchen geometry. The **D3004/602010 dome** (same chassis, Fs 425 Hz, 850 Hz min crossover) is the eligible alternative — see entry above.

### Audaphon TWS 30/4 ★★ — Candidate (30mm dome, Fs=470Hz, 93dB; lautsprechershop.de exclusive)
- Role: **HIGH** | Type: Soft dome (fabric) | Dome: **30 mm** | Faceplate OD: **104 mm** round | Metal faceplate | Impedance: 4Ω | Power: **100W**
- Sensitivity: **93 dB @ 2.83V/1m** | Fs: **470 Hz** | LSS house brand — **not available at SI/HFC/Willys**
- ⚠ Full T/S (Re, Qts, cutout, depth) not confirmed from LSS page — datasheet not yet fetched
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS tweeter index, June 2026) | LSS price: **€79.00 inc VAT / €66.39 exc VAT** | Stock (Jun 2026): in stock at LSS
- **Min crossover:** 2× Fs = **940 Hz** — second-lowest dome in catalogue after D3004/602010 (850 Hz); 160 Hz lower than SEAS H1189-06 (1,100 Hz).
- **DSP correction vs TB sub (85 dB ref):** −8.0 dB attenuation (4Ω: 1W sens = 93 − 3.01 = 89.99 dB).
- **Power at reference (4Ω, 98 dB):** 10^((98−89.99)/10) = **6.3W** (6.3% of 100W ✓). At burst (101 dB): **12.6W** (12.6% ✓). Effectively indestructible at project SPL.
- **Centre spacing (FP OD 104 mm):** DSA90-8 → **98mm** | DS115-8 → **110mm** | SB12PFCR25-4 → **113mm** | 12W/4524G00 (~125mm) → **114mm** | 15W/4434G00 (114mm) → **109mm** | WF118WA07 (118mm) → **111mm** | Morel 428 (118.5mm) → **111mm**
- **Why this stands out:** 940 Hz minimum crossover dramatically lower than any comparable 104mm dome from other vendors. The 30mm dome is the largest diaphragm of any candidate — potential for smooth, natural high frequency. 93 dB high sensitivity ensures near-indestructible power at project SPL. At €79 it is the best-value extremely-low-Fs dome per unit of crossover flexibility.
- **vs D3004/602010 (850 Hz, €142):** D3004 is 90 Hz lower in min xover and 42mm more compact (62mm FP). TWS 30/4 saves €63 for a 90 Hz crossover headroom penalty. For pairings where the 104mm FP spacing is acceptable and 940 Hz is sufficient, TWS 30/4 is the clear value choice.
- **vs SEAS H1189-06 (1,100 Hz, £55.00 Willys / £56.92 HFC):** TWS 30/4 has 160 Hz lower min xover and costs more at LSS (€79.00 vs €71.86). Prefers TWS 30/4 when crossover window matters; H1189-06 when buying from UK suppliers without EU delivery cost.

### Dayton Audio RS28A-4 ★ — Candidate (28mm 100W dome, Fs=600Hz; lautsprechershop.de)
- Role: **HIGH** | Type: Soft dome (fabric) | Dome: **28 mm** | Faceplate OD: **103 mm** round | Impedance: 4Ω | Power: **100W**
- Sensitivity: **91 dB @ 2.83V/1m** | Fs: **600 Hz** | Not available at SI/HFC/Willys — LSS exclusive in UK context
- ⚠ Full T/S (Re, Qts, cutout, depth) not confirmed from LSS page — fetch Dayton RS28A-4 datasheet for complete data
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS tweeter index, June 2026) | LSS price: **€89.40 inc VAT / €75.13 exc VAT** | Stock (Jun 2026): in stock at LSS
- **Min crossover:** 2× Fs = **1,200 Hz** — same class as SB29SDAC (1,200 Hz) and D2604/830000 (1,260 Hz).
- **DSP correction vs TB sub (85 dB ref):** −6.0 dB attenuation (4Ω: 1W sens = 91 − 3.01 = 87.99 dB).
- **Power at reference (4Ω, 98 dB):** 10^((98−87.99)/10) = **10.0W** (10% of 100W ✓). At burst (101 dB): **20.0W** (20% ✓). Effectively indestructible.
- **Centre spacing (FP OD 103 mm):** DSA90-8 → **98mm** | DS115-8 → **109mm** | SB12PFCR25-4 → **112mm** | 12W/4524G00 (~125mm) → **114mm** | 15W/4434G00 (114mm) → **109mm** | WF118WA07 (118mm) → **111mm**
- **Why considered:** 100W power rating at €89.40 is excellent value for a 103mm-class dome. 91 dB sensitivity (2 dB lower than TWS 30/4) means 2 dB less DSP pad required. 28mm dome in standard class for this FP size.
- **vs Audaphon TWS 30/4 (940 Hz, €79):** TWS 30/4 has 260 Hz lower min xover, 2 dB higher sensitivity, 1mm larger dome, €10 cheaper. RS28A-4 wins only on 2 dB lower DSP pad requirement — a marginal advantage. Prefer TWS 30/4 for the 260 Hz crossover freedom in most pairings. RS28A-4 is relevant only if 940 Hz → 1,200 Hz crossover gap is unimportant and 91 dB sensitivity is preferred.

### Wavecor TW022WA05 ★★ — Candidate (22mm silk dome, Fs=750Hz; lautsprechershop.de)
- Role: **HIGH** | Type: Soft dome (silk) | Dome: **22 mm** | Faceplate OD: **103.75 mm** round | Impedance: 4Ω
- Sensitivity: **? (unconfirmed — fetch datasheet)** | Power: **? (unconfirmed — fetch datasheet)** | Fs: **750 Hz** | LSS-only in UK context
- ⚠ Full T/S (Re, Qts, exact sensitivity, power) not confirmed from LSS page — fetch Wavecor TW022WA05 datasheet before ordering
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS tweeter index, June 2026) | LSS price: **€78.10 inc VAT / €65.63 exc VAT** | Stock (Jun 2026): in stock at LSS
- **Min crossover:** 2× Fs = **1,500 Hz** — comfortable margin below all standard mid beaming limits (≥2,400 Hz).
- **DSP correction vs TB sub (85 dB ref):** Not calculable — sensitivity unconfirmed. Fetch datasheet.
- **Power at reference:** Not calculable — sensitivity unconfirmed. Fetch datasheet.
- **Available @ 24V into 4Ω:** ~61W >> 40W ✓.
- **Centre spacing (FP OD 103.75 mm):** DSA90-8 → **98mm** | DS115-8 → **110mm** | 12W/4524G00 (~125mm) → **114mm** | 15W/4434G00 (114mm) → **109mm** | WF118WA07 (118mm) → **111mm** | Morel 428 (118.5mm) → **111mm**
- **Why this stands out:** At €78.10 it prices between SB26STCN (€36.45, 25mm, Fs=950Hz) and SEAS H1189-06 (€71.86, 27mm, Fs=550Hz). The 22mm dome is smaller than all 25–30mm dome candidates → slightly wider off-axis dispersion above 10 kHz. Fs=750 Hz gives 1,500 Hz min crossover — broad window for all mids in the catalogue.
- **Concern:** All specs estimated — datasheet required. 103.75mm FP is large (same class as H1189-06, DX25TG59-04).
- **vs TW022WA06 (€80.30, +ferrofluid):** €2.20 more for ferrofluid. At ≤40W burst in this project, ferrofluid is unnecessary. Prefer WA05.

### SEAS 22TAF/G — ❌ REJECTED (60° off-axis — owner, June 2026) | Sd 5.9 cm² → D=27.4mm → same class as RST28F

### Wavecor TW022WA06 ★★ — Candidate (22mm silk dome + ferrofluid, Fs=750Hz; lautsprechershop.de)
- Role: **HIGH** | Same as TW022WA05 but with magnetic fluid (ferrofluid) added to voice coil gap for enhanced thermal handling.
- LSS price: **€80.30 inc VAT / €67.48 exc VAT** | Stock (Jun 2026): in stock at LSS
- All acoustic specs as TW022WA05 (specs unconfirmed — fetch datasheet before ordering). Ferrofluid lowers Fs slightly and adds thermal headroom; exact values unconfirmed.
- **vs TW022WA05 (€78.10):** €2.20 premium for ferrofluid. At ≤40W burst in this project, ferrofluid provides marginal benefit. Prefer WA05 on value unless continuous high-power use is expected.

---

## Midranges

### 101 dB Gate — Verified Shortlist (June 2026)

Gate: Max SPL = Sens@2.83V + 10·log₁₀(P/P_ref) ≥ 101 dB, where P_ref = 2W (4Ω) or 1W (8Ω). Power basis: IEC or DIN continuous RMS. All values computed from verified datasheet specs.

Sealed box formula: Fc = Fs·√(1+Vas/Vb); Qtc = Qts·√(1+Vas/Vb). Rec = Qtc≈0.75 (DSP-corrected target). Min = smallest box satisfying both Fc≤160 Hz AND Qtc≤0.9.

| Driver | Price | Max SPL | Fs ratio @150Hz | f_beam | Sealed Vb rec → Fc | Sealed Vb min → Fc | P @101 dB | Result |
|--------|-------|---------|-----------------|--------|--------------------|--------------------|-----------|--------|
| **SB12MNRX2-25-4** ★ SELECTED | £48 Willys / €62 SI | **104.5 dB** | 2.36× ✓ | 2,746 Hz ✓ | **1.2 L → 149 Hz** | 1.2 L → 149 Hz† | 22.4W | ✓ All gates |
| **Morel EW 428** | €153 LSS | **108.8 dB** | 2.42× ✓ | 2,570 Hz ✓‡ | **1.3 L → 133 Hz** | 0.85 L → 159 Hz | 25.1W | ✓ All gates |
| **Morel EM 428** | €134 LSS | **108.8 dB** | 2.21× ✓ | 2,570 Hz ✓‡ | **1.5 L → 124 Hz** | 0.92 L → 149 Hz | 25.1W | ✓ All gates |
| **Morel CAW 428** | €109 LSS | **109.8 dB** | 2.03× ✓§ | 2,570 Hz ✓‡ | **1.6 L → 146 Hz** | 1.22 L → 160 Hz† | 20.0W | ✓ (Vb ≥ 1.22 L) |
| **12W/8524G00** (8Ω) | unverified | **102.0 dB** | 2.88× ✓ | 2,527 Hz ✓‡ | **1.8 L → 122 Hz** | 1.2 L → 146 Hz | 31.6W | ✓ (large box) |
| **WF118WA07** | €96 LSS | **101.0 dB** | 2.68× ✓ | 2,641 Hz ✓ | **1.5 L → 117 Hz** | 0.93 L → 140 Hz | 50.2W≈limit | ⚠ burst at rated limit |

†Binding constraint is Fc≤160 Hz, not Qtc; a smaller box pushes Fc above 160 Hz before Qtc hits 0.9.  
‡Sd = 57–59 cm² exceeds the ≤55 cm² proxy; measured f_beam ≥ 2,500 Hz — operative gate passes.  
§CAW 428: Fs=74 Hz is at the 2× minimum margin.

**Enclosure note:** All candidates except 12W/8524G00 fit comfortably in a 1.2–1.6 L sealed mid chamber. The 12W/8524G00 wants 1.8 L for Qtc=0.75; it squeezes into 1.2 L at Qtc=0.9 but the 1.8 L preference makes it a poor fit for a compact build.

**Drivers failing Gate 1 (representative):** DS115-8 100.7 dB; SB12PFCR25-4 99.3 dB; B4N 99.0 dB; SB12NRX25-4 100.3 dB. All fall short because they're in the 87–88 dB / 25–35W class.

---

### Dayton Audio DSA90-8 — Candidate (top-ranked)
- Role: **MID** | Size: 3" | Frame OD: 92.3 mm round | Impedance: 8Ω
- Cone: Black anodised aluminium | Dust cap: Concave, black (stealth)
- Sensitivity: 84.7 dB | Power: 20 W RMS / 40 W max | Xmax: ±2.5 mm | Fs: 66.6 Hz
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/dayton-audio-dsa90-8.html) (specs fetched June 2026)
- **Datasheet:** [research/dayton_audio_dsa90-8.pdf](research/dayton_audio_dsa90-8.pdf) | [original URL](https://www.parts-express.com/pedocs/specs/295-522--dayton-audio-DSA90-8-specifications.pdf)
- SoundImports price: €34.95 | Stock (June 2026): 10+
- **Why liked:** Most compact frame that passes the circular rule. Black anodised cone and concave dust cap are the most visually stealthy option available. Runs cleanly past 8 kHz. Per-pairing crossover window in combos.md. 10+ in stock.
- **Concern:** 20 W RMS rating is modest. Fs of 66.6 Hz means a 120 Hz sub/mid crossover places it only 1.8× above Fs — marginal excursion headroom at the low end. **Mitigated by raising the crossover to 150–160 Hz** (the TB sub handles this easily), which increases the Fs margin to 2.25× and brings peak power within the 40 W max rating.
- **DSP adjustment needed:** +0.3 dB gain to match TB sub reference level (85 dB). Effectively zero correction — the best-matched mid candidate.

### Dayton Audio TCP115-8 — Candidate
- Role: **MID** | Size: 4" | Frame OD: 116 mm round | Impedance: 8Ω
- Cone: Treated paper | Dust cap: Inverted paper (low-profile, dark) | Surround: High-roll rubber
- Sensitivity: 81.9 dB | Power: 40 W RMS / 80 W max | Xmax: ±4.0 mm | Fs: 59.2 Hz
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/dayton-audio-tcp115-8.html) (specs fetched June 2026)
- **Datasheet:** [research/dayton_audio_tcp115-8.pdf](research/dayton_audio_tcp115-8.pdf) | [original URL](https://www.daytonaudio.com/images/resources/295-416--dayton-audio-tcp115-8-specification-sheet.pdf)
- SoundImports price: €14.01 | Stock (June 2026): **10+ in stock**
- **Why liked:** Warmest character of all evaluated mids — punchy low-mids suit the GHM-inspired tonal goal best. 4.0 mm Xmax gives the most excursion headroom of any candidate at the 150 Hz crossover. 40 W RMS / 80 W max is double the DSA90-8's power rating. Fs 59.2 Hz means a 150 Hz crossover sits 2.53× above resonance — better margin than the DSA90-8. Round frame passes circular rule. Very affordable at €14.01.
- **Concern:** Sensitivity of 81.9 dB requires +3.1 dB DSP gain to match TB sub reference level (85 dB) — this roughly doubles the amplifier power demand vs a sensitivity-matched driver. The JAB5 official datasheet (confirmed June 2026) only specifies 100W at 36V into 6Ω — no 24V/8Ω figure is published. Derived estimate is ~31W at 24V into 8Ω, which is a deficit for TCP115-8's 40.7W RMS need. A 29V supply closes the RMS gap but burst headroom remains short. See amp.md for full analysis.

### Dayton Audio DS115-8 — Candidate (top-ranked 8Ω)
- Role: **MID** | Size: 4" | Frame OD: 115.6 mm round | Impedance: 8Ω
- Cone: **Coated paper — confirmed dark from official Dayton Audio datasheet (PDF)** | Surround: Half-roll rubber
- Sensitivity: 85.3 dB @ 2.83V/1m | Power: 35W RMS | Xmax: 4.1 mm | Fs: 55.2 Hz
- Qts: 0.38 | Qms: 2.10 | Qes: 0.46 | Re: 5.8Ω | Le: 0.8 mH | Mms: 7.9 g | Cms: 1.05 mm/N | BL: 5.88 Tm | Vas: 4.33 L | Sd: 54.1 cm² | Vd: 22.2 cm³
- Baffle cutout: 93.6 mm | Depth: 54.7 mm | VC diameter: 25.4 mm
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/dayton-audio-ds115-8.html) | [Dayton Audio product page](https://www.daytonaudio.com/product/1054/ds115-8-4-designer-series-woofer-speaker-8-ohm) | Datasheet: [research/dayton_ds115-8_specifications.pdf](research/dayton_ds115-8_specifications.pdf) | [original URL](https://www.parts-express.com/pedocs/specs/295-424--dayton-audio-ds115-8-specifications.pdf)
- SoundImports price: €36.95 | Stock (June 2026): 4 units
- **Measured data (DATS + Dayton FRD, in-repo):** [research/measured/ds115-8/](research/measured/ds115-8/) — on-axis + 15/30/45° FRD, ZMA, DATS T/S. Confirms 83.9 dB/1W (= 85.3 dB/2.83V via Re 5.79Ω).
- **Measured FR observations:** flat ±0.5 dB 150 Hz–2 kHz; mild +1.3 dB rise at 1.5 kHz (DSP-flatten before LP); large **+8.2 dB cone breakup at 6.5 kHz** — sits 2.1 oct above the 1500 Hz LR4 LP → suppressed ~50 dB → inaudible (optional DSP notch for insurance). 45° off-axis holds flat to ~1.5 kHz then beams — validates the 1500 Hz crossover for the off-axis kitchen position.
- **In the 0.59 L soil-pipe chamber:** Vas/Vb = 7.3 → **Fc ≈ 159 Hz, Qtc ≈ 1.09** (resonance lands at the crossover; mild hump). 150 Hz is the practical low limit; mid is excursion-limited in the 150–200 Hz region. See [enclosure.md](enclosure.md) — consider a ~180 Hz sub/mid crossover to work the mid above its resonance.
- **Why liked:** Best Fs margin of any 8Ω candidate (55.2 Hz → 2.72× at 150 Hz crossover). Best Xmax of any 8Ω candidate (4.1 mm). Sensitivity 85.3 dB is essentially a perfect match to the 85 dB sub — only −0.3 dB DSP correction needed (zero in practice). 35W RMS provides comfortable thermal margin. Datasheet explicitly states "Cosmetic frame with low profile lip, designed for front mounting — no countersinking required." Confirmed dark coated paper cone — visual rule passes.
- **Concern:** Only 4 units in stock — enough for one build but no surplus. Re 5.8Ω is slightly higher than a standard 8Ω driver; the amp channel draws slightly less current than a true 8Ω load at the same voltage.
- **DSP adjustment needed:** −0.3 dB (effectively zero).

### HiVi Swan B4N — Candidate
- Role: **MID** | Size: 4" | Frame OD: 116.5 mm round | Cutout: 108 mm | Depth: 67.6 mm | Impedance: 8Ω
- Cone: Aluminium/bronze alloy (bright metallic finish) | Surround: Rubber
- Sensitivity: 85 dB @ 2.83V/1m | Power: 25W RMS / 50W max | Xmax: 3.2 mm
- **T/S (CLIO, Sample 5, HiVi lab, 2004-05-09 — authoritative):** Fs: **66.27 Hz** | Re: 6.40 Ω | Qms: 2.94 | Qes: 0.54 | Qts: 0.46 | Mms: 7.86 g | Cms: 0.73 mm/N | Vas: 2.86 L | Bl: 6.22 N/A | L1K: 0.82 mH | L10K: 0.38 mH | Effective cone dia: 82 mm
- **Fs discrepancy:** SoundImports product page lists Fs = 56 Hz — contradicted by HiVi's own CLIO lab measurement (66.27 Hz). CLIO figure used for all calculations.
- **Source:** [SoundImports](https://www.soundimports.eu/en/hivi-b4n.html) | Datasheets: [research/hivi_b4n_datasheet_1.pdf](research/hivi_b4n_datasheet_1.pdf) (drawings + FR) | [research/hivi_b4n_datasheet_2.pdf](research/hivi_b4n_datasheet_2.pdf) (CLIO T/S + impedance) | Original URLs: [pdf_hiVi_B4N_1.pdf](https://doc.soundimports.nl/pdf/brands/HiVi/B4N/pdf_hiVi_B4N_1.pdf) | [pdf_hiVi_B4N_2.pdf](https://doc.soundimports.nl/pdf/brands/HiVi/B4N/pdf_hiVi_B4N_2.pdf)
- SoundImports price: €22.45 | Stock (June 2026): 10+
- **Fs margin at 150 Hz crossover:** 150/66.27 = **2.26×** — passes ≥2× minimum. Tighter than DS115-8 (2.72×). Previously estimated as 2.68× based on the incorrect SI page figure.
- **Frequency response (CLIO MLS):** ~82–84 dB from 200 Hz–1 kHz; slight dip ~700 Hz; rising above 1 kHz; severe cone breakup peak at 4–5 kHz (~90–92 dB on-axis); steep rolloff above 5 kHz. 30° off-axis tracks on-axis to ~3 kHz then diverges. LR24 LP attenuates the breakup by ~24 dB at 4 kHz, well above the crossover region — adequate. Breakup is severe enough that the DSP limiter is worth setting conservatively.
- **Why liked:** Perfect sensitivity match to TB sub (85 dB) — zero DSP correction. 10+ stock. €22.45 is cheapest standalone mid candidate. Round frame. Metallic bronze cone is visually distinctive — counterpoint to dark paper DS115-8.
- **Concern:** 25W RMS lowest power rating of active mid candidates. Xmax 3.2 mm lower than DS115-8 (4.1 mm). Vas 2.86 L (CLIO) is much smaller than 4.53 L on SI page — use CLIO figure for enclosure modelling. A sealed cavity of ~0.5 L is sufficient.
- **Visual note:** "Bronze/aluminum alloy" cone — bright metallic copper-gold appearance, visually distinctive from paper mids. Owner has reviewed and accepts.
- **DSP adjustment needed:** 0 dB — perfectly matched to sub reference.

### Dayton Audio RS100-8 — Candidate (low stock)
- Role: **MID** | Size: 4" | Frame OD: 98 mm round | Impedance: 8Ω
- Cone: Black anodised aluminium | Sensitivity: 84.6 dB | Power: 30 W RMS / 60 W max | Xmax: ±3.5 mm | Fs: 92 Hz
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/dayton-audio-rs100-8.html) (specs fetched June 2026)
- SoundImports price: €48.95 | Stock (June 2026): **1 unit only**
- **What's good:** Better power handling than DSA90-8 (30 W RMS vs 20 W); more Xmax (3.5 mm vs 2.5 mm). Black cone passes visual rule.
- **Concern:** Fs of 92 Hz with a 150 Hz crossover is only 1.63× margin — tighter than DSA90-8 at 150 Hz. Only 1 unit in stock — not reliable for a build where a replacement might be needed. Price at €48.95 is high relative to performance gain over DSA90-8.

### SB Acoustics SB12PACR25-4 — Candidate (aluminium cone, UK stock)
- Role: **MID** | Size: 4" | Frame OD: 122 mm | Impedance: 4Ω | Plastic chassis
- Cone: Anodised aluminium (dark) | Surround: Low damping rubber
- Sensitivity: 87 dB @ 2.83V/1m | Power: 30W RMS | Fs: 52.5 Hz | Xmax: 5.0 mm | Sd: 50 cm²
- Qts: 0.31 | Qes: 0.33 | Qms: 5.0 | BL: 4.35 Tm | Mms: 6.1 g | Re: 3.1Ω | Le: 0.25 mH | Vas: 5.3 L
- **Source:** [SB Acoustics product page](https://sbacoustics.com/product/4-sb12pacr25-4/) | [Willy's HiFi UK](https://willys-hifi.com/products/sb-acoustics-sb12pacr25-4-midwoofer) (fetched June 2026)
- SoundImports: OOS | **Willy's HiFi UK: £23.76, in stock** (no import concerns — UK supplier)
- **DSP correction vs TB sub (85 dB ref):** −2.0 dB — near-perfect match.
- **Power check:** At reference (98 dB): 25.2W ✓ (within 30W, 84% of rating). At woofer max (101 dB): 50.2W ✗ — over rating. Practical fix: DSP sub limiter at ~40W caps system at 98 dB; mid then needs 25.2W — fine.
- **Fs check:** 52.5 Hz → **2.86× at 150 Hz** — best Fs margin of any available mid candidate.
- **Xmax:** 5.0 mm — joint best with SB12PACR25-4-COAX woofer, better than DS115-8 (4.1 mm).
- **Beaming:** Sd 50 cm² → effective cone dia ~80 mm → beaming starts ~2,730 Hz. Beaming limit above the typical 4" mid crossover range.
- **Character:** Aluminium cone — detailed and analytical, similar to DSA90-8. Less warm than DS115-8 paper cone.
- **Note:** Same driver family as SB12PACR25-4-COAX (without tweeter). BL and Qts differ slightly from coaxial version due to separate build batches.

### SB Acoustics SB12NRX25-4 — Candidate (new — paper NRX cone)
- Role: **MID** | Size: 4" | Frame OD: ~122 mm | Impedance: 4Ω | Cast aluminium vented chassis
- Cone: Proprietary composition paper | Surround: High-damping butyl rubber
- Sensitivity: 87.5 dB @ 2.83V/1m | Power: 30W RMS | Fs: 55 Hz | Xmax: 5.0 mm | Sd: 50 cm²
- Qts: 0.40 | Re: 3.1Ω (est)
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/sb-acoustics-sb12nrx25-4.html) (fetched June 2026)
- SoundImports price: **€59.95** | Stock (June 2026): 8 units
- **DSP correction vs TB sub (85 dB ref):** −2.5 dB — near-perfect match.
- **Fs check:** 55 Hz → **2.72× at 150 Hz** — same class as DS115-8, best of any 4" mid.
- **Xmax:** 5.0 mm — matches SB12PFCR25-4; better than DS115-8 (4.1 mm).
- **Beaming:** Sd 50 cm² → beaming starts ~2,730 Hz. Beaming limit above the typical 4" mid crossover range.
- **Character:** Paper NRX cone — warm, natural. CCAW voice coil for low moving mass. Vented pole piece reduces compression. Paper cone = same warm tonality class as SB12PFCR25-4.
- **vs SB12PFCR25-4:** Same Fs, Xmax, Sd, sensitivity, power, and cone character. Key difference: NRX25-4 costs €59.95 vs PFCR25-4 at €25.95. The NRX chassis (cast aluminium, vented) is higher grade. No acoustic advantage over PFCR at this crossover. Choose PFCR25-4 on value; NRX25-4 only if PFCR25-4 sells out.
- **Concern:** At €59.95 it is over twice the price of the functionally equivalent PFCR25-4.

### SB Acoustics SB12PFCR25-4 — Candidate (paper fiber cone)
- Role: **MID** | Size: 4" | Frame OD: ~122 mm (same family as PACR — confirm before ordering) | Impedance: 4Ω | Plastic chassis
- Cone: Natural fiber paper (proprietary SB Acoustics in-house material) | Surround: Butyl rubber
- Sensitivity: 87.5 dB @ 2.83V/1m | Power: 30W RMS | Fs: 58 Hz | Xmax: 4.9 mm | Sd: 50 cm²
- Qts: 0.43 | Qes: 0.49 | Qms: 3.4 | BL: 3.5 Tm | Mms: 5.3 g | Re: 3.1Ω | Le: 0.26 mH | Vas: 5.2 L
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/sb-acoustics-sb12pfcr25-4.html) | [SB Acoustics](https://sbacoustics.com/product/4-sb12pfcr25-4/) (fetched June 2026)
- SoundImports price: **€25.95** | Stock (June 2026): 10+
- **DSP correction vs TB sub (85 dB ref):** −2.5 dB — near-perfect match.
- **Power check:** At reference (98 dB): 22.4W ✓ (within 30W). At woofer max (101 dB): 44.7W ✗. Same practical fix: DSP sub limiter ~40W keeps mid within 30W.
- **Fs check:** 58 Hz → **2.59× at 150 Hz** — excellent, better than DSA90-8 (2.25×) and SIG120-4 (2.01×).
- **Xmax:** 4.9 mm — effectively equal to SB12PACR25-4 and better than DS115-8.
- **Beaming:** Sd 50 cm², effective diameter 80 mm (r = 40 mm) → beaming onset ~2,730 Hz (verified loudspeakerdatabase). On-axis it stays flat well above this; the 60° response slopes off in the 3–5 kHz region (rigid-piston estimate ~−4/−8/−14 dB at 3/4/5 kHz, likely less in reality as the cone decouples).
- **Pairing with high-Fs wide-dispersion tweeters:** A [DIY build (FB DIY Loudspeaker group, June 2026)](https://www.facebook.com/groups/DIYLoudspeakerProjecPad/posts/1871934119829083/) runs **SB12PFCR25-4 + ND13FA-4 first-order at 5 kHz, no L-pad, "works brilliantly"** — an on-axis result. Crossing the 4" up to 5 kHz is fine on-axis; only a strict 60°-flat-power target is affected (the mid is beaming there). A genuinely strong, cheaper, more sensitive mid than DS115-8 (87.5 vs 85.3 dB, Xmax 4.9 vs 4.1).
- **Character:** Natural fiber paper cone — warm, natural tonality. Better match to GHM-inspired tonal goal than the aluminium PACR version. Reviewers describe "deep midbass and warm sound character."
- **Price note:** At €25.95 this is the cheapest standalone mid candidate with competitive specs — cheaper than B4N (€22.45 but lower Xmax and power), TCP115-8 (€14.01 but needs 29V PSU), DS115-8 (€36.95). Excellent value.

### SB Acoustics SB12PACR25-4-COAX — Candidate (coaxial — mid + tweeter in one unit)
- Role: **MID** | **This is the coaxial version** — integrated 12.4mm dome tweeter in the woofer cone centre. Separate terminals; each driven by its own JAB5 channel.
- Size: 4" | Frame OD: 122 mm | Impedance: 4Ω (both sections) | Depth: 69 mm | Cutout: 102 mm
- **Woofer:** Anodised aluminium cone | 87.5 dB @ 2.83V/1m | 30W RMS | Fs: 55 Hz | Xmax: 5 mm | Sd: 45 cm²
  - Qts: 0.35 | Qes: 0.38 | Qms: 4.84 | BL: 4.0 Tm | Mms: 5.6 g | Re: 3.1Ω | Le: 0.25 mH
- **Tweeter:** 12.4 mm compact dome | 87.5 dB @ 2.83V/1m | **10W RMS** | Fs: 1,300 Hz | Re: 3.0Ω
- **Chassis:** Vented reinforced plastic (not cast aluminium)
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/sb-acoustics-sb12pacr25-4-coax.html) | [SB Acoustics](https://sbacoustics.com/product/4-sb12pacr25-4-coax/) (fetched June 2026)
- **Datasheet:** [research/sb_acoustics_sb12pacr25-4-coax.pdf](research/sb_acoustics_sb12pacr25-4-coax.pdf) | [original URL](https://doc.soundimports.nl/pdf/brands/SB%20Acoustics/SB12PACR25-4-COAX/SB12PACR25-4-COAX-data.pdf) (downloaded June 2026)
- SoundImports price: **€68.45** | Stock (June 2026): 8 units
- **DSP correction vs TB sub (85 dB ref):** −2.5 dB on both woofer and mid channels — perfectly matched to each other; slight pad vs sub.
- **Woofer power check:** At reference (98 dB): 22.4W ✓ (within 30W). At woofer max (101 dB): 44.8W ✗ (over 30W — marginal).
- **Tweeter power check — key limitation:** At reference (98 dB): needs 22.4W vs **10W rated** — tweeter is overdriven at reference level. Max tweeter SPL before distress: ~94 dB @1m → ~89 dB at 6ft listener position. The sub's 80W burst capability cannot be used with this tweeter — system SPL is limited to ~94 dB @1m.
- **Is 94 dB enough?** For kitchen counter listening at 6ft, 89 dB at ear is comfortably loud. The sub's power is simply limited by DSP to match the tweeter ceiling. Usable if the build is not intended to play very loud.
- **The compelling case — coaxial alignment:** Woofer and tweeter share the same acoustic centre — zero time offset at the crossover. No centre-spacing calculation. No vertical integration lobing. Front baffle is cleaner. Uses the JAB5's fourth channel for the tweeter. This is the only way to achieve true point-source mid+tweeter in this build.
- **Concerns:** Tweeter dome colour unconfirmed. Depth 69mm is deepest of any candidate — check internal clearance. At €68.45 it is more expensive than any individual driver but covers both mid and tweeter slots. Tweeter at 12.4mm is very small — HF power handling and extension above 15 kHz may be limited.
- **Crossover:** Tweeter Fs 1000 Hz → minimum crossover ≥2000 Hz; typical crossovers are comfortable (2× margin).

### Dayton Audio PA130-8 — Candidate
- Role: **MID** | Size: 5" | Frame OD: 132 mm | Impedance: 8Ω
- Cone: Paper | Sensitivity: 88.2 dB | Power: 50W RMS / 100W max | Xmax: 2 mm | Fs: 83.4 Hz
- Qts: 0.51 | Vas: 3.95 L
- Supplier: [SoundImports](https://www.soundimports.eu/en/dayton-audio-pa130-8.html) | Price: €33.45 | Stock: 10+
- **DSP correction vs TB sub (85 dB ref):** −3.2 dB.
- **Power check:** At reference (98 dB): 9.6W. At woofer max (101 dB): 19.1W. Both well within 50W. ✓
- **Concern — Fs:** 83.4 Hz → 1.8× at 150 Hz crossover. Tightest margin of any mid candidate. Raises crossover to 175 Hz gives 2.1×; 200 Hz gives 2.4×.
- **Concern — Xmax:** 2 mm. At 150 Hz with 5" cone, excursion headroom is limited at high SPL near the crossover.
- **Concern — frame OD:** 132 mm — widest mid candidate. On 190 mm baffle leaves ~29 mm each side. Tight but mounts. Sub on side (Option A) only — sub and mid both on front would not fit.
- **Reinstated June 2026:** Previously excluded on OD/Xmax/Fs rules. None of those are power or visual fails. Paper cone passes visual.

### SB Acoustics SB13PFCR25-4 — Candidate
- Role: **MID** | Size: 5" | Frame OD: circular plastic chassis (large) | Impedance: 4Ω
- Cone: Natural fibre (paper blend) | Sensitivity: 89 dB | Power: 40W RMS | Xmax: 4.5 mm | Fs: 44 Hz
- Qts: 0.29 | Vas: 13.4 L | Sd: 87 cm²
- Supplier: [SoundImports](https://www.soundimports.eu/en/sb13pfcr25-4-woofer.html) | Price: €28.45 | Stock: 10+
- **Power check:** At reference (98 dB, 4Ω): 15.9W. At woofer max (101 dB): 31.7W. Both within 40W. ✓
- **Concern — Qts:** 0.29 is very low — designed for large vented enclosures (Vas 13.4 L). As an active mid with DSP HP at 150 Hz it doesn't need a tuned enclosure (any sealed rear chamber works), but the driver's transient behaviour will be very damped. Fs 44 Hz → 3.4× at 150 Hz — outstanding Fs margin.
- **Concern — frame OD:** 5" nominal, frame likely 130+ mm — similar to PA130-8. Tight on 190 mm baffle.
- **Reinstated June 2026:** Previously excluded on size/Qts rules. Power passes, no visual issue.

### Peerless by Tymphany SLS-85S25CP04-04 — Candidate (reinstated June 2026)
- Role: **MID** | Size: 3.5" | Frame: 105 × 91 mm oval-rectangular | Impedance: 4Ω
- Cone: Treated paper | Sensitivity: 86 dB | Power: 30W RMS | Xmax: **10.2 mm** | Fs: 73 Hz
- Qts: 0.36 | Vas: 1.43 L
- Supplier: [SoundImports](https://www.soundimports.eu/en/peerless-by-tymphany-sls-85s25cp04-04.html) | Price: €29.95 | Stock: 10+
- **Why interesting:** Xmax 10.2 mm is equal to SDS-P830656 — outstanding mechanical headroom. Paper cone, warm character. Fs 73 Hz → 2.05× at 150 Hz crossover (adequate). 4Ω: at 29V delivers 90W vs 31.7W needed at 98 dB ✓. Frame 105×91mm — if the 91mm axis is vertical, centre spacing with compact tweeters (DT-28N ~72mm OD) is ~82mm.
- **DSP correction:** −1 dB vs sub (86 dB vs 85 dB ref).
- **Power at reference:** 4Ω, 86 dB → 2×10^((98−86)/10) = 31.7W (within 30W RMS — marginal; DSP limit at 30W; at burst 63.4W vs 30W — cap sub via DSP limiter). 29V required.

### Peerless by Tymphany SDS-P830656 — Candidate (reconsidering)
- Role: **MID** | Size: 5.25" | Frame: **152 × 134 mm** truncated cast frame | Impedance: 8Ω
- Cone: Coated paper | Sensitivity: 86.1 dB @ 2.83V/1m | Power: 60W RMS | Xmax: 10 mm | Fs: 65 Hz
- Re: 5.9Ω | Qts: 0.62 | Qes: 0.76 | Qms: 3.47 | Vas: 6.58 L | Sd: 86.6 cm² | BL: 5.53 Tm | Mms: 9.67 g
- Baffle cutout: 118 mm | Bolt circle: 141.8 mm | Depth: 66 mm | Frequency response: 50–5,000 Hz
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/peerless-by-tymphany-sds-p830656.html) (specs fetched June 2026)
- **Datasheet:** [research/peerless_sds-p830656.pdf](research/peerless_sds-p830656.pdf) | [original URL](https://doc.soundimports.nl/pdf/brands/Peerless%20by%20Tymphany/SDS-P830656/SDS-P830656.pdf) (downloaded June 2026)
- SoundImports price: €29.95 | Stock: 10+
- **The case for it:** Truncated on two sides — if oriented with short dimension (134 mm) vertical, tweeter centre sits only ~96 mm above mid centre (vs ~104 mm for DS115-8 + SB19ST). Flat top edge lets a square TN25 faceplate butt right up against it with minimal gap. Sensitivity 86.1 dB ≈ only −1.1 dB correction needed. Fs 65 Hz → 2.3× at 150 Hz crossover. Xmax 10 mm is outstanding. 60W RMS — no power concern.
- **Concerns:** Frame is 152 mm wide. In Option C (190 mm wide cabinet), leaves only 19 mm each side — very tight for mounting hardware. Depth 66 mm is the deepest mid candidate — check internal clearance. Sd 86.6 cm² is large for a mid; beaming above ~2,000 Hz is a real risk at 60° off-axis. Coated paper cone colour to confirm from datasheet.
- **DSP correction vs TB sub (85 dB ref):** −1.1 dB (essentially zero).

### Celestion TF0510 — Candidate (weak specs — see concerns)
- Role: **MID** | Size: 5" | Frame: 136 × 151 mm (pressed steel — approximately round; mounting PCD 140 mm, 4 slots) | Impedance: 8Ω
- Cone: Kevlar-loaded paper | Surround: Cloth-sealed | Sensitivity: 91 dB @ 1W/1m | Power: 30W RMS (AES)
- Fs: **106 Hz** | Xmax: **1.1 mm** | Qts: 0.46 | Qms: 2.40 | Qes: 0.58
- Re: 6.43Ω | Le: 0.38 mH | Mms: 5.7 g | Cms: 0.40 mm/N | BL: 6.5 Tm | Vas: 4.2 L
- D (effective): 100 mm → Sd ≈ 78.5 cm² | Cutout: 117 mm | Depth: 68 mm
- Frequency range: 130–8,000 Hz | Magnet: Ferrite | VC: 1" copper on polyimide former
- Supplier: [Thomann UK](https://www.thomann.co.uk/celestion_tf0510.htm) | Price: **£30** | Stock: in stock
- **Datasheet:** [research/celestion_tf0510.pdf](research/celestion_tf0510.pdf) | [original URL](https://fast-images.static-thomann.de/pics/atg/atgdata/document/specs/315585.pdf) (downloaded June 2026)
- **Power check:** At reference (98 dB, 8Ω): 5.0W. At woofer max (101 dB): 10.0W. Both well within 30W. ✓
- **Concern — Fs:** 106 Hz → **1.42× at 150 Hz**. Worst Fs margin of any mid candidate. Operating close to resonance — elevated distortion, higher excursion at the crossover point. Even at 200 Hz crossover: 1.89×. Mitigated slightly by active DSP HP filter which provides mechanical protection.
- **Concern — Xmax:** 1.1 mm — lowest of any mid candidate. At 150 Hz, excursion demand near the crossover limits clean output headroom before mechanical clipping.
- **What's interesting:** Kevlar-loaded paper cone (warm but detailed character), Celestion UK heritage, £30 at Thomann UK (cheapest available mid), Celestion specifies it as "MF in 3-way". Would be a strong candidate if Fs were 60–70 Hz and Xmax were 3+ mm.
### Scan-Speak Discovery D7608/920010 — Rejected (Qts too high, Xmax too low, price)
- Role: **MID** | Size: 3" mid-dome | Frame OD: circular | Impedance: 8Ω
- Diaphragm: not specified | Sensitivity: 92 dB | Power: 80W RMS | Xmax: 0.4 mm | Fs: 300 Hz
- Qts: 1.73 | Vas: 0.01 ft³
- Supplier: [SoundImports](https://www.soundimports.eu/en/scan-speak-d7608-920010.html) | Price: €106.95 | Stock: 6
- **Reason for rejection:** Xmax of only 0.4 mm is far below the 2.5 mm minimum. Qts of 1.73 is extremely high, indicating it requires a specific resonant chamber. Requires "vented / open rearside" — complex mounting. Price at €106.95 is also over the combined budget for this driver alone.

### HiVi Swan DM-7500 — Candidate (over stated budget)
- Role: **MID** | Size: 3" mid-dome | Impedance: 5Ω | Sensitivity: 94 dB | Power: 20W RMS / 120W max | Fs: 300 Hz
- Supplier: [SoundImports](https://www.soundimports.eu/en/hivi-dm-7500.html) | Price: €79.95 | Stock: 10+
- **Power check (5Ω, 94 dB):** At reference (98 dB): 4.0W. At woofer max (101 dB): 8.0W. Both well within 20W. ✓ DSP correction: −9 dB.
- **Fs note:** 300 Hz — this is a mid-dome, not a cone mid. The 150 Hz crossover is 0.5× its Fs — far below resonance. **Would need crossover at 600 Hz minimum (2× Fs).** That means the sub would handle 40–600 Hz, and this covers 600 Hz–20 kHz with no separate tweeter. A 2.5-way or 2-way active rather than true 3-way.
- **Impedance:** 5Ω — JAB5 handles it safely; power at 24V into 5Ω ≈ 49W. Fine.
- **Price:** €79.95 — exceeds the £75 combined mid+tweeter budget unless budget is extended.

### Dayton Audio RS52FN-8 — Rejected (Xmax, Fs, size)
- Role: **MID** | Size: 2" midrange dome | Frame OD: 130 mm (5.12") | Impedance: 8Ω
- Diaphragm: damped fabric | Sensitivity: 90 dB | Power: 60W RMS / 120W max | Xmax: 1 mm | Fs: 394 Hz
- Qts: 1.05 | Sd: 26.4 cm²
- Supplier: [SoundImports](https://www.soundimports.eu/en/dayton-audio-rs52fn-8.html) | Price: €62.95 | Stock: 9
- **Reason for rejection:** Xmax of only 1 mm is far below the 2.5 mm minimum. Fs at 394 Hz with typical 150 Hz crossover would be only 0.38× Fs ratio — would be severely overdriven at the crossover point. This is a dedicated upper-midrange dome, not a woofer-style mid.

### Tectonic TEBM65C20F-8 BMR — Candidate (noted; low sensitivity)
- Role: **MID** | Size: 3.5" | Frame OD: 108 mm round | Impedance: 8Ω
- Diaphragm: Paper (Balanced Mode Radiator — distributed excitation, not piston) | Surround: Foam
- Sensitivity: **81 dB @ 2.83V/1m** | Power: 30W RMS / 60W max | Xmax: 3.5 mm | Fs: 86 Hz
- Qts: 0.89 | Depth: 56.8 mm | Frequency response: 80–20,000 Hz
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/tectonic-elements-tebm65c20f-8.html) (fetched June 2026)
- SoundImports price: **€49.95** | Stock (June 2026): 10+
- **What makes it different:** A BMR driver is not a conventional piston. Excitation is distributed across the cone via bending waves at higher frequencies — this gives the driver unusually wide, near-omnidirectional dispersion above a certain frequency. Off-axis response at 60–90° is far superior to any conventional dome or cone mid. This is directly relevant to the kitchen 60° geometry. Tectonic states "dispersion up to 100 degrees."
- **DSP correction vs TB sub (85 dB ref):** +4.0 dB boost needed — this is a significant DSP demand in the mid channel.
- **Fs check:** 86 Hz → **1.74× at 150 Hz crossover** — below the 2× target. Tighter than any recommended mid candidate. Would benefit from crossover raised to 175–200 Hz.
- **Xmax:** 3.5 mm — adequate. Same class as TCP115-8.
- **The engineering case:** BMR technology used in premium soundbars (Bang & Olufsen, Tectonic OEM) specifically for its wide dispersion. In a kitchen counter speaker, this could outperform a conventional mid + ring radiator for off-axis stability. The 4 dB sensitivity deficit is a manageable DSP trade-off.
- **Concern — sensitivity:** 81 dB requires a +4 dB boost in DSP. The amp must deliver 2.5× more power to this driver than to an 85 dB mid, all else equal. At 24V into 8Ω: ~31W available. At reference (98 dB): needs 50W — **exceeds available power at 24V**. At 29V: 45W available, still 11% short. **Needs 32V or higher to reach reference level without limiting.** This is the main blocker.
- **Status:** Keep as a curiosity for a high-voltage variant build (36V JAB5 with appropriate limiters). Not suitable at 24V or 29V for reference-level matching.

### Markaudio PLUVIA-7HD (Gold) — Candidate (power-limited, zero-correction curiosity)
- Role: **MID** | Size: 4" | Frame OD: **122.3 mm** round | Impedance: 8Ω | Cone: Mg/Al alloy | Full-range design
- Sensitivity: **85.74 dB @ 2.83V/1m** | Power: **20W RMS** | Xmax: 4 mm | Fs: 72.5 Hz
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/markaudio-pluvia-7hd-gold.html) | Price: **€52.45** | Stock (June 2026): 10+
- **Fs check:** 72.5 Hz → **2.07× at 150 Hz crossover** — passes 2× minimum by margin.
- **DSP correction vs TB sub (85 dB ref):** −0.74 dB — essentially **zero correction**. Closest sensitivity match to sub of any mid candidate.
- **Power at reference (98 dB):** 10^((98−85.74)/10) = **16.8W** (84% of 20W — close to limit). At burst (101 dB): **33.5W** — 67% over rating; driver destroyed at uncapped burst.
- **Amp ceiling:** At 24V into 8Ω JAB5 delivers ~30.6W. Even the amp's maximum output exceeds the driver's 20W RMS rating — no safe operating point without a DSP limiter.
- **The interesting case:** 85.74 dB is the uniquely closest sensitivity match to the 85 dB sub of any candidate — zero DSP gain/cut, maximum dynamic range, no inter-channel mismatch.
- **Practical fix — DSP limiter at 18W:** Max mid SPL = **97.3 dB @1m**. Match sub at 37W → 97 dB. Gives a 97 dB system cap vs 98 dB reference. Acceptable for kitchen counter use at 6ft.
- **vs DS115-8:** DS115-8 has near-identical sensitivity (85.3 dB), higher power (35W), better Fs margin (2.72× vs 2.07×), and costs €16 less (€36.95 vs €52.45). PLUVIA wins only on 0.44 dB closer sensitivity match and Mg/Al cone character.

---

### Dayton Audio SIG150-4 — Candidate
- Role: **MID** | Size: 5.25" | Frame OD: **152 mm** round | Impedance: 4Ω | Open cast aluminium frame
- Cone: Anodised aluminium
- Sensitivity: 91.1 dB @ 2.83V/1m (loudspeakerdatabase: 87.4 dB @1W/1m → 90.4 dB @2.83V — minor discrepancy; SoundImports used)
- Power: 60W RMS / 120W peak | Frequency response: 60–4,000 Hz
- Fs: 61.5 Hz | Xmax: 4 mm | Sd: 96 cm² | Vas: 8.7 L | Qts: 0.49 | Qes: 0.53 | Qms: 5.78
- BL: 5.2 Tm | Re: 3.7Ω | Le: 0.35 mH | Mms: 10.2 g | VC: 26.7 mm
- Depth: 67 mm | Cutout: 120 mm | 6 mounting holes
- **Source:** [Dayton Audio product page](https://daytonaudio.com/product/1915/sig150-4-5-25-signature-series-woofer-60w-driver-4-ohm) | [SoundImports](https://www.soundimports.eu/en/dayton-audio-sig150-4.html) | T/S: [loudspeakerdatabase.com](https://loudspeakerdatabase.com/Dayton/SIG150-4) (fetched June 2026)
- SoundImports price: €44.95 (on sale €37.15) | Stock (June 2026): in stock
- **DSP correction vs TB sub (85 dB ref):** −6.1 dB pad needed.
- **Power check:** At reference (98 dB): 9.8W. At woofer max (101 dB): 19.5W. Both within 60W. ✓ 4Ω channel delivers ~61W at 24V — huge headroom.
- **Fs check:** 61.5 Hz → **2.44× at 150 Hz crossover** — excellent. Better than DSA90-8 (2.25×) and SIG120-4 (2.01×). Close to DS115-8 (2.72×).
- **Xmax:** 4 mm — same class as DS115-8 (4.1 mm). Very good.
- **Critical concern — beaming:** Sd 96 cm² → effective cone diameter ~110 mm. Beaming becomes significant at ~f = c/(π×a) ≈ 343/(π×0.055) = **~2,000 Hz**. This driver is already beaming substantially by 2,000 Hz. At 40–50° off-axis, mid output at 2–3 kHz will be audibly attenuated. **Mitigation:** lower the mid/tweeter crossover to ~1,500–2,000 Hz; requires a tweeter with Fs ≤750–1,000 Hz (SB19ST, DX25TG59-04, or RST28F-4 all qualify).
- **Cabinet fit concern:** 152 mm OD on 190 mm wide baffle leaves ~19 mm each side — very tight for mounting hardware. Option A layout (sub on side, SIG150-4 on front baffle alone) gives more room.
- **Depth concern:** 67 mm — verify internal clearance. Same depth issue as SDS-P830656.
- **Mixed review note:** One reported cone breakage under normal listening conditions. Note as durability flag.
- **Note on SIG120-4:** The SIG120-4 (4", 123 mm OD) is a **separate, smaller driver and remains OOS** (confirmed June 2026). The SIG150-4 is not the same driver.

### Dayton Audio SIG120-4 — Top candidate — OUT OF STOCK
- Role: **MID** | Size: 4" | Frame OD: 123 mm (4.84") round | Impedance: 4Ω | Baffle cutout: 95 mm (3.74") | Depth: 59 mm
- Cone: Black (single-piece black dish, confirmed) | Cone area Sd: 56.4 cm²
- Sensitivity: **89.7 dB @ 2.83V/1m** | Fs: 74.6 Hz | Xmax: 4 mm | Qts: 0.43 | Qms: 4.84 | Qes: 0.47
- Vas: 0.109 ft³ (3.09 L) | Re: 3.7Ω | Le: 0.22 mH | Mms: 6.7 g | Cms: 0.68 mm/N | BL: 5 Tm
- Power: 40W RMS / 80W max | Frequency range: 75–8,500 Hz
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/dayton-audio-sig120-4.html) (specs fetched June 2026)
- SoundImports price: €34.95 | Stock at SoundImports (June 2026): **OUT OF STOCK**
- **Audiophonics (France): €34.90 — IN STOCK ("last items") — order urgently** | Ships to UK via Colissimo/UPS/DPD | UK import VAT (20%) likely added at checkout
- **Note:** 123 mm OD on 190 mm baffle leaves 33.5 mm margin each side — adequate clearance for surface mounting.
- **Visual note:** Continuous round frame with a single-piece black dish. Black finish confirmed.
- **Impedance note:** 4Ω — JAB5 mid channel into 4Ω delivers ~42W at 24V supply, which comfortably exceeds any sensitivity-matching requirement.
- **Acoustic assessment:** Fs 74.6 Hz is higher than DSA90-8 (66.6 Hz) and TCP115-8 (59.2 Hz). A 150 Hz crossover places it only 2.01× above Fs — adequate but not as generous as TCP115-8 (2.53×). Sensitivity at 89.7 dB is 4.7 dB above the 85 dB sub reference — needs −4.7 dB DSP attenuation. Xmax 4 mm is good.
- **DSP correction vs TB sub (85 dB ref):** −4.7 dB attenuation needed.

### Scan-Speak Discovery 12W/4524G00 ★★ — Candidate (compact 4.5" Discovery, Fs=50Hz; lautsprechershop.de)
- Role: **MID** | Size: 4.5" | Frame OD: **~124.7 mm** (inferred from 8Ω sibling 12W/8524G00 datasheet — same physical platform; LSS page listed 100 mm which is the cutout, not OD) | Cutout: **~100 mm** | Impedance: 4Ω | Cone: NRSC Fibre Glass (Discovery grade) | Depth: ~53 mm
- Sensitivity: **88.8 dB @ 2.83V/1m** ⚠ not confirmed — LSS page only; 8Ω sibling is 86 dB @2.83V | Power: **40W RMS / 70W max** ⚠ not confirmed for 4Ω | Xmax: **±3 mm** | Fs: **50 Hz**
- ⚠ Sensitivity and power for the 4Ω version not confirmed from datasheet — the 8Ω sibling (12W/8524G00) is fully verified: 86 dB @2.83V / 40W IEC / Sd 59 cm² / Fs 52 Hz / Qts 0.32 / Vas 8.2 L (see note below)
- **Note on 8Ω sibling (12W/8524G00):** Fully verified June 2026 from Scan-Speak datasheet. OD 124.7 mm, cutout 100 mm, depth 53.4 mm, Sd 59 cm², Fs 52 Hz, Qts 0.32, Vas 8.2 L, 40W IEC / 70W max, 86 dB @2.83V. Mechanical specs expected identical to 4Ω version; only impedance and sensitivity differ. **8Ω version Max SPL: 86 + 10·log₁₀(40) = 102.0 dB ✓.** Datasheet: [research/scan_speak_12w-8524g00.pdf](research/scan_speak_12w-8524g00.pdf)
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS woofer index, June 2026) | LSS price: **€59.40 inc VAT / €49.92 exc VAT** | Stock (Jun 2026): in stock at LSS
- **Fs margin at 150 Hz crossover:** 150/50 = **3.0×** — excellent; best Fs margin of any 4Ω 4.5" candidate.
- **DSP correction vs TB sub (85 dB ref):** −3.8 dB attenuation (4Ω: 1W sens = 88.8 − 3.01 = 85.79 dB).
- **Power at reference (4Ω, 98 dB):** 10^((98−85.79)/10) = **16.6W** (41.5% of 40W ✓). At burst (101 dB): **33.2W** (83% of 40W — near limit; 47% of 70W max ✓). Set DSP sub limiter at 40W to protect driver.
- **Beaming (inferred from 8Ω sibling Sd=59 cm²):** r_eff = √(0.0059/π) = 43.3 mm → f_beam = 344/(π×0.0433) = **2,527 Hz** ✓ (Sd=59 > 55 cm² proxy; f_beam passes operative ≥2,500 Hz gate). 0.8× ceiling = **2,022 Hz**. Window with SB19ST (Fs=980 Hz): 1,960–2,022 Hz (62 Hz, 0.04 oct, marginal — tightest of all candidates).
- **Sealed box (8Ω sibling, Vas=8.2 L, Fs=52 Hz, Qts=0.32):** At 1.2 L: Fc = 52×2.799 = **145.5 Hz** ✓; Qtc = 0.32×2.799 = **0.896** ✓ (barely). At 1.5 L: Fc = **132 Hz** ✓, Qtc = **0.81** ✓. Large Vas means Qtc is near 0.9 in minimum box; use 1.5 L for comfort. Note: Scan-Speak lists "Cabinet volume — closed box: N.a." (no recommended volume given, not impossible).
- **Centre spacing (FP OD ~124.7 mm):** D3004/602010 (62mm) → **93mm** | Audaphon TWS 30/4 (104mm) → **114mm** | RS28A-4 (103mm) → **114mm** | SB19ST (88mm) → **106mm**
- **Why this stands out:** Fs=50Hz delivers 3.0× margin at 150 Hz — outstanding. 8Ω sibling confirmed at 102.0 dB max SPL; 4Ω version expected higher. Scan-Speak Discovery construction quality at €59.40.
- **Concern:** Xmax=3mm is lower than DS115-8 (4.1mm) and SB12PFCR25-4 (4.9mm). Large Vas (8.2 L) demands a larger box for well-damped alignment. Crossover window is the tightest of all candidates (62 Hz only). Sensitivity of 4Ω version unverified — fetch 12W/4524G00 datasheet before ordering.

### Scan-Speak Discovery 15W/4434G00 ★★ — Candidate (5.25" Discovery, exceptional Fs+Xmax; lautsprechershop.de)
- Role: **MID** | Size: 5.25" | Frame OD: **114 mm** round | Impedance: 4Ω | Cone: Paper (Discovery grade) | Baffle cutout: ~95 mm (est)
- Sensitivity: **89.7 dB @ 2.83V/1m** | Power: **60W RMS / 120W max** | Xmax: **±4.3 mm** | Fs: **43 Hz**
- ⚠ Full T/S not confirmed from LSS page — fetch Scan-Speak Discovery 15W/4434G00 datasheet
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS woofer index, June 2026) | LSS price: **€68.40 inc VAT / €57.48 exc VAT** | Stock (Jun 2026): in stock at LSS
- **Fs margin at 150 Hz crossover:** 150/43 = **3.49×** — outstanding; best of any mid candidate evaluated in this project.
- **DSP correction vs TB sub (85 dB ref):** −4.7 dB attenuation (4Ω: 1W sens = 89.7 − 3.01 = 86.69 dB).
- **Power at reference (4Ω, 98 dB):** 10^((98−86.69)/10) = **13.5W** (22.5% of 60W ✓). At burst (101 dB): **27.0W** (45% of 60W ✓; 22.5% of 120W ✓). Substantial thermal headroom.
- **Beaming:** ? (unconfirmed — Sd not yet confirmed; fetch datasheet for accurate beaming calculation). Upper crossover ceiling unknown until Sd confirmed.
- **Centre spacing (FP OD 114 mm):** D3004/602010 (62mm) → **88mm** | Audaphon TWS 30/4 (104mm) → **109mm** | RS28A-4 (103mm) → **109mm** | XT25TG30-04 (104mm) → **109mm** | H1189-06 (103.8mm) → **109mm**
- **Why this stands out:** Fs=43Hz is the lowest of any mid candidate in this project. 3.49× margin at 150 Hz crossover is essentially risk-free at the sub/mid boundary. Xmax=4.3mm is the best of any Scan-Speak Discovery mid, matching the best SB Acoustics candidates. 60W RMS provides comfortable headroom. At €68.40 it undercuts WF118WA07 (€95.70) significantly. 4Ω → 61W at 24V.
- **Concern:** 5.25" cone — beaming limit unconfirmed until Sd confirmed from datasheet. 114mm FP on 190mm baffle leaves 38mm each side — comfortable for surface mounting.

### Scan-Speak Illuminator 12MU/4731T00 ★★ — Candidate (premium Illuminator dedicated mid; lautsprechershop.de)
- Role: **MID** | Size: 4.5" | Frame OD: **101 mm** round | Impedance: 4Ω | Cone: Scan-Speak Illuminator (dedicated midrange motor) | Baffle cutout: ~82 mm (est)
- Sensitivity: **90 dB @ 2.83V/1m** | Power: **80W RMS / 150W max** | Xmax: **±3.5 mm** | Fs: **64 Hz**
- ⚠ Full T/S not confirmed from LSS page — fetch Scan-Speak Illuminator 12MU/4731T00 datasheet
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS woofer index, June 2026) | LSS price: **€306.00 inc VAT / €257.14 exc VAT** | Stock (Jun 2026): in stock at LSS
- **Fs margin at 150 Hz crossover:** 150/64 = **2.34×** — good; comfortable margin.
- **DSP correction vs TB sub (85 dB ref):** −5.0 dB attenuation (4Ω: 1W sens = 90 − 3.01 = 86.99 dB).
- **Power at reference (4Ω, 98 dB):** 10^((98−86.99)/10) = **12.6W** (15.8% of 80W ✓). At burst (101 dB): **25.2W** (31.5% of 80W ✓; 16.8% of 150W ✓). Power effectively unlimited at project SPL.
- **Beaming:** ? (unconfirmed — Sd not yet confirmed; fetch datasheet). Compact FP is the ideal combination for a mid driver.
- **Centre spacing (FP OD 101 mm):** D3004/602010 (62mm) → **82mm** | Audaphon TWS 30/4 (104mm) → **103mm** | RS28A-4 (103mm) → **102mm** | XT25TG30-04 (104mm) → **103mm** | H1189-06 (103.8mm) → **102mm**
- **Why considered:** The Scan-Speak Illuminator 12MU is a purpose-built midrange unit — the Illuminator motor (FEA-optimised, copper ring, short voice coil in long gap) targets the 300 Hz–5 kHz range specifically. 101mm FP is nearly as compact as 12W/4524G00 (~125mm OD inferred). 90 dB is the highest sensitivity of any new LSS mid. At €306 it is 4–5× the cost of the 12W/4524G00 (€59.40) for a dedicated mid motor vs a woofer-range driver pressed into mid service.
- **Concern:** €306 is significant for a kitchen counter build. Acoustic performance in this application (active DSP, 150 Hz crossover, limited off-axis demands) may not justify the premium over the €59.40 12W/4524G00. Recommended for builds where the best possible midrange fidelity is the primary goal regardless of cost.

### Wavecor WF118WA07 ★★ — Candidate (4.5" Balanced Drive paper cone, Fs=56Hz; lautsprechershop.de)
- Role: **MID** | Size: 4.5" | Frame OD: **118 mm** (truncated — flat-edged, not fully circular) | Impedance: 4Ω | Cutout: **92 mm** | Depth: **61.4 mm** | Neodymium motor
- Cone: **Paper** (Balanced Drive construction) | VC diameter: 26 mm | Surround: rubber
- Sensitivity: **87 dB @ 2.83V/1m** | Power: **50W RMS / 100W program** | Xmax: **±4 mm** | Fs: **56 Hz**
- Qts: 0.36 | Qes: 0.38 | Qms: 7.80 | Re: 3.2Ω | Le: 0.22 mH | BL: 4.5 Tm | Mms: 6.9 g | Vas: 4.9 L | Sd: **54 cm²**
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS woofer index, June 2026) | [Parts Express product page](https://www.parts-express.com/Wavecor-WF118WA07-4-1-2-Balanced-Drive-Paper-Cone-Mid-Woofer-with-Truncated-Frame-4-Ohm-298-1140) | Datasheet: [research/wavecor_wf118wa07_datasheet.pdf](research/wavecor_wf118wa07_datasheet.pdf) / [original (Parts Express)](https://www.parts-express.com/pedocs/specs/298-1140-1142--wavecore-wf118wa07-08-specifications.pdf) | LSS price: **€95.70 inc VAT / €80.42 exc VAT** | Stock (Jun 2026): in stock at LSS
- **Fs margin at 150 Hz crossover:** 150/56 = **2.68×** — excellent; same class as DS115-8 (2.72×).
- **DSP correction vs TB sub (85 dB ref):** −2.0 dB attenuation (1.7 dB more than DS115-8).
- **Power at reference (4Ω, 98 dB):** (2.83²/4) × 10^((98−87)/10) = 2.0 × 12.59 = **25.2W** (50.4% of 50W ✓). At burst (101 dB): **50.2W** ≈ 50W rating. **Set DSP limiter at 48W** → max mid SPL = 87 + 10×log₁₀(24) = **100.8 dB** (0.2 dB below 101 dB burst ceiling — inaudible).
- **Beaming:** Sd 54 cm² → r_eff 41.5 mm → f_beam 2,641 Hz → **0.8× ceiling = 2,113 Hz**. Identical to DS115-8 (Sd 54.1 cm²).
- **Crossover window (R2604/833000, Fs 440 Hz):** 880–2,113 Hz = **1.27 octaves** (comfortable). Ideal crossover √(880 × 2113) = **1,363 Hz**.
- **Frame note:** "Truncated frame" = circular frame with flat-cut edges. OD 118mm is the maximum span; flat sections reduce the width in one axis. Fits a 190mm baffle with ≥36mm clearance each side, same class as DS115-8 (115.6mm).
- **Depth note:** 61.4mm total; internal protrusion = 61.4 − 18 = **43.4mm** (DS115-8: 36.7mm). Both fit the 70mm soil-pipe chamber with clearance.
- **Centre spacing (FP OD 118 mm):** D3004/602010 (62mm) → **90mm** | Audaphon TWS 30/4 (104mm) → **111mm** | RS28A-4 (103mm) → **111mm** | XT25TG30-04 (104mm) → **111mm** | H1189-06 (103.8mm) → **111mm**
- **vs DS115-8 (locked):** Identical Sd (54 cm²) → identical beaming ceiling (2,113 Hz) and crossover window. Identical Fs margin (2.68× vs 2.72×). Same Xmax class (4mm vs 4.1mm). Paper cone character the same. WA07 is 1.7 dB more sensitive → 1.7 dB more DSP attenuation needed → similar power at the driver. Both need a DSP limiter (WA07 at 48W / DS115-8 at 35W) and both reach 100.8 dB vs 101 dB burst — same 0.2 dB shortfall. WA07 is €58.75 more expensive (€95.70 vs €36.95) with no acoustic advantage over the DS115-8.
- **Why considered:** Higher power rating (50W vs 35W). Wavecor Balanced Drive motor for BL linearity. Qts 0.36 (DS115-8: 0.38) — marginally better damping in sealed rear chamber. Paper cone matches DS115-8 character.
- **vs Wavecor WF120BD05 (Fs=48Hz, 60W, €149.60):** WA07 is €54 cheaper. BD05 wins on Fs margin (3.13× vs 2.68×) and 60W burst rating (no limiter needed). Choose WA07 for value; BD05 if burst headroom is required.

### Wavecor WF120BD05 ★★ — Candidate (4.5" BD motor, lowest-Fs Wavecor 11cm; lautsprechershop.de)
- Role: **MID** | Size: 4.5" | Frame OD: **120 mm** round | Impedance: 4Ω | Cone: ? (BD motor variant; datasheet pending) | Baffle cutout: ~99 mm (est) | Premium BD (Balanced Drive) motor
- Sensitivity: **87 dB @ 2.83V/1m** | Power: **60W** | Xmax: **±4 mm** | Fs: **48 Hz**
- ⚠ Full T/S and cone material not confirmed — fetch Wavecor WF120BD05 datasheet before ordering
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS woofer index, June 2026) | LSS price: **€149.60 inc VAT / €125.71 exc VAT** | Stock (Jun 2026): in stock at LSS
- **Fs margin at 150 Hz crossover:** 150/48 = **3.13×** — excellent; between WF118WA07 (2.68×) and 15W/4434G00 (3.49×).
- **DSP correction vs TB sub (85 dB ref):** −2.0 dB — same as WF118WA07.
- **Power at reference (4Ω, 98 dB):** 25.2W (42% of 60W ✓). At burst (101 dB): **50.3W** (83.8% of 60W ✓ — adequate headroom; no DSP limiter required for driver protection at project SPL).
- **Beaming:** ? (unconfirmed — Sd not yet confirmed; fetch datasheet).
- **Centre spacing (FP OD 120 mm):** D3004/602010 (62mm) → **91mm** | Audaphon TWS 30/4 (104mm) → **112mm** | RS28A-4 (103mm) → **112mm** | XT25TG30-04 (104mm) → **112mm**
- **Why considered:** BD (Balanced Drive) motor is Wavecor's premium architecture — improved BL linearity at high excursion. Fs=48Hz (8Hz lower than WF118WA07) gives 3.13× margin at 150 Hz. 60W rating eliminates the burst limiter concern that affects WF118WA07. FP=120mm within 122mm limit with 2mm to spare.
- **vs WF118WA07 (€95.70):** €54 more for 8Hz lower Fs, 10W more power rating (no limiter needed), premium BD motor. Prefer WA07 on value; BD05 if burst margin is a priority.

### Morel EW 428 ★★ — Candidate (4.5" premium motor, best Xmax in 428 family; lautsprechershop.de)
- Role: **MID** | Size: 4.5" | Frame OD: **118.5 mm** | Cutout: **94 mm** | Depth: **56 mm** | Impedance: **8Ω** | Cone: Damped Polymer Composite (DPC) | Surround: rubber
- Sensitivity: **87 dB @ 2.83V/1m** (= 87 dB @ 1W/1m for 8Ω) | Power: **150W (DIN)** | Xmax: **±4.5 mm** | Fs: **62 Hz**
- **T/S (verified from datasheet):** Qts 0.35 | Qes 0.41 | Qms 2.36 | Sd **57 cm²** | Vas **4.7 L** | Mms 6.16 g | Cms 1.046 mm/N | Rms 1.02 kg/s | BL 6.1 N·A | Re 6.3Ω | Le 0.44 mH
- **Source:** Morel EW 428 datasheet (verified June 2026) | [research/morel_ew428.pdf](research/morel_ew428.pdf) | LSS: **€153.00 inc VAT / €128.57 exc VAT** | Stock (Jun 2026): in stock at LSS
- **Gate 1 — Max SPL (8Ω, P_ref=1W):** 87 + 10·log₁₀(150) = **108.8 dB** ✓ — 7.8 dB above 101 dB burst ceiling.
- **Gate 2 — Fs margin:** 150/62 = **2.42×** ✓
- **Gate 3 — Beaming (Sd=57 cm²):** r_eff = √(0.0057/π) = 42.6 mm → f_beam = 344/(π×0.0426) = **2,570 Hz** ✓. Sd=57 cm² exceeds the ≤55 cm² proxy threshold by 2 cm² but beaming onset is above 2,500 Hz — operative gate passes. 0.8× ceiling = **2,056 Hz** (crossover window with SB19ST: 1,960–2,056 Hz, 96 Hz / 0.07 oct, marginal).
- **Gate 4 — Physical:** OD 118.5 mm ✓ (≤130 mm) | Depth 56 mm ✓ (≤110 mm) | 8Ω ✓
- **Gate 5 — Sealed 1.2 L:** α = 4.7/1.2 = 3.917; √(1+3.917) = 2.217; Fc = 62 × 2.217 = **137.5 Hz** ✓; Qtc = 0.35 × 2.217 = **0.776** ✓
- **DSP correction vs TB sub (85 dB ref):** −2.0 dB — near-perfect match.
- **Power at reference (8Ω, 98 dB):** 10^(11/10) = **12.6W** (8.4% of 150W ✓). At burst (101 dB): 10^(14/10) = **25.1W** (16.7% ✓). Amp at 36V into 8Ω: 68.9W available — no limiter needed.
- **Centre spacing (FP OD 118.5 mm):** D3004/602010 (62mm) → **90mm** | Audaphon TWS 30/4 (104mm) → **111mm** | RS28A-4 (103mm) → **111mm** | SB19ST (88mm) → **103mm**
- **Why this stands out:** 150W rating vs 25.1W burst demand = 6× safety factor — uniquely immune to over-drive. Xmax=4.5mm is the best in the Morel 428 family and best of any 4.5" candidate. Fc=137.5 Hz in 1.2 L gives the most sub/mid room of any verified mid. No DSP power limiter needed at any project SPL.
- **Concern:** €153 significant. Crossover window with SB19ST is marginal (96 Hz, 0.07 oct) — ideal xover ~2,007 Hz. DPC cone character differs from paper; not warm/natural but neutral-analytical.
- **vs WF118WA07 (4Ω, Xmax=4mm, €95.70):** WA07 is €57 cheaper, Fs margin better (2.68×), 4Ω. EW 428 wins on 150W ceiling (no limiter), Xmax (4.5mm vs 4mm), Fc lower (138 vs 126 Hz). Choose WA07 for value; EW 428 if burst headroom is paramount.

### Morel CAW 428 ★ — Candidate (4.5", 4mm Xmax, lower cost than EW 428; lautsprechershop.de)
- Role: **MID** | Size: 4.5" | Frame OD: **118.5 mm** | Cutout: **94 mm** | Depth: **50 mm** | Impedance: **8Ω** | Cone: Damped Polymer Composite (DPC)
- Sensitivity: **88 dB @ 2.83V/1m** | Power: **150W (DIN)** | Xmax: **±4.0 mm** | Fs: **74 Hz**
- **T/S (verified from datasheet):** Qts 0.38 | Qes 0.46 | Qms 2.33 | Sd **57 cm²** | Vas **4.5 L** | Mms 4.55 g | Cms 1.007 mm/N | Rms 0.91 kg/s | BL 5.0 N·A | Re 5.5Ω | Le 0.32 mH
- **Source:** Morel CAW 428 datasheet (verified June 2026) | [research/morel_caw428.pdf](research/morel_caw428.pdf) | LSS: **€109.00 inc VAT / €91.60 exc VAT** | Stock (Jun 2026): in stock at LSS
- **Gate 1 — Max SPL (8Ω, P_ref=1W):** 88 + 10·log₁₀(150) = **109.8 dB** ✓
- **Gate 2 — Fs margin:** 150/74 = **2.03×** ⚠ marginal — just at 2× minimum. At 160 Hz crossover: 2.16×.
- **Gate 3 — Beaming (Sd=57 cm²):** same as EW 428 → f_beam = **2,570 Hz** ✓ (Sd=57 > 55 cm² proxy; f_beam passes operative gate). 0.8× ceiling = **2,056 Hz**.
- **Gate 4 — Physical:** OD 118.5 mm ✓ | Depth 50 mm ✓ (shallowest of any candidate) | 8Ω ✓
- **Gate 5 — Sealed 1.2 L:** α = 4.5/1.2 = 3.75; √4.75 = 2.179; Fc = 74 × 2.179 = **161.3 Hz** ⚠ (1.3 Hz over 160 Hz target); Qtc = 0.38 × 2.179 = **0.828** ✓. **Use 1.3–1.5 L box:** at 1.5 L → Fc = 74 × 2.0 = **148 Hz** ✓, Qtc = **0.76** ✓.
- **DSP correction vs TB sub (85 dB ref):** −3.0 dB.
- **Power at reference (8Ω, 98 dB):** 10^(10/10) = **10.0W** (6.7% of 150W ✓). At burst (101 dB): 10^(13/10) = **20.0W** (13.3% ✓).
- **Centre spacing:** Same OD as EW 428 (118.5 mm) → same spacings.
- **vs Morel EW 428 (Fs=62Hz, Xmax=4.5mm, €153):** EW 428 is better: 12Hz lower Fs (2.42× vs 2.03×), 0.5mm more Xmax, lower Fc in 1.2 L (138 vs 161 Hz). Cost delta: EW 428 is €44 more. Choose EW 428; CAW 428 only if budget constrained (€44 saving) with crossover raised to 160 Hz and box volume ≥1.3 L.

### Morel EM 428 ★ — Candidate (4.5" standard motor, entry of 428 family; lautsprechershop.de)
- Role: **MID** | Size: 4.5" | Frame OD: **118.5 mm** | Cutout: **94 mm** | Depth: **56 mm** | Impedance: **8Ω** | Cone: Damped Polymer Composite (DPC)
- Sensitivity: **87 dB @ 2.83V/1m** | Power: **150W (DIN)** | Xmax: **±3.0 mm** | Fs: **68 Hz**
- **T/S (verified from datasheet):** Qts 0.41 | Qes 0.48 | Qms 3.03 | Sd **57 cm²** | Vas **3.5 L** | Mms 6.55 g | Cms 0.88 mm/N | Rms 0.86 kg/s | BL 5.4 N·A | Re 5.4Ω | Le 0.36 mH
- **Source:** Morel EM 428 datasheet (verified June 2026) | [research/morel_em428.pdf](research/morel_em428.pdf) | LSS: **€134.00 inc VAT / €112.61 exc VAT** | Stock (Jun 2026): in stock at LSS
- **Gate 1 — Max SPL (8Ω, P_ref=1W):** 87 + 10·log₁₀(150) = **108.8 dB** ✓
- **Gate 2 — Fs margin:** 150/68 = **2.21×** ✓
- **Gate 3 — Beaming (Sd=57 cm²):** same as EW 428 → f_beam = **2,570 Hz** ✓. 0.8× ceiling = **2,056 Hz**.
- **Gate 4 — Physical:** OD 118.5 mm ✓ | Depth 56 mm ✓ | 8Ω ✓
- **Gate 5 — Sealed 1.2 L:** α = 3.5/1.2 = 2.917; √(1+2.917) = 1.979; Fc = 68 × 1.979 = **134.6 Hz** ✓; Qtc = 0.41 × 1.979 = **0.811** ✓. Smallest Vas of any Morel 428 → lowest Fc in 1.2 L box.
- **DSP correction vs TB sub (85 dB ref):** −2.0 dB.
- **Power at reference (8Ω, 98 dB):** 10^(11/10) = **12.6W** (8.4% of 150W ✓). At burst (101 dB): 10^(14/10) = **25.1W** (16.7% ✓).
- **vs Morel EW 428 (Fs=62Hz, Xmax=4.5mm, €153):** EW 428 is better in every acoustic parameter: 6Hz lower Fs, 1.5mm more Xmax, same 150W rating — at only €19 more. **Choose EW 428 over EM 428 unconditionally.** EM 428 relevant only if EW 428 sells out.

### SEAS CA12RCY H1152-08 ★ — Candidate (classic paper cone, 4.5"; lautsprechershop.de)
- Role: **MID** | Size: 4.5" | Frame OD: **120.4 mm** round | Impedance: **8Ω** | Cone: Paper (SEAS Prestige classic)
- Sensitivity: **? (unconfirmed)** | Power: **? (unconfirmed)** | Xmax: **? (unconfirmed)** | Fs: **? (unconfirmed)**
- ⚠ Full T/S not confirmed. The local file `research/seas_ca12rcy.pdf` is **the wrong driver** — it contains the SEAS 27TFFNC/CG H1406 tweeter, not the CA12RCY. Fetch the correct CA12RCY datasheet from seas.no before any analysis or ordering.
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS woofer index, June 2026) | LSS price: **€94.90 inc VAT / €79.75 exc VAT** | Stock (Jun 2026): in stock at LSS
- **Fs margin at 150 Hz crossover:** Not calculable — Fs unconfirmed. Fetch datasheet.
- **DSP correction vs TB sub (85 dB ref):** Not calculable — sensitivity unconfirmed. Fetch datasheet.
- **Power at reference:** Not calculable — sensitivity unconfirmed. Fetch datasheet.
- **Beaming:** ? (unconfirmed — Sd not yet confirmed; fetch datasheet for accurate beaming calculation).
- **Centre spacing (FP OD 120.4 mm):** D3004/602010 (62mm) → **91mm** | Audaphon TWS 30/4 (104mm) → **112mm** | TW022WA05 (103.75mm) → **112mm** | H1189-06 (103.8mm) → **112mm**
- **Why considered:** SEAS Prestige paper cone with classic warm character. €94.90 is well-priced for SEAS Prestige quality. 8Ω → ~31W at 24V. Full analysis pending datasheet.
- **Concern:** Beaming limit unconfirmed. Tweeter selection and crossover ceiling to be determined from datasheet Sd.
- **vs WF118WA07 (4Ω, Fs=56Hz, €95.70):** Nearly identical price. WA07 has 4Ω (61W at 24V vs 31W). CA12RCY wins on SEAS Prestige paper cone tonality. Full comparison pending CA12RCY datasheet.

### SB Acoustics SB12CACS25-4 ★ — Candidate (ceramic cone, 4"; Willys-Hifi / lautsprechershop.de)
- Role: **MID** | Size: 4" | Frame OD: **123 mm** ⚠ 1mm over project FP limit | Impedance: **4Ω** | Cone: Ceramic (aluminium oxide)
- Sensitivity: **87.5 dB @ 2.83V/1m** | Power: **30W RMS** | Xmax: **±5.0 mm** | Fs: **51 Hz**
- ⚠ Full T/S (Re, Qts, Sd, Vas) not confirmed — fetch SB Acoustics SB12CACS25-4 datasheet; confirm ceramic cone breakup frequency before ordering
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/sb-acoustics-sb12cacs25-4-ceramic-midwoofer) | Willys price: **£58.96** | Stock (Jun 2026): UK in stock
- Also at LSS: **€73.70 inc VAT / €61.93 exc VAT**
- **Fs margin at 150 Hz crossover:** 150/51 = **2.94×** — excellent; best Fs margin of any 4" candidate.
- **DSP correction vs TB sub (85 dB ref):** −2.5 dB — near-perfect match (4Ω: 1W sens = 87.5 − 3.01 = 84.49 dB).
- **Power at reference (4Ω, 87.5 dB, 98 dB target):** P = (2.83²/4) × 10^((98−87.5)/10) = 2.0 × 11.22 = **22.4W** (74.7% of 30W — approaching limit). At burst (101 dB): **44.8W** — exceeds 30W. **Set DSP limiter at 28W:** max mid SPL = 87.5 + 10×log(28/2) = 87.5 + 11.46 = **98.96 dB** ≈ 99 dB. Sub peaks at 101 dB: 2 dB gap at transients — acceptable for kitchen use.
- **Available @ 24V into 4Ω:** ~61W — amp headroom fine; driver is the limit.
- **Beaming (est. cone dia ~90mm):** f_beam ≈ 34400/(π×0.045) ≈ **2,440 Hz** — same class as DS115-8 (~2,636 Hz).
- **Centre spacing (FP OD 123 mm):** D3004/602010 (62mm) → **93mm** | Audaphon TWS 30/4 (104mm) → **114mm** | H1189-06 (103.8mm) → **113mm**
- **Why considered:** Xmax=5mm is the highest of any 4" candidate (matches SB12PACR25-4). Fs=51Hz gives 2.94× margin at 150 Hz — best in the 4" field. Ceramic cone character is different from paper/Al mids: harder, more revealing. At 123mm FP it's 1mm over the 122mm project limit — a known compromise accepted for the Xmax advantage.
- **FP concern:** 123mm OD is technically outside the ≤122mm FP limit. On 190mm baffle leaves 33.5mm each side. Surface mounting is fine; the 1mm over-spec is cosmetic only. Treat as FP=123mm approved.
- **Ceramic cone concern:** Aluminium oxide ceramic breakup peaks can be sharp. Confirm cone breakup frequency is above the mid/tweeter crossover (≥2,500 Hz) from datasheet before ordering.
- **vs SB12PFCR25-4 (4Ω, paper, Fs=58Hz, Xmax=4.9mm, €25.95):** CACS wins on Fs margin (2.94× vs 2.59×) and Xmax by 0.1mm. Paper wins on lower cost (€25.95 vs £58.96), softer tonality, and no ceramic breakup concern. Choose CACS only when Fs margin is the deciding factor.

### Vifa NE123-W08 ★ — Candidate (paper-composite cone, 4"; HiFi Collective / lautsprechershop.de)
- Role: **MID** | Size: 4" | Impedance: **8Ω** | Cone: Paper composite (NE-series construction) | Surround: Rubber
- Sensitivity: **? (unconfirmed — fetch datasheet)** | Power: **? (unconfirmed — fetch datasheet)** | Xmax: **? (unconfirmed — fetch datasheet)** | Fs: **? (unconfirmed — fetch datasheet)**
- ⚠ Full T/S not confirmed — fetch Vifa/Peerless NE123-W-08 datasheet before ordering; confirm FP OD
- **Source:** [HiFi Collective](https://www.hificollective.co.uk) (HFC woofer index, June 2026) | HFC price: **£60.84** (inc/ex-VAT status unconfirmed) | Stock: confirm before ordering
- Also at LSS: **€108.40 inc VAT / €91.09 exc VAT**
- **Fs margin at 150 Hz crossover:** Not calculable — Fs unconfirmed. Fetch datasheet.
- **Power at reference:** Not calculable — sensitivity and impedance unconfirmed. Fetch datasheet.
- **Why considered:** Vifa NE series (former Peerless by Tymphany, now ScanSpeak-manufactured) is known for excellent linearity, low distortion, and wide frequency extension. The NE123 is used in high-quality DIY builds as a mid with clean response to 5+ kHz. At HFC £60.84 it is priced similarly to DS115-8 + premium. If specs confirm, could be an alternative to DS115-8 for a "reference quality" mid with warm paper character.
- **Priority:** Confirm FP OD, Xmax, Fs from datasheet. If FP is ≤122mm and Xmax ≥4mm, promote to ★★.

---

## Hard-Excluded Drivers

These are excluded permanently and should not be re-evaluated.

### Peerless by Tymphany PLS-P830987 — Hard excluded
- Role: **EXCL** | Size: 3" nominal | Frame: **78×78 mm square** (confirmed pincushion — 4 flat edges, not a circle)
- Sensitivity: 81.8 dB | Fs: 110 Hz | Xmax: 5.4 mm | Qts: 1.0 | Power: 25W RMS | Imp: 8Ω
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/peerless-by-tymphany-pls-p830987.html) (specs fetched June 2026)
- **Reason:** 78×78 mm square frame is a non-circular design requirement — not a marginal deviation. All four flat sides will be visible from any angle when surface-mounted. Fails the circular rule unconditionally.
- **Also poor acoustically:** Fs 110 Hz gives only 1.36× margin at 150 Hz crossover; Qts 1.0 is very high; sensitivity 81.8 dB is 3.2 dB below sub reference. This driver would be a poor choice even if the frame were round.

### Lavoce MD03.10 — Hard excluded
- Role: **EXCL** | **Reason:** Designed as a rear-mount PA driver. Has flat-sided ear tabs on the mounting flange (non-circular), AND a front gasket specifically for flush-mount sealing. Both make it visually unacceptable when surface-mounted — the gasket sits proud of the baffle face and the ear tabs protrude from the sides. Even if technically front-mountable, the appearance is that of a PA driver bolted to a board.
- **Also:** Excessively expensive for this application (PA pricing, not hi-fi DIY).
- **Source confirmation:** [Bluearan product page](https://bluearan.co.uk/index.php?id=LAVMAF10300AF) confirms gasket-front mounting design.

### Tang Band W3-315E — Excluded (power)
- Role: **EXCL** | 3" | Frame OD: 3.66" (93 mm) | Impedance: 8Ω | Cone: Aluminium/Magnesium (white) | No phase plug
- Sensitivity: 87 dB @ 2.83V/1m | Power: 10W RMS / 20W max | Fs: 100 Hz | Xmax: 1.25 mm | Sd: 32 cm²
- Qts: 0.52 | Re: 6.6Ω | Mms: 2 g | Frequency response: 100–20,000 Hz
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/tang-band-w3-315e.html) (specs fetched June 2026)
- **Datasheet:** [research/tang_band_w3-315e.pdf](research/tang_band_w3-315e.pdf) | [original URL](https://doc.soundimports.nl/pdf/brands/Tang%20Band/W3-315E/pdf_Tang%20Band_W3-315E_1.pdf) (downloaded June 2026)
- **Visual:** White cone, no phase plug. Owner notes: contender but not favourite.
- **Reason excluded:** Cannot balance with woofer. At 87 dB sensitivity, needs 12.6W at reference level (98 dB) — already above the 10W RMS rating. At woofer max (101 dB) needs 25.1W vs 20W max. Power handling definitely excludes it.

### Monacor SPX-31M — Hard excluded
- Role: **EXCL** | **Reason:** 83 dB sensitivity (needs excessive DSP gain) + Xmax only 1.1 mm (inadequate at 150 Hz crossover).

### Peerless by Tymphany BC25TG15-04 — Hard excluded
- Role: **EXCL** | Sensitivity: 93.9 dB | Power: 7W RMS | Supplier: [SoundImports](https://www.soundimports.eu/en/peerless-by-tymphany-bc25tg15-04.html) | Price: €29.95
- **Reason:** Needs 10.3W to balance with woofer at max. Rated only 7W. Cannot balance at full volume.

### Peerless by Tymphany OC25SC65-04 — Hard excluded (tweeters)
- Role: **EXCL** | Sensitivity: 92.3 dB | Power: 12W RMS | Supplier: [SoundImports](https://www.soundimports.eu/en/peerless-by-tymphany-oc25sc65-04.html) | Price: €26.95
- **Reason:** Faceplate-less twist-lock design — cannot surface-mount to a flat baffle. Also at woofer max, needs 14.8W against 12W rated — over-driven at full volume.

### Dayton Audio ND25FN-4 — Hard excluded (tweeters)
- Role: **EXCL** | **Reason:** No faceplate at all — designed for embedding into waveguides. Cannot surface-mount.

---

## Out-of-Stock / Deferred

| Driver | Status |
|--------|--------|
| SB Acoustics SB12PACR25-4 | OOS at SoundImports until November 2026; available Willy's HiFi UK (£23.76) — see Candidate entry |

---

## Eliminated on Specification

| Driver | Reason |
|--------|--------|
| Monacor DT-25N | Fs 1600 Hz marginal for low crossovers; waveguide design |
| Dayton ND20FA-6 | Fs 2005 Hz too high; 15W RMS; 6Ω impedance |
| Scan-Speak D7608/920010 | Xmax 0.4 mm; Qts 1.73; €106.95 over budget |
| HiVi Swan DM-7500 | €79.95 over budget; 600 Hz+ min crossover eliminates separate tweeter |
| Dayton Audio RS52FN-8 | Xmax 1 mm; Fs 394 Hz (not suitable as bass-mid) |
| Dayton Audio PA130-8 | Frame OD 132 mm; Xmax 2 mm |
| SB Acoustics SB13PFCR25-4 | 5" nominal, large frame; Qts 0.29 |

---

## June 2026 Mass Index — Tweeters (all visual constraints removed)

All tweeters indexed from SoundImports pages 4–6 (cheapest sort, June 2026). No visual exclusions applied.

### Peerless by Tymphany XT25SC40-04 — Catalogue — INELIGIBLE (ring radiator)
- Role: **HIGH** | Type: Ring radiator | Size: 1" (25mm) | Imp: 4Ω | Sensitivity: 94 dB | Power: 100W RMS | Fs: 1018 Hz
- Neodymium motor. Compact cutout 1.73" (44mm). Depth 0.79" (20mm).
- **Source:** https://www.soundimports.eu/en/peerless-by-tymphany-xt25sc40-04.html | Price: €29.95 | Stock: 10+
- Note: Ring radiator — ineligible (poor 60° off-axis, RAW-CAt Tweeter Shootout Part 6, Nov 2025). Fs 1018 Hz → min xover 2036 Hz.

### Peerless by Tymphany DX20BF00-04 — Catalogue (OOS)
- Role: **HIGH** | Type: Dome | Size: 3/4" | Imp: 4Ω | Specs: not retrieved (pre-order, page returned full specs unavailable)
- **Source:** https://www.soundimports.eu/en/peerless-by-tymphany-dx20bf00-04.html | Price: €29.95 | Stock: OOS

### Dayton Audio TD25F-4 — Catalogue
- Role: **HIGH** | Type: Dome (silk) | Size: 1" (25mm) | Imp: 4Ω | Sensitivity: 91 dB | Power: 20W RMS | Fs: 900 Hz
- Semi-horn loaded faceplate. Cutout 2.75" (70mm). Ferrofluid.
- **Source:** https://www.soundimports.eu/en/dayton-audio-td25f-4.html | Price: €29.95 | Stock: 10+
- Note: Fs 900 Hz → min xover 1800 Hz. "Semi-horn" faceplate — narrower HF dispersion than flat-face designs. 20W adequate.

### SB Acoustics SB26ST-C000-5 — Catalogue
- Role: **HIGH** | Type: Dome (fine weave fabric) | Size: 1" | Imp: 5Ω | Sensitivity: 91 dB | Power: 80W RMS | Fs: 870 Hz | Xmax: 0.6 mm
- CCAW voice coil. Saturation-controlled motor. Internal pressure equalization.
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb26st-c000-5.html | Price: €30.95 | Stock: 10+
- Note: 5Ω unusual — JAB5 handles it; ~49W available at 24V. 80W power rating is excellent. Fs 870 Hz comfortable.

### Dayton Audio CF18N-4 — Catalogue
- Role: **HIGH** | Type: Dome (woven carbon fiber) | Size: 3/4" (18mm) | Imp: 4Ω | Sensitivity: 90 dB | Power: 40W RMS | Fs: 1100 Hz
- Neodymium motor. Ferrofluid. Cast aluminium faceplate with protective grill.
- **Source:** https://www.soundimports.eu/en/dayton-audio-cf18n-4.html | Price: €30.54 (sale, was €36.95) | Stock: **pre-order / OOS** (Jun 2026)
- Note: Carbon fiber dome — distinctive appearance. Reviewer noted rolloff above 12 kHz beyond 30°. Fs 1100 Hz → min xover 2200 Hz. **OOS — CF1/CF2/CF3 pairings not available for immediate order.**

### Peerless by Tymphany NE25VTS-04 — Catalogue
- Role: **HIGH** | Type: Dome (silk) | Size: 1" | Imp: 4Ω | Sensitivity: 91.1 dB | Power: 15W RMS | Fs: 730 Hz | OD: 66.3 mm
- Neodymium magnet. Aluminium faceplate. Aluminium rear chamber doubles as heatsink. Copper cap.
- **Source:** https://www.soundimports.eu/en/peerless-by-tymphany-ne25vts-04.html | Price: €39.95 | Stock: 10+
- Note: Very compact 66.3mm OD (similar to ND25FA-4 at 66mm). Fs 730 Hz → min xover 1460 Hz. Low 15W power — same concern as DX25TG59-04 family but lower sensitivity means higher power draw.

### SB Acoustics SB21SDC-C000-4 — Catalogue (ring dome, 1 in stock)
- Role: **HIGH** | Type: Ring dome | Size: 3/4" (20mm) | Imp: 4Ω | Sensitivity: 91 dB | Power: 40W RMS | Fs: 720 Hz | Qts: 0.95 | OD: 3.62" (92mm)
- CCAW voice coil. Copper cap. Dual balanced compression chamber.
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb21sdc-c000-4.html | Price: €39.95 | Stock: 1
- Note: Ring dome design — same principle as ring radiator but with dome element. Fs 720 Hz → min xover 1440 Hz. Only 1 unit in stock.

### SB Acoustics SB29SDAC-C000-4 — Catalogue
- Role: **HIGH** | Type: Dome (1 1/8", 25mm actual dome on 29mm voice coil) | Imp: 4Ω | Sensitivity: 93 dB | Power: 60W RMS | Fs: 600 Hz | Qts: 0.80 | Xmax: 0.25 mm
- CCAW voice coil. Dual balanced compression chamber. Cast aluminium faceplate. Copper cap.
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb29sdac-c000-4.html | Price: €44.95 | Stock: 10
- Note: Fs 600 Hz → min xover 1200 Hz — widest crossover placement of the SB29 family. 93 dB high sensitivity. Saturation-controlled motor.
- **Off-axis gate — PASS for the critical band (owner reading, June 2026):** 60° response tracks roughly on-axis to ~11 kHz, then falls off a cliff at ~12 kHz. The critical kitchen band (2.8–10 kHz) is fully covered at 60°; only top-octave air above ~12 kHz is lost at wide angles — acceptable for the 60° geometry. Conventional soft dome (not a ring radiator), so eligible.

### SB Acoustics SB29RDC-C000-4 — Catalogue (ring dome)
- Role: **HIGH** | Type: Ring dome (fabric) | Size: 1 1/8" (25mm) | Imp: 4Ω | Sensitivity: 93 dB | Power: 100W RMS | Fs: 600 Hz | Qts: 0.65 | Xmax: 0.25 mm
- Fabric ring dome. Stabilizing ring reduces distortion. Copper cap.
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb29rdc-c000-4.html | Price: €53.45 | Stock: 10+
- Note: Same Fs as SDAC (600 Hz) but ring dome construction. 100W power handling. 0.7 dB lower sensitivity than RDNC.

### SB Acoustics SB29RDNC-C000-4 — Catalogue (ring dome, neodymium)
- Role: **HIGH** | Type: Ring dome (fabric) | Size: 1 1/8" (25mm) | Imp: 4Ω | Sensitivity: 94 dB | Power: 100W RMS | Fs: 580 Hz | Re: 3Ω
- Neodymium magnet. Fabric ring dome. Chambered back for reduced back-wave reflections. Copper cap.
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb29rdnc-c000-4.html | Price: €68.45 | Stock: 10+
- Note: Highest-end SB29 ring dome. 94 dB sensitivity. Fs 580 Hz → min xover 1160 Hz. Premium price. Mixed reviews (some praise, others find it lacks detail vs alternatives).

### Dayton Audio AMT Mini-8 — Catalogue (AMT, OOS)
- Role: **HIGH** | Type: AMT (Air Motion Transformer / folded Kapton ribbon) | Imp: 8Ω | Sensitivity: 88 dB | Power: 15W RMS | Freq: 3500–40,000 Hz | Face OD: 2.25" (57mm)
- **Source:** https://www.soundimports.eu/en/dayton-audio-amt-mini-8.html | Price: €36.45 | Stock: pre-order (OOS)
- Note: AMT construction — different operating principle from dome. 88 dB sensitivity is the lowest of any tweeter candidate. Reviewer noted "output very low." 15W RMS modest.

### Monacor DT-100 — Catalogue
- Role: **HIGH** | Type: Dome (soft) | Size: 1" | Imp: 8Ω | Sensitivity: 92 dB | Power: 30W RMS / 60W max | Fs: 1500 Hz | Faceplate: 80×116mm (rectangular)
- Ferrofluid cooled. Cutout: 72mm.
- **Source:** https://www.soundimports.eu/en/monacor-dt-100.html | Price: €43.95 | Stock: 10+
- Note: Rectangular 80×116mm faceplate — not circular. Fs 1500 Hz → min xover 3000 Hz. Recommended crossover: 2500 Hz (12 dB/oct). High sensitivity at 92 dB.

### Dayton Audio TD20F-4 — Catalogue
- Role: **HIGH** | Type: Dome (silk) | Size: 3/4" (18mm) | Imp: 4Ω | Sensitivity: 90 dB | Power: 20W RMS | Fs: ~3000 Hz (from freq response start) | OD: 2.56" (65mm) | Depth: 0.59" (15mm)
- Neodymium motor. Ferrofluid.
- **Source:** https://www.soundimports.eu/en/dayton-audio-td20f-4.html | Price: €17.45 | Stock: 10+
- Note: Very compact (65mm OD, 15mm deep). Fs very high — frequency response starts at 3 kHz. Crossover must be ≥3 kHz. Cheapest 3/4" candidate after ND20FA-6.

### Peerless by Tymphany D26NC56-06 — Catalogue (OOS)
- Role: **HIGH** | Type: Dome | Size: 1" | Imp: 6Ω | Price: €24.95 | Stock: pre-order (OOS)
- **Source:** https://www.soundimports.eu/en/peerless-by-tymphany-d26nc56-06.html
- Note: Specs not retrieved from product page (OOS). Pre-order only.

### Monacor DT 94-8 — Catalogue (URL unconfirmed)
- Role: **HIGH** | Type: Dome | Size: 0.8" | Imp: 8Ω | Price: €29.95 | Stock: 3 (per index)
- **Source:** URL not confirmed via search (0 results for "DT94"). Listed in SoundImports tweeter index June 2026.
- Note: Tiny 0.8" dome. Specs not retrieved. Very small dome favours HF dispersion.

### Monacor DT-28N — Catalogue
- Role: **HIGH** | Type: Dome (silk) | Size: 1 1/8" (28mm) | Imp: 8Ω | Sensitivity: 94 dB | Power: 50W RMS / 100W max | Fs: 1200 Hz | Freq: 2000–20,000 Hz
- Neodymium. Small waveguided faceplate. Cutout: 50mm. Depth: 21mm.
- **Source:** https://www.soundimports.eu/en/monacor-dt-28n.html | Price: €40.95 | Stock: 5
- Note: Fs 1200 Hz → min xover 2400 Hz. 94 dB very high sensitivity (needs ~9 dB DSP pad vs 85 dB sub). 50W power. Compact at 50mm cutout. Neodymium.

### Scan-Speak Discovery D2604/830000 — Catalogue
- Role: **HIGH** | Type: Dome (textile) | Size: 1" | Imp: 4Ω | Sensitivity: 92 dB | Power: 100W RMS / 240W max | Fs: ~630 Hz (from freq response start) | OD: 104.2mm | Cutout: 75mm | Depth: 25.4mm
- Qts: 0.79 | Qms: 3.46 | Qes: 1.02
- **Source:** https://www.soundimports.eu/en/scan-speak-d2604830000.html | Price: €44.95 | Stock: 10+ (listed as pre-order)
- Note: 100W is highest power of any standard dome candidate. 92 dB high sensitivity. Large 104.2mm OD. Scan-Speak Discovery series pedigree.

### SEAS Prestige 27TFFNC/CG H1406-04 — Catalogue
- Role: **HIGH** | Type: Dome (sonolex precoated fabric) | Size: 1.1" (26mm dome on wider former) | Imp: 4Ω | Sensitivity: 91 dB | Power: 80W RMS / 200W max | Freq: 2500–30,000 Hz
- Neodymium. Wide roll surround. Dual-chamber magnet. Magnetic fluid immersion.
- **Source:** https://www.soundimports.eu/en/seas-27tffnc-cg.html | Price: €40.45 (sale, was €48.95) | Stock: **pre-order / OOS** (Jun 2026)
- Note: SEAS Prestige series. 80W power. Magnetic fluid improves power handling. Sonolex fabric dome. **OOS — SE1/SE2 pairings not available for immediate order.**

### Markaudio TW 6 — Catalogue
- Role: **HIGH** | Type: Dome (aluminium) | Size: 1" | Imp: 4Ω | Sensitivity: 98 dB | Power: 15W RMS / 30W max | Fs: 1700 Hz | OD: 74mm
- Ferrofluid. Custom polymer frame with integrated waveguide.
- **Source:** https://www.soundimports.eu/en/markaudio-tw-6.html | Price: €44.95 | Stock: 8
- Note: 98 dB — highest sensitivity of any tweeter evaluated in this project. Needs −13 dB DSP pad vs 85 dB sub; at reference needs only 0.9W RMS. Al dome typically bright character. Fs 1700 Hz → min xover 3400 Hz. Waveguide narrows off-axis response.

### Peerless by Tymphany DA25BG08-06 — Catalogue
- Role: **HIGH** | Type: Dome (aluminium) | Size: 1" | Imp: 6Ω | Sensitivity: 91.6 dB | Power: 15W RMS | Fs: 710 Hz | OD: not stated
- Ferrite magnet. Heat-sinking design.
- **Source:** https://www.soundimports.eu/en/peerless-by-tymphany-da25bg08-06.html | Price: €39.95 | Stock: 10+
- Note: Aluminium dome. Low 15W power. Fs 710 Hz → min xover 1420 Hz. 6Ω: JAB5 at 24V ~41W available; needs ~4W at reference.

### GRS A25-2T — Catalogue
- Role: **HIGH** | Type: Dome (fabric) | Size: 2" | Imp: 6Ω | Sensitivity: 92.8 dB | Power: 30W RMS | Freq: 1500–16,000 Hz | OD: not stated
- Neodymium. Dimensionally compatible with Dynaco A25 crossover.
- **Source:** https://www.soundimports.eu/en/grs-a25-2t.html | Price: €39.95 | Stock: 10+
- Note: 2" dome — larger dome typically narrower HF dispersion. Designed as Dynaco A25 replacement. 92.8 dB sensitivity. Reviewer noted unit-to-unit variation requiring individual measurement.

### SEAS 27TDFC H1189-06 — Catalogue (10+ in stock)
- Role: **HIGH** | Type: Dome (soft textile) + rear chamber | Size: 1" (27mm) | Imp: 6Ω | Sensitivity: 90 dB | Power: 90W RMS / 220W max | Fs: 550 Hz | FP OD: 103.8mm | Cutout: 73mm | Depth: 39mm
- **Source:** https://www.soundimports.eu/en/seas-27tdfc.html | Price: €71.86 (sale) | Stock: 10+
- Note: Widest-window standard dome in catalogue. Fs 550 Hz → min xover 1,100 Hz. 90W/220W; at project SPL needs only 16.8W burst. 6Ω: 41W available at 24V. See full Candidate entry above.

### Scan-Speak Discovery R2604/833000 — Catalogue — INELIGIBLE (ring radiator)
- Role: **HIGH** | Type: Ring Radiator (dual) | Size: 1" (25mm) | Imp: 4Ω | Sensitivity: 92 dB | Power: 100W RMS | Fs: 440 Hz | Re: 2.9Ω | Xmax: 0.2mm
- **Source:** https://www.soundimports.eu/en/scan-speak-r2604-833000.html | Price: €62.45 | Stock: 10+
- Note: Ring radiator — ineligible (poor 60° off-axis, RAW-CAt Tweeter Shootout Part 6, Nov 2025). Had the widest crossover window of any tweeter (Fs 440 Hz). See full analysis in section above.

### Scan-Speak Discovery R2604/832000 — Catalogue — INELIGIBLE (ring radiator)
- Role: **HIGH** | Type: Ring Radiator (dual) | Size: 1" (25mm) | Imp: 4Ω | Sensitivity: 90 dB | Power: 100W RMS | Fs: 500 Hz | Re: 2.9Ω | Xmax: 0.2mm
- **Source:** https://www.soundimports.eu/en/scan-speak-r2604-832000.html | Price: €52.95 | Stock: 10+
- Note: Ring radiator — ineligible (poor 60° off-axis, RAW-CAt Tweeter Shootout Part 6, Nov 2025). Fs 500 Hz → min 1,000 Hz xover.

### SB Acoustics SB21RDC-C000-4 — Catalogue — INELIGIBLE (ring radiator)
- Role: **HIGH** | Type: Ring Radiator | Size: 3/4" (20mm) | Imp: 4Ω | Sensitivity: 90 dB | Power: 40W RMS | Fs: 760 Hz | Re: 3.1Ω | Xmax: 0.5mm
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb21rdc-c000-4.html | Price: €49.95 | Stock: 8
- Note: Ring radiator — ineligible (poor 60° off-axis, RAW-CAt Tweeter Shootout Part 6, Nov 2025). Fs 760 Hz → min xover 1,520 Hz.

### SB Acoustics SB29RDAC-C000-4 — Catalogue (ring dome)
- Role: **HIGH** | Type: Ring dome (fabric) | Size: 1¼" (25mm) | Imp: 4Ω | Sensitivity: 93 dB | Power: 100W RMS | Fs: 900 Hz | FP OD: 103.8mm | Cutout: 70mm
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb29rdac-c000-4.html | Price: €56.95 | Stock: OOS; 6 expected 31 Jul 2026
- Note: Ferrite ring dome — same 29 mm fabric-ring diaphragm as SB29RDNC. Ring domes carry no off-axis advantage. Fs 900 Hz → min xover 1,800 Hz. See full Candidate entry above.

### Dayton Audio CF120-4 — Catalogue (OOS at SI; in stock Audiophonics)
- Role: **HIGH** | Size: 4.5" | Frame OD: ~127mm | Cutout: ~95mm | Depth: ~57mm | Imp: 4Ω | Sensitivity: 89.1 dB | Power: 30W RMS / 60W max | Cone: carbon fiber
- Fs: 53.2 Hz | Qts: 0.28 | Qes: 0.32 | Qms: 1.89 | Vas: 4.87L | Xmax: 3.5mm | Sd: 51.5 cm²
- **Source:** https://www.soundimports.eu/en/dayton-audio-cf120-4.html (OOS) | SI Price: €62.45 (sale) | Audiophonics: €49.92 (sale), in stock
- Note: Carbon fiber 4.5" midwoofer. Fs 53.2 Hz → min LP crossover 106 Hz (excellent). Beaming limit 2,703 Hz — place mid LP at or below this. Burst power needed: 31W vs 30W rated — tight (DSP limiter at 28W gives 100.6 dB). OOS at SI; in stock at Audiophonics (€49.92). Consider if DS115-8 goes OOS.

---

## June 2026 Mass Index — Woofers & Midranges (all visual constraints removed)

All drivers indexed from SoundImports woofer pages (3"–5.25" filter, cheapest sort, June 2026). No visual exclusions applied.

### Dayton Audio CE78PF-4 — Catalogue
- Role: **MID** | Size: 3" | Frame OD: 78mm | Imp: 4Ω | Sensitivity: 85 dB | Power: 10W RMS / 20W max | Fs: 100 Hz | Xmax: 1.4mm
- **Source:** https://www.soundimports.eu/en/dayton-audio-ce78pf-4.html | Price: €12.95 | Stock: 7
- Note: Very low power (10W) and Xmax (1.4mm). Suitable only for satellite or ultra-low-level mid role. Smallest OD (78mm) evaluated.

### Dayton Audio PC83-4 — Catalogue
- Role: **MID** | Size: 3" | Imp: 4Ω | Sensitivity: 86.8 dB | Power: 30W RMS / 60W max | Freq: 80–20,000 Hz | Cone: poly-damped woven glass fiber
- Copper cap to control inductance.
- **Source:** https://www.soundimports.eu/en/dayton-audio-pc83-4.html | Price: €15.65 | Stock: 2 (10 expected June 19 2026)
- Note: 30W RMS is solid for a 3" driver. Glass fiber cone. Budget option.

### GRS 4PF-8 — Catalogue
- Role: **MID** | Size: 4" | Imp: 8Ω | Sensitivity: 83 dB | Power: 40W RMS / 70W max | Fs: 137 Hz | Cone: poly-laminated paper, treated foam surround
- **Source:** https://www.soundimports.eu/en/grs-4pf-8.html | Price: €13.95 | Stock: 10
- Note: Very high Fs (137 Hz) → min xover 274 Hz. 83 dB sensitivity is lowest of any mid candidate — needs +2 dB DSP gain. Budget driver.

### SB Acoustics SB10PGC21-4 — Catalogue
- Role: **MID** | Size: 3" | Frame: square chassis | Imp: 4Ω | Sensitivity: 84 dB | Power: 20W RMS | Freq: 90–20,000 Hz | Cone: fiberglass
- CCAW voice coil. Vented.
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb10pgc21-4.html | Price: €18.95 | Stock: 10+
- Note: Square chassis (not circular frame). 84 dB sensitivity. Designed for FAST, satellites, tiny enclosures. 20W RMS modest.

### HiVi Swan B3S — Catalogue
- Role: **MID** | Size: 3" | Frame: square | Imp: 8Ω | Sensitivity: 82 dB | Power: 15W RMS / 30W max | Fs: 100 Hz | Xmax: 3mm
- Al/Mg alloy concave cone. Magnetically shielded. Stamped steel frame.
- **Source:** https://www.soundimports.eu/en/hivi-b3s.html | Price: €18.45 | Stock: 8
- Note: Square frame. Very low 82 dB sensitivity. 15W modest. Fs 100 Hz → min xover 200 Hz. Shielded.

### HiVi Swan M3N-B — Catalogue
- Role: **MID** | Size: 3" | Imp: 8Ω | Sensitivity: 82 dB | Power: 15W RMS | Fs: 91 Hz | Xmax: 3mm | VC: 20mm | Bolt circle: 83mm | Cutout: 68mm
- Black Al/Mg alloy cone. Magnetically shielded. Hi-temp VC.
- **Source:** https://www.soundimports.eu/en/hivi-m3n-b.html | Price: €18.45 | Stock: 10+
- Note: 3" black Al/Mg cone. Very low 82 dB sensitivity. Fs 91 Hz is decent. 15W RMS modest.

### Monacor SPX-32M — Catalogue
- Role: **MID** | Size: 3" | Imp: 8Ω | Sensitivity: 88 dB | Power: 20W RMS / 40W max | Fs: 110 Hz | Cone: paper | Freq: 100–22,000 Hz
- Solid wooden phase plug.
- **Source:** https://www.soundimports.eu/en/monacor-spx-32m.html | Price: €27.45 | Stock: 8
- Note: 88 dB is well-matched to sub reference. Wooden phase plug — distinctive visual. Fs 110 Hz → min xover 220 Hz. Full-range oriented.

### FaitalPRO 3FE25-4F — Catalogue
- Role: **MID** | Size: 3" | Imp: 4Ω | Sensitivity: 91 dB | Power: 20W RMS / 40W max | Fs: 110 Hz | Freq: 100–20,000 Hz | Cone: treated paper | VC: 19mm Al on Kapton | Frame: steel
- **Source:** https://www.soundimports.eu/en/faitalpro-3fe25-4f.html | Price: €19.95 | Stock: 10+
- Note: 91 dB very high for a 3" driver — needs ~6 dB DSP pad. Fs 110 Hz → min xover 220 Hz. FaitalPRO quality for PA/pro audio applications.

### FaitalPRO 3FE25-8F — Catalogue
- Role: **MID** | Size: 3" | Imp: 8Ω | Sensitivity: 91 dB | Power: 20W RMS / 40W max | Fs: 110 Hz | Freq: 100–20,000 Hz | Cone: treated paper | Re: 6.2Ω
- **Source:** https://www.soundimports.eu/en/faitalpro-3fe25-8f.html | Price: €19.95 | Stock: 10+
- Note: 8Ω version of 3FE25-4F. Identical sensitivity and Fs.

### FaitalPRO 3FE25-16F — Catalogue
- Role: **MID** | Size: 3" | Imp: 16Ω | Sensitivity: 91 dB | Power: 20W RMS / 40W max | Fs: 110 Hz | Freq: 100–20,000 Hz | Cone: treated paper
- **Source:** https://www.soundimports.eu/en/faitalpro-3fe25-16f.html | Price: €19.95 | Stock: 10+
- Note: 16Ω version — unusual impedance not compatible with JAB5 without series resistor.

### SEAS FA8RCND/S — Catalogue
- Role: **MID** | Size: 3" | Imp: 4Ω | Sensitivity: 86 dB | Power: 10W RMS / 12W max | Fs: 72 Hz | Xmax: 4mm | Freq: 100–20,000 Hz | Cone: paper | VC: 25.5mm
- **Source:** https://www.soundimports.eu/en/seas-fa8rcnds.html | Price: €32.45 | Stock: 8
- Note: Only 10W RMS / 12W max — extremely low power for this project. At 98 dB reference needs 12.6W already over rated power. Not suitable unless DSP limits system SPL. Xmax 4mm is excellent for size. Fs 72 Hz outstanding.

### SICA 3.5 F 1 CS-8 — Catalogue
- Role: **MID** | Size: 3.5" | Frame OD: 88mm | Imp: 8Ω | Sensitivity: 88.5 dB | Power: 90W program (continuous not stated) | Freq: 110–12,000 Hz | Cone: waterproof paper | VC: 1" Kapton
- **Source:** https://www.soundimports.eu/en/sica-35-f-1-cs-8.html | Price: €28.95 | Stock: 4
- Note: Pro audio / PA driver. 90W program power. Compact OD 88mm. Freq starts at 110 Hz → mid-band use only. 88.5 dB sensitivity well-matched. No Fs, Xmax, or Qts stated.

### Peerless by Tymphany TC9FD18-08 — Catalogue
- Role: **MID** | Size: 3.5" | Imp: 8Ω | Sensitivity: 84 dB | Power: 30W RMS | Fs: 130 Hz | Qts: 0.97 | Cutout: 80mm | Cone: NRSC patented paper | Freq: 70–20,000 Hz
- Copper pole cap. Non-resonant polymer chassis.
- **Source:** https://www.soundimports.eu/en/peerless-by-tymphany-tc9fd18-08.html | Price: €34.95 | Stock: 10+
- Note: High Qts (0.97) — Butterworth-like character, relatively underdamped. Fs 130 Hz → min xover 260 Hz. 84 dB low — needs DSP gain. Popular in DIY community for open-baffle and line array applications.

### Dayton Audio ND91-4 — Catalogue
- Role: **MID** | Type: full-range woofer | Size: 3.5" | Frame: **round** | Frame OD: **103.5 mm** | Impedance: 4Ω | Cutout: 85 mm | Depth: 63.4 mm | 4 mounting holes | Shielded: yes
- Cone: black anodised aluminium alloy | Rubber surround | VC: 1" 4-layer underhung, aluminium wire, Kapton/polyimide former | Copper alloy shorting ring | Magnet: **Neodymium (Neo-Balanced, self-shielded)**
- Sensitivity: 85.6 dB | Power: 30W RMS / 60W max | Freq: 65–17,000 Hz
- Fs: 74 Hz | Xmax: 4.6 mm | Vd: 12.2 cm³ | Sd: 30.4 cm² | Vas: 1.4 L | Qts: 0.41 | Qes: 0.45 | Qms: 4.24
- BL: 4.59 Tm | Re: 4.3Ω | Le: 0.83 mH | Mms: 4.8 g | Cms: 0.96 mm/N | VC: 25 mm
- Sealed alignment: 0.01 ft³ (0.28 L), F3 = 132 Hz | Vented alignment: 0.03 ft³ (0.85 L), F3 = 73 Hz
- **Source:** [SoundImports](https://www.soundimports.eu/en/dayton-audio-nd91-4.html) | Datasheet: [local](research/dayton_nd91-4_datasheet.pdf) / [original](https://doc.soundimports.nl/pdf/brands/Dayton%20Audio/ND91-4/pdf_dayton%20audio_ND91-4_1.pdf) (fetched June 2026) | Price: €33.95 | Stock: 10+
- **Fs check:** 74 Hz → 2× = 148 Hz — just passes the 150 Hz crossover target.
- **Beaming:** Sd 30.4 cm² → effective radius 31.1 mm → beaming starts ~3,520 Hz. No concern.
- **DSP correction vs TB sub (85 dB ref):** −0.6 dB — near-perfect sensitivity match; essentially no pad needed.
- **Power check:** At 98 dB: 8.5W. At 101 dB: 17W. Both within 30W rating. ✓
- **Note:** ND91-4 is a full-range woofer. The ND90-4 is a separate square-framed bass midwoofer from the same Dayton ND compact series — see entry below.

### Dayton Audio ND90-4 — Catalogue
- Role: **MID** | Type: full-range woofer | Size: 3.5" | Frame: **square** | Frame OD: **103.5 mm** | Impedance: 4Ω | Cutout: 85 mm | Depth: 60.8 mm | 4 mounting holes | Shielded: yes (self-shielded)
- Cone: black anodised aluminium alloy | Rubber surround | VC: 19 mm, 4-layer underhung, copper wire, Kapton/polyimide former | Magnet: **Neodymium (Neo-Balanced)**
- Sensitivity: **85.7 dB** @ 2.83V/1m | Power: 20W RMS / 40W max | Freq: 80–15,000 Hz
- Fs: 90.2 Hz | Xmax: 4.0 mm | Vd: 12.5 cm³ | Sd: 31.2 cm² | Vas: 1.06 L | Qts: 0.63 | Qes: 0.72 | Qms: 5.10
- BL: 3.47 Tm | Re: 3.6Ω | Le: 0.62 mH | Mms: 4.3 g | Cms: 0.73 mm/N
- **Source:** [SoundImports](https://www.soundimports.eu/en/dayton-audio-nd90-4.html) | Datasheet: [local](research/dayton_nd90-4_datasheet.pdf) / [original](https://doc.soundimports.nl/pdf/brands/Dayton%20Audio/ND90-4/pdf_dayton%20audio_ND90-4_1.pdf) (fetched June 2026)
- **Fs check:** 90.2 Hz → 2× = 180 Hz — above the 150 Hz crossover target. Fails the 2× rule.
- **DSP correction vs TB sub (85 dB ref):** −0.7 dB — near-identical sensitivity to sub (and to ND91-4).
- **Companion PR:** ND90-PR (also square frame) at SI €14.95.
- **vs ND91-4:** Same sensitivity. Higher Fs (fails 2× rule), lower Xmax (4mm vs 4.6mm), lower power (20W vs 30W), smaller VC (19mm vs 25mm). ND91-4 is the better mid candidate. ND90-4 advantage: neodymium motor is more compact.

### Tectonic TEBM65C20F-8 BMR — Catalogue
- Role: **MID** | Size: 3.5" | Imp: 8Ω | Sensitivity: 81 dB | Power: 30W RMS / 60W max | Xmax: 3.5mm | Freq: 80–20,000 Hz | Type: Balanced Mode Radiator
- **Source:** SoundImports product page | Price: €49.95 | Stock: in stock
- Note: BMR technology — single driver covers 80–20kHz as full-range. Could eliminate separate tweeter. 81 dB sensitivity very low (needs +4 dB DSP gain). Price premium. Unusual operating principle.

### Peerless by Tymphany PLS-P830986 — Catalogue
- Role: **MID** | Size: 3" | Imp: 8Ω | Sensitivity: 84.2 dB | Power: 25W RMS | Fs: 110 Hz | Xmax: 4.35mm | Cone: anodized aluminum (black) | Cutout: ~75mm | VC: 25.7mm
- Neodymium. Copper cap. Damped plastic basket.
- **Source:** https://www.soundimports.eu/en/peerless-by-tymphany-pls-p830986.html | Price: €29.95 | Stock: 10+
- Note: Black anodized aluminum cone — visually compatible. Xmax 4.35mm excellent for a 3" driver. 84.2 dB sensitivity needs +0.8 dB DSP gain. Fs 110 Hz → min xover 220 Hz.

### Markaudio CHN-70 — Catalogue
- Role: **MID** | Size: ~5" | Imp: 8Ω | Sensitivity: 86.7 dB | Power: 16W RMS / 50W max | Fs: 71.6 Hz | Xmax: 4mm | Cone: paper | Freq: ~70–20,000 Hz
- Full-range design.
- **Source:** SoundImports product page | Price: €32.45 | Stock: 4
- Note: Full-range (no separate tweeter needed) but 16W continuous is low for this system. Fs 71.6 Hz → min xover 143 Hz (excellent). Xmax 4mm solid. Only 4 in stock.

### Markaudio Alpair-5 Grey — Catalogue (OOS)
- Role: **MID** | Size: 3" | Imp: 4Ω | Sensitivity: 85.45 dB | Power: 5W RMS | Fs: ~85–95 Hz (pair-matched to ±1 Hz @ F0) | Freq: 90–25,000 Hz
- Free-to-air single suspension design. Pair-matched.
- **Source:** https://www.soundimports.eu/en/markaudio-alpair-5-grey.html | Price: €49.95 | Stock: OOS

### Markaudio Alpair-5 Gold — Catalogue (OOS)
- Role: **MID** | Size: 3" | Imp: 4Ω | Sensitivity: 85.5 dB | Power: 5W RMS | Fs: 94.5 Hz | Xmax: 3mm | Qts: 0.50 | Vas: 1.78 L | Cone: aluminum
- **Source:** https://www.soundimports.eu/en/markaudio-alpair-5-gold.html | Price: €49.95 | Stock: OOS
- Note: Both Alpair-5 variants OOS. Only 5W RMS — insufficient for this system at any meaningful SPL.

### Markaudio Alpair-5G — Catalogue (OOS)
- Role: **MID** | Size: 3" | Imp: 4Ω | Sensitivity: 88.53 dB | Power: 7W RMS | Cone: UTAG (Ultra Thin Acoustic Glass) | Freq: Fs–40,000 Hz
- **Source:** https://www.soundimports.eu/en/markaudio-alpair-5g.html | Price: €64.95 | Stock: OOS
- Note: Glass cone for improved transients. 7W RMS still insufficient for this system.

### HiVi Swan M4N — Catalogue
- Role: **MID** | Size: 4" | Imp: 8Ω | Sensitivity: 82 dB | Power: 15W RMS / 30W max | Fs: 69 Hz | Cone: Al/Mg alloy | VC: 22mm CCA | Frame: stamped steel, shielded
- **Source:** https://www.soundimports.eu/en/hivi-m4n.html | Price: €19.95 | Stock: 10+
- Note: Very low 82 dB sensitivity. 15W low power. Fs 69 Hz → 2.17× at 150 Hz. Magnetically shielded.

### HiVi Swan M4N-B — Catalogue
- Role: **MID** | Size: 4" | Imp: 8Ω | Power: 15W RMS | Fs: 69 Hz | Qts: 1.08 | Vas: 4.3 L | Xmax: 3mm | Re: 6.5Ω | Cone: Al/Mg alloy
- **Source:** https://www.soundimports.eu/en/hivi-m4n-b.html | Price: €22.45 | Stock: in stock
- Note: Qts 1.08 is very high — poorly damped, not suited for a sealed or vented mid chamber without careful tuning. Effectively same Fs as M4N but different damping. "Similar sound to B4N" per reviewers. 15W low.

### HiVi Swan M5N — Catalogue
- Role: **MID** | Size: 5" | Imp: 8Ω | Sensitivity: 87 dB | Power: 35W RMS / 70W max | Fs: 50 Hz | Xmax: 2.7mm | Cone: Al/Mg alloy | VC: 1"
- Symmetric Motor Drive (SMD) technology. Magnetically shielded.
- **Source:** https://www.soundimports.eu/en/hivi-m5n.html | Price: €29.95 | Stock: 10+
- Note: 87 dB near-matched to sub. Fs 50 Hz → 3.0× at 150 Hz (excellent). 5" Al/Mg — good beaming limit. 35W solid. Shielded.

### Dayton Audio DMA105-8 — Catalogue (10+ in stock)
- Role: **MID** | Size: 4" | Imp: 8Ω | Sensitivity: 84.8 dB | Power: 35W RMS | Fs: 72 Hz | Cone: rigid aluminum | Motor: dual neodymium magnet | Frame: 8-spoke open (aluminum)
- **Source:** https://www.soundimports.eu/en/dayton-audio-dma105-8.html | Price: €26.45 | Stock: 10+ (updated Jun 2026; previously pre-order)
- Note: Neodymium dual-magnet motor. 8-spoke open frame (circular). 84.8 dB sensitivity. Fs 72 Hz → 2.08× at 150 Hz (marginal; safer to cross at 200–250 Hz LP). 35W adequate. Now in stock — viable candidate.

### Visaton KT 100 V — Catalogue
- Role: **MID** | Size: 4" | Imp: 4Ω | Sensitivity: 83 dB | Power: 25W RMS / 40W max | Fs: 42 Hz | VC: 25mm | Freq: 32–9,500 Hz
- Rubber surround. Low-noise design. T-yoke.
- **Source:** https://www.soundimports.eu/en/visaton-kt-100-v.html | Price: €28.95 | Stock: 5
- Note: Fs 42 Hz is extraordinarily low for a 4" driver — this is a bass/woofer unit, not a midrange. Freq response ends at 9500 Hz; not usable above mid crossover. Would need crossover at 84 Hz (2×Fs). Very low sensitivity (83 dB). Designed for compact vented bass enclosures.

### Dayton Audio DA115-8 — Catalogue
- Role: **MID** | Size: 4" | Imp: 8Ω | Sensitivity: 84.9 dB | Power: 20W RMS / 40W max | Fs: 60 Hz | Cone: aluminum | Frame: cosmetic stamped steel | VC: 25mm
- **Source:** https://www.soundimports.eu/en/dayton-audio-da115-8.html | Price: €29.95 | Stock (**14 June 2026**): **3 units** (very low stock)
- Note: 84.9 dB close to sub reference. Fs 60 Hz → 2.5× at 150 Hz (solid). 20W modest. Aluminum cone (analytical character). 3 in stock.

### Monacor SPM-116/8 — Catalogue
- Role: **MID** | Size: 4" | Imp: 8Ω | Sensitivity: 87 dB | Power: 40W RMS / 80W max | Fs: 75 Hz | Cone: paper | Surround: rubber | Freq: 75–18,000 Hz
- **Source:** https://www.soundimports.eu/en/monacor-spm-116-8.html | Price: €21.45 | Stock: 8
- Note: 87 dB near-matched to sub. 40W solid. Fs 75 Hz → 2.0× at 150 Hz (adequate). Paper cone (warm character). Affordable at €21.45.

### FaitalPRO 4FE35-4F — Catalogue
- Role: **MID** | Size: 4" | Imp: 4Ω | Sensitivity: 91 dB | Power: 30W RMS / 60W max | Fs: 100 Hz | Qts: 0.73 | Vas: 2.4 L | Xmax: 1.73mm | VC: 19mm Al/Kapton | Frame: steel | Cutout: 91.5mm
- **Source:** https://www.soundimports.eu/en/faitalpro-4fe35-4f.html | Price: €26.95 | Stock: 10+
- Note: 91 dB very high sensitivity — needs ~6 dB DSP pad. Fs 100 Hz → 1.5× at 150 Hz (very tight). Xmax only 1.73mm — lowest of any 4" candidate. Pro audio / PA orientation.

### Beyma 4FR40 — Catalogue
- Role: **MID** | Size: 4" | Frame OD: 118.2mm | Imp: 8Ω | Sensitivity: 87 dB | Power: 40W AES / 80W program | Cone: paper | Surround: Santoprene | Frame: pressed steel, ceramic magnet | Freq: 100–20,000 Hz
- **Source:** https://www.soundimports.eu/en/beyma-4fr40.html | Price: €30.95 | Stock: 10+
- Note: 87 dB well-matched to sub. 40W solid. Paper cone and Santoprene surround (warm character). Full-range orientation (100–20kHz specified). OD 118.2mm wide.

### Monacor SP-4/60PRO — Catalogue
- Role: **MID** | Size: 4" | Frame: 113×113mm (square) | Imp: 8Ω | Sensitivity: 90 dB | Power: 30W RMS / 60W max | Fs: 92 Hz | Qts: 0.60 | Xmax: 2.3mm
- **Source:** SoundImports product page | Price: €29.95 | Stock: in stock
- Note: Square 113×113mm frame — not circular. Fs 92 Hz → 1.63× at 150 Hz (marginal). 90 dB well-matched. 30W adequate.

### Tang Band W4-655F — Catalogue
- Role: **MID** | Size: 4" | Frame OD: 125mm | Imp: 8Ω | Sensitivity: 89 dB | Power: 25W RMS / 50W max | Freq: 70–14,000 Hz | Xmax: 3mm
- Golden phase plug.
- **Source:** SoundImports product page | Price: €49.95 | Stock: in stock
- Note: Golden (brass-coloured) phase plug — distinctive visual. 89 dB near-matched to sub. 3mm Xmax adequate. 14 kHz upper limit suggests limited HF output above crossover; would need a tweeter ≤ 14 kHz.

### PRV Audio 4MR60-4 — Catalogue
- Role: **MID** | Size: 4" | Imp: 4Ω | Sensitivity: 90 dB | Power: 60W RMS | Freq: 90–15,000 Hz | Cone: fiberglass | VC: 20mm CCAW/Kapton | BL: 3.42 Tm | Moving mass: 4.32 g
- **Source:** https://www.soundimports.eu/en/prv-audio-4mr60-4.html | Price: €24.95 | Stock: 4
- Note: 90 dB well-matched. 60W power — highest of any 4" candidate. Fiberglass cone. Freq limited at 15 kHz. 4Ω: ~61W at 24V available. Pro audio / mid driver.

### PRV Audio 4MR60-NDY-4 — Catalogue
- Role: **MID** | Size: 4" | Imp: 4Ω | Sensitivity: 91 dB | Power: 60W RMS / 120W max | Freq: 90–20,000 Hz | Cone: fiberglass (glass fiber) | Motor: neodymium | Depth: 1.75" (shallow)
- **Source:** https://www.soundimports.eu/en/prv-audio-4mr60-ndy-4.html | Price: €49.95 | Stock: 10+
- Note: Neodymium version of 4MR60. 91 dB — needs ~6 dB DSP pad. 60W power. Shallow install depth. Freq 90–20kHz (could run full-range).

### Monacor MSH-115 — Catalogue
- Role: **MID** | Size: 4" | Imp: 8Ω | Sensitivity: 89 dB | Power: 50W RMS / 120W max | Fs: 85 Hz | Cone: paper coated ("special cone")
- **Source:** https://www.soundimports.eu/en/monacor-msh-115.html | Price: €66.95 | Stock: 9
- Note: 89 dB near-matched. 50W solid. Fs 85 Hz → 1.76× at 150 Hz (tight). Expensive at €66.95 for a 4" mid. "High-end technology" per Monacor. No Xmax stated.

### SB Acoustics SB12NRX25-4 — Catalogue
- Role: **MID** | Size: 4" | Imp: 4Ω | Sensitivity: 87.5 dB | Power: 30W RMS | Fs: 55 Hz | Xmax: 5mm | Cone: Norex (composition paper) | Surround: foam | VC: 1" | Freq: 100–2000 Hz (manufacturer spec)
- **Source:** SoundImports product page | Price: €59.95 | Stock: 8
- Note: 5mm Xmax — excellent. Fs 55 Hz → 2.72× at 150 Hz (matches DS115-8). Foam surround — less common in hi-fi, can age. Norex composite paper. Not recommended for reflex boxes (per SI).

### SB Acoustics SB12NRXF25-4 — Catalogue
- Role: **MID** | Size: 4" | Imp: 4Ω | Sensitivity: 87 dB | Power: 30W RMS | Fs: 61 Hz | Xmax: 5mm | Surround: foam | Freq: 100–2000 Hz | VC: 25.4mm
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb12nrxf25-4.html | Price: €62.45 | Stock: 6
- Note: Foam surround version with slightly higher Fs (61 Hz) than SB12NRX25-4. 5mm Xmax excellent. Foam surrounds can degrade over time. 5 stars from reviews — "gem in this class."

### SB Acoustics SB12MNRX25-4 — Catalogue
- Role: **MID** | Size: 4" | Imp: 4Ω | Sensitivity: 88.5 dB | Power: 30W RMS | Fs: 58 Hz | Xmax: 2.3mm | Cone: natural fibers | Surround: butyl rubber (high damping)
- **Source:** SoundImports product page | Price: €62.45 | Stock: in stock
- Note: High-damping surround for non-resonant character. 88.5 dB — needs −3.5 dB pad. Xmax only 2.3mm for a €62 driver.

### SB Acoustics SB12MNRX2-25-4 ✅ SELECTED — MID (the only 4" that matches the W5 output)
- Role: **MID** | Size: 4" Norex midrange | Imp: 4Ω | Re: 3.2Ω | Le: 0.15 mH | Sd: 50 cm² | VC: 25.4 mm | OD: 123 mm | Net wt: 0.92 kg | Shorting ring
- **Sensitivity: 90.5 dB @ 2.83V/1m** | **Power: 50W RMS** | **Fs: 63.5 Hz** | Qts 0.32 (Qms 4.19, Qes 0.35) | Mms 4.2 g | Bl 3.9 Tm | Vas 5.3 L | Cms 1.5 mm/N | **Xmax: ±2.2 mm (4.4 mm p-p linear travel)**
- **Source (verified):** [SB datasheet](https://sbacoustics.com/wp-content/uploads/2021/03/4in-SB12MNRX2-25-4.pdf) + [product page](https://sbacoustics.com/product/4-sb12mnrx2-25-4-norex/) (owner-confirmed Jun 2026); local `research/speakers/sb12mnrx2.pdf` | [SoundImports](https://www.soundimports.eu/en/sb-acoustics-sb12mnrx2-25-4.html) €61.95, 10+
- **Why selected — output match to W5-1138SMF (the governing requirement):** W5 sets the system ceiling at **98 dB @40W RMS / 101 dB @80W burst**. Max SPL = sens + 10·log₁₀(P/2W, 4Ω) = 90.5 + 10·log₁₀(25) = **104.5 dB** → matches the 101 dB burst with **+3.5 dB margin**. It is the **only 4" mid that reaches the burst** — PFCR25-4 and NRX25-4 (both 87.5 dB / 30 W) are power-limited at **99.3 dB (−1.7 dB short)**; B4N (85/25) at 99.0. MNRX2 matches via sensitivity + power, not excursion.
- **Xmax caveat:** ±2.2 mm is modest, but adequate for a mid crossed at 150 Hz — excursion-limited SPL at 150 Hz ≈ 105 dB (> 101). Relies on a clean 150 Hz handoff to the sub (no lower).
- **Crossovers:** to sub at 150 Hz → Fs 63.5 = **2.36× margin** (≥2× ✓). To tweeter: beams ~2,730 Hz (Sd 50) → clean handoff at 2 kHz. DSP pad −5.5 dB vs 85 dB sub.
- **Corrects prior errors:** earlier catalogue figures (91 dB / Fs 58 / Xmax 4.4 one-way / Qts 0.27 / Vas 6.3) were wrong — superseded by the verified datasheet values above.

### SB Acoustics SB12PFC25-4 — Catalogue (OOS or same as PFCR25-4)
- Role: **MID** | Size: 4" | Imp: 4Ω | Sensitivity: 87.5 dB | Power: 30W RMS | Fs: 58 Hz | Xmax: 5mm | Qts: 0.43 | Vas: 5.1 L | Cone: natural fiber paper | Surround: butyl rubber | VC: 1"
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb12pfc25-4.html | Price: listed (status unclear)
- Note: Near-identical specs to SB12PFCR25-4 already in this catalogue. May be an older designation for the same driver. If in stock, effectively interchangeable with PFCR25-4.

### SB Acoustics SB12PAC25-4 — Catalogue (OOS)
- Role: **MID** | Size: 4" | Imp: 4Ω | Sensitivity: 87 dB | Power: 30W RMS | Fs: 52.5 Hz | Xmax: 5mm | Qts: 0.31 | Cone: aluminum | OD: 108.9mm
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb12pac25-4.html | Price: listed | Stock: OOS
- Note: Similar specs to SB12PACR25-4 (same Fs, Xmax, Qts). May be older designation. OD 108.9mm slightly smaller than Willy's HiFi PACR (122mm) — different chassis sourcing or model revision.

### Peerless by Tymphany HDS-P830870 — Catalogue (pre-order)
- Role: **MID** | Size: 4" | Imp: 8Ω | Price: €49.95 | Stock: pre-order
- **Source:** https://www.soundimports.eu/en/peerless-by-tymphany-hds-p830870.html
- Note: Specs not retrieved (URL returned 404 on direct fetch; confirmed via search). Pre-order only.

### Visaton WS 13 E — Catalogue
- Role: **MID** | Size: 5" | Imp: 8Ω | Sensitivity: 86 dB | Power: 40W RMS / 60W max | Fs: 83 Hz | Xmax: 0.75mm | Vas: 7.4 L | Cone: paper | Freq: 83–12,000 Hz
- **Source:** SoundImports product page | Price: €21.95 | Stock: 9
- Note: 5" paper cone with very low Xmax (0.75mm). Fs 83 Hz → 1.81× at 150 Hz. Designed for small multimedia enclosures. Budget-friendly at €21.95. Xmax 0.75mm will limit maximum SPL near crossover.

### Visaton SC 13 — Catalogue
- Role: **MID** | Size: 5" | Frame OD: 162mm | Imp: 8Ω | Sensitivity: 90 dB | Power: 40W RMS / 60W max | Fs: 78 Hz | Xmax: 0.75mm | Vas: 7.4 L | Cone: cellulose | VC: 20mm | BL: 4.2 Tm | Depth: 62mm
- Magnetically shielded.
- **Source:** https://www.soundimports.eu/en/visaton-sc-13.html | Price: €32.95 | Stock: 8
- Note: 90 dB well-matched to sub. Large 162mm OD — would dominate a 190mm baffle. Xmax only 0.75mm (same concern as WS 13 E). Shielded. Good Fs (78 Hz → 1.92× at 150 Hz). Cellulose cone.

### Markaudio CHN-70 — Catalogue
- Role: **MID** | Size: ~5" | Imp: 8Ω | Sensitivity: 86.7 dB | Power: 16W RMS / 50W max | Fs: 71.6 Hz | Xmax: 4mm | Cone: paper | Freq: ~70–20,000 Hz
- Full-range driver.
- **Source:** SoundImports product page | Price: €32.45 | Stock: 4
- Note: Full-range. 16W RMS is low but 50W max suggests thermal limit is 50W. 4mm Xmax solid for a 5". Fs 71.6 Hz → 2.1× at 150 Hz. Only 4 in stock.

### SB Acoustics SB13PFC25-8 — Catalogue
- Role: **MID** | Size: 5" | Imp: 8Ω | Sensitivity: 87 dB | Power: 40W RMS | Fs: 45 Hz | Cone: natural fiber paper | VC: 1"
- **Source:** SoundImports product page | Price: €28.45 | Stock: 7
- Note: Fs 45 Hz → 3.33× at 150 Hz (excellent Fs margin). 87 dB near-matched. 40W solid. 8Ω: ~31W at 24V available — just within rating. Consider 29V supply for thermal headroom.

### SB Acoustics SB13PFC25-4 — Catalogue
- Role: **MID** | Size: 5" | Imp: 4Ω | Sensitivity: 89 dB | Power: 40W RMS | Fs: 44 Hz | Xmax: 4.5mm | Qts: 0.29 | Vas: 0.47 ft³ (13.3 L) | Cone: natural fiber paper (proprietary in-house)
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb13pfc25-4.html | Price: listed | Stock: see SoundImports
- Note: 4Ω version — 61W at 24V available (massive headroom). 89 dB well-matched. Fs 44 Hz → 3.41× at 150 Hz. Low Qts (0.29) suits active DSP crossover well. Xmax 4.5mm excellent. Note: this is probably the same as the SB13PFCR25-4 already listed (model number cross-check needed).

### Dayton Audio RS75T-8 — Catalogue
- Role: **MID** | Size: 3" | Frame: truncated cast (not fully circular) | Imp: 8Ω | Sensitivity: 84.3 dB | Power: 15W RMS / 30W max | Fs: 189 Hz | Cone: black anodized aluminum
- **Source:** SoundImports product page | Price: €49.95 | Stock: 6
- Note: Fs 189 Hz is extremely high → min xover 378 Hz. Suitable only as a dedicated midrange starting above 400 Hz — not a typical mid-woofer. Black anodized aluminum cone. Truncated cast frame. 15W modest. Reference Series quality.

### Dayton Audio RS125-4 — Catalogue
- Role: **MID** | Size: 5" | Frame: cast aluminum (6 mounting holes) | Imp: 4Ω | Sensitivity: 89.9 dB | Power: 30W RMS | Fs: 57.2 Hz | Xmax: 4mm | Cone: aluminum | Freq: 65–5,400 Hz
- Two short-circuit paths in motor. Rubber surround.
- **Source:** https://www.soundimports.eu/en/dayton-audio-rs125-4.html | Price: €66.95 | Stock: 10+
- Note: Reference Series aluminum cone. 89.9 dB near-perfect match. Fs 57.2 Hz → 2.62× at 150 Hz. 4mm Xmax. Cast aluminum frame (cast frames are typically circular). Premium price at €66.95.

### Dayton Audio RS125P-4 — Catalogue
- Role: **MID** | Size: 5" | Frame: cast (6 holes) | Imp: 4Ω | Sensitivity: 90 dB | Power: 30W RMS / 45W max | Fs: 70 Hz | Cone: paper/Kevlar/glass composite | VC: 25mm Cu/Al | Phase plug: solid aluminum
- **Source:** https://www.soundimports.eu/en/dayton-audio-rs125p-4.html | Price: €64.95 | Stock: 9
- Note: Proprietary composite paper cone. Aluminum phase plug (may be silver-coloured). 90 dB near-perfect. Fs 70 Hz → 2.14× at 150 Hz. Reviewer noted lack of dust cover makes it unsuitable for non-downfiring applications.

ions.

tions.

ions.

s.

