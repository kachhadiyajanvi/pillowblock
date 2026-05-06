import glob

for file_name in glob.glob('blog-*.html'):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '**' in content:
        new_content = content.replace('**', '')
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {file_name}')
