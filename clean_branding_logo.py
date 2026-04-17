from PIL import Image
import os

# Path to the branding logo PNG
logo_path = r'e:\PILLOW BLOCK WEB\assets\branding-logo.png'

if not os.path.exists(logo_path):
    raise FileNotFoundError(f'Logo file not found: {logo_path}')

# Open image with alpha channel
im = Image.open(logo_path).convert('RGBA')

pixels = list(im.getdata())
new_pixels = []
changed = 0
for pixel in pixels:
    r, g, b, a = pixel
    # Identify checkerboard background: typically grayscale squares (r == g == b)
    # and not already transparent. We'll treat any such pixel as background.
    if r == g == b and a != 0:
        # Make fully transparent
        new_pixels.append((r, g, b, 0))
        changed += 1
    else:
        new_pixels.append(pixel)

im.putdata(new_pixels)
im.save(logo_path)
print(f'Checkerboard cleanup completed. Pixels made transparent: {changed}')
