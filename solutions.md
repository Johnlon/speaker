# Solutions — Curated Recommendations

This document presents final curated driver recommendations for the kitchen counter monitor speaker build. All recommendations are evaluated on acoustic alignment, electrical compatibility, and physical constraints, **ignoring stock availability** to target the absolute best engineering and acoustic outcomes.

The speaker is designed to play alongside a dedicated active subwoofer (crossing over at 150 Hz), with system crossover and DSP alignment handled by an Analog Devices ADAU1701 DSP and a Wuzhi JAB5 amplifier (offering four channels powered by a 24V to 29V power supply). The owner's tonal reference is the classic British sound (e.g. B&W DM4).

---

## Best Overall Recommendations

For this specific project—a compact cabinet sitting on a kitchen counter where the listener is frequently situated at 60° off-axis—the ring radiator or ring dome design is acoustically mandatory. Standard domes suffer severe high-frequency rolloff at 60°, whereas ring radiators maintain flat, controlled off-axis response much higher into the treble. 

The three primary recommendations below target different optimization goals:

| Priority | ID | Midrange | Tweeter | Crossover | Price | PSU | Why |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Best Overall (Burnproof / Performance)** | **RP3** | **SB12PFCR25-4** *(4" paper)* | **Scan-Speak R2604/833000** | 880–2,730 Hz | ~£68 | 24V/3.4A/82W / 28V/4.4A/124W | Ring radiator off-axis advantages combined with a massive crossover window ($880\text{--}2,730\text{ Hz}$). The 100W tweeter rating provides complete burnout immunity under full amplifier rail voltage. |
| **Best Overall (Premium Mid)** | **PACR1** | **SB12PACR25-4** *(4" Dark Al)* | **Scan-Speak R2604/833000** | 880–2,730 Hz | ~£70 | 24V/3.3A/80W / 28V/4.4A/122W | Upgrades the paper mid to dark anodized aluminum. Lowers midrange distortion, increases transient speed, and provides a huge $5.0\text{ mm}$ $X_{\text{max}}$ with $F_s=52.5\text{Hz}$ ($2.85\times$ safety margin at $150\text{ Hz}$). |
| **Best Overall (Compact spacing)** | **XCR3** | **SB12PFCR25-4** *(4" paper)* | **SB Acoustics SB21RDCN-C000-4** | 1,700–2,730 Hz | ~£64 | 24V/3.7A/89W / 28V/4.7A/131W | Compact neodymium ring dome. The small 58mm round faceplate reduces driver spacing to **90mm** (a 23% reduction vs RP3), significantly improving vertical lobing and integration. |

---

## Quick Selection Guide

| If your design priority is... | Best pick | ID | Price | Key Reason |
| :--- | :--- | :--- | :--- | :--- |
| 60° off-axis kitchen listening | SB12PFCR25-4 + Scan-Speak R2604/833000 | RP3 | ~£68 | Wide dispersion + 100W safety + maximum crossover latitude |
| Tighter spacing + ring radiator | SB12PFCR25-4 + SB21RDCN-C000-4 | XCR3 | ~£64 | Annular ring dome in a compact 58mm flange; 90mm centre spacing |
| On-axis reference quality | SB12MNRX2-25-4 + SB29RDNC-C000-4 | S3-Neo | ~£105 | Dedicated low-distortion midrange + premium 72mm neo ring dome |
| Classic paper warmth (British look) | Dayton DS115-8 + SEAS 27TDFC H1189-06 | DS_DF | ~£93 | Soft paper mid + smooth chambered SEAS dome; low 1.1kHz crossover |
| Narrowest baffle / minimum width | Dayton DSA90-8 + Peerless XT25SC40-04 | XC1 | ~£55 | 3" aluminum mid + 43.9mm ring rad; record 68mm centre spacing |
| Point-source phase coherence | SB12PACR25-4-COAX | B9 | ~£59 | Coaxial design eliminates time-alignment issues entirely |

---

## Scenario 1 — Kitchen 60° Off-Axis Listening (Primary Use Case)

The primary listener is standing at the counter, cooking, or moving about, placing them $\sim 60^\circ$ off the speaker's main axis. Tweeters with wide off-axis dispersion are highly ranked. Ring radiators and ring domes are the strongest choices; 19mm small domes are best among standard domes.

| Rank | ID | Mid | Tweeter | Crossover | Price | PSU | Character | Why |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | RP3 | SB12PFCR25-4 | R2604/833000 | 880–2,730 Hz | ~£68 | 24V/3.4A/82W / 28V/4.4A/124W | Warm + detailed | Widest crossover window ($880\text{--}2,730\text{ Hz}$) for a ring radiator, 100W safety against calibration error, natural paper warmth. |
| 2 | PACR1 | SB12PACR25-4 | R2604/833000 | 880–2,730 Hz | ~£70 | 24V/3.3A/80W / 28V/4.4A/122W | Detailed + crisp | Upgrades the midrange to an anodized aluminum cone for lower distortion, keeping the same wide-dispersion 100W tweeter. |
| 3 | XCR3 | SB12PFCR25-4 | SB21RDCN-C000-4 | 1,700–2,730 Hz | ~£64 | 24V/3.7A/89W / 28V/4.7A/131W | Detailed + cohesive | Annular ring dome in a 58mm flange; tight 90mm spacing reduces lobing; 40W power rating. |
| 4 | RR2 | SB12PFCR25-4 | XT25TG30-04 | 880–2,730 Hz | ~£50 | 24V/3.4A/83W / 28V/4.4A/125W | Warm + wide | Best value wide-window ring radiator. Same acoustic window as RP3 but utilizes a 15W tweeter (requires DSP limiter). |
| 5 | RD2 | SB12PFCR25-4 | SB21SDC-C000-4 | 1,440–2,730 Hz | ~£56 | 24V/3.5A/84W / 28V/4.5A/126W | Warm + detailed | Annular ring dome, compact 92mm flange, low $720\text{Hz}$ Fs. |
| 6 | S1 | DS115-8 | SB19ST | 1,960–2,636 Hz | ~£50 | 24V/3.7A/88W / 28V/4.7A/130W | Warm | Small 19mm dome provides wide dispersion among standard domes. Classic paper mid. |

---

## Scenario 2 — On-Axis Listening (Direct, Centred)

For seated, critical listening directly in front of the monitor. Off-axis roll-off is less critical; instead, midrange resolution, low distortion at the crossover point, and transient speed are prioritized.

| Rank | ID | Mid | Tweeter | Crossover | Price | PSU | Character | Why |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | S3-Neo | SB12MNRX2-25-4 | SB29RDNC-C000-4 | 1,160–2,730 Hz | ~£105 | 24V/2.8A/67W / 28V/3.9A/109W | Detailed + neutral | Flagship monitor. Low-$Q_{ts}$ natural-fibre midrange reproduces transients with high accuracy. Premium 72mm neo ring dome. |
| 2 | DS_DF | Dayton DS115-8 | SEAS 27TDFC H1189-06 | 1,100–2,636 Hz | ~£93 | 24V/3.3A/79W / 28V/4.3A/121W | Smooth + warm | Recreates classic British hi-fi warmth. The rear-chambered SEAS tweeter has $F_s=550\text{Hz}$, allowing a low 1.1kHz crossover to keep the mid out of beaming. |
| 3 | B9 | SB12PACR25-4-COAX | (built-in) | 2,600–2,730 Hz | ~£59 | 24V/4.2A/100W / 28V/5.1A/142W | Clean + cohesive | Point-source coaxial design guarantees perfect phase integration and zero time offset. Dark aluminum cone look. |
| 4 | RP2 | Dayton DS115-8 | R2604/833000 | 880–2,636 Hz | ~£80 | 24V/3.3A/79W / 28V/4.3A/121W | Warm + detailed | Combines classic paper mid warmth with a wide-window 100W ring radiator. |
| 5 | D6R2 | Dayton DS115-8 | D2604/830000 | 1,260–2,636 Hz | ~£73 | 24V/3.2A/77W / 28V/4.2A/119W | Detailed | Scan-Speak 100W textile dome. Resonant frequency of $630\text{Hz}$ gives a wide tuning window. |

---

## Scenario 3 — Compact Baffle / Minimum Width

Designed for the narrowest possible front baffle footprint. Spacing is driven by midrange outer frame diameter and tweeter faceplate diameter.

| Rank | ID | Mid | Tweeter | Spacing | Price | PSU | Character | Why |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | XC1 | Dayton DSA90-8 | XT25SC40-04 | **68 mm** | ~£55 | 24V/3.3A/78W / 29V/4.2A/121W | Detailed + wide | **Minimum spacing record.** Utilizes a 43.9mm ring radiator, enabling a cabinet only 115mm wide. |
| 2 | SE1 | Dayton DSA90-8 | SEAS H1406-04 | **73 mm** | ~£74 | 24V/3.5A/83W / 28V/4.5A/125W | Detailed | Oval faceplate ($69.7 \times 54\text{ mm}$) mounted in portrait. Very narrow baffle footprint, 80W power safety. |
| 3 | MDT22 | Dayton DSA90-8 | Morel MDT22T | **73 mm** | ~£78 | 24V/3.4A/81W / 29V/4.3A/124W | Warm | Round 3" mid paired with a square $54 \times 54\text{ mm}$ Morel soft dome. Low $F_s=650\text{Hz}$, 80W safety. |
| 4 | XCR1 | Dayton DSA90-8 | SB21RDCN-C000-4 | **75 mm** | ~£76 | 24V/3.6A/88W / 29V/4.5A/130W | Detailed + wide | Compact neodymium ring dome. Spacing is only 75mm, with a wide crossover window ($1,700\text{--}3,260\text{ Hz}$). |
| 5 | B10 | Dayton DSA90-8 | ND25FA-4 | **79 mm** | ~£44 | 24V/3.6A/86W / 29V/4.4A/128W | Detailed | Tightest round dome spacing. Narrow crossover window ($2,700\text{ Hz}$ minimum). |

---

## Scenario 4 — Visual/Aesthetic Recommendations

The visual presentation of the speaker face is highly customizable depending on driver shapes:

### Consistent Circular Theme
Traditional, symmetrical monitor look. The subwoofer, midrange, and tweeter are all round.
*   **DSA90-8 + SB19ST (ID: A3, ~£49):** 90mm centre spacing. Extremely neat circular alignment.
*   **Dayton DS115-8 + SB19ST (ID: S1, ~£50):** Classic warm paper midwoofer paired with a round 19mm fabric dome. Looks like a mini-monitor from the golden era of hi-fi.

### Square / Non-Round Contrast
Breaks the standard circular pattern by placing a non-round driver on the baffle to contrast with the round subwoofer.
*   **DSA90-8 + Morel MDT22T (ID: MDT22, ~£78):** Square faceplate ($54 \times 54\text{ mm}$) tweeter placed directly above a round 3" midwoofer. Clean lines, geometric contrast, 73mm spacing.
*   **Peerless SLS-85S25CP04-04 + Monacor DT-28N (ID: B12, ~£61):** An oval midrange driver ($105 \times 91\text{ mm}$) paired with a circular waveguide tweeter. Breaks up standard rectangular grids. Massive $10.2\text{ mm}$ midrange $X_{\text{max}}$.

### Ring Radiator High-Tech
Features the distinct dual-concentric ring diaphragm and center phase plug of a ring radiator, giving the baffle a technical, high-performance aesthetic.
*   **Dayton DSA90-8 + Peerless XT25SC40-04 (ID: XC1, ~£55):** Tiny concentric ring radiator centered above the aluminum midrange. High-tech look on a minimal baffle.
*   **SB12PFCR25-4 + Scan-Speak R2604/833000 (ID: RP3, ~£68):** Structured paper midwoofer combined with the large, detailed face of a Scan-Speak dual-ring radiator. 

---

## High-Power Tweeter Comparison & Burnout Safety

### Why Tweeter Power Handling Matters
Under normal matching conditions, tweeters receive very little power. At a continuous reference level of $98\text{ dB}$ SPL, the tweeter receives only $5\text{--}12\text{ W}$ because its high sensitivity must be padded down in the DSP. At a burst SPL of $101\text{ dB}$, power demands double to $10\text{--}24\text{ W}$. 

However, the JAB5 amplifier powered by a 28V or 29V PSU is capable of delivering **$45\text{ W}$ RMS into 8Ω and $90\text{ W}$ RMS into 4Ω** per channel. If a DSP volume limiter is not set correctly, or if there is a transient calibration surge, a standard 15W tweeter (such as the XT25TG30-04) can instantly burn out. Choosing a high-power tweeter ($\ge 80\text{ W}$ RMS) provides complete hardware protection against DSP configuration errors.

### High-Power Tweeter Shortlist

| Model | Power (RMS) | Flange OD | Sensitivity | Res. Freq (Fs) | Min Crossover | Price | Key Features |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SB Acoustics SB26STCN-C000-4** | **120 W** | 72 mm | 92.0 dB | 950 Hz | 1,900 Hz | ~£29 | Neodymium magnet, compact 72mm round flange. Indestructible on 24V rails. |
| **Scan-Speak R2604/833000** | **100 W** | 104 mm | 92.0 dB | 440 Hz | 880 Hz | ~£46 | Discovery dual-ring radiator. **Widest crossover window** ($880\text{ Hz}$ minimum). Annular dispersion. |
| **Peerless XT25SC40-04** | **100 W** | 43.9 mm | 94.0 dB | 1,018 Hz | 2,036 Hz | ~€30 | Smallest ring radiator faceplate in the field. Ideal for tight spaces. |
| **SEAS 27TFFNC/CG H1406-04** | **80 W** | 69.7×54 mm | 91.0 dB | 1,170 Hz | 2,340 Hz | ~£34 | Oval faceplate, ultra-shallow ($21.5\text{ mm}$ deep). Portrait spacing champion. |
| **Morel MDT22T** | **80 W** | 54×54 mm | 89.0 dB | 650 Hz | 1,300 Hz | ~£48 | Square faceplate, large rear chamber, low resonant frequency. Vented magnet. |
