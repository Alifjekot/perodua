import os
from PIL import Image

src_path = r"C:\Users\fitri\.gemini\antigravity-ide\brain\1fdfdff9-4a08-479b-831a-eb3900466d0f\media__1782965780050.png"
dest_dir = r"c:\xampps\htdocs\public_html\customer"
dest_img_path = os.path.join(dest_dir, "farhan.png")

def main():
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        
    img = Image.open(src_path)
    width, height = img.size
    
    # We want a portrait crop for About Me
    # The subject (Ahmad Farhan) is in the middle-right.
    # Let's crop from X = 320 to X = 820 (width = 500), and Y = 0 to Y = 584 (height = 584)
    # This is a nice 500x584 portrait crop.
    left = 300
    top = 0
    right = 800
    bottom = height
    
    cropped_img = img.crop((left, top, right, bottom))
    cropped_img.save(dest_img_path)
    print("Cropped and saved to", dest_img_path)

if __name__ == "__main__":
    main()
