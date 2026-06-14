# SoundImports Tweeter Index — Populated Spec Reference
Pages 4–6 scanned June 2026. Specs populated June 2026 from SI product pages, drivers.md, and datasheets.

**Status codes:** ✓ in drivers.md | ★ new candidate | ~ weak/concern | ✗ rejected | OOS | ? need fetch

---

## Tweeter Candidates

| Model                    | Type      | Imp | Price         | Stock          | Fs Hz  | Sens dB | Pwr W | FP OD mm    | Dome mm  | Min Xover Hz | Status                                               |
| ------------------------ | --------- | --- | ------------- | -------------- | ------ | ------- | ----- | ----------- | -------- | ------------ | ---------------------------------------------------- |
| ND20FA-6                 | Dome      | 6Ω  | €14.95        | 10+            | 2,005  | 91.5    | 15    | 45          | 19       | 4,010        | ✓ — highest min-xover; tiny FP                       |
| ND25FA-4                 | Dome      | 4Ω  | €15.95        | 10+            | 1,350  | 90      | 20    | 66          | 25       | 2,700        | ✓ (B10) — compact FP                                 |
| DC25T-8                  | Dome (Ti) | 8Ω  | €18.97        | 10+            | 1,468  | 93      | 50    | —           | 25       | 2,936        | ✓ — Ti dome; bright                                  |
| SB19ST-C000-4            | Dome      | 4Ω  | €21.45        | 10+            | 980    | 88.5    | 30    | 88          | 19       | 1,960        | ✓ (S1,S2,A1–A3,A6–A8,B1,B5) — reference              |
| BC25SC06-04              | Dome      | 4Ω  | €24.95        | 10+            | 1,350  | 95.4    | 50    | ~70         | 25       | 2,700        | ✓ — 50W; high sens; confirm colour                   |
| HiVi TN25                | Dome      | 5Ω  | €25.45        | 5              | 1,500  | 91      | 20    | 54×54 sq    | 25       | 3,000        | ✓ (B6) — square FP; tightest spacing                 |
| XT25SC90-04              | Ring Rad  | 4Ω  | £18.20 Falcon | 10+            | 825    | 90.1    | 100   | ~90         | 25       | 1,650        | ✓ (RR4) — 100W; UK stock                             |
| OC25SC65-04              | Dome      | 4Ω  | €26.95        | 10+            | 1,400  | 92.3    | 12    | 41 no plate | 25       | 2,800        | ✗ no faceplate; 12W                                  |
| SB14ST-C000-4            | Dome      | 4Ω  | €28.45        | exp 27-08-2026 | —      | —       | —     | —           | 14       | —            | OOS Aug 2026                                         |
| BC25TG15-04              | Dome      | 4Ω  | €29.95        | 10+            | 1,100  | 93.9    | 7     | 104         | 25       | 2,200        | ✗ 7W power rating fatal                              |
| DT-25N                   | Dome      | 8Ω  | €29.95        | 10+            | 1,600  | 95      | 40    | 66          | 25       | 3,200        | ✓ — high Fs; min xover 3,200 Hz                      |
| Swan TN28-B              | Dome      | 6Ω  | €29.95        | 10+            | 1,300  | 90      | 15    | 47.6        | 28       | 2,600        | ★ ultra-compact FP 47.6mm; tight spacing potential   |
| XT25SC40-04              | Ring Rad  | 4Ω  | €29.95        | 10+            | 1,018  | 94      | 100   | 43.9        | 25       | 2,036        | ★ SMALLEST ring rad FP 43.9mm; 100W; min xover 2036  |
| DT 94-8                  | Dome      | 8Ω  | €29.95        | 3              | 1,900  | 90      | 70    | 94          | 20       | 3,800        | ✗ min xover 3800Hz exceeds 2800Hz project target     |
| DX20BF00-04              | Dome      | 4Ω  | €29.95        | 10+            | 840    | 88      | 10    | 66          | 20       | 1,680        | ✗ 10W — fatal at burst; needs 20W at 101dB          |
| TD25F-4                  | Dome(semi)| 4Ω  | €29.95        | 10+            | 900    | 91      | 20    | 93.5        | 25       | 1,800        | ✓ — semi-horn FP; Cutout 70mm; Depth 32mm; narrows off-axis |
| GT-525                   | Dome      | 8Ω  | €29.95        | 4              | —      | —       | —     | —           | 25       | —            | ? URL not found on SI (tried 3 patterns)             |
| SB26ST-C000-5            | Dome      | 5Ω  | €30.95        | 10+            | 870    | 91      | 80    | ~72         | 26       | 1,740        | ★ 80W; assumed ~72mm FP (SB26 family); ST1-3 pairings |
| DX25TG59-04              | Dome      | 4Ω  | €32.95        | 10+            | 590    | 93.4    | 15    | 104         | 25       | 1,180        | ✓ (A4,A5,B3,B4,B7,B8) — best Fs margin               |
| XT19TD00-04              | Ring Rad  | 4Ω  | €34.95        | 10+            | ~820   | 88.9    | 20    | 94          | 19       | ~1,640       | ✓ — small ring rad; 94mm FP                          |
| SB26STC-C000-04          | Dome      | 4Ω  | €34.95        | exp 28-08-2026 | —      | —       | —     | —           | 26       | —            | OOS Aug 2026                                         |
| DTM-104/8                | Dome      | 8Ω  | €34.95        | exp 31-07-2026 | —      | —       | —     | —           | 25       | —            | OOS Jul 2026                                         |
| SB26STCN-C000-4          | Dome      | 4Ω  | €36.45        | 10+            | 950    | 92      | 120   | 72          | 25       | 1,900        | ✓ — 120W; compact 72mm FP                            |
| AMT Mini-8               | AMT       | 8Ω  | €36.45        | 10+            | ~1,750 | 88      | 15    | 57          | AMT fold | ~3,500       | ~ stated lower limit 3.5kHz; super-tweeter role only |
| CF18N-4                  | Dome (CF) | 4Ω  | €36.95        | 6              | 1,100  | 90      | 40    | **58**      | 18       | 2,200        | ★ carbon fiber 18mm dome; FP=58mm (3rd smallest); Cutout=37mm; Depth=38mm |
| D27TG35-06               | Dome      | 6Ω  | €39.95        | 10+            | 900    | 91.8    | 15    | 104         | 25       | 1,800        | ✓ — 6Ω; large FP                                     |
| NE25VTS-04               | Dome      | 4Ω  | €39.95        | 10+            | 730    | 91.1    | 15    | 66.3        | 25       | 1,460        | ★ compact FP; similar to ND25FA; higher sens         |
| D2606/920000             | Dome      | 6Ω  | €39.95        | 10+            | 1,100  | 91.4    | 100   | —           | 25       | 2,200        | ✓ — Scan-Speak quality; 100W                         |
| DA25BG08-06              | Dome      | 6Ω  | €39.95        | 10+            | 710    | 91.6    | 15    | 104         | 25       | 1,420        | ★ Fs=710Hz; same FP class as DX25; 15W (OK at ref)  |
| SB21SDC-C000-4           | Ring Dome | 4Ω  | €39.95        | 1+7-Jul        | 720    | 91      | 40    | 92          | 21       | 1,440        | ★ ring dome; cheaper SB29 alt; 40W; Fs=720Hz         |
| NE19VTS-04               | Dome      | 4Ω  | €29.95        | exp 31-12-2026 | —      | —       | —     | —           | 19       | —            | OOS Dec 2026                                         |
| XT25TG30-04              | Ring Rad  | 4Ω  | £29.90 Falcon | pre-order SI   | 440    | 91.9    | 15    | 104         | 25       | 880          | ✓ (RR1–3) — lowest Fs; widest xover window           |
| DT-28N                   | Dome      | 8Ω  | €40.95        | 5              | 1,200  | ~92     | 50    | ~72         | 28       | 2,400        | ✓ (B11,B12) — compact wg; 50W                        |
| SB29SDAC-C000-4          | Ring Dome | 4Ω  | €44.95        | 10             | 600    | ~91     | ~30   | ~104        | 29       | 1,200        | ✓ (S3,RR6) — ring dome construction                  |
| Discovery D2604/830000   | Dome      | 4Ω  | €44.95        | 10+            | ~630   | 92      | 100   | 104.2       | 26       | ~1,260       | ✓ — 100W/240W; Cutout 75mm; Depth 25.4mm; SI URL confirmed |
| TW 6 (Markaudio)         | Dome      | 4Ω  | €44.95        | 8              | 1,700  | —       | —     | —           | 25       | 3,400        | ✓ (C4) — min xover above most mid beaming limits     |
| RST28F-4                 | Dome      | 4Ω  | €46.95        | 10+            | 710    | 93.5    | 80    | 104.8       | 28       | 1,420        | ✓ — 80W; very high sens; large FP                    |
| SEAS 27TFFNC/CG H1406-04 | Dome      | 4Ω  | €48.95        | 4              | 1,170  | 91      | 80    | 69.7×54oval | 26       | 2,340        | ★ 80W; oval 69.7×54mm FP; Depth 21.5mm; Cutout 46mm |
| XT25BG60-04              | Ring Rad  | 4Ω  | €49.95        | 10+            | 570    | 92.6    | 15    | 104.5       | 25       | 1,140        | ✓ — ring rad; huge 104.5mm FP concern                |
| SB26ADC-C000-4           | Dome (Al) | 4Ω  | €52.45        | 10+            | 680    | 90      | 120   | ~104        | 26       | 1,360        | ✓ — 120W; bright Al dome                             |

---

## Excluded — Wrong Application

| Model                                | Type                 | Reason                                          |
| ------------------------------------ | -------------------- | ----------------------------------------------- |
| PRT-8                                | Phenolic Ring        | OOS; compression-horn type                      |
| WG175Ph                              | Horn                 | OOS; horn-mount only                            |
| TW350Ti-4                            | Bullet (pair)        | OOS; bullet profile                             |
| D250TI-S/B                           | Compression          | OOS; horn-mount                                 |
| D270Ph-S                             | Compression          | OOS; horn-mount                                 |
| ST200                                | Horn Super Tweeter   | Above 5kHz only                                 |
| ST601-4 / ST603-4                    | Bullet (pairs)       | Bullet profile; unsuitable for flat baffle      |
| CD 78.26/245-8                       | Compression          | Horn-mount                                      |
| PRO Neo-8                            | Horn Super Tweeter   | Above 5kHz                                      |
| RT-10                                | Ribbon               | Low impedance; 2 in stock                       |
| CP-16 (Beyma)                        | Compression          | Horn-mount                                      |
| H2606/920000                         | Horn Dome            | Horn-mount                                      |
| TW500Ti-4                            | Super Tweeter (pair) | OOS; above 10kHz                                |
| GRS A25-2T                           | 2" Dome Midrange     | Midrange role, not tweeter                      |
| Swan DMB-A                           | 2" Dome Midrange     | Midrange role; 1 in stock                       |
| 13-1761S                             | Dome pair            | OOS                                             |
| RST28A-4                             | 1⅛" Dome             | OOS                                             |
| DC28F-8 / DC28FT-8 / DC28FS-8        | Dome                 | OOS                                             |
| D19TD-05                             | 3/4" Dome            | exp Sep 2026; small dome; high min-xover        |
| LP 85.25 / 98.25 / 111.25 / 53×58 TW | Dome variants        | Data limited; various OOS                       |
| DT-300                               | Dome                 | exp Sep 2026                                    |
| SB21SDCN-C000-4                      | 3/4" Dome            | exp Aug 2026                                    |
| ST601-4                              | Bullet pair          | 2 in stock                                      |
| SB26STAC-C000-4                      | Dome                 | exp Aug 2026                                    |
| SEAS 27TFFNC/G H1396-04              | Dome                 | exp Jul 2026                                    |
| ND25FN-4                             | Dome                 | No faceplate; cannot surface-mount              |
| OC25SC65-04                          | Dome                 | Faceplate-less twist-lock; cannot surface-mount |
| BC25TG15-04                          | Dome                 | 7W power rating — fatal at reference SPL        |

---

## Key Reference

- **Project tweeter crossover target:** 2,800 Hz HP (LR48)
- **Dome ≤19 mm preferred** for widest off-axis dispersion (kitchen 60°)
- **Min Xover** = 2 × Fs
- **Power needed at burst (101 dB):** P = 10^((101 − Sens) / 10) watts
- **FP OD drives centre spacing:** spacing = (mid_OD + tweet_OD) / 2

*Sources: SoundImports product pages (fetched June 2026), drivers.md entries, research/ datasheets*
