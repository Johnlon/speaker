# Amplifier & Electronics

---

## Sure Electronics JAB5 (AA-AB32184)

**Role:** Main amplifier + DSP board. Drives all three channels: subwoofer, midrange, tweeter.

- **Channels:** 4 (3 used: sub, mid, tweeter; 1 spare)
- **Rated power:** 4×100W @ 6Ω (at higher voltage supply — not the 24V target)
- **Supply voltage range:** 10–39V DC
- **DSP:** ADAU1701 (Analog Devices) — programmed in SigmaStudio
- **Bluetooth:** BT5.0 with aptX HD codec
- **THD:** 0.07% (rated)
- **S/N ratio:** 100 dB (rated)
- **Idle current:** ~0.5A at 24V
- **Source:** [Sure Electronics store](https://store.sure-electronics.com/product/756) — JavaScript-rendered; specs also confirmed via [Audiophonics product page](https://www.audiophonics.fr/en/) (fetched June 2026)
- **Datasheet:** [research/jab5_datasheet.pdf](research/jab5_datasheet.pdf) | [original URL](https://files.sure-electronics.com/download/JAB5_Datasheet.pdf) (downloaded June 2026)

### Power at 24V supply (operational figures)

Class D full H-bridge formula: **P = V² / (2 × R) × η**, where η ≈ 0.85.
The rated 100W/ch is specified at **36V into 6Ω** (confirmed in official datasheet — no 24V or 8Ω figures are given). At 24V, derived from first principles:

| Load | Formula | Available power |
|------|---------|-----------------|
| 4Ω (sub, tweeter) | 24² / (2×4) × 0.85 | **~61W** |
| 6Ω (rated load) | 24² / (2×6) × 0.85 | **~41W** |
| 8Ω (mid channel) | 24² / (2×8) × 0.85 | **~31W** |

> **JAB5 datasheet note (confirmed June 2026):** The official datasheet specifies only 100W/ch at 36V into 6Ω. No per-channel figure at 24V into 8Ω is published. The ~31W into 8Ω at 24V above is derived from the standard Class D formula — it is the best available estimate and will not be superseded by a manufacturer figure. The ~31W figure is the binding constraint for the mid driver choice — see PSU Voltage section below.

### Power budget at full volume (24V supply)

| Channel | Driver | Imp | Power needed | Available @ 24V | Headroom |
|---------|--------|-----|--------------|-----------------|----------|
| Sub | TB W5-1138SMF | 4Ω | 40W RMS | ~61W | 53% |
| Mid — SIG120-4 (OOS) | SIG120-4 | 4Ω | 13.5W | ~61W | 352% |
| Mid — DS115-8 | DS115-8 | 8Ω | 18.6W | ~31W | 66% |
| Mid — HiVi B4N | HiVi B4N | 8Ω | 20.0W | ~31W | 55% |
| Mid — DSA90-8 | DSA90-8 | 8Ω | 21.4W | ~31W | 45% |
| Mid — TCP115-8 | TCP115-8 | 8Ω | 40.7W | ~31W | **Deficit — 9.7W short** |
| Tweeter | SB19ST | 4Ω | 17.8W | ~61W | 243% |

Total DC draw at sustained full output: ~165W. The LRS-150-24 is rated 156W — tight for continuous sine-wave full power. Real music is far lower average power. Real music crest factor is 10–15 dB (rock) to 20 dB (classical); average power is typically 1/10 to 1/20 of peak.

---

## Power Supply — Mean Well LRS-150-24

- **Output:** 24V DC, 6.5A continuous (156W)
- **Input:** 85–264V AC
- **Efficiency:** ~87% at full load
- **Dimensions:** 159 × 97 × 30 mm
- **Intended mounting:** Sealed electronics vault in base of enclosure (26 mm height)
- **Thermal concern:** PSU in sealed vault generates heat. At full load (~165W DC draw / ~87% efficiency) the PSU itself dissipates ~23W. Sealed vault needs a thermal calculation to verify the PSU stays within its operating temperature range. The Mean Well LRS-150-24 is rated to 70°C ambient at full load, with derating above 50°C.

> **Open action:** Calculate or measure vault temperature rise at sustained full-load operation. If a sealed vault cannot maintain <50°C, options are: ventilation slot on rear panel, slight oversizing to LRS-200-24 (200W, same footprint), or derating operation at sustained high levels.

---

## PSU Voltage — Headroom Analysis

### Minimum voltage for each mid at RMS level (matched to sub at 98 dB)

Formula: V_min = √(P_needed × 2R / η)

| Mid | P needed (8Ω) | V_min for RMS | Available @ 24V | Fine at 24V? |
|-----|--------------|---------------|-----------------|-------------|
| DSA90-8 | 21.4W | **20.0V** | 31W (45% headroom) | Yes |
| TCP115-8 | 40.7W | **27.7V** | 31W (**deficit**) | **No** |

### Minimum voltage for burst headroom (matching sub at 80W burst → 101 dB)

At burst, each mid must produce 2× its RMS operating power.

| Mid | P at burst (8Ω) | V_min for burst | Fine at 24V? | Fine at 29V? |
|-----|----------------|-----------------|-------------|-------------|
| DSA90-8 | 42.7W | **28.4V** | No | Yes (44.7W @ 29V, tight) |
| TCP115-8 | 81.3W | **39.1V** | No | No (44.7W @ 29V — still short) |

**At 36V (JAB5 rated supply), all driver candidates are comfortably powered.** TCP115-8 gets 69W into 8Ω vs 40.7W needed — 70% headroom. DSP limiters are mandatory at this voltage; without them the 4Ω sub and tweeter channels see 138W, which would destroy both.

**At 29V, DSA90-8 achieves near-burst parity with the sub** — adequate for all candidates except TCP115-8.

> Caution: At 29V into 4Ω, the sub and tweeter channels can deliver ~89W — above the sub's 80W max and far above the tweeter's 30W rating. DSP channel limiters are **mandatory** at any voltage above 24V.

---

### Options for Improving Headroom

#### Option 1 — Higher-voltage PSU (simplest)

Swap to a Mean Well LRS-150-27, LRS-150-29, or LRS-150-30. These are the same footprint (159×97×30 mm) as the 24V version.

| Supply | P into 8Ω | P into 4Ω | Net result |
|--------|-----------|-----------|-----------|
| 24V | 31W | 61W | TCP115-8 under-powered at 8Ω; DSA90-8 RMS fine; SIG120-4 (4Ω) very comfortable |
| 27V | 39W | 77W | DSA90-8 RMS fine; approaching burst headroom |
| 29V | 45W | 89W | DSA90-8 has burst parity; TCP fine |
| 32V | 54W | 109W | All 8Ω mids comfortable at RMS and burst |
| **36V** | **69W** | **138W** | **JAB5 rated operating voltage — full spec.** All drivers comfortable. DSP channel limiters mandatory (sub ≤80W, tweeter ≤30W). TCP115-8 now works easily. |

**Recommended:** 29V is the sweet spot — gives burst headroom for DSA90-8 without requiring extreme DSP limiting. Cost: £15–20.

**Side effect:** At 29V, total continuous power budget is ~165W × (29/24)² = ~240W DC. The LRS-150-24 cannot supply this. Move to LRS-200-29 or LRS-200-30 (~£25) for the higher voltage option.

#### Option 2 — Bulk capacitor bank (interesting sub-project ★)

A capacitor reservoir mounted close to the JAB5 board prevents the supply rail from sagging during transient current demand. The Mean Well is optimised for steady-state; there's a 1–5 ms lag before PSU regulation catches up with a sudden peak load. During that lag, the rail sags and the amp clips earlier than it should.

**The calculation:**  
A 80W transient at 24V draws I = 80/24 = 3.33A. Over 10 ms with 1V sag allowed:  
C = I × t / ΔV = 3.33 × 0.010 / 1 = **33,000 µF**

A bank of 4× 10,000 µF / 35V keeps the rail above 23.2V for a 10 ms burst. With 40,000 µF total, effective sag is only 0.83V — the amp delivers near-theoretical power for the full duration of a musical transient.

**The build:**
- 4× Nichicon UHE or Panasonic FM series 10,000 µF / 35V (£5–8 each — use quality audio-grade caps)
- Mount in the base electronics vault, leads as short as possible to the JAB5 power input
- 6 mm² copper bus bar or wide PCB traces between cap bank and amp
- 10Ω / 5W wirewound or NTC thermistor in series at the PSU output — limits inrush current when caps charge at power-on
- 10 kΩ / 1W bleed resistor across the cap bank — discharges safely after power-off

**Effect:** Doesn't increase continuous power (that's determined by V and R). Does prevent the ~25% instantaneous power loss that occurs when the rail sags from 24V to ~22V during a drum hit. Genuinely audible improvement on transient cleanliness.

**Why it's interesting:** Copper bus bars, quality capacitors, measured before/after with a scope on the power rail. The kind of sub-project that makes a build feel engineered rather than assembled.

**Cost:** ~£30–40 in components. Recommended regardless of PSU voltage choice.

#### Option 3 — Higher voltage + cap bank (best of both)

29V LRS-200-29 + 40,000 µF cap bank = maximum headroom with minimum transient impedance. Recommended if committing to DSA90-8 and wanting transient performance to match the sub cleanly.

**Combined effect:** At 29V with 40 mF on the rail, the mid channel delivers the full 44.7W for the duration of any musical transient — well above the 42.7W needed by DSA90-8 at burst. The system is now transient-complete.

#### Option 4 — 4Ω mid driver (most elegant, no PSU change)

The SIG120-4 is a 4Ω midrange. At 24V into 4Ω, the JAB5 delivers ~61W — more than double what any 8Ω mid gets. Burst to 80W is easy.

If the SIG120-4 passes its spec check (Fs, Xmax, sensitivity — currently being fetched), it might be the cleanest solution: no PSU upgrade, no caps required, full headroom on the existing supply.

The catch is the impedance shift. The JAB5 mid channel at 4Ω draws twice the current at the same SPL — the PSU budget increases, and the DSP sensitivity correction (currently calculated for 8Ω drivers) needs recalculating.

#### Option 5 — Dual PSU, per-channel voltage (advanced project)

Two supplies:
- Sub + tweeter (4Ω channels): LRS-150-24 (24V — ample at 61W)
- Mid (8Ω channel): separate LRS-50-29 or LRS-75-29 (29V, 2–3A — mid peak current is ~2.5A)

Each channel gets the voltage it needs, independently regulated. No cross-channel interaction. The mid supply can also power the ADAU1701 DSP section if separated cleanly.

**Cost:** Adds £20–30 for a second small PSU, plus wiring complexity. Genuinely interesting to design and measure.

#### Option 6 — Boost converter on mid channel (exploratory)

A DC-DC boost module steps 24V up to 32V just for the mid channel. At 32V into 8Ω: P = 32²/16 × 0.85 = **54.4W** — comfortable for any 8Ω mid.

**Reality check:** Off-the-shelf boost modules (XL6009, LM2577 based) are noisy and marginal at 50W. A class D amplifier is sensitive to supply noise. This is viable as a later experiment but not for the first build. A proper synchronous boost converter with LC filtering would work — but at that point you're building a PSU, not buying one.

---

### Recommended Path

**Update (June 2026):** Research agent conclusions overridden. DS115-8 (dark coated paper cone — confirmed by official datasheet) and HiVi B4N (copper-tone anodising — owner-accepted) are both reinstated as candidates. Full field: SIG120-4 (OOS), DS115-8, HiVi B4N, DSA90-8, TCP115-8.

**First build:** 24V PSU is adequate for all mid candidates except TCP115-8. Add cap bank for transient cleanliness regardless of driver choice.

**With DS115-8 (top available candidate — paper cone, 4 units):** 24V fine (18.6W needed, 31W available). Best crossover margin (Fs 55.2 Hz, 2.72× at 150 Hz). Warm character. Recommend ordering before stock runs out.

**With HiVi B4N (zero DSP correction, 10+ stock):** 24V fine (20W needed, 31W available). Perfect sensitivity match (0 dB correction). Good Fs margin. Cheapest available pairing with SB19ST (~£37).

**With SIG120-4 (4Ω mid, OOS):** No PSU upgrade needed — ~61W available at 24V into 4Ω. Visually excellent. Fs 74.6 Hz gives slightly tighter crossover margin (2.01× at 150 Hz). Currently out of stock — watch SoundImports.

**With DSA90-8:** 24V fine. Compact frame, but aluminium mid character is more analytical than the GHM warmth target.

**With TCP115-8:** Needs 29V PSU — see Option 1 above.

---

## DSP — ADAU1701 (on JAB5 board)

Programmed via SigmaStudio (Analog Devices free software). All crossover, EQ, and level correction implemented in the DSP before the DAC stage.

### Crossover targets

| Stage | Filter type | Frequency | Slope |
|-------|-------------|-----------|-------|
| Sub low-pass | Linkwitz-Riley | 150 Hz | 24 dB/oct |
| Mid band-pass | LR | 150 Hz HP / 2,800 Hz LP | 24 dB/oct |
| Tweeter high-pass | LR | 2,800 Hz | 48 dB/oct |

### Level correction (vs TB sub at 85 dB reference)

| Driver | Correction | Reason |
|--------|------------|--------|
| DSA90-8 (mid) | +0.3 dB | Essentially zero — naturally matched |
| TCP115-8 (mid) | +3.1 dB | Sensitivity 3.1 dB below sub reference |
| SB19ST (tweeter) | −3.5 dB | Sensitivity 3.5 dB above sub reference |

### Loudness compensation

Implement a gentle bass shelf boost (~4–6 dB centred on 60–80 Hz) that diminishes as the master volume control rises. This replicates the Google Home Max automatic loudness feature — the system sounds full and warm at low volumes, then delivers flat extended response at full tilt.

> SigmaStudio implementation: use a volume-dependent signal path where a bass boost filter is blended in inverse proportion to the volume control position. The ADAU1701's lookup table and multiplier blocks are sufficient for this.
