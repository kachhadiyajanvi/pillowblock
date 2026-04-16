import re
import os

files_to_clean = [
    r'e:\PILLOW BLOCK WEB\about.html',
    r'e:\PILLOW BLOCK WEB\industry-industrial.html',
    r'e:\PILLOW BLOCK WEB\industry-process.html',
    r'e:\PILLOW BLOCK WEB\industry-infrastructure.html',
    r'e:\PILLOW BLOCK WEB\product-ucp.html',
    r'e:\PILLOW BLOCK WEB\product-ucf.html',
    r'e:\PILLOW BLOCK WEB\product-ucfl.html',
    r'e:\PILLOW BLOCK WEB\product-ucfc.html',
    r'e:\PILLOW BLOCK WEB\product-uct.html',
    r'e:\PILLOW BLOCK WEB\news.html',
    r'e:\PILLOW BLOCK WEB\news-events.html',
    r'e:\PILLOW BLOCK WEB\news-newsletters.html',
    r'e:\PILLOW BLOCK WEB\news-blogs.html'
]

label_replacements = {
    'SECTOR ANALYSIS': 'INDUSTRIAL SECTORS',
    'NETWORK STATUS': 'GLOBAL PARTNERS',
    'SYSTEM METRICS': 'PRODUCT PERFORMANCE',
    'CORE CAPABILITIES': 'OUR SERVICES',
    'APPLICATION REVIEW': 'TECHNICAL INSIGHTS',
    'TECHNICAL SPECIFICATIONS': 'PRODUCT DATA',
    'SPECIFICATION HUB': 'TECHNICAL DATA',
    'EVENT LOG': 'LATEST EVENTS',
    'MISSION TIMELINE': 'OUR HISTORY'
}

def industrialize_file(path):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return
        
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove ind-id elements
    content = re.sub(r'<div class="ind-id">.*?</div>', '', content)
    
    # 2. Update industrial-labels
    for old, new in label_replacements.items():
        content = content.replace(f'<span class="industrial-label">{old}</span>', f'<span class="industrial-label">{new}</span>')
        content = content.replace(f'<span class="section-tag">{old}</span>', f'<span class="section-tag">{new}</span>')

    # 3. Remove footer bolts
    content = re.sub(r'<div class="footer-bolt.*?"></div>', '', content)
    
    # 4. Standardize footer bottom
    content = re.sub(
        r'<div class="footer-bottom">[\s\S]*?</div>',
        """<div class="footer-bottom">
                <p>&copy; 2026 CNZ Bearings. ISO 9001:2015 CERTIFIED.</p>
                <div style="font-weight: 800; color: var(--primary);">PRECISION MANUFACTURING GROUP</div>
            </div>""",
        content
    )
    
    # 5. Remove any inline bracket styles if they exist
    content = content.replace('border-radius: 20px;', 'border-radius: 4px;') # Hard corners
    content = content.replace('backdrop-filter: blur(25px);', '') # Remove scifi glassmorphism
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Industrialized: {os.path.basename(path)}")

for f in files_to_clean:
    industrialize_file(f)

print("Master industrialization cleanup complete.")
