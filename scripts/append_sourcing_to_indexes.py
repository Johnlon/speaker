import os

# Sourcing dataset for all recommended drivers
sourcing_db = {
    # Woofers & Midranges
    "SB Acoustics SB12PFCR25-4": {
        "SoundImports (EU)": ("€25.95", "https://www.soundimports.eu/en/sb-acoustics-sb12pfcr25-4.html"),
        "Willys-Hifi (UK)": ("£20.58", "https://willys-hifi.com/products/sb-acoustics-sb12pfcr25-4-paper-midwoofer"),
    },
    "SB Acoustics SB12PACR25-4": {
        "SoundImports (EU)": ("€32.45 (OOS)", "https://www.soundimports.eu/en/sb-acoustics-sb12pacr25-4.html"),
        "Willys-Hifi (UK)": ("£23.76", "https://willys-hifi.com/products/sb-acoustics-sb12pacr25-4-mid-woofer"),
    },
    "SB Acoustics SB12MNRX2-25-4": {
        "SoundImports (EU)": ("€61.95", "https://www.soundimports.eu/en/sb-acoustics-sb12mnrx2-25-4.html"),
        "Willys-Hifi (UK)": ("£48.10", "https://willys-hifi.com/products/sb-acoustics-sb12mnrx2-25-4-midrange"),
    },
    "Dayton Audio DS115-8": {
        "SoundImports (EU)": ("€36.95", "https://www.soundimports.eu/en/dayton-audio-ds115-8.html"),
        "Willys-Hifi (UK)": ("£32.00", "https://willys-hifi.com/products/dayton-audio-ds115-8-4-designer-series-woofer-8-ohm"),
        "Wilmslow Audio (UK)": ("(Contact for Price)", "https://wilmslowaudio.co.uk/dayton-audio-ds115-8-4-designer-series-woofer-speaker"),
    },
    "Dayton Audio DSA90-8": {
        "SoundImports (EU)": ("€34.95", "https://www.soundimports.eu/en/dayton-audio-dsa90-8.html"),
        "Willys-Hifi (UK)": ("£29.90", "https://willys-hifi.com/products/dayton-audio-dsa90-8-3-aluminum-cone-woofer"),
    },
    "SB Acoustics SB12PACR25-4-COAX": {
        "SoundImports (EU)": ("€68.45", "https://www.soundimports.eu/en/sb-acoustics-sb12pacr25-4-coax.html"),
        "Willys-Hifi (UK)": ("£52.53", "https://willys-hifi.com/products/sb-acoustics-sb12pacr25-4-coax-coaxial-speaker"),
    },
    "Tymphany SLS-85S25": {
        "SoundImports (EU)": ("€24.95", "https://www.soundimports.eu/en/tymphany-sls-85s25cp04-04.html"),
        "Parts Express (US)": ("$22.99", "https://www.parts-express.com/Tymphany-SLS-85S25CP04-04-3-Paper-Cone-Woofer-4-Ohm-264-1148"),
    },
    "Tang Band W5-1138SMF": {
        "SoundImports (EU)": ("€54.95", "https://www.soundimports.eu/en/tang-band-w5-1138smf.html"),
        "Parts Express (US)": ("$56.98", "https://www.parts-express.com/Tang-Band-W5-1138SMF-5-1-4-Paper-Cone-Subwoofer-Speaker-264-831"),
    },
    
    # Tweeters
    "Scan-Speak R2604/833000": {
        "SoundImports (EU)": ("€62.45", "https://www.soundimports.eu/en/scan-speak-r2604-833000.html"),
        "Willys-Hifi (UK)": ("£46.00", "https://willys-hifi.com/products/scan-speak-discovery-r2604-833000-dual-ring-tweeter"),
        "Falcon Acoustics (UK)": ("£45.95", "https://www.falconacoustics.co.uk/scanspeak-r2604-833000-tweeter-discovery-range.html"),
        "Wilmslow Audio (UK)": ("£63.29 (inc. VAT)", "https://www.wilmslowaudio.co.uk/scanspeak-discovery-r2604-833000"),
    },
    "SB Acoustics SB21RDCN": {
        "SoundImports (EU)": ("€59.95", "https://www.soundimports.eu/en/sb-acoustics-sb21rdcn-c000-4.html"),
        "Willys-Hifi (UK)": ("£45.60", "https://willys-hifi.com/products/sb-acoustics-sb21rdcn-c000-4-tweeter"),
    },
    "Peerless XT25TG30-04": {
        "SoundImports (EU)": ("€49.95", "https://www.soundimports.eu/en/peerless-by-tymphany-xt25tg30-04.html"),
        "Willys-Hifi (UK)": ("£31.95", "https://willys-hifi.com/products/vifa-xt25tg30-04-tweeter"),
        "Falcon Acoustics (UK)": ("£29.90", "https://www.falconacoustics.co.uk/peerless-vifa-xt25tg30-04-tweeter.html"),
    },
    "SB Acoustics SB21SDC": {
        "SoundImports (EU)": ("€39.95", "https://www.soundimports.eu/en/sb-acoustics-sb21sdc-c000-4.html"),
        "Willys-Hifi (UK)": ("£30.24", "https://willys-hifi.com/products/sb-acoustics-sb21sdc-c000-4-tweeter"),
    },
    "SB Acoustics SB19ST": {
        "SoundImports (EU)": ("€21.45", "https://www.soundimports.eu/en/sb-acoustics-sb19st-c000-4.html"),
        "Willys-Hifi (UK)": ("£15.20", "https://willys-hifi.com/products/sb-acoustics-sb19st-c000-4-tweeter"),
        "Falcon Acoustics (UK)": ("£14.30", "https://www.falconacoustics.co.uk/sb-acoustics-sb19st-c000-4-19mm-tweeter.html"),
    },
    "SB Acoustics SB29RDNC": {
        "SoundImports (EU)": ("€78.95", "https://www.soundimports.eu/en/sb-acoustics-sb29rdnc-c000-4.html"),
        "Willys-Hifi (UK)": ("£59.88", "https://willys-hifi.com/products/sb-acoustics-sb29rdnc-c000-4-tweeter"),
    },
    "SEAS 27TDFC H1189": {
        "SoundImports (EU)": ("€71.86", "https://www.soundimports.eu/en/seas-27tdfc.html"),
        "Willys-Hifi (UK)": ("£55.00", "https://willys-hifi.com/products/seas-prestige-27tdfc-h1189-06-tweeter"),
        "Falcon Acoustics (UK)": ("£56.92", "https://www.falconacoustics.co.uk/seas-27tdfc-prestige-tweeter.html"),
        "HiFi Collective (UK)": ("£56.92", "https://www.hificollective.co.uk/speakers/seas-27tdfc-tweeter-h1189.html"),
    },
    "Scan-Speak D2604/830000": {
        "SoundImports (EU)": ("€52.95", "https://www.soundimports.eu/en/scan-speak-d2604-830000.html"),
        "Willys-Hifi (UK)": ("£41.50", "https://willys-hifi.com/products/scan-speak-discovery-d2604-830000-tweeter"),
    },
    "Peerless XT25SC40-04": {
        "SoundImports (EU)": ("€32.95", "https://www.soundimports.eu/en/peerless-by-tymphany-xt25sc40-04.html"),
        "Willys-Hifi (UK)": ("£24.00", "https://willys-hifi.com/products/vifa-xt25sc40-04-tweeter"),
    },
    "SEAS 27TFFNC/CG H1406-04": {
        "SoundImports (EU)": ("€42.95", "https://www.soundimports.eu/en/seas-27tffnc-cg.html"),
        "Willys-Hifi (UK)": ("£33.00", "https://willys-hifi.com/products/seas-prestige-27tffnc-cg-h1406-04-tweeter"),
        "Falcon Acoustics (UK)": ("£32.95", "https://www.falconacoustics.co.uk/drive-units-1/seas-drive-units/seas-speakers-tweeters-drive-units.html"),
        "HiFi Collective (UK)": ("£33.66", "https://www.hificollective.co.uk/speakers/seas-h1406-27tffnc-cg-tweeter.html"),
    },
    "Morel MDT22T": {
        "SoundImports (EU)": ("€63.95", "https://www.soundimports.eu/en/morel-mdt-22.html"),
        "Willys-Hifi (UK)": ("£48.00", "https://willys-hifi.com/products/morel-mdt-22-tweeter"),
    },
    "Dayton Audio ND25FA-4": {
        "SoundImports (EU)": ("€21.45", "https://www.soundimports.eu/en/dayton-audio-nd25fa-4.html"),
        "Willys-Hifi (UK)": ("£17.50", "https://willys-hifi.com/collections/dayton-audio-drive-units"),
    },
    "Peerless XT25SC90-04": {
        "Willys-Hifi (UK)": ("£19.52", "https://willys-hifi.com/products/vifa-xt25sc90-04-tweeter"),
        "Falcon Acoustics (UK)": ("£18.20", "https://www.falconacoustics.co.uk/peerless-vifa-xt25sc90-04-tweeter-pair.html"),
    },
    "Monacor DT-28N": {
        "SoundImports (EU)": ("€40.95", "https://www.soundimports.eu/en/monacor-dt-28n.html"),
        "Willys-Hifi (UK)": ("£32.50", "https://willys-hifi.com/products/monacor-dt-28n-neodymium-dome-tweeter"),
    },
    "SB Acoustics SB26STCN-C000-4": {
        "SoundImports (EU)": ("€39.95", "https://www.soundimports.eu/en/sb-acoustics-sb26stcn-c000-4.html"),
        "Willys-Hifi (UK)": ("£29.40", "https://willys-hifi.com/products/sb-acoustics-sb26stcn-c000-4-tweeter"),
    }
}

def generate_sourcing_section(file_drivers):
    section = "\n---\n\n## Seller Purchase Links & Pricing Reference\n\nDirect links to purchase recommended drivers featured in this catalog:\n\n"
    for name in file_drivers:
        if name in sourcing_db:
            section += f"### {name}\n"
            for seller, (price, link) in sourcing_db[name].items():
                section += f"- **{seller}:** [{price}]({link})\n"
            section += "\n"
    return section

index_files = {
    "C:/Users/johnl/work/speaker/research/si_tweeter_index.md": [
        "Dayton Audio ND25FA-4", "SB Acoustics SB19ST", "Peerless XT25SC90-04", 
        "Peerless XT25SC40-04", "Peerless XT25TG30-04", "SB Acoustics SB26STCN-C000-4",
        "SB Acoustics SB21SDC", "SB Acoustics SB29RDNC", "SB Acoustics SB21RDCN", 
        "Morel MDT22T", "Scan-Speak R2604/833000", "SEAS 27TDFC H1189", "SEAS 27TFFNC/CG H1406-04"
    ],
    "C:/Users/johnl/work/speaker/research/si_woofer_index.md": [
        "SB Acoustics SB12PFCR25-4", "SB Acoustics SB12PACR25-4", "SB Acoustics SB12MNRX2-25-4",
        "Dayton Audio DS115-8", "Dayton Audio DSA90-8", "SB Acoustics SB12PACR25-4-COAX",
        "Tymphany SLS-85S25", "Tang Band W5-1138SMF"
    ],
    "C:/Users/johnl/work/speaker/research/willys_new_tweeters.md": [
        "SB Acoustics SB21RDCN", "Morel MDT22T", "Scan-Speak R2604/833000", "SB Acoustics SB26STCN-C000-4"
    ],
    "C:/Users/johnl/work/speaker/research/willys_new_mids.md": [
        "SB Acoustics SB12PFCR25-4", "SB Acoustics SB12PACR25-4", "SB Acoustics SB12MNRX2-25-4"
    ],
    "C:/Users/johnl/work/speaker/research/hfc_tweeter_index.md": [
        "SEAS 27TDFC H1189", "SEAS 27TFFNC/CG H1406-04", "Scan-Speak R2604/833000", "Morel MDT22T"
    ],
    "C:/Users/johnl/work/speaker/research/hfc_woofer_index.md": [
        "SB Acoustics SB12PFCR25-4", "SB Acoustics SB12MNRX2-25-4"
    ]
}

for filepath, drivers in index_files.items():
    if not os.path.exists(filepath):
        print(f"Skipping missing file: {filepath}")
        continue
    
    print(f"Appending sourcing section to {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Strip any existing Sourcing section
    if "## Seller Purchase Links & Pricing Reference" in content:
        content = content.split("## Seller Purchase Links & Pricing Reference")[0].rstrip()
    
    sourcing_section = generate_sourcing_section(drivers)
    new_content = content.rstrip() + "\n" + sourcing_section
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

print("Index files successfully updated with direct links to all sellers and prices.")
