import re

def update_file(filepath):
    print(f"Updating: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Define exact replacements
    replacements = [
        # SB12PFCR25-4 Willys link
        ("https://willys-hifi.com/collections/sb-acoustics-drive-units-all", 
         "https://willys-hifi.com/products/sb-acoustics-sb12pfcr25-4-paper-midwoofer"),
        
        # Scan-Speak R2604/833000 Falcon link
        ("https://www.falconacoustics.co.uk/drive-units-1/scanspeak-speakers-drive-units/scanspeak-tweeters-drive-units.html",
         "https://www.falconacoustics.co.uk/scanspeak-r2604-833000-tweeter-discovery-range.html"),
        
        # Peerless XT25TG30-04 Falcon link
        ("https://www.falconacoustics.co.uk/drive-units-1/peerless-drive-units/peerless-tweeters-drive-units.html",
         "https://www.falconacoustics.co.uk/peerless-vifa-xt25tg30-04-tweeter.html"),
        
        # SB Acoustics SB19ST Falcon link
        ("https://www.falconacoustics.co.uk/drive-units-1/sb-acoustics/sb-acoustics-tweeters.html",
         "https://www.falconacoustics.co.uk/sb-acoustics-sb19st-c000-4-19mm-tweeter.html"),
         
        # SEAS 27TDFC H1189 Falcon link
        ("https://www.falconacoustics.co.uk/drive-units-1/seas-drive-units/seas-speakers-tweeters-drive-units.html",
         "https://www.falconacoustics.co.uk/seas-27tdfc-prestige-tweeter.html"),
    ]

    for old_url, new_url in replacements:
        content = content.replace(old_url, new_url)

    # Some specific replacements where generic categories were used for different items
    # E.g. in the table, XT25SC90-04 uses peerless-tweeters-drive-units.html, but its direct link is different.
    # Let's target lines with XT25SC90-04 and replace its link.
    # We can do this with regex or string replacement if we target specific blocks.
    
    # Let's replace the Falcon link for XT25SC90-04 specifically in solutions.md
    content = content.replace(
        'XT25SC90-04](research/peerless_xt25sc90-04.pdf) ([Willys](https://willys-hifi.com/products/vifa-xt25sc90-04-tweeter) \| [Falcon](https://www.falconacoustics.co.uk/peerless-vifa-xt25tg30-04-tweeter.html))',
        'XT25SC90-04](research/peerless_xt25sc90-04.pdf) ([Willys](https://willys-hifi.com/products/vifa-xt25sc90-04-tweeter) \| [Falcon](https://www.falconacoustics.co.uk/peerless-vifa-xt25sc90-04-tweeter-pair.html))'
    )
    content = content.replace(
        'XT25SC90-04](research/peerless_xt25sc90-04.pdf) ([Willys](https://willys-hifi.com/products/vifa-xt25sc90-04-tweeter) | [Falcon](https://www.falconacoustics.co.uk/peerless-vifa-xt25tg30-04-tweeter.html))',
        'XT25SC90-04](research/peerless_xt25sc90-04.pdf) ([Willys](https://willys-hifi.com/products/vifa-xt25sc90-04-tweeter) | [Falcon](https://www.falconacoustics.co.uk/peerless-vifa-xt25sc90-04-tweeter-pair.html))'
    )
    content = content.replace(
        '| **Peerless XT25SC90-04** | [PDF](research/peerless_xt25sc90-04.pdf) | — | [£19.52](https://willys-hifi.com/products/vifa-xt25sc90-04-tweeter) | [£18.20](https://www.falconacoustics.co.uk/peerless-vifa-xt25tg30-04-tweeter.html) |',
        '| **Peerless XT25SC90-04** | [PDF](research/peerless_xt25sc90-04.pdf) | — | [£19.52](https://willys-hifi.com/products/vifa-xt25sc90-04-tweeter) | [£18.20](https://www.falconacoustics.co.uk/peerless-vifa-xt25sc90-04-tweeter-pair.html) |'
    )

    # In solutions.html:
    # <tr>
    #   <td style="font-weight: bold; color: white;">Peerless XT25SC90-04</td>
    #   <td><a href="research/peerless_xt25sc90-04.pdf" class="btn-badge badge-pdf">Local PDF</a></td>
    #   <td>—</td>
    #   <td><a href="https://willys-hifi.com/products/vifa-xt25sc90-04-tweeter" class="btn-badge badge-willys">£19.52</a></td>
    #   <td><a href="https://www.falconacoustics.co.uk/peerless-vifa-xt25tg30-04-tweeter.html" class="btn-badge badge-falcon">£18.20</a></td>
    # </tr>
    # Wait, XT25SC90-04 was mapped to XT25TG30-04 on Falcon in the previous step?
    # Let's fix that!
    content = content.replace(
        'href="https://www.falconacoustics.co.uk/peerless-vifa-xt25tg30-04-tweeter.html" class="btn-badge badge-falcon">£18.20</a>',
        'href="https://www.falconacoustics.co.uk/peerless-vifa-xt25sc90-04-tweeter-pair.html" class="btn-badge badge-falcon">£18.20</a>'
    )
    # Also in other places where Peerless XT25SC90-04 is linked:
    # E.g.:
    # <strong>XT25SC90-04</strong> ... <a href="https://www.falconacoustics.co.uk/peerless-vifa-xt25tg30-04-tweeter.html" class="btn-badge badge-falcon">Falcon</a>
    content = re.sub(
        r'XT25SC90-04(.*?)href="https://www.falconacoustics.co.uk/peerless-vifa-xt25tg30-04-tweeter.html"(.*?)Falcon',
        r'XT25SC90-04\1href="https://www.falconacoustics.co.uk/peerless-vifa-xt25sc90-04-tweeter-pair.html"\2Falcon',
        content
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

update_file("C:/Users/johnl/work/speaker/solutions.md")
update_file("C:/Users/johnl/work/speaker/solutions.html")
print("Done!")
