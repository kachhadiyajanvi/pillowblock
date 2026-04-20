import os
import re

mega_menu_html_template = """                    <li class="has-mega">
                        <a href="index.html#industries"{active_class}>Industries</a>
                        <div class="mega-menu">
                            <div class="container">
                                <div class="mega-grid">
                                    <div class="mega-col">
                                        <div class="mega-title">Heavy Industrial</div>
                                        <ul class="mega-list">
                                            <li><a href="industry-industrial.html" class="mega-item">Manufacturing & Production</a></li>
                                            <li><a href="industry-industrial.html" class="mega-item">Mining & Heavy Industry</a></li>
                                            <li><a href="industry-industrial.html" class="mega-item">Construction & Infrastructure</a></li>
                                            <li><a href="industry-industrial.html" class="mega-item">Automotive & Transportation</a></li>
                                            <li><a href="industry-industrial.html" class="mega-item">Steel & Metal Processing</a></li>
                                        </ul>
                                    </div>
                                    <div class="mega-col">
                                        <div class="mega-title">Process & Sciences</div>
                                        <ul class="mega-list">
                                            <li><a href="industry-process.html" class="mega-item">Food & Beverage Processing</a></li>
                                            <li><a href="industry-process.html" class="mega-item">Pharmaceutical & Healthcare</a></li>
                                            <li><a href="industry-process.html" class="mega-item">Chemical & Process Industry</a></li>
                                            <li><a href="industry-process.html" class="mega-item">Textile & Paper Industry</a></li>
                                            <li><a href="industry-process.html" class="mega-item">Recycling & Waste Management</a></li>
                                        </ul>
                                    </div>
                                    <div class="mega-col">
                                        <div class="mega-title">Energy & Infrastructure</div>
                                        <ul class="mega-list">
                                            <li><a href="industry-infrastructure.html" class="mega-item">Agriculture & Farming</a></li>
                                            <li><a href="industry-infrastructure.html" class="mega-item">HVAC & Ventilation</a></li>
                                            <li><a href="industry-infrastructure.html" class="mega-item">Material Handling & Logistics</a></li>
                                            <li><a href="industry-infrastructure.html" class="mega-item">Renewable Energy</a></li>
                                            <li><a href="industry-infrastructure.html" class="mega-item">Packaging & Printing</a></li>
                                            <li><a href="industry-infrastructure.html" class="mega-item">Marine & Shipbuilding</a></li>
                                            <li><a href="industry-infrastructure.html" class="mega-item">Power Generation Plants</a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </li>"""

pattern = re.compile(r'(\s*)<li class="(?:has-dropdown|has-mega)">\s*<a href="[^"]*#industries"( class="active")?>Industries</a>\s*<div class="(?:dropdown-menu|mega-menu)">.*?</div>\s*</li>', re.DOTALL)

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        match = pattern.search(content)
        if match:
            active_class = match.group(2) if match.group(2) else ""
            replacement = mega_menu_html_template.format(active_class=active_class)
            new_content = pattern.sub(replacement, content)
            
            if content != new_content:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")
        else:
            # print(f"No match in {filename}")
            pass
