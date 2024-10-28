from PIL import Image, ImageDraw, ImageFont

# Create a blank canvas with white background
img = Image.new('RGB', (800, 600), 'white')
draw = ImageDraw.Draw(img)

# Define font for text
try:
    font = ImageFont.truetype("arial.ttf", 18)
except IOError:
    font = ImageFont.load_default()

# Draw HTML structure diagram using Paint-like style
# Main <html> block
draw.rectangle((50, 50, 750, 550), outline="black", width=3)  # <html> block
draw.text((55, 55), "<html>", fill="black", font=font)
draw.text((55, 515), "</html>", fill="black", font=font)

# <head> section inside <html>
draw.rectangle((70, 80, 730, 180), outline="blue", width=2)  # <head> block
draw.text((75, 85), "<head>", fill="black", font=font)
draw.text((85, 115), "<title>My Website</title>", fill="black", font=font)
draw.text((75, 145), "</head>", fill="black", font=font)

# <body> section inside <html>
draw.rectangle((70, 200, 730, 500), outline="green", width=2)  # <body> block
draw.text((75, 205), "<body>", fill="black", font=font)
draw.text((85, 235), "<h1>Welcome to My Website</h1>", fill="black", font=font)
draw.text((85, 265), "<p>This is a paragraph.</p>", fill="black", font=font)
draw.text((85, 295), "<button>Click Me!</button>", fill="black", font=font)
draw.text((75, 475), "</body>", fill="black", font=font)

# Save the image
img_path = "/mnt/data/html_structure_paint_final.png"
img.save(img_path)

img_path


