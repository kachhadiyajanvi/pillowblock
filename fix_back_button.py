import os, glob

for file_name in glob.glob('blog-*.html'):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Target string
    old_str = '<i data-lucide=\"terminal\" size=\"18\"></i> CD .. / TECHNICAL_LIBRARY'
    new_str = '<i data-lucide=\"arrow-left\" size=\"18\"></i> Back'
    
    if old_str in content:
        new_content = content.replace(old_str, new_str)
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {file_name}')
