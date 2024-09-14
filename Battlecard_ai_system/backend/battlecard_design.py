from PIL import Image, ImageDraw, ImageFont

def create_battlecard_image(battlecard_content):
    img = Image.new('RGB', (800, 600), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    
    # Use a default font
    font = ImageFont.load_default()
    
    # Insert battlecard content into the image
    d.text((10, 10), battlecard_content, font=font, fill=(0, 0, 0))
    
    img.save("battlecard.png")
    return "battlecard.png"
