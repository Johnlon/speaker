# Kitchen Counter Monitor — Explicit Requirements

This file records only requirements explicitly stated by the owner, plus technical constraints that follow directly from those requirements. Do not add interpretation or analysis.

---

## Listening Context

- Kitchen counter placement, 5–6 feet from listener
- Listener frequently at 60° off-axis (at the cooker)
- Use spans quiet background listening up to full volume (party, classical)

---

## Frequency Response

- Flat, natural response from the low 30s Hz upward
- 38 Hz native tuning via passive radiator — no digital bass boost to reach this target

---

## DSP / Loudness

- GHM-style loudness compensation: gentle bass shelf boost at low volumes, flattening as volume rises

---

## Power — Mid and Tweeter Must Keep Up with the Sub

When the subwoofer is driven to its rated maximum (40W RMS continuous, 80W peak), the mid and tweeter must be capable of matching the sub's output at those levels, with a little headroom to spare. This applies to both continuous RMS output and burst/peak transients.

Driver selections must be vetted against this before inclusion in recommendations.

---

## Off-Axis Stability

- Tonal balance must remain stable across the full 60° horizontal sweep
- Tweeter dome ≤19 mm preferred (wider HF dispersion above crossover)
- Mild toe-in (10–15°) is possible but the design must not depend on it

## Crossover Phase Coherence

- All three drivers must sum flat and in-phase at the crossover points — no audible suck-outs or brightness peaks at the transitions

---

## Recommendation Tables

- PSU voltage (24V or 29V) must be shown as a column in the quick reference table and both budget recommendation tables
- Recommendations must include visual sub-groups covering:
  - Pairings where mid and tweeter are both circular/round
  - Pairings where mid and tweeter are square or non-round
  - Other visual classes as appropriate (e.g. mixed shapes, oval, compact waveguide)
- Owner is not yet sure what good looks like in terms of visual types and layouts — recommendations should help explore this
- Driver centre spacing must be noted where it affects acoustic performance (lobing geometry at the crossover frequency - )

## Physical

- All drivers surface-mounted — proud of the baffle, not flush-recessed
- No wiring or connectors visible on front or top face
- Compact — Google Home Max footprint is the size reference; up to ~5 cm taller is acceptable
- Classic look — inspired by B&W DM4 and similar wooden speaker designs

