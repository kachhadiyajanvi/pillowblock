import os
import re

directory = r'e:\PILLOW BLOCK WEB'
# Target is the whatsapp-float link. We want to find its content and ensure wa-tooltip is inside.
whatsapp_pattern = re.compile(r'(<a\s+href="https://wa.me/918511153657"[^>]*class="whatsapp-float"[^>]*>)(.*?)(</a>)', re.DOTALL | re.IGNORECASE)

html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for filename in html_files:
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = whatsapp_pattern.search(content)
    if match:
        full_a_tag = match.group(0)
        inner_content = match.group(2)
        
        # Check if wa-tooltip exists
        if '<div class="wa-tooltip">' not in inner_content:
            # Inject tooltip before the pulse (if exists) or just after the icon
            new_inner = inner_content.replace('<div class="wa-pulse"></div>', '')
            new_inner = new_inner.strip() + '\n        <div class="wa-tooltip">Chat with us</div>\n        <div class="wa-pulse"></div>'
            new_a_tag = match.group(1) + new_inner + match.group(3)
            new_content = content.replace(full_a_tag, new_a_tag)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed (Injected): {filename}")
        else:
            # Already exists, check text
            if 'Chat with us' not in inner_content:
                # This should have been caught by the simple replace script, but let's be safe
                new_inner = re.sub(r'<div class="wa-tooltip">.*?</div>', '<div class="wa-tooltip">Chat with us</div>', inner_content)
                new_a_tag = match.group(1) + new_inner + match.group(3)
                new_content = content.replace(full_a_tag, new_a_tag)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed (Updated Text): {filename}")
            else:
                print(f"Already OK: {filename}")
    else:
        print(f"WhatsApp button not found in: {filename}")
