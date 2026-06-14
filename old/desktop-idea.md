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

