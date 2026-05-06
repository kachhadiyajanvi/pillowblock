import os

with open('news-blogs.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'alt="Bearing Types"': 'alt="Different types of pillow block bearing housing units side by side"'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open('news-blogs.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated alt tag for Card 002')
