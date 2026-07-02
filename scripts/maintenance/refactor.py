import os
import re
import glob

# Paths
ROOT_DIR = r"c:\xampps\htdocs\public_html"
ASSETS_CSS_DIR = os.path.join(ROOT_DIR, "assets", "css")
ASSETS_JS_DIR = os.path.join(ROOT_DIR, "assets", "js")
MODELS_DIR = os.path.join(ROOT_DIR, "models")

ROOT_PAGES = ["index.html", "about.html", "feedback.html"]

def refactor():
    html_files = glob.glob(os.path.join(ROOT_DIR, "*.html"))
    
    all_styles = set()
    tailwind_config_content = ""
    
    # Extract styles and tailwind config
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract tailwind config
        tw_match = re.search(r'<script>\s*tailwind\.config\s*=\s*({.*?})\s*</script>', content, re.DOTALL)
        if tw_match:
            tailwind_config_content = "tailwind.config = " + tw_match.group(1) + ";"
            
        # Extract styles
        style_matches = re.findall(r'<style>(.*?)</style>', content, re.DOTALL)
        for s in style_matches:
            # Clean up the style string a bit to avoid duplicate variations
            all_styles.add(s.strip())
            
    # Write CSS and JS files
    with open(os.path.join(ASSETS_CSS_DIR, "styles.css"), 'w', encoding='utf-8') as f:
        f.write("\n".join(all_styles))
        
    if tailwind_config_content:
        with open(os.path.join(ASSETS_JS_DIR, "tailwind-config.js"), 'w', encoding='utf-8') as f:
            f.write(tailwind_config_content)
            
    # Process files
    for filepath in html_files:
        filename = os.path.basename(filepath)
        is_root_page = filename in ROOT_PAGES
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Remove old styles and tailwind configs
        content = re.sub(r'<script>\s*tailwind\.config\s*=\s*{.*?}\s*</script>', '', content, flags=re.DOTALL)
        content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
        
        # Replace image paths
        # From gambar/ to assets/img/ (for root) or ../assets/img/ (for models)
        img_prefix = "assets/img/" if is_root_page else "../assets/img/"
        content = re.sub(r'src="gambar/', f'src="{img_prefix}', content)
        content = re.sub(r"src='gambar/", f"src='{img_prefix}", content)
        
        # Add CSS and JS links in HEAD
        css_path = "assets/css/styles.css" if is_root_page else "../assets/css/styles.css"
        js_path = "assets/js/tailwind-config.js" if is_root_page else "../assets/js/tailwind-config.js"
        
        head_injections = f"""
    <script src="{js_path}"></script>
    <link rel="stylesheet" href="{css_path}">
"""
        # Inject before </head>
        content = re.sub(r'</head>', f'{head_injections}</head>', content, flags=re.IGNORECASE)
        
        # Update navigation links
        # The car models might have links to index.html, about.html, feedback.html
        # We need to prepend ../ for those if this is a model page, or change links TO model pages
        
        all_models = [os.path.basename(f) for f in html_files if os.path.basename(f) not in ROOT_PAGES]
        
        if is_root_page:
            # We are in root, links to models need models/ prefix
            for model in all_models:
                content = re.sub(rf'href="{model}"', f'href="models/{model}"', content)
            
            new_filepath = filepath # Stays in root
        else:
            # We are in models, links to root pages need ../ prefix
            for root_page in ROOT_PAGES:
                content = re.sub(rf'href="{root_page}"', f'href="../{root_page}"', content)
            # Links to other models stay the same!
            
            new_filepath = os.path.join(MODELS_DIR, filename)
            
        with open(new_filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        # If the file moved, delete the old one
        if not is_root_page and filepath != new_filepath:
            os.remove(filepath)

if __name__ == "__main__":
    refactor()
    print("Refactoring completed.")
