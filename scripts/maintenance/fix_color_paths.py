import os
import glob

MODELS_DIR = r"c:\xampps\htdocs\public_html\models"

def main():
    html_files = glob.glob(os.path.join(MODELS_DIR, "*.html"))
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        updated = False
        
        # 1. Replace 'gambar/ with '../assets/img/
        if "'gambar/" in content:
            content = content.replace("'gambar/", "'../assets/img/")
            updated = True
        if '"gambar/' in content:
            content = content.replace('"gambar/', '"../assets/img/')
            updated = True
            
        # 2. Replace 'car/ with '../car/
        if "'car/" in content:
            content = content.replace("'car/", "'../car/")
            updated = True
        if '"car/' in content:
            content = content.replace('"car/', '"../car/')
            updated = True
            
        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed color paths in: {filepath}")
        else:
            print(f"No path updates in: {filepath}")

if __name__ == "__main__":
    main()
