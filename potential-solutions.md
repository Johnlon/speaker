# Potential Solutions — Mid + Tweeter Pairings

All combinations evaluated against the locked subwoofer: **Tang Band W5-1138SMF** (85 dB, 4Ω, 40W/80W, Fs 45 Hz).

Driver specifications are in [drivers.md](drivers.md).

> **June 2026 update:** Visual constraints removed by owner instruction. Appearance is noted for reference only — no driver is excluded on grounds of cone colour, dome material, frame shape, or phase plug colour. Ranking criteria order: (1) acoustic fit, (2) engineering compatibility, (3) practical fit.

---

## System Reference

- Sub at 40W RMS: 85 + 10×log(40/2) = **98 dB @1m** (continuous reference)
- Sub burst at 80W: 85 + 10×log(80/2) = **101 dB @1m** (transient ceiling)
- PSU / amp power (JAB5, η = 0.85, full H-bridge class D):

| Supply | 8Ω channel | 4Ω channel |
|--------|------------|------------|
| 24V | 31W | 61W |
| 29V (recommended — LRS-200-29) | **45W** | **90W** |
| 36V (JAB5 rated max) | 69W | 139W |

- Crossover targets: sub LP 150 Hz (LR24) · mid BP 150–2,800 Hz · tweeter HP 2,800 Hz (LR48)

---

## Beaming Limits — Maximum Useful Mid/Tweeter Crossover

f_beam = c / (π × a), where a = √(Sd/π)

| Mid | Sd | Cone dia | Beams above |
|-----|----|----------|-------------|
| DSA90-8 | 35 cm² | 67 mm | **3,260 Hz** |
| ND91-4 (3.5") | ~50 cm² est | ~80 mm | ~2,730 Hz |
| SB12PFCR/MNRX2-25-4 (4") | 50 cm² | 80 mm | **2,730 Hz** |
| DS115-8 | 54.1 cm² | 83 mm | 2,636 Hz |
| HiVi B4N | ~54 cm² | ~83 mm | ~2,636 Hz |
| SPM-116/8 / Beyma 4FR40 / DA115-8 (4") | ~54 cm² | ~83 mm | ~2,600 Hz |
| TCP115-8 / SIG120-4 (4") | ~56 cm² | ~85 mm | ~2,570 Hz |
| Celestion TF0510 | 78.5 cm² | 100 mm | 2,185 Hz |
| HiVi M5N (5") | ~78 cm² | ~100 mm | ~2,185 Hz |
| SB13PFC25-8 / SDS-P830656 (5–5.25") | 86–87 cm² | ~105 mm | ~2,080 Hz |
| SIG150-4 (5.25") | 96 cm² | 110 mm | **1,990 Hz** |

---

## Tweeter Minimum Crossover (2× Fs rule)

| Tweeter | Fs | Min xover |
|---------|----|-----------|
| XT25TG30-04 (ring radiator) | 440 Hz | **880 Hz** — lowest of any candidate |
| DX25TG59-04 | 590 Hz | 1,180 Hz |
| SB29RDNC-C000-4 / SB29RDC-C000-4 | 580–600 Hz | 1,160–1,200 Hz |
| SB29SDAC-C000-4 | 600 Hz | 1,200 Hz |
| SB26ADC-C000-4 | 680 Hz | 1,360 Hz |
| RST28F-4 | 710 Hz | 1,420 Hz |
| SB26ST-C000-5 | 870 Hz | 1,740 Hz |
| XT25SC90-04 (ring radiator) | 825 Hz | 1,650 Hz |
| XT25BG60-04 (ring radiator) | 570 Hz | 1,140 Hz |
| D27TG35-06 | 900 Hz | 1,800 Hz |
| SB26STCN-C000-4 | 950 Hz | 1,900 Hz |
| **SB19ST-C000-4** | **980 Hz** | **1,960 Hz** ← reference tweeter |
| XT25SC40-04 (ring radiator) | 1,018 Hz | 2,036 Hz |
| D2606/920000 | 1,100 Hz | 2,200 Hz |
| CF18N-4 | 1,100 Hz | 2,200 Hz |
| DT-28N | 1,200 Hz | 2,400 Hz |
| SEAS H1406-04 | ~1,250 Hz (est) | ~2,500 Hz |
| ND25FA-4 / BC25SC06-04 | 1,350 Hz | 2,700 Hz |
| DC25T-8 | 1,468 Hz | 2,936 Hz |
| HiVi TN25 | 1,500 Hz | 3,000 Hz |
| DT-25N | 1,600 Hz | 3,200 Hz |
| Markaudio TW 6 | 1,700 Hz | **3,400 Hz** — highest; very constrained pairing window |

---

## Ranked Pairings

### Tier S — Outstanding all-rounders

**S1 · DS115-8 + SB19ST**
- Xover: 2,500 Hz | Centre spacing: 102 mm (0.75λ) | Price: €36.95 + €21.45 = **€58 (~£50)** — or ~£41 using Falcon UK tweeter (£14.30)
- Mid (8Ω, 85.3 dB): −0.3 dB | 18.6W at 98 dB (31W available at 24V — 66% headroom; 45W at 29V — 142% ✓)
- Tweeter (4Ω, 88.5 dB, Fs 980 Hz): −3.5 dB | 17.8W at 98 dB (within 30W ✓)
- Fs margin: 55.2 Hz → **2.72× at 150 Hz** — best of any paper-cone mid
- Beaming 2,636 Hz — 2,500 Hz crossover is below limit ✓
- **Why S1:** Confirmed dark coated-paper cone (datasheet-verified). Warm, musical character exactly matching the GHM-inspired tonal goal. SB19ST 19 mm dome = widest HF dispersion of any tweeter candidate — directly addresses the 60° off-axis kitchen position. Near-zero DSP correction. Best Fs margin. Only concern: 4 units left at SoundImports — order now.

---

**S2 · SB12PFCR25-4 + SB19ST**
- Xover: 2,700 Hz | Centre spacing: 105 mm (0.78λ) | Price: €25.95 + €21.45 = **€47 (~£41)**
- Mid (4Ω, 87.5 dB): −2.5 dB | 11.2W at 98 dB (61W at 24V — massive headroom ✓)
- Tweeter: −3.5 dB | 17.8W ✓
- Fs margin: 58 Hz → **2.59× at 150 Hz** — excellent
- Beaming 2,730 Hz — 2,700 Hz crossover sits just inside limit ✓
- **Why S2:** Natural fibre paper cone — warm, organic character. 10+ units both drivers at SoundImports — no stock pressure. Cheaper than S1. At woofer max (101 dB), mid needs 44.7W vs 30W rated — cap sub at ~40W with DSP limiter (practical fix). This is the default order if DS115-8 sells out, and arguably the better value choice regardless.

---

**S3 · SB12MNRX2-25-4 + SB29SDAC-C000-4** ← premium pick
- Xover: 1,200–2,700 Hz (1,500 Hz window for experimentation) | Centre spacing: ~107 mm | Price: €61.95 + €44.95 = **€107 (~£92)**
- Mid (4Ω, 91 dB, Qts 0.27): −6 dB | **10W** at 98 dB (90W at 29V → 800% headroom ✓)
- Tweeter (4Ω, 93 dB, Fs 600 Hz): −8 dB | 6.3W (within 60W ✓)
- Beaming 2,730 Hz. SB29SDAC min xover 1,200 Hz → wide crossover latitude.
- **Why S3:** Engineering showcase within the £100 limit. Both drivers have extraordinary power margins — this system cannot be clipped by the mid or tweeter at any realistic kitchen SPL. SDAC ring dome construction (stabilising ring reduces distortion vs standard dome) improves off-axis dispersion vs a conventional dome. MNRX2's Qts 0.27 = highly controlled transient behaviour through the midrange. Natural fibre + ring dome = warm-to-neutral character with wide dispersion.

---

### Tier A — Very good; specific strengths

**A1 · HiVi B4N + SB19ST**
- Xover: 2,500 Hz | Spacing: 102 mm | Price: **€44 (~£38)**
- Mid (8Ω, 85 dB): **0 dB correction** — perfect natural match to sub | 20W at 98 dB (31W at 24V ✓)
- Tweeter: −3.5 dB | 17.8W ✓
- Fs: 56 Hz → 2.68× at 150 Hz. 10+ stock both.
- **Best for:** Simplest possible DSP — zero EQ needed on the mid channel. Reliable, good value, always in stock. Al/Mg cone (copper-tone anodising — appearance noted). Power at woofer max: 40W vs 25W RMS — cap sub at 35W via DSP. Best choice when you want a working system quickly without EQ fuss.

---

**A2 · SB12MNRX2-25-4 + SB19ST**
- Xover: 2,700 Hz | Spacing: 105 mm | Price: **€83 (~£72)**
- Mid (4Ω, 91 dB): −6 dB | 10W at 98 dB (90W at 29V → 800% headroom). Mid channel is never the limiting component at any volume.
- **Best for:** Maximum dynamic capability within the £100 budget using the 19 mm tweeter for best off-axis performance. Qts 0.27 gives very well-controlled midrange transients. Natural fibre cone, warm character. If the listening involves wide dynamic range content (classical, jazz) and you want the amp channel to never struggle, this is the pick.

---

**A3 · DSA90-8 + SB19ST**
- Xover: 2,800 Hz | Spacing: **90 mm** (0.66λ — tightest round pairing) | Price: **€56 (~£49)**
- Mid (8Ω, 84.7 dB): +0.3 dB | 21.4W at 98 dB (marginal at 24V — 31W available; 29V gives 45W ✓)
- Tweeter: −3.5 dB | 17.8W ✓
- Beaming 3,260 Hz — 2,800 Hz crossover is comfortable below limit ✓
- **Best for:** Smallest mid footprint (OD 92 mm) → narrowest baffle, tightest centre spacing. 90 mm at 2,800 Hz = 0.66λ — best lobing geometry of any round pairing. Black anodised aluminium cone. Consider raising sub/mid crossover to 165 Hz (Fs 66.6 Hz → 2.48× instead of 2.25×).

---

**A4 · DS115-8 + DX25TG59-04**
- Xover: 1,800–2,500 Hz | Spacing: 110 mm | Price: **€70 (~£60)**
- Mid: −0.3 dB | 18.6W ✓ | Tweeter (4Ω, 93.4 dB, Fs 590 Hz): −8.4 dB | 5.8W (limiter at 12W for burst protection ✓)
- **Best for:** Paper warmth + the most flexible crossover point of any standard-dome tweeter (Fs 590 Hz → min 1,180 Hz). Crossover window 1,800–2,500 Hz. If EQ tuning suggests moving the crossover point, this pair accommodates it without new hardware. DX25TG59-04's ferrofluid cooling adds thermal safety margin.

---

**A5 · SB12PFCR25-4 + DX25TG59-04**
- Xover: 1,800–2,700 Hz | Spacing: 110 mm | Price: **€59 (~£51)**
- Same concept as A4: natural fibre warmth + flexible crossover. Better stock and lower price than A4. Choose this if DS115-8 sells out.

---

**A6 · Beyma 4FR40 + SB19ST**
- Xover: 2,500 Hz | Spacing: 103 mm | Price: €30.95 + €21.45 = **€52 (~£45)**
- Mid (8Ω, 87 dB): −2 dB | 12.6W at 98 dB (24V adequate ✓). OD 118.2 mm. 10+ in stock.
- **Best for:** Paper + Santoprene surround = warm, punchy character. 40W AES rating gives comfortable headroom. Beyma build quality (Spanish PA manufacturer, good components). Full-range design extends cleanly above the 2,500 Hz crossover.
- **Note:** Fs not explicitly published; likely ~80–100 Hz. If Fs is at 100 Hz, 150 Hz crossover = 1.5× — marginal. Confirm Fs from datasheet before ordering.

---

**A7 · SPM-116/8 + SB19ST**
- Xover: 2,500 Hz | Spacing: 102 mm | Price: €21.45 + €21.45 = **€43 (~£37)**
- Mid (8Ω, 87 dB): 12.6W at 98 dB — 24V adequate ✓. Paper cone. 40W/80W power.
- **Best for:** Cheapest paper-cone pairing in the catalogue at ~£37. Monacor construction. Works on 24V.
- **Note:** Fs 75 Hz → 2.0× at 150 Hz — adequate but the tightest of the paper-cone mids. Consider raising sub/mid crossover to 165 Hz.

---

**A8 · SIG120-4 + SB19ST** ← in stock at Audiophonics FR; ships to UK
- Xover: 2,500 Hz | Centre spacing: 105 mm | Price: ~€34.90 (Audiophonics) + €21.45 = **~€56 (~£48)**
- Mid (4Ω, 89.7 dB): 13.5W at 98 dB — 24V supply delivers 61W into 4Ω → 352% headroom. No PSU upgrade ever needed.
- Beaming 2,570 Hz — 2,500 Hz crossover is below limit ✓
- **Best for:** Best amplifier headroom of any 4" mid candidate — the 4Ω load gives the mid channel 61W at 24V while only needing 13.5W. Black single-piece anodised dish. The system will never be amp-limited on the mid channel regardless of programme material. Single order at Audiophonics FR.

---

### Tier B — Good; notable trade-offs

**B1 · TCP115-8 + SB19ST** — warmest character; requires 29V PSU
- Xover: 2,500 Hz | Spacing: 102 mm | Price: **€35 (~£31)** — cheapest pairing overall
- Mid (8Ω, 81.9 dB): +3.1 dB | 40.7W at 98 dB. Needs 29V (45W available → adequate with DSP limiting ✓). At 24V (31W available): under-powered by 9.7W — mid channel soft-clips.
- Fs: 59.2 Hz → 2.53× at 150 Hz. Xmax 4.0 mm. Universally the warmest, punchiest character of any mid evaluated.
- **Trade-off:** Requires LRS-200-29 PSU upgrade (~£25). Factor into build budget. With 29V the system is fully viable.

---

**B2 · ND91-4 + SB19ST** — Xmax champion in compact form
- Xover: 2,700 Hz | Spacing: 97 mm | Price: **€55 (~£48)**
- Mid (4Ω, 85.6 dB): −0.6 dB | 34.8W at 98 dB (90W at 29V ✓ — 159% headroom). Rated 30W RMS; needs DSP limiter at 30W (limits max SPL to ~97.4 dB — close enough).
- Fs unconfirmed (freq response starts 65 Hz; likely ~70–80 Hz → ~2.0× at 150 Hz — adequate).
- **Best for:** Xmax 4.6 mm is the highest of any small mid candidate. 3.5" driver = compact footprint, tight baffle. Black anodised aluminium cone. 4Ω mid provides better amp headroom than 8Ω equivalents.
- **Note:** Confirm Fs from datasheet before ordering.

---

**B3 · HiVi M5N + DX25TG59-04** — 5" driver, exceptional Fs margin
- Xover: 1,200–2,100 Hz | Spacing: ~103 mm | Price: €29.95 + €32.95 = **€63 (~£54)**
- Mid (8Ω, 87 dB): −2 dB | 12.6W ✓. Fs 50 Hz → **3.0× at 150 Hz** — best Fs margin of any new candidate. 5" driver beams above 2,185 Hz.
- **Why DX25TG59-04 not SB19ST:** SB19ST min xover is 1,960 Hz, but M5N beams at 2,185 Hz — the window is only 225 Hz wide. DX25TG59-04 (min 1,180 Hz) opens the window to 1,200–2,100 Hz. Al/Mg cone, shielded. 35W/70W rating.

---

**B4 · SB13PFC25-8 + DX25TG59-04** — 5" natural fibre, outstanding Fs
- Xover: 1,200–2,080 Hz | Spacing: ~110 mm | Price: €28.45 + €32.95 = **€61 (~£53)**
- Mid (8Ω, 87 dB): −2 dB | 12.6W ✓. Fs 45 Hz → **3.33× at 150 Hz** — best Fs margin of all drivers evaluated. Natural fibre paper cone — warm character. 40W RMS.
- **Why DX25TG59-04:** Same reason as B3 — SB19ST's 1,960 Hz minimum crossover leaves insufficient margin below the 2,080 Hz beaming limit of this 5" driver.

---

**B5 · DA115-8 + SB19ST** — budget aluminium, near-perfect sensitivity
- Xover: 2,500 Hz | Spacing: 102 mm | Price: **€51 (~£44)**
- Mid (8Ω, 84.9 dB): +0.1 dB | 20.4W at 98 dB. 20W RMS rating — just over (same marginal situation as DSA90-8). Fs 60 Hz → 2.5×. Only 3 in stock.
- **Best for:** Near-perfect sensitivity match at lower cost than DSA90-8. Aluminium cone — analytical character. Budget option when stock and price matter.

---

**B6 · DSA90-8 + HiVi TN25** — tightest spacing of any pairing
- Xover: 3,000 Hz | Centre spacing: **73 mm** (0.64λ) | Price: **€60 (~£52)**
- Mid: +0.3 dB ✓ | Tweeter (5Ω, 91 dB, Fs 1,500 Hz): −6 dB | 8W ✓
- **Best for:** Absolute minimum acoustic centre separation — 73 mm at 3,000 Hz. The TN25's 54×54 mm square face fits directly against the DSA90-8 cone. Square faceplate is the visual note (not an exclusion). TN25 depth 63.5 mm — check enclosure clearance.
- **Note:** TN25 Fs 1,500 Hz → min xover 3,000 Hz. Response starts at 2,500 Hz, only 500 Hz below crossover — tight but protected by LR48 HP filter.

---

**B7 · SDS-P830656 + DX25TG59-04** — Xmax 10 mm, truncated frame
- Xover: 1,500–2,000 Hz | Spacing: ~105 mm | Price: **€63 (~£54)**
- Mid (8Ω, 86.1 dB): −1.1 dB | Fs 65 Hz → 2.3× | Xmax **10 mm** — highest of any mid by a large margin. Beams above 2,080 Hz.
- **Best for:** Extraordinary mechanical headroom — this driver physically cannot over-excite at 150 Hz crossover at any realistic SPL. Truncated 152×134 mm frame (appearance noted — not excluded). DX25TG59-04 (Fs 590 Hz) keeps the crossover at 1,500–2,000 Hz, below beaming limit. 60W RMS power — no thermal concern.

---

**B8 · SIG150-4 + DX25TG59-04** — large mid, low crossover concept
- Xover: 1,500–1,990 Hz | Spacing: 128 mm | Price: ~**€70 (~£60)**
- Mid (4Ω, 91.1 dB): −6.1 dB | 9.8W at 98 dB (61W at 24V — 522% headroom ✓). Beams above 1,990 Hz. Frame OD 152 mm — very wide.
- **Best for:** Maximum amplifier headroom in a front-baffle sub layout (Option B). The SIG150-4 + DX25TG59-04 combination allows a crossover below 2,000 Hz that no other tweeter in this catalogue (except XT25TG30-04) can match. Best suited when speaker is aimed at the listener rather than pointing straight ahead.
- **Trade-off:** 152 mm OD leaves only 19 mm each side on a 190 mm baffle. Off-axis 40–50° is audibly coloured above 2 kHz.

---

**B9 · SB12PACR25-4-COAX** — point-source; SPL ceiling 94 dB
- Xover (internal): 2,800 Hz | Centre spacing: **0 mm** | Price: **€68 (~£59)**
- Integrated tweeter: 10W rated. At 98 dB reference it needs 22.4W → overdriven. Max system SPL: ~94 dB @1m. Sub must be DSP-limited to ~18W to match.
- **Best for:** True acoustic point source — zero time offset at crossover, no lobing at any angle. Uniquely coherent imaging. Adequate for background/moderate kitchen SPL. Uses JAB5's fourth amp channel for the tweeter.

---

**B10 · DSA90-8 + ND25FA-4** — tightest round spacing
- Xover: 2,700 Hz | Spacing: **79 mm** (0.58λ) | Price: **€51 (~£44)**
- ND25FA-4: 66 mm OD — smallest tweeter faceplate evaluated. Analytical character throughout.
- **Best for:** Minimum round-frame centre separation. Best lobing geometry of any all-round-driver pair. Choose if baffle width is tightly constrained.

---

**B11 · DSA90-8 + DT-28N** — compact tweeter, very tight spacing
- Xover: 2,500 Hz | Spacing: **~82 mm** | Price: €34.95 + €40.95 = **€76 (~£65)**
- Mid (8Ω, 84.7 dB): 21.4W at 98 dB — 24V adequate ✓ (31W available, marginal; 29V gives 45W ✓)
- Tweeter (8Ω, 94 dB, Fs 1,200 Hz, 50W, cutout 50 mm, depth 21 mm): 2.5W at 98 dB — barely loaded. Fs 1,200 Hz → min xover 2,400 Hz.
- **Best for:** DT-28N is one of the most compact tweeters in the catalogue (50 mm cutout, 21 mm depth, estimated OD ~72 mm). Paired with the DSA90-8 (92 mm OD) it gives ~82 mm centre-to-centre — almost as tight as the TN25 combination and with a neater round (or near-round) faceplate. 50W tweeter power rating. 8Ω across both drivers → 24V supply adequate for both. Neodymium tweeter motor.
- **Visually:** DT-28N's small integrated waveguide faceplate sits cleanly above the DSA90-8. Both are compact. The spacing is tight enough that the pair reads as a unit rather than two separate elements.

---

**B12 · SLS-85S25CP04-04 + DT-28N** — non-round mid + compact tweeter, aesthetic pairing
- Xover: 2,500 Hz | Spacing: **~82 mm** (91 mm axis vertical) | Price: €29.95 + €40.95 = **€71 (~£61)**
- Mid (4Ω, 86 dB, oval-rectangular 105×91 mm, Xmax 10.2 mm): 31.7W at 98 dB — **requires 29V** (90W available at 29V into 4Ω ✓). Paper cone. Fs 73 Hz → 2.05× at 150 Hz.
- Tweeter: same as B11 — 2.5W at 98 dB ✓
- Beaming for SLS (~3.5"): ~2,730 Hz — 2,500 Hz crossover is below limit ✓
- **Best for:** The SLS-85S25CP04-04's oval 105×91 mm frame has a non-circular but visually coherent look — something between round and rectangular. With the 91 mm dimension vertical and DT-28N immediately above, the pair is close and proportionally matched. Xmax 10.2 mm gives outstanding mechanical headroom at 150 Hz crossover — this driver cannot be over-excursed at any realistic kitchen SPL. Paper cone for warm character.
- **Trade-off:** Requires 29V PSU (LRS-200-29 ~£25). At burst (101 dB), mid needs 63.4W vs 30W rated — DSP sub limiter mandatory to cap system SPL at ~97 dB (where mid needs 31.7W — within rating). Still loud enough for full kitchen listening.

---

### Ring Radiator Pairings

Ring radiators (XT25 family) produce inherently wide, controlled dispersion through their annular geometry — directly benefiting the 60° off-axis kitchen position. The XT25TG30-04 additionally has the lowest Fs of any tweeter evaluated (440 Hz → 880 Hz minimum crossover).

**RR1 · DS115-8 + XT25TG30-04** — warm paper + widest crossover window
- Xover: 880–2,636 Hz (any point in this range) | Spacing: 113 mm | Price: €36.95 (SI) + £29.90 (Falcon) ≈ **~£62**
- Mid: −0.3 dB | 18.6W ✓ | Tweeter (4Ω, 91.9 dB, Fs 440 Hz): −6.9 dB | 8.2W. DSP limiter at 13W mandatory (burst needs 16.3W vs 15W rated — limiter caps tweeter at 100 dB max; sub peaks at 101 dB, 1 dB gap is inaudible).
- **Best for:** Paper warmth + ring radiator off-axis dispersion + the widest crossover tuning window of any pairing in this project. During EQ optimisation, the crossover can be moved anywhere across a 1,800 Hz range without new hardware.

---

**RR2 · SB12PFCR25-4 + XT25TG30-04** — natural fibre + ring radiator
- Xover: 880–2,730 Hz | Spacing: 116 mm | Price: €25.95 (SI) + £29.90 (Falcon) ≈ **~£52**
- Same concept as RR1 at lower cost. Natural fibre warmth + ring radiator dispersion. 10+ stock mid.
- **Best value ring radiator pairing.** If off-axis performance at 60° is the primary driver and budget is under £55, this is the choice.

---

**RR3 · SB12MNRX2-25-4 + XT25TG30-04** — maximum headroom + ring radiator
- Xover: 880–2,730 Hz | Spacing: 116 mm | Price: €61.95 (SI) + £29.90 (Falcon) ≈ **~£83**
- Mid (4Ω, 91 dB): 10W at 98 dB (90W available at 29V → 800% headroom). Natural fibre cone.
- **Best for:** The engineering-first ring radiator build. Mid channel is essentially unloaded at all kitchen SPLs. Combined with the ring radiator's off-axis advantage, the best-performing system for the 60° listening geometry under £100.

---

**RR4 · DSA90-8 + XT25SC90-04** — budget UK ring radiator; single Falcon order
- Xover: 2,800 Hz | Spacing: 91 mm | Price: Falcon UK ~**£37** (both in stock)
- Tweeter (4Ω, 90.1 dB, 100W): 12.3W at 98 dB (within 100W — enormous safety margin). Fs 825 Hz → min 1,650 Hz.
- **Best for:** Cheapest ring radiator pairing. Both drivers UK stock, single order from Falcon Acoustics, no import. XT25SC90-04 100W rating means the tweeter will outlast the build. Compact: 91 mm centre spacing.

---

**RR5 · SIG150-4 + XT25TG30-04** — only tweeter that properly works with SIG150-4
- Xover: 1,000–1,990 Hz | Spacing: 140 mm | Price: ~**£67**
- SB19ST's 1,960 Hz minimum crossover leaves only 30 Hz margin below SIG150-4's 1,990 Hz beaming limit — no practical room. DX25TG59-04 (min 1,180 Hz) gives a 810 Hz window. XT25TG30-04 (min 880 Hz) gives the full 1,000–1,990 Hz range.
- **Trade-off:** SIG150-4 OD 152 mm, very wide baffle. Off-axis 40–50° suffers above 2 kHz.

---

**RR6 · DS115-8 + SB29SDAC-C000-4** — ring dome + paper warmth
- Xover: 1,200–2,636 Hz | Spacing: ~110 mm | Price: €36.95 + €44.95 = **€82 (~£71)**
- Mid: −0.3 dB | 18.6W ✓ | Tweeter (4Ω, 93 dB, Fs 600 Hz): −8 dB | 6.3W (vs 60W → massive ✓)
- **Best for:** Paper cone warmth + SB29 ring dome construction. The SDAC's stabilising ring reduces distortion at the crossover region vs a conventional dome. Min xover 1,200 Hz gives 1,400 Hz of tuning flexibility. Within the £100 budget.
- **Note:** SB29RDNC (€68.45) is the neodymium upgrade — 1 dB higher sensitivity (94 dB), same Fs. SDAC (€44.95, 10 in stock) is the value choice.

---

### Tier C — Weaker specs

**C1 · RS100-8 + SB19ST** — Fs margin too tight
- ~€70. Fs 92 Hz → 1.63× at 150 Hz — tightest Fs margin of any mid. Analytical character.

**C2 · PA130-8 + SB19ST** — Xmax 2 mm, marginal Fs
- ~€55. Xmax 2 mm + Fs 1.8× at 150 Hz + OD 132 mm = three weaknesses simultaneously.

**C3 · Celestion TF0510 + SB19ST** — weakest Fs and Xmax
- ~£52. Fs 106 Hz (1.42× at 150 Hz). Xmax 1.1 mm. Paper-Kevlar character is interesting but specs are weakest of the field.

**C4 · DSA90-8 + Markaudio TW 6** — crossover above beaming limit
- ~€80 (~£69). TW 6 Fs 1,700 Hz → min xover 3,400 Hz. DSA90-8 beams at 3,260 Hz — required crossover sits above the mid's beaming limit. Off-axis at 40–50° will show a mid-frequency dip. TW 6's waveguide narrows dispersion further. Only consider if speaker is aimed directly at the listener and TW 6 appearance is the priority.

---

## Budget Recommendations

### Best picks under £50 (mid + tweeter combined)

Order at SoundImports unless noted. No PSU change required. All pairings use 24V supply.

| Rank | Pairing | Approx price | Character | Why |
|------|---------|-------------|-----------|-----|
| **1** | SB12PFCR25-4 + SB19ST | ~£41 (SI) / ~£37 (Falcon tweeter) | Warm, natural | Best value in the catalogue: natural fibre warmth, 10+ stock, no PSU upgrade |
| **2** | HiVi B4N + SB19ST | ~£38 | Warm | Zero DSP correction; simplest setup; always in stock |
| **3** | SPM-116/8 + SB19ST | ~£37 | Warm | Cheapest paper-cone pairing; adequate specs |
| **4** | DSA90-8 + XT25SC90-04 | ~£37 (Falcon both) | Detailed, wide dispersion | Cheapest ring radiator option; single UK order |
| **5** | DSA90-8 + SB19ST | ~£49 | Detailed | Tightest round spacing; narrowest baffle; compact build |

**Warm on a budget:** SB12PFCR25-4 + SB19ST at ~£37–41. No other combination at this price gives natural-fibre warmth combined with a 19 mm dome.

**Absolute minimum spend:** TCP115-8 + SB19ST at ~£31 — but add £25 for LRS-200-29 PSU (required); total ~£56 crosses the £50 threshold. Still the cheapest complete solution.

---

### Best picks under £100 (mid + tweeter combined)

These pairings justify the higher spend with a clear, specific upgrade over the budget tier.

| Rank | Pairing | Approx price | Character | Why it justifies the spend |
|------|---------|-------------|-----------|--------------------------|
| **1** | DS115-8 + SB19ST | ~£50 (SI) / ~£41 (Falcon tweeter) | Warm, musical | Reference pairing; confirmed paper warmth + best off-axis tweeter. **Order now — 4 units left.** |
| **2** | SB12MNRX2-25-4 + SB29SDAC | ~£92 | Warm-neutral, dynamic | 800% mid headroom + ring dome; engineering showcase; 1,500 Hz xover window |
| **3** | RR1: DS115-8 + XT25TG30-04 | ~£62 | Warm + wide dispersion | Paper warmth + ring radiator off-axis advantage + widest xover window of any pairing |
| **4** | RR2: SB12PFCR25-4 + XT25TG30-04 | ~£52 | Warm + wide dispersion | Same ring radiator benefit at lower cost; best value under £100 for off-axis performance |
| **5** | A2: SB12MNRX2-25-4 + SB19ST | ~£72 | Warm, dynamic | Best dynamic headroom with conventional tweeter; natural fibre |

**Ring radiator vs conventional dome:** The XT25TG30-04 costs ~£16 more than the SB19ST at Falcon. For a speaker where the listener is frequently at 60°, the ring radiator's controlled wide dispersion is a directly audible benefit. RR2 (SB12PFCR25-4 + XT25TG30-04) at ~£52 is the strongest single upgrade argument in the catalogue.

**If DS115-8 sells out** before ordering: move to S2 (SB12PFCR25-4 + SB19ST) or RR2 — both are always in stock and both stay under £50.

---

## Quick Reference — All Pairings

| ID | Mid | Tweeter | Xover | Spacing | Price | Character | Key reason for rank |
|----|-----|---------|-------|---------|-------|-----------|-------------------|
| S1 | DS115-8 | SB19ST | 2,500 Hz | 102 mm | ~£50 | Warm | Confirmed paper warmth + 19 mm dome; 4 left — order now |
| S2 | SB12PFCR25-4 | SB19ST | 2,700 Hz | 105 mm | ~£41 | Warm, natural | Best value; 10+ stock; natural fibre |
| S3 | SB12MNRX2-25-4 | SB29SDAC | 1,200–2,700 Hz | ~107 mm | ~£92 | Warm-neutral | 800% headroom; ring dome; engineering showcase |
| A1 | HiVi B4N | SB19ST | 2,500 Hz | 102 mm | ~£38 | Warm | Sensitivity-matched to sub; simple DSP |
| A2 | SB12MNRX2-25-4 | SB19ST | 2,700 Hz | 105 mm | ~£72 | Warm, dynamic | Max 4Ω headroom; natural fibre |
| A3 | DSA90-8 | SB19ST | 2,800 Hz | 90 mm | ~£49 | Detailed | Tightest round spacing; narrowest baffle |
| A4 | DS115-8 | DX25TG59-04 | 1,800–2,500 Hz | 110 mm | ~£60 | Warm, flexible | Paper warmth + widest standard-dome xover |
| A5 | SB12PFCR25-4 | DX25TG59-04 | 1,800–2,700 Hz | 110 mm | ~£51 | Warm, flexible | A4 concept; cheaper |
| A6 | Beyma 4FR40 | SB19ST | 2,500 Hz | 103 mm | ~£45 | Warm | Paper+Santoprene; confirm Fs before ordering |
| A7 | SPM-116/8 | SB19ST | 2,500 Hz | 102 mm | ~£37 | Warm | Cheapest paper mid |
| A8 | SIG120-4 | SB19ST | 2,500 Hz | 105 mm | ~£48 | Clear, dynamic | 4Ω mid; 352% amp headroom; Audiophonics FR |
| B1 | TCP115-8 | SB19ST | 2,500 Hz | 102 mm | ~£31 | Warmest | Cheapest overall; **29V PSU required** |
| B2 | ND91-4 | SB19ST | 2,700 Hz | 97 mm | ~£48 | Detailed | Xmax 4.6 mm; compact 3.5"; **29V preferred** |
| B3 | HiVi M5N | DX25TG59-04 | 1,200–2,100 Hz | ~103 mm | ~£54 | Warm | 5"; Fs 3.0×; needs DX25 not SB19ST |
| B4 | SB13PFC25-8 | DX25TG59-04 | 1,200–2,080 Hz | ~110 mm | ~£53 | Warm | Fs 45 Hz (3.33×); natural fibre 5" |
| B5 | DA115-8 | SB19ST | 2,500 Hz | 102 mm | ~£44 | Detailed | Near-perfect sensitivity match |
| B6 | DSA90-8 | HiVi TN25 | 3,000 Hz | 73 mm | ~£52 | Detailed | Tightest spacing (73 mm); square tweeter |
| B7 | SDS-P830656 | DX25TG59-04 | 1,500–2,000 Hz | ~105 mm | ~£54 | Natural | Xmax 10 mm; truncated frame |
| B8 | SIG150-4 | DX25TG59-04 | 1,500–1,990 Hz | 128 mm | ~£60 | Neutral | Large mid; low xover; very wide baffle |
| B9 | SB12PACR25-4-COAX | built-in | 2,800 Hz | 0 mm | ~£59 | Clear | Point source; 94 dB SPL ceiling |
| B10 | DSA90-8 | ND25FA-4 | 2,700 Hz | 79 mm | ~£44 | Detailed | Tightest round spacing (79 mm) |
| B11 | DSA90-8 | DT-28N | 2,500 Hz | ~82 mm | ~£65 | Detailed | Compact neo tweeter; tight spacing; 24V ok |
| B12 | SLS-85S25CP04-04 | DT-28N | 2,500 Hz | ~82 mm | ~£61 | Warm | Oval mid + compact tweeter; Xmax 10.2 mm; 29V needed |
| RR1 | DS115-8 | XT25TG30-04 | 1,000–2,636 Hz | 113 mm | ~£62 | Warm + wide | Best ring radiator; widest xover window |
| RR2 | SB12PFCR25-4 | XT25TG30-04 | 1,000–2,730 Hz | 116 mm | ~£52 | Warm + wide | Best value ring radiator |
| RR3 | SB12MNRX2-25-4 | XT25TG30-04 | 1,000–2,730 Hz | 116 mm | ~£83 | Warm + max headroom | Max headroom + ring radiator |
| RR4 | DSA90-8 | XT25SC90-04 | 2,800 Hz | 91 mm | ~£37 | Detailed + wide | Budget UK ring; single Falcon order |
| RR5 | SIG150-4 | XT25TG30-04 | 1,000–1,990 Hz | 140 mm | ~£67 | Neutral | Only tweeter for SIG150-4 |
| RR6 | DS115-8 | SB29SDAC | 1,200–2,636 Hz | ~110 mm | ~£71 | Warm + ring dome | Ring dome + paper warmth; wide xover |
| C1 | RS100-8 | SB19ST | 2,500 Hz | 93 mm | ~£60 | Detailed | Fs 1.63× — tightest margin |
| C2 | PA130-8 | SB19ST | 2,000 Hz | 110 mm | ~£47 | Natural | Xmax 2 mm; Fs 1.8× |
| C3 | TF0510 | SB19ST | 2,200 Hz | ~110 mm | ~£45 | Natural | Weakest Fs + Xmax |
| C4 | DSA90-8 | TW 6 | 3,200–3,400 Hz | 83 mm | ~£69 | Detailed | Xover above beaming limit; poor 60° performance |

---

## Power Summary — Mids at 98 dB Reference

The key question for each mid is whether 24V (31W/8Ω, 61W/4Ω) is sufficient, or whether 29V is required. **Prefer 24V** — smaller, cheaper PSU.

| Mid | Imp | Sens | Power at 98 dB | Rating | PSU needed | Margin |
|-----|-----|------|----------------|--------|------------|--------|
| SB12MNRX2-25-4 | 4Ω | 91 dB | 10W | 50W | **24V** | 510% |
| SIG120-4 | 4Ω | 89.7 dB | 13.5W | 40W | **24V** | 352% |
| SB12PFCR25-4 | 4Ω | 87.5 dB | 11.2W | 30W | **24V** | 445% |
| HiVi M5N | 8Ω | 87 dB | 12.6W | 35W | **24V** | 146% |
| SPM-116/8 | 8Ω | 87 dB | 12.6W | 40W | **24V** | 146% |
| Beyma 4FR40 | 8Ω | 87 dB | 12.6W | 40W | **24V** | 146% |
| SB13PFC25-8 | 8Ω | 87 dB | 12.6W | 40W | **24V** | 146% |
| DS115-8 | 8Ω | 85.3 dB | 18.6W | 35W | **24V** | 66% |
| HiVi B4N | 8Ω | 85 dB | 20.0W | 25W | **24V** | 55% |
| DA115-8 | 8Ω | 84.9 dB | 20.4W | 20W | **24V** | marginal — limiter |
| DSA90-8 | 8Ω | 84.7 dB | 21.4W | 20W | **24V** | marginal — limiter |
| SLS-85S25CP04-04 | 4Ω | 86 dB | 31.7W | 30W | **29V** | marginal RMS |
| ND91-4 | 4Ω | 85.6 dB | 34.8W | 30W | **29V** | exceeds RMS — limiter |
| TCP115-8 | 8Ω | 81.9 dB | 40.7W | 40W | **29V required** | deficit at 24V |

> Formula: 8Ω P = 10^((98−sens)/10). 4Ω P = 2×10^((98−sens)/10). Amp: P = V²/(2R) × 0.85.

---

## Power Summary — Tweeters at 98 dB Reference

| Tweeter | Imp | Sens | Power needed | Rating | Notes |
|---------|-----|------|-------------|--------|-------|
| Markaudio TW 6 | 4Ω | 98 dB | 2W | 15W | Negligible draw |
| DT-28N | 8Ω | 94 dB | 2.5W | 50W | Negligible draw |
| SB29RDNC | 4Ω | 94 dB | 5.0W | 100W | Massive headroom |
| XT25SC40-04 | 4Ω | 94 dB | 5.0W | 100W | Massive headroom |
| RST28F-4 | 4Ω | 93.5 dB | 5.6W | 80W | 14× over-rated |
| DX25TG59-04 | 4Ω | 93.4 dB | 5.8W | 15W | Fine ✓; limiter at 12W |
| SB29SDAC | 4Ω | 93 dB | 6.3W | 60W | Massive headroom |
| SB26STCN | 4Ω | 92 dB | 8.0W | 120W | Massive headroom |
| HiVi TN25 | 5Ω | 91 dB | 8.0W | 20W | Fine ✓ |
| XT25TG30-04 | 4Ω | 91.9 dB | 8.2W | 15W | Fine ✓; limiter at 13W |
| XT25SC90-04 | 4Ω | 90.1 dB | 12.3W | 100W | Massive headroom |
| CF18N-4 | 4Ω | 90 dB | 12.6W | 40W | Fine ✓ |
| ND25FA-4 | 4Ω | 90 dB | 12.6W | 20W | Fine ✓ |
| SB19ST | 4Ω | 88.5 dB | 17.8W | 30W | Fine ✓ |

---

## Supplier Notes (June 2026)

- **SoundImports** (EU) — primary source for most drivers
- **Falcon Acoustics** (UK) — SB19ST £14.30, XT25TG30-04 £29.90, XT25SC90-04 £18.20, DX25TG59-04 £20.85 — UK stock, no import delay
- **Audiophonics** (France) — SIG120-4 available, ships to UK
