# Driver measurement-data store (FRD / ZMA)

Layout: `datafiles/<driver>/FRD/*.frd`, `.../ZMA/*.zma`, plus the vendor's GRAPH/TEXT/README.
FRD = frequency response (Hz, SPL dB, phase°); ZMA = impedance (Hz, Ω, phase°). Off-axis FRDs are named `…@<angle>.frd`.

## Stored — official Dayton data (less-smoothed than the glossy datasheet; trust these)

| Driver | Angles | Source |
|--------|--------|--------|
| **DC28F-8** | 0/15/30/45° + ZMA | daytonaudio.com `DC28F-8_data.zip` |
| **DC28FS-8** | 0/15/30/45° + ZMA | daytonaudio.com `DC28FS-8_data.zip` |
| **DC28FT-8** | 0/15/30/45° + ZMA | daytonaudio.com `DC28FT-8_data.zip` |

Dayton stops at **45°** (no 60°). These FRDs expose the real response ripple the datasheet PDF smooths out (see `research/tweeter_offaxis_evidence.md` §6).

## DIGITISED FRD — SB survivors (no official FRD exists for SB)

SB Acoustics publishes no FRD (PDF datasheets only); the artisanacoustics Google-Drive folder is **dead**. So these are **traced by eye from the 400-DPI datasheet polar renders** (`research/speakers/_render/*_full-1.png`) — magnitude only, ~±1–2 dB, **no phase** (derive minimum-phase in the sim tool). Approximate, NOT a measurement.

| Driver | Files |
|--------|-------|
| **SB19ST-C000-4** | `FRD/SB19ST-C000-4_DIGITISED@{0,30,60}.frd` |
| **SB21SDCN-C000-4** | `FRD/SB21SDCN-C000-4_DIGITISED@{0,30,60}.frd` (also has independent HiFiCompass measurement — review PDF on file) |

Digitised 60° vs on-axis: SB19ST ≈ −4 @ 10 k, −5 @ 15 k, −11 @ 20 k. SB21SDCN ≈ −2 @ 10 k, −5 @ 15 k, −8 @ 20 k.

## Out / not pursued

- **Peerless NE19VTS-04** — ❌ OUT (conflicting datasheets: 88.3 vs 90.4 dB, 100 vs 20 W; 60° ordinary). No FRD gathered.
- **SB26ADC-C000-4 / SB17NBAC35-4** — real community FRD/ZMA exist in a [diyAudio sharing thread](https://www.diyaudio.com/community/threads/sbacoustics-nac-61-sb17nbac35-4-and-sb26adc000-4-frd-zma-sharing.403170/) (downloadable attachments), but these are not on the shortlist — grab only if SB26ADC becomes a candidate.
