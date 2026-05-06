import os

with open('news-blogs.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'alt="Selection Logic"': 'alt="Engineer selecting pillow block bearing for heavy load application"',
    'alt="Conveyors"': 'alt="Conveyor belt system using pillow block bearings in logistics facility"'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open('news-blogs.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated alt tags')
