import re

# Exact mappings for replacement in solutions.md and solutions.html
replacements = [
    # SB12PFCR25-4
    ("https://willys-hifi.com/collections/sb-acoustics-drive-units-all",
     "https://willys-hifi.com/products/sb-acoustics-sb12pfcr25-4-paper-midwoofer"),
    
    # Scan-Speak R2604/833000 Falcon
    ("https://www.falconacoustics.co.uk/drive-units-1/scanspeak-speakers-drive-units/scanspeak-tweeters-drive-units.html",
     "https://www.falconacoustics.co.uk/scanspeak-r2604-833000-tweeter-discovery-range.html"),
    
    # Peerless XT25TG30-04 Falcon
    ("https://www.falconacoustics.co.uk/drive-units-1/peerless-drive-units/peerless-tweeters-drive-units.html",
     "https://www.falconacoustics.co.uk/peerless-vifa-xt25tg30-04-tweeter.html"),
    
    # SB Acoustics SB19ST Falcon
    ("https://www.falconacoustics.co.uk/drive-units-1/sb-acoustics/sb-acoustics-tweeters.html",
     "https://www.falconacoustics.co.uk/sb-acoustics-sb19st-c000-4-19mm-tweeter.html"),
     
    # SEAS 27TDFC H1189 Falcon
    ("https://www.falconacoustics.co.uk/drive-units-1/seas-drive-units/seas-speakers-tweeters-drive-units.html",
     "https://www.falconacoustics.co.uk/seas-27tdfc-prestige-tweeter.html"),
     
    # Peerless XT25SC90-04 Falcon (often generic or wrong link)
    ("https://www.falconacoustics.co.uk/drive-units-1/peerless-drive-units/peerless-tweeters-drive-units.html",
     "https://www.falconacoustics.co.uk/peerless-vifa-xt25sc90-04-tweeter-pair.html"),
]

def run_update(filepath):
    print(f"Updating report links in: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Perform the straightforward replacements
    for old_url, new_url in replacements:
        content = content.replace(old_url, new_url)
        
    # Let's fix specific occurrences that might have been missed or had specific surrounding text
    
    # 1. H1189 Falcon link in solutions.md:
    content = content.replace(
        "([Willys](https://willys-hifi.com/products/seas-prestige-27tdfc-h1189-06-tweeter) | [Falcon](https://www.falconacoustics.co.uk/seas-27tdfc-prestige-tweeter.html) | [SI](https://www.soundimports.eu/en/seas-27tdfc.html))",
        "([Willys](https://willys-hifi.com/products/seas-prestige-27tdfc-h1189-06-tweeter) | [Falcon](https://www.falconacoustics.co.uk/seas-27tdfc-prestige-tweeter.html) | [HFC](https://www.hificollective.co.uk/speakers/seas-27tdfc-tweeter-h1189.html) | [SI](https://www.soundimports.eu/en/seas-27tdfc.html))"
    )
    
    # 2. H1189 in solutions.html: add HiFi Collective badge/link
    content = content.replace(
        '<a href="https://willys-hifi.com/products/seas-prestige-27tdfc-h1189-06-tweeter" class="btn-badge badge-willys">Willys</a> <a href="https://www.falconacoustics.co.uk/seas-27tdfc-prestige-tweeter.html" class="btn-badge badge-falcon">Falcon</a> <a href="https://www.soundimports.eu/en/seas-27tdfc.html" class="btn-badge badge-si">SI</a>',
        '<a href="https://willys-hifi.com/products/seas-prestige-27tdfc-h1189-06-tweeter" class="btn-badge badge-willys">Willys</a> <a href="https://www.falconacoustics.co.uk/seas-27tdfc-prestige-tweeter.html" class="btn-badge badge-falcon">Falcon</a> <a href="https://www.hificollective.co.uk/speakers/seas-27tdfc-tweeter-h1189.html" class="btn-badge badge-hfc">HFC</a> <a href="https://www.soundimports.eu/en/seas-27tdfc.html" class="btn-badge badge-si">SI</a>'
    )
    
    content = content.replace(
        '<a href="https://willys-hifi.com/products/seas-prestige-27tdfc-h1189-06-tweeter" class="btn-badge badge-willys">Buy Willys</a> <a href="https://www.falconacoustics.co.uk/seas-27tdfc-prestige-tweeter.html" class="btn-badge badge-falcon">Buy Falcon</a> <a href="https://www.soundimports.eu/en/seas-27tdfc.html" class="btn-badge badge-si">Buy SI</a>',
        '<a href="https://willys-hifi.com/products/seas-prestige-27tdfc-h1189-06-tweeter" class="btn-badge badge-willys">Buy Willys</a> <a href="https://www.falconacoustics.co.uk/seas-27tdfc-prestige-tweeter.html" class="btn-badge badge-falcon">Buy Falcon</a> <a href="https://www.hificollective.co.uk/speakers/seas-27tdfc-tweeter-h1189.html" class="btn-badge badge-hfc">Buy HFC</a> <a href="https://www.soundimports.eu/en/seas-27tdfc.html" class="btn-badge badge-si">Buy SI</a>'
    )
    
    # 3. SEAS 27TFFNC/CG H1406-04 in solutions.md:
    content = content.replace(
        "([Willys](https://willys-hifi.com/products/seas-prestige-27tffnc-cg-h1406-04-tweeter) | [Falcon](https://www.falconacoustics.co.uk/drive-units-1/seas-drive-units/seas-speakers-tweeters-drive-units.html) | [SI](https://www.soundimports.eu/en/seas-27tffnc-cg.html))",
        "([Willys](https://willys-hifi.com/products/seas-prestige-27tffnc-cg-h1406-04-tweeter) | [HFC](https://www.hificollective.co.uk/speakers/seas-h1406-27tffnc-cg-tweeter.html) | [SI](https://www.soundimports.eu/en/seas-27tffnc-cg.html))"
    )
    
    # 4. SEAS 27TFFNC/CG H1406-04 in solutions.html:
    content = content.replace(
        '<a href="https://willys-hifi.com/products/seas-prestige-27tffnc-cg-h1406-04-tweeter" class="btn-badge badge-willys">Willys</a> <a href="https://www.falconacoustics.co.uk/drive-units-1/seas-drive-units/seas-speakers-tweeters-drive-units.html" class="btn-badge badge-falcon">Falcon</a> <a href="https://www.soundimports.eu/en/seas-27tffnc-cg.html" class="btn-badge badge-si">SI</a>',
        '<a href="https://willys-hifi.com/products/seas-prestige-27tffnc-cg-h1406-04-tweeter" class="btn-badge badge-willys">Willys</a> <a href="https://www.hificollective.co.uk/speakers/seas-h1406-27tffnc-cg-tweeter.html" class="btn-badge badge-hfc">HFC</a> <a href="https://www.soundimports.eu/en/seas-27tffnc-cg.html" class="btn-badge badge-si">SI</a>'
    )
    
    content = content.replace(
        '<a href="https://willys-hifi.com/products/seas-prestige-27tffnc-cg-h1406-04-tweeter" class="btn-badge badge-willys">Buy Willys</a> <a href="https://www.falconacoustics.co.uk/drive-units-1/seas-drive-units/seas-speakers-tweeters-drive-units.html" class="btn-badge badge-falcon">Buy Falcon</a> <a href="https://www.soundimports.eu/en/seas-27tffnc-cg.html" class="btn-badge badge-si">Buy SI</a>',
        '<a href="https://willys-hifi.com/products/seas-prestige-27tffnc-cg-h1406-04-tweeter" class="btn-badge badge-willys">Buy Willys</a> <a href="https://www.hificollective.co.uk/speakers/seas-h1406-27tffnc-cg-tweeter.html" class="btn-badge badge-hfc">Buy HFC</a> <a href="https://www.soundimports.eu/en/seas-27tffnc-cg.html" class="btn-badge badge-si">Buy SI</a>'
    )

    # 5. Fix XT25SC90-04 Falcon link mismatch (pointing to XT25TG30 on Falcon)
    content = content.replace(
        "https://www.falconacoustics.co.uk/peerless-vifa-xt25tg30-04-tweeter.html",
        "https://www.falconacoustics.co.uk/peerless-vifa-xt25sc90-04-tweeter-pair.html"
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

run_update("C:/Users/johnl/work/speaker/solutions.md")
run_update("C:/Users/johnl/work/speaker/solutions.html")
print("Report links successfully updated.")
