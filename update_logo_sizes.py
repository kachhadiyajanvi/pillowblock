import os
import re

def update_html_logos():
    directory = r'E:\PILLOW BLOCK WEB'
    header_old = 'style="height: 45px;"'
    header_new = 'style="height: 75px;"'
    footer_old = 'style="height: 60px; margin-bottom: 20px;"'
    footer_new = 'style="height: 100px; margin-bottom: 20px;"'

    count = 0
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = content.replace(header_old, header_new)
            new_content = new_content.replace(footer_old, footer_new)

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                print(f"Updated: {filename}")

    print(f"Total files updated: {count}")

if __name__ == "__main__":
    update_html_logos()
