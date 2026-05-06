import re

with open('news-blogs.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_card = False
card_depth = 0

for i in range(len(lines)):
    line = lines[i]
    
    # Check for opening tag
    match = re.search(r'<div class="dossier-card" data-category="(.*?)" onclick="window\.location=\'(.*?)\'">', line)
    if match:
        category = match.group(1)
        url = match.group(2)
        lines[i] = line.replace(match.group(0), f'<a class="dossier-card" data-category="{category}" href="{url}" style="text-decoration:none;">')
        in_card = True
        card_depth = 1
        continue
        
    if in_card:
        # count div tags
        div_opens = len(re.findall(r'<div\b[^>]*>', line))
        div_closes = len(re.findall(r'</div>', line))
        card_depth += div_opens
        card_depth -= div_closes
        
        if card_depth <= 0:
            # this line closes the card!
            # Replace the last </div> with </a>
            # Find the last </div>
            last_div_idx = line.rfind('</div>')
            if last_div_idx != -1:
                lines[i] = line[:last_div_idx] + '</a>' + line[last_div_idx+6:]
            in_card = False
            card_depth = 0

with open('news-blogs.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Updated news-blogs.html')
