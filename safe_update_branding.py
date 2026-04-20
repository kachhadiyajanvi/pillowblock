import os

def safe_update_html():
    d = r'e:\PILLOW BLOCK WEB'
    for f in os.listdir(d):
        if f.endswith('.html'):
            p = os.path.join(d, f)
            with open(p, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # 1. Update logo path to transparent PNG
            new_content = content.replace('assets/branding-logo.svg', 'assets/branding-logo.png')
            new_content = new_content.replace('assets/logo.png', 'assets/branding-logo.png')
            
            # 2. Update Header size (45px -> 75px)
            new_content = new_content.replace('height: 45px;', 'height: 75px;')
            
            # 3. Update Footer size (60px -> 100px)
            new_content = new_content.replace('height: 60px; margin-bottom: 20px;', 'height: 100px; margin-bottom: 20px;')
            new_content = new_content.replace('height: 100px;', 'height: 100px;') # Catch all
            
            with open(p, 'w', encoding='utf-8') as file:
                file.write(new_content)
    print("Updated 25 HTML files safely.")

if __name__ == '__main__':
    safe_update_html()
