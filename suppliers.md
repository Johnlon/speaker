# Supplier Research — Desktop Speaker Project

Researched June 2026. All URLs fetched via WebFetch.

---

## 1. SoundImports (soundimports.eu) — PRIMARY RECOMMENDED SUPPLIER

- **Website:** https://www.soundimports.eu/en/
- **Ships to UK:** Yes — EU-based (Netherlands), ships internationally including UK. Post-Brexit duties may apply.
- **Contact:** +31-85-0711860 | [email protected]
- **Catalogue size:** 228 dome tweeters, 134 mid-range woofers, 612 bass-mid woofers (as of June 2026)
- **Prices:** EUR. Current sale pricing shown with ~17% discounts; bulk (4+ units) adds a further 5%.
- **Stock info:** Most items show "10+ In stock" with "ordered now, shipped today" policy. Individual products show exact counts.
- **Technical support:** Claimed in-house technical support available.
- **Quality assessment:** Excellent range. Stocks all major Hi-Fi driver brands: SB Acoustics, Dayton Audio (Reference and standard lines), Scan-Speak, SEAS, Peerless by Tymphany, HiVi Swan, Morel, Monacor, PURIFI, Tang Band, Visaton, Fountek.
- **Key finds:** SB19ST-C000-4 (top tweeter candidate), DSA90-8 (top mid candidate), TCP115-8, DS115-8, HiVi B4N — all in stock.
- **Weakness — pagination bug:** The category listing at `/en/audio-components/tweeters/` always serves the same ~24 products regardless of page parameter, even with the correct `?hr-page={"page":N}` URL format. There are 432 tweeters across 18 pages but only the first ~24 are browsable via category. **Workaround: use targeted search (`/en/search?q=model`) to find specific drivers.** Drivers behind the pagination include XT25BG60-04, XT19TD00-04, and others. Note: XT25TG30-04 and XT25SC90-04 *were* on the first page and were missed in the original survey (not a pagination issue — a survey gap).

**Pages fetched:**
- https://www.soundimports.eu/en/audio-components/tweeters/dome-tweeter/?p=1 through p=10 (all returned same ~10–15 items)
- https://www.soundimports.eu/en/audio-components/woofers/mid-range-woofer/?p=1 through p=6
- https://www.soundimports.eu/en/audio-components/woofers/bass-mid-woofer/?p=1 through p=5
- Individual product pages for 25+ drivers (see drivers.md)

---

## 2. Thomann UK (thomann.co.uk)

- **Website:** https://www.thomann.co.uk/
- **Ships to UK:** Yes — major European music/audio retailer, established UK operation.
- **Note:** Redirects from thomann.de/gb/ to thomann.co.uk automatically.
- **Catalogue:** Broad but skewed towards professional/live sound and musical instrument amplification. Their "dome tweeter" and "midrange speaker driver" categories return primarily PA replacement components and branded replacement parts (JBL, EV, Yamaha, the box) rather than Hi-Fi DIY drivers.
- **Key finds:** None suitable — the tweeters listed were 44mm+ voice coil PA drivers, replacement parts, and branded units (£3–£21 range). No Hi-Fi dome tweeters with published T/S parameters found.
- **Assessment:** Not useful for this project. Thomann does not stock Hi-Fi DIY speaker drivers in meaningful quantities. Skip for this build.

**Pages fetched:**
- https://www.thomann.co.uk/dome_tweeter.html (redirected, loaded — PA/pro audio only)
- https://www.thomann.co.uk/midrange_speaker_drivers.html (404 — page not found)

---

## 3. Blue Aran (bluearan.co.uk)

- **Website:** https://www.bluearan.co.uk/
- **Ships to UK:** Yes — UK-based supplier.
- **Tagline:** "The UK's no.1 Loudspeaker Component Stockist"
- **Catalogue:** Heavy emphasis on professional/PA drivers. Stocks Beyma, Eminence, Lavoce, Peerless (OEM/pro versions). Tweeters listed are primarily professional compression drivers and PA-grade dome tweeters.
- **Dome tweeters found (with prices):**
  - Beyma T-25M 25mm 20W 4Ω — £92.03 (over budget)
  - Beyma T-25S 25mm 20W 4Ω — £85.79 (over budget)
  - Eminence SD28 25mm 20W 4Ω — £11.67 (specs unknown, likely PA grade)
  - Lavoce TN100.70 25mm 10W 8Ω, 90dB, Fs 1500 Hz — £6.57
  - Lavoce TN131.00 25mm 15W 8Ω, 92dB, Fs 1250 Hz — £10.09
  - Lavoce TN101.00 25mm 15W 8Ω, 92dB, Fs 1600 Hz — £9.09
  - Peerless OC25SC65 1" 4Ω 80W — £13.33
  - Peerless BC25SC55-04 "Slimline Tweeter" — £14.18
- **Key finding:** The Lavoce and Eminence tweeters are PA grade with unknown faceplate geometry and visual appearance. The Peerless units match models already researched via SoundImports. Product pages did not load properly (returned navigation frames with no product data).
- **Assessment:** Primarily professional/PA speaker supplier. Not well suited for Hi-Fi DIY drivers. Category pages consistently returned "No results" errors during research, suggesting site architecture issues or filter problems. Would need to contact directly for exact stock.
- **Contact attempt:** Category pages CATEGORY=TWEETERS and CATEGORY=DOME+TWEETERS returned "No results" filter errors.

**Pages fetched:**
- https://www.bluearan.co.uk/ (loaded — navigation structure only)
- https://www.bluearan.co.uk/index.php?category=TWEETERS (no results returned)
- https://www.bluearan.co.uk/index.php?category=DRIVERS (no results returned)
- https://www.bluearan.co.uk/index.php?category=DOME+TWEETERS (no results returned)
- https://www.bluearan.co.uk/index.php?search=dome+tweeter (loaded with results — see above)

---

## 4. Wilmslow Audio (wilmslowaudio.co.uk)

- **Website:** https://www.wilmslowaudio.co.uk/
- **Ships to UK:** Yes — UK-based, 50+ years in trade. Demonstration room available by appointment.
- **Contact:** 01455 286603 | sales@wilmslow-audio.co.uk
- **Catalogue:** Classic Hi-Fi DIY brands. **Does NOT stock SB Acoustics or SEAS** — so SB19ST-C000-4 (frontrunner tweeter) and DX25TG59-04 are not available here.
  - **Tweeters:** Monacor, Scanspeak, Vifa/Peerless, Morel, Fostex, Fountek (ribbons), Coles, Visaton, Dayton Audio
  - **Midrange:** Volt, Scanspeak, Morel
  - **Bass-mid/bass:** Monacor, Morel, Peerless, Scanspeak, Visaton, Volt, Vifa, Fountek, Dayton Audio
  - **Amplifiers:** Hypex Fusion, Monacor subwoofer modules

**Confirmed prices (June 2026, inc. VAT):**

| Driver | Category | Price | Notes |
|--------|----------|-------|-------|
| Vifa XT25TG-30-04 | Tweeter | **£42.60** | 104mm face — vs Willys-Hifi £31.95 (33% more expensive) |
| Vifa D27TG-35-06 | Tweeter | **£38.40** | 104mm face — vs Falcon £28.35, Willys £27.52 (£10+ more) |
| Scanspeak D2606/9200.00 | Tweeter | **£40.49** | Discovery — vs Falcon £29.35 (£11 more) |
| Scanspeak D2604/8330.00 | Tweeter | **£54.68** | Discovery |
| Scanspeak R2604/8320.00 | Tweeter | **£56.60** | Discovery ring radiator |
| Scanspeak D2905/9300.00 | Tweeter | **£138.91** | Classic — over budget |
| Scanspeak Illuminator/Revelator | Tweeter | £131–£507 | Way over budget |
| Fountek NeoCD 1.0 | Ribbon tweeter | **£100.80** | 100mm face — over budget but noted for future |
| Fountek NeoX 1.0 | Ribbon tweeter | **£124.80** | 98×70mm — over budget |
| Coles CE4001K | Super tweeter | **£78.00** | 7Ω — niche BBC monitor item, over budget |
| Coles CE4001G | Super tweeter | **£78.00** | 16Ω — niche, over budget |
| Morel CAT298 | Tweeter | **£81.05** | Cheapest Morel; 104mm — over budget |
| Morel Supreme/Elite | Tweeter | £157–£710 | Matched pairs — way over budget |
| Dayton Audio TCP115-4 | 4" mid (4Ω) | **£24.00** | In stock |
| Dayton Audio DS115-8 | 4" mid (8Ω) | **£50.40** | In stock — expensive vs SoundImports |
| Volt VM527 | 50mm dome mid | **£282.00** | Prestige — way over budget |

**Assessment:** Prices for Vifa/Peerless and Scanspeak tweeters are £10–15 more expensive than Falcon Acoustics or Willys-Hifi on every comparable model checked. No SB Acoustics or SEAS means none of the current shortlisted candidates (SB19ST-C000-4, DX25TG59-04, BC25SC06-04, NE19VTS-04) are stocked here. Dayton Audio DS115-8 at £50.40 is overpriced vs alternatives. **Only worth using for:** Fountek ribbons or Coles super tweeters if those become relevant, or as last-resort UK fallback if Falcon/Willys are out of stock on a Vifa/Scanspeak Discovery unit.

**Pages fetched (June 2026):**
- https://wilmslowaudio.co.uk/ — site structure, contact details, 50+ years trading note
- https://wilmslowaudio.co.uk/categories/speaker-drive-units — brand list by category
- https://wilmslowaudio.co.uk/treble-units — tweeter brand list (9 brands confirmed)
- https://wilmslowaudio.co.uk/treble-units/scanspeak — full 23-model Scanspeak tweeter listing
- https://wilmslowaudio.co.uk/treble-units/vifa — 2 Vifa tweeters with prices
- https://wilmslowaudio.co.uk/treble-units/morel — 14 Morel tweeters with prices
- https://wilmslowaudio.co.uk/treble-units/fountek — 6 Fountek ribbon tweeters with prices
- https://wilmslowaudio.co.uk/treble-units/coles — 2 Coles super tweeters with prices
- https://wilmslowaudio.co.uk/midrange-units — midrange brand list (Volt, Scanspeak, Morel)
- https://wilmslowaudio.co.uk/volt-vm527 — Volt VM527 50mm dome mid, £282 inc VAT
- https://wilmslowaudio.co.uk/bass-mid-bass-units/dayton-audio — 10 Dayton Audio drivers with prices

---

## 5. HiFi Collective (hificollective.co.uk)

- **Website:** https://www.hificollective.co.uk/
- **Ships to UK:** Yes — UK-based supplier.
- **Catalogue:** Premium Hi-Fi components. Brands include Audience, Audax, Audio Note, Aurum Cantus, Cube Audio, Dynaudio, Duelund, Fostex, Jantzen, Monacor, Morel, Mundorf (AMT), Peerless, Scanspeak, SEAS, Viawave (ribbon), Vifa, Jupiter, Volt.
- **Assessment:** Premium/audiophile-grade components. Likely above budget for this project. Driver pages returned 404 errors during research, suggesting significant URL structure change since last known crawl. Worth visiting directly if budget allows higher-spec drivers.
- **Key observation:** Their focus on Audio Note, Duelund, Cube Audio etc. suggests their price point is above the £75 combined budget for mid+tweeter.

**Pages fetched:**
- https://www.hificollective.co.uk/ (homepage navigation loaded)
- https://www.hificollective.co.uk/speaker-drivers/ (404)
- https://www.hificollective.co.uk/speaker-drivers/tweeters/ (404)
- https://www.hificollective.co.uk/speaker-drivers/midrange/ (404)
- https://www.hificollective.co.uk/components/loudspeaker-drive-units/ (404)

---

## 6. Falcon Acoustics (falconacoustics.co.uk) — RECOMMENDED UK SECONDARY

- **Website:** https://www.falconacoustics.co.uk/
- **Ships to UK:** Yes — UK-based (Oxford, England). No Brexit import hassle. Also ships internationally.
- **Catalogue:** Specialist Hi-Fi driver retailer. UK sole distributor for SEAS. Stocks SB Acoustics (incl. Satori), Scanspeak, Peerless/Vifa, Morel, Audax, Fountek ribbon tweeters, Coles. BBC LS3/5a focus but carries a wide general range.
- **Pricing:** Very competitive on Peerless/Vifa and SB Acoustics standard range. Satori and premium Scanspeak are above budget.
- **Assessment:** Excellent UK source for tweeters already in our candidate list. Confirmed competitive pricing below SoundImports (EU) on several key drivers. Fully recommended as secondary UK supplier.

**Confirmed stock and pricing (June 2026):**

| Driver | Role | Price | Stock | Notes |
|--------|------|-------|-------|-------|
| SB19ST-C000-4 | Tweeter (frontrunner) | **£14.30** | In stock | Cheaper than SoundImports (€21.45≈£18) |
| DX25TG59-04 | Tweeter candidate | **£20.85** | In stock | UK stock confirmed; Fs 622 Hz, silk dome |
| D27TG-35-06 | Tweeter candidate | **£28.35** | In stock | 104mm face, 6Ω, silk dome, Fs 728 Hz |
| Scanspeak D2606/920000 | Tweeter candidate | **£29.35** | In stock | Consistent with Wilmslow price |
| XT25SC90-04 | Tweeter — ring radiator | **£18.20** | In stock | See note below |
| SB26ADC-C000-4 | Tweeter | £32.95 | **Out of stock** | |
| Peerless NE85W-04 | Mid (full range, 2.5") | £31.40 | In stock | Fs 105 Hz — marginal at 150 Hz xover |
| Peerless NE95W-04 | Mid (full range, 3") | £43.70 | In stock | Fs 103 Hz — marginal at 150 Hz xover |
| SEAS MCA12RC/P H1186-04 | Mid (4.7", 4Ω) | £40.55 | In stock | Prestige range — unconfirmed visual |

**XT25SC90-04 note:** Ring radiator design (not fabric dome). Fs 825 Hz (min xover 1,650 Hz), 90.1 dB, 100W, 4Ω, ~90mm face. Excellent off-axis characteristics typical of ring radiators. **Visual check needed** — ring radiators have a distinctive annular appearance; face colour unknown (may be silver). Only consider if visual is acceptable.

**Category URLs that work (use /drive-units-1/ prefix):**
- https://www.falconacoustics.co.uk/drive-units-1/sb-acoustics/sb-acoustics-tweeters.html
- https://www.falconacoustics.co.uk/drive-units-1/peerless-drive-units/peerless-tweeters-drive-units.html
- https://www.falconacoustics.co.uk/drive-units-1/seas-drive-units/seas-speakers-tweeters-drive-units.html
- https://www.falconacoustics.co.uk/drive-units-1/scanspeak-speakers-drive-units/scanspeak-tweeters-drive-units.html
- https://www.falconacoustics.co.uk/drive-units-1/peerless-drive-units/peerless-midwoofers-midranges-drive-units.html

---

## 7. Axiomedia (axiomedia.it)

- **Website:** https://www.axiomedia.it/
- **Ships to UK:** **Unknown** — no explicit international shipping information found. Italy-based (Villasanta, MB). Post-Brexit shipping from Italy to UK may incur customs/duties.
- **Catalogue:** Italian professional audio retailer specialising in Beyma drivers (PA/pro audio). Carries planar tweeters (€476–€548), large subwoofers (18"–21"), and midwoofers (10"+). No Hi-Fi dome tweeters or 3"–5" midranges visible.
- **Assessment:** Not suitable for this project. Pro audio/PA orientation, high prices, uncertain UK shipping, and no visible Hi-Fi DIY drivers in the product range. Skip.

**Pages fetched:**
- https://www.axiomedia.it/ (homepage loaded — PA/pro audio confirmed)

---

## 8. Parts Express (parts-express.com)

- **Website:** https://www.parts-express.com/
- **Ships to UK:** **Yes** — confirmed international shipping. UPS and DHL available. Note: shipping charges at checkout do NOT include UK customs duties, taxes, or broker fees. For orders over ~$135 USD (roughly £105 at current rates), HMRC VAT and potentially duty will be charged on arrival.
- **Practical assessment for this project:** USD pricing plus international shipping (typically $25–60 for small driver orders) plus UK customs (20% VAT + potential 3.7% import duty on speakers from USA) makes Parts Express expensive vs EU suppliers. On a €50 total spend from SoundImports, EU-to-UK VAT situation is simpler and cheaper.
- **Catalogue:** Excellent range — Dayton Audio Reference series, GRS, Goldwood, CSS, and others. However, their category pages (https://www.parts-express.com/cat/tweeters/29 and /cat/midrange-speakers/30) returned empty responses and 404s during fetching.
- **Key note:** The Dayton Audio drivers available at SoundImports (DSA90-8, TCP115-8, DS115-8, ND25FA-4 etc.) are the same units sold by Parts Express. Sourcing from SoundImports (EU-based) is likely lower total cost for UK buyers given post-Brexit shipping costs from USA.
- **Assessment:** Not recommended as primary source for this UK project due to shipping cost overhead and customs complexity. Use only if SoundImports is out of stock on a needed item.

**Pages fetched:**
- https://www.parts-express.com/ (homepage — confirms international shipping)
- https://www.parts-express.com/faq#Shipping (confirms UK shipping, no UK-specific cost details)
- https://www.parts-express.com/cat/tweeters/29 (empty response)
- https://www.parts-express.com/cat/midrange-speakers/30 (404)

---

## 9. Willys-Hifi (willys-hifi.com) — RECOMMENDED UK SECONDARY

- **Website:** https://willys-hifi.com/
- **Ships to UK:** Yes — UK-based (Southend-on-Sea area). Family business, 40+ years in trade.
- **Phone:** +44 1702 523999
- **Catalogue:** Wide Hi-Fi DIY range from Accuton, Audax, Dayton Audio, Fountek, Hiquphon, Monacor, Morel, Peerless/Vifa, SB Acoustics, Scanspeak. Also crossover components (capacitors, inductors, resistors) and cabinet parts. Estimated 2,000+ drive units in UK stock.
- **Assessment:** Excellent UK primary alternative to Falcon Acoustics. Stronger range than Falcon on Morel and Dayton Audio lines. Competitive pricing — often below SoundImports on key Peerless/Vifa lines.
- **Shipping:** UK domestic only (international not confirmed on homepage).

**Confirmed stock and pricing (June 2026):**

| Driver | Role | Willys £ | SI equiv. | Notes |
|--------|------|----------|-----------|-------|
| NE19VTS-04 | Tweeter | **£25.20** | €29.95 OOS Dec 2026 | In stock at Willys; SI OOS |
| SB12PACR25-4 | Mid | **£23.76** | €32.45 OOS Nov 2026 | In stock at Willys; £9 below SI; SI OOS |
| DX25TG59-04 | Tweeter | **£18.44** | €32.95 (≈£28) | £10 below SI |
| BC25SC06-04 | Tweeter | **£16.78** | €24.95 (≈£21) | £4 below SI |
| XT25SC90-04 | Tweeter | **£19.52** | — | Similar to Falcon £18.20 |
| XT25TG30-04 | Tweeter | **£31.95** | €49.95 (≈£43) | Falcon £29.90 is cheaper; Willys middle option |
| D27TG-35-06 | Tweeter | **£27.52** | €39.95 (≈£34) | Slightly above Falcon £28.35 |
| BC25SC55-04 | Tweeter | **£16.65** | €? SI | Truncated FP, 100W, Fs 1,400 Hz |
| H26TG45-06 | Tweeter | **£31.80** | — | Waveguide design; 96 dB, 100W |
| SB29SDNC-C000-4 | Tweeter | **£56.64** | — | 72mm FP, 95.5 dB, 80W; cloth dome |
| Morel MDT12 | Tweeter | **£39.50** | €? SI | 54mm FP, 80W, 19mm depth |
| SB12MNRX2-25-4 | Mid | **£48.10** | €61.95 (≈£53) | £5 below SI |

**Category URLs:**
- https://willys-hifi.com/collections/vifa-peerless-tweeters
- https://willys-hifi.com/collections/dome-tweeters
- https://willys-hifi.com/collections/midrange-speakers
- https://willys-hifi.com/collections/sb-acoustics-drive-units-all
- https://willys-hifi.com/collections/dayton-audio-drive-units
- https://willys-hifi.com/collections/new-arrivals

---

## Summary Table

| Supplier | Ships UK | Budget-friendly | Hi-Fi DIY range | Recommended |
|----------|----------|-----------------|-----------------|-------------|
| SoundImports (EU) | Yes | Yes (EUR, sale pricing) | Excellent | **PRIMARY** |
| Wilmslow Audio (UK) | Yes (domestic) | No — prices 15–33% above Falcon/Willys on same drivers | Moderate (no SB Acoustics/SEAS) | Last resort UK fallback only |
| Blue Aran (UK) | Yes (domestic) | Yes (PA-grade) | Poor (PA focus) | Not for this project |
| HiFi Collective (UK) | Yes (domestic) | No (premium) | Very good | Over budget |
| Falcon Acoustics (UK) | Yes (domestic) | Yes (competitive on Peerless/SB Acoustics) | Very good | **SECONDARY — use for UK orders** |
| Willys-Hifi (UK) | Yes (domestic) | Yes (often below SI on Peerless/Vifa) | Excellent | **SECONDARY — strong on Morel, Dayton, Peerless** |
| Thomann UK | Yes | N/A | Poor (PA/musical instruments) | No |
| Parts Express (USA) | Yes (international) | No (shipping+customs overhead) | Very good | Last resort only |
| Axiomedia (Italy) | Unknown | No (PA/expensive) | Poor (PA focus) | No |

---

## Reference Resources

Speaker driver selection guides bookmarked during research (June 2026):

| Resource | URL |
|----------|-----|
| Parts Express — Woofer Selection Guide | https://www.parts-express.com/woofer-selection-guide |
| Parts Express — Tweeter Selection Guide | https://www.parts-express.com/which-tweeter-is-right-for-you |
| Alibaba — Speaker Driver Buyer Guide | https://electronics.alibaba.com/buyingguides/speaker-driver-guide-how-to-choose-right |
| YouTube — Speaker Driver Video Guide | https://www.youtube.com/watch?v=ul8NJNPpM60 |
