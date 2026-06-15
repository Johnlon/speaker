"""
Add price labels to all seller badges in solutions.html.
Maps each known seller URL to its price, then rewrites badge labels from
e.g. "Willys" → "Willys £20.58" and "SI" → "SI €25.95".
Badges that already contain a currency symbol are left unchanged (sourcing tab).
PDF/web badges are never modified.
"""
import re

# URL → price for every seller link that appears in the scenario tabs
url_prices = {
    # --- Willys-Hifi ---
    "https://willys-hifi.com/products/sb-acoustics-sb12pfcr25-4-paper-midwoofer":          "£20.58",
    "https://willys-hifi.com/products/sb-acoustics-sb12pacr25-4-mid-woofer":               "£23.76",
    "https://willys-hifi.com/products/sb-acoustics-sb12mnrx2-25-4-midrange":               "£48.10",
    "https://willys-hifi.com/products/dayton-audio-ds115-8-4-designer-series-woofer-8-ohm":"£32.00",
    "https://willys-hifi.com/products/dayton-audio-dsa90-8-3-aluminum-cone-woofer":        "£29.90",
    "https://willys-hifi.com/products/sb-acoustics-sb12pacr25-4-coax-coaxial-speaker":     "£52.53",
    "https://willys-hifi.com/products/scan-speak-discovery-r2604-833000-dual-ring-tweeter":"£46.00",
    "https://willys-hifi.com/products/sb-acoustics-sb21rdcn-c000-4-tweeter":               "£41.60",
    "https://willys-hifi.com/products/vifa-xt25tg30-04-tweeter":                           "£31.95",
    "https://willys-hifi.com/products/sb-acoustics-sb21sdc-c000-4-tweeter":                "£28.51",
    "https://willys-hifi.com/products/sb-acoustics-sb19st-c000-4-tweeter":                 "£15.20",
    "https://willys-hifi.com/products/sb-acoustics-sb29rdnc-c000-4-tweeter":               "£59.88",
    "https://willys-hifi.com/products/seas-prestige-27tdfc-h1189-06-tweeter":              "£55.00",
    "https://willys-hifi.com/products/scan-speak-discovery-d2604-830000-tweeter":          "£41.50",
    "https://willys-hifi.com/products/vifa-xt25sc40-04-tweeter":                           "£24.00",
    "https://willys-hifi.com/products/seas-prestige-27tffnc-cg-h1406-04-tweeter":         "£33.00",
    "https://willys-hifi.com/products/morel-mdt-22-tweeter":                               "£48.00",
    "https://willys-hifi.com/collections/dayton-audio-drive-units":                        "£17.50",
    "https://willys-hifi.com/products/vifa-xt25sc90-04-tweeter":                           "£19.52",
    "https://willys-hifi.com/products/sb-acoustics-sb26stcn-c000-4-tweeter":               "£29.40",
    "https://willys-hifi.com/products/monacor-dt-28n-neodymium-dome-tweeter":              "£32.50",

    # --- SoundImports ---
    "https://www.soundimports.eu/en/sb-acoustics-sb12pfcr25-4.html":                       "€25.95",
    "https://www.soundimports.eu/en/sb-acoustics-sb12pacr25-4.html":                       "€32.45",
    "https://www.soundimports.eu/en/sb-acoustics-sb12mnrx2-25-4.html":                     "€61.95",
    "https://www.soundimports.eu/en/dayton-audio-ds115-8.html":                            "€36.95",
    "https://www.soundimports.eu/en/dayton-audio-dsa90-8.html":                            "€34.95",
    "https://www.soundimports.eu/en/sb-acoustics-sb12pacr25-4-coax.html":                  "€68.45",
    "https://www.soundimports.eu/en/tymphany-sls-85s25cp04-04.html":                       "€24.95",
    "https://www.soundimports.eu/en/tang-band-w5-1138smf.html":                            "€54.95",
    "https://www.soundimports.eu/en/scan-speak-r2604-833000.html":                         "€62.45",
    "https://www.soundimports.eu/en/sb-acoustics-sb21rdcn-c000-4.html":                    "€59.95",
    "https://www.soundimports.eu/en/peerless-by-tymphany-xt25tg30-04.html":               "€49.95",
    "https://www.soundimports.eu/en/sb-acoustics-sb21sdc-c000-4.html":                     "€39.95",
    "https://www.soundimports.eu/en/sb-acoustics-sb19st-c000-4.html":                      "€21.45",
    "https://www.soundimports.eu/en/sb-acoustics-sb29rdnc-c000-4.html":                    "€78.95",
    "https://www.soundimports.eu/en/seas-27tdfc.html":                                     "€71.86",
    "https://www.soundimports.eu/en/scan-speak-d2604-830000.html":                         "€52.95",
    "https://www.soundimports.eu/en/peerless-by-tymphany-xt25sc40-04.html":               "€32.95",
    "https://www.soundimports.eu/en/seas-27tffnc-cg.html":                                 "€42.95",
    "https://www.soundimports.eu/en/morel-mdt-22.html":                                    "€63.95",
    "https://www.soundimports.eu/en/dayton-audio-nd25fa-4.html":                           "€21.45",
    "https://www.soundimports.eu/en/monacor-dt-28n.html":                                  "€40.95",
    "https://www.soundimports.eu/en/sb-acoustics-sb26stcn-c000-4.html":                    "€39.95",

    # --- Falcon Acoustics ---
    "https://www.falconacoustics.co.uk/scanspeak-r2604-833000-tweeter-discovery-range.html":    "£45.95",
    "https://www.falconacoustics.co.uk/peerless-vifa-xt25tg30-04-tweeter.html":                 "£29.90",
    "https://www.falconacoustics.co.uk/peerless-vifa-xt25sc90-04-tweeter-pair.html":            "£18.20",
    "https://www.falconacoustics.co.uk/sb-acoustics-sb19st-c000-4-19mm-tweeter.html":           "£14.30",
    # seas-27tdfc-prestige-tweeter.html is used for both H1189 (£56.92) and H1406 (£32.95) -
    # leave unpriced to avoid showing wrong amount

    # --- HiFi Collective ---
    "https://www.hificollective.co.uk/speakers/seas-27tdfc-tweeter-h1189.html":            "£56.92",
    "https://www.hificollective.co.uk/speakers/seas-h1406-27tffnc-cg-tweeter.html":       "£33.66",

    # --- Parts Express ---
    "https://www.parts-express.com/Tymphany-SLS-85S25CP04-04-3-Paper-Cone-Woofer-4-Ohm-264-1148": "$22.99",
    "https://www.parts-express.com/Tang-Band-W5-1138SMF-5-1-4-Paper-Cone-Subwoofer-Speaker-264-831": "$56.98",
}

SKIP_CLASSES = {"badge-pdf", "badge-web"}
CURRENCY = {"£", "€", "$"}

pattern = re.compile(
    r'<a href="([^"]+)" class="(btn-badge [^"]+)">([^<]+)</a>'
)

def replace_badge(m):
    href, css, label = m.group(1), m.group(2), m.group(3)
    # Never touch PDF or web badges
    if any(c in css for c in SKIP_CLASSES):
        return m.group(0)
    # Skip if label already contains a price
    if any(ch in label for ch in CURRENCY):
        return m.group(0)
    price = url_prices.get(href)
    if price:
        return f'<a href="{href}" class="{css}">{label} {price}</a>'
    return m.group(0)


filepath = "C:/Users/johnl/work/speaker/solutions.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

new_content = pattern.sub(replace_badge, content)

changed = sum(1 for a, b in zip(content.split("\n"), new_content.split("\n")) if a != b)
print(f"Lines changed: {changed}")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)

print("solutions.html updated — all seller badges now include prices.")
