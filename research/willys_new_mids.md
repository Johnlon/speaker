# Willys-Hifi New Midrange Candidates — June 2026 Sweep

Drivers not yet in `drivers.md` or `si_tweeter_index.md`. Fetched from willys-hifi.com June 2026.
To merge: add passing candidates to drivers.md midrange section.

**Exchange rate reference:** €1 ≈ £0.85 (June 2026)

---

## New Candidates (not in current index)

### SB Acoustics SB12CACS25-4 — ceramic cone midwoofer
- Size: 4" | Frame OD: 123 mm | Impedance: 4Ω | Re: 3.1Ω
- Cone: White ceramic bonded to aluminium substrate | Surround: rubber
- Sensitivity: **88 dB @ 2.83V/1m** | Power: **30W RMS** | Fs: **51 Hz** | Qts: 0.31 | Qes: 0.33 | Qms: 4.89 | Vas: 5.7 L
- Xmax: not confirmed on page
- **Source:** [Willys-Hifi](https://willys-hifi.com/products/sb-acoustics-sb12cacs25-4-ceramic-midwoofer-speaker) | Price: **£58.96** | Stock: UK in stock June 2026
- **Also available:** 8Ω version SB12CACS25-8 at £58.96
- **Fs check:** 51 Hz → 2.94× at 150 Hz crossover ✓ (comfortable margin).
- **DSP correction vs TB sub (85 dB ref):** −3.0 dB pad.
- **Power at reference (98 dB):** 10^(10/10) = 10.0W (33% of 30W ✓). Burst 101 dB: 20.0W (67% ✓). Headroom adequate.
- **Beaming (Sd ~50 cm², same class as SB12PFCR25-4):** beaming ≈ 2,730 Hz — fine at 2,800 Hz crossover.
- **Why interesting:** SB Acoustics ceramic construction claims "excellent stiffness to damping ratio" — potentially lower cone coloration and sharper transient. Ceramic cones tend to have very flat pass-band but often have hard breakup resonances.
- **Concern — breakup:** Ceramic cone breakup resonances can be severe. Need to verify FR plot from datasheet to confirm no prominent breakup below 3,500 Hz, which would land uncomfortably close to the 2,800 Hz crossover. LR48 provides 48 dB/oct roll but breakup at 3,000 Hz would be a concern.
- **Concern — cost:** £58.96 is by far the most expensive mid candidate. More than twice the SB12PFCR25-4 (£20.58) for similar sensitivity and power.
- **Concern — colour:** White ceramic cone is visually distinct. Owner has removed visual exclusions; noted as unusual but not grounds for rejection.
- **vs SB12PFCR25-4 (£20.58 Willys):** PFCR: 87.5 dB, 30W, Fs 58 Hz, Qts 0.43, paper. CACS: 88 dB, 30W, Fs 51 Hz, Qts 0.31 — marginally better T/S but at 2.87× price premium. Only justified if ceramic breakup is confirmed above 3 kHz from datasheet.
- **Action required:** Fetch SB Acoustics CACS25-4 datasheet; confirm FR and breakup from FR plot before ordering.

---

## Screened — Rejected

| Model | Willys price | Reason |
|-------|-------------|--------|
| SB13PFCR25-4 | £24.50 | Frame 150mm → beaming ≈ 2,300–2,500 Hz; tight crossover window ≤500 Hz; large baffle required |
| SB13PFCR25-8 | £24.50 | Same concerns as 4Ω version |
| SB12NRXF25-4 | £43.11 | Foam surround (longevity concern); Fs 61 Hz, Qts 0.48 — inferior to SB12PFCR25-4 (£20.58, butyl) and NRX25-4 (£45.75, butyl) already indexed |
| SB12NRXF25-8 | £43.11 | Same concerns as 4Ω version |
| Monacor MSH-115 | £41.57 | Fs 85 Hz → 1.76× at 150 Hz crossover — below 2× minimum |
| Monacor MSH-115HQ | £49.70 | Expected similar Fs — below 2× minimum. Specs not fetched. |
| Fountek FW100B | £34.15 | Fs 77 Hz → 1.95× at 150 Hz (marginal); power exceeds 35W at burst 101 dB; square pincushion 104×104mm frame |
| Peerless HDS-106 P830870 | £38.78 | Fs 100 Hz → 1.5× at 150 Hz — well below 2× minimum |
| SB12NRX25-8 | £45.75 | 8Ω version of NRX25-4 (already in index). At 8Ω: available ~31W; burst needs 25W — fine but limits to 29V PSU for headroom. Add to index as 8Ω option only. |

---

## New Woofer/Full-Range — Screened (for completeness)

| Model | Willys price | Verdict |
|-------|-------------|---------|
| SB65WBAC25-4 | £25.95 | 2.5" full range — too small for 150–2800 Hz mid role |
| SB10PGC21-4 | £15.80 | 3" polypropylene glass — very small; no specs fetched |
| Scanspeak 12W/4524G00 | £53.10 | 4" Discovery Range mid — specs not fetched; expensive |
| Scanspeak 12W/8524G00 | £53.10 | 8Ω version — same; specs not fetched |

---

## Price / Stock Corrections for Indexed Mids

| Model | SI price | Willys price | Saving | Notes |
|-------|---------|-------------|--------|-------|
| SB12NRX25-4 | €59.95 (≈£51.0) | **£45.75** | £5.3 | Update drivers.md — Willys is preferred source |
| SB12PFCR25-4 | €25.95 (≈£22.1) | **£20.58** | £1.5 | Update drivers.md |
| SB12PACR25-4 | £23.76 (Willys already noted in drivers.md) | £23.76 | — | Already correct |
| SB12PAC25-4 | not in index | **£22.54** | — | "PAC" plain chassis (no rear faceplate ring). Almost certainly same driver as PACR25-4 minus the rear ring. Not worth adding separately unless PACR25-4 goes OOS. |

---

## Out of Scope — 5"+ Woofers (Willys in stock)

Listed for completeness; too large for mid role in this build (beaming starts <2,000 Hz):

- SB15 series (5.5", 140mm frame) — SB15MFC30-4 £54.30, SB15NRX2C30-4 £46.75, SB15CAC30-4 £79.53, SB15CRC30-4 £88.80, SB15NBAC30-4 £64.65
- Scanspeak 15W series (6.5") — £49.63–£280.63
- SB Acoustics Satori MW13P series — £129.61

These are full-range woofer class; crossover to tweeter would need to be below 1,800 Hz and centre spacing would exceed any tweeter candidate. Not applicable.

*Sources: willys-hifi.com product pages fetched June 2026*
