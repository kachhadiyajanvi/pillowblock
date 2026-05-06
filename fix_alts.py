import os

with open('news-blogs.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'alt="Comparison"': 'alt="Pillow block vs plummer block housing comparison"',
    'alt="Failures"': 'alt="Failed pillow block bearing showing lubrication damage"',
    'alt="Installation"': 'alt="Technician installing a pillow block bearing on shaft"',
    'alt="Lubrication"': 'alt="Industrial grease being applied to a pillow block bearing"',
    'alt="Materials"': 'alt="Cast iron vs stainless steel pillow block housing cross-section"'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open('news-blogs.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated alt tags')
