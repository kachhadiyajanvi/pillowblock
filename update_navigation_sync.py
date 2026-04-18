import os
import re

def update_navigation(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for the News dropdown item that specifically points to catalogue.html
    # We want to change the text to "Newsletters" and the link to "news-newsletters.html"
    
    # 1. Update the dropdown link
    dropdown_pattern = re.compile(r'(<a\s+href="catalogue\.html"\s+class="dropdown-item"><span>)Catalogue(</span></a>)', re.IGNORECASE)
    new_content = dropdown_pattern.sub(r'\1Newsletters\2', content)
    new_content = new_content.replace('href="catalogue.html" class="dropdown-item"', 'href="news-newsletters.html" class="dropdown-item"')

    # 2. Safety check: ensure we didn't touch the main nav link "Catalogue"
    # The main nav usually looks like: <li><a href="catalogue.html">Catalogue</a></li>
    # The regex above only touches items with class="dropdown-item"
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    updated_count = 0
    for html_file in html_files:
        if update_navigation(html_file):
            print(f"Updated navigation in: {html_file}")
            updated_count += 1
    
    print(f"\nTotal files updated: {updated_count}")

if __name__ == "__main__":
    main()
