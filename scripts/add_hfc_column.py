# Let's read and parse solutions.html to add the HiFi Collective column and row cells.
filepath = "C:/Users/johnl/work/speaker/solutions.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Table Header
old_header = """                <th>Model</th>
                <th>Datasheet</th>
                <th>SoundImports (EU)</th>
                <th>Willys-Hifi (UK)</th>
                <th>Falcon Acoustics (UK)</th>"""

new_header = """                <th>Model</th>
                <th>Datasheet</th>
                <th>SoundImports (EU)</th>
                <th>Willys-Hifi (UK)</th>
                <th>Falcon Acoustics (UK)</th>
                <th>HiFi Collective (UK)</th>"""

content = content.replace(old_header, new_header)

# Replace Tweeter Rows to include the 6th column cell (HiFi Collective)
rows_replacements = [
    # Scan-Speak R2604/833000
    ("""                <td style="font-weight: bold; color: white;">Scan-Speak R2604/833000</td>
                <td><a href="research/scanspeak_r2604-833000.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/scan-speak-r2604-833000.html" class="btn-badge badge-si">€62.45</a></td>
                <td><a href="https://willys-hifi.com/products/scan-speak-discovery-r2604-833000-dual-ring-tweeter" class="btn-badge badge-willys">£46.00</a></td>
                <td><a href="https://www.falconacoustics.co.uk/scanspeak-r2604-833000-tweeter-discovery-range.html" class="btn-badge badge-falcon">£45.95</a></td>""",
     """                <td style="font-weight: bold; color: white;">Scan-Speak R2604/833000</td>
                <td><a href="research/scanspeak_r2604-833000.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/scan-speak-r2604-833000.html" class="btn-badge badge-si">€62.45</a></td>
                <td><a href="https://willys-hifi.com/products/scan-speak-discovery-r2604-833000-dual-ring-tweeter" class="btn-badge badge-willys">£46.00</a></td>
                <td><a href="https://www.falconacoustics.co.uk/scanspeak-r2604-833000-tweeter-discovery-range.html" class="btn-badge badge-falcon">£45.95</a></td>
                <td>—</td>"""),

    # SB Acoustics SB21RDCN
    ("""                <td style="font-weight: bold; color: white;">SB Acoustics SB21RDCN</td>
                <td><a href="research/sb_acoustics_sb21rdcn-c000-4.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/sb-acoustics-sb21rdcn-c000-4.html" class="btn-badge badge-si">€59.95</a></td>
                <td><a href="https://willys-hifi.com/products/sb-acoustics-sb21rdcn-c000-4-tweeter" class="btn-badge badge-willys">£45.60</a></td>
                <td>—</td>""",
     """                <td style="font-weight: bold; color: white;">SB Acoustics SB21RDCN</td>
                <td><a href="research/sb_acoustics_sb21rdcn-c000-4.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/sb-acoustics-sb21rdcn-c000-4.html" class="btn-badge badge-si">€59.95</a></td>
                <td><a href="https://willys-hifi.com/products/sb-acoustics-sb21rdcn-c000-4-tweeter" class="btn-badge badge-willys">£45.60</a></td>
                <td>—</td>
                <td>—</td>"""),

    # Peerless XT25TG30-04
    ("""                <td style="font-weight: bold; color: white;">Peerless XT25TG30-04</td>
                <td><a href="research/peerless_xt25tg30-04.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/peerless-by-tymphany-xt25tg30-04.html" class="btn-badge badge-si">€49.95</a></td>
                <td><a href="https://willys-hifi.com/products/vifa-xt25tg30-04-tweeter" class="btn-badge badge-willys">£31.95</a></td>
                <td><a href="https://www.falconacoustics.co.uk/peerless-vifa-xt25sc90-04-tweeter-pair.html" class="btn-badge badge-falcon">£29.90</a></td>""",
     """                <td style="font-weight: bold; color: white;">Peerless XT25TG30-04</td>
                <td><a href="research/peerless_xt25tg30-04.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/peerless-by-tymphany-xt25tg30-04.html" class="btn-badge badge-si">€49.95</a></td>
                <td><a href="https://willys-hifi.com/products/vifa-xt25tg30-04-tweeter" class="btn-badge badge-willys">£31.95</a></td>
                <td><a href="https://www.falconacoustics.co.uk/peerless-vifa-xt25sc90-04-tweeter-pair.html" class="btn-badge badge-falcon">£29.90</a></td>
                <td>—</td>"""),

    # SB Acoustics SB21SDC
    ("""                <td style="font-weight: bold; color: white;">SB Acoustics SB21SDC</td>
                <td><a href="research/sb_acoustics_sb21sdc-c000-4.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/sb-acoustics-sb21sdc-c000-4.html" class="btn-badge badge-si">€39.95</a></td>
                <td><a href="https://willys-hifi.com/products/sb-acoustics-sb21sdc-c000-4-tweeter" class="btn-badge badge-willys">£30.24</a></td>
                <td>—</td>""",
     """                <td style="font-weight: bold; color: white;">SB Acoustics SB21SDC</td>
                <td><a href="research/sb_acoustics_sb21sdc-c000-4.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/sb-acoustics-sb21sdc-c000-4.html" class="btn-badge badge-si">€39.95</a></td>
                <td><a href="https://willys-hifi.com/products/sb-acoustics-sb21sdc-c000-4-tweeter" class="btn-badge badge-willys">£30.24</a></td>
                <td>—</td>
                <td>—</td>"""),

    # SB Acoustics SB19ST
    ("""                <td style="font-weight: bold; color: white;">SB Acoustics SB19ST</td>
                <td><a href="research/sb_acoustics_sb19st-c000-4.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/sb-acoustics-sb19st-c000-4.html" class="btn-badge badge-si">€21.45</a></td>
                <td><a href="https://willys-hifi.com/products/sb-acoustics-sb19st-c000-4-tweeter" class="btn-badge badge-willys">£15.20</a></td>
                <td><a href="https://www.falconacoustics.co.uk/sb-acoustics-sb19st-c000-4-19mm-tweeter.html" class="btn-badge badge-falcon">£14.30</a></td>""",
     """                <td style="font-weight: bold; color: white;">SB Acoustics SB19ST</td>
                <td><a href="research/sb_acoustics_sb19st-c000-4.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/sb-acoustics-sb19st-c000-4.html" class="btn-badge badge-si">€21.45</a></td>
                <td><a href="https://willys-hifi.com/products/sb-acoustics-sb19st-c000-4-tweeter" class="btn-badge badge-willys">£15.20</a></td>
                <td><a href="https://www.falconacoustics.co.uk/sb-acoustics-sb19st-c000-4-19mm-tweeter.html" class="btn-badge badge-falcon">£14.30</a></td>
                <td>—</td>"""),

    # SB Acoustics SB29RDNC
    ("""                <td style="font-weight: bold; color: white;">SB Acoustics SB29RDNC</td>
                <td><a href="research/sb_acoustics_sb29rdnc-c000-4.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/sb-acoustics-sb29rdnc-c000-4.html" class="btn-badge badge-si">€78.95</a></td>
                <td><a href="https://willys-hifi.com/products/sb-acoustics-sb29rdnc-c000-4-tweeter" class="btn-badge badge-willys">£59.88</a></td>
                <td>—</td>""",
     """                <td style="font-weight: bold; color: white;">SB Acoustics SB29RDNC</td>
                <td><a href="research/sb_acoustics_sb29rdnc-c000-4.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/sb-acoustics-sb29rdnc-c000-4.html" class="btn-badge badge-si">€78.95</a></td>
                <td><a href="https://willys-hifi.com/products/sb-acoustics-sb29rdnc-c000-4-tweeter" class="btn-badge badge-willys">£59.88</a></td>
                <td>—</td>
                <td>—</td>"""),

    # SEAS 27TDFC H1189
    ("""                <td style="font-weight: bold; color: white;">SEAS 27TDFC H1189</td>
                <td><a href="research/seas_27tdfc_h1189.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/seas-27tdfc.html" class="btn-badge badge-si">€71.86</a></td>
                <td><a href="https://willys-hifi.com/products/seas-prestige-27tdfc-h1189-06-tweeter" class="btn-badge badge-willys">£55.00</a></td>
                <td><a href="https://www.falconacoustics.co.uk/seas-27tdfc-prestige-tweeter.html" class="btn-badge badge-falcon">£56.92</a></td>""",
     """                <td style="font-weight: bold; color: white;">SEAS 27TDFC H1189</td>
                <td><a href="research/seas_27tdfc_h1189.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/seas-27tdfc.html" class="btn-badge badge-si">€71.86</a></td>
                <td><a href="https://willys-hifi.com/products/seas-prestige-27tdfc-h1189-06-tweeter" class="btn-badge badge-willys">£55.00</a></td>
                <td><a href="https://www.falconacoustics.co.uk/seas-27tdfc-prestige-tweeter.html" class="btn-badge badge-falcon">£56.92</a></td>
                <td><a href="https://www.hificollective.co.uk/speakers/seas-27tdfc-tweeter-h1189.html" class="btn-badge badge-hfc">£56.92</a></td>"""),

    # Scan-Speak D2604/830000
    ("""                <td style="font-weight: bold; color: white;">Scan-Speak D2604/830000</td>
                <td><a href="research/scanspeak_d2604-830000.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/scan-speak-d2604-830000.html" class="btn-badge badge-si">€52.95</a></td>
                <td><a href="https://willys-hifi.com/products/scan-speak-discovery-d2604-830000-tweeter" class="btn-badge badge-willys">£41.50</a></td>
                <td>—</td>""",
     """                <td style="font-weight: bold; color: white;">Scan-Speak D2604/830000</td>
                <td><a href="research/scanspeak_d2604-830000.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/scan-speak-d2604-830000.html" class="btn-badge badge-si">€52.95</a></td>
                <td><a href="https://willys-hifi.com/products/scan-speak-discovery-d2604-830000-tweeter" class="btn-badge badge-willys">£41.50</a></td>
                <td>—</td>
                <td>—</td>"""),

    # Peerless XT25SC40-04
    ("""                <td style="font-weight: bold; color: white;">Peerless XT25SC40-04</td>
                <td><a href="research/peerless_xt25sc40-04.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/peerless-by-tymphany-xt25sc40-04.html" class="btn-badge badge-si">€32.95</a></td>
                <td><a href="https://willys-hifi.com/products/vifa-xt25sc40-04-tweeter" class="btn-badge badge-willys">£24.00</a></td>
                <td>—</td>""",
     """                <td style="font-weight: bold; color: white;">Peerless XT25SC40-04</td>
                <td><a href="research/peerless_xt25sc40-04.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/peerless-by-tymphany-xt25sc40-04.html" class="btn-badge badge-si">€32.95</a></td>
                <td><a href="https://willys-hifi.com/products/vifa-xt25sc40-04-tweeter" class="btn-badge badge-willys">£24.00</a></td>
                <td>—</td>
                <td>—</td>"""),

    # SEAS 27TFFNC/CG H1406-04
    ("""                <td style="font-weight: bold; color: white;">SEAS 27TFFNC/CG H1406-04</td>
                <td><a href="research/seas_h1406-04.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/seas-27tffnc-cg.html" class="btn-badge badge-si">€42.95</a></td>
                <td><a href="https://willys-hifi.com/products/seas-prestige-27tffnc-cg-h1406-04-tweeter" class="btn-badge badge-willys">£33.00</a></td>
                <td><a href="https://www.falconacoustics.co.uk/drive-units-1/seas-drive-units/seas-speakers-tweeters-drive-units.html" class="btn-badge badge-falcon">£32.95</a></td>""",
     """                <td style="font-weight: bold; color: white;">SEAS 27TFFNC/CG H1406-04</td>
                <td><a href="research/seas_h1406-04.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/seas-27tffnc-cg.html" class="btn-badge badge-si">€42.95</a></td>
                <td><a href="https://willys-hifi.com/products/seas-prestige-27tffnc-cg-h1406-04-tweeter" class="btn-badge badge-willys">£33.00</a></td>
                <td><a href="https://www.falconacoustics.co.uk/drive-units-1/seas-drive-units/seas-speakers-tweeters-drive-units.html" class="btn-badge badge-falcon">£32.95</a></td>
                <td><a href="https://www.hificollective.co.uk/speakers/seas-h1406-27tffnc-cg-tweeter.html" class="btn-badge badge-hfc">£33.66</a></td>"""),

    # Morel MDT22T
    ("""                <td style="font-weight: bold; color: white;">Morel MDT22T</td>
                <td><a href="research/morel_mdt22t.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/morel-mdt-22.html" class="btn-badge badge-si">€63.95</a></td>
                <td><a href="https://willys-hifi.com/products/morel-mdt-22-tweeter" class="btn-badge badge-willys">£48.00</a></td>
                <td>—</td>""",
     """                <td style="font-weight: bold; color: white;">Morel MDT22T</td>
                <td><a href="research/morel_mdt22t.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/morel-mdt-22.html" class="btn-badge badge-si">€63.95</a></td>
                <td><a href="https://willys-hifi.com/products/morel-mdt-22-tweeter" class="btn-badge badge-willys">£48.00</a></td>
                <td>—</td>
                <td>—</td>"""),

    # Dayton Audio ND25FA-4
    ("""                <td style="font-weight: bold; color: white;">Dayton Audio ND25FA-4</td>
                <td><a href="research/dayton_nd25fa-4.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/dayton-audio-nd25fa-4.html" class="btn-badge badge-si">€21.45</a></td>
                <td><a href="https://willys-hifi.com/collections/dayton-audio-drive-units" class="btn-badge badge-willys">£17.50</a></td>
                <td>—</td>""",
     """                <td style="font-weight: bold; color: white;">Dayton Audio ND25FA-4</td>
                <td><a href="research/dayton_nd25fa-4.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/dayton-audio-nd25fa-4.html" class="btn-badge badge-si">€21.45</a></td>
                <td><a href="https://willys-hifi.com/collections/dayton-audio-drive-units" class="btn-badge badge-willys">£17.50</a></td>
                <td>—</td>
                <td>—</td>"""),

    # Peerless XT25SC90-04
    ("""                <td style="font-weight: bold; color: white;">Peerless XT25SC90-04</td>
                <td><a href="research/peerless_xt25sc90-04.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td>—</td>
                <td><a href="https://willys-hifi.com/products/vifa-xt25sc90-04-tweeter" class="btn-badge badge-willys">£19.52</a></td>
                <td><a href="https://www.falconacoustics.co.uk/peerless-vifa-xt25sc90-04-tweeter-pair.html" class="btn-badge badge-falcon">£18.20</a></td>""",
     """                <td style="font-weight: bold; color: white;">Peerless XT25SC90-04</td>
                <td><a href="research/peerless_xt25sc90-04.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td>—</td>
                <td><a href="https://willys-hifi.com/products/vifa-xt25sc90-04-tweeter" class="btn-badge badge-willys">£19.52</a></td>
                <td><a href="https://www.falconacoustics.co.uk/peerless-vifa-xt25sc90-04-tweeter-pair.html" class="btn-badge badge-falcon">£18.20</a></td>
                <td>—</td>"""),

    # Monacor DT-28N
    ("""                <td style="font-weight: bold; color: white;">Monacor DT-28N</td>
                <td><a href="research/monacor_dt-28n.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/monacor-dt-28n.html" class="btn-badge badge-si">€40.95</a></td>
                <td><a href="https://willys-hifi.com/products/monacor-dt-28n-neodymium-dome-tweeter" class="btn-badge badge-willys">£32.50</a></td>
                <td>—</td>""",
     """                <td style="font-weight: bold; color: white;">Monacor DT-28N</td>
                <td><a href="research/monacor_dt-28n.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/monacor-dt-28n.html" class="btn-badge badge-si">€40.95</a></td>
                <td><a href="https://willys-hifi.com/products/monacor-dt-28n-neodymium-dome-tweeter" class="btn-badge badge-willys">£32.50</a></td>
                <td>—</td>
                <td>—</td>"""),

    # SB Acoustics SB26STCN-C000-4
    ("""                <td style="font-weight: bold; color: white;">SB Acoustics SB26STCN-C000-4</td>
                <td><a href="research/sb_acoustics_sb26stcn-c000-4.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/sb-acoustics-sb26stcn-c000-4.html" class="btn-badge badge-si">€39.95</a></td>
                <td><a href="https://willys-hifi.com/products/sb-acoustics-sb26stcn-c000-4-tweeter" class="btn-badge badge-willys">£29.40</a></td>
                <td>—</td>""",
     """                <td style="font-weight: bold; color: white;">SB Acoustics SB26STCN-C000-4</td>
                <td><a href="research/sb_acoustics_sb26stcn-c000-4.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
                <td><a href="https://www.soundimports.eu/en/sb-acoustics-sb26stcn-c000-4.html" class="btn-badge badge-si">€39.95</a></td>
                <td><a href="https://willys-hifi.com/products/sb-acoustics-sb26stcn-c000-4-tweeter" class="btn-badge badge-willys">£29.40</a></td>
                <td>—</td>
                <td>—</td>""")
]

for old_row, new_row in rows_replacements:
    content = content.replace(old_row, new_row)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("solutions.html updated successfully with HiFi Collective column.")
