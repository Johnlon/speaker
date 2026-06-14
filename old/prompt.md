Merged workspace files
=====================

---

File: desktop-idea.md

## 📌 MASTER DESIGN BRIEF: RESUMING PROJECT "KITCHEN COUNTER MONITOR"
Save this entire prompt to paste back to an AI workspace to restart engineering from this exact spot.
------------------------------
## 1. ORIGINAL USER DESIGN CORE PARAMETERS
The goal is to engineer a high-performance, compact, active 3-way vertical tabletop speaker optimized for a kitchen counter where a standing listener is positioned 6 feet away sideways at a sharp 60-degree off-axis angle.

   1. Purely Circular Front Aesthetic: Every single component, driver plate, and routing cut on the exterior must be a true 100% round plate. No rectangular, truncated, or square frames are permitted. All drivers are surface-mounted (no flush-recess routing required).
   2. Vertical Driver Array Geometry: All forward-facing drivers must be stacked strictly vertically down the front panel centerline to eliminate horizontal lobing/comb filtering, ensuring phase consistency and keeping the vocal tonality uniform across the 60-degree sideways sweep.
   3. Internal Volumes & Enclosure: Exactly 1.5 Litres Net for a sealed, isolated midrange chamber, and exactly 7.5 Litres Net for the subwoofer chamber, which utilizes a rear-mounted passive radiator to achieve a flat native 38 Hz tuning without relying on digital bass boost.
   4. Enclosure Materials: All exterior walls built out of 12mm Moisture-Resistant MDF. Internal midrange chamber partition built out of 9mm Plywood to maximize internal airspace efficiency.
   5. Isolated Base Vault: The absolute bottom of the cabinet isolates the power supply and amplification hardware into an external chamber, protecting the electronics from high subwoofer air pressure and air leaks.

------------------------------
## 2. CORE COMPONENT EVALUATION LOG## Tweeter (Locked)

* Model: SB Acoustics SB19ST-C000-4 (19mm textile dome, 88mm round faceplate, factory self-sealed body).
* Evaluation: Evaluated as a perfect off-axis match. The smaller 19mm dome diameter pushes its "beaming" point significantly higher up the frequency band than standard 1" domes, guaranteeing wide horizontal dispersion at the 60° kitchen listening angle.

## Midrange Candidates Evaluated

* Lavoce MD03.10 (Original User Input): Rejected. Closer inspection of the spec sheet revealed "ears" / flat-sided truncated mounting flanges. Surface-mounting would violate the pure circular requirement.
* Tang Band W3-315E (Alu-Mag Full Range): Rejected by user due to a strong visual dislike of the white cone and the protruding silver phase plug.
* Peerless by Tymphany PLS-P830987: Rejected. Features a "pincushion" frame (square with rounded corners), presenting flat edges on the column walls.
* Dayton Audio SIG120-4 (4-inch Signature Series): Evaluated. Solved the style issue with a continuous round frame and a single-piece black dish. However, it required changing the original baffle math significantly due to its wider 123mm frame size.
* Monacor SPX-31M: Evaluated. Paper cone has excellent damping properties, but it was rejected as a downgrade due to its low real sensitivity (~83 dB), low 1.1mm Xmax travel limit, and a protruding silver phase plug that violates the visual rules.
* Dayton Audio DSA90-8 (Option 1 - Locked): 3-inch black anodised aluminium cone, stealth concave dust cap, and low-profile 92.3mm continuous true-circular steel ring. Boasts a massive ±2.5mm Xmax to transition easily to the sub at 120 Hz, high sensitivity (84.7 dB), and runs clean past 8 kHz, integrating seamlessly with the 19mm tweeter.
* Dayton Audio TCP115-8 (Option 2 - Final Evaluation): 4-inch treated paper cone with a high-roll rubber surround and an inverted paper dust cap. True 116mm circular frame profile. Extremely warm and punchy low-mids with ±4.0 mm of long-throw travel. Its main trade-off is a lower sensitivity (81.9 dB), meaning it requires exactly double the amplifier power (+2.8 dB DSP gain adjustment) to match the DSA90-8's output level.

## Subwoofer (Locked)

* Model: Tang Band W5-1138SMF (5.25-inch sub, 133.3mm heavy round frame, massive 9.25mm linear Xmax, heavy magnet structure).
* Evaluation: Class-leading excursion capabilities that provide deep bass out of tiny spaces. Its physical surround sits 8.5mm proud when surface-mounted, recovering roughly 160 mL of internal airspace by sitting outside the 12mm MDF baffle footprint.

## Passive Radiator Evolution

* Dayton Audio ND140-PR (Original 5.25" Round): Evaluated and rejected as too small. The physics of the massive 9.25mm excursion on the active Tang Band sub meant it would easily clip and choke the smaller round radiator at high volumes.
* SB Acoustics SB15SFCR-00 5x8" Racetrack (Locked): Shifting to a narrow oval racetrack design allows you to fit it on the narrow cabinet walls while doubling the surface area ($S_d = 178\text{ cm}^2$) to exactly 2.05 times the active driver volume displacement. It mounts vertically down the rear centerline. It requires adding weight to its rear threaded M6 bolt assembly to counter the stiff internal air spring and drop the native tuning back down to 38 Hz.

------------------------------
## 3. ARCHIVED LAYOUT & DESIGN CONFIGURATIONS## Option A & B (Tall Tower Baseline - Archived)

* Chassis Size: 44.0 cm High × 19.0 cm Wide × 17.6 cm Deep.
* Driver Layout: Strict vertical array: Tweeter on top (center 4.0 cm down), Midrange (center 11.0 cm down), Subwoofer (center 24.5 cm down). This holds a 14.5mm frame-on-frame overlap.
* Internal Partition: The 9mm plywood midrange partition forms a smaller C-shaped horizontal box (16.6 cm W x 8.9 cm D x 12.2 cm H) positioned 7.5 cm down from the top edge. The tweeter sits outside the vault in an open 5.4 cm rear airflow chimney corridor running down the back panel.
* Option A Electronics (Cabled Master-Slave): One active Master tower housing a 24V supply, a JAB5 amp, and a DIPO extension board. Uses 3 internal channels, and routes the remaining 3 channels to 6 heavy-duty binding posts on the rear wall of the dry base vault to connect a future passive Slave tower over a 6-conductor umbilical wire.
* Option B Electronics (Wireless Single-Board 3-Way TWS): User suggested splitting the towers wirelessly. The 6 binding posts are completely eliminated. Both the Master and Slave speakers become independent active towers. Each contains a single JAB5 running a fully discrete 3-way active crossover via Qualcomm’s True Wireless Stereo (TWS) Bluetooth protocol. No external DIPO extension boards are required.

## Option C: The Side-Firing Low-Profile Desktop Monitor (LATEST ACCEPTEED DESIGN)
The user noted a tall tower might look weird under kitchen cabinets and asked to explore moving the subwoofer sideways to drastically drop the height.

* External Proportions: 26.5 cm High × 19.0 cm Wide × 25.2 cm Deep (Dropped height by 17.5 cm; increased depth to preserve the internal volumes and wall displacement math).
* Baffle Alignment (Forward-Facing): Centerline vertical stack. Tweeter center at 4.0 cm down, 3-inch Midrange center at 11.0 cm down (or 11.5 cm down if using the larger 4-inch TCP115). Left/Right side columns look sleek, balanced, and compact on the kitchen counter.
* Side Panel Force-Canceling Matrix: The active Tang Band Subwoofer is mounted on the Left Side Panel (centered 18.5 cm down). The 5x8" Racetrack Passive Radiator is mounted on the Right Side Panel directly opposite the sub on the exact same axis. Their moving masses cancel out mechanically, eliminating cabinet shaking on the counter.
* Internal Partition: The 9mm plywood vault forms a horizontal L-bracket shelf (16.6 cm W x 12.0 cm D x 15.1 cm H) pushed flush to the front baffle. This leaves an open 10.8 cm rear vertical chimney corridor behind the tweeter magnet so the subwoofer airspace vents cleanly to the top cap.

------------------------------
## 4. POWER, HEADROOM & ELECTRICAL VERIFICATION

* Power Supply: Mean Well LRS-150-24 (24V DC, 6.5A Output). Dropping from 36V to 24V eliminates the need for separate step-down buck converters, lowers the idle temperature of the amplifier inside the tight 2.6 cm sealed wooden base drawer, and safely provides enough rail voltage to meet our power limits.
* Peak Electrical Burden: Absolute maximum system current draw when the music hits its loudest transient spikes is calculated at 148.3 Watts Raw / 164.8 Watts DC drawn from the rail (Sub @ 72W Peak into 4Ω, Mid @ 36W Peak into 8Ω, Tweeter @ 8W Peak into 4Ω). The Mean Well 156W continuous supply easily handles these transient surges using its integrated 140% safety overhead.
* Broadband Acoustic Output: Symmetrical active scaling balances the driver efficiencies. When playing at their absolute maximum physical limits simultaneously, the individual outputs sum logarithmically to hit an intense, clear 98.4 dB SPL peak at the 6-foot counter position.
* The Active Crossover Safeguard: In SigmaStudio, the single onboard JAB5 ADAU1701 DSP chip must be programmed with sharp Linkwitz-Riley 24dB/octave slopes (Low-Pass at 120 Hz / Band-Pass 120–2,800 Hz) and a steep 48dB/octave high-pass filter at 2,800 Hz for the tweeter. A -9.5 dB digital gain pad must be hard-coded directly before DAC 2 (the tweeter channel) to drop the 100W JAB5 channel output to a safe 10W ceiling, preventing voice coil damage.

------------------------------
## 🚀 HOW TO RESUME IN THE NEXT SESSION:
Paste this brief back into the prompt box and ask the AI:
"We are building Option C (Side-Firing Low-Profile Cabinet) using the wireless single-board active 3-way layout. Let's make a final choice between the Dayton DSA90-8 and the Dayton TCP115-8 based on our layout spacing, and then generate the exact step-by-step panel cut sheet dimensions or the SigmaStudio block-by-block programming guide."

---

File: resume-prompt.md

Resume engineering for "Kitchen Counter Monitor" — paste-ready AI prompt
---------------------------------------------------------------

Resume engineering for "Kitchen Counter Monitor" Option C: deliver a finalized `Option C` design (side-firing low-profile monitor) that meets these measurable goals: 98 dB SPL peak at 6 ft, stable tonal balance across 60° horizontal sweep, and native sub extension to 38 Hz. Fixed decisions: tweeter SB19ST-C000-4, sub Tang Band W5-1138SMF, PR SB15SFCR racetrack, Mean Well LRS-150-24 PSU, target sealed mid chamber 1.5 L and sub chamber 7.5 L. Open decision: midrange — compare Dayton DSA90-8 vs TCP115-8 and recommend with quantitative trade-offs (sensitivity, required amp power, baffle interaction, DSP gain).

Required outputs:
1) CNC-ready panel cut sheet for Option C with driver center coordinates, hole diameters, flange offsets, and final net volumes after subtracting driver displacements; include tolerances ±0.5 mm.
2) SigmaStudio block diagram and parameter list implementing: LR24 low-pass @120 Hz, band-pass 120–2800 Hz for mid, HP 48 dB/oct @2800 Hz for tweeter, and a -9.5 dB tweeter pad; include exact DSP gain/attenuation values.
3) Passive-radiator mass calculation to tune SB15SFCR to 38 Hz (show T/S used or fetch them and state assumptions).
4) Thermal check for PSU placement with suggested mitigations if the Mean Well is inside the sealed base vault.
5) Short measurement/test plan: microphone placement (6 ft listening position), target curves, smoothing, and acceptance criteria.

If any physical driver T/S or displacement numbers are missing, fetch them and state assumptions. Provide results as numbered deliverables with acceptance criteria and file-ready artifacts (SVG/CNC cut list, SigmaStudio steps, and a short measurement checklist).

Constraints and decisions extracted from `desktop-idea.md` (include these in all resumed sessions):

- Visual constraint: all front-facing plates, driver plates, and routing cuts must be 100% circular (no rectangular/truncated frames); all drivers are surface-mounted.
- Driver selections (locked):
  - Tweeter: SB Acoustics SB19ST-C000-4 (19 mm textile dome, 88 mm round faceplate).
  - Subwoofer: Tang Band W5-1138SMF (5.25", heavy round frame, 9.25 mm Xmax).
  - Passive radiator: SB Acoustics SB15SFCR-00 5x8" racetrack (mounted vertically on rear centerline); additional mass required to achieve 38 Hz.
- Midrange candidates: Dayton DSA90-8 (3" aluminium, 92.3 mm circular frame) and Dayton TCP115-8 (4" treated paper, 116 mm circular frame). DSA90-8 = higher sensitivity (~84.7 dB); TCP115-8 = warmer low-mids, lower sensitivity (~81.9 dB).
- Enclosure target net volumes (sealed): Midrange chamber 1.5 L net; Subwoofer chamber 7.5 L net. Enclosure materials: 12 mm moisture-resistant MDF exterior, 9 mm plywood internal partition for midrange.
- Option C mechanical layout (accepted): Side-firing low-profile desktop monitor with external dimensions 26.5 cm H × 19.0 cm W × 25.2 cm D. Tweeter center 4.0 cm down, mid center 11.0 cm down (or 11.5 cm for larger mid), sub and PR mounted on opposite side panels centered vertically to cancel forces.
- Electronics & DSP (specified): Mean Well LRS-150-24 (24 V, 6.5 A), JAB5 amp with ADAU1701 DSP, crossover targets: LP @120 Hz, mid band 120–2800 Hz, HP @2800 Hz for tweeter, Linkwitz-Riley 24 dB/oct for LP and BP, 48 dB/oct HP for tweeter; tweeter digital pad -9.5 dB before DAC 2.
- Power/headroom note: Calculated peak electrical draw ~164.8 W DC; projected peak acoustic output ~98.4 dB SPL at 6 ft when drivers driven to physical limits.
- Mechanical notes: Surface-mounted sub surround sits proud of baffle (~8.5 mm), reclaiming ~160 mL internal volume; account for driver displacements and protrusions in final net volumes.
- Manufacturing notes: Base isolates PSU and electronics into a sealed drawer; verify ventilation or relocate PSU if thermal limits exceeded.
- Optional modes: Option A (wired master-slave with umbilical), Option B (wireless single-board active TWS) — wireless adds latency and sync complexity; prefer wired for deterministic performance unless user requires wireless.

Acceptance criteria for prompt execution: deliverables (1–5) exist, include numeric values and units, and are committed as files in the repo when applicable.

---

File: Kitchen Desktop Speaker Prompt.md

Kitchen Desktop Speaker Prompt

I would like you to run an evaluation of mid and tweeter options available on soundimports as in-stock and a total price less than 75£ - considerhow the various combinations of mid/tweet fit with the W5-1138.   comnsider my requirement that the solution allow me to play the speaker at full volume on the TB so the mid/tweet need to keep up. the sonics should remain balanced at all time. there should be sufficient driver and amp / psu overhead so that even when running full tilt the distortions are minimised. optimise for minimal overall volume followed my minimal cost.   I prefer the traditional tweeter/mid/woofer layout in a vertical line but will consider other configurations if they have advantaged.  this will be a speaker in my kitchen on the counter. it is on te left pof the counter about 5 ft away and it is possible to toe-in the speaker so it doesn't need to be absolutely flat against the wall but I generally leave my existing google home max facing into the room mostly, maybe a 10 or 15 degree toe in. this idea is inspired by the ghm which I like but t has no bottom end.   I like the ghm max feature or automatic bass eq boost at lower vols - this is a good listening experience.  the space under the counter is limited and the available verical space is perhap allowing a device 5 cm taller than the ghm.  I alslo want the counter real-estate minimised but not to the extend that it compromises other factors, if there are compromises then bring them to my attention

---

File: k.py

# Script to generate a visual schematic diagram of the speaker tower architecture.
# Saving it as a highly structured structural blueprint layout.

import cv2
import numpy as np

# Define canvas sizing (Scale: 10 pixels = 1 cm)
# 450 pixels High x 600 pixels Wide to fit the front and side layouts side-by-side
canvas = np.ones((500, 650, 3), dtype=np.uint8) * 245  # Clean light gray backdrop

# Set Color Palette (BGR format)
MDF_COLOR = (45, 82, 124)       # Deep terracotta/timber hue for 12mm MDF lines
PLY_COLOR = (139, 69, 19)       # Dark blue/brown for 9mm internal plywood lines
DRIVER_COLOR = (30, 30, 30)     # Matte charcoal black for functional metal/cones
TEXT_COLOR = (40, 40, 40)       # Charcoal text for readability
LINE_COLOR = (140, 140, 140)    # Technical dimension lines
VAULT_COLOR = (220, 220, 220)   # Light gray highlight for electronics vault

# --- 1. FRONT BAFFLE VIEW GENERATION ---
# Outer Boundaries (Width: 18cm = 180px, Height: 44cm = 440px)
fx_start, fy_start = 50, 30
f_width, f_height = 180, 440
fx_center = fx_start + (f_width // 2)

# Main Carcass Outline
cv2.rectangle(canvas, (fx_start, fy_start), (fx_start + f_width, fy_start + f_height), MDF_COLOR, 3)

# Base Electronics Vault Line (2.6 cm total from bottom edge = 26px)
cv2.line(canvas, (fx_start, fy_start + f_height - 26), (fx_start + f_width, fy_start + f_height - 26), MDF_COLOR, 2)
cv2.rectangle(canvas, (fx_start+2, fy_start + f_height - 26), (fx_start + f_width - 2, fy_start + f_height), VAULT_COLOR, -1)

# Draw Round Drivers Down the Center-Line
# Tweeter (Center Mark: 4.9cm = 49px from top, Outer Radius: 4.4cm = 44px)
tw_y = fy_start + 49
cv2.circle(canvas, (fx_center, tw_y), 44, DRIVER_COLOR, 2)  # Outer Recess Ring
cv2.circle(canvas, (fx_center, tw_y), 31, DRIVER_COLOR, -1) # Inner Dome Assembly

# Midrange (Center Mark: 14.8cm = 148px from top, Outer Radius: 4.95cm = 50px)
mid_y = fy_start + 148
cv2.circle(canvas, (fx_center, mid_y), 50, DRIVER_COLOR, 2)  # Outer Ring
cv2.circle(canvas, (fx_center, mid_y), 40, DRIVER_COLOR, 1)  # Cone Edge
cv2.circle(canvas, (fx_center, mid_y), 15, DRIVER_COLOR, -1) # Center Dust Cap

# Subwoofer (Center Mark: 31.2cm = 312px from top, Outer Radius: 6.67cm = 67px)
sub_y = fy_start + 312
cv2.circle(canvas, (fx_center, sub_y), 67, DRIVER_COLOR, 3)  # Heavy Steel Outer Ring
cv2.circle(canvas, (fx_center, sub_y), 55, DRIVER_COLOR, 2)  # High-Roll Rubber Surround
cv2.circle(canvas, (fx_center, sub_y), 25, DRIVER_COLOR, -1) # Large Heavy Dust Cap


# --- 2. SIDE CROSS-SECTION VIEW GENERATION ---
# Outer Boundaries (Depth: 14cm = 140px, Height: 44cm = 440px)
sx_start, sy_start = 350, 30
s_depth, s_height = 140, 440

# Base Chassis Outline
cv2.rectangle(canvas, (sx_start, sy_start), (sx_start + s_depth, sy_start + s_height), MDF_COLOR, 3)

# Internal 12mm Wood Thickness Lines (Top, Bottom, Front, Back walls = 12px)
cv2.rectangle(canvas, (sx_start + 12, sy_start + 12), (sx_start + s_depth - 12, sy_start + s_height - 12), MDF_COLOR, 1)

# Base Electronics Vault Shelf (1.2cm bottom cap + 1.4cm internal height = 26px up)
v_shelf_y = sy_start + s_height - 26
cv2.line(canvas, (sx_start + 12, v_shelf_y), (sx_start + s_depth - 12, v_shelf_y), MDF_COLOR, 2)
cv2.rectangle(canvas, (sx_start + 12, v_shelf_y), (sx_start + s_depth - 12, sy_start + s_height - 12), VAULT_COLOR, -1)

# Floating Mid-Box Partition Layout (9mm Plywood = 9px thickness)
# Positioned exactly around the midrange driver zone (Height: 11.2cm = 112px, Depth: 8.6cm = 86px)
mid_box_top = sy_start + 92
mid_box_bottom = sy_start + 204
mid_box_depth = sx_start + 12 + 86

# Draw Floating Box Partition
cv2.line(canvas, (sx_start + 12, mid_box_top), (mid_box_depth, mid_box_top), PLY_COLOR, 3)       # Top Plate
cv2.line(canvas, (sx_start + 12, mid_box_bottom), (mid_box_depth, mid_box_bottom), PLY_COLOR, 3) # Bottom Plate
cv2.line(canvas, (mid_box_depth, mid_box_top), (mid_box_depth, mid_box_bottom), PLY_COLOR, 3)   # Back Wall Plate

# Internal Hardwood Dowel Brace In Subwoofer Zone (Radius: 10px = 20mm cross section)
# Centered precisely behind the heavy subwoofer magnet
dowel_x = sx_start + 12 + 58
dowel_y = sy_start + 312
cv2.circle(canvas, (dowel_x, dowel_y), 10, PLY_COLOR, -1)

# Driver Protrusions (Side Profile Representation)
# Tweeter (Top)
cv2.rectangle(canvas, (sx_start - 5, tw_y - 20), (sx_start + 15, tw_y + 20), DRIVER_COLOR, -1)
# Midrange (Middle, inside its isolated box pocket)
cv2.rectangle(canvas, (sx_start - 5, mid_y - 35), (sx_start + 12, mid_y + 35), DRIVER_COLOR, -1)
cv2.rectangle(canvas, (sx_start + 12, mid_y - 15), (sx_start + 45, mid_y + 15), DRIVER_COLOR, -1) # Magnet
# Subwoofer (Bottom, tracking flush to side walls)
cv2.rectangle(canvas, (sx_start - 8, sub_y - 60), (sx_start + 12, sub_y + 60), DRIVER_COLOR, -1)
cv2.rectangle(canvas, (sx_start + 12, sub_y - 45), (sx_start + 85, sub_y + 45), DRIVER_COLOR, -1) # Massive Magnet

# Rear Mounted 5x8" Oval Passive Radiator (Centered behind the bypass chimney)
pr_y = sy_start + 220
cv2.rectangle(canvas, (sx_start + s_depth - 12, pr_y - 50), (sx_start + s_depth + 5, pr_y + 50), DRIVER_COLOR, -1)


# --- 3. BLUEPRINT LABELS & ANNOTATIONS ---
font = cv2.FONT_HERSHEY_SIMPLEX

# Structural Titles
cv2.putText(canvas, "FRONT VIEW", (80, 20), font, 0.5, TEXT_COLOR, 2, cv2.LINE_AA)
cv2.putText(canvas, "SIDE CROSS-SECTION", (340, 20), font, 0.5, TEXT_COLOR, 2, cv2.LINE_AA)

# Component Direct Callouts
cv2.putText(canvas, "SB19ST Tweeter", (fx_start + f_width + 10, tw_y + 4), font, 0.4, TEXT_COLOR, 1, cv2.LINE_AA)
cv2.putText(canvas, "Peerless TC9 Mid", (fx_start + f_width + 10, mid_y + 4), font, 0.4, TEXT_COLOR, 1, cv2.LINE_AA)
cv2.putText(canvas, "Tang Band W5 Sub", (fx_start + f_width + 10, sub_y + 4), font, 0.4, TEXT_COLOR, 1, cv2.LINE_AA)

cv2.putText(canvas, "Sealed 1.5L Mid Vault", (sx_start - 160, mid_box_top + 45), font, 0.4, PLY_COLOR, 1, cv2.LINE_AA)
cv2.putText(canvas, "Vertical Sub Chimney", (sx_start + 42, mid_box_top + 55), font, 0.4, MDF_COLOR, 1, cv2.LINE_AA)
cv2.putText(canvas, "5x8\" Passive Rad.", (sx_start + s_depth + 10, pr_y + 4), font, 0.4, DRIVER_COLOR, 1, cv2.LINE_AA)
cv2.putText(canvas, "Solid Dowel Brace", (sx_start + 45, sub_y + 25), font, 0.4, PLY_COLOR, 1, cv2.LINE_AA)
cv2.putText(canvas, "Electronics Vault", (sx_start + 15, s_height + 15), font, 0.4, TEXT_COLOR, 1, cv2.LINE_AA)

# Dimensional Baseline Annotations
cv2.putText(canvas, "H: 44.0 cm", (20, 240), font, 0.45, TEXT_COLOR, 1, cv2.LINE_AA)
cv2.putText(canvas, "W: 18.0 cm", (100, 485), font, 0.45, TEXT_COLOR, 1, cv2.LINE_AA)
cv2.putText(canvas, "D: 14.0 cm", (390, 485), font, 0.45, TEXT_COLOR, 1, cv2.LINE_AA)

# Save image file directly to workspace directory
cv2.imwrite("speaker_blueprint.png", canvas)

---

File: k1.py


import cv2
import numpy as np

# Initialize canvas (550 High x 350 Wide, White Background for contrast)
canvas = np.ones((550, 350, 3), dtype=np.uint8) * 255

# Color Rules (BGR)
MDF_BORDER = (45, 82, 124)      # Terracotta/Timber edge identifier
CHARCOAL_METAL = (40, 40, 40)   # Matte driver frame finish
LIGHT_GRAY = (220, 220, 220)    # Base vault indicator
TEXT_DARK = (30, 30, 30)        # Label color
LINE_GUIDE = (150, 150, 150)    # Dimension ticks

# 1. Main Cabinet Parameters (19.0cm Wide x 44.0cm High scaled 10px = 1cm)
bx, by = 80, 40
bw, bh = 190, 440
b_center = bx + (bw // 2)

# Structural Bounds
cv2.rectangle(canvas, (bx, by), (bx + bw, by + bh), MDF_BORDER, 3)

# Base Electronics Vault Line (2.6cm total from bottom edge = 26px)
vault_y = by + bh - 26
cv2.line(canvas, (bx, vault_y), (bx + bw, vault_y), MDF_BORDER, 2)
cv2.rectangle(canvas, (bx + 2, vault_y + 1), (bx + bw - 2, by + bh - 2), LIGHT_GRAY, -1)

# Mid-Box Internal Footprint Reference Line (Terminates at 20.2cm from top = 202px)
mid_box_floor_y = by + 202
cv2.line(canvas, (bx + 2, mid_box_floor_y), (bx + bw - 2, mid_box_floor_y), MDF_BORDER, 1, cv2.LINE_AA)

# 2. Driver Cutout Machining Targets (Vertical Center Line = 9.5cm = 95px from edge)
# Tweeter Center: 4.9cm (49px), Radius: 4.4cm (44px)
tw_y = by + 49
cv2.circle(canvas, (b_center, tw_y), 44, CHARCOAL_METAL, 2)
cv2.circle(canvas, (b_center, tw_y), 31, CHARCOAL_METAL, -1)
cv2.line(canvas, (b_center - 50, tw_y), (b_center + 50, tw_y), LINE_GUIDE, 1)

# Midrange Center: 14.8cm (148px), Radius: 4.95cm (50px)
mid_y = by + 148
cv2.circle(canvas, (b_center, mid_y), 50, CHARCOAL_METAL, 2)
cv2.circle(canvas, (b_center, mid_y), 15, CHARCOAL_METAL, -1)
cv2.line(canvas, (b_center - 55, mid_y), (b_center + 55, mid_y), LINE_GUIDE, 1)

# Subwoofer Center: 34.5cm (345px), Radius: 6.67cm (67px)
sub_y = by + 345
cv2.circle(canvas, (b_center, sub_y), 67, CHARCOAL_METAL, 3)
cv2.circle(canvas, (b_center, sub_y), 25, CHARCOAL_METAL, -1)
cv2.line(canvas, (b_center - 72, sub_y), (b_center + 72, sub_y), LINE_GUIDE, 1)

# 3. Geometric Callouts & Measurement Tags
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(canvas, "FRONT BAFFLE PROFILE", (bx + 15, by - 15), font, 0.5, TEXT_DARK, 2, cv2.LINE_AA)

# Side Measurement Markers
cv2.putText(canvas, "0.0 cm", (bx - 55, by + 5), font, 0.35, TEXT_DARK, 1, cv2.LINE_AA)
cv2.putText(canvas, "4.9 cm (Tweet Ctr)", (bx - 55, tw_y + 4), font, 0.35, TEXT_DARK, 1, cv2.LINE_AA)
cv2.putText(canvas, "14.8 cm (Mid Ctr)", (bx - 55, mid_y + 4), font, 0.35, TEXT_DARK, 1, cv2.LINE_AA)
cv2.putText(canvas, "20.2 cm (Mid Floor)", (bx - 55, mid_box_floor_y + 4), font, 0.35, MDF_BORDER, 1, cv2.LINE_AA)
cv2.putText(canvas, "34.5 cm (Sub Ctr)", (bx - 55, sub_y + 4), font, 0.35, TEXT_DARK, 1, cv2.LINE_AA)
cv2.putText(canvas, "41.4 cm (Vault Ctr)", (bx - 55, vault_y + 4), font, 0.35, TEXT_DARK, 1, cv2.LINE_AA)
cv2.putText(canvas, "44.0 cm", (bx - 55, by + bh + 4), font, 0.35, TEXT_DARK, 1, cv2.LINE_AA)

# Dimension Ticks
cv2.putText(canvas, "<- W: 19.0 cm ->", (bx + 35, by + bh + 22), font, 0.4, TEXT_DARK, 1, cv2.LINE_AA)
cv2.putText(canvas, "SB19ST", (bx + bw + 10, tw_y + 4), font, 0.4, CHARCOAL_METAL, 1, cv2.LINE_AA)
cv2.putText(canvas, "TC9FD18", (bx + bw + 10, mid_y + 4), font, 0.4, CHARCOAL_METAL, 1, cv2.LINE_AA)
cv2.putText(canvas, "W5-1138SMF", (bx + bw + 10, sub_y + 4), font, 0.4, CHARCOAL_METAL, 1, cv2.LINE_AA)
cv2.putText(canvas, "Base Vault", (bx + bw + 10, vault_y + 15), font, 0.4, TEXT_DARK, 1, cv2.LINE_AA)

# Export PNG to workspace folder
cv2.imwrite("speaker_blueprint.png", canvas)
Merged workspace files — Kitchen Counter Monitor
Generated: 2026-06-11

---

## File: desktop-idea.md

## 📌 MASTER DESIGN BRIEF: RESUMING PROJECT "KITCHEN COUNTER MONITOR"
Save this entire prompt to paste back to an AI workspace to restart engineering from this exact spot.
------------------------------
## 1. ORIGINAL USER DESIGN CORE PARAMETERS
The goal is to engineer a high-performance, compact, active 3-way vertical tabletop speaker optimized for a kitchen counter where a standing listener is positioned 6 feet away sideways at a sharp 60-degree off-axis angle.

   1. Purely Circular Front Aesthetic: Every single component, driver plate, and routing cut on the exterior must be a true 100% round plate. No rectangular, truncated, or square frames are permitted. All drivers are surface-mounted (no flush-recess routing required).
   2. Vertical Driver Array Geometry: All forward-facing drivers must be stacked strictly vertically down the front panel centerline to eliminate horizontal lobing/comb filtering, ensuring phase consistency and keeping the vocal tonality uniform across the 60-degree sideways sweep.
   3. Internal Volumes & Enclosure: Exactly 1.5 Litres Net for a sealed, isolated midrange chamber, and exactly 7.5 Litres Net for the subwoofer chamber, which utilizes a rear-mounted passive radiator to achieve a flat native 38 Hz tuning without relying on digital bass boost.
   4. Enclosure Materials: All exterior walls built out of 12mm Moisture-Resistant MDF. Internal midrange chamber partition built out of 9mm Plywood to maximize internal airspace efficiency.
   5. Isolated Base Vault: The absolute bottom of the cabinet isolates the power supply and amplification hardware into an external chamber, protecting the electronics from high subwoofer air pressure and air leaks.

------------------------------
## 2. CORE COMPONENT EVALUATION LOG## Tweeter (Locked)

* Model: SB Acoustics SB19ST-C000-4 (19mm textile dome, 88mm round faceplate, factory self-sealed body).
* Evaluation: Evaluated as a perfect off-axis match. The smaller 19mm dome diameter pushes its "beaming" point significantly higher up the frequency band than standard 1" domes, guaranteeing wide horizontal dispersion at the 60° kitchen listening angle.

## Midrange Candidates Evaluated

* Lavoce MD03.10 (Original User Input): Rejected. Closer inspection of the spec sheet revealed "ears" / flat-sided truncated mounting flanges. Surface-mounting would violate the pure circular requirement.
* Tang Band W3-315E (Alu-Mag Full Range): Rejected by user due to a strong visual dislike of the white cone and the protruding silver phase plug.
* Peerless by Tymphany PLS-P830987: Rejected. Features a "pincushion" frame (square with rounded corners), presenting flat edges on the column walls.
* Dayton Audio SIG120-4 (4-inch Signature Series): Evaluated. Solved the style issue with a continuous round frame and a single-piece black dish. However, it required changing the original baffle math significantly due to its wider 123mm frame size.
* Monacor SPX-31M: Evaluated. Paper cone has excellent damping properties, but it was rejected as a downgrade due to its low real sensitivity (~83 dB), low 1.1mm Xmax travel limit, and a protruding silver phase plug that violates the visual rules.
* Dayton Audio DSA90-8 (Option 1 - Locked): 3-inch black anodised aluminium cone, stealth concave dust cap, and low-profile 92.3mm continuous true-circular steel ring. Boasts a massive ±2.5mm Xmax to transition easily to the sub at 120 Hz, high sensitivity (84.7 dB), and runs clean past 8 kHz, integrating seamlessly with the 19mm tweeter.
* Dayton Audio TCP115-8 (Option 2 - Final Evaluation): 4-inch treated paper cone with a high-roll rubber surround and an inverted paper dust cap. True 116mm circular frame profile. Extremely warm and punchy low-mids with ±4.0 mm of long-throw travel. Its main trade-off is a lower sensitivity (81.9 dB), meaning it requires exactly double the amplifier power (+2.8 dB DSP gain adjustment) to match the DSA90-8's output level.

## Subwoofer (Locked)

* Model: Tang Band W5-1138SMF (5.25-inch sub, 133.3mm heavy round frame, massive 9.25mm linear Xmax, heavy magnet structure).
* Evaluation: Class-leading excursion capabilities that provide deep bass out of tiny spaces. Its physical surround sits 8.5mm proud when surface-mounted, recovering roughly 160 mL of internal airspace by sitting outside the 12mm MDF baffle footprint.

## Passive Radiator Evolution

* Dayton Audio ND140-PR (Original 5.25" Round): Evaluated and rejected as too small. The physics of the massive 9.25mm excursion on the active Tang Band sub meant it would easily clip and choke the smaller round radiator at high volumes.
* SB Acoustics SB15SFCR-00 5x8" Racetrack (Locked): Shifting to a narrow oval racetrack design allows you to fit it on the narrow cabinet walls while doubling the surface area ($S_d = 178\text{ cm}^2$) to exactly 2.05 times the active driver volume displacement. It mounts vertically down the rear centerline. It requires adding weight to its rear threaded M6 bolt assembly to counter the stiff internal air spring and drop the native tuning back down to 38 Hz.

------------------------------
## 3. ARCHIVED LAYOUT & DESIGN CONFIGURATIONS## Option A & B (Tall Tower Baseline - Archived)

* Chassis Size: 44.0 cm High × 19.0 cm Wide × 17.6 cm Deep.
* Driver Layout: Strict vertical array: Tweeter on top (center 4.0 cm down), Midrange (center 11.0 cm down), Subwoofer (center 24.5 cm down). This holds a 14.5mm frame-on-frame overlap.
* Internal Partition: The 9mm plywood midrange partition forms a smaller C-shaped horizontal box (16.6 cm W x 8.9 cm D x 12.2 cm H) positioned 7.5 cm down from the top edge. The tweeter sits outside the vault in an open 5.4 cm rear airflow chimney corridor running down the back panel.
* Option A Electronics (Cabled Master-Slave): One active Master tower housing a 24V supply, a JAB5 amp, and a DIPO extension board. Uses 3 internal channels, and routes the remaining 3 channels to 6 heavy-duty binding posts on the rear wall of the dry base vault to connect a future passive Slave tower over a 6-conductor umbilical wire.
* Option B Electronics (Wireless Single-Board 3-Way TWS): User suggested splitting the towers wirelessly. The 6 binding posts are completely eliminated. Both the Master and Slave speakers become independent active towers. Each contains a single JAB5 running a fully discrete 3-way active crossover via Qualcomm’s True Wireless Stereo (TWS) Bluetooth protocol. No external DIPO extension boards are required.

## Option C: The Side-Firing Low-Profile Desktop Monitor (LATEST ACCEPTEED DESIGN)
The user noted a tall tower might look weird under kitchen cabinets and asked to explore moving the subwoofer sideways to drastically drop the height.

* External Proportions: 26.5 cm High × 19.0 cm Wide × 25.2 cm Deep (Dropped height by 17.5 cm; increased depth to preserve the internal volumes and wall displacement math).
* Baffle Alignment (Forward-Facing): Centerline vertical stack. Tweeter center at 4.0 cm down, 3-inch Midrange center at 11.0 cm down (or 11.5 cm down if using the larger 4-inch TCP115). Left/Right side columns look sleek, balanced, and compact on the kitchen counter.
* Side Panel Force-Canceling Matrix: The active Tang Band Subwoofer is mounted on the Left Side Panel (centered 18.5 cm down). The 5x8" Racetrack Passive Radiator is mounted on the Right Side Panel directly opposite the sub on the exact same axis. Their moving masses cancel out mechanically, eliminating cabinet shaking on the counter.
* Internal Partition: The 9mm plywood vault forms a horizontal L-bracket shelf (16.6 cm W x 12.0 cm D x 15.1 cm H) pushed flush to the front baffle. This leaves an open 10.8 cm rear vertical chimney corridor behind the tweeter magnet so the subwoofer airspace vents cleanly to the top cap.

------------------------------
## 4. POWER, HEADROOM & ELECTRICAL VERIFICATION

* Power Supply: Mean Well LRS-150-24 (24V DC, 6.5A Output). Dropping from 36V to 24V eliminates the need for separate step-down buck converters, lowers the idle temperature of the amplifier inside the tight 2.6 cm sealed wooden base drawer, and safely provides enough rail voltage to meet our power limits.
* Peak Electrical Burden: Absolute maximum system current draw when the music hits its loudest transient spikes is calculated at 148.3 Watts Raw / 164.8 Watts DC drawn from the rail (Sub @ 72W Peak into 4Ω, Mid @ 36W Peak into 8Ω, Tweeter @ 8W Peak into 4Ω). The Mean Well 156W continuous supply easily handles these transient surges using its integrated 140% safety overhead.
* Broadband Acoustic Output: Symmetrical active scaling balances the driver efficiencies. When playing at their absolute maximum physical limits simultaneously, the individual outputs sum logarithmically to hit an intense, clear 98.4 dB SPL peak at the 6-foot counter position.
* The Active Crossover Safeguard: In SigmaStudio, the single onboard JAB5 ADAU1701 DSP chip must be programmed with sharp Linkwitz-Riley 24dB/octave slopes (Low-Pass at 120 Hz / Band-Pass 120–2,800 Hz) and a steep 48dB/octave high-pass filter at 2,800 Hz for the tweeter. A -9.5 dB digital gain pad must be hard-coded directly before DAC 2 (the tweeter channel) to drop the 100W JAB5 channel output to a safe 10W ceiling, preventing voice coil damage.

------------------------------
## 🚀 HOW TO RESUME IN THE NEXT SESSION:
Paste this brief back into the prompt box and ask the AI:
"We are building Option C (Side-Firing Low-Profile Cabinet) using the wireless single-board active 3-way layout. Let's make a final choice between the Dayton DSA90-8 and the Dayton TCP115-8 based on our layout spacing, and then generate the exact step-by-step panel cut sheet dimensions or the SigmaStudio block-by-block programming guide."

---

## File: resume-prompt.md

Resume engineering for "Kitchen Counter Monitor" — paste-ready AI prompt
---------------------------------------------------------------

Resume engineering for "Kitchen Counter Monitor" Option C: deliver a finalized `Option C` design (side-firing low-profile monitor) that meets these measurable goals: 98 dB SPL peak at 6 ft, stable tonal balance across 60° horizontal sweep, and native sub extension to 38 Hz. Fixed decisions: tweeter SB19ST-C000-4, sub Tang Band W5-1138SMF, PR SB15SFCR racetrack, Mean Well LRS-150-24 PSU, target sealed mid chamber 1.5 L and sub chamber 7.5 L. Open decision: midrange — compare Dayton DSA90-8 vs TCP115-8 and recommend with quantitative trade-offs (sensitivity, required amp power, baffle interaction, DSP gain).

Required outputs:
1) CNC-ready panel cut sheet for Option C with driver center coordinates, hole diameters, flange offsets, and final net volumes after subtracting driver displacements; include tolerances ±0.5 mm.
2) SigmaStudio block diagram and parameter list implementing: LR24 low-pass @120 Hz, band-pass 120–2800 Hz for mid, HP 48 dB/oct @2800 Hz for tweeter, and a -9.5 dB tweeter pad; include exact DSP gain/attenuation values.
3) Passive-radiator mass calculation to tune SB15SFCR to 38 Hz (show T/S used or fetch them and state assumptions).
4) Thermal check for PSU placement with suggested mitigations if the Mean Well is inside the sealed base vault.
5) Short measurement/test plan: microphone placement (6 ft listening position), target curves, smoothing, and acceptance criteria.

If any physical driver T/S or displacement numbers are missing, fetch them and state assumptions. Provide results as numbered deliverables with acceptance criteria and file-ready artifacts (SVG/CNC cut list, SigmaStudio steps, and a short measurement checklist).

Constraints and decisions extracted from `desktop-idea.md` (include these in all resumed sessions):

- Visual constraint: all front-facing plates, driver plates, and routing cuts must be 100% circular (no rectangular/truncated frames); all drivers are surface-mounted.
- Driver selections (locked):
  - Tweeter: SB Acoustics SB19ST-C000-4 (19 mm textile dome, 88 mm round faceplate).
  - Subwoofer: Tang Band W5-1138SMF (5.25", heavy round frame, 9.25 mm Xmax).
  - Passive radiator: SB Acoustics SB15SFCR-00 5x8" racetrack (mounted vertically on rear centerline); additional mass required to achieve 38 Hz.
- Midrange candidates: Dayton DSA90-8 (3" aluminium, 92.3 mm circular frame) and Dayton TCP115-8 (4" treated paper, 116 mm circular frame). DSA90-8 = higher sensitivity (~84.7 dB); TCP115-8 = warmer low-mids, lower sensitivity (~81.9 dB).
- Enclosure target net volumes (sealed): Midrange chamber 1.5 L net; Subwoofer chamber 7.5 L net. Enclosure materials: 12 mm moisture-resistant MDF exterior, 9 mm plywood internal partition for midrange.
- Option C mechanical layout (accepted): Side-firing low-profile desktop monitor with external dimensions 26.5 cm H × 19.0 cm W × 25.2 cm D. Tweeter center 4.0 cm down, mid center 11.0 cm down (or 11.5 cm for larger mid), sub and PR mounted on opposite side panels centered vertically to cancel forces.
- Electronics & DSP (specified): Mean Well LRS-150-24 (24 V, 6.5 A), JAB5 amp with ADAU1701 DSP, crossover targets: LP @120 Hz, mid band 120–2800 Hz, HP @2800 Hz for tweeter, Linkwitz-Riley 24 dB/oct for LP and BP, 48 dB/oct HP for tweeter; tweeter digital pad -9.5 dB before DAC 2.
- Power/headroom note: Calculated peak electrical draw ~164.8 W DC; projected peak acoustic output ~98.4 dB SPL at 6 ft when drivers driven to physical limits.
- Mechanical notes: Surface-mounted sub surround sits proud of baffle (~8.5 mm), reclaiming ~160 mL internal volume; account for driver displacements and protrusions in final net volumes.
- Manufacturing notes: Base isolates PSU and electronics into a sealed drawer; verify ventilation or relocate PSU if thermal limits exceeded.
- Optional modes: Option A (wired master-slave with umbilical), Option B (wireless single-board active TWS) — wireless adds latency and sync complexity; prefer wired for deterministic performance unless user requires wireless.

Acceptance criteria for prompt execution: deliverables (1–5) exist, include numeric values and units, and are committed as files in the repo when applicable.

Additional terse observations (from desktop-idea.md):
- Passive radiator SB15SFCR: Sd ≈ 178 cm² (~2.05× active driver displacement); mount vertical on rear centerline and add mass to the rear M6-threaded bolt assembly to lower native tuning to 38 Hz.
- Maintain an open rear chimney corridor ≈10.8 cm behind the tweeter magnet to vent sub airspace cleanly to the top cap.
- Tang Band sub surround sits ~8.5 mm proud of the baffle, reclaiming ≈160 mL — include this in final net-volume math.

---

## File: Kitchen Desktop Speaker Prompt.md

Kitchen Desktop Speaker Prompt

I would like you to run an evaluation of mid and tweeter options available on soundimports as in-stock and a total price less than 75£ - considerhow the various combinations of mid/tweet fit with the W5-1138.   comnsider my requirement that the solution allow me to play the speaker at full volume on the TB so the mid/tweet need to keep up. the sonics should remain balanced at all time. there should be sufficient driver and amp / psu overhead so that even when running full tilt the distortions are minimised. optimise for minimal overall volume followed my minimal cost.   I prefer the traditional tweeter/mid/woofer layout in a vertical line but will consider other configurations if they have advantaged.  this will be a speaker in my kitchen on the counter. it is on te left pof the counter about 5 ft away and it is possible to toe-in the speaker so it doesn't need to be absolutely flat against the wall but I generally leave my existing google home max facing into the room mostly, maybe a 10 or 15 degree toe in. this idea is inspired by the ghm which I like but t has no bottom end.   I like the ghm max feature or automatic bass eq boost at lower vols - this is a good listening experience.  the space under the counter is limited and the available verical space is perhap allowing a device 5 cm taller than the ghm.  I alslo want the counter real-estate minimised but not to the extend that it compromises other factors, if there are compromises then bring them to my attention  

---

## File: k.py

```python
# Script to generate a visual schematic diagram of the speaker tower architecture.
# Saving it as a highly structured structural blueprint layout.

import cv2
import numpy as np

# Define canvas sizing (Scale: 10 pixels = 1 cm)
# 450 pixels High x 600 pixels Wide to fit the front and side layouts side-by-side
canvas = np.ones((500, 650, 3), dtype=np.uint8) * 245  # Clean light gray backdrop

# Set Color Palette (BGR format)
MDF_COLOR = (45, 82, 124)       # Deep terracotta/timber hue for 12mm MDF lines
PLY_COLOR = (139, 69, 19)       # Dark blue/brown for 9mm internal plywood lines
DRIVER_COLOR = (30, 30, 30)     # Matte charcoal black for functional metal/cones
TEXT_COLOR = (40, 40, 40)       # Charcoal text for readability
LINE_COLOR = (140, 140, 140)    # Technical dimension lines
VAULT_COLOR = (220, 220, 220)   # Light gray highlight for electronics vault

# --- 1. FRONT BAFFLE VIEW GENERATION ---
# Outer Boundaries (Width: 18cm = 180px, Height: 44cm = 440px)
fx_start, fy_start = 50, 30
f_width, f_height = 180, 440
fx_center = fx_start + (f_width // 2)

# Main Carcass Outline
cv2.rectangle(canvas, (fx_start, fy_start), (fx_start + f_width, fy_start + f_height), MDF_COLOR, 3)

# Base Electronics Vault Line (2.6 cm total from bottom edge = 26px)
cv2.line(canvas, (fx_start, fy_start + f_height - 26), (fx_start + f_width, fy_start + f_height - 26), MDF_COLOR, 2)
cv2.rectangle(canvas, (fx_start+2, fy_start + f_height - 26), (fx_start + f_width - 2, fy_start + f_height), VAULT_COLOR, -1)

# Draw Round Drivers Down the Center-Line
# Tweeter (Center Mark: 4.9cm = 49px from top, Outer Radius: 4.4cm = 44px)
tw_y = fy_start + 49
cv2.circle(canvas, (fx_center, tw_y), 44, DRIVER_COLOR, 2)  # Outer Recess Ring
cv2.circle(canvas, (fx_center, tw_y), 31, DRIVER_COLOR, -1) # Inner Dome Assembly

# Midrange (Center Mark: 14.8cm = 148px from top, Outer Radius: 4.95cm = 50px)
mid_y = fy_start + 148
cv2.circle(canvas, (fx_center, mid_y), 50, DRIVER_COLOR, 2)  # Outer Ring
cv2.circle(canvas, (fx_center, mid_y), 40, DRIVER_COLOR, 1)  # Cone Edge
cv2.circle(canvas, (fx_center, mid_y), 15, DRIVER_COLOR, -1) # Center Dust Cap

# Subwoofer (Center Mark: 31.2cm = 312px from top, Outer Radius: 6.67cm = 67px)
sub_y = fy_start + 312
cv2.circle(canvas, (fx_center, sub_y), 67, DRIVER_COLOR, 3)  # Heavy Steel Outer Ring
cv2.circle(canvas, (fx_center, sub_y), 55, DRIVER_COLOR, 2)  # High-Roll Rubber Surround
cv2.circle(canvas, (fx_center, sub_y), 25, DRIVER_COLOR, -1) # Large Heavy Dust Cap


# --- 2. SIDE CROSS-SECTION VIEW GENERATION ---
# Outer Boundaries (Depth: 14cm = 140px, Height: 44cm = 440px)
sx_start, sy_start = 350, 30
s_depth, s_height = 140, 440

# Base Chassis Outline
cv2.rectangle(canvas, (sx_start, sy_start), (sx_start + s_depth, sy_start + s_height), MDF_COLOR, 3)

# Internal 12mm Wood Thickness Lines (Top, Bottom, Front, Back walls = 12px)
cv2.rectangle(canvas, (sx_start + 12, sy_start + 12), (sx_start + s_depth - 12, sy_start + s_height - 12), MDF_COLOR, 1)

# Base Electronics Vault Shelf (1.2cm bottom cap + 1.4cm internal height = 26px up)
v_shelf_y = sy_start + s_height - 26
cv2.line(canvas, (sx_start + 12, v_shelf_y), (sx_start + s_depth - 12, v_shelf_y), MDF_COLOR, 2)
cv2.rectangle(canvas, (sx_start + 12, v_shelf_y), (sx_start + s_depth - 12, sy_start + s_height - 12), VAULT_COLOR, -1)

# Floating Mid-Box Partition Layout (9mm Plywood = 9px thickness)
# Positioned exactly around the midrange driver zone (Height: 11.2cm = 112px, Depth: 8.6cm = 86px)
mid_box_top = sy_start + 92
mid_box_bottom = sy_start + 204
mid_box_depth = sx_start + 12 + 86

# Draw Floating Box Partition
cv2.line(canvas, (sx_start + 12, mid_box_top), (mid_box_depth, mid_box_top), PLY_COLOR, 3)       # Top Plate
cv2.line(canvas, (sx_start + 12, mid_box_bottom), (mid_box_depth, mid_box_bottom), PLY_COLOR, 3) # Bottom Plate
cv2.line(canvas, (mid_box_depth, mid_box_top), (mid_box_depth, mid_box_bottom), PLY_COLOR, 3)   # Back Wall Plate

# Internal Hardwood Dowel Brace In Subwoofer Zone (Radius: 10px = 20mm cross section)
# Centered precisely behind the heavy subwoofer magnet
dowel_x = sx_start + 12 + 58
dowel_y = sy_start + 312
cv2.circle(canvas, (dowel_x, dowel_y), 10, PLY_COLOR, -1)

# Driver Protrusions (Side Profile Representation)
# Tweeter (Top)
cv2.rectangle(canvas, (sx_start - 5, tw_y - 20), (sx_start + 15, tw_y + 20), DRIVER_COLOR, -1)
# Midrange (Middle, inside its isolated box pocket)
cv2.rectangle(canvas, (sx_start - 5, mid_y - 35), (sx_start + 12, mid_y + 35), DRIVER_COLOR, -1)
cv2.rectangle(canvas, (sx_start + 12, mid_y - 15), (sx_start + 45, mid_y + 15), DRIVER_COLOR, -1) # Magnet
# Subwoofer (Bottom, tracking flush to side walls)
cv2.rectangle(canvas, (sx_start - 8, sub_y - 60), (sx_start + 12, sub_y + 60), DRIVER_COLOR, -1)
cv2.rectangle(canvas, (sx_start + 12, sub_y - 45), (sx_start + 85, sub_y + 45), DRIVER_COLOR, -1) # Massive Magnet

# Rear Mounted 5x8" Oval Passive Radiator (Centered behind the bypass chimney)
pr_y = sy_start + 220
cv2.rectangle(canvas, (sx_start + s_depth - 12, pr_y - 50), (sx_start + s_depth + 5, pr_y + 50), DRIVER_COLOR, -1)


# --- 3. BLUEPRINT LABELS & ANNOTATIONS ---
font = cv2.FONT_HERSHEY_SIMPLEX

# Structural Titles
cv2.putText(canvas, "FRONT VIEW", (80, 20), font, 0.5, TEXT_COLOR, 2, cv2.LINE_AA)
cv2.putText(canvas, "SIDE CROSS-SECTION", (340, 20), font, 0.5, TEXT_COLOR, 2, cv2.LINE_AA)

# Component Direct Callouts
cv2.putText(canvas, "SB19ST Tweeter", (fx_start + f_width + 10, tw_y + 4), font, 0.4, TEXT_COLOR, 1, cv2.LINE_AA)
cv2.putText(canvas, "Peerless TC9 Mid", (fx_start + f_width + 10, mid_y + 4), font, 0.4, TEXT_COLOR, 1, cv2.LINE_AA)
cv2.putText(canvas, "Tang Band W5 Sub", (fx_start + f_width + 10, sub_y + 4), font, 0.4, TEXT_COLOR, 1, cv2.LINE_AA)

cv2.putText(canvas, "Sealed 1.5L Mid Vault", (sx_start - 160, mid_box_top + 45), font, 0.4, PLY_COLOR, 1, cv2.LINE_AA)
cv2.putText(canvas, "Vertical Sub Chimney", (sx_start + 42, mid_box_top + 55), font, 0.4, MDF_COLOR, 1, cv2.LINE_AA)
cv2.putText(canvas, "5x8\" Passive Rad.", (sx_start + s_depth + 10, pr_y + 4), font, 0.4, DRIVER_COLOR, 1, cv2.LINE_AA)
cv2.putText(canvas, "Solid Dowel Brace", (sx_start + 45, sub_y + 25), font, 0.4, PLY_COLOR, 1, cv2.LINE_AA)
cv2.putText(canvas, "Electronics Vault", (sx_start + 15, s_height + 15), font, 0.4, TEXT_COLOR, 1, cv2.LINE_AA)

# Dimensional Baseline Annotations
cv2.putText(canvas, "H: 44.0 cm", (20, 240), font, 0.45, TEXT_COLOR, 1, cv2.LINE_AA)
cv2.putText(canvas, "W: 18.0 cm", (100, 485), font, 0.45, TEXT_COLOR, 1, cv2.LINE_AA)
cv2.putText(canvas, "D: 14.0 cm", (390, 485), font, 0.45, TEXT_COLOR, 1, cv2.LINE_AA)

# Save image file directly to workspace directory
cv2.imwrite("speaker_blueprint.png", canvas)
```

---

## File: k1.py

```python


import cv2
import numpy as np

# Initialize canvas (550 High x 350 Wide, White Background for contrast)
canvas = np.ones((550, 350, 3), dtype=np.uint8) * 255

# Color Rules (BGR)
MDF_BORDER = (45, 82, 124)      # Terracotta/Timber edge identifier
CHARCOAL_METAL = (40, 40, 40)   # Matte driver frame finish
LIGHT_GRAY = (220, 220, 220)    # Base vault indicator
TEXT_DARK = (30, 30, 30)        # Label color
LINE_GUIDE = (150, 150, 150)    # Dimension ticks

# 1. Main Cabinet Parameters (19.0cm Wide x 44.0cm High scaled 10px = 1cm)
bx, by = 80, 40
bw, bh = 190, 440
b_center = bx + (bw // 2)

# Structural Bounds
cv2.rectangle(canvas, (bx, by), (bx + bw, by + bh), MDF_BORDER, 3)

# Base Electronics Vault Line (2.6cm total from bottom edge = 26px)
vault_y = by + bh - 26
cv2.line(canvas, (bx, vault_y), (bx + bw, vault_y), MDF_BORDER, 2)
cv2.rectangle(canvas, (bx + 2, vault_y + 1), (bx + bw - 2, by + bh - 2), LIGHT_GRAY, -1)

# Mid-Box Internal Footprint Reference Line (Terminates at 20.2cm from top = 202px)
mid_box_floor_y = by + 202
cv2.line(canvas, (bx + 2, mid_box_floor_y), (bx + bw - 2, mid_box_floor_y), MDF_BORDER, 1, cv2.LINE_AA)

# 2. Driver Cutout Machining Targets (Vertical Center Line = 9.5cm = 95px from edge)
# Tweeter Center: 4.9cm (49px), Radius: 4.4cm (44px)
tw_y = by + 49
cv2.circle(canvas, (b_center, tw_y), 44, CHARCOAL_METAL, 2)
cv2.circle(canvas, (b_center, tw_y), 31, CHARCOAL_METAL, -1)
cv2.line(canvas, (b_center - 50, tw_y), (b_center + 50, tw_y), LINE_GUIDE, 1)

# Midrange Center: 14.8cm (148px), Radius: 4.95cm (50px)
mid_y = by + 148
cv2.circle(canvas, (b_center, mid_y), 50, CHARCOAL_METAL, 2)
cv2.circle(canvas, (b_center, mid_y), 15, CHARCOAL_METAL, -1)
cv2.line(canvas, (b_center - 55, mid_y), (b_center + 55, mid_y), LINE_GUIDE, 1)

# Subwoofer Center: 34.5cm (345px), Radius: 6.67cm (67px)
sub_y = by + 345
cv2.circle(canvas, (b_center, sub_y), 67, CHARCOAL_METAL, 3)
cv2.circle(canvas, (b_center, sub_y), 25, CHARCOAL_METAL, -1)
cv2.line(canvas, (b_center - 72, sub_y), (b_center + 72, sub_y), LINE_GUIDE, 1)

# 3. Geometric Callouts & Measurement Tags
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(canvas, "FRONT BAFFLE PROFILE", (bx + 15, by - 15), font, 0.5, TEXT_DARK, 2, cv2.LINE_AA)

# Side Measurement Markers
cv2.putText(canvas, "0.0 cm", (bx - 55, by + 5), font, 0.35, TEXT_DARK, 1, cv2.LINE_AA)
cv2.putText(canvas, "4.9 cm (Tweet Ctr)", (bx - 55, tw_y + 4), font, 0.35, TEXT_DARK, 1, cv2.LINE_AA)
cv2.putText(canvas, "14.8 cm (Mid Ctr)", (bx - 55, mid_y + 4), font, 0.35, TEXT_DARK, 1, cv2.LINE_AA)
cv2.putText(canvas, "20.2 cm (Mid Floor)", (bx - 55, mid_box_floor_y + 4), font, 0.35, MDF_BORDER, 1, cv2.LINE_AA)
cv2.putText(canvas, "34.5 cm (Sub Ctr)", (bx - 55, sub_y + 4), font, 0.35, TEXT_DARK, 1, cv2.LINE_AA)
cv2.putText(canvas, "41.4 cm (Vault Ctr)", (bx - 55, vault_y + 4), font, 0.35, TEXT_DARK, 1, cv2.LINE_AA)
cv2.putText(canvas, "44.0 cm", (bx - 55, by + bh + 4), font, 0.35, TEXT_DARK, 1, cv2.LINE_AA)

# Dimension Ticks
cv2.putText(canvas, "<- W: 19.0 cm ->", (bx + 35, by + bh + 22), font, 0.4, TEXT_DARK, 1, cv2.LINE_AA)
cv2.putText(canvas, "SB19ST", (bx + bw + 10, tw_y + 4), font, 0.4, CHARCOAL_METAL, 1, cv2.LINE_AA)
cv2.putText(canvas, "TC9FD18", (bx + bw + 10, mid_y + 4), font, 0.4, CHARCOAL_METAL, 1, cv2.LINE_AA)
cv2.putText(canvas, "W5-1138SMF", (bx + bw + 10, sub_y + 4), font, 0.4, CHARCOAL_METAL, 1, cv2.LINE_AA)
cv2.putText(canvas, "Base Vault", (bx + bw + 10, vault_y + 15), font, 0.4, TEXT_DARK, 1, cv2.LINE_AA)

# Export PNG to workspace folder
cv2.imwrite("speaker_blueprint.png", canvas)
```
