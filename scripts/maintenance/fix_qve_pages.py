import os

QVE_PATH = r"c:\xampps\htdocs\public_html\models\qve.html"
DETAILS_PATH = r"c:\xampps\htdocs\public_html\models\qve-details.html"

# General color replacements dict for QVE pages
color_replacements = {
    # Blue/sky to emerald/teal replacements
    "bg-sky-50": "bg-emerald-50/50",
    "bg-sky-100": "bg-emerald-100",
    "border-sky-100": "border-emerald-100",
    "border-sky-200": "border-emerald-200",
    "text-sky-950": "text-slate-900",
    "text-sky-900": "text-slate-900",
    "text-sky-800": "text-emerald-900",
    "text-sky-750": "text-emerald-800",
    "text-sky-700": "text-emerald-800",
    "text-sky-600": "text-emerald-600",
    "text-sky-500": "text-emerald-500",
    "text-sky-400": "text-emerald-400",
    "text-sky-300": "text-emerald-400",
    "hover:bg-sky-50": "hover:bg-emerald-50/50",
    "hover:border-sky-100": "hover:border-emerald-100",
    "hover:border-sky-200": "hover:border-emerald-200",
    "from-sky-": "from-emerald-",
    "to-sky-": "to-emerald-",
    "via-sky-": "via-teal-",
    "from-cyan-": "from-emerald-",
    "to-cyan-": "to-emerald-",
    "via-cyan-": "via-teal-",
    "to-blue-": "to-emerald-",
    "from-blue-": "from-emerald-",
    "bg-blue-": "bg-emerald-",
    "border-blue-": "border-emerald-",
    "text-blue-": "text-emerald-",
    "shadow-blue-": "shadow-emerald-",
    "shadow-sky-": "shadow-emerald-",
    "bg-emerald-50/50 text-peroduaDark": "bg-emerald-50/50 text-emerald-800",
    "bg-sky-200/40": "bg-emerald-500/10",
    "bg-sky-300/40": "bg-emerald-500/10",
    "bg-blue-200/30": "bg-emerald-500/10",
    "bg-sky-200/30": "bg-emerald-500/10",
}

def fix_qve():
    with open(QVE_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace title
    content = content.replace("<title>Perodua Axia - Ahmad Farhan Sales Online</title>", 
                              "<title>Perodua QVE - Ahmad Farhan Sales Online</title>")
    
    # Fix the active/inactive color buttons and add color-swatch-btn class
    old_blue_btn = """                <button onclick="changeCarColor('Ice Blue','../assets/img/qve-blue.png','#7dd3fc',this)"
                    class="group w-full flex items-center gap-4 p-4 rounded-2xl border border-slate-200 hover:border-emerald-300 transition bg-white shadow-sm">"""
    
    new_blue_btn = """                <button onclick="changeCarColor('Ice Blue','../assets/img/qve-blue.png','#7dd3fc',this)"
                    class="color-swatch-btn group w-full flex items-center gap-4 p-4 rounded-2xl border border-emerald-300 shadow-[0_8px_20px_rgba(16,185,129,0.1)] ring-2 ring-emerald-300/30 transition bg-white shadow-sm">"""
    
    old_grey_btn = """                <button onclick="changeCarColor('Caviar Grey','../assets/img/qve-grey.png','#3f4a55',this)"
                    class="group w-full flex items-center gap-4 p-4 rounded-2xl border border-slate-200 hover:border-slate-400 transition bg-white shadow-sm">"""
    
    new_grey_btn = """                <button onclick="changeCarColor('Caviar Grey','../assets/img/qve-grey.png','#3f4a55',this)"
                    class="color-swatch-btn group w-full flex items-center gap-4 p-4 rounded-2xl border border-slate-100 bg-slate-50/50 hover:border-slate-400 transition shadow-sm">"""
    
    content = content.replace(old_blue_btn, new_blue_btn)
    content = content.replace(old_grey_btn, new_grey_btn)
    
    # Update active styles inside JS function
    content = content.replace("rgba(14,165,233,0.1)", "rgba(16,185,129,0.1)")
    
    # Apply color conversions
    for old, new in color_replacements.items():
        content = content.replace(old, new)
        
    with open(QVE_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed qve.html")

def fix_details():
    with open(DETAILS_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace title
    content = content.replace("<title>Perodua Ativa 1.0 X Variant Details - Ahmad Farhan Sales Online</title>",
                              "<title>Perodua QVE Details - Ahmad Farhan Sales Online</title>")
    
    # Fix broken image path
    content = content.replace('src="customer/farhan.png"', 'src="../customer/farhan.png"')
    
    # Apply color conversions
    for old, new in color_replacements.items():
        content = content.replace(old, new)
        
    with open(DETAILS_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed qve-details.html")

def main():
    fix_qve()
    fix_details()

if __name__ == "__main__":
    main()
