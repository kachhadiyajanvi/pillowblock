import re

file_path = r'e:\PILLOW BLOCK WEB\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove ind-id elements (SYS-01, SEC-01, INF-01 etc)
content = re.sub(r'<div class="ind-id">.*?</div>', '', content)

# 2. Update technical labels to more grounded ones
label_replacements = {
    'SECTOR ANALYSIS': 'INDUSTRIAL SECTORS',
    'NETWORK STATUS': 'GLOBAL PARTNERS',
    'SYSTEM METRICS': 'PRODUCT PERFORMANCE',
    'CORE CAPABILITIES': 'OUR SERVICES',
    'APPLICATION REVIEW': 'TECHNICAL INSIGHTS'
}

for old, new in label_replacements.items():
    content = content.replace(f'<span class="industrial-label">{old}</span>', f'<span class="industrial-label">{new}</span>')

# 3. Remove footer bolts
content = re.sub(r'<div class="footer-bolt.*?"></div>', '', content)

# 4. Standardize footer bottom across index.html too
content = re.sub(
    r'<div class="footer-bottom">[\s\S]*?</div>',
    """<div class="footer-bottom">
                <p>&copy; 2026 CNZ Bearings. ISO 9001:2015 CERTIFIED.</p>
                <div style="font-weight: 800; color: var(--primary);">PRECISION MANUFACTURING GROUP</div>
            </div>""",
    content
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Index industrialization complete.")
