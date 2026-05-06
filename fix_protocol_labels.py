import glob

for file_name in glob.glob('blog-*.html'):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    for line in lines:
        if 'letter-spacing: 4px; color: var(--primary)' in line and 'span' in line:
            continue
        new_lines.append(line)
        
    if len(new_lines) != len(lines):
        with open(file_name, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f'Updated {file_name}')
