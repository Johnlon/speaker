# Driver Catalogue

Per-driver analysis: derived figures, power checks, DSP correction, decisions. Raw specs are in `research/si_tweeter_index.md` and `research/si_woofer_index.md`.

One entry per driver. Status: **Locked** / **Candidate** / **Rejected**.

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
- Size: 5.25" | Frame OD: 133.3 mm (6.14" OD) | Impedance: 4Ω
- Sensitivity: **85 dB @ 2.83V/1m** | Xmax: 9.25 mm | Power: 40W RMS / 80W max
- Fs: 45 Hz | Qts: 0.49 | Vas: 0.17 ft³ (4.81 L) | Sd: 94 cm² | Re: 3.4Ω
- Frequency range: 45–1,500 Hz | Sealed F3: 73 Hz | Vented F3: 35 Hz
- Surround sits ~8.5 mm proud of baffle when surface-mounted → reclaims ~160 mL internal volume
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/tang-band-w5-1138smf.html) (specs fetched June 2026)
- **Datasheet:** [research/tang_band_w5-1138smf.pdf](research/tang_band_w5-1138smf.pdf) | [original URL](https://www.tb-speaker.com/uploads/files/cadcecac0ea8af7e07014e520d4ea00d.pdf)
- SoundImports price: €54.95 | Stock (June 2026): 10+
- **Why locked:** Class-leading excursion for its size; round frame; dark/stealth motor. This is the performance anchor — all other driver choices are judged against its output capability.

---

## Passive Radiator

### SB Acoustics SB15SFCR-00 5×8" Racetrack — Candidate
- Shape: Oval racetrack | Sd ≈ 178 cm² (~2.05× the TB sub's Sd)
- Mounts vertically on side or rear panel
- Requires added mass to rear M6-threaded bolt to lower native tuning to 38 Hz
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/sb-acoustics-sb15sfcr-00.html) — fetch for confirmed Sd and mass range
- **Why liked:** Narrow profile fits on a slim cabinet side wall while providing sufficient Sd to couple correctly with the TB sub's 9.25 mm Xmax. Preferred for Option A (side-sub) layout.
- **Limitation:** Oval shape only suits Option A (side panels). Not an aesthetic fit for front-baffle layouts where circles are the theme.

### Dayton Audio ND140-PR — Candidate (dual-side configuration only)
- Shape: Round | Nominal diameter: 5.25" | **Confirmed Sd: 86.6 cm²** (single unit)
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

### Peerless by Tymphany XT25BG60-04 — Candidate (ring radiator — best power match of the XT25 family)
- Type: **Ring radiator**, fabric diaphragm | VC: 25 mm | Faceplate OD: **104.5 mm** | Cutout: 73 mm | Depth: 67 mm | Impedance: 4Ω
- Sensitivity: **92.6 dB @ 2.83V/1m** | Power: **15W RMS** | Fs: **570 Hz** | Frequency response: flat well beyond 20 kHz
- Ferrite magnet | Rear chamber | Patented dual concentric diaphragm with waveguide
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/peerless-by-tymphany-xt25bg60-04.html) (fetched June 2026)
- **Datasheet:** download to research/ on order (doc.soundimports.nl pattern)
- SoundImports price: **€41.28** (10+ in stock) | June 2026
- **DSP correction vs TB sub (85 dB ref):** −7.6 dB pad needed.
- **Power at reference:** 98 dB from 92.6 dB → needs **6.9W** RMS (46% of 15W ✓) | burst 101 dB → **13.8W** (92% of 15W — within rating, just) | DSP limiter at 14W gives small margin.
- **Why this is the best-matched ring radiator for this system:** At burst (101 dB), needs 13.8W vs 15W rating — stays within spec (just). The XT25TG30-04 (91.9 dB, also 15W) needs 16.3W at burst — over rated power. The XT25BG60-04's 0.7 dB higher sensitivity is the critical difference. Fs 570 Hz → min xover 1,140 Hz — more crossover flexibility than XT25SC90-04 (1,650 Hz) while staying within 15W at burst, unlike XT25TG30-04.
- **Off-axis:** Same ring radiator off-axis advantage as all XT25 series — wide controlled dispersion, directly relevant to 40–50° kitchen position.
- **Concern:** 104.5 mm OD is large. Centre spacing with any standard 4" mid: (mid_OD + 104.5)/2.

### Peerless by Tymphany XT19TD00-04 — Candidate (¾" ring radiator — smallest face)
- Type: **Ring radiator**, dual diaphragm | VC: 19 mm | Faceplate OD: **94 mm** | Cutout: 68 mm | Depth: 44 mm | Impedance: 4Ω
- Sensitivity: **88.9 dB @ 2.83V/1m** | Power: **20W RMS** | Frequency response: 800–20,000 Hz
- Copper-clad aluminium voice coil | Patented ring radiator + waveguide | 5-star reviews (×4)
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/peerless-by-tymphany-xt19td00-04.html) (fetched June 2026)
- SoundImports price: **€28.88** (10+ in stock) | June 2026
- **DSP correction vs TB sub (85 dB ref):** −3.9 dB pad needed.
- **Power at reference:** 98 dB from 88.9 dB → needs **16.2W** RMS (81% of 20W — fine ✓) | burst 101 dB → **32.3W** (exceeds 20W — DSP limiter mandatory at ≤19W, max tweeter SPL 98.9 dB)
- **Why smaller matters:** 94 mm OD vs 104 mm for the XT25 family → 5 mm smaller radius → tighter centre spacing with any mid. With DSA90-8 (92 mm OD): spacing = 93 mm. Smallest round tweeter face in the field (SB19ST is 88 mm, this is 94 mm — close).
- **Off-axis:** ¾" ring radiator — smaller annular element may give slightly different (wider?) directivity than 1" XT25 units at high frequency.
- **Concern — power:** Sensitivity 88.9 dB is the lowest of the ring radiator family. At reference level it draws 81% of its power rating — less headroom than the BG60 or TG30. DSP limiter at 19W caps SPL at 98.9 dB, 2.1 dB below sub burst ceiling. Acceptable.
- **Concern — colour:** Not confirmed.

### Peerless by Tymphany XT25TG30-04 — Candidate (ring radiator — lowest Fs of all tweeter candidates)
- Type: **Ring radiator** (dual concentric diaphragm, central waveguide) | VC: 25 mm | Faceplate OD: **104 mm** | Cutout: 73 mm | Depth: 51.7 mm | Impedance: 4Ω
- Sensitivity: **91.9 dB @ 2.83V/1m** | Power: **15W RMS** | Fs: **440 Hz** | Re: 3.1Ω | Frequency response: 800–20,000 Hz
- Qts: 0.44 | Le: 0.009 mH | Ferrite magnet | Rear chamber | No ferrofluid
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/peerless-by-tymphany-xt25tg30-04.html) (specs fetched June 2026)
- **Datasheet:** [original URL](https://doc.soundimports.nl/pdf/brands/Peerless%20by%20Tymphany/XT25TG30-04/XT25TG30-04.pdf) — download to research/ on order
- SoundImports price: €49.95 (**10+ in stock**, Jun 2026) | Falcon Acoustics price: **£29.90** (in stock, UK) | Falcon is ~£13 cheaper
- **DSP correction vs TB sub (85 dB ref):** −6.9 dB pad needed.
- **Power at reference:** 98 dB from 91.9 dB driver → needs 8.2W RMS (54% of 15W rating ✓) | burst 101 dB → 16.3W (exceeds rating — see below)
- **DSP limiter:** Set tweeter channel at 13W → maximum tweeter SPL = 91.9 + 10×log(13/2) = **100.0 dB**. Sub peaks at 101 dB. 1 dB gap at burst, irrelevant in practice (bass transients, not treble).
- **Why this is the standout tweeter find:** Fs 440 Hz is the lowest of **any tweeter candidate in this project**. Minimum crossover: **880 Hz**. This means the XT25TG30-04 is compatible with every mid driver in the field including the large 5"+ drivers (SIG150-4, SDS-P830656, SB13PFCR25-4) that beam early and need a crossover at or below 2,000 Hz. No other tweeter in the field can open that range of crossover positions.
- **Off-axis advantage:** Ring radiators have inherently wide, controlled dispersion because the annular ring radiates energy at larger off-axis angles than an equivalent dome. Directly relevant to the 40–50° kitchen listening geometry.
- **Concern — power:** 15W rating is the same as DX25TG59-04 but sensitivity is 1.5 dB lower, so it needs more power for the same SPL. DSP limiter at 13W is essential. DX25TG59-04 has more headroom at the same rating because of its higher sensitivity.
- **Concern — faceplate size:** 104 mm OD is the widest tweeter in the candidate field. Same as DX25TG59-04 and D27TG35-06. Cabinet baffle must be at least 190 mm wide to fit alongside any standard 4" mid.

### Peerless by Tymphany XT25SC90-04 — Candidate (ring radiator)
- Type: **Ring radiator** (dual concentric diaphragm, central waveguide) | VC: 25 mm | Faceplate OD: ~90 mm | Impedance: 4Ω
- Sensitivity: **90.1 dB @ 2.83V/1m** | Power: **100W RMS** | Fs: **825 Hz** | Re: 3.2Ω
- Qts: 0.93 | Qes: 1.007 | Qms: 7.2 | No ferrofluid | Rear chamber
- **Source:** Falcon Acoustics product page (fetched June 2026)
- Falcon Acoustics price: **£18.20** (in stock, UK) | SoundImports: not confirmed | June 2026
- **DSP correction vs TB sub (85 dB ref):** −5.1 dB pad needed.
- **Power at reference:** 98 dB → 12.3W (12.3% of 100W ✓) | burst 101 dB → 24.5W (24.5% ✓). Large power headroom.
- **Why liked:** Fs 825 Hz → minimum crossover 1,650 Hz — works with all mid drivers. 100W power rating is the most robust of any tweeter in the field. £18.20 is the second cheapest tweeter after ND20FA-6. Ring radiator off-axis characteristics similar to XT25TG30-04.
- **Vs XT25TG30-04:** Higher power headroom (100W vs 15W). Lower Fs flexibility (1,650 Hz vs 880 Hz min xover). Lower sensitivity (90.1 vs 91.9 dB). Cheaper (£18.20 vs £29.90). For mid/tweeter windows above 1,650 Hz (all standard 4" mids), the SC90 is perfectly adequate and £11.70 cheaper.

### SB Acoustics SB19ST-C000-4 — Candidate (top-ranked)
- Dome: 19 mm textile | Faceplate OD: 88 mm round | Impedance: 4Ω
- Sensitivity: 88.5 dB @ 2.83V/1m | Power: 30W RMS | Fs: 980 Hz | Re: 3.4Ω | Xmax: 0.6 mm | Sd: 3.8 cm²
- Qts: 1.22 | Qes: 1.50 | Qms: 6.45 | BL: 1.75 Tm | Mms: 0.22 g
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/sb-acoustics-sb19st-c000-4.html) (specs fetched June 2026)
- **Datasheet:** [research/sb_acoustics_sb19st-c000-4.pdf](research/sb_acoustics_sb19st-c000-4.pdf) | [original URL](https://sbacoustics.com/wp-content/uploads/2020/05/SB19ST-C000-4.pdf)
- SoundImports price: €21.45 | Stock (June 2026): 10+
- **DSP correction vs TB sub (85 dB ref):** −3.5 dB pad needed (tweeter is 3.5 dB above sub reference)
- **Why liked:** Smallest dome of all candidates → widest horizontal dispersion furthest into HF → best performance at 60° off-axis kitchen position. Fabric dome = warm, natural character matching GHM tonal preference. Sensitivity at 88.5 dB means tweeter power budget is comfortable — needs 17.8W at 4Ω to match sub at full volume; well within 30W rating. Round 88 mm faceplate passes circular rule. Surface-mountable.

### SB Acoustics SB26ADC-C000-4 — Candidate
- Dome: 26 mm aluminium (copper cap) | Faceplate OD: ~104 mm round (not confirmed — SB26 series typical) | Impedance: 4Ω
- Sensitivity: 90 dB @ 2.83V/1m | Power: 120W RMS | Fs: 680 Hz | Re: 3.2Ω | Xmax: 0.6 mm | Sd: 6.2 cm²
- Qts: 1.20 | Qes: 2.0 | Qms: 2.9 | Mms: 0.38 g
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/sb-acoustics-sb26adc-c000-4.html) (specs fetched June 2026)
- SoundImports price: €52.45 | Stock (June 2026): 10+
- **DSP correction vs TB sub (85 dB ref):** −5.0 dB pad needed
- **What's good:** 120W RMS — effectively indestructible. Fs 680 Hz → min crossover 1,360 Hz.
- **Concern:** Aluminium dome sounds brighter/harder than the warm fabric character this project targets. At €52.45 it takes most of the £75 budget, leaving little for the mid.

### HiVi TN25 — Candidate (owner-accepted visual)
- Dome: 25 mm fabric | Faceplate: 54.1 × 54.1 mm square (2.13") | Impedance: 5Ω | Re: 4.6Ω
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
- Dome: 25 mm soft dome (neodymium) | Faceplate OD: 66 mm (2.60") round | Impedance: 4Ω
- Sensitivity: 90 dB | Power: 20W RMS | Fs: 1350 Hz | Qts: 1.56 | Qes: 2.61 | Qms: 3.87
- Re: 3.20Ω | Le: 0.48 mH | Cutout: 45 mm | Depth: 25 mm
- Supplier: [SoundImports](https://www.soundimports.eu/en/dayton-audio-nd25fa-4.html) | Price: €15.95 | Stock: 10+
- **Why liked:** Compact round faceplate (66 mm OD) — smallest footprint of any candidate tweeter. 90 dB sensitivity exceeds the 85 dB sub reference and is only 1.5 dB below the SB19ST. Neodymium motor for tight, efficient operation. Budget-friendly at €15.95. Fs 1350 Hz gives comfortable room below target crossovers.
- **Concern:** Dome colour not confirmed from product page text — likely dark/black based on neodymium compact design. Power at 20W RMS is modest (same as SB19ST-C000-4). Qts 1.56 is high; needs to be used above its Fs by a comfortable margin, which is met at target crossovers. **Recommend confirming dome colour before ordering.**
- **Note:** Dome colour could not be confirmed from web content; manufacturer datasheet confirms it as a black soft dome. Sensitivity at 2.83V/1m is 90 dB.
- **Source:** https://www.soundimports.eu/en/dayton-audio-nd25fa-4.html (fetched June 2026)

### Peerless by Tymphany BC25SC06-04 — Candidate
- Dome: 25 mm textile | Faceplate OD: ~70 mm (2.75") round | Impedance: 4Ω
- Sensitivity: 95.4 dB | Power: 50W RMS | Fs: 1350 Hz | Qts: 1.26
- Cutout: ~43 mm | Depth: ~32 mm
- Supplier: [SoundImports](https://www.soundimports.eu/en/peerless-by-tymphany-bc25sc06-04.html) | Price: €24.95 | Stock: 10+
- **Why liked:** 50W RMS power — highest power handling of any candidate tweeter in budget. Circular faceplate confirmed. 95.4 dB sensitivity is very high — means significant DSP attenuation (~7–10 dB) would be needed to match the 85 dB sub, which is straightforward with the JAB5. Includes finned heat sink for thermal management.
- **Concern:** 95.4 dB sensitivity requires large DSP attenuation vs the 85 dB sub. Dome colour not confirmed from page text.
- **Source:** https://www.soundimports.eu/en/peerless-by-tymphany-bc25sc06-04.html (fetched June 2026)

### SB Acoustics SB26STCN-C000-4 — Candidate
- Dome: 25 mm fine weave soft fabric | Faceplate OD: 72 mm round | Impedance: 4Ω
- Sensitivity: 92 dB | Power: 120W RMS | Fs: 950 Hz | Re: 3.2Ω | Le: 0.04 mH
- Supplier: [SoundImports](https://www.soundimports.eu/en/sb-acoustics-sb26stcn-c000-4.html) | Price: €36.45 | Stock: 10+
- **Why liked:** Massive 120W RMS power handling — effectively indestructible in this application. Fs 950 Hz gives good margin below target crossovers. Soft fabric dome offers warm character similar to SB19ST. Neodymium magnet. Internal pressure equalisation. 72 mm faceplate is compact and confirmed circular.
- **Concern:** At €36.45 it leaves only ~£32 for the midrange if paired with this tweeter. Dome colour not confirmed from page text — likely dark fabric. Sensitivity at 92 dB is 7 dB above sub; needs DSP attenuation.
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb26stcn-c000-4.html (fetched June 2026)

### Dayton Audio RST28F-4 — Candidate (owner-accepted)
- Dome: 28 mm (1-1/8") silk | Faceplate OD: 4.125" (~105 mm) | Cutout: 2.875" (~73 mm) | Depth: 1.75" (~44 mm) | Impedance: 4Ω
- Sensitivity: 93.5 dB @ 2.83V/1m | Power: 80W RMS | Frequency response: 1,400–20,000 Hz
- Fs: 710 Hz | Re: 3Ω | Le: 0.03 mH | Qts: 0.92 | Qes: 1.46 | Qms: 2.52
- **Dome size note:** SoundImports page lists "25 mm (1")" but the product name RST28F indicates 28 mm (1-1/8"). Likely a SoundImports data entry error. The 28mm figure from the product name is trusted pending PDF confirmation.
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/dayton-audio-rst28f-4.html) (specs fetched June 2026)
- **Datasheet:** [research/dayton_audio_rst28f-4.pdf](research/dayton_audio_rst28f-4.pdf) | [original URL](https://doc.soundimports.nl/pdf/brands/Dayton%20Audio/RST28F-4/pdf_Dayton%20Audio_RST28F-4_1.pdf) (image-based PDF, downloaded June 2026)
- SoundImports price: €46.95 | Stock: 10+
- **Why considered:** 80W RMS is the highest power rating in the tweeter field by far — effectively indestructible. Fs 710 Hz → min crossover 1,420 Hz. Very high sensitivity at 93.5 dB means only 5.6W needed to match reference — amp is virtually always loafing.
- **DSP correction vs TB sub (85 dB ref):** −8.5 dB pad needed. Large attenuation, but the JAB5 handles this in DSP without issue.
- **Trade-off — dome size:** 28 mm dome is wider than the ≤19 mm ideal stated in REQUIREMENTS.md. Wider dome = narrower dispersion above ~6 kHz. At the 60° kitchen position, output above 8–10 kHz may be 3–6 dB lower than on-axis compared to a 19 mm dome. The practical impact is on air and presence rather than tone.
- **Trade-off — price:** €46.95 leaves ~£28 for the midrange within the combined £75 budget. Workable with DS115-8 (€36.95 + €46.95 = €83.90 ≈ £72) or HiVi B4N (€22.45 + €46.95 = €69.40 ≈ £60).

### Peerless by Tymphany DX25TG59-04 — Candidate (reinstated)
- Dome: 25 mm silk (damped, ferrofluid-cooled VC) | Faceplate OD: 104 mm | Cutout: 74 mm | Depth: 33 mm | Impedance: 4Ω
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
- Dome: 25 mm silk | Faceplate OD: 66 mm (integral waveguide) | Impedance: 8Ω
- Sensitivity: 95 dB @ 2.83V/1m | Power: 40W RMS / 80W max | Fs: 1600 Hz | Frequency response: 1,600–20,000 Hz
- Supplier: [SoundImports](https://www.soundimports.eu/en/monacor-dt-25n.html) | Price: €29.95 | Stock: 10+
- **DSP correction vs TB sub (85 dB ref):** −10 dB pad needed.
- **Note:** Fs 1600 Hz means crossover should be at least 3,200 Hz (2× Fs). Response starts at 1,600 Hz. Waveguide narrows dispersion — affects 60° off-axis position. Needs high-Fs-tolerant crossover point. 8Ω on JAB5 tweeter channel: ~31W available at 24V; needs ~3.2W at reference — no power concern.

### Peerless by Tymphany D27TG35-06 — Candidate (reinstated)
- Dome: 25 mm silk | Faceplate OD: 104 mm | Impedance: 6Ω
- Sensitivity: 91.8 dB | Power: 15W RMS | Fs: 900 Hz
- Supplier: [SoundImports](https://www.soundimports.eu/en/peerless-by-tymphany-d27tg35-06.html) | Price: €39.95 | Stock: 10+
- **Power at reference:** At woofer max (80W), tweeter needs 11.1W — within 15W rating with 35% headroom.
- **DSP correction vs TB sub (85 dB ref):** −6.8 dB pad needed.
- **Note:** 6Ω impedance — JAB5 is rated into 6Ω (its specified load), so this is fine. ~41W available at 24V, well above the 11.1W needed.
- **Concern:** Dome colour unconfirmed. Faceplate 104 mm is large (same as DX25TG59-04). Fetch datasheet to confirm colour before ordering.

### Peerless by Tymphany NE25VTS-04 — Candidate (compact faceplate)
- Dome: 25 mm silk (neodymium, copper cap) | Faceplate OD: **66.3 mm** | Impedance: 4Ω
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
- Dome: 19 mm silk (neodymium, copper cap) | Faceplate OD: **52 mm** | Cutout: 38 mm | Depth: 35.5 mm | Impedance: 4Ω
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
- Dome: 29 mm cloth (textile, dark) | Faceplate OD: **72 mm** | Impedance: 4Ω
- Sensitivity: **95.5 dB @ 2.83V/1m** | Power: **80W RMS** | Fs: **630 Hz** | Sd: 9.6 cm²
- Neodymium motor | Re: 3.0Ω | VC diameter: 29 mm
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/sb-acoustics-sb29sdnc-c000-4-tweeter) | [SB Acoustics product page](https://sbacoustics.com/product/sb29sdnc-c000-4-fabric/)
- Willys-Hifi price: **£56.64** (UK, in stock June 2026)
- **DSP correction vs TB sub (85 dB ref):** −10.5 dB pad needed.
- **Power at reference:** 98 dB → 3.6W (4.5% of 80W) | burst 101 dB → 7.1W (8.9% ✓). Effectively indestructible at project SPL levels.
- **PSU:** 24V / 28V (sub-limited; tweeter barely loaded).
- **Why considered:** 72mm FP is compact (same as SB26STCN). Fs 630 Hz → min xover 1,260 Hz — second widest crossover window of any cloth dome candidate. 80W rating gives enormous headroom. Cloth dome = warm character.
- **Vs SB26STCN-C000-4:** Both 72mm FP. SB29SDNC: 95.5 dB (3.5 dB more sensitive), 80W vs 120W, Fs 630 vs 950 Hz (better margin), 29mm dome vs 25mm (narrower dispersion), £56.64 vs ~£31 (significantly more expensive). Use SB29SDNC only if the lower Fs crossover flexibility justifies the cost.
- **Concern:** 29mm dome is wider than the ≤19mm ideal for off-axis dispersion. At 60° kitchen position, output above 8–10 kHz is slightly lower than a 19–25mm dome. Same concern as RST28F-4.

### Morel MDT12 — Candidate (compact FP, ultra-shallow, Willys-Hifi)
- Dome: 28 mm (1-1/8") textile (dark) | Faceplate OD: **54 mm** | Impedance: 8Ω
- Sensitivity: **89 dB @ 2.83V/1m** | Power: **80W RMS** | Fs: **1,000 Hz** | Depth: **19 mm**
- Neodymium motor | Chamberless design | Frequency response: 1,800–25,000 Hz
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/morel-mdt12-soft-dome-tweeter) | [SoundImports](https://www.soundimports.eu/en/morel-mdt-12.html)
- Willys-Hifi price: **£39.50** (UK, in stock June 2026)
- **DSP correction vs TB sub (85 dB ref):** −4.0 dB pad needed.
- **Power at reference (8Ω):** 98 dB → 7.9W (10% of 80W ✓) | burst 101 dB → 15.9W (20% ✓). Large headroom.
- **Available @ 24V into 8Ω:** ~31W. 31W >> 15.9W needed ✓.
- **PSU:** 24V / 28V (sub-limited).
- **Why considered:** 54mm FP is the 3rd most compact dome in the field (after NE19VTS-04 at 52mm and XT25SC40-04 ring rad at 43.9mm). Extremely shallow at 19mm depth — barely protrudes from baffle. 80W with chamberless design keeps rear volume minimal. 8Ω = lower current draw.
- **Concern:** 28mm dome → same off-axis dispersion concern as RST28F-4. Fs 1,000 Hz → min xover 2,000 Hz. Response specified from 1,800 Hz — per-pairing window in combos.md.

### Dayton Audio ND20FA-6 — Candidate
- Dome: 19 mm soft dome | Faceplate OD: 45 mm | Impedance: 6Ω
- Sensitivity: 91.5 dB @ 2.83V/1m | Power: 15W RMS | Fs: 2005 Hz | Frequency response: 2,000–20,000 Hz
- Supplier: [SoundImports](https://www.soundimports.eu/en/dayton-audio-nd20fa-6.html) | Price: €14.95 | Stock: 10+
- **DSP correction vs TB sub (85 dB ref):** −6.5 dB pad needed.
- **Note:** Fs 2005 Hz means crossover must be at least 4,000 Hz (2× Fs) — the highest crossover of any tweeter candidate. Limits mid driver choice to those that extend cleanly to 4 kHz+. 6Ω on JAB5: ~41W available at 24V; needs ~4W at reference — no power concern. 19mm dome — best off-axis of all candidates. Cheapest tweeter at €14.95.

### Scan-Speak Discovery D2606/920000 — Candidate
- Dome: 25 mm coated textile | Faceplate OD: not confirmed | Impedance: 6Ω
- Sensitivity: 91.4 dB @ 2.83V/1m | Power: 100W RMS / 200W max | Fs: 1100 Hz
- Supplier: [SoundImports](https://www.soundimports.eu/en/scan-speak-d2606-920000.html) | Price: €39.95 | Stock: 10+
- **DSP correction vs TB sub (85 dB ref):** −6.4 dB pad needed.
- **Note:** Scan-Speak quality — likely excellent. 6Ω: JAB5 at 24V delivers ~41W; needs ~5.6W at reference. €39.95 is the most expensive tweeter candidate — constrains mid budget if £75 total. Faceplate OD not confirmed — fetch before ordering.

### Dayton Audio DC25T-8 — Catalogue (visual constraints removed June 2026)
- Dome: 25 mm titanium | Impedance: 8Ω | Sensitivity: 93 dB | Power: 50W RMS | Fs: 1,468 Hz | Response: 3,000–20,000 Hz
- Supplier: [SoundImports](https://www.soundimports.eu/en/dayton-audio-dc25t-8.html) | Price: €18.97 | Stock: 10+
- Note: Titanium dome (silver metallic appearance). Precision phase lens. Previously visual-excluded — visual constraints removed June 2026. Remaining concern: Fs 1,468 Hz → min crossover 2,936 Hz is high; response starts at 3,000 Hz. €18.97 — budget-friendly.

### Peerless by Tymphany XT25SC40-04 — Candidate (ultra-compact ring radiator)
- Type: **Ring radiator** | VC: 25 mm | Faceplate OD: **43.9 mm** (smallest ring rad in field) | Impedance: 4Ω
- Sensitivity: **94 dB @ 2.83V/1m** | Power: **100W RMS** | Fs: **1,018 Hz** | Frequency response: to 20,000+ Hz
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/xt25sc40-04.html) (fetched June 2026)
- SoundImports price: **€29.95** | Stock (June 2026): 10+
- **Min crossover:** 2× Fs = **2,036 Hz**.
- **DSP correction vs TB sub (85 dB ref):** −9.0 dB pad needed (tweeter is 9 dB hotter than sub reference).
- **Power at reference (98 dB):** 10^((98−94)/10) = **2.5W** (2.5% of 100W — minimal draw). At burst (101 dB): **5.0W** (5% of 100W). 100W power rating is effectively indestructible in this application.
- **Why this matters — spacing:** 43.9 mm faceplate is the smallest tweeter OD in the entire field by a wide margin. With DSA90-8 (92 mm OD): centre spacing = (92 + 43.9) / 2 = **68 mm** — new project minimum (beats B6 at 73 mm AND is a ring radiator, not a square dome). Pairing XC1.
- **Ring radiator advantage:** Wide controlled off-axis dispersion — relevant to 60° kitchen geometry. Same advantage as XT25TG30-04 and XT25SC90-04 but in a dramatically smaller package.
- **Sensitivity mismatch:** 94 dB vs DSA90-8's 84.7 dB = 9.3 dB differential. The ADAU1701 DSP handles this comfortably; the tweeter channel simply receives 9 dB less gain. No audible artefact.
- **Concern — small diaphragm:** Ring element is smaller than XT25SC90-04 (90 mm FP). Verify polar plots if available. Very small annular ring at 43.9 mm may have narrower dispersion than the larger ring radiators above 10 kHz — but below 10 kHz all ring rads are wide. Kitchen use is dominated by lower treble (2.8–8 kHz) where dispersion should be fine.
- **vs XT25SC90-04:** SC40 has 43.9 mm FP vs SC90's ~90 mm. SC40 at 68 mm spacing beats SC90 at 91 mm. Both 100W rated. SC90 has lower Fs (825 Hz vs 1,018 Hz) — both give adequate headroom above min crossover for all standard 4" mids. SC40 costs same (€29.95 vs £18.20). SC40 wins on spacing; SC90 wins on Fs margin.

### SB Acoustics SB21SDC-C000-4 — Candidate (compact ring dome)
- Type: **Ring dome** (SB Acoustics ring construction, annular diaphragm) | Dome: 21 mm | Faceplate OD: **92 mm** | Impedance: 4Ω
- Sensitivity: **91 dB @ 2.83V/1m** | Power: **40W RMS** | Fs: **720 Hz** | Frequency response: to 20,000+ Hz
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/sb21sdc-c000-4.html) (fetched June 2026)
- SoundImports price: **€39.95** | Stock (June 2026): 1 unit + 7 expected 3-Jul-2026
- **Min crossover:** 2× Fs = **1,440 Hz** — excellent; same range as SB29SDAC's 1,200 Hz.
- **DSP correction vs TB sub (85 dB ref):** −6.0 dB pad needed.
- **Power at reference (98 dB):** 10^((98−91)/10) = **5.0W** (12.5% of 40W ✓). At burst (101 dB): **10.0W** (25% ✓). Excellent headroom.
- **Why interesting — cheaper ring dome:** SB29SDAC (S3/RR6 pairings) costs €44.95. SB21SDC costs €39.95 — €5 cheaper with similar ring dome construction. The SB21SDC has a 92 mm faceplate vs SB29SDAC's ~104 mm → tighter spacing. Fs 720 Hz vs SB29's 600 Hz → min xover 1,440 Hz vs 1,200 Hz — slightly tighter but still excellent.
- **New pairings enabled:** RD1 (DS115-8 + SB21SDC = 104 mm spacing, 1,440–2,636 Hz window, ~£49), RD2 (SB12PFCR25-4 + SB21SDC = 107 mm spacing, ~£40 — cheapest ring dome pairing in catalogue).
- **vs SB29SDAC:** SB21 is €5 cheaper, 92 mm vs 104 mm FP (tighter spacing), 21 mm vs 29 mm dome (slightly less diaphragm area). SB21 is the value ring dome; SB29 is the full engineering showcase.
- **Stock caveat:** Only 1 available now; 7 expected July 3. For pairing RD2 (~£40) this is the first ring dome option that doesn't break the £50 driver budget.

### Scan-Speak Discovery D2604/830000 — Candidate
- Dome: 26 mm textile | Faceplate OD: **104.2 mm** | Cutout: **75 mm** | Depth: **25.4 mm** | Impedance: 4Ω | Re: 2.8Ω
- Sensitivity: **92 dB @ 2.83V/1m** | Power: **100W RMS / 240W max** | Fs: **~630 Hz** (est. from Qts data; response starts 1,000 Hz) | Qts: 0.79 | Qms: 3.46 | Qes: 1.02
- **Source:** [SoundImports](https://www.soundimports.eu/en/scan-speak-d2604830000.html) (fetched June 2026; URL confirmed) | [Scan-Speak](https://www.scan-speak.dk/product/d2604-830000/)
- SoundImports price: **€44.95** | Stock (June 2026): 10+ (listed as pre-order at SI but in stock)
- **Min crossover:** 2× Fs ≈ **1,260 Hz** — excellent; same window class as SB29SDAC (1,200 Hz). Only XT25TG30-04 (880 Hz) goes lower among domes.
- **DSP correction vs TB sub (85 dB ref):** −7.0 dB pad needed.
- **Power at reference (98 dB):** 4.0W (4% of 100W). At burst (101 dB): 8.0W (8%). Effectively indestructible at 100W/240W rating.
- **Why interesting:** Scan-Speak Discovery class engineering in a 104mm faceplate with 100W power handling, Fs ~630 Hz, and widest crossover window of any dome in the candidate field. €44.95 mid-range price. 104mm OD — same footprint class as DX25TG59-04, SB29SDAC. Depth only 25.4mm (shallowest large-FP tweeter in the field).
- **Pairing note:** At 104.2mm FP, spacing with DS115-8 (116mm OD) ≈ 110mm; with SB12PFCR25-4 (~122mm OD) ≈ 113mm — same as DA1/DA2. Centre spacing with DSA90-8 ≈ 98mm.

### Scan-Speak Discovery R2604/833000 — Candidate (100W ring radiator, Fs 440 Hz — new window champion)
- Type: **Dual Ring Radiator**, fabric diaphragm | VC: 25 mm | Faceplate OD: **~104 mm** (estimated; same Discovery family as D2604) | Impedance: 4Ω | Re: 2.9Ω | Xmax: 0.2 mm
- Sensitivity: **92 dB @ 2.83V/1m** | Power: **100W RMS** | Fs: **440 Hz** | Wave-guide centre plug | Extended response to 40 kHz+
- **Source:** [SoundImports](https://www.soundimports.eu/en/scan-speak-r2604-833000.html) (fetched June 2026) | Price: **€62.45** | Stock (Jun 2026): **10+**
- **Min crossover:** 2× Fs = **880 Hz** — identical to XT25TG30-04. Same crossover flexibility as the ring radiator champion, but with 100W instead of 15W.
- **DSP correction vs TB sub (85 dB ref):** −7.0 dB pad needed (same as D2604/830000).
- **Power at reference (98 dB):** 4.0W (4% of 100W). At burst (101 dB): 8.0W (8%). Indestructible.
- **Why this stands out:** Combines XT25TG30-04's crossover window depth (Fs 440 Hz) with D2604's 100W power rating. The ring radiator diaphragm gives superior off-axis dispersion vs a dome — critical for 60° kitchen listening. Only €12.50 more than XT25TG30-04. New absolute window champion with DSA90-8: **2,380 Hz window** (880–3,260 Hz) — wider than any pairing in the catalogue.
- **Pairing note:** At ~104mm FP, spacing with DS115-8 ≈ 110mm; with SB12PFCR25-4 ≈ 113mm; with DSA90-8 ≈ 98mm. Same physical footprint as D2604/830000 and SB29RDNC-C000-4.

### Scan-Speak Discovery R2604/832000 — Candidate (100W ring radiator, Fs 500 Hz)
- Type: **Dual Ring Radiator**, fabric diaphragm | VC: 25 mm | Faceplate OD: **~104 mm** (est.) | Impedance: 4Ω | Re: 2.9Ω | Xmax: 0.2 mm
- Sensitivity: **90 dB @ 2.83V/1m** | Power: **100W RMS** | Fs: **500 Hz** | Extended response to 40 kHz+
- **Source:** [SoundImports](https://www.soundimports.eu/en/scan-speak-r2604-832000.html) (fetched June 2026) | Price: **€52.95** | Stock (Jun 2026): **10+**
- **Min crossover:** 2× Fs = **1,000 Hz** — slightly higher than R2604/833000 (880 Hz) but still wider window than D2604/830000 (1,260 Hz).
- **DSP correction vs TB sub (85 dB ref):** −5.0 dB pad needed.
- **Power at reference (98 dB):** 6.3W (6.3% of 100W). At burst (101 dB): 12.6W (12.6%). Indestructible.
- **Why interesting:** Budget Discovery ring radiator — 100W for only €52.95 (cheaper than SB29RDNC at €68.45, same price bracket as XT25TG30-04). Wider window than D2604/830000 despite being a ring radiator. Best budget 100W ring radiator option. Prefer R2604/833000 at +€9.50 for the 880 Hz min xover — 120 Hz extra window is meaningful for DSP flexibility.
- **Pairing note:** At ~104mm FP, spacing with DS115-8 ≈ 110mm; with SB12PFCR25-4 ≈ 113mm; with DSA90-8 ≈ 98mm.

### SEAS 27TDFC H1189-06 — Candidate (90W dome, Fs 550 Hz — widest-window standard dome)
- Dome: 27 mm soft textile | Rear chamber | Faceplate OD: **103.8 mm** | Cutout: 73 mm | Depth: **39 mm** | Impedance: 6Ω
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
- Dome: **18 mm woven carbon fiber** | Faceplate OD: **58 mm** | Cutout: 36.9 mm | Depth: 38.3 mm | Impedance: 4Ω | Re: 3.54Ω
- Sensitivity: **90 dB @ 2.83V/1m** | Power: **40W RMS** | Fs: **1,100 Hz** | Frequency response: 2,500–20,000 Hz
- Qts: 1.2 | Qms: 2.0 | Qes: 3.1 | Neodymium motor | Ferrofluid VC cooling
- **Source:** [SoundImports](https://www.soundimports.eu/en/dayton-audio-cf18n-4.html) (fetched June 2026) | Price: **€30.54** (sale, was €36.95) | Stock (Jun 2026): **pre-order / OOS** (was 6 units; gone OOS)
- **Min crossover:** 2× Fs = **2,200 Hz**. Response starts 2,500 Hz — crossover must be placed above this; LR48 slope provides ample mechanical protection below it.
- **DSP correction vs TB sub (85 dB ref):** −5.0 dB pad needed.
- **Power at reference (98 dB):** 6.3W (15.8% of 40W). At burst (101 dB): 12.6W (31.5%). Well within 40W rating.
- **Why this stands out — spacing:** 58mm FP OD is the 3rd smallest in the entire candidate field, after XT25SC40-04 (43.9mm) and HiVi TN28-B (47.6mm). With DSA90-8 (92mm OD): spacing = (92+58)/2 = **75mm** — between TN1 (70mm) and B6 (73mm). With SB12PFCR25-4 (~122mm): **90mm spacing**.
- **Why this stands out — off-axis:** 18mm dome = widest off-axis dispersion of any dome candidate except ND20FA-6 (45mm FP, 19mm dome, but Fs=2,005 Hz min xover 4,010 Hz). Carbon fiber dome = detailed, low-colouration character. At 60° kitchen geometry the 18mm dome maintains output well into HF.
- **Why this stands out — power:** 40W RMS is double the typical 15-20W fabric/silk dome at this FP size. CF3 pairing (SB12PFCR25-4 + CF18N-4 at ~£53) gives 90mm spacing with both 30W mid and 40W tweeter — very robust.
- **Concern — HF rolloff at 30° off-axis:** Reviewer noted "rolloff above 12 kHz beyond 30°." At 60° kitchen position HF above 12 kHz will be attenuated. This is less audible than mid-treble rolloff; the critical 2.8–10 kHz range may still be fine.
- **Concern — depth:** 38.3mm depth requires adequate tweeter chamber depth.
- **Carbon fiber visual note:** Woven CF dome has a distinctive dark-weave appearance — different from fabric or silk domes. Owner has removed all visual exclusions; CF appearance is noted as distinctive, not a concern.

### SEAS Prestige 27TFFNC/CG H1406-04 — Candidate (80W, low-profile, oval faceplate)
- Dome: 26 mm Sonolex precoated fabric | Faceplate: **69.7 × 54 mm oval** | Cutout: 46 mm | Depth: **21.5 mm** | Impedance: 4Ω | Re: 2.7Ω
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
- Dome: 26 mm fine weave soft fabric | Faceplate OD: **~72 mm** (assumed — SB26 family standard; confirm from datasheet) | Impedance: 5Ω | Re: 4.4Ω
- Sensitivity: **91 dB @ 2.83V/1m** | Power: **80W RMS** | Fs: **870 Hz** | Xmax: 0.6 mm | Sd: 6.2 cm²
- CCAW voice coil (0.33 g moving mass) | Saturation-controlled motor | Internal pressure equalisation
- **Source:** [SoundImports](https://www.soundimports.eu/en/sb-acoustics-sb26st-c000-5.html) | [SB Acoustics](https://sbacoustics.com/product/sb26st-c000-5/) | Price: **€30.95** | Stock (June 2026): 10+
- **Min crossover:** 2× Fs = **1,740 Hz**.
- **DSP correction vs TB sub (85 dB ref):** −6.0 dB pad needed.
- **Power at reference (98 dB):** 5.0W (6.3% of 80W). At burst (101 dB): **10.0W** (12.5%). Effectively indestructible in this application.
- **5Ω note:** JAB5 at 24V → ~49W into 5Ω. Massively above the 10W needed at burst.
- **Why this matters:** 80W RMS in a ~72mm compact faceplate is the standout combination. The SB26STCN-C000-4 (same SB26 family, 72mm FP, 120W) costs €36.45; the SB26ST at €30.95 is €6 cheaper and still far exceeds any power requirement. Combines compact spacing (ST series = SB26 small-ish faceplate vs 104mm large-FP tweeters) with very high thermal robustness.
- **FP OD caveat:** SB26STCN-C000-4 (confirmed 72mm FP) is from the same SB26 chassis family. 72mm is assumed for SB26ST-C000-5 but not confirmed from dimension drawing — verify before ordering. If confirmed 72mm: spacing with DSA90-8 (92mm OD) = **82mm**; with DS115-8 (116mm OD) = 94mm; with SB12PFCR25-4 (~122mm OD) = 97mm.
- **vs SB26STCN-C000-4:** SB26ST costs €6 less but has 80W vs 120W and 5Ω vs 4Ω. At the power levels in this project (10W max at burst), 80W vs 120W is irrelevant. Choose SB26ST for the €6 saving.
- **Pairings enabled:** ST1 (DS115-8 + SB26ST: 94mm spacing, 1,740–2,636 Hz window); ST2 (SB12PFCR25-4 + SB26ST: 97mm, 1,740–2,730 Hz); ST3 (DSA90-8 + SB26ST: 82mm, 1,740–3,260 Hz).

### Dayton Audio ND25FN-4 — Rejected (no faceplate — unmountable on standard baffle)
- Dome: 25 mm treated silk | Impedance: 4Ω | Sensitivity: 90 dB | Power: 20W RMS | Fs: 1,350 Hz
- Supplier: [SoundImports](https://www.soundimports.eu/en/dayton-audio-nd25fn-4.html) | Price: €12.36 | Stock: 10+
- **Reason:** Designed as a bare element for waveguide or custom mounting — explicitly has no faceplate. Cannot be conventionally front-baffle mounted without fabricating a custom mounting ring. Power at reference (98 dB) needs 12.6W vs 20W rated — power is fine. Excluded solely on mounting practicality grounds.

### Peerless by Tymphany BC25TG15-04 — Rejected
- Dome: 25 mm silk | Faceplate OD: 104 mm | Impedance: 4Ω
- Sensitivity: 93.9 dB | Power: 7W RMS | Fs: 1100 Hz
- Supplier: [SoundImports](https://www.soundimports.eu/en/peerless-by-tymphany-bc25tg15-04.html) | Price: €29.95 | Stock: 10+
- **Reason for rejection:** Power at only 7W RMS is catastrophically below the 20W minimum requirement. Would be destroyed at moderate volumes on this system.

### Peerless by Tymphany OC25SC65-04 — Rejected
- Dome: 25 mm coated textile | Faceplate OD: 41 mm body (faceplate-less design) | Impedance: 4Ω
- Sensitivity: 92.3 dB | Power: 12W RMS | Fs: 1400 Hz
- Supplier: [SoundImports](https://www.soundimports.eu/en/peerless-by-tymphany-oc25sc65-04.html) | Price: €26.95 | Stock: 10+
- **Reason for rejection:** Faceplate-less twist-lock design — cannot be surface-mounted to a flat baffle without custom hardware. Power at 12W RMS fails the 20W minimum requirement.

### Dayton Audio ND25FW-4 — Candidate (in stock Amazon UK)
- Dome: 1" (25 mm) treated silk | Round waveguide faceplate OD: 104 mm | Impedance: 4Ω
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

### SB Acoustics SB21RDCN-C000-4 ★ — most compact ring radiator, neodymium (Willys-Hifi)
- Type: Ring radiator | Dome: **21 mm fabric ring** | Faceplate OD: **58.0 mm** round | Cutout: **38.25 mm** | Depth: **22.7 mm total** (3.2 mm protrusion, ~19.5 mm behind baffle) | Impedance: 4Ω | Re: 3.1Ω | Le: 0.04 mH
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
- **FR at 60° off-axis:** Ring radiator maintains wide directivity. On-axis flat ~1kHz–15kHz; 30° off-axis tracks to ~5kHz; 60° off-axis tracks to ~3kHz then diverges gradually. At 2,800 Hz the 60° response is very close to on-axis. Excellent for kitchen listening geometry.
- **Why this stands out — compactness:** 58mm FP is among the smallest in-stock tweeters in the field. For any mid ≤122mm, SB21RDCN keeps centre spacing ≤90mm.
- **Why this stands out — technology:** Ring radiator inherently produces wider off-axis HF than a conventional dome of the same diaphragm area. At the kitchen 60° position this matters.
- **Why this stands out — depth:** 22.7mm total depth (19.5mm behind baffle) — among the shallowest in the field, comparable to MDT12 (19mm). No rear-chamber clearance concern.
- **Concern:** Qts 1.28 is high — typical for ring-radiator and high-Fs tweeters. Not a concern in normal use above the min crossover.
- **Pairings enabled (new combo IDs):**
  - **XCR1:** DSA90-8 + SB21RDCN-C000-4 → 75mm spacing, window 1,700–3,260 Hz (1,560 Hz wide)
  - **XCR2:** DS115-8 + SB21RDCN-C000-4 → 87mm spacing, window 1,700–2,636 Hz (936 Hz wide)
  - **XCR3:** SB12PFCR25-4 + SB21RDCN-C000-4 → 90mm spacing, window 1,700–2,730 Hz (1,030 Hz wide)

### Scan-Speak Discovery D2604/833000 ★ — lowest Fs dome in field, tuned rear chamber (Willys-Hifi)
- Type: Textile dome | Dome: **26 mm dark textile, wide surround** | Faceplate OD: **104.2 mm** round | Cutout: **74 mm** | Depth: **~55 mm total** (~5 mm protrusion, ~50 mm behind baffle; tuned rear chamber — much deeper than D2604/830000's 25.4 mm) | Impedance: 4Ω | Re: 2.8Ω | Le: 0.04 mH
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

### Morel MDT22T — Candidate (lower Fs than MDT12 but far deeper; Willys-Hifi)
- Type: Soft dome | Dome: **28 mm selected soft fabric (dark)** | Faceplate: **54 × 54 mm SQUARE** (R5.5mm corner radii) | Cutout: **Ø44.0 mm** (chassis) | Depth: **~55 mm total** (3 mm protrusion, ~52 mm behind baffle) | Impedance: 8Ω | Re: 5.2Ω | Le: 0.05 mH @ 1kHz
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
- Type: Ring dome | Dome: **29 mm fabric ring** | Faceplate OD: **103.8 mm** round | Cutout: **70.0 mm** | Depth: **37.25 mm total** (4.0 mm protrusion, 33.25 mm behind baffle) | Impedance: 4Ω | Re: 3.0Ω | Le: 0.05 mH | Net weight: 0.54 kg | Cast aluminium faceplate
- Sensitivity: **93 dB @ 2.83V/1m** | Power: **100W** | Fs: **600 Hz** | Sd: 9.6 cm² | VC dia: 29mm | Air gap: 2.5mm | Xlin (p-p): 0.5mm | Mms: 0.45g | BL: 2.4 Tm | Qms: 2.2 | Qes: 0.9 | Qts: 0.64 | Flux density: 1.1T | Mounting: 7× Ø4.2mm holes
- ⚠️ Willys product page states cutout 74mm — **SB Acoustics datasheet confirms 70.0mm**
- Dome colour: **Dark** (dark ring fabric, confirmed from SB Acoustics datasheet photo)
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/sb-acoustics-sb29rdac-c000-4-tweeter) | **Datasheet:** [research/sb_acoustics_sb29rdac-c000-4.pdf](research/sb_acoustics_sb29rdac-c000-4.pdf) | [SB Acoustics URL](https://sbacoustics.com/wp-content/uploads/2025/03/SB29RDAC-C000-4.pdf) | Price: **£44.39** | Stock (Jun 2026): UK in stock
- **Min crossover:** 2× Fs = **1,200 Hz**. | **DSP correction:** −8.0 dB. | **Power at reference:** 3.2W (3.2% of 100W); burst 6.3W (6.3%). Indestructible.
- **Centre spacing (FP OD 103.8 mm):** DSA90-8 → 98mm | DS115-8 → 110mm | SB12PFCR25-4 → 113mm
- **vs SB29RDNC-C000-4 (£54.31 Willys, confirmed in index):** RDAC = ferrite, RDNC = neodymium. Both 100W, ~104mm FP, 29mm ring dome, Fs ~580–600 Hz. RDAC saves **£9.92** (18%). Both within limits. RDAC is the value choice; prefer RDNC only for reduced mounting weight.

### SB Acoustics SB21RDC-C000-4 — Candidate (ferrite ring dome; Willys-Hifi)
- Type: Ring radiator | Dome: **21 mm fabric ring** | Faceplate OD: **92.0 mm** round | Cutout: **62.5 mm** | Depth: **30.6 mm total** (3.3 mm protrusion, 26.5 mm behind baffle) | Impedance: 4Ω | Re: 3.1Ω | Le: 0.04 mH | Net weight: 0.33 kg
- Sensitivity: **90 dB @ 2.83V/1m** | Power: **40W RMS** (IEC HP Butterworth 2600 Hz 12dB/oct) | Fs: **760 Hz**
- Sd: 4.6 cm² | VC dia: 20.4mm | VC height: 1.5mm | Air gap: 2.5mm | Xlin (p-p): 1.0mm | Mms: 0.25g | BL: 1.5 Tm | Qms: 2.54 | Qes: 1.64 | Qts: 1.0 | Flux density: 1.02T
- ⚠️ Willys product page states 60W power — **SB Acoustics datasheet confirms 40W**
- Dome colour: **Dark** (dark ring fabric, confirmed from SB Acoustics datasheet photo)
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/sb-acoustics-sb21rdc-c000-4-tweeter) | **Datasheet:** [research/sb_acoustics_sb21rdc-c000-4.pdf](research/sb_acoustics_sb21rdc-c000-4.pdf) | [SB Acoustics URL](https://sbacoustics.com/wp-content/uploads/2020/02/SB21RDC-C000-4.pdf) | Price: **£36.55** | Stock (Jun 2026): UK in stock
- **Min crossover:** 2× Fs = **1,520 Hz**. | **DSP correction:** −5.0 dB. | **Power at reference:** 6.3W (15.8% of 40W ✓); burst 12.6W (31.5% ✓).
- **Centre spacing (FP OD 92 mm):** DSA90-8 (92mm) → 92mm | DS115-8 → 104mm | SB12PFCR25-4 → 107mm
- **vs SB21RDCN-C000-4:** Same 21mm ring radiator diaphragm. RDC ferrite (0.33kg), RDCN neodymium (0.06kg). RDC: 92mm FP, £36.55, Fs 760 Hz (min xover 1,520 Hz). RDCN: 58mm FP, £41.60, Fs 850 Hz (min xover 1,700 Hz). RDCN's 34mm FP compactness advantage decisively outweighs the 180 Hz Fs advantage. Prefer RDCN for all new designs; only choose RDC if 92mm FP spacing is already committed.

### Scan-Speak Illuminator D3004/602010 ★★ — Candidate (ultra-low Fs dome, 850 Hz min xover; lautsprechershop.de)
- Type: Soft dome (textile) + rear chamber | Dome: **26 mm** | Faceplate OD: **61.9 mm** round | Impedance: 4Ω | Power: **50W RMS / 130W max**
- Sensitivity: **89.6 dB @ 2.83V/1m** | Fs: **425 Hz**
- ⚠ Full T/S (Re, Qts, cutout, depth) not confirmed from LSS page — fetch Scan-Speak Illuminator D3004 datasheet for complete mechanical dimensions
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS tweeter index, June 2026) | LSS price: **€142.20 inc VAT / €119.50 exc VAT** (~£119 inc) | Stock (Jun 2026): **in stock at LSS** | Previously listed ⚠ DISC at Willys (last stock £115.05) — LSS confirms available
- **Min crossover:** 2× Fs = **850 Hz** — lowest of any dome in the entire catalogue. Enables mid/tweeter crossover below 1 kHz.
- **DSP correction vs TB sub (85 dB ref):** −4.6 dB attenuation (4Ω: 1W sens = 89.6 − 3.01 = 86.59 dB).
- **Power at reference (4Ω, 98 dB):** 10^((98−86.59)/10) = **13.8W** (27.6% of 50W ✓). At burst (101 dB): **27.6W** (55.2% of 50W ✓; 21.2% of 130W ✓).
- **Centre spacing (FP OD 61.9 mm):** DSA90-8 (92.3mm) → **77mm** | DS115-8 (115.6mm) → **89mm** | SB12PFCR25-4 (~122mm) → **92mm** | 12W/4524G00 (100mm) → **81mm** | 15W/4434G00 (114mm) → **88mm** | WF118WA07 (118mm) → **90mm** | Morel 428 (118.5mm) → **90mm**
- **Why this stands out:** 850 Hz minimum crossover is 90 Hz lower than any ring radiator and 250 Hz lower than any dome in the catalogue. The compact 61.9mm FP creates the tightest achievable centre-spacing — 77–92mm depending on mid — minimising vertical lobe smearing. With a 4" mid (beaming ~2,600–2,900 Hz), crossover window is 850–2,600+ Hz (over 1,700 Hz of freedom). With a 5.25" mid (beaming ~2,390 Hz), window is 850–2,390 Hz — still excellent. Scan-Speak Illuminator-grade transient response and low distortion at 850 Hz crossover point.
- **Pairings:** ILL1/ILL2/ILL3 (existing combos) updated to remove DISC flag; LS-series in combos.md covers new LSS mids.

### Scan-Speak Illuminator R3004/602010 ★★ — Candidate (ring radiator, Fs=420Hz, compact FP; lautsprechershop.de)
- Type: Ring radiator | FP OD: **61.9 mm** round | Impedance: 4Ω | Power: not confirmed from page
- Fs: **420 Hz** | Sensitivity: not confirmed from LSS page
- ⚠ Full T/S (Re, Qts, sensitivity, power, cutout, depth) not confirmed — fetch Scan-Speak R3004/602010 datasheet from scan-speak.dk before ordering
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS tweeter index, June 2026) | LSS price: **€179.10 inc VAT / €150.50 exc VAT** (~£150) | Stock (Jun 2026): in stock at LSS
- **Min crossover:** 2× Fs = **840 Hz** — 10 Hz lower than D3004/602010 (850 Hz). Narrowly the most flexible crossover window of any tweeter in this catalogue.
- **Centre spacing (FP OD 61.9 mm):** DSA90-8 → **77mm** | DS115-8 → **89mm** | 12W/4524G00 (100mm) → **81mm** | 15W/4434G00 (114mm) → **88mm** | WF118WA07 (118mm) → **90mm** | Morel 428 (118.5mm) → **90mm**
- **Why this stands out:** Ring radiator construction on the same compact 61.9mm Illuminator chassis as D3004/602010. Ring radiator off-axis dispersion is inherently wider than a dome — critical at the 60° kitchen listening geometry. If Fs=420Hz is confirmed, this pairs with any mid in the catalogue including 5.25" drivers (beaming ~2,390 Hz → window = 840–2,390 Hz = 1,550 Hz wide).
- **vs D3004/602010 (€142.20, dome, Fs=425Hz):** R3004 is €37 more for ring radiator construction with potentially superior off-axis behaviour. The compact 62mm FP is the same on both. Choose D3004/602010 until R3004 datasheet confirms power rating, sensitivity, and ring radiator off-axis advantage at 62mm ring size.
- **Priority:** Fetch datasheet before ordering.

### Audaphon TWS 30/4 ★★ — Candidate (30mm dome, Fs=470Hz, 93dB; lautsprechershop.de exclusive)
- Type: Soft dome (fabric) | Dome: **30 mm** | Faceplate OD: **104 mm** round | Metal faceplate | Impedance: 4Ω | Power: **100W**
- Sensitivity: **93 dB @ 2.83V/1m** | Fs: **470 Hz** | LSS house brand — **not available at SI/HFC/Willys**
- ⚠ Full T/S (Re, Qts, cutout, depth) not confirmed from LSS page — datasheet not yet fetched
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS tweeter index, June 2026) | LSS price: **€79.00 inc VAT / €66.39 exc VAT** (~£66 inc) | Stock (Jun 2026): in stock at LSS
- **Min crossover:** 2× Fs = **940 Hz** — second-lowest dome in catalogue after D3004/602010 (850 Hz); 160 Hz lower than SEAS H1189-06 (1,100 Hz).
- **DSP correction vs TB sub (85 dB ref):** −8.0 dB attenuation (4Ω: 1W sens = 93 − 3.01 = 89.99 dB).
- **Power at reference (4Ω, 98 dB):** 10^((98−89.99)/10) = **6.3W** (6.3% of 100W ✓). At burst (101 dB): **12.6W** (12.6% ✓). Effectively indestructible at project SPL.
- **Centre spacing (FP OD 104 mm):** DSA90-8 → **98mm** | DS115-8 → **110mm** | SB12PFCR25-4 → **113mm** | 12W/4524G00 (100mm) → **102mm** | 15W/4434G00 (114mm) → **109mm** | WF118WA07 (118mm) → **111mm** | Morel 428 (118.5mm) → **111mm**
- **Why this stands out:** 940 Hz minimum crossover dramatically lower than any comparable 104mm dome from other vendors. The 30mm dome is the largest diaphragm of any candidate — potential for smooth, natural high frequency. 93 dB high sensitivity ensures near-indestructible power at project SPL. At €79 it is the best-value extremely-low-Fs dome per unit of crossover flexibility.
- **vs D3004/602010 (850 Hz, €142):** D3004 is 90 Hz lower in min xover and 42mm more compact (62mm FP). TWS 30/4 saves €63 for a 90 Hz crossover headroom penalty. For pairings where the 104mm FP spacing is acceptable and 940 Hz is sufficient, TWS 30/4 is the clear value choice.
- **vs SEAS H1189-06 (1,100 Hz, ~£57 HFC/Falcon):** TWS 30/4 has 160 Hz lower min xover and costs ~£9 more at LSS. Prefers TWS 30/4 when crossover window matters; H1189-06 when buying from UK suppliers without EU delivery cost.

### Dayton Audio RS28A-4 ★ — Candidate (28mm 100W dome, Fs=600Hz; lautsprechershop.de)
- Type: Soft dome (fabric) | Dome: **28 mm** | Faceplate OD: **103 mm** round | Impedance: 4Ω | Power: **100W**
- Sensitivity: **91 dB @ 2.83V/1m** | Fs: **600 Hz** | Not available at SI/HFC/Willys — LSS exclusive in UK context
- ⚠ Full T/S (Re, Qts, cutout, depth) not confirmed from LSS page — fetch Dayton RS28A-4 datasheet for complete data
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS tweeter index, June 2026) | LSS price: **€89.40 inc VAT / €75.13 exc VAT** (~£75 inc) | Stock (Jun 2026): in stock at LSS
- **Min crossover:** 2× Fs = **1,200 Hz** — same class as SB29SDAC (1,200 Hz) and D2604/830000 (1,260 Hz).
- **DSP correction vs TB sub (85 dB ref):** −6.0 dB attenuation (4Ω: 1W sens = 91 − 3.01 = 87.99 dB).
- **Power at reference (4Ω, 98 dB):** 10^((98−87.99)/10) = **10.0W** (10% of 100W ✓). At burst (101 dB): **20.0W** (20% ✓). Effectively indestructible.
- **Centre spacing (FP OD 103 mm):** DSA90-8 → **98mm** | DS115-8 → **109mm** | SB12PFCR25-4 → **112mm** | 12W/4524G00 (100mm) → **102mm** | 15W/4434G00 (114mm) → **109mm** | WF118WA07 (118mm) → **111mm**
- **Why considered:** 100W power rating at €89.40 is excellent value for a 103mm-class dome. 91 dB sensitivity (2 dB lower than TWS 30/4) means 2 dB less DSP pad required. 28mm dome in standard class for this FP size.
- **vs Audaphon TWS 30/4 (940 Hz, €79):** TWS 30/4 has 260 Hz lower min xover, 2 dB higher sensitivity, 1mm larger dome, €10 cheaper. RS28A-4 wins only on 2 dB lower DSP pad requirement — a marginal advantage. Prefer TWS 30/4 for the 260 Hz crossover freedom in most pairings. RS28A-4 is relevant only if 940 Hz → 1,200 Hz crossover gap is unimportant and 91 dB sensitivity is preferred.

### Wavecor TW022WA05 ★★ — Candidate (22mm silk dome, Fs=750Hz; lautsprechershop.de)
- Type: Soft dome (silk) | Dome: **22 mm** | Faceplate OD: **103.75 mm** round | Impedance: 4Ω
- Sensitivity: **est. 88 dB @ 2.83V/1m** | Power: **est. 100W RMS** | Fs: **750 Hz** | LSS-only in UK context
- ⚠ Full T/S (Re, Qts, exact sensitivity, power) not confirmed from LSS page — fetch Wavecor TW022WA05 datasheet before ordering
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS tweeter index, June 2026) | LSS price: **€78.10 inc VAT / €65.63 exc VAT** (~£66) | Stock (Jun 2026): in stock at LSS
- **Min crossover:** 2× Fs = **1,500 Hz** — comfortable margin below all standard mid beaming limits (≥2,400 Hz).
- **DSP correction vs TB sub (85 dB ref):** est. −3.0 dB (4Ω: 1W sens ≈ 88 − 3.01 = 84.99 dB ≈ sub reference).
- **Power at reference (est. 4Ω, 88 dB sens, 98 dB target):** P = (2.83²/4) × 10^((98−88)/10) = 2.0 × 10.0 = **20.0W** (20% of 100W est ✓). At burst (101 dB): **40.0W** (40% est ✓). Well within rating.
- **Available @ 24V into 4Ω:** ~61W >> 40W ✓.
- **Centre spacing (FP OD 103.75 mm):** DSA90-8 → **98mm** | DS115-8 → **110mm** | 12W/4524G00 (100mm) → **102mm** | 15W/4434G00 (114mm) → **109mm** | WF118WA07 (118mm) → **111mm** | Morel 428 (118.5mm) → **111mm**
- **Why this stands out:** At €78.10 it prices between SB26STCN (€36.45, 25mm, Fs=950Hz) and SEAS H1189-06 (€71.86, 27mm, Fs=550Hz). The 22mm dome is smaller than all 25–30mm dome candidates → slightly wider off-axis dispersion above 10 kHz. Fs=750 Hz gives 1,500 Hz min crossover — broad window for all mids in the catalogue. If 100W power confirmed, offers very large safety margin vs estimated 40W burst demand.
- **Concern:** All specs estimated — datasheet required. 103.75mm FP is large (same class as H1189-06, DX25TG59-04).
- **vs TW022WA06 (€80.30, +ferrofluid):** €2.20 more for ferrofluid. At ≤40W burst in this project, ferrofluid is unnecessary. Prefer WA05.

### Wavecor TW022WA06 ★★ — Candidate (22mm silk dome + ferrofluid, Fs=750Hz; lautsprechershop.de)
- Same as TW022WA05 but with magnetic fluid (ferrofluid) added to voice coil gap for enhanced thermal handling.
- LSS price: **€80.30 inc VAT / €67.48 exc VAT** (~£67) | Stock (Jun 2026): in stock at LSS
- All acoustic specs as TW022WA05 (specs estimated — datasheet needed). Ferrofluid lowers Fs slightly (est. ~740 Hz) and adds ~10–20W thermal headroom.
- **vs TW022WA05 (€78.10):** €2.20 premium for ferrofluid. At ≤40W burst in this project, ferrofluid provides marginal benefit. Prefer WA05 on value unless continuous high-power use is expected.

---

## Midranges

### Dayton Audio DSA90-8 — Candidate (top-ranked)
- Size: 3" | Frame OD: 92.3 mm round | Impedance: 8Ω
- Cone: Black anodised aluminium | Dust cap: Concave, black (stealth)
- Sensitivity: 84.7 dB | Power: 20 W RMS / 40 W max | Xmax: ±2.5 mm | Fs: 66.6 Hz
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/dayton-audio-dsa90-8.html) (specs fetched June 2026)
- **Datasheet:** [research/dayton_audio_dsa90-8.pdf](research/dayton_audio_dsa90-8.pdf) | [original URL](https://www.parts-express.com/pedocs/specs/295-522--dayton-audio-DSA90-8-specifications.pdf)
- SoundImports price: €34.95 | Stock (June 2026): 10+
- **Why liked:** Most compact frame that passes the circular rule. Black anodised cone and concave dust cap are the most visually stealthy option available. Runs cleanly past 8 kHz. Per-pairing crossover window in combos.md. 10+ in stock.
- **Concern:** 20 W RMS rating is modest. Fs of 66.6 Hz means a 120 Hz sub/mid crossover places it only 1.8× above Fs — marginal excursion headroom at the low end. **Mitigated by raising the crossover to 150–160 Hz** (the TB sub handles this easily), which increases the Fs margin to 2.25× and brings peak power within the 40 W max rating.
- **DSP adjustment needed:** +0.3 dB gain to match TB sub reference level (85 dB). Effectively zero correction — the best-matched mid candidate.

### Dayton Audio TCP115-8 — Candidate
- Size: 4" | Frame OD: 116 mm round | Impedance: 8Ω
- Cone: Treated paper | Dust cap: Inverted paper (low-profile, dark) | Surround: High-roll rubber
- Sensitivity: 81.9 dB | Power: 40 W RMS / 80 W max | Xmax: ±4.0 mm | Fs: 59.2 Hz
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/dayton-audio-tcp115-8.html) (specs fetched June 2026)
- **Datasheet:** [research/dayton_audio_tcp115-8.pdf](research/dayton_audio_tcp115-8.pdf) | [original URL](https://www.daytonaudio.com/images/resources/295-416--dayton-audio-tcp115-8-specification-sheet.pdf)
- SoundImports price: €14.01 | Stock (June 2026): **10+ in stock**
- **Why liked:** Warmest character of all evaluated mids — punchy low-mids suit the GHM-inspired tonal goal best. 4.0 mm Xmax gives the most excursion headroom of any candidate at the 150 Hz crossover. 40 W RMS / 80 W max is double the DSA90-8's power rating. Fs 59.2 Hz means a 150 Hz crossover sits 2.53× above resonance — better margin than the DSA90-8. Round frame passes circular rule. Very affordable at €14.01.
- **Concern:** Sensitivity of 81.9 dB requires +3.1 dB DSP gain to match TB sub reference level (85 dB) — this roughly doubles the amplifier power demand vs a sensitivity-matched driver. The JAB5 official datasheet (confirmed June 2026) only specifies 100W at 36V into 6Ω — no 24V/8Ω figure is published. Derived estimate is ~31W at 24V into 8Ω, which is a deficit for TCP115-8's 40.7W RMS need. A 29V supply closes the RMS gap but burst headroom remains short. See amp.md for full analysis.

### Dayton Audio DS115-8 — Candidate (top-ranked 8Ω)
- Size: 4" | Frame OD: 115.6 mm round | Impedance: 8Ω
- Cone: **Coated paper — confirmed dark from official Dayton Audio datasheet (PDF)** | Surround: Half-roll rubber
- Sensitivity: 85.3 dB @ 2.83V/1m | Power: 35W RMS | Xmax: 4.1 mm | Fs: 55.2 Hz
- Qts: 0.38 | Qms: 2.10 | Qes: 0.46 | Re: 5.8Ω | Le: 0.8 mH | Mms: 7.9 g | Cms: 1.05 mm/N | BL: 5.88 Tm | Vas: 4.33 L | Sd: 54.1 cm² | Vd: 22.2 cm³
- Baffle cutout: 93.6 mm | Depth: 54.7 mm | VC diameter: 25.4 mm
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/dayton-audio-ds115-8.html) | [Dayton Audio product page](https://www.daytonaudio.com/product/1054/ds115-8-4-designer-series-woofer-speaker-8-ohm) | Datasheet: [research/dayton_ds115-8_specifications.pdf](research/dayton_ds115-8_specifications.pdf) | [original URL](https://www.parts-express.com/pedocs/specs/295-424--dayton-audio-ds115-8-specifications.pdf)
- SoundImports price: €36.95 | Stock (June 2026): 4 units
- **Why liked:** Best Fs margin of any 8Ω candidate (55.2 Hz → 2.72× at 150 Hz crossover). Best Xmax of any 8Ω candidate (4.1 mm). Sensitivity 85.3 dB is essentially a perfect match to the 85 dB sub — only −0.3 dB DSP correction needed (zero in practice). 35W RMS provides comfortable thermal margin. Datasheet explicitly states "Cosmetic frame with low profile lip, designed for front mounting — no countersinking required." Confirmed dark coated paper cone — visual rule passes.
- **Concern:** Only 4 units in stock — enough for one build but no surplus. Re 5.8Ω is slightly higher than a standard 8Ω driver; the amp channel draws slightly less current than a true 8Ω load at the same voltage.
- **DSP adjustment needed:** −0.3 dB (effectively zero).

### HiVi Swan B4N — Candidate
- Size: 4" | Frame OD: 116.5 mm round | Cutout: 108 mm | Depth: 67.6 mm | Impedance: 8Ω
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
- Size: 4" | Frame OD: 98 mm round | Impedance: 8Ω
- Cone: Black anodised aluminium | Sensitivity: 84.6 dB | Power: 30 W RMS / 60 W max | Xmax: ±3.5 mm | Fs: 92 Hz
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/dayton-audio-rs100-8.html) (specs fetched June 2026)
- SoundImports price: €48.95 | Stock (June 2026): **1 unit only**
- **What's good:** Better power handling than DSA90-8 (30 W RMS vs 20 W); more Xmax (3.5 mm vs 2.5 mm). Black cone passes visual rule.
- **Concern:** Fs of 92 Hz with a 150 Hz crossover is only 1.63× margin — tighter than DSA90-8 at 150 Hz. Only 1 unit in stock — not reliable for a build where a replacement might be needed. Price at €48.95 is high relative to performance gain over DSA90-8.

### SB Acoustics SB12PACR25-4 — Candidate (aluminium cone, UK stock)
- Size: 4" | Frame OD: 122 mm | Impedance: 4Ω | Plastic chassis
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
- Size: 4" | Frame OD: ~122 mm | Impedance: 4Ω | Cast aluminium vented chassis
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
- Size: 4" | Frame OD: ~122 mm (same family as PACR — confirm before ordering) | Impedance: 4Ω | Plastic chassis
- Cone: Natural fiber paper (proprietary SB Acoustics in-house material) | Surround: Butyl rubber
- Sensitivity: 87.5 dB @ 2.83V/1m | Power: 30W RMS | Fs: 58 Hz | Xmax: 4.9 mm | Sd: 50 cm²
- Qts: 0.43 | Qes: 0.49 | Qms: 3.4 | BL: 3.5 Tm | Mms: 5.3 g | Re: 3.1Ω | Le: 0.26 mH | Vas: 5.2 L
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/sb-acoustics-sb12pfcr25-4.html) | [SB Acoustics](https://sbacoustics.com/product/4-sb12pfcr25-4/) (fetched June 2026)
- SoundImports price: **€25.95** | Stock (June 2026): 10+
- **DSP correction vs TB sub (85 dB ref):** −2.5 dB — near-perfect match.
- **Power check:** At reference (98 dB): 22.4W ✓ (within 30W). At woofer max (101 dB): 44.7W ✗. Same practical fix: DSP sub limiter ~40W keeps mid within 30W.
- **Fs check:** 58 Hz → **2.59× at 150 Hz** — excellent, better than DSA90-8 (2.25×) and SIG120-4 (2.01×).
- **Xmax:** 4.9 mm — effectively equal to SB12PACR25-4 and better than DS115-8.
- **Beaming:** Same Sd 50 cm² as PACR → beaming starts ~2,730 Hz. Beaming limit above the typical 4" mid crossover range.
- **Character:** Natural fiber paper cone — warm, natural tonality. Better match to GHM-inspired tonal goal than the aluminium PACR version. Reviewers describe "deep midbass and warm sound character."
- **Price note:** At €25.95 this is the cheapest standalone mid candidate with competitive specs — cheaper than B4N (€22.45 but lower Xmax and power), TCP115-8 (€14.01 but needs 29V PSU), DS115-8 (€36.95). Excellent value.

### SB Acoustics SB12PACR25-4-COAX — Candidate (coaxial — mid + tweeter in one unit)
- **This is the coaxial version** — integrated 12.4mm dome tweeter in the woofer cone centre. Separate terminals; each driven by its own JAB5 channel.
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
- Size: 5" | Frame OD: 132 mm | Impedance: 8Ω
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
- Size: 5" | Frame OD: circular plastic chassis (large) | Impedance: 4Ω
- Cone: Natural fibre (paper blend) | Sensitivity: 89 dB | Power: 40W RMS | Xmax: 4.5 mm | Fs: 44 Hz
- Qts: 0.29 | Vas: 13.4 L | Sd: 87 cm²
- Supplier: [SoundImports](https://www.soundimports.eu/en/sb13pfcr25-4-woofer.html) | Price: €28.45 | Stock: 10+
- **Power check:** At reference (98 dB, 4Ω): 15.9W. At woofer max (101 dB): 31.7W. Both within 40W. ✓
- **Concern — Qts:** 0.29 is very low — designed for large vented enclosures (Vas 13.4 L). As an active mid with DSP HP at 150 Hz it doesn't need a tuned enclosure (any sealed rear chamber works), but the driver's transient behaviour will be very damped. Fs 44 Hz → 3.4× at 150 Hz — outstanding Fs margin.
- **Concern — frame OD:** 5" nominal, frame likely 130+ mm — similar to PA130-8. Tight on 190 mm baffle.
- **Reinstated June 2026:** Previously excluded on size/Qts rules. Power passes, no visual issue.

### Peerless by Tymphany SLS-85S25CP04-04 — Candidate (reinstated June 2026)
- Size: 3.5" | Frame: 105 × 91 mm oval-rectangular | Impedance: 4Ω
- Cone: Treated paper | Sensitivity: 86 dB | Power: 30W RMS | Xmax: **10.2 mm** | Fs: 73 Hz
- Qts: 0.36 | Vas: 1.43 L
- Supplier: [SoundImports](https://www.soundimports.eu/en/peerless-by-tymphany-sls-85s25cp04-04.html) | Price: €29.95 | Stock: 10+
- **Why interesting:** Xmax 10.2 mm is equal to SDS-P830656 — outstanding mechanical headroom. Paper cone, warm character. Fs 73 Hz → 2.05× at 150 Hz crossover (adequate). 4Ω: at 29V delivers 90W vs 31.7W needed at 98 dB ✓. Frame 105×91mm — if the 91mm axis is vertical, centre spacing with compact tweeters (DT-28N ~72mm OD) is ~82mm.
- **DSP correction:** −1 dB vs sub (86 dB vs 85 dB ref).
- **Power at reference:** 4Ω, 86 dB → 2×10^((98−86)/10) = 31.7W (within 30W RMS — marginal; DSP limit at 30W; at burst 63.4W vs 30W — cap sub via DSP limiter). 29V required.

### Peerless by Tymphany SDS-P830656 — Candidate (reconsidering)
- Size: 5.25" | Frame: **152 × 134 mm** truncated cast frame | Impedance: 8Ω
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
- Size: 5" | Frame: 136 × 151 mm (pressed steel — approximately round; mounting PCD 140 mm, 4 slots) | Impedance: 8Ω
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
- Size: 3" mid-dome | Frame OD: circular | Impedance: 8Ω
- Diaphragm: not specified | Sensitivity: 92 dB | Power: 80W RMS | Xmax: 0.4 mm | Fs: 300 Hz
- Qts: 1.73 | Vas: 0.01 ft³
- Supplier: [SoundImports](https://www.soundimports.eu/en/scan-speak-d7608-920010.html) | Price: €106.95 | Stock: 6
- **Reason for rejection:** Xmax of only 0.4 mm is far below the 2.5 mm minimum. Qts of 1.73 is extremely high, indicating it requires a specific resonant chamber. Requires "vented / open rearside" — complex mounting. Price at €106.95 is also over the combined budget for this driver alone.

### HiVi Swan DM-7500 — Candidate (over stated budget)
- Size: 3" mid-dome | Impedance: 5Ω | Sensitivity: 94 dB | Power: 20W RMS / 120W max | Fs: 300 Hz
- Supplier: [SoundImports](https://www.soundimports.eu/en/hivi-dm-7500.html) | Price: €79.95 | Stock: 10+
- **Power check (5Ω, 94 dB):** At reference (98 dB): 4.0W. At woofer max (101 dB): 8.0W. Both well within 20W. ✓ DSP correction: −9 dB.
- **Fs note:** 300 Hz — this is a mid-dome, not a cone mid. The 150 Hz crossover is 0.5× its Fs — far below resonance. **Would need crossover at 600 Hz minimum (2× Fs).** That means the sub would handle 40–600 Hz, and this covers 600 Hz–20 kHz with no separate tweeter. A 2.5-way or 2-way active rather than true 3-way.
- **Impedance:** 5Ω — JAB5 handles it safely; power at 24V into 5Ω ≈ 49W. Fine.
- **Price:** €79.95 — exceeds the ~£75 combined mid+tweeter budget unless budget is extended.

### Dayton Audio RS52FN-8 — Rejected (Xmax, Fs, size)
- Size: 2" midrange dome | Frame OD: 130 mm (5.12") | Impedance: 8Ω
- Diaphragm: damped fabric | Sensitivity: 90 dB | Power: 60W RMS / 120W max | Xmax: 1 mm | Fs: 394 Hz
- Qts: 1.05 | Sd: 26.4 cm²
- Supplier: [SoundImports](https://www.soundimports.eu/en/dayton-audio-rs52fn-8.html) | Price: €62.95 | Stock: 9
- **Reason for rejection:** Xmax of only 1 mm is far below the 2.5 mm minimum. Fs at 394 Hz with typical 150 Hz crossover would be only 0.38× Fs ratio — would be severely overdriven at the crossover point. This is a dedicated upper-midrange dome, not a woofer-style mid.

### Tectonic TEBM65C20F-8 BMR — Candidate (noted; low sensitivity)
- Size: 3.5" | Frame OD: 108 mm round | Impedance: 8Ω
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
- Size: 4" | Frame OD: **122.3 mm** round | Impedance: 8Ω | Cone: Mg/Al alloy | Full-range design
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
- Size: 5.25" | Frame OD: **152 mm** | Impedance: 4Ω | Open cast aluminium frame
- Cone: Anodised aluminium (colour unconfirmed — assume black like SIG120-4 pending visual)
- Sensitivity: 91.1 dB @ 2.83V/1m (loudspeakerdatabase: 87.4 dB @1W/1m → 90.4 dB @2.83V — minor discrepancy; SoundImports used)
- Power: 60W RMS / 120W peak | Frequency response: 60–4,000 Hz
- Fs: 61.5 Hz | Xmax: 4 mm | Sd: 96 cm² | Vas: 8.7 L | Qts: 0.49 | Qes: 0.53 | Qms: 5.78
- BL: 5.2 Tm | Re: 3.7Ω | Le: 0.35 mH | Mms: 10.2 g | VC: 26.7 mm
- Depth: 67 mm | Cutout: 120 mm | 6 mounting holes
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/dayton-audio-sig150-4.html) | T/S: [loudspeakerdatabase.com](https://loudspeakerdatabase.com/Dayton/SIG150-4) (fetched June 2026)
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
- Size: 4" | Frame OD: 123 mm (4.84") round | Impedance: 4Ω | Baffle cutout: 95 mm (3.74") | Depth: 59 mm
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
- Size: 4.5" | Frame OD: **100 mm** round | Impedance: 4Ω | Cone: Paper (Discovery grade) | Baffle cutout: ~82 mm (est)
- Sensitivity: **88.8 dB @ 2.83V/1m** | Power: **40W RMS / 70W max** | Xmax: **±3 mm** | Fs: **50 Hz**
- ⚠ Full T/S (Re, Qts, Sd, Vas, Mms) not confirmed from LSS page — fetch Scan-Speak Discovery 12W datasheet
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS woofer index, June 2026) | LSS price: **€59.40 inc VAT / €49.92 exc VAT** (~£50) | Stock (Jun 2026): in stock at LSS
- **Fs margin at 150 Hz crossover:** 150/50 = **3.0×** — excellent; best Fs margin of any 4Ω 4.5" candidate.
- **DSP correction vs TB sub (85 dB ref):** −3.8 dB attenuation (4Ω: 1W sens = 88.8 − 3.01 = 85.79 dB).
- **Power at reference (4Ω, 98 dB):** 10^((98−85.79)/10) = **16.6W** (41.5% of 40W ✓). At burst (101 dB): **33.2W** (83% of 40W — near limit; 47% of 70W max ✓). Set DSP sub limiter at 40W to protect driver.
- **Beaming (Sd est. ~45 cm²):** f_beam ≈ 34400/(π×√(45/π)) ≈ **~2,890 Hz** (estimate; datasheet Sd needed for accuracy).
- **Centre spacing (FP OD 100 mm):** D3004/602010 (62mm) → **81mm** | Audaphon TWS 30/4 (104mm) → **102mm** | RS28A-4 (103mm) → **102mm** | XT25TG30-04 (104mm) → **102mm** | H1189-06 (103.8mm) → **102mm** | DX25TG59-04 (104mm) → **102mm** | SB12PFCR25-4 (122mm) → **111mm**
- **Why this stands out:** FP=100mm is the most compact 4.5" mid in the catalogue — 15mm narrower than DS115-8 (116mm). Fs=50Hz delivers 3.0× margin at 150 Hz crossover. At €59.40 it prices close to DS115-8 (€36.95) with Scan-Speak Discovery construction and far smaller footprint. 4Ω → 61W available at 24V — ample headroom. The compact FP opens pairings with D3004/602010 (81mm spacing) that would be impossible with DS115-8 (89mm).
- **Concern:** Xmax=3mm is lower than DS115-8 (4.1mm) and SB12PFCR25-4 (4.9mm). 40W RMS rating is modest; DSP limiter at 40W essential for burst protection.

### Scan-Speak Discovery 15W/4434G00 ★★ — Candidate (5.25" Discovery, exceptional Fs+Xmax; lautsprechershop.de)
- Size: 5.25" | Frame OD: **114 mm** round | Impedance: 4Ω | Cone: Paper (Discovery grade) | Baffle cutout: ~95 mm (est)
- Sensitivity: **89.7 dB @ 2.83V/1m** | Power: **60W RMS / 120W max** | Xmax: **±4.3 mm** | Fs: **43 Hz**
- ⚠ Full T/S not confirmed from LSS page — fetch Scan-Speak Discovery 15W/4434G00 datasheet
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS woofer index, June 2026) | LSS price: **€68.40 inc VAT / €57.48 exc VAT** (~£57) | Stock (Jun 2026): in stock at LSS
- **Fs margin at 150 Hz crossover:** 150/43 = **3.49×** — outstanding; best of any mid candidate evaluated in this project.
- **DSP correction vs TB sub (85 dB ref):** −4.7 dB attenuation (4Ω: 1W sens = 89.7 − 3.01 = 86.69 dB).
- **Power at reference (4Ω, 98 dB):** 10^((98−86.69)/10) = **13.5W** (22.5% of 60W ✓). At burst (101 dB): **27.0W** (45% of 60W ✓; 22.5% of 120W ✓). Substantial thermal headroom.
- **Beaming (Sd est. ~66 cm²):** f_beam ≈ 34400/(π×√(66/π)) ≈ **~2,390 Hz** (estimate; datasheet Sd needed). Upper crossover ceiling: ~2,400 Hz — still compatible with all tweeters in catalogue (all have min xover ≤ 1,200 Hz).
- **Centre spacing (FP OD 114 mm):** D3004/602010 (62mm) → **88mm** | Audaphon TWS 30/4 (104mm) → **109mm** | RS28A-4 (103mm) → **109mm** | XT25TG30-04 (104mm) → **109mm** | H1189-06 (103.8mm) → **109mm**
- **Why this stands out:** Fs=43Hz is the lowest of any mid candidate in this project. 3.49× margin at 150 Hz crossover is essentially risk-free at the sub/mid boundary. Xmax=4.3mm is the best of any Scan-Speak Discovery mid, matching the best SB Acoustics candidates. 60W RMS provides comfortable headroom. At €68.40 it undercuts WF118WA07 (€95.70) significantly. 4Ω → 61W at 24V.
- **Concern:** 5.25" cone with estimated Sd≈66cm² starts beaming above ~2,390 Hz — restricts mid/tweeter crossover to below ~2,400 Hz. This is within all tweeters' capability. 114mm FP on 190mm baffle leaves 38mm each side — comfortable for surface mounting.

### Scan-Speak Illuminator 12MU/4731T00 ★★ — Candidate (premium Illuminator dedicated mid; lautsprechershop.de)
- Size: 4.5" | Frame OD: **101 mm** round | Impedance: 4Ω | Cone: Scan-Speak Illuminator (dedicated midrange motor) | Baffle cutout: ~82 mm (est)
- Sensitivity: **90 dB @ 2.83V/1m** | Power: **80W RMS / 150W max** | Xmax: **±3.5 mm** | Fs: **64 Hz**
- ⚠ Full T/S not confirmed from LSS page — fetch Scan-Speak Illuminator 12MU/4731T00 datasheet
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS woofer index, June 2026) | LSS price: **€306.00 inc VAT / €257.14 exc VAT** (~£257) | Stock (Jun 2026): in stock at LSS
- **Fs margin at 150 Hz crossover:** 150/64 = **2.34×** — good; comfortable margin.
- **DSP correction vs TB sub (85 dB ref):** −5.0 dB attenuation (4Ω: 1W sens = 90 − 3.01 = 86.99 dB).
- **Power at reference (4Ω, 98 dB):** 10^((98−86.99)/10) = **12.6W** (15.8% of 80W ✓). At burst (101 dB): **25.2W** (31.5% of 80W ✓; 16.8% of 150W ✓). Power effectively unlimited at project SPL.
- **Beaming (Sd est. ~46 cm²):** f_beam ≈ 34400/(π×√(46/π)) ≈ **~2,860 Hz** (estimate). Compact FP + wide beaming is the ideal combination for a mid driver.
- **Centre spacing (FP OD 101 mm):** D3004/602010 (62mm) → **82mm** | Audaphon TWS 30/4 (104mm) → **103mm** | RS28A-4 (103mm) → **102mm** | XT25TG30-04 (104mm) → **103mm** | H1189-06 (103.8mm) → **102mm**
- **Why considered:** The Scan-Speak Illuminator 12MU is a purpose-built midrange unit — the Illuminator motor (FEA-optimised, copper ring, short voice coil in long gap) targets the 300 Hz–5 kHz range specifically. 101mm FP is nearly as compact as 12W/4524G00 (100mm). 90 dB is the highest sensitivity of any new LSS mid. At €306 it is 4–5× the cost of the 12W/4524G00 (€59.40) for a dedicated mid motor vs a woofer-range driver pressed into mid service.
- **Concern:** €306 is significant for a kitchen counter build. Acoustic performance in this application (active DSP, 150 Hz crossover, limited off-axis demands) may not justify the premium over the €59.40 12W/4524G00. Recommended for builds where the best possible midrange fidelity is the primary goal regardless of cost.

### Wavecor WF118WA07 ★★ — Candidate (4.5" Neo motor, Fs=56Hz; lautsprechershop.de)
- Size: 4.5" | Frame OD: **118 mm** round | Impedance: 4Ω | Cone: ? (datasheet pending) | Baffle cutout: ~95 mm (est) | Neodymium motor
- Sensitivity: **87 dB @ 2.83V/1m** | Power: **50W** | Xmax: **±4 mm** | Fs: **56 Hz**
- ⚠ Full T/S and cone material not confirmed — fetch Wavecor WF118WA07 datasheet before ordering
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS woofer index, June 2026) | LSS price: **€95.70 inc VAT / €80.42 exc VAT** (~£80) | Stock (Jun 2026): in stock at LSS
- **Fs margin at 150 Hz crossover:** 150/56 = **2.68×** — excellent; same class as DS115-8 (2.72×).
- **DSP correction vs TB sub (85 dB ref):** −2.0 dB — near-perfect sensitivity match; one of the closest of any candidate.
- **Power at reference (4Ω, 98 dB):** 10^((98−83.99)/10) = **25.2W** (50.4% of 50W ✓). At burst (101 dB): **50.3W** — ⚠ marginally over 50W rating. **Set DSP limiter at ~45W** (peak mid SPL ~100 dB @1m) to protect driver; 1 dB headroom penalty vs system ceiling.
- **Beaming (Sd est. ~50 cm²):** f_beam ≈ 34400/(π×√(50/π)) ≈ **~2,740 Hz** (estimate; same class as DS115-8 ~2,636 Hz).
- **Centre spacing (FP OD 118 mm):** D3004/602010 (62mm) → **90mm** | Audaphon TWS 30/4 (104mm) → **111mm** | RS28A-4 (103mm) → **111mm** | XT25TG30-04 (104mm) → **111mm** | H1189-06 (103.8mm) → **111mm**
- **Why this stands out:** Neo motor delivers excellent BL linearity and lower moving mass vs ferrite equivalent. Fs=56Hz at 150 Hz crossover = 2.68× margin — same class as DS115-8 (2.72×), better than B4N (2.26×). Xmax=4mm matches DS115-8 (4.1mm). −2 dB DSP correction is the closest sensitivity match of any new LSS mid. FP=118mm stays within the 122mm limit with 4mm to spare. 4Ω → 61W at 24V.
- **Concern:** Burst power (50.3W) just exceeds the 50W driver rating. DSP sub limiter at 45W is essential. Cone material unknown — datasheet required before ordering. €95.70 is €59 more than 12W/4524G00 with marginally better Xmax and similar Fs margin.
- **vs Wavecor WF120BD05 (Fs=48Hz, 60W, €149.60):** WA07 is €54 cheaper. BD05 wins on Fs margin (3.13× vs 2.68×) and 60W burst rating (eliminates limiter concern). Choose WA07 for value; BD05 if burst headroom is required.

### Wavecor WF120BD05 ★★ — Candidate (4.5" BD motor, lowest-Fs Wavecor 11cm; lautsprechershop.de)
- Size: 4.5" | Frame OD: **120 mm** round | Impedance: 4Ω | Cone: ? (BD motor variant; datasheet pending) | Baffle cutout: ~99 mm (est) | Premium BD (Balanced Drive) motor
- Sensitivity: **87 dB @ 2.83V/1m** | Power: **60W** | Xmax: **±4 mm** | Fs: **48 Hz**
- ⚠ Full T/S and cone material not confirmed — fetch Wavecor WF120BD05 datasheet before ordering
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS woofer index, June 2026) | LSS price: **€149.60 inc VAT / €125.71 exc VAT** (~£126) | Stock (Jun 2026): in stock at LSS
- **Fs margin at 150 Hz crossover:** 150/48 = **3.13×** — excellent; between WF118WA07 (2.68×) and 15W/4434G00 (3.49×).
- **DSP correction vs TB sub (85 dB ref):** −2.0 dB — same as WF118WA07.
- **Power at reference (4Ω, 98 dB):** 25.2W (42% of 60W ✓). At burst (101 dB): **50.3W** (83.8% of 60W ✓ — adequate headroom; no DSP limiter required for driver protection at project SPL).
- **Beaming (Sd est. ~52 cm²):** f_beam ≈ **~2,690 Hz** (estimate; similar to WF118WA07).
- **Centre spacing (FP OD 120 mm):** D3004/602010 (62mm) → **91mm** | Audaphon TWS 30/4 (104mm) → **112mm** | RS28A-4 (103mm) → **112mm** | XT25TG30-04 (104mm) → **112mm**
- **Why considered:** BD (Balanced Drive) motor is Wavecor's premium architecture — improved BL linearity at high excursion. Fs=48Hz (8Hz lower than WF118WA07) gives 3.13× margin at 150 Hz. 60W rating eliminates the burst limiter concern that affects WF118WA07. FP=120mm within 122mm limit with 2mm to spare.
- **vs WF118WA07 (€95.70):** €54 more for 8Hz lower Fs, 10W more power rating (no limiter needed), premium BD motor. Prefer WA07 on value; BD05 if burst margin is a priority.

### Morel EW 428 ★★ — Candidate (4.5" premium motor, best Xmax in 428 family; lautsprechershop.de)
- Size: 4.5" | Frame OD: **118.5 mm** round | Impedance: **8Ω** | Cone: ? (EW = premium motor, cone material TBC) | Baffle cutout: ~97 mm (est)
- Sensitivity: **87 dB @ 2.83V/1m** (= 87 dB @ 1W/1m for 8Ω) | Power: **150W** | Xmax: **±4.5 mm** | Fs: **62 Hz**
- ⚠ Full T/S and cone material not confirmed — fetch Morel EW 428 datasheet before ordering
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS woofer index, June 2026) | LSS price: **€153.00 inc VAT / €128.57 exc VAT** (~£129) | Stock (Jun 2026): in stock at LSS
- **Fs margin at 150 Hz crossover:** 150/62 = **2.42×** — good, adequate margin.
- **DSP correction vs TB sub (85 dB ref):** −2.0 dB — near-perfect match (same class as WF118WA07).
- **Power at reference (8Ω, 98 dB):** 10^((98−87)/10) = **12.6W** (8.4% of 150W ✓). At burst (101 dB): **25.1W** (16.7% ✓). Power practically indestructible — 150W is 6× the burst requirement.
- **Beaming (Sd est. ~50 cm²):** f_beam ≈ **~2,740 Hz** (estimate; same size class as DS115-8).
- **Centre spacing (FP OD 118.5 mm):** D3004/602010 (62mm) → **90mm** | Audaphon TWS 30/4 (104mm) → **111mm** | RS28A-4 (103mm) → **111mm** | XT25TG30-04 (104mm) → **111mm** | H1189-06 (103.8mm) → **111mm**
- **Why this stands out:** 150W rating at 25.1W burst demand = 6× safety factor — uniquely immune to over-drive. Xmax=4.5mm is the best in the Morel 428 family and matches or exceeds all other 4.5" mids. 8Ω means mid channel at 24V delivers ~31W → well above 25.1W burst. No DSP power limiter needed.
- **Concern:** €153 is significant. Fs=62Hz (2.42× margin) is adequate but not exceptional compared to WF118WA07 (2.68×). 8Ω gives less amp headroom than 4Ω alternatives (31W vs 61W at 24V), though 31W >> 25.1W burst.
- **vs WF118WA07 (4Ω, Xmax=4mm, €95.70):** WA07: lower cost, better Fs margin (2.68×), 4Ω (more amp headroom), Xmax only 0.5mm less, but burst power at rating limit (50W). EW 428: 150W ceiling, Xmax=4.5mm, 8Ω (less amp overhead, still adequate). Choose WA07 for value; EW 428 if burst power headroom and 150W thermal rating matter.

### Morel CAW 428 ★ — Candidate (4.5", 4mm Xmax, lower cost than EW 428; lautsprechershop.de)
- Size: 4.5" | Frame OD: **118.5 mm** round | Impedance: **8Ω** | Power: **150W** | Xmax: **±4 mm** | Fs: **74 Hz** | Sensitivity: **88 dB @ 1W/1m** (= 88 dB @ 2.83V/1m for 8Ω)
- ⚠ Full T/S not confirmed — fetch Morel CAW 428 datasheet
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS woofer index, June 2026) | LSS price: **€109.00 inc VAT / €91.60 exc VAT** (~£92) | Stock (Jun 2026): in stock at LSS
- **Fs margin at 150 Hz crossover:** 150/74 = **2.03×** — ⚠ just at the 2× minimum threshold. Raise crossover to 160–170 Hz (sub handles this easily) to increase margin to 2.16–2.30×.
- **DSP correction vs TB sub (85 dB ref):** −3.0 dB — modest correction.
- **Power at reference (8Ω, 98 dB):** 10.0W (6.7% of 150W ✓). At burst (101 dB): **20.0W** (13.3% ✓).
- **Beaming:** Same FP as EW 428 → same ~2,740 Hz estimate.
- **Centre spacing:** Same as EW 428 (FP=118.5mm).
- **vs Morel EW 428 (Fs=62Hz, Xmax=4.5mm, €153):** EW 428 is strictly better acoustically at only €44 more. EW 428 has 12Hz lower Fs (better margin), 0.5mm more Xmax, better motor. Choose EW 428 unless budget constrained. CAW 428 with crossover raised to 165Hz is viable if €44 matters.

### Morel EM 428 ★ — Candidate (4.5" standard motor, entry of 428 family; lautsprechershop.de)
- Size: 4.5" | Frame OD: **118.5 mm** round | Impedance: **8Ω** | Power: **150W** | Xmax: **±3 mm** | Fs: **68 Hz** | Sensitivity: **87 dB @ 1W/1m**
- ⚠ Full T/S not confirmed — fetch Morel EM 428 datasheet
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS woofer index, June 2026) | LSS price: **€134.00 inc VAT / €112.61 exc VAT** (~£113) | Stock (Jun 2026): in stock at LSS
- **Fs margin at 150 Hz crossover:** 150/68 = **2.21×** — adequate.
- **DSP correction vs TB sub (85 dB ref):** −2.0 dB.
- **Power at reference (8Ω, 98 dB):** 12.6W (8.4% of 150W ✓). At burst (101 dB): **25.1W** (16.7% ✓).
- **Beaming:** Same FP as EW 428 → ~2,740 Hz estimate.
- **vs Morel EW 428 (Fs=62Hz, Xmax=4.5mm, €153):** EW 428 is better in every acoustic parameter: 6Hz lower Fs, 1.5mm more Xmax, better motor — at only €19 more. **Choose EW 428 over EM 428 unconditionally.** EM 428 is only relevant if EW 428 sells out at LSS.

### SEAS CA12RCY H1152-08 ★ — Candidate (classic paper cone, 4.5"; lautsprechershop.de)
- Size: 4.5" | Frame OD: **120.4 mm** round | Impedance: **8Ω** | Cone: Paper (SEAS Prestige classic)
- Sensitivity: **est. 87 dB @ 2.83V/1m** | Power: **est. 80W RMS** | Xmax: **±3 mm** | Fs: **57 Hz**
- ⚠ Full T/S not confirmed from LSS page — fetch SEAS CA12RCY H1152-08 datasheet before ordering
- **Source:** [Lautsprechershop.de](https://www.lautsprechershop.de/chassis/zy2_main_en.htm) (LSS woofer index, June 2026) | LSS price: **€94.90 inc VAT / €79.75 exc VAT** (~£80) | Stock (Jun 2026): in stock at LSS
- **Fs margin at 150 Hz crossover:** 150/57 = **2.63×** — good, same class as DS115-8 (2.72×).
- **DSP correction vs TB sub (85 dB ref):** est. −2.0 dB — near-perfect match.
- **Power at reference (8Ω, est. 87 dB, 98 dB target):** P = (2.83²/8) × 10^((98−87)/10) = 1.0 × 10^(1.1) = **12.6W** (15.8% of 80W est ✓). At burst (101 dB): **25.1W** (31.4% ✓). Good headroom.
- **Available @ 24V into 8Ω:** ~31W > 25.1W ✓.
- **Beaming (120.4 mm FP → est. cone dia ~97mm):** f_beam ≈ 34400/(π×0.0485) ≈ **2,260 Hz** (estimate). Upper crossover ceiling ~2,200 Hz.
- **Centre spacing (FP OD 120.4 mm):** D3004/602010 (62mm) → **91mm** | Audaphon TWS 30/4 (104mm) → **112mm** | TW022WA05 (103.75mm) → **112mm** | H1189-06 (103.8mm) → **112mm**
- **Why considered:** SEAS Prestige paper cone with classic warm character. Fs=57Hz and est. 3mm Xmax are competitive. €94.90 is well-priced for SEAS Prestige quality. 8Ω → ~31W at 24V vs 25.1W burst required — adequate.
- **Concern:** Beaming limit ~2,260 Hz tighter than standard 4" mids (~2,700 Hz). Set mid/tweeter crossover ≤2,200 Hz — requires tweeter with min xover ≤1,500 Hz: D3004/602010 (850Hz ✓), R3004/602010 (840Hz ✓), TWS 30/4 (940Hz ✓), H1189-06 (1,100Hz ✓), TW022WA05 (1,500Hz ✓), all ring radiators ✓.
- **vs WF118WA07 (4Ω, Fs=56Hz, €95.70, est. Xmax=4mm):** Nearly identical price and Fs. WA07 has 4Ω (61W at 24V vs 31W) and est. 1mm more Xmax. CA12RCY wins on SEAS Prestige paper cone tonality. Choose WA07 for amp headroom; CA12RCY for SEAS warm character.

### SB Acoustics SB12CACS25-4 ★ — Candidate (ceramic cone, 4"; Willys-Hifi / lautsprechershop.de)
- Size: 4" | Frame OD: **123 mm** ⚠ 1mm over project FP limit | Impedance: **4Ω** | Cone: Ceramic (aluminium oxide)
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
- Size: 4" | Impedance: **8Ω** | Cone: Paper composite (NE-series construction) | Surround: Rubber
- Sensitivity: **est. 87–88 dB @ 2.83V/1m** | Power: **est. 40–50W RMS** | Xmax: **est. ±4.5 mm** | Fs: **est. 50–55 Hz**
- ⚠ Full T/S not confirmed — fetch Vifa/Peerless NE123-W-08 datasheet before ordering; confirm FP OD
- **Source:** [HiFi Collective](https://www.hificollective.co.uk) (HFC woofer index, June 2026) | HFC price: **£60.84** (inc/ex-VAT status unconfirmed) | Stock: confirm before ordering
- Also at LSS: **€108.40 inc VAT / €91.09 exc VAT** (~£91)
- **Fs margin at 150 Hz crossover:** est. 150/52 ≈ **2.9×** — excellent (estimate).
- **Power at reference (est. 8Ω, 87.5 dB, 98 dB target):** est. 12.6W (well within est. 40W ✓). Burst est. 25.1W (est. 50% of 50W ✓).
- **Why considered:** Vifa NE series (former Peerless by Tymphany, now ScanSpeak-manufactured) is known for excellent linearity, low distortion, and wide frequency extension. The NE123 is used in high-quality DIY builds as a mid with clean response to 5+ kHz. At HFC £60.84 it is priced similarly to DS115-8 + premium. If specs confirm, could be an alternative to DS115-8 for a "reference quality" mid with warm paper character.
- **Priority:** Confirm FP OD, Xmax, Fs from datasheet. If FP is ≤122mm and Xmax ≥4mm, promote to ★★.

---

## Hard-Excluded Drivers

These are excluded permanently and should not be re-evaluated.

### Peerless by Tymphany PLS-P830987 — Hard excluded
- Size: 3" nominal | Frame: **78×78 mm square** (confirmed pincushion — 4 flat edges, not a circle)
- Sensitivity: 81.8 dB | Fs: 110 Hz | Xmax: 5.4 mm | Qts: 1.0 | Power: 25W RMS | Imp: 8Ω
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/peerless-by-tymphany-pls-p830987.html) (specs fetched June 2026)
- **Reason:** 78×78 mm square frame is a non-circular design requirement — not a marginal deviation. All four flat sides will be visible from any angle when surface-mounted. Fails the circular rule unconditionally.
- **Also poor acoustically:** Fs 110 Hz gives only 1.36× margin at 150 Hz crossover; Qts 1.0 is very high; sensitivity 81.8 dB is 3.2 dB below sub reference. This driver would be a poor choice even if the frame were round.

### Lavoce MD03.10 — Hard excluded
- **Reason:** Designed as a rear-mount PA driver. Has flat-sided ear tabs on the mounting flange (non-circular), AND a front gasket specifically for flush-mount sealing. Both make it visually unacceptable when surface-mounted — the gasket sits proud of the baffle face and the ear tabs protrude from the sides. Even if technically front-mountable, the appearance is that of a PA driver bolted to a board.
- **Also:** Excessively expensive for this application (PA pricing, not hi-fi DIY).
- **Source confirmation:** [Bluearan product page](https://bluearan.co.uk/index.php?id=LAVMAF10300AF) confirms gasket-front mounting design.

### Tang Band W3-315E — Excluded (power)
- 3" | Frame OD: 3.66" (93 mm) | Impedance: 8Ω | Cone: Aluminium/Magnesium (white) | No phase plug
- Sensitivity: 87 dB @ 2.83V/1m | Power: 10W RMS / 20W max | Fs: 100 Hz | Xmax: 1.25 mm | Sd: 32 cm²
- Qts: 0.52 | Re: 6.6Ω | Mms: 2 g | Frequency response: 100–20,000 Hz
- **Source:** [SoundImports product page](https://www.soundimports.eu/en/tang-band-w3-315e.html) (specs fetched June 2026)
- **Datasheet:** [research/tang_band_w3-315e.pdf](research/tang_band_w3-315e.pdf) | [original URL](https://doc.soundimports.nl/pdf/brands/Tang%20Band/W3-315E/pdf_Tang%20Band_W3-315E_1.pdf) (downloaded June 2026)
- **Visual:** White cone, no phase plug. Owner notes: contender but not favourite.
- **Reason excluded:** Cannot balance with woofer. At 87 dB sensitivity, needs 12.6W at reference level (98 dB) — already above the 10W RMS rating. At woofer max (101 dB) needs 25.1W vs 20W max. Power handling definitely excludes it.

### Monacor SPX-31M — Hard excluded
- **Reason:** 83 dB sensitivity (needs excessive DSP gain) + Xmax only 1.1 mm (inadequate at 150 Hz crossover).

### Peerless by Tymphany BC25TG15-04 — Hard excluded
- Sensitivity: 93.9 dB | Power: 7W RMS | Supplier: [SoundImports](https://www.soundimports.eu/en/peerless-by-tymphany-bc25tg15-04.html) | Price: €29.95
- **Reason:** Needs 10.3W to balance with woofer at max. Rated only 7W. Cannot balance at full volume.

### Peerless by Tymphany OC25SC65-04 — Hard excluded (tweeters)
- Sensitivity: 92.3 dB | Power: 12W RMS | Supplier: [SoundImports](https://www.soundimports.eu/en/peerless-by-tymphany-oc25sc65-04.html) | Price: €26.95
- **Reason:** Faceplate-less twist-lock design — cannot surface-mount to a flat baffle. Also at woofer max, needs 14.8W against 12W rated — over-driven at full volume.

### Dayton Audio ND25FN-4 — Hard excluded (tweeters)
- **Reason:** No faceplate at all — designed for embedding into waveguides. Cannot surface-mount.

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

### Peerless by Tymphany XT25SC40-04 — Catalogue
- Type: Ring radiator | Size: 1" (25mm) | Imp: 4Ω | Sensitivity: 94 dB | Power: 100W RMS | Fs: 1018 Hz
- Neodymium motor. Compact cutout 1.73" (44mm). Depth 0.79" (20mm).
- **Source:** https://www.soundimports.eu/en/peerless-by-tymphany-xt25sc40-04.html | Price: €29.95 | Stock: 10+
- Note: Highest sensitivity of any ring radiator candidate (94 dB). Fs 1018 Hz → min xover 2036 Hz. Compact neodymium version of the XT25 ring radiator family.

### Peerless by Tymphany DX20BF00-04 — Catalogue (OOS)
- Type: Dome | Size: 3/4" | Imp: 4Ω | Specs: not retrieved (pre-order, page returned full specs unavailable)
- **Source:** https://www.soundimports.eu/en/peerless-by-tymphany-dx20bf00-04.html | Price: €29.95 | Stock: OOS

### Dayton Audio TD25F-4 — Catalogue
- Type: Dome (silk) | Size: 1" (25mm) | Imp: 4Ω | Sensitivity: 91 dB | Power: 20W RMS | Fs: 900 Hz
- Semi-horn loaded faceplate. Cutout 2.75" (70mm). Ferrofluid.
- **Source:** https://www.soundimports.eu/en/dayton-audio-td25f-4.html | Price: €29.95 | Stock: 10+
- Note: Fs 900 Hz → min xover 1800 Hz. "Semi-horn" faceplate — narrower HF dispersion than flat-face designs. 20W adequate.

### SB Acoustics SB26ST-C000-5 — Catalogue
- Type: Dome (fine weave fabric) | Size: 1" | Imp: 5Ω | Sensitivity: 91 dB | Power: 80W RMS | Fs: 870 Hz | Xmax: 0.6 mm
- CCAW voice coil. Saturation-controlled motor. Internal pressure equalization.
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb26st-c000-5.html | Price: €30.95 | Stock: 10+
- Note: 5Ω unusual — JAB5 handles it; ~49W available at 24V. 80W power rating is excellent. Fs 870 Hz comfortable.

### Dayton Audio CF18N-4 — Catalogue
- Type: Dome (woven carbon fiber) | Size: 3/4" (18mm) | Imp: 4Ω | Sensitivity: 90 dB | Power: 40W RMS | Fs: 1100 Hz
- Neodymium motor. Ferrofluid. Cast aluminium faceplate with protective grill.
- **Source:** https://www.soundimports.eu/en/dayton-audio-cf18n-4.html | Price: €30.54 (sale, was €36.95) | Stock: **pre-order / OOS** (Jun 2026)
- Note: Carbon fiber dome — distinctive appearance. Reviewer noted rolloff above 12 kHz beyond 30°. Fs 1100 Hz → min xover 2200 Hz. **OOS — CF1/CF2/CF3 pairings not available for immediate order.**

### Peerless by Tymphany NE25VTS-04 — Catalogue
- Type: Dome (silk) | Size: 1" | Imp: 4Ω | Sensitivity: 91.1 dB | Power: 15W RMS | Fs: 730 Hz | OD: 66.3 mm
- Neodymium magnet. Aluminium faceplate. Aluminium rear chamber doubles as heatsink. Copper cap.
- **Source:** https://www.soundimports.eu/en/peerless-by-tymphany-ne25vts-04.html | Price: €39.95 | Stock: 10+
- Note: Very compact 66.3mm OD (similar to ND25FA-4 at 66mm). Fs 730 Hz → min xover 1460 Hz. Low 15W power — same concern as DX25TG59-04 family but lower sensitivity means higher power draw.

### SB Acoustics SB21SDC-C000-4 — Catalogue (ring dome, 1 in stock)
- Type: Ring dome | Size: 3/4" (20mm) | Imp: 4Ω | Sensitivity: 91 dB | Power: 40W RMS | Fs: 720 Hz | Qts: 0.95 | OD: 3.62" (92mm)
- CCAW voice coil. Copper cap. Dual balanced compression chamber.
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb21sdc-c000-4.html | Price: €39.95 | Stock: 1
- Note: Ring dome design — same principle as ring radiator but with dome element. Fs 720 Hz → min xover 1440 Hz. Only 1 unit in stock.

### SB Acoustics SB29SDAC-C000-4 — Catalogue
- Type: Dome (1 1/8", 25mm actual dome on 29mm voice coil) | Imp: 4Ω | Sensitivity: 93 dB | Power: 60W RMS | Fs: 600 Hz | Qts: 0.80 | Xmax: 0.25 mm
- CCAW voice coil. Dual balanced compression chamber. Cast aluminium faceplate. Copper cap.
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb29sdac-c000-4.html | Price: €44.95 | Stock: 10
- Note: Fs 600 Hz → min xover 1200 Hz — widest crossover placement of the SB29 family. 93 dB high sensitivity. Saturation-controlled motor.

### SB Acoustics SB29RDC-C000-4 — Catalogue (ring dome)
- Type: Ring dome (fabric) | Size: 1 1/8" (25mm) | Imp: 4Ω | Sensitivity: 93 dB | Power: 100W RMS | Fs: 600 Hz | Qts: 0.65 | Xmax: 0.25 mm
- Fabric ring dome. Stabilizing ring reduces distortion. Copper cap.
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb29rdc-c000-4.html | Price: €53.45 | Stock: 10+
- Note: Same Fs as SDAC (600 Hz) but ring dome construction. 100W power handling. 0.7 dB lower sensitivity than RDNC.

### SB Acoustics SB29RDNC-C000-4 — Catalogue (ring dome, neodymium)
- Type: Ring dome (fabric) | Size: 1 1/8" (25mm) | Imp: 4Ω | Sensitivity: 94 dB | Power: 100W RMS | Fs: 580 Hz | Re: 3Ω
- Neodymium magnet. Fabric ring dome. Chambered back for reduced back-wave reflections. Copper cap.
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb29rdnc-c000-4.html | Price: €68.45 | Stock: 10+
- Note: Highest-end SB29 ring dome. 94 dB sensitivity. Fs 580 Hz → min xover 1160 Hz. Premium price. Mixed reviews (some praise, others find it lacks detail vs alternatives).

### Dayton Audio AMT Mini-8 — Catalogue (AMT, OOS)
- Type: AMT (Air Motion Transformer / folded Kapton ribbon) | Imp: 8Ω | Sensitivity: 88 dB | Power: 15W RMS | Freq: 3500–40,000 Hz | Face OD: 2.25" (57mm)
- **Source:** https://www.soundimports.eu/en/dayton-audio-amt-mini-8.html | Price: €36.45 | Stock: pre-order (OOS)
- Note: AMT construction — different operating principle from dome. 88 dB sensitivity is the lowest of any tweeter candidate. Reviewer noted "output very low." 15W RMS modest.

### Monacor DT-100 — Catalogue
- Type: Dome (soft) | Size: 1" | Imp: 8Ω | Sensitivity: 92 dB | Power: 30W RMS / 60W max | Fs: 1500 Hz | Faceplate: 80×116mm (rectangular)
- Ferrofluid cooled. Cutout: 72mm.
- **Source:** https://www.soundimports.eu/en/monacor-dt-100.html | Price: €43.95 | Stock: 10+
- Note: Rectangular 80×116mm faceplate — not circular. Fs 1500 Hz → min xover 3000 Hz. Recommended crossover: 2500 Hz (12 dB/oct). High sensitivity at 92 dB.

### Dayton Audio TD20F-4 — Catalogue
- Type: Dome (silk) | Size: 3/4" (18mm) | Imp: 4Ω | Sensitivity: 90 dB | Power: 20W RMS | Fs: ~3000 Hz (from freq response start) | OD: 2.56" (65mm) | Depth: 0.59" (15mm)
- Neodymium motor. Ferrofluid.
- **Source:** https://www.soundimports.eu/en/dayton-audio-td20f-4.html | Price: €17.45 | Stock: 10+
- Note: Very compact (65mm OD, 15mm deep). Fs very high — frequency response starts at 3 kHz. Crossover must be ≥3 kHz. Cheapest 3/4" candidate after ND20FA-6.

### Peerless by Tymphany D26NC56-06 — Catalogue (OOS)
- Type: Dome | Size: 1" | Imp: 6Ω | Price: €24.95 | Stock: pre-order (OOS)
- **Source:** https://www.soundimports.eu/en/peerless-by-tymphany-d26nc56-06.html
- Note: Specs not retrieved from product page (OOS). Pre-order only.

### Monacor DT 94-8 — Catalogue (URL unconfirmed)
- Type: Dome | Size: 0.8" | Imp: 8Ω | Price: €29.95 | Stock: 3 (per index)
- **Source:** URL not confirmed via search (0 results for "DT94"). Listed in SoundImports tweeter index June 2026.
- Note: Tiny 0.8" dome. Specs not retrieved. Very small dome favours HF dispersion.

### Monacor DT-28N — Catalogue
- Type: Dome (silk) | Size: 1 1/8" (28mm) | Imp: 8Ω | Sensitivity: 94 dB | Power: 50W RMS / 100W max | Fs: 1200 Hz | Freq: 2000–20,000 Hz
- Neodymium. Small waveguided faceplate. Cutout: 50mm. Depth: 21mm.
- **Source:** https://www.soundimports.eu/en/monacor-dt-28n.html | Price: €40.95 | Stock: 5
- Note: Fs 1200 Hz → min xover 2400 Hz. 94 dB very high sensitivity (needs ~9 dB DSP pad vs 85 dB sub). 50W power. Compact at 50mm cutout. Neodymium.

### Scan-Speak Discovery D2604/830000 — Catalogue
- Type: Dome (textile) | Size: 1" | Imp: 4Ω | Sensitivity: 92 dB | Power: 100W RMS / 240W max | Fs: ~630 Hz (from freq response start) | OD: 104.2mm | Cutout: 75mm | Depth: 25.4mm
- Qts: 0.79 | Qms: 3.46 | Qes: 1.02
- **Source:** https://www.soundimports.eu/en/scan-speak-d2604830000.html | Price: €44.95 | Stock: 10+ (listed as pre-order)
- Note: 100W is highest power of any standard dome candidate. 92 dB high sensitivity. Large 104.2mm OD. Scan-Speak Discovery series pedigree.

### SEAS Prestige 27TFFNC/CG H1406-04 — Catalogue
- Type: Dome (sonolex precoated fabric) | Size: 1.1" (26mm dome on wider former) | Imp: 4Ω | Sensitivity: 91 dB | Power: 80W RMS / 200W max | Freq: 2500–30,000 Hz
- Neodymium. Wide roll surround. Dual-chamber magnet. Magnetic fluid immersion.
- **Source:** https://www.soundimports.eu/en/seas-27tffnc-cg.html | Price: €40.45 (sale, was €48.95) | Stock: **pre-order / OOS** (Jun 2026)
- Note: SEAS Prestige series. 80W power. Magnetic fluid improves power handling. Sonolex fabric dome. **OOS — SE1/SE2 pairings not available for immediate order.**

### Markaudio TW 6 — Catalogue
- Type: Dome (aluminium) | Size: 1" | Imp: 4Ω | Sensitivity: 98 dB | Power: 15W RMS / 30W max | Fs: 1700 Hz | OD: 74mm
- Ferrofluid. Custom polymer frame with integrated waveguide.
- **Source:** https://www.soundimports.eu/en/markaudio-tw-6.html | Price: €44.95 | Stock: 8
- Note: 98 dB — highest sensitivity of any tweeter evaluated in this project. Needs −13 dB DSP pad vs 85 dB sub; at reference needs only 0.9W RMS. Al dome typically bright character. Fs 1700 Hz → min xover 3400 Hz. Waveguide narrows off-axis response.

### Peerless by Tymphany DA25BG08-06 — Catalogue
- Type: Dome (aluminium) | Size: 1" | Imp: 6Ω | Sensitivity: 91.6 dB | Power: 15W RMS | Fs: 710 Hz | OD: not stated
- Ferrite magnet. Heat-sinking design.
- **Source:** https://www.soundimports.eu/en/peerless-by-tymphany-da25bg08-06.html | Price: €39.95 | Stock: 10+
- Note: Aluminium dome. Low 15W power. Fs 710 Hz → min xover 1420 Hz. 6Ω: JAB5 at 24V ~41W available; needs ~4W at reference.

### GRS A25-2T — Catalogue
- Type: Dome (fabric) | Size: 2" | Imp: 6Ω | Sensitivity: 92.8 dB | Power: 30W RMS | Freq: 1500–16,000 Hz | OD: not stated
- Neodymium. Dimensionally compatible with Dynaco A25 crossover.
- **Source:** https://www.soundimports.eu/en/grs-a25-2t.html | Price: €39.95 | Stock: 10+
- Note: 2" dome — larger dome typically narrower HF dispersion. Designed as Dynaco A25 replacement. 92.8 dB sensitivity. Reviewer noted unit-to-unit variation requiring individual measurement.

### SEAS 27TDFC H1189-06 — Catalogue (10+ in stock)
- Type: Dome (soft textile) + rear chamber | Size: 1" (27mm) | Imp: 6Ω | Sensitivity: 90 dB | Power: 90W RMS / 220W max | Fs: 550 Hz | FP OD: 103.8mm | Cutout: 73mm | Depth: 39mm
- **Source:** https://www.soundimports.eu/en/seas-27tdfc.html | Price: €71.86 (sale) | Stock: 10+
- Note: Widest-window standard dome in catalogue. Fs 550 Hz → min xover 1,100 Hz. 90W/220W; at project SPL needs only 16.8W burst. 6Ω: 41W available at 24V. See full Candidate entry above.

### Scan-Speak Discovery R2604/833000 — Catalogue (10+ in stock)
- Type: Ring Radiator (dual) | Size: 1" (25mm) | Imp: 4Ω | Sensitivity: 92 dB | Power: 100W RMS | Fs: 440 Hz | Re: 2.9Ω | Xmax: 0.2mm
- **Source:** https://www.soundimports.eu/en/scan-speak-r2604-833000.html | Price: €62.45 | Stock: 10+
- Note: **New window champion.** Fs=440Hz identical to XT25TG30-04 but 100W vs 15W. RP1 pairing with DSA90-8 = 2,380Hz DSP window — absolute widest in catalogue. See full analysis in Candidate section above.

### Scan-Speak Discovery R2604/832000 — Catalogue (10+ in stock)
- Type: Ring Radiator (dual) | Size: 1" (25mm) | Imp: 4Ω | Sensitivity: 90 dB | Power: 100W RMS | Fs: 500 Hz | Re: 2.9Ω | Xmax: 0.2mm
- **Source:** https://www.soundimports.eu/en/scan-speak-r2604-832000.html | Price: €52.95 | Stock: 10+
- Note: Budget Discovery ring rad. Fs=500Hz → min 1,000Hz xover. 100W. €52.95 = comparable to XT25TG30-04 at same ring rad price point but 6.7× more power. See full analysis above.

### SB Acoustics SB21RDC-C000-4 — Catalogue (8 in stock)
- Type: Ring Radiator | Size: 3/4" (20mm) | Imp: 4Ω | Sensitivity: 90 dB | Power: 40W RMS | Fs: 760 Hz | Re: 3.1Ω | Xmax: 0.5mm
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb21rdc-c000-4.html | Price: €49.95 | Stock: 8
- Note: Ring radiator variant of SB21SDC-C000-4 (ring dome). Fs 760 Hz → min xover 1,520 Hz. 40W power. 8 in stock. Slightly higher Fs (760 vs 720 Hz) and €10 more than SB21SDC — choose SDC unless ring rad dispersion is specifically preferred and stock of SDC is exhausted.

### SB Acoustics SB29RDAC-C000-4 — Catalogue (OOS until ~Jul 31)
- Type: Ring Radiator (fabric) | Size: 1¼" (25mm) | Imp: 4Ω | Sensitivity: 93 dB | Power: 100W RMS | Fs: 900 Hz | FP OD: 103.8mm | Cutout: 70mm
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb29rdac-c000-4.html | Price: €56.95 | Stock: OOS; 6 expected 31 Jul 2026
- Note: Ring radiator (not dome despite "dome tweeter" label on SI). Fs 900 Hz → min xover 1,800 Hz (worse than XT25TG30 at 880Hz and R2604/833000 at 880Hz). 100W. At €56.95 it falls between R2604/832000 (€52.95, Fs 500Hz, better) and R2604/833000 (€62.45, Fs 440Hz, better). Not a priority over R2604 series. Monitor restock if R2604 goes OOS.

### Dayton Audio CF120-4 — Catalogue (OOS at SI; in stock Audiophonics)
- Size: 4.5" | Frame OD: ~127mm | Cutout: ~95mm | Depth: ~57mm | Imp: 4Ω | Sensitivity: 89.1 dB | Power: 30W RMS / 60W max | Cone: carbon fiber
- Fs: 53.2 Hz | Qts: 0.28 | Qes: 0.32 | Qms: 1.89 | Vas: 4.87L | Xmax: 3.5mm | Sd: 51.5 cm²
- **Source:** https://www.soundimports.eu/en/dayton-audio-cf120-4.html (OOS) | SI Price: €62.45 (sale) | Audiophonics: €49.92 (sale), in stock
- Note: Carbon fiber 4.5" midwoofer. Fs 53.2 Hz → min LP crossover 106 Hz (excellent). Beaming limit 2,703 Hz — place mid LP at or below this. Burst power needed: 31W vs 30W rated — tight (DSP limiter at 28W gives 100.6 dB). OOS at SI; in stock at Audiophonics (€49.92). Consider if DS115-8 goes OOS.

---

## June 2026 Mass Index — Woofers & Midranges (all visual constraints removed)

All drivers indexed from SoundImports woofer pages (3"–5.25" filter, cheapest sort, June 2026). No visual exclusions applied.

### Dayton Audio CE78PF-4 — Catalogue
- Size: 3" | Frame OD: 78mm | Imp: 4Ω | Sensitivity: 85 dB | Power: 10W RMS / 20W max | Fs: 100 Hz | Xmax: 1.4mm
- **Source:** https://www.soundimports.eu/en/dayton-audio-ce78pf-4.html | Price: €12.95 | Stock: 7
- Note: Very low power (10W) and Xmax (1.4mm). Suitable only for satellite or ultra-low-level mid role. Smallest OD (78mm) evaluated.

### Dayton Audio PC83-4 — Catalogue
- Size: 3" | Imp: 4Ω | Sensitivity: 86.8 dB | Power: 30W RMS / 60W max | Freq: 80–20,000 Hz | Cone: poly-damped woven glass fiber
- Copper cap to control inductance.
- **Source:** https://www.soundimports.eu/en/dayton-audio-pc83-4.html | Price: €15.65 | Stock: 2 (10 expected June 19 2026)
- Note: 30W RMS is solid for a 3" driver. Glass fiber cone. Budget option.

### GRS 4PF-8 — Catalogue
- Size: 4" | Imp: 8Ω | Sensitivity: 83 dB | Power: 40W RMS / 70W max | Fs: 137 Hz | Cone: poly-laminated paper, treated foam surround
- **Source:** https://www.soundimports.eu/en/grs-4pf-8.html | Price: €13.95 | Stock: 10
- Note: Very high Fs (137 Hz) → min xover 274 Hz. 83 dB sensitivity is lowest of any mid candidate — needs +2 dB DSP gain. Budget driver.

### SB Acoustics SB10PGC21-4 — Catalogue
- Size: 3" | Frame: square chassis | Imp: 4Ω | Sensitivity: 84 dB | Power: 20W RMS | Freq: 90–20,000 Hz | Cone: fiberglass
- CCAW voice coil. Vented.
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb10pgc21-4.html | Price: €18.95 | Stock: 10+
- Note: Square chassis (not circular frame). 84 dB sensitivity. Designed for FAST, satellites, tiny enclosures. 20W RMS modest.

### HiVi Swan B3S — Catalogue
- Size: 3" | Frame: square | Imp: 8Ω | Sensitivity: 82 dB | Power: 15W RMS / 30W max | Fs: 100 Hz | Xmax: 3mm
- Al/Mg alloy concave cone. Magnetically shielded. Stamped steel frame.
- **Source:** https://www.soundimports.eu/en/hivi-b3s.html | Price: €18.45 | Stock: 8
- Note: Square frame. Very low 82 dB sensitivity. 15W modest. Fs 100 Hz → min xover 200 Hz. Shielded.

### HiVi Swan M3N-B — Catalogue
- Size: 3" | Imp: 8Ω | Sensitivity: 82 dB | Power: 15W RMS | Fs: 91 Hz | Xmax: 3mm | VC: 20mm | Bolt circle: 83mm | Cutout: 68mm
- Black Al/Mg alloy cone. Magnetically shielded. Hi-temp VC.
- **Source:** https://www.soundimports.eu/en/hivi-m3n-b.html | Price: €18.45 | Stock: 10+
- Note: 3" black Al/Mg cone. Very low 82 dB sensitivity. Fs 91 Hz is decent. 15W RMS modest.

### Monacor SPX-32M — Catalogue
- Size: 3" | Imp: 8Ω | Sensitivity: 88 dB | Power: 20W RMS / 40W max | Fs: 110 Hz | Cone: paper | Freq: 100–22,000 Hz
- Solid wooden phase plug.
- **Source:** https://www.soundimports.eu/en/monacor-spx-32m.html | Price: €27.45 | Stock: 8
- Note: 88 dB is well-matched to sub reference. Wooden phase plug — distinctive visual. Fs 110 Hz → min xover 220 Hz. Full-range oriented.

### FaitalPRO 3FE25-4F — Catalogue
- Size: 3" | Imp: 4Ω | Sensitivity: 91 dB | Power: 20W RMS / 40W max | Fs: 110 Hz | Freq: 100–20,000 Hz | Cone: treated paper | VC: 19mm Al on Kapton | Frame: steel
- **Source:** https://www.soundimports.eu/en/faitalpro-3fe25-4f.html | Price: €19.95 | Stock: 10+
- Note: 91 dB very high for a 3" driver — needs ~6 dB DSP pad. Fs 110 Hz → min xover 220 Hz. FaitalPRO quality for PA/pro audio applications.

### FaitalPRO 3FE25-8F — Catalogue
- Size: 3" | Imp: 8Ω | Sensitivity: 91 dB | Power: 20W RMS / 40W max | Fs: 110 Hz | Freq: 100–20,000 Hz | Cone: treated paper | Re: 6.2Ω
- **Source:** https://www.soundimports.eu/en/faitalpro-3fe25-8f.html | Price: €19.95 | Stock: 10+
- Note: 8Ω version of 3FE25-4F. Identical sensitivity and Fs.

### FaitalPRO 3FE25-16F — Catalogue
- Size: 3" | Imp: 16Ω | Sensitivity: 91 dB | Power: 20W RMS / 40W max | Fs: 110 Hz | Freq: 100–20,000 Hz | Cone: treated paper
- **Source:** https://www.soundimports.eu/en/faitalpro-3fe25-16f.html | Price: €19.95 | Stock: 10+
- Note: 16Ω version — unusual impedance not compatible with JAB5 without series resistor.

### SEAS FA8RCND/S — Catalogue
- Size: 3" | Imp: 4Ω | Sensitivity: 86 dB | Power: 10W RMS / 12W max | Fs: 72 Hz | Xmax: 4mm | Freq: 100–20,000 Hz | Cone: paper | VC: 25.5mm
- **Source:** https://www.soundimports.eu/en/seas-fa8rcnds.html | Price: €32.45 | Stock: 8
- Note: Only 10W RMS / 12W max — extremely low power for this project. At 98 dB reference needs 12.6W already over rated power. Not suitable unless DSP limits system SPL. Xmax 4mm is excellent for size. Fs 72 Hz outstanding.

### SICA 3.5 F 1 CS-8 — Catalogue
- Size: 3.5" | Frame OD: 88mm | Imp: 8Ω | Sensitivity: 88.5 dB | Power: 90W program (continuous not stated) | Freq: 110–12,000 Hz | Cone: waterproof paper | VC: 1" Kapton
- **Source:** https://www.soundimports.eu/en/sica-35-f-1-cs-8.html | Price: €28.95 | Stock: 4
- Note: Pro audio / PA driver. 90W program power. Compact OD 88mm. Freq starts at 110 Hz → mid-band use only. 88.5 dB sensitivity well-matched. No Fs, Xmax, or Qts stated.

### Peerless by Tymphany TC9FD18-08 — Catalogue
- Size: 3.5" | Imp: 8Ω | Sensitivity: 84 dB | Power: 30W RMS | Fs: 130 Hz | Qts: 0.97 | Cutout: 80mm | Cone: NRSC patented paper | Freq: 70–20,000 Hz
- Copper pole cap. Non-resonant polymer chassis.
- **Source:** https://www.soundimports.eu/en/peerless-by-tymphany-tc9fd18-08.html | Price: €34.95 | Stock: 10+
- Note: High Qts (0.97) — Butterworth-like character, relatively underdamped. Fs 130 Hz → min xover 260 Hz. 84 dB low — needs DSP gain. Popular in DIY community for open-baffle and line array applications.

### Dayton Audio ND91-4 — Catalogue
- Size: 3.5" | Imp: 4Ω | Sensitivity: 85.6 dB | Power: 30W RMS / 60W max | Xmax: 4.6mm | Cone: black anodized aluminum | Freq: 65–17,000 Hz
- Rubber surround. Polyimide former. Copper alloy shorting ring.
- **Source:** https://www.soundimports.eu/en/dayton-audio-nd91-4.html | Price: €33.95 | Stock: 10+
- Note: Black anodized aluminum cone — visually compatible. Xmax 4.6mm is the highest of any small mid candidate. 85.6 dB near-perfect match to sub. 4Ω: ~61W at 24V available. Fs not stated on page; freq response starts 65 Hz.

### Tectonic TEBM65C20F-8 BMR — Catalogue
- Size: 3.5" | Imp: 8Ω | Sensitivity: 81 dB | Power: 30W RMS / 60W max | Xmax: 3.5mm | Freq: 80–20,000 Hz | Type: Balanced Mode Radiator
- **Source:** SoundImports product page | Price: €49.95 | Stock: in stock
- Note: BMR technology — single driver covers 80–20kHz as full-range. Could eliminate separate tweeter. 81 dB sensitivity very low (needs +4 dB DSP gain). Price premium. Unusual operating principle.

### Peerless by Tymphany PLS-P830986 — Catalogue
- Size: 3" | Imp: 8Ω | Sensitivity: 84.2 dB | Power: 25W RMS | Fs: 110 Hz | Xmax: 4.35mm | Cone: anodized aluminum (black) | Cutout: ~75mm | VC: 25.7mm
- Neodymium. Copper cap. Damped plastic basket.
- **Source:** https://www.soundimports.eu/en/peerless-by-tymphany-pls-p830986.html | Price: €29.95 | Stock: 10+
- Note: Black anodized aluminum cone — visually compatible. Xmax 4.35mm excellent for a 3" driver. 84.2 dB sensitivity needs +0.8 dB DSP gain. Fs 110 Hz → min xover 220 Hz.

### Markaudio CHN-70 — Catalogue
- Size: ~5" | Imp: 8Ω | Sensitivity: 86.7 dB | Power: 16W RMS / 50W max | Fs: 71.6 Hz | Xmax: 4mm | Cone: paper | Freq: ~70–20,000 Hz
- Full-range design.
- **Source:** SoundImports product page | Price: €32.45 | Stock: 4
- Note: Full-range (no separate tweeter needed) but 16W continuous is low for this system. Fs 71.6 Hz → min xover 143 Hz (excellent). Xmax 4mm solid. Only 4 in stock.

### Markaudio Alpair-5 Grey — Catalogue (OOS)
- Size: 3" | Imp: 4Ω | Sensitivity: 85.45 dB | Power: 5W RMS | Fs: ~85–95 Hz (pair-matched to ±1 Hz @ F0) | Freq: 90–25,000 Hz
- Free-to-air single suspension design. Pair-matched.
- **Source:** https://www.soundimports.eu/en/markaudio-alpair-5-grey.html | Price: €49.95 | Stock: OOS

### Markaudio Alpair-5 Gold — Catalogue (OOS)
- Size: 3" | Imp: 4Ω | Sensitivity: 85.5 dB | Power: 5W RMS | Fs: 94.5 Hz | Xmax: 3mm | Qts: 0.50 | Vas: 1.78 L | Cone: aluminum
- **Source:** https://www.soundimports.eu/en/markaudio-alpair-5-gold.html | Price: €49.95 | Stock: OOS
- Note: Both Alpair-5 variants OOS. Only 5W RMS — insufficient for this system at any meaningful SPL.

### Markaudio Alpair-5G — Catalogue (OOS)
- Size: 3" | Imp: 4Ω | Sensitivity: 88.53 dB | Power: 7W RMS | Cone: UTAG (Ultra Thin Acoustic Glass) | Freq: Fs–40,000 Hz
- **Source:** https://www.soundimports.eu/en/markaudio-alpair-5g.html | Price: €64.95 | Stock: OOS
- Note: Glass cone for improved transients. 7W RMS still insufficient for this system.

### HiVi Swan M4N — Catalogue
- Size: 4" | Imp: 8Ω | Sensitivity: 82 dB | Power: 15W RMS / 30W max | Fs: 69 Hz | Cone: Al/Mg alloy | VC: 22mm CCA | Frame: stamped steel, shielded
- **Source:** https://www.soundimports.eu/en/hivi-m4n.html | Price: €19.95 | Stock: 10+
- Note: Very low 82 dB sensitivity. 15W low power. Fs 69 Hz → 2.17× at 150 Hz. Magnetically shielded.

### HiVi Swan M4N-B — Catalogue
- Size: 4" | Imp: 8Ω | Power: 15W RMS | Fs: 69 Hz | Qts: 1.08 | Vas: 4.3 L | Xmax: 3mm | Re: 6.5Ω | Cone: Al/Mg alloy
- **Source:** https://www.soundimports.eu/en/hivi-m4n-b.html | Price: €22.45 | Stock: in stock
- Note: Qts 1.08 is very high — poorly damped, not suited for a sealed or vented mid chamber without careful tuning. Effectively same Fs as M4N but different damping. "Similar sound to B4N" per reviewers. 15W low.

### HiVi Swan M5N — Catalogue
- Size: 5" | Imp: 8Ω | Sensitivity: 87 dB | Power: 35W RMS / 70W max | Fs: 50 Hz | Xmax: 2.7mm | Cone: Al/Mg alloy | VC: 1"
- Symmetric Motor Drive (SMD) technology. Magnetically shielded.
- **Source:** https://www.soundimports.eu/en/hivi-m5n.html | Price: €29.95 | Stock: 10+
- Note: 87 dB near-matched to sub. Fs 50 Hz → 3.0× at 150 Hz (excellent). 5" Al/Mg — good beaming limit. 35W solid. Shielded.

### Dayton Audio DMA105-8 — Catalogue (10+ in stock)
- Size: 4" | Imp: 8Ω | Sensitivity: 84.8 dB | Power: 35W RMS | Fs: 72 Hz | Cone: rigid aluminum | Motor: dual neodymium magnet | Frame: 8-spoke open (aluminum)
- **Source:** https://www.soundimports.eu/en/dayton-audio-dma105-8.html | Price: €26.45 | Stock: 10+ (updated Jun 2026; previously pre-order)
- Note: Neodymium dual-magnet motor. 8-spoke open frame (circular). 84.8 dB sensitivity. Fs 72 Hz → 2.08× at 150 Hz (marginal; safer to cross at 200–250 Hz LP). 35W adequate. Now in stock — viable candidate.

### Visaton KT 100 V — Catalogue
- Size: 4" | Imp: 4Ω | Sensitivity: 83 dB | Power: 25W RMS / 40W max | Fs: 42 Hz | VC: 25mm | Freq: 32–9,500 Hz
- Rubber surround. Low-noise design. T-yoke.
- **Source:** https://www.soundimports.eu/en/visaton-kt-100-v.html | Price: €28.95 | Stock: 5
- Note: Fs 42 Hz is extraordinarily low for a 4" driver — this is a bass/woofer unit, not a midrange. Freq response ends at 9500 Hz; not usable above mid crossover. Would need crossover at 84 Hz (2×Fs). Very low sensitivity (83 dB). Designed for compact vented bass enclosures.

### Dayton Audio DA115-8 — Catalogue
- Size: 4" | Imp: 8Ω | Sensitivity: 84.9 dB | Power: 20W RMS / 40W max | Fs: 60 Hz | Cone: aluminum | Frame: cosmetic stamped steel | VC: 25mm
- **Source:** https://www.soundimports.eu/en/dayton-audio-da115-8.html | Price: €29.95 | Stock (**14 June 2026**): **3 units** (very low stock)
- Note: 84.9 dB close to sub reference. Fs 60 Hz → 2.5× at 150 Hz (solid). 20W modest. Aluminum cone (analytical character). 3 in stock.

### Monacor SPM-116/8 — Catalogue
- Size: 4" | Imp: 8Ω | Sensitivity: 87 dB | Power: 40W RMS / 80W max | Fs: 75 Hz | Cone: paper | Surround: rubber | Freq: 75–18,000 Hz
- **Source:** https://www.soundimports.eu/en/monacor-spm-116-8.html | Price: €21.45 | Stock: 8
- Note: 87 dB near-matched to sub. 40W solid. Fs 75 Hz → 2.0× at 150 Hz (adequate). Paper cone (warm character). Affordable at €21.45.

### FaitalPRO 4FE35-4F — Catalogue
- Size: 4" | Imp: 4Ω | Sensitivity: 91 dB | Power: 30W RMS / 60W max | Fs: 100 Hz | Qts: 0.73 | Vas: 2.4 L | Xmax: 1.73mm | VC: 19mm Al/Kapton | Frame: steel | Cutout: 91.5mm
- **Source:** https://www.soundimports.eu/en/faitalpro-4fe35-4f.html | Price: €26.95 | Stock: 10+
- Note: 91 dB very high sensitivity — needs ~6 dB DSP pad. Fs 100 Hz → 1.5× at 150 Hz (very tight). Xmax only 1.73mm — lowest of any 4" candidate. Pro audio / PA orientation.

### Beyma 4FR40 — Catalogue
- Size: 4" | Frame OD: 118.2mm | Imp: 8Ω | Sensitivity: 87 dB | Power: 40W AES / 80W program | Cone: paper | Surround: Santoprene | Frame: pressed steel, ceramic magnet | Freq: 100–20,000 Hz
- **Source:** https://www.soundimports.eu/en/beyma-4fr40.html | Price: €30.95 | Stock: 10+
- Note: 87 dB well-matched to sub. 40W solid. Paper cone and Santoprene surround (warm character). Full-range orientation (100–20kHz specified). OD 118.2mm wide.

### Monacor SP-4/60PRO — Catalogue
- Size: 4" | Frame: 113×113mm (square) | Imp: 8Ω | Sensitivity: 90 dB | Power: 30W RMS / 60W max | Fs: 92 Hz | Qts: 0.60 | Xmax: 2.3mm
- **Source:** SoundImports product page | Price: €29.95 | Stock: in stock
- Note: Square 113×113mm frame — not circular. Fs 92 Hz → 1.63× at 150 Hz (marginal). 90 dB well-matched. 30W adequate.

### Tang Band W4-655F — Catalogue
- Size: 4" | Frame OD: 125mm | Imp: 8Ω | Sensitivity: 89 dB | Power: 25W RMS / 50W max | Freq: 70–14,000 Hz | Xmax: 3mm
- Golden phase plug.
- **Source:** SoundImports product page | Price: €49.95 | Stock: in stock
- Note: Golden (brass-coloured) phase plug — distinctive visual. 89 dB near-matched to sub. 3mm Xmax adequate. 14 kHz upper limit suggests limited HF output above crossover; would need a tweeter ≤ 14 kHz.

### PRV Audio 4MR60-4 — Catalogue
- Size: 4" | Imp: 4Ω | Sensitivity: 90 dB | Power: 60W RMS | Freq: 90–15,000 Hz | Cone: fiberglass | VC: 20mm CCAW/Kapton | BL: 3.42 Tm | Moving mass: 4.32 g
- **Source:** https://www.soundimports.eu/en/prv-audio-4mr60-4.html | Price: €24.95 | Stock: 4
- Note: 90 dB well-matched. 60W power — highest of any 4" candidate. Fiberglass cone. Freq limited at 15 kHz. 4Ω: ~61W at 24V available. Pro audio / mid driver.

### PRV Audio 4MR60-NDY-4 — Catalogue
- Size: 4" | Imp: 4Ω | Sensitivity: 91 dB | Power: 60W RMS / 120W max | Freq: 90–20,000 Hz | Cone: fiberglass (glass fiber) | Motor: neodymium | Depth: 1.75" (shallow)
- **Source:** https://www.soundimports.eu/en/prv-audio-4mr60-ndy-4.html | Price: €49.95 | Stock: 10+
- Note: Neodymium version of 4MR60. 91 dB — needs ~6 dB DSP pad. 60W power. Shallow install depth. Freq 90–20kHz (could run full-range).

### Monacor MSH-115 — Catalogue
- Size: 4" | Imp: 8Ω | Sensitivity: 89 dB | Power: 50W RMS / 120W max | Fs: 85 Hz | Cone: paper coated ("special cone")
- **Source:** https://www.soundimports.eu/en/monacor-msh-115.html | Price: €66.95 | Stock: 9
- Note: 89 dB near-matched. 50W solid. Fs 85 Hz → 1.76× at 150 Hz (tight). Expensive at €66.95 for a 4" mid. "High-end technology" per Monacor. No Xmax stated.

### SB Acoustics SB12NRX25-4 — Catalogue
- Size: 4" | Imp: 4Ω | Sensitivity: 87.5 dB | Power: 30W RMS | Fs: 55 Hz | Xmax: 5mm | Cone: Norex (composition paper) | Surround: foam | VC: 1" | Freq: 100–2000 Hz (manufacturer spec)
- **Source:** SoundImports product page | Price: €59.95 | Stock: 8
- Note: 5mm Xmax — excellent. Fs 55 Hz → 2.72× at 150 Hz (matches DS115-8). Foam surround — less common in hi-fi, can age. Norex composite paper. Not recommended for reflex boxes (per SI).

### SB Acoustics SB12NRXF25-4 — Catalogue
- Size: 4" | Imp: 4Ω | Sensitivity: 87 dB | Power: 30W RMS | Fs: 61 Hz | Xmax: 5mm | Surround: foam | Freq: 100–2000 Hz | VC: 25.4mm
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb12nrxf25-4.html | Price: €62.45 | Stock: 6
- Note: Foam surround version with slightly higher Fs (61 Hz) than SB12NRX25-4. 5mm Xmax excellent. Foam surrounds can degrade over time. 5 stars from reviews — "gem in this class."

### SB Acoustics SB12MNRX25-4 — Catalogue
- Size: 4" | Imp: 4Ω | Sensitivity: 88.5 dB | Power: 30W RMS | Fs: 58 Hz | Xmax: 2.3mm | Cone: natural fibers | Surround: butyl rubber (high damping)
- **Source:** SoundImports product page | Price: €62.45 | Stock: in stock
- Note: High-damping surround for non-resonant character. 88.5 dB — needs −3.5 dB pad. Xmax only 2.3mm for a €62 driver.

### SB Acoustics SB12MNRX2-25-4 — Catalogue
- Size: 4" | Imp: 4Ω | Sensitivity: 91 dB | Power: 50W RMS | Fs: 58 Hz | Qts: 0.27 | Qms: 3.60 | Qes: 0.29 | Xmax: 4.4mm | Vas: 6.3 L | OD: 123mm | Cone: natural fibers | Surround: butyl rubber | VC: 25.4mm | Re: 3.2Ω | BL: 4.1 Tm
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb12mnrx2-25-4.html | Price: €61.95 | Stock: 10+
- Note: Updated version of MNRX25-4. Significantly higher sensitivity (91 vs 88.5 dB) and power (50 vs 30W). Qts 0.27 very low — well-damped, easy to place in any enclosure. Xmax 4.4mm excellent. Low Qts means strong bass control. 150 Hz crossover: 58 Hz → 2.59× margin (solid).

### SB Acoustics SB12PFC25-4 — Catalogue (OOS or same as PFCR25-4)
- Size: 4" | Imp: 4Ω | Sensitivity: 87.5 dB | Power: 30W RMS | Fs: 58 Hz | Xmax: 5mm | Qts: 0.43 | Vas: 5.1 L | Cone: natural fiber paper | Surround: butyl rubber | VC: 1"
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb12pfc25-4.html | Price: listed (status unclear)
- Note: Near-identical specs to SB12PFCR25-4 already in this catalogue. May be an older designation for the same driver. If in stock, effectively interchangeable with PFCR25-4.

### SB Acoustics SB12PAC25-4 — Catalogue (OOS)
- Size: 4" | Imp: 4Ω | Sensitivity: 87 dB | Power: 30W RMS | Fs: 52.5 Hz | Xmax: 5mm | Qts: 0.31 | Cone: aluminum | OD: 108.9mm
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb12pac25-4.html | Price: listed | Stock: OOS
- Note: Similar specs to SB12PACR25-4 (same Fs, Xmax, Qts). May be older designation. OD 108.9mm slightly smaller than Willy's HiFi PACR (122mm) — different chassis sourcing or model revision.

### Peerless by Tymphany HDS-P830870 — Catalogue (pre-order)
- Size: 4" | Imp: 8Ω | Price: €49.95 | Stock: pre-order
- **Source:** https://www.soundimports.eu/en/peerless-by-tymphany-hds-p830870.html
- Note: Specs not retrieved (URL returned 404 on direct fetch; confirmed via search). Pre-order only.

### Visaton WS 13 E — Catalogue
- Size: 5" | Imp: 8Ω | Sensitivity: 86 dB | Power: 40W RMS / 60W max | Fs: 83 Hz | Xmax: 0.75mm | Vas: 7.4 L | Cone: paper | Freq: 83–12,000 Hz
- **Source:** SoundImports product page | Price: €21.95 | Stock: 9
- Note: 5" paper cone with very low Xmax (0.75mm). Fs 83 Hz → 1.81× at 150 Hz. Designed for small multimedia enclosures. Budget-friendly at €21.95. Xmax 0.75mm will limit maximum SPL near crossover.

### Visaton SC 13 — Catalogue
- Size: 5" | Frame OD: 162mm | Imp: 8Ω | Sensitivity: 90 dB | Power: 40W RMS / 60W max | Fs: 78 Hz | Xmax: 0.75mm | Vas: 7.4 L | Cone: cellulose | VC: 20mm | BL: 4.2 Tm | Depth: 62mm
- Magnetically shielded.
- **Source:** https://www.soundimports.eu/en/visaton-sc-13.html | Price: €32.95 | Stock: 8
- Note: 90 dB well-matched to sub. Large 162mm OD — would dominate a 190mm baffle. Xmax only 0.75mm (same concern as WS 13 E). Shielded. Good Fs (78 Hz → 1.92× at 150 Hz). Cellulose cone.

### Markaudio CHN-70 — Catalogue
- Size: ~5" | Imp: 8Ω | Sensitivity: 86.7 dB | Power: 16W RMS / 50W max | Fs: 71.6 Hz | Xmax: 4mm | Cone: paper | Freq: ~70–20,000 Hz
- Full-range driver.
- **Source:** SoundImports product page | Price: €32.45 | Stock: 4
- Note: Full-range. 16W RMS is low but 50W max suggests thermal limit is 50W. 4mm Xmax solid for a 5". Fs 71.6 Hz → 2.1× at 150 Hz. Only 4 in stock.

### SB Acoustics SB13PFC25-8 — Catalogue
- Size: 5" | Imp: 8Ω | Sensitivity: 87 dB | Power: 40W RMS | Fs: 45 Hz | Cone: natural fiber paper | VC: 1"
- **Source:** SoundImports product page | Price: €28.45 | Stock: 7
- Note: Fs 45 Hz → 3.33× at 150 Hz (excellent Fs margin). 87 dB near-matched. 40W solid. 8Ω: ~31W at 24V available — just within rating. Consider 29V supply for thermal headroom.

### SB Acoustics SB13PFC25-4 — Catalogue
- Size: 5" | Imp: 4Ω | Sensitivity: 89 dB | Power: 40W RMS | Fs: 44 Hz | Xmax: 4.5mm | Qts: 0.29 | Vas: 0.47 ft³ (13.3 L) | Cone: natural fiber paper (proprietary in-house)
- **Source:** https://www.soundimports.eu/en/sb-acoustics-sb13pfc25-4.html | Price: listed | Stock: see SoundImports
- Note: 4Ω version — 61W at 24V available (massive headroom). 89 dB well-matched. Fs 44 Hz → 3.41× at 150 Hz. Low Qts (0.29) suits active DSP crossover well. Xmax 4.5mm excellent. Note: this is probably the same as the SB13PFCR25-4 already listed (model number cross-check needed).

### Dayton Audio RS75T-8 — Catalogue
- Size: 3" | Frame: truncated cast (not fully circular) | Imp: 8Ω | Sensitivity: 84.3 dB | Power: 15W RMS / 30W max | Fs: 189 Hz | Cone: black anodized aluminum
- **Source:** SoundImports product page | Price: €49.95 | Stock: 6
- Note: Fs 189 Hz is extremely high → min xover 378 Hz. Suitable only as a dedicated midrange starting above 400 Hz — not a typical mid-woofer. Black anodized aluminum cone. Truncated cast frame. 15W modest. Reference Series quality.

### Dayton Audio RS125-4 — Catalogue
- Size: 5" | Frame: cast aluminum (6 mounting holes) | Imp: 4Ω | Sensitivity: 89.9 dB | Power: 30W RMS | Fs: 57.2 Hz | Xmax: 4mm | Cone: aluminum | Freq: 65–5,400 Hz
- Two short-circuit paths in motor. Rubber surround.
- **Source:** https://www.soundimports.eu/en/dayton-audio-rs125-4.html | Price: €66.95 | Stock: 10+
- Note: Reference Series aluminum cone. 89.9 dB near-perfect match. Fs 57.2 Hz → 2.62× at 150 Hz. 4mm Xmax. Cast aluminum frame (cast frames are typically circular). Premium price at €66.95.

### Dayton Audio RS125P-4 — Catalogue
- Size: 5" | Frame: cast (6 holes) | Imp: 4Ω | Sensitivity: 90 dB | Power: 30W RMS / 45W max | Fs: 70 Hz | Cone: paper/Kevlar/glass composite | VC: 25mm Cu/Al | Phase plug: solid aluminum
- **Source:** https://www.soundimports.eu/en/dayton-audio-rs125p-4.html | Price: €64.95 | Stock: 9
- Note: Proprietary composite paper cone. Aluminum phase plug (may be silver-coloured). 90 dB near-perfect. Fs 70 Hz → 2.14× at 150 Hz. Reviewer noted lack of dust cover makes it unsuitable for non-downfiring applications.

ions.

tions.

ions.

s.

