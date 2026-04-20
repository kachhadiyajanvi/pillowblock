import os

directory = r'e:\PILLOW BLOCK WEB'
search_text = 'Direct Support'
replace_text = 'Chat with us'

html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for filename in html_files:
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if search_text in content:
        new_content = content.replace(search_text, replace_text)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {filename}")
    else:
        print(f"No match in: {filename}")
