import math

# === PR TUNING — net sub volume recalculation for soil pipe mid box ===
gross = 0.166 * 0.185 * 0.246          # 7.54 L
sub_basket_vol = 0.51e-3               # 0.51 L (confirmed from prior calc)
pipe_od_m = 0.110                      # 110 mm OD
pipe_len_m = 0.070                     # 70 mm long
soil_pipe_vol = math.pi * (pipe_od_m/2)**2 * pipe_len_m   # outer volume
tweeter_vol = 0.05e-3
net_sub_vol = gross - sub_basket_vol - soil_pipe_vol - tweeter_vol
print(f"Net sub volume (soil pipe): {net_sub_vol*1000:.2f} L  (was 5.8 L with MDF box)")

Vb = net_sub_vol
rho_c2 = 142356                       # rho0 * c^2 Pa (N/m^2)
Sd_pr  = 178e-4                       # m^2
Mms_pr = 0.062                        # kg stock
Fs_pr  = 21.0                         # Hz stock
Kms = Mms_pr * (2*math.pi*Fs_pr)**2
Kair = rho_c2 * Sd_pr**2 / Vb
print(f"Kms={Kms:.0f} N/m  Kair={Kair:.0f} N/m  (Kair at {Vb*1000:.2f} L)")
print(f"{'Target Fb':>12} {'Mms total':>12} {'Added mass':>12}")
for Fb in [35, 38, 40, 42, 45]:
    omega_b = 2*math.pi*Fb
    Mms_total = (Kms + Kair) / omega_b**2
    added = Mms_total - Mms_pr
    print(f"{Fb:>10} Hz {Mms_total*1000:>10.0f} g {added*1000:>11.0f} g")
print()


V = 29.0   # supply voltage
eta = 0.85
idle = 0.5  # amp idle current

# Sub: W5-1138SMF, 4 ohm, 85 dB @ 2.83V/1m
sub_imp = 4.0
sub_sens_283 = 85.0
sub_sens_1w = sub_sens_283 - 10*math.log10(2.83**2 / sub_imp)
p_sub_98  = 10**((98  - sub_sens_1w)/10)
p_sub_101 = 10**((101 - sub_sens_1w)/10)

# DS115-8 mid: 8 ohm, 85.3 dB @ 2.83V/1m
mid_imp = 8.0
mid_sens_283 = 85.3
mid_sens_1w = mid_sens_283 - 10*math.log10(2.83**2 / mid_imp)
p_mid_98  = 10**((98  - mid_sens_1w)/10)
p_mid_101 = 10**((101 - mid_sens_1w)/10)

# R2604/833000 tweeter: 4 ohm, 92 dB @ 2.83V/1m
tw_imp = 4.0
tw_sens_283 = 92.0
tw_sens_1w = tw_sens_283 - 10*math.log10(2.83**2 / tw_imp)
p_tw_98  = 10**((98  - tw_sens_1w)/10)
p_tw_101 = 10**((101 - tw_sens_1w)/10)

print(f"{'Driver':<18} {'Sens 1W':>8} {'P @ 98dB':>10} {'P @ 101dB':>10} {'Avail 29V':>10} {'Margin':>8}")
print("-"*70)
for name, imp, s1w, p98, p101 in [
    ("Sub W5-1138SMF",    sub_imp, sub_sens_1w, p_sub_98,  p_sub_101),
    ("DS115-8 mid",       mid_imp, mid_sens_1w, p_mid_98,  p_mid_101),
    ("R2604/833000 tweet",tw_imp,  tw_sens_1w,  p_tw_98,   p_tw_101),
]:
    avail = (V**2 / (2*imp)) * eta
    margin = 10*math.log10(avail/p101)
    print(f"{name:<18} {s1w:>7.1f}dB {p98:>9.1f}W {p101:>9.1f}W {avail:>9.1f}W {margin:>+7.1f}dB")

print()
total_rms   = p_sub_98  + p_mid_98  + p_tw_98
total_burst = p_sub_101 + p_mid_101 + p_tw_101
I_rms   = total_rms   / V + idle
I_burst = total_burst / V + idle

print(f"Total power @ 98dB (RMS): {total_rms:.1f} W  ->  {I_rms:.2f} A at {V}V")
print(f"Total power @101dB (burst):{total_burst:.1f} W  ->  {I_burst:.2f} A at {V}V")

print()
print("=== PSU OPTIONS ===")
# No LRS-150 variant at 27V/29V exists. LRS-150-36 at 36V: 154.8W / 36V = 4.3A rated.
# RSP-150-27 (different series, larger) at 27V trimmed to 29V: ~5.17A.
# Using RSP-150-27 trimmed as nearest Mean Well reference.
psu_rsp150_27 = 5.17  # 150W / 29V
print(f"RSP-150-27 @ 29V (trimmed):  ~{psu_rsp150_27}A available vs {I_burst:.2f}A burst -> {(psu_rsp150_27-I_burst)*1000:+.0f} mA margin  (barely sufficient, no cap bank = RISKY)")

# With cap bank: PSU only needs to supply RMS; caps supply burst
psu_rms_needed = I_rms
print(f"\nWith 4x10,000 uF cap bank (40,000 uF / 35V):")
print(f"  PSU supplies RMS:  {psu_rms_needed:.2f} A  -- RSP-150-27 @ 29V rated ~5.17A, margin = {(psu_rsp150_27 - psu_rms_needed):.2f}A  OK")
# Cap bank supplies burst supplement
I_cap = I_burst - I_rms
print(f"  Caps supply extra: {I_cap:.2f} A during transient peaks")
# Rail sag over 10ms burst
C_total = 4 * 10e-3   # 4 x 10,000 uF = 40,000 uF = 0.04 F
delta_V_10ms = (I_cap * 0.010) / C_total
print(f"  Rail sag over 10ms burst: {delta_V_10ms*1000:.0f} mV  (V drops {V} -> {V-delta_V_10ms:.2f} V)  OK")
delta_V_50ms = (I_cap * 0.050) / C_total
print(f"  Rail sag over 50ms burst: {delta_V_50ms*1000:.0f} mV  (V drops to {V-delta_V_50ms:.2f} V)  OK")

print()
print("=== BASE FITTING ===")
jab5_l, jab5_w, jab5_h = 121.92, 91.44, 45.1

base_int_w = 190 - 12 - 12   # 166
base_int_d = 215 - 12 - 12   # 191
base_int_h = 80 - 12 - 12    # 56

print(f"Base internal: {base_int_w} x {base_int_d} x {base_int_h} mm  (W x D x H)")
print(f"JAB5:          {jab5_l} x {jab5_w} x {jab5_h} mm")
print()

for psu_name, psu_l, psu_w, psu_h in [
    ("LRS-150-36 (Mean Well, no 27/29V variant exists)", 159.0, 97.0, 30.0),
    ("AliExpress 127x83x38 (pending)", 127.0, 83.0, 38.0),
]:
    print(f"PSU: {psu_name}  [{psu_l} x {psu_w} x {psu_h} mm]")
    depth_needed = jab5_w + 10 + psu_w
    spare = base_int_d - depth_needed
    status = "OK" if spare >= 0 else f"SHORT by {-spare:.1f} mm"
    print(f"  Side-by-side depth: {jab5_w}+10+{psu_w} = {depth_needed:.1f} mm vs {base_int_d} mm -> {spare:+.1f} mm  {status}")
    print(f"  PSU width {psu_l} mm in base width {base_int_w} mm -> {base_int_w-psu_l:.1f} mm spare")
    print(f"  PSU height {psu_h} mm in base internal height {base_int_h} mm -> {base_int_h-psu_h:.1f} mm clearance above PSU")
    h_stacked = psu_h + 5 + jab5_h
    print(f"  Stacked: {psu_h}+5+{jab5_h} = {h_stacked:.1f} mm vs {base_int_h} mm -> {'FITS' if h_stacked <= base_int_h else f'DOES NOT FIT ({h_stacked-base_int_h:.1f} mm over)'}")
    print()
