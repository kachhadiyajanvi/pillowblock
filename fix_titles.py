import os

with open('news-blogs.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '<h3 class="dossier-title">WHAT IS A PILLOW BLOCK?</h3>': '<h3 class="dossier-title">What Is a Pillow Block?</h3>',
    '<h3 class="dossier-title">PRODUCT TYPES EXPLAINED</h3>': '<h3 class="dossier-title">Product Types Explained</h3>',
    '<h3 class="dossier-title">PILLOW VS PLUMMER BLOCK</h3>': '<h3 class="dossier-title">Pillow vs Plummer Block</h3>',
    '<h3 class="dossier-title">CORE INSTALLATION STAGE</h3>': '<h3 class="dossier-title">Core Installation Stage</h3>',
    '<h3 class="dossier-title">FAILURE SOURCE DIAGNOSIS</h3>': '<h3 class="dossier-title">Failure Source Diagnosis</h3>',
    '<h3 class="dossier-title">ALLOY & MATERIAL SCIENCE</h3>': '<h3 class="dossier-title">Alloy & Material Science</h3>',
    '<h3 class="dossier-title">HEAVY LOAD SELECTION</h3>': '<h3 class="dossier-title">Heavy Load Selection</h3>',
    '<h3 class="dossier-title">CONVEYOR DYNAMICS</h3>': '<h3 class="dossier-title">Conveyor Dynamics</h3>',
    '<h3 class="dossier-title">LUBRICATION PROTOCOLS</h3>': '<h3 class="dossier-title">Lubrication Protocols</h3>',
    '<h3 class="dossier-title">CRITICAL MOUNTING ERRORS</h3>': '<h3 class="dossier-title">Critical Mounting Errors</h3>'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open('news-blogs.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated titles')
