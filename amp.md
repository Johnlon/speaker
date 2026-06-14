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

Per-driver power requirements (watts needed per channel at reference SPL) are in [drivers.md](drivers.md). Per-pairing PSU voltage and current figures are in [combos.md](combos.md).

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

### Minimum PSU voltage formula

**V_min = √(P_needed × 2R / η)** where η = 0.85

Per-driver P_needed figures are in [drivers.md](drivers.md). The table below shows what power each voltage step makes available at each impedance:

> At 29V and above: 4Ω channels (sub, tweeter) can exceed sub's 80W max and most tweeter ratings. **DSP channel limiters are mandatory at any supply above 24V.**

---

### Options for Improving Headroom

#### Option 1 — Higher-voltage PSU (simplest)

Swap to a Mean Well LRS-150-27, LRS-150-29, or LRS-150-30. These are the same footprint (159×97×30 mm) as the 24V version.

| Supply | P into 8Ω | P into 4Ω | Net result |
|--------|-----------|-----------|-----------|
| 24V | 31W | 61W | Adequate for most 8Ω mids at RMS; 4Ω mid has full headroom |
| 27V | 39W | 77W | 8Ω mid approaching burst headroom |
| 29V | 45W | 89W | 8Ω mid has burst parity with sub; 4Ω mid very comfortable |
| 32V | 54W | 109W | All mid impedances comfortable at RMS and burst |
| **36V** | **69W** | **138W** | **JAB5 rated operating voltage — full spec.** DSP channel limiters mandatory (sub ≤80W, tweeter per rating). |

**Sweet spot: 29V** — gives burst headroom for 8Ω mids without requiring extreme DSP limiting. Cost: £15–20.

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

29V LRS-200-29 + 40,000 µF cap bank = maximum headroom with minimum transient impedance. Best all-round solution for 8Ω mid drivers.

**Combined effect:** At 29V with 40 mF on the rail, the mid channel delivers the full 44.7W for the duration of any musical transient — sufficient for any 8Ω mid driver in the field. The system is transient-complete.

#### Option 4 — 4Ω mid driver (most elegant, no PSU change)

A 4Ω mid driver at 24V into 4Ω gives the JAB5 ~61W per channel — more than double what any 8Ω mid gets. Burst headroom is easy with no PSU upgrade.

Trade-off: the mid channel draws twice the current at the same SPL — check total PSU current budget. Per-driver analysis in [drivers.md](drivers.md).

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

Per-driver PSU recommendations are in [drivers.md](drivers.md). Per-pairing recommendations are in [solutions.md](solutions.md).

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

Formula: **Correction (dB) = 85 − driver_sensitivity**

A positive value means the channel needs gain; negative means attenuation. Per-driver correction figures are in [drivers.md](drivers.md). The ADAU1701 handles corrections in both directions with no signal degradation.

### Loudness compensation

Implement a gentle bass shelf boost (~4–6 dB centred on 60–80 Hz) that diminishes as the master volume control rises. This replicates the Google Home Max automatic loudness feature — the system sounds full and warm at low volumes, then delivers flat extended response at full tilt.

> SigmaStudio implementation: use a volume-dependent signal path where a bass boost filter is blended in inverse proportion to the volume control position. The ADAU1701's lookup table and multiplier blocks are sufficient for this.
