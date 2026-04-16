import re

file_path = r'e:\PILLOW BLOCK WEB\style.css'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update .tech-hud-section background (already done, but making sure grid is right)
# 2. Update .hud-dashboard (simplify)
content = content.replace(
    'background: rgba(255, 255, 255, 0.02);\n    backdrop-filter: blur(25px);\n    -webkit-backdrop-filter: blur(25px);\n    border: 1px solid rgba(255, 255, 255, 0.05);\n    border-radius: 20px;',
    'background: #11151c;\n    border: 1px solid rgba(255, 255, 255, 0.08);\n    border-radius: 4px;'
)

# 3. Clean up search input inner
search_input_patt = r'\.search-input-inner \{[\s\S]*?\}'
search_input_repl = """.search-input-inner {
    position: relative;
    background: #fff;
    border: 2px solid var(--border);
    border-radius: 4px;
    display: flex;
    align-items: center;
    transition: all 0.3s ease;
}"""
content = re.sub(search_input_patt, search_input_repl, content, count=1)

# 4. Remove bracket corners and tactical pulse
to_remove = [
    r'/\* Bracket Corners \*/',
    r'\.search-input-inner::before,[\s\S]*?\}',
    r'\.search-input-inner::before \{[\s\S]*?\}',
    r'\.search-input-inner::after \{[\s\S]*?\}',
    r'\.search-input-inner:focus-within \{[\s\S]*?\}',
    r'\.search-input-inner:focus-within::before,[\s\S]*?\}',
    r'/\* Tactical Pulse Line \*/',
    r'\.search-input-inner:focus-within \.pulse-line \{[\s\S]*?\}',
    r'@keyframes hudPulse \{[\s\S]*?\}'
]

for patt in to_remove:
    content = re.sub(patt, '', content)

# 5. Fix search input input styling
input_patt = r'\.search-input-inner input \{[\s\S]*?\}'
input_repl = """.search-input-inner input {
    flex: 1;
    background: transparent !important;
    border: none !important;
    padding: 16px 20px !important;
    color: var(--secondary) !important;
    font-family: var(--font-body) !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    outline: none !important;
}"""
content = re.sub(input_patt, input_repl, content, count=1)

# 6. Simplify search input icons
icon_patt = r'\.search-input-inner i \{[\s\S]*?\}'
icon_repl = """.search-input-inner i {
    padding: 0 20px;
    color: var(--primary);
    border-right: 1px solid var(--border);
    width: auto !important;
    height: 20px !important;
}"""
content = re.sub(icon_patt, icon_repl, content, count=1)

# 7. Placeholder fix
placeholder_patt = r'\.search-input-inner input::placeholder \{[\s\S]*?\}'
placeholder_repl = """.search-input-inner input::placeholder {
    color: var(--text-muted) !important;
}"""
content = re.sub(placeholder_patt, placeholder_repl, content, count=1)

# 8. Focus within placeholder fix
focus_placeholder_patt = r'\.search-input-inner:focus-within input::placeholder \{[\s\S]*?\}'
focus_placeholder_repl = """.search-input-inner:focus-within input::placeholder {
    color: var(--text-muted);
}"""
content = re.sub(focus_placeholder_patt, focus_placeholder_repl, content, count=1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Industrialization script complete.")
