import os, glob, re

for file_name in glob.glob('blog-*.html'):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_tag = '<article class=\"article-console\">'
    end_tag = '</article>'
    
    if start_tag in content and end_tag in content:
        start_idx = content.find(start_tag)
        end_idx = content.find(end_tag, start_idx)
        
        pre = content[:start_idx]
        post = content[end_idx:]
        article_content = content[start_idx:end_idx]
        
        # Replace color: #fff; with color: #000;
        article_content = article_content.replace('color: #fff;', 'color: #000;')
        # Also handle color: #ffffff;
        article_content = article_content.replace('color: #ffffff;', 'color: #000;')
        # Also handle color: #FFF;
        article_content = article_content.replace('color: #FFF;', 'color: #000;')
        # Also handle color: #FFFFFF;
        article_content = article_content.replace('color: #FFFFFF;', 'color: #000;')
        # Also handle color:#fff;
        article_content = article_content.replace('color:#fff;', 'color:#000;')
        
        new_content = pre + article_content + post
        
        if new_content != content:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {file_name}')
