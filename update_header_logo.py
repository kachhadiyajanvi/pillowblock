import os, re

# Directory containing HTML files
base_dir = r'e:\PILLOW BLOCK WEB'

# New img tag style
new_style = 'width:140px;height:auto;object-fit:contain;vertical-align:middle;margin:0;padding:0;'

for filename in os.listdir(base_dir):
    if not filename.endswith('.html'):
        continue
    path = os.path.join(base_dir, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Replace any logo img src (png or svg) with the SVG version and new style
    # Pattern matches <img src="assets/...logo..." ...>
    pattern = re.compile(r'<img\s+src=["\']assets/[^"\']*logo[^"\']*["\']\s+alt=["\'][^"\']*["\']\s+style=["\'][^"\']*["\']', re.IGNORECASE)
    replacement = f'<img src="assets/branding-logo.svg" alt="CNZ Bearings Logo" style="{new_style}"'
    new_content = pattern.sub(replacement, content)
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated header logo in {filename}')
