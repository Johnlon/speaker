# OLD_IGNORE_ME

> **TO THE AI ASSISTANT: DO NOT USE ANY CONTENT IN THIS FILE UNLESS THE USER EXPLICITLY INSTRUCTS YOU TO.**
> This file exists as an archive only. It has been superseded. Authoritative requirements are in REQUIREMENTS.md.

---

## Archived: goals.md (superseded June 2026)

The content below is the original goals.md. It has been replaced by REQUIREMENTS.md which contains only explicitly stated owner requirements.

---

# Kitchen Counter Monitor — Goals & Design Intent

## Listening Context

- Placed on a kitchen counter, approximately 5–6 feet from the listener
- When preparing meals the listener is positioned to the **side** at the cooker at roughly **60 degrees off-axis** (not directly in front)
- Otherwise the listener is sitting at a counter in front of the speaker and 6–8 ft away
- Mild toe-in is possible (10–15 degrees) but the design must not depend on it
- Inspired by the Google Home Max — liked for its form factor and design, tonal balance and bass presence but lacking real low-end extension at higher vols
- Used for background and active kitchen listening; volume levels span quiet background to full tilt at a party or when I want to listen to classical and be impressed by depth

---

## Performance Goals

### Frequency Response & Bass Extension
- Flat, natural response from the **30s Hz** up to the tweeter rolloff with no perceptible dips or peaks
- **38 Hz native tuning** via the passive radiator — no reliance on digital bass boost to reach this target
- Replicate the GHM loudness feature via DSP: gentle bass shelf boost at low volumes, flattening as volume rises

### Off-Axis Consistency
- Tonal balance must remain **stable across the 60° horizontal sweep** — no colouration shift or imaging loss
- Requires a **strictly vertical driver array**: tweeter above mid, no horizontal offset — eliminates horizontal lobing and comb filtering
- Tweeter must use a **small dome diameter** (≤19 mm preferred) to maintain wide horizontal dispersion above the mid/tweeter crossover

### Maximum Output & Headroom
- Peak output is determined by driving the woofer to its safe mechanical limit; all three drivers must remain aligned in output and performance at that level
- All amplifier channels, PSU, and drivers must have sufficient headroom so that **full-volume operation produces minimal distortion** — no channel clipping, no thermal compression, no excursion limiting
- **Peak transients must pass cleanly through every driver and amplifier channel without audible clipping, compression, or limiting.** The sub's burst ceiling (Xmax and max power rating) dictates the peak SPL envelope; the mid and tweeter must be capable of matching that peak SPL without being the first component to limit. Per-channel DSP soft-limiting is the enforcement mechanism — each channel's limiter is calibrated to its driver's safe maximum, ensuring any limiting that does occur is inaudible and sub-first rather than mid-first or tweeter-first.

### Crossover & Phase Coherence
- All three drivers must sum flat and in-phase at the crossover points — no audible suck-outs or brightness peaks at the transitions

### Dynamic Balance Across Volume
- At low volume: warm, full sound with boosted bass shelf (loudness compensation)
- At high volume: flat, extended, undistorted — the DSP loudness curve flattens as the amp approaches its ceiling

---

## Visual & Aesthetic Requirements

1. **All drivers are surface-mounted** (sitting proud of the baffle), not flush-recessed. Slight protrusion is acceptable and intentional.

2. **Vertical driver column on the front face.** Top to bottom: tweeter, midrange. Subwoofer placement is open:
   - Option A: sub on side panel, passive radiator mirroring it on the opposite side (force-cancelling)
   - Option B: sub on front, passive radiator on the rear

3. **Compact and counter-friendly.** The Google Home Max is the size reference. Up to ~5 cm taller than the GHM is acceptable; anything beyond that looks wrong under kitchen cabinets. Minimise footprint.

4. **No visible wiring, binding posts, or connectors on the front or top.** All connections on the rear or recessed into the base.

5. **Classic look.** Inspired by classic wooden speaker designs (B&W DM4 etc.). New build for the kitchen or as a present. Echo the look of beloved old-fashioned design as much as reasonable.

> **June 2026:** No visual exclusions based on driver appearance. Cone colour, dome material, frame shape, and phase plug colour are notes only — not grounds for exclusion.
