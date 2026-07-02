import os
import glob

ROOT_DIR = r"c:\xampps\htdocs\public_html"
MODELS_DIR = os.path.join(ROOT_DIR, "models")

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace profile image path
    new_content = content.replace("customer/akmal.png", "customer/farhan.png")
    
    # For about.html, replace the main conference photo with Farhan's photo
    if "about.html" in filepath:
        new_content = new_content.replace("assets/img/akmal-conference.jpeg", "customer/farhan.png")
        new_content = new_content.replace("alt=\"Akmal\"", "alt=\"Ahmad Farhan\"")

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated images in {filepath}")
    else:
        print(f"No changes in {filepath}")

def main():
    # Root files
    update_file(os.path.join(ROOT_DIR, "index.html"))
    update_file(os.path.join(ROOT_DIR, "about.html"))
    update_file(os.path.join(ROOT_DIR, "feedback.html"))
    
    # Model files
    model_files = glob.glob(os.path.join(MODELS_DIR, "*.html"))
    for filepath in model_files:
        update_file(filepath)

if __name__ == "__main__":
    main()
