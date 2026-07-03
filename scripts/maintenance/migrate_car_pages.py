import os
import glob
import re
import shutil

SRC_DIR = r"C:\xampps\htdocs\abang khairudin\legacy_site"
DEST_DIR = r"c:\xampps\htdocs\public_html\models"

# Ensure destination directory exists
os.makedirs(DEST_DIR, exist_ok=True)

# List of patterns to copy
patterns = ["alza*.html", "ativa*.html", "myvi*.html", "aruz*.html", "axia*.html", "bezza*.html", "traz*.html"]

# General replacements for names and numbers
replacements = {
    # Names
    "Akmal Sales Online": "Ahmad Farhan Sales Online",
    "Khairudin Sales Online": "Ahmad Farhan Sales Online",
    "Follow Khairudin": "Follow Ahmad Farhan",
    "Follow Akmal": "Follow Ahmad Farhan",
    "booking with Khairudin": "booking with Ahmad Farhan",
    "booking with Akmal": "booking with Ahmad Farhan",
    "Contact Khairudin": "Contact Farhan",
    "Contact Akmal": "Contact Farhan",
    "CONTACT AKMAL": "CONTACT FARHAN",
    "CONTACT KHAIRUDIN": "CONTACT FARHAN",
    "Khairudin": "Ahmad Farhan",
    "Akmal": "Ahmad Farhan",
    "Darudin": "Ahmad Farhan",
    "Darundin": "Ahmad Farhan",
    
    # Phone numbers
    "60193751193": "60193650861",
    "60176503339": "60193650861",
    "60183500631": "60193650861",
    "019-375 1193": "019-365 0861",
    "017-650 3339": "019-365 0861",
    "017 650 3339": "019-365 0861",
    "018-350 0631": "019-365 0861",
    "018 350 0631": "019-365 0861",
    "+60 18-350 0631": "+60 19-365 0861",
    
    # Theme configuration script replacement
    '<script src="theme.js"></script>': '<script src="../assets/js/tailwind-config.js"></script>\n    <link rel="stylesheet" href="../assets/css/styles.css">',
    
    # Root Links remapping to parent directory
    'href="index.html"': 'href="../index.html"',
    'href="about.html"': 'href="../about.html"',
    'href="feedback.html"': 'href="../feedback.html"',
    'href="models/our-cars.html"': 'href="our-cars.html"',
    'href="our-cars.html"': 'href="our-cars.html"',
    
    # Image Paths remapping to parent directory
    'src="gambar/': 'src="../gambar/',
    "src='gambar/": "src='../gambar/",
    'src="car/': 'src="../car/',
    "src='car/": "src='../car/",
    'src="customer/': 'src="../customer/',
    "src='customer/": "src='../customer/",
    "'gambar/": "'../gambar/",
    "'car/": "'../car/",
    "'customer/": "'../customer/",
    'onerror="this.src=\'customer/': 'onerror="this.src=\'../customer/',
    'onerror="this.src=\'gambar/': 'onerror="this.src=\'../gambar/',
    'onerror="this.src=\'car/': 'onerror="this.src=\'../car/',
    'url(\'gambar/': 'url(\'../gambar/',
    'url(gambar/': 'url(../gambar/',
    'url(\'car/': 'url(\'../car/',
    'url(car/': 'url(../car/',
    
    # Gold visualizer color adjustments
    "bg-[#f5f3ef]": "bg-slate-50",
    "bg-amber-300/20": "bg-emerald-500/10",
    "bg-yellow-200/20": "bg-emerald-500/10",
    "shadow-[0_45px_90px_rgba(212,175,55,0.08)]": "shadow-[0_45px_90px_rgba(16,185,129,0.08)]",
    "shadow-[0_40px_80px_rgba(14,165,233,0.08)]": "shadow-[0_40px_80px_rgba(16,185,129,0.08)]",
    "shadow-[0_15px_40px_rgba(14,165,233,0.04)]": "shadow-[0_15px_40px_rgba(16,185,129,0.04)]",
    "rgba(14, 165, 233": "rgba(16, 185, 129",
    "rgba(14,165,233": "rgba(16,185,129",
    "from-cyan-50 via-sky-50 to-blue-100": "from-emerald-50 via-teal-50 to-emerald-100",
    "from-cyan-50 via-sky-50 to-sky-100": "from-emerald-50 via-teal-50 to-emerald-100",
    "from-sky-50 via-white to-blue-100": "from-emerald-50 via-white to-emerald-100",
    
    # Sky-blue color remapping in Tailwind
    "text-sky-950": "text-slate-900",
    "text-sky-900": "text-slate-900",
    "text-sky-800": "text-emerald-900",
    "text-sky-700": "text-emerald-800",
    "text-sky-600": "text-emerald-600",
    "text-sky-500": "text-emerald-500",
    "text-sky-400": "text-emerald-400",
    
    "bg-sky-950": "bg-slate-900",
    "bg-sky-900": "bg-slate-900",
    "bg-sky-800": "bg-emerald-900",
    "bg-sky-700": "bg-emerald-800",
    "bg-sky-600": "bg-emerald-600",
    "bg-sky-500": "bg-emerald-500",
    "bg-sky-400": "bg-emerald-400",
    "bg-sky-100": "bg-emerald-100",
    "bg-sky-50": "bg-emerald-50/50",
    
    "border-sky-": "border-emerald-",
    "hover:bg-sky-": "hover:bg-emerald-",
    "hover:border-sky-": "hover:border-emerald-",
    "ring-sky-": "ring-emerald-",
    
    "from-sky-": "from-emerald-",
    "to-sky-": "to-emerald-",
    "via-sky-": "via-teal-",
    "from-cyan-": "from-emerald-",
    "to-blue-100": "to-emerald-100",
    "to-blue-50": "to-emerald-50",
    "shadow-sky-": "shadow-emerald-",
    
    # Gold/Amber text and elements remapping to Emerald Green
    "text-amber-500": "text-emerald-600",
    "text-amber-600": "text-emerald-700",
    "text-amber-700": "text-emerald-800",
    "text-amber-800": "text-emerald-900",
    "bg-amber-": "bg-emerald-",
    "border-amber-": "border-emerald-",
    "shadow-amber-": "shadow-emerald-",
    "from-amber-": "from-emerald-",
    "to-amber-": "to-emerald-",
    "via-amber-": "via-teal-",
}

def migrate_file(src_path, dest_path):
    print(f"Migrating {os.path.basename(src_path)}...")
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Apply general replacements
    new_content = content
    for old, new in replacements.items():
        new_content = new_content.replace(old, new)

    # Let's fix sibling link paths inside the files if there are any that point to root models
    # Example: if there are links to index pages or sibling sub-variants.
    # Sibling variants are alza-x.html, bezza-g.html, which will be in the same models/ folder.
    # Therefore, references to 'alza-x.html' should NOT change because they are both in the same models/ folder.
    # References to 'feedback.html' will be remapped to '../feedback.html' by placements rules.
    
    # Let's check for case-insensitive replacements for names and phone numbers
    new_content = re.sub(r'017-650\s*3339', '019-365 0861', new_content, flags=re.IGNORECASE)
    new_content = re.sub(r'019-375\s*1193', '019-365 0861', new_content, flags=re.IGNORECASE)
    new_content = re.sub(r'018-350\s*0631', '019-365 0861', new_content, flags=re.IGNORECASE)
    new_content = re.sub(r'60193751193', '60193650861', new_content, flags=re.IGNORECASE)
    new_content = re.sub(r'60176503339', '60193650861', new_content, flags=re.IGNORECASE)
    new_content = re.sub(r'60183500631', '60193650861', new_content, flags=re.IGNORECASE)
    
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(new_content)

def main():
    copied_count = 0
    for pattern in patterns:
        search_path = os.path.join(SRC_DIR, pattern)
        for filepath in glob.glob(search_path):
            filename = os.path.basename(filepath)
            dest_filepath = os.path.join(DEST_DIR, filename)
            
            # Avoid copying backup files
            if filename.endswith(".bak"):
                continue
                
            migrate_file(filepath, dest_filepath)
            copied_count += 1
            
    print(f"\nMigration complete. Copied and converted {copied_count} files.")

if __name__ == "__main__":
    main()
