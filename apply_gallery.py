from pathlib import Path
p = Path("src/pages/about.astro")
if not p.exists():
    raise SystemExit("Run this script from the root of BrownYumYum/cain-portfolio.")
s = p.read_text(encoding="utf-8")
if 'class="journey-gallery' in s:
    raise SystemExit("The gallery appears to be installed already; no changes made.")
anchor = '    <section class="about-education"'
if anchor not in s:
    raise SystemExit("Expected About-page insertion point not found. No changes made.")
s = s.replace(anchor, Path("journey-gallery-section.html").read_text(encoding="utf-8") + '\n' + anchor, 1)
s += '\n' + Path("journey-gallery-style.html").read_text(encoding="utf-8")
p.write_text(s, encoding="utf-8")
print("Added curated journey gallery to src/pages/about.astro")
