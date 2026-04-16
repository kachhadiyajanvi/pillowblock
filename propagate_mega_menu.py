import os
import re

mega_menu_html_template = """                    <li class="has-mega">
                        <a href="index.html#industries"{active_class}>Industries</a>
                        <div class="mega-menu">
                            <div class="container">
                                <div class="mega-grid">
                                    <div class="mega-col">
                                        <div class="mega-title"><i data-lucide="factory"></i>Heavy Industrial</div>
                                        <ul class="mega-list">
                                            <li><a href="industry-industrial.html" class="mega-item"><i data-lucide="cog"></i>Manufacturing & Production</a></li>
                                            <li><a href="industry-industrial.html" class="mega-item"><i data-lucide="pickaxe"></i>Mining & Heavy Industry</a></li>
                                            <li><a href="industry-industrial.html" class="mega-item"><i data-lucide="building"></i>Construction & Infrastructure</a></li>
                                            <li><a href="industry-industrial.html" class="mega-item"><i data-lucide="car"></i>Automotive & Transportation</a></li>
                                            <li><a href="industry-industrial.html" class="mega-item"><i data-lucide="anvil"></i>Steel & Metal Processing</a></li>
                                        </ul>
                                    </div>
                                    <div class="mega-col">
                                        <div class="mega-title"><i data-lucide="flask-conical"></i>Process & Sciences</div>
                                        <ul class="mega-list">
                                            <li><a href="industry-process.html" class="mega-item"><i data-lucide="utensils"></i>Food & Beverage Processing</a></li>
                                            <li><a href="industry-process.html" class="mega-item"><i data-lucide="pill"></i>Pharmaceutical & Healthcare</a></li>
                                            <li><a href="industry-process.html" class="mega-item"><i data-lucide="beaker"></i>Chemical & Process Industry</a></li>
                                            <li><a href="industry-process.html" class="mega-item"><i data-lucide="scroll"></i>Textile & Paper Industry</a></li>
                                            <li><a href="industry-process.html" class="mega-item"><i data-lucide="recycle"></i>Recycling & Waste Management</a></li>
                                        </ul>
                                    </div>
                                    <div class="mega-col">
                                        <div class="mega-title"><i data-lucide="zap"></i>Energy & Infrastructure</div>
                                        <ul class="mega-list">
                                            <li><a href="industry-infrastructure.html" class="mega-item"><i data-lucide="tractor"></i>Agriculture & Farming</a></li>
                                            <li><a href="industry-infrastructure.html" class="mega-item"><i data-lucide="fan"></i>HVAC & Ventilation</a></li>
                                            <li><a href="industry-infrastructure.html" class="mega-item"><i data-lucide="truck"></i>Material Handling & Logistics</a></li>
                                            <li><a href="industry-infrastructure.html" class="mega-item"><i data-lucide="sun"></i>Renewable Energy</a></li>
                                            <li><a href="industry-infrastructure.html" class="mega-item"><i data-lucide="package"></i>Packaging & Printing</a></li>
                                            <li><a href="industry-infrastructure.html" class="mega-item"><i data-lucide="ship"></i>Marine & Shipbuilding</a></li>
                                            <li><a href="industry-infrastructure.html" class="mega-item"><i data-lucide="zap"></i>Power Generation Plants</a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </li>"""

pattern = re.compile(r'(\s*)<li class="has-dropdown">\s*<a href="[^"]*#industries"( class="active")?>Industries</a>\s*<div class="dropdown-menu">.*?</div>\s*</li>', re.DOTALL)

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
