# Tweeter 60° Off-Axis — Collected Evidence (checkable)

Purpose: real measured polar/off-axis data for the tweeter shortlist, for the 60° kitchen geometry. Every row links a source you can open yourself. Graph-read values carry ±1–2 dB precision; where only a manufacturer plot exists that is stated. **Marketing words ("wide dispersion") are not evidence and are excluded.**

Reference: the disqualifying benchmark is RAW-CAt Ultimate Tweeter Shootout Part 6 (Nov 2025) — ring radiators measure horn-like at 60° (large deviation by 30°, severe rolloff by 60°). Goal: hold the kitchen-critical **2.8–10 kHz** band within a few dB at 60°.

> **⚠ CRITICAL CAVEAT #2 — Dayton datasheet off-axis is heavily SMOOTHED + loose QC.** Per [diyAudio "can I trust Dayton off-axis data"](https://www.diyaudio.com/community/threads/dayton-audio-tweeters-can-i-trust-off-axis-data.400624/): experienced members say the Dayton datasheet polars look "too good to be true," use heavy smoothing "that hides a lot off-axis," and batch-to-batch variance is wide. The **FRD data files Dayton provides are less smoothed and more honest** — use those, not the glossy plots. One member: like-for-like (0°/30° to 20 kHz) Dayton ≈ Peerless, i.e. the apparent Dayton off-axis edge is a smoothing artifact. **Net: NO manufacturer off-axis datasheet here is reliable — SB mislabels the angle (~15°), Dayton over-smooths. Trust only independent data (HiFiCompass, RAW-CAt UTS) + Dayton FRD files.**

> **⚠ CRITICAL CAVEAT #1 — SB Acoustics datasheet angles are optimistic.** HiFiCompass independently measured the SB21SDCN/RDCN and found the **datasheet's "60°" curve actually corresponds to the measured 45°** (and datasheet "30°" ≈ measured 20°) — see [the saved review](research/speakers/SB%20Acoustics%20SB21SDCN-C000-4%2C%20SB21RDCN-C000-4%20_%20HiFiCompass.pdf). All SB datasheets use the same method (IEC baffle, 31.6 cm), so **a "60°" reading off ANY SB datasheet below is really ~45° behaviour and the true 60° is worse.** This means the SB19ST and SB29SDAC datasheet 60° figures below are best-case; their *true* 60° needs an independent measured polar. Datasheet polar ≠ verified 60°.

---

## 0. Peerless by Tymphany NE19VTS-04 — ❌ OUT (conflicting datasheets)

**Withdrawn June 2026.** The official [Tymphany datasheet](https://cdn.shopify.com/s/files/1/0809/2387/files/NE19VTS-04.pdf) (local `research/speakers/NE19VTS-04_tymphany.pdf`) gives **88.29 dB @ 2.83V, Fs 742, 100 W** — vs the SoundImports sheet's 90.4 dB, 20 W, Fs 770. A 2 dB / 5× power disagreement between two manufacturer sheets = untrustworthy. Real sensitivity (~88 dB) ≈ SB19ST, and the 60° is ordinary (top-octave droop + notch ~28–30 kHz). Its two claimed edges (sensitivity, trustworthy data) both fail → out. Original analysis retained below for reference only.

### (reference, withdrawn) original NE19VTS-04 read

**Source (read directly):** [Tymphany datasheet, July 2025](https://doc.soundimports.nl/pdf/brands/Peerless%20by%20Tymphany/NE19VTS-04/NE19VTS.pdf) — local copy `research/speakers/Peerless_NE19VTS-04_datasheet.pdf`. Plots **On-axis / 30° / 60°.**

**Verified specs:** 19 mm fabric dome · neo · 4 Ω · Re 2.8 Ω · Sd 4.91 cm² · **Fs 770 Hz** · **90.4 dB/2.83V** · 20 W · **Ø52 mm faceplate** (compact, 3-bolt) · range 700–20 kHz.

**60° curve (read at 400 DPI via pdftoppm — curve ID by physics: red=on-axis, blue=30°, green=60°):**
| Freq | 60° vs on-axis |
|------|----------------|
| 200 Hz–5 kHz | ~0 to −1 dB (overlaid) |
| 6–7 kHz | **−5 dB localized dip** (diffraction at flange) |
| 8–10 kHz | −2 to −3 dB |
| 13 kHz | ~−4 dB |
| 15 kHz | ~−7 dB |
| 18–20 kHz | ~−9 dB, then steep |

**Internet opinion:** diyAudio — "all of those tweeters were fantastic," well-regarded NE series; one builder crossed it at 3,500 Hz/12 dB and "liked it a lot." Mild knock: one thread notes 2nd/3rd-harmonic THD slightly higher than some rivals for a given drive voltage (higher-order better above 1.6 kHz). Availability noted as thinning ("disappearing"). Sources: [diyAudio NE series](https://www.diyaudio.com/community/threads/peerless-ne-series-anyone-used-them.252871/), [Parts-Express](https://www.parts-express.com/peerless-by-tymphany-ne19vts-04-3-4-silk-dome-tweeter--264-1006).

**Why it leads:** lowest Fs of the shortlist (crosses ~1.5 kHz → cleanest window), most compact faceplate (Ø52), highest sensitivity (90.4 dB), and — decisively — its 60° comes from a **Tymphany datasheet with NO evidence of mislabelling** (unlike the SB sheets, proven ~15° optimistic). Power: max ~100.4 dB at 20 W → covers reference, 0.6 dB under burst (limiter, inaudible). The 6–7 kHz dip is the one thing to verify. **Still a manufacturer datasheet — an independent polar would make it bulletproof.**

---

## 1. SB Acoustics SB19ST-C000-4 — STRONGEST EVIDENCE (manufacturer 60° curve)

**Source (read directly):** [SB Acoustics datasheet PDF, REV.3](https://sbacoustics.com/wp-content/uploads/2020/05/SB19ST-C000-4.pdf) — local copy `research/speakers/SB19ST-C000-4_datasheet.pdf`. The datasheet plots **blue = on-axis, green = 30°, red = 60°** (IEC baffle, 31.6 cm, 2.83 V/1 m).
**Independent check:** [Parts-Express TechTalk measurement thread](https://techtalk.parts-express.com/forum/tech-talk-forum/65287-sb-acoustics-sb19st-c000-4-tested) ("damn near perfect out to 30 degrees").

**Verified specs (datasheet):** 19 mm fabric dome · 4 Ω · Re 3.4 Ω · Sd 3.8 cm² · **Fs 980 Hz** · **88.5 dB/2.83V** · 30 W · faceplate Ø88 mm · cutout Ø60 mm · 21 mm deep.

**60° curve (read at 400 DPI via pdftoppm — blue=on-axis, green=30°, red=60° per SB legend):**
| Freq | 60° vs on-axis |
|------|----------------|
| 1–6 kHz | ~0 to −1 dB (overlaid) |
| 8 kHz | ~−2 dB |
| 10–13 kHz | ~−3 to −4 dB |
| 15 kHz | ~−5 dB |
| 18–20 kHz | ~−7 dB |
| ~24 kHz | deep notch (irrelevant) |

**Internet opinion:** Parts-Express TechTalk independent test — off-axis "damn near perfect out to 30 degrees." Widely praised value: "a great tweeter at $50 and an unbelievable buy at $18," "an absolute bargain." Sources: [TechTalk test](https://techtalk.parts-express.com/forum/tech-talk-forum/65287-sb-acoustics-sb19st-c000-4-tested), [diyAudio build](https://www.diyaudio.com/community/threads/first-design-sb12pfcr25-4-sb19st-c000-4.408797/).

**Analysis:** smooth, monotonic roll-off on the datasheet — **no cliff in band.** BUT this is an SB sheet → its "60°" is really ~45° (HiFiCompass-proven, see caveat), so the **true 60° is worse than shown.** Fs 980 → crosses ~2 kHz. Strong reputation/value; 60° best-case but unconfirmed.

---

## 2. SB Acoustics SB29SDAC-C000-4 — manufacturer 60° curve (confirms owner reading)

**Source (read directly):** [SB Acoustics datasheet PDF, REV.0](https://sbacoustics.com/wp-content/uploads/2020/02/SB29SDAC-C000-4.pdf) — local copy `research/speakers/SB29SDAC-C000-4_datasheet.pdf`. Same blue/green/red = 0/30/60° convention.
**Independent check:** [HiFiCompass SB29SDAC measurement](https://hificompass.com/en/speakers/measurements/sbacoustics/sb-acoustics-sb29sdac-c000-4) · [LoudspeakerLab off-axis traces](https://loudspeakerlab.io/drivers/sb-acoustics/sb29sdac-c000).

**Verified specs (datasheet):** 29 mm fabric dome · 4 Ω · Re 3.0 Ω · Sd 9.6 cm² · **Fs 600 Hz** · **93 dB/2.83V** · 60 W · faceplate Ø103.8 mm · cutout Ø70 mm · 40.8 mm deep.

**60° curve, read off the datasheet:**
| Freq | 60° vs on-axis |
|------|----------------|
| ≤5 kHz | ~0 dB |
| 8 kHz | ~−2 dB |
| 10 kHz | ~−3 to −4 dB |
| 11 kHz | still OK |
| **12–14 kHz** | **CLIFF — deep notch, ~−15 to −20 dB** (red plunges to ~70 dB vs ~90 on-axis) |
| 17–18 kHz | partial recovery (~−12 dB) then dives again |

**Analysis:** **confirms the owner's reading exactly** — fine at 60° to ~10–11 kHz, then falls off a cliff at ~12 kHz (the 29 mm dome breaks up / cancels off-axis at the top). Critical 2.8–10 kHz band is fine; top octave collapses at 60°. Higher output and lower crossover than SB19ST (93 dB, Fs 600), but worse top-octave 60°.

---

## 2b. SB Acoustics SB21SDCN-C000-4 — compact; datasheet 60° good BUT proven optimistic

**Source (read directly):** [SB datasheet REV.1](https://doc.soundimports.nl/pdf/brands/SB%20Acoustics/SB21SDCN-C000-4/SB21SDCN-C000-4.pdf) — local copy `research/speakers/SB21SDCN-C000-4_datasheet.pdf`.
**Independent measurement (the important one):** [HiFiCompass review (saved)](research/speakers/SB%20Acoustics%20SB21SDCN-C000-4%2C%20SB21RDCN-C000-4%20_%20HiFiCompass.pdf) — measured this exact driver and found datasheet 60° = real 45°.

**Verified specs (datasheet):** 20 mm dome · neo · 4 Ω · Re 3.1 Ω · Sd 4.9 cm² · **Fs 850 Hz** · **90 dB/2.83V** · 40 W · **faceplate Ø58 mm · cutout Ø38 mm · 24 mm deep** (very compact → tightest mid-tweeter spacing of the dome shortlist).

**Datasheet 60° curve (read at 400 DPI via pdftoppm — blue=0, green=30°, red=60°):** ~0 to −1 dB to 6–7 kHz; −2 dB @ 10 k; −3 to −4 dB @ 13 k; −5 dB @ 15 k; −6 to −7 dB @ 18 k; notch ~21 k. Near-identical to SB19ST on paper, in a much smaller plate.

**Internet opinion:** HiFiCompass — "more airy and emotional"; a user (Madisound) — "wide dispersion and a very clear tone, surpassed my expectations," crossed at 2,400 Hz successfully. Compact (Ø58), well-built. Source: [Madisound listing](https://www.madisoundspeakerstore.com/soft-dome-tweeters-sb-acoustics/sb-acoustics-sb21sdcn-c000-4-dome-tweeter-neo-58mm/).

**Analysis — HiFiCompass review read in detail (Kozhushko, Dec 2020; full text + plots in the saved PDF):**
- Measured Fs **834 Hz** (vs 850 stated), measured sensitivity **89 dB** (1 dB below spec), on-axis flat 800 Hz–40 kHz, low distortion, usable down to 3 kHz.
- **Off-axis (the point):** *"both radiate well on the sides up to ~6 kHz, after which the radiation pattern begins to narrow"* → 60° is fine through the critical 2.8–6 kHz, narrowing is a **top-octave** problem. *"The dome has a wider dispersion than the ring radiator."* *"I would not say the dispersion in the upper octave is very good — from such a small size I expected better."* → even the dome is only **mediocre at 60° in the 10–20 kHz octave**.
- **Proves the datasheet optimism:** *"the datasheet 60° is more consistent in reality with the measured 45°, and datasheet 30° with measured 20°."* So the SB21SDCN datasheet "−6 dB at 60°" is really ~45° behaviour; **true 60° is worse.**
- Plot-read (approximate, thumbnail): normalized 0/15/30/45/60° curves within a couple dB to ~6–7 kHz, fanning to ~−10 to −20 dB by 20 kHz; 60° ~−4 to −6 dB around 10 kHz. **Exact dB-at-60° per frequency are NOT tabulated by the reviewer and not legible in the rendered thumbnail** — open the full-res `..._offaxis_normalized_5-30db.png` for precise values.

**Net:** SB21SDCN's *real* 60° is fine through the critical band but only mediocre in the top octave — not a standout. Its main value to this project is as the **one independent measurement that proves SB datasheet angles are ~15° optimistic**, which is why NE19VTS-04 (Tymphany sheet, no such proven flaw) currently outranks the SB pair on evidence quality.

## 3. Dayton ND13FA-4 / ND16FA-4 — only 45° published (no 60° from manufacturer)

- **ND13FA-4:** [datasheet (doc.soundimports.nl)](https://doc.soundimports.nl/pdf/brands/Dayton%20Audio/ND13FA-4/pdf_Dayton%20Audio_ND13FA-4_1.pdf) — polar shows **0/15/30/45° only**. Even to 45° (smallest 13 mm dome → widest dispersion). **60° not published.**
- **ND16FA-4:** Dayton FRD data files, off-axis to **45° only** — measured −3.1 dB @ 10 kHz, **−4.4 dB @ 13 kHz at 45°** (best 45° in the project). **60° not published** (the project's "~6–7 dB @ 60°" was an inference, not data).

**Analysis:** these micro-domes almost certainly have the *widest* true 60° of the field (physics: smallest diaphragm), but it is **unverified** — Dayton stops at 45°. Their blocker remains crossover (Fs 2,072–2,832 → 4–5.6 kHz floor), usable only with a high-beaming mid or steep DSP slope.

---

## 4. Monacor DT-100 / DT-28N — NO polar published (60° unknown)

- **DT-100:** [datasheet](https://doc.soundimports.nl/pdf/brands/Monacor/DT-100/pdf_monacor_DT-100_1.pdf) — local `research/speakers/Monacor_DT-100_datasheet.pdf`. **No off-axis plot.** The "wide dispersion" wording was the Willys listing, not Monacor.
- **DT-28N:** [datasheet](https://doc.soundimports.nl/pdf/brands/Monacor/DT-28N/pdf_monacor_DT-28N_1.pdf). **No off-axis plot.**

**Analysis:** no measured 60° evidence exists from the manufacturer, and no third-party polar found for either (budget Monacor, rarely independently measured). 25/28 mm diaphragms are *larger* than SB19ST's 19 mm → physically narrower top-octave, not wider. **Cannot be credited for 60° without a measurement you take yourself or a third-party polar.**

---

## Verdict on the evidence

## 5. SB Acoustics SB29RDNC-C000-4 — UTS GREEN off-axis, but notchy top octave (ring dome)

**Sources:** [SB datasheet](https://sbacoustics.com/wp-content/uploads/2020/02/SB29RDNC-C000-4.pdf) — local `research/speakers/SB29RDNC-C000-4_datasheet.pdf`; RAW-CAt UTS (green); [HiFiCompass SB29RDC](https://hificompass.com/en/speakers/measurements/sbacoustics/sb-acoustics-sb29rdc-c000-4) (sibling).
**Verified specs:** 29 mm ring dome · 4 Ω · Re 3.0 · **Fs 680 Hz · 94 dB/2.83V · 100 W** · Qts 0.45 · copper cap · Ø103.8 faceplate / Ø70 cutout.
**Off-axis — DOWNGRADED (datasheet + human-confirmed):** the SB datasheet 60° (red, read at 400 DPI) tracks to ~8–10 kHz then **drops out massively — deep notches ~−15 to −20 dB at 13–16 kHz**; **30° holds ~−5 dB**. Owner confirmed by eye: "massive dropout at 60°, ~5 dB at 30°." With the SB ~15° optimism the true 60° is worse still. The RAW-CAt UTS "GREEN" grade is **contradicted for the 60° gate** — it must reflect critical-band/lower-angle behaviour, not the top-octave 60° collapse.
**Verdict:** strong on Fs (crosses ~1.4 k), sensitivity (94 dB), power (100 W) — but its **60° off-axis is rough (massive top-octave dropout)**, plus large Ø104 faceplate (loose mid spacing) and ring-dome. **Not a good 60°-kitchen pick despite the UTS green.**

## 6. Dayton DC28 family (DC28F-8 / DC28FS-8 / DC28FT-8) — datasheet off-axis NOT trustworthy

**Sources:** Parts-Express datasheets (local `research/speakers/dayton_DC28F-8.pdf`, `dayton_275-075.pdf`=DC28FS-8, `dayton_DC28FT-8.pdf`); trust thread above.
**Verified specs (all 28 mm / 1‑1/8″ silk dome, 8 Ω, 50 W, 89 dB/1W):** DC28F-8 Fs 834, usable 1,300+; DC28FS-8 Fs 905, usable 1,600+ (shielded); **DC28FT-8 Fs 834, usable 1,300+, TRUNCATED faceplate → close mid spacing.**
**Off-axis — honest FRD data (DC28FT-8, Dayton's less-smoothed measured files, `research/speakers/dc28ft_data/`; 45° is widest measured):**
| Freq | 30° | 45° |
|---|---|---|
| ≤3 k | ~0 | ~0 |
| 5 k | −3.5 | **−5.1** |
| 10 k | −2.7 | −3.4 |
| 12 k | −3.1 | −3.3 |
| 15 k | −5.4 | **−7.8** |
| 18 k | −8.3 | −17.8 |
| 20 k | −11.1 | −32.9 |

Critical band (2.8–10 k) holds within ~3–5 dB at 45° — fine. **Top octave collapses** (−8 dB @ 15 k → −33 dB @ 20 k at 45°) = the 28 mm dome beaming, far steeper than a 19 mm. FRD also shows real ±2–3 dB **ripple** the glossy datasheet smoothed out (confirms Caveat #2). **No 60° (Dayton stops at 45°); 60° will be worse.**
**Verdict:** strengths = low Fs (cross ~1.3–1.7 k), 50 W, 89 dB, well-regarded sound (Tritrix / Affordable Accuracy Monitor), DC28FT truncated plate = tight mid spacing, cheap. Off-axis is fine in the critical band but gives up the top octave at wide angles and is unproven at 60°. A genuine value pick if top-octave-at-60° is treated as low priority (Zaph); the 19–20 mm domes hold dispersion measurably higher.

## Cross-source hard evidence — RAW-CAt UTS shootout + Zaph

**RAW-CAt "Ultimate Tweeter Shootout" spreadsheet** (`research/speakers/UTS off axis.xlsx`; same source family as the Part 6 data used to disqualify ring radiators). Colour key: GREEN = good, RED = bad, WHITE = ok. Off-axis is scored by "Split Hz" (where off-axis diverges) and "16 kHz ±". Our candidates:

| Driver (UTS row) | Mount mm | Sens | Lowest xover (distortion-limited) | Freq resp | High-Rez | **Off-axis grade** | Split / 16k± |
|---|---|---|---|---|---|---|---|
| **Vifa NE19VTS-04** | 36 | 86.6 | **4,500 Hz** | GREEN | GREEN+ | **WHITE (ok)** | 4.7 / **0** |
| **SB21SDCN-C000-4** | 37 | 86.7 | 3,500 Hz | GREEN | GREEN | **WHITE (ok)** | 4.1 / 2.8 |
| SB29RDNC-C000-4 | 56 | 91.8 | 2,500 Hz | GREEN | GREEN+ | **GREEN (good)** | 3 / 10.5 |
| SB19ST | — | — | — | — | — | **not in shootout** | — |

Signals: NE19VTS and SB21SDCN both grade only **"ok" (white)** off-axis here — not standouts — so "front-runner on off-axis" is overstated; they're equivalent. NE19VTS's **16 kHz deviation = 0** (best) and smallest mount (36 mm) are pluses; its **distortion-limited lowest crossover is 4,500 Hz** (higher than SB21SDCN's 3,500) — a caution echoed by the diyAudio THD note. **SB29RDNC** is graded GREEN off-axis in UTS — but this is **contradicted by its datasheet + owner's direct read: massive top-octave dropout at 60° (−15 to −20 dB @ 13–16 k), only 30° holds (~−5 dB).** So the UTS green reflects lower-angle/critical-band behaviour; its **true 60° is rough — not a good 60° pick** despite 94 dB / 100 W / low Fs.

**Zaph|Audio off-axis analysis** ([zaphaudio.com/offaxis.html](https://zaphaudio.com/offaxis.html)) — principle, not our specific drivers: **"the importance of top-octave [off-axis] response is highly overrated… everything to do with placement flexibility, nothing to do with sound quality"**; the real priority is **harmonic distortion near the crossover**. And **3/4″ domes "show very little off-axis droop."** → Our 19–20 mm picks are inherently fine off-axis; the 12–16 kHz droop we've been weighing matters less than distortion at the crossover.

**Net reconciliation:** the three small domes are all *adequate* off-axis (UTS "ok" + Zaph "3/4″ little droop"); the top-octave 60° differences are minor and, per Zaph, low-priority. The decision should weight **distortion-at-crossover + practicality** (size, sensitivity, price, stock) more than the top-octave droop. That keeps NE19VTS strong (tiny, clean 16k, green FR) but flags its higher distortion-limited crossover; SB21SDCN (low distortion, crosses lower, independent data) is fully level with it; SB29RDNC earns a fresh look on its GREEN off-axis grade.

---

| Tweeter | 60° data | Datasheet 60° reading | Caveat |
|---------|----------|------------------------|--------|
| ~~NE19VTS-04~~ | — | — | **OUT — conflicting datasheets (88.3 vs 90.4 dB; 100 vs 20 W); 60° ordinary** |
| **SB19ST** | SB datasheet 0/30/60 | graceful, −5–6 dB @ 13 k | datasheet 60° ≈ real 45° → true 60° worse; needs independent polar |
| SB21SDCN | SB datasheet + HiFiCompass | datasheet ~−6 dB top | HiFiCompass: datasheet 60° = real 45°; compact Ø58 |
| SB29SDAC | SB datasheet 0/30/60 | cliff −15–20 dB @ 12–14 k | datasheet 60° optimistic too → real worse |
| ND13/ND16FA | 45° only | excellent to 45° | 60° unpublished |
| TD20F-4 | 45° only | ~−3–4 dB @ 10 k @ 45° | 60° unpublished; crosses high (Fs 1,696) |
| DT-100 / DT-28N | none | — | no polar at all |

**Honest conclusion:** the SB datasheets make SB19ST, SB21SDCN and (to ~11 k) SB29SDAC *look* good at "60°," but **that "60°" is proven to be ~45° in reality** (HiFiCompass on SB21SDCN) — so the SB figures are best-case, not verified. On best-available evidence:
- ~~NE19VTS-04~~ — **OUT**: its two manufacturer datasheets conflict (88.3 vs 90.4 dB; 100 vs 20 W), real sensitivity ≈ SB19ST, 60° ordinary. No reliable edge.
- **SB19ST** — smoothest SB-datasheet roll-off, Fs 980, 30 W, strong reputation/value. Now the leading 19 mm dome by default; 60° from the mislabelled SB sheet → true 60° unconfirmed.
- **SB21SDCN** — compact (Ø58), good on the SB datasheet, same optimism caveat; its real polar is already in the HiFiCompass review on file.
- Everything else is crossover-limited (Dayton micro-domes, TD20F-4) or has no off-axis data (Monacor).

**The decisive next step:** cross-check NE19VTS-04 and SB19ST against *independent* measured polars (HiFiCompass / Erin's Audio Corner). NE19VTS-04 leads on current evidence because its datasheet 60° is the only one not under the SB mislabel cloud — an independent polar would make it bulletproof. Treat all SB "60°" figures here as ~45° best-case until measured.
