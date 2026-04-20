import re
import os

def repair_svg():
    path = r'E:\PILLOW BLOCK WEB\assets\branding-logo.svg'
    if not os.path.exists(path):
        print(f"Error: {path} not found.")
        return

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove filter and mask attributes that point to internal IDs
    # This restores the original colors of the embedded PNG
    new_content = re.sub(r'\s(filter|mask)="url\(#[a-zA-Z0-9_-]+\)"', '', content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("SVG successfully repaired. Filters and masks removed.")

if __name__ == "__main__":
    repair_svg()
