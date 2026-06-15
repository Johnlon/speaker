"""
add_role_tags.py — prepend Role: **<ROLE>** | to the first spec bullet of every
### driver entry in drivers.md, based on which ## section it lives in.

Safe to re-run: entries that already start with "Role:" are left unchanged.
"""

import re
import sys

DRIVERS_MD = r"C:\Users\johnl\work\speaker\drivers.md"

# Map the exact ## heading text to the Role tag value
SECTION_ROLE_MAP = {
    "## Subwoofer": "SUB",
    "## Passive Radiator": "PR",
    "## Tweeters": "HIGH",
    "## June 2026 Mass Index — Tweeters (all visual constraints removed)": "HIGH",
    "## Midranges": "MID",
    "## June 2026 Mass Index — Woofers & Midranges (all visual constraints removed)": "MID",
    "## Hard-Excluded Drivers": "EXCL",
}

def process(path):
    with open(path, encoding="utf-8") as fh:
        lines = fh.readlines()

    current_role = None   # role string for the active ## section, or None
    in_entry = False      # True between a ### line and its first bullet
    modified = 0
    skipped_already = 0
    output = []

    for i, line in enumerate(lines):
        stripped = line.rstrip("\n")

        # Detect ## section changes (must be exactly ## not ###)
        if re.match(r'^## ', stripped):
            current_role = SECTION_ROLE_MAP.get(stripped)
            in_entry = False
            output.append(line)
            continue

        # Detect ### driver entry start
        if re.match(r'^### ', stripped):
            in_entry = True
            output.append(line)
            continue

        # If we're inside an entry and this is the first bullet line
        if in_entry and stripped.startswith("- "):
            in_entry = False  # consume: only first bullet matters
            if current_role is None:
                # Unrecognised section — leave untouched
                output.append(line)
                continue
            role_tag = f"Role: **{current_role}**"
            # Check if already tagged
            if stripped.startswith(f"- {role_tag}") or "Role: **" in stripped[:30]:
                skipped_already += 1
                output.append(line)
                continue
            # Prepend the role tag
            # line is "- <rest>\n" → "- Role: **X** | <rest>\n"
            rest = stripped[2:]  # strip leading "- "
            new_line = f"- {role_tag} | {rest}\n"
            output.append(new_line)
            modified += 1
            continue

        # Any non-bullet line while inside an entry keeps in_entry True so we
        # only consume when we actually hit a bullet.  But blank lines or
        # sub-headings should reset it.
        if in_entry:
            # A blank line or a line that is clearly not a continuation
            # (another heading, a horizontal rule, etc.) means there's no
            # immediate first-bullet — reset.
            if stripped == "" or stripped.startswith("#") or stripped.startswith("---"):
                in_entry = False

        output.append(line)

    with open(path, "w", encoding="utf-8") as fh:
        fh.writelines(output)

    print(f"Done. Modified: {modified} lines, already-tagged skipped: {skipped_already}.")
    return modified

if __name__ == "__main__":
    process(DRIVERS_MD)
