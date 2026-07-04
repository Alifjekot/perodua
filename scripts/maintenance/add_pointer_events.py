import os
import glob
import re

ROOT_DIR = r"c:\xampps\htdocs\public_html"

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match absolute inset-0 divs that immediately contain a child absolute div with blur or rounded-full (typical layout for background glows)
    pattern = r'<div class="absolute inset-0">\s*<div class="absolute [^>]*blur-[^>]*>'
    
    def replacer(match):
        matched_str = match.group(0)
        return matched_str.replace('class="absolute inset-0"', 'class="absolute inset-0 pointer-events-none"')

    new_content, count = re.subn(pattern, replacer, content, flags=re.DOTALL)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Added pointer-events-none to {count} background glow layer(s) in {os.path.basename(filepath)}")

def main():
    # Process root HTML files
    for filepath in glob.glob(os.path.join(ROOT_DIR, "*.html")):
        fix_file(filepath)
    # Process model HTML files
    for filepath in glob.glob(os.path.join(ROOT_DIR, "models", "*.html")):
        fix_file(filepath)

if __name__ == "__main__":
    main()
