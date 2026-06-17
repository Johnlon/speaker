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
- **Board dimensions:** 121.92 × 91.44 × 45.1 mm (L × W × H, H = component height including heatsink)
- **Source:** [Sure Electronics store](https://store.sure-electronics.com/product/756) — JavaScript-rendered; specs also confirmed via [Audiophonics product page](https://www.audiophonics.fr/en/) (fetched June 2026)
- **Datasheet:** [research/jab5_datasheet.pdf](research/jab5_datasheet.pdf) | [original URL](https://files.sure-electronics.com/download/JAB5_Datasheet.pdf) (downloaded June 2026)

### Power at 29V supply (selected operating voltage)

Class D full H-bridge formula: **P = V² / (2 × R) × η**, where η ≈ 0.85.
The rated 100W/ch is specified at **36V into 6Ω** (confirmed in official datasheet — no mid-voltage figures are published). At 29V:

| Load | Formula | Available power |
|------|---------|-----------------|
| 4Ω (sub, tweeter) | 29² / (2×4) × 0.85 | **~89W** |
| 6Ω (rated load) | 29² / (2×6) × 0.85 | **~60W** |
| 8Ω (mid channel) | 29² / (2×8) × 0.85 | **~45W** |

> **JAB5 datasheet note:** The official datasheet specifies only 100W/ch at 36V into 6Ω. All figures above are derived from the standard Class D formula. DSP channel limiters are mandatory — at 29V into 4Ω the sub and tweeter channels can deliver 89W; the sub is rated 80W peak and the tweeter must be limited per its own rating.

Per-driver power requirements (watts needed per channel at reference SPL) are in [drivers.md](drivers.md). Per-pairing PSU voltage and current figures are in [combos.md](combos.md).

---

## Power Supply — Target: 29V, ≥ 3A continuous (with cap bank)

**Selected supply voltage: 29V.** This gives 44.7W into 8Ω (DS115-8 mid) and 89.4W into 4Ω (sub, tweeter) — full burst headroom for all three drivers.

**Current requirements** (derived from scratch.py, drivers at 98/101 dB reference):

| Condition | Total power | Current at 29V + idle |
|-----------|------------|----------------------|
| RMS (98 dB continuous) | 66.6W | **2.80A** |
| Burst (101 dB peak) | 132.8W | **5.08A** |

With the 40,000 µF cap bank (see Option 2 below), the PSU only needs to supply RMS current (2.80A). The caps cover the burst delta (2.28A) for up to 10–50 ms with < 600 mV rail sag.

### PSU candidate — AliExpress SMPS (127 × 83 × 38 mm)

- **Dimensions:** 127 × 83 × 38 mm (fits base side-by-side with JAB5; 6.6 mm spare depth)
- **Price:** ~£24.59
- **Voltage to confirm:** must be ≥ 27.4V (29V target — check listing before ordering)
- **Current to confirm:** ≥ 5.1A for no cap bank; ≥ 3A with cap bank
- **Input:** 85–264V AC (verify on listing)

The Mean Well LRS-150-27 (159 × 97 × 30 mm) is 7.4 mm too deep to fit the current 215 mm cabinet side-by-side. It would require increasing cabinet depth to 225 mm external.

**Thermal note:** PSU in a semi-sealed base at full continuous load. At ~80W output / 87% efficiency, PSU self-dissipation is ~12W. The 80 mm base (56 mm internal) has limited natural convection. A 20 mm ventilation slot on the rear panel is recommended for sustained loud use.

> **Open action:** Confirm AliExpress PSU output voltage and current rating from the listing before ordering.

---

## PSU Voltage — Headroom Analysis

### Minimum PSU voltage formula

**V_min = √(P_needed × 2R / η)** where η = 0.85

Per-driver P_needed figures are in [drivers.md](drivers.md). The table below shows what power each voltage step makes available at each impedance:

> At 29V and above: 4Ω channels (sub, tweeter) can exceed sub's 80W max and most tweeter ratings. **DSP channel limiters are mandatory at any supply above 24V.**

---

### Options for Improving Headroom

#### Selected: 29V supply + capacitor bank

29V has been chosen as the operating voltage. At 29V the DS115-8 mid gets 44.7W and the sub gets 89.4W — both within headroom. DSP channel limiters cap sub at 80W and tweeter per its rating.

The capacitor bank (Option 2 below) is recommended alongside the 29V supply to handle burst transients cleanly.

#### Option 2 — Bulk capacitor bank (interesting sub-project ★)

A capacitor reservoir mounted close to the JAB5 board prevents the supply rail from sagging during transient current demand. Any switching PSU has a 1–5 ms regulation lag — during that window the rail sags and the amp clips earlier than it should.

**The calculation at 29V:**  
Burst draw = 5.08A. RMS draw = 2.80A. Cap must supply the difference (2.28A) for up to 10 ms:  
C = I × t / ΔV = 2.28 × 0.010 / 0.57 = **40,000 µF** (57 mV sag at 40 mF — effectively transparent)

**The build:**
- 4× Nichicon UHE or Panasonic FM series 10,000 µF / 35V (£5–8 each — use quality audio-grade caps)
- Mount in the base electronics vault, leads as short as possible to the JAB5 power input
- 6 mm² copper bus bar or wide PCB traces between cap bank and amp
- 10Ω / 5W wirewound or NTC thermistor in series at the PSU output — limits inrush current when caps charge at power-on
- 10 kΩ / 1W bleed resistor across the cap bank — discharges safely after power-off

**Effect:** At 29V with 40 mF cap bank, rail sag over a 10 ms burst is only 57 mV (29.0V → 28.4V). The PSU can be sized for RMS current (≥3A) rather than burst (≥5.1A). Genuine engineering improvement.

**Why it's interesting:** Copper bus bars, quality capacitors, measured before/after with a scope on the power rail. The kind of sub-project that makes a build feel engineered rather than assembled.

**Cost:** £30–40 in components. Strongly recommended.

---

Per-driver PSU figures are in [drivers.md](drivers.md). Per-pairing figures are in [combos.md](combos.md).

---

## DSP — ADAU1701 (on JAB5 board)

Programmed via SigmaStudio (Analog Devices free software). All crossover, EQ, and level correction implemented in the DSP before the DAC stage.

### Crossover targets

| Stage | Filter type | Frequency | Slope |
|-------|-------------|-----------|-------|
| Sub low-pass | Linkwitz-Riley | 150 Hz | 24 dB/oct |
| Mid band-pass | LR | 150 Hz HP / 1,500 Hz LP | 24 dB/oct |
| Tweeter high-pass | LR | 1,500 Hz | 48 dB/oct |

### Level correction (vs TB sub at 85 dB reference)

Formula: **Correction (dB) = 85 − driver_sensitivity**

A positive value means the channel needs gain; negative means attenuation. Per-driver correction figures are in [drivers.md](drivers.md). The ADAU1701 handles corrections in both directions with no signal degradation.

### Loudness compensation

Implement a gentle bass shelf boost (~4–6 dB centred on 60–80 Hz) that diminishes as the master volume control rises. This replicates the Google Home Max automatic loudness feature — the system sounds full and warm at low volumes, then delivers flat extended response at full tilt.

> SigmaStudio implementation: use a volume-dependent signal path where a bass boost filter is blended in inverse proportion to the volume control position. The ADAU1701's lookup table and multiplier blocks are sufficient for this.
