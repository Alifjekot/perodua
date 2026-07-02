import os
import re
import glob

ROOT_DIR = r"c:\xampps\htdocs\public_html"
MODELS_DIR = os.path.join(ROOT_DIR, "models")

def get_navbar(prefix, active_page):
    def get_desktop_class(item):
        if item == active_page:
            return "text-peroduaDark font-bold text-sm tracking-wide border-b-2 border-peroduaDark py-2"
        else:
            return "text-slate-600 hover:text-peroduaDark font-semibold text-sm tracking-wide transition-colors duration-200"

    if active_page == 'cars':
        cars_btn_class = "text-peroduaDark font-bold text-sm tracking-wide flex items-center space-x-1 py-2 focus:outline-none transition-colors duration-200 border-b-2 border-peroduaDark"
    else:
        cars_btn_class = "text-slate-600 group-hover:text-peroduaDark font-semibold text-sm tracking-wide flex items-center space-x-1 py-2 focus:outline-none transition-colors duration-200"

    def get_mobile_class(item):
        if item == active_page:
            return "block py-2 text-peroduaDark font-bold border-b border-slate-50"
        else:
            return "block py-2 text-slate-600 hover:text-peroduaDark font-bold border-b border-slate-50"

    home_path = f"{prefix}index.html"
    feedback_path = f"{prefix}feedback.html"
    about_path = f"{prefix}about.html"
    logo_path = f"{prefix}assets/img/logo-perodua.png"
    
    alza_path = f"{prefix}models/alza.html" if not prefix else "alza.html"
    ativa_path = f"{prefix}models/ativa.html" if not prefix else "ativa.html"
    myvi_path = f"{prefix}models/myvi.html" if not prefix else "myvi.html"
    aruz_path = f"{prefix}models/aruz.html" if not prefix else "aruz.html"
    axia_path = f"{prefix}models/axia.html" if not prefix else "axia.html"
    bezza_path = f"{prefix}models/bezza.html" if not prefix else "bezza.html"
    traz_path = f"{prefix}models/traz.html" if not prefix else "traz.html"

    return f"""<!-- Top Announcement Bar -->
    <div class="bg-gradient-to-r from-brandSlate to-slate-900 text-white text-xs py-2.5 px-4 text-center sm:text-right sm:px-8 font-medium tracking-wide shadow-sm">
        <span class="inline-flex items-center mr-4">
            <i class="fa-solid fa-location-dot text-perodua mr-1.5 animate-pulse"></i> Glenmarie Branch
        </span>
        <a href="https://wa.me/60176503339?text=Hi%2C%20saya%20berminat%20untuk%20membeli%20kereta%20Perodua.%20Boleh%20saya%20dapatkan%20maklumat%20lanjut%20mengenai%20model%20dan%20promosi%20terkini%3F" class="inline-flex items-center text-slate-200 hover:text-perodua ml-2 transition-colors duration-200">
            <i class="fa-brands fa-whatsapp text-emerald-400 mr-1.5 text-sm"></i> Contact Advisor
        </a>
    </div>

    <!-- Sticky Navigation Header -->
    <header class="bg-white/90 backdrop-blur-md shadow-sm border-b border-slate-100 sticky top-0 z-50 transition-all duration-300">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-20 items-center">
                <div class="flex items-center space-x-4">
                    <a href="{home_path}" class="flex-shrink-0 transition-transform hover:scale-105 duration-200">
                        <img src="{logo_path}" alt="Perodua Logo" class="h-10 w-auto object-contain"
                            onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Perodua_logo.svg/512px-Perodua_logo.svg.png'">
                    </a>
                    <div class="hidden lg:block pl-4 border-l-2 border-slate-200">
                        <span class="font-black text-lg block text-slate-900 tracking-tight leading-none">Glenmarie Sales</span>
                        <span class="text-[10px] text-peroduaDark font-bold uppercase tracking-widest mt-1 block">Authorized Branch</span>
                    </div>
                </div>

                <nav class="hidden md:flex space-x-8 items-center">
                    <a href="{home_path}" class="{get_desktop_class('home')}">Home</a>

                    <div class="relative group">
                        <button class="{cars_btn_class}">
                            <span>Our Cars</span>
                            <i class="fa-solid fa-chevron-down text-[10px] transition-transform duration-300 group-hover:rotate-180"></i>
                        </button>
                        <div class="absolute left-0 mt-2 w-64 bg-white border border-slate-100 rounded-2xl shadow-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50 py-3 transform scale-95 group-hover:scale-100">
                            <a href="{alza_path}" class="flex items-center px-4 py-3 text-xs font-bold text-slate-700 hover:bg-slate-50 hover:text-peroduaDark rounded-xl mx-2 transition-all"><i class="fa-solid fa-car-side mr-3 text-slate-400 w-5 text-center"></i> NEW PERODUA ALZA</a>
                            <a href="{ativa_path}" class="flex items-center px-4 py-3 text-xs font-bold text-slate-700 hover:bg-slate-50 hover:text-peroduaDark rounded-xl mx-2 transition-all"><i class="fa-solid fa-car-side mr-3 text-slate-400 w-5 text-center"></i> PERODUA ATIVA</a>
                            <a href="{myvi_path}" class="flex items-center px-4 py-3 text-xs font-bold text-slate-700 hover:bg-slate-50 hover:text-peroduaDark rounded-xl mx-2 transition-all"><i class="fa-solid fa-car-side mr-3 text-slate-400 w-5 text-center"></i> PERODUA MYVI</a>
                            <a href="{aruz_path}" class="flex items-center px-4 py-3 text-xs font-bold text-slate-700 hover:bg-slate-50 hover:text-peroduaDark rounded-xl mx-2 transition-all"><i class="fa-solid fa-car-side mr-3 text-slate-400 w-5 text-center"></i> PERODUA ARUZ</a>
                            <a href="{axia_path}" class="flex items-center px-4 py-3 text-xs font-bold text-slate-700 hover:bg-slate-50 hover:text-peroduaDark rounded-xl mx-2 transition-all"><i class="fa-solid fa-car-side mr-3 text-slate-400 w-5 text-center"></i> PERODUA AXIA</a>
                            <a href="{bezza_path}" class="flex items-center px-4 py-3 text-xs font-bold text-slate-700 hover:bg-slate-50 hover:text-peroduaDark rounded-xl mx-2 transition-all"><i class="fa-solid fa-car-side mr-3 text-slate-400 w-5 text-center"></i> PERODUA BEZZA</a>
                            <a href="{traz_path}" class="flex items-center px-4 py-3 text-xs font-bold text-slate-700 hover:bg-slate-50 hover:text-peroduaDark rounded-xl mx-2 transition-all"><i class="fa-solid fa-car-side mr-3 text-slate-400 w-5 text-center"></i> PERODUA TRAZ</a>
                        </div>
                    </div>

                    <a href="{feedback_path}" class="{get_desktop_class('feedback')}">Feedback Customer</a>
                    <a href="{about_path}" class="{get_desktop_class('about')}">About Me</a>

                    <a href="https://wa.me/60176503339?text=Hi%2C%20saya%20berminat%20untuk%20membeli%20kereta%20Perodua.%20Boleh%20saya%20dapatkan%20maklumat%20lanjut%20mengenai%20model%20dan%20promosi%20terkini%3F" target="_blank"
                        class="bg-emerald-500 hover:bg-emerald-600 text-white font-bold px-5 py-2.5 rounded-xl flex items-center space-x-2 shadow-md shadow-emerald-500/20 hover:shadow-emerald-500/30 transition duration-200 transform hover:-translate-y-0.5">
                        <i class="fa-brands fa-whatsapp text-lg"></i> <span>017-650 3339</span>
                    </a>
                </nav>

                <div class="md:hidden flex items-center">
                    <button id="mobile-menu-btn" class="text-slate-800 p-2.5 rounded-xl bg-slate-50 hover:bg-slate-100 transition-colors focus:outline-none">
                        <div class="flex items-center space-x-2">
                            <span class="text-xs font-bold uppercase tracking-wider text-slate-600">Menu</span>
                            <i class="fa-solid fa-bars text-lg text-peroduaDark"></i>
                        </div>
                    </button>
                </div>
            </div>
        </div>

        <!-- Mobile Menu Container -->
        <div id="mobile-menu" class="hidden md:hidden bg-white border-t border-slate-100 px-4 py-6 space-y-4 shadow-xl transition-all duration-300 animate-fadeIn">
            <a href="{home_path}" class="{get_mobile_class('home')}">Home</a>
            <a href="{feedback_path}" class="{get_mobile_class('feedback')}">Feedback Customer</a>
            <a href="{about_path}" class="{get_mobile_class('about')}">About Me</a>
            <div class="text-[10px] text-slate-400 font-bold tracking-widest uppercase pt-2">Car Model Options</div>
            <div class="grid grid-cols-2 gap-2">
                <a href="{alza_path}" class="bg-slate-50 p-3 rounded-xl text-xs font-bold text-center text-slate-700 block hover:bg-peroduaDark hover:text-white transition-all">Alza</a>
                <a href="{ativa_path}" class="bg-slate-50 p-3 rounded-xl text-xs font-bold text-center text-slate-700 block hover:bg-peroduaDark hover:text-white transition-all">Ativa</a>
                <a href="{myvi_path}" class="bg-slate-50 p-3 rounded-xl text-xs font-bold text-center text-slate-700 block hover:bg-peroduaDark hover:text-white transition-all">Myvi</a>
                <a href="{aruz_path}" class="bg-slate-50 p-3 rounded-xl text-xs font-bold text-center text-slate-700 block hover:bg-peroduaDark hover:text-white transition-all">Aruz</a>
                <a href="{axia_path}" class="bg-slate-50 p-3 rounded-xl text-xs font-bold text-center text-slate-700 block hover:bg-peroduaDark hover:text-white transition-all">Axia</a>
                <a href="{bezza_path}" class="bg-slate-50 p-3 rounded-xl text-xs font-bold text-center text-slate-700 block hover:bg-peroduaDark hover:text-white transition-all">Bezza</a>
                <a href="{traz_path}" class="bg-slate-50 p-3 rounded-xl text-xs font-bold text-center text-slate-700 block hover:bg-peroduaDark hover:text-white transition-all">Traz</a>
            </div>
            <a href="https://wa.me/60176503339?text=Hi%2C%20saya%20berminat%20untuk%20membeli%20kereta%20Perodua.%20Boleh%20saya%20dapatkan%20maklumat%20lanjut%20mengenai%20model%20dan%20promosi%20terkini%3F" class="w-full bg-emerald-500 text-white font-bold py-3.5 rounded-xl flex items-center justify-center space-x-2 shadow-lg shadow-emerald-500/20 active:scale-95 transition-all">
                <i class="fa-brands fa-whatsapp text-xl"></i> <span>Contact Akmal</span>
            </a>
        </div>
    </header>"""

def process_file(filepath, prefix, active_page):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find the optional top announcement bar and the header
    pattern = r'(?:(?:<!--.*?-->\s*)?<div[^>]*class="[^"]*brandSlate[^"]*"[^>]*>.*?</div>\s*)?(?:<!--.*?-->\s*)?<header[^>]*>.*?</header>'
    
    navbar_html = get_navbar(prefix, active_page)
    
    # Let's perform replacement
    new_content, count = re.subn(pattern, navbar_html, content, flags=re.DOTALL)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath} ({active_page})")
    else:
        print(f"Could not find navbar in {filepath}")

def main():
    # Root pages
    process_file(os.path.join(ROOT_DIR, "index.html"), "", "home")
    process_file(os.path.join(ROOT_DIR, "about.html"), "", "about")
    process_file(os.path.join(ROOT_DIR, "feedback.html"), "", "feedback")
    
    # Model pages
    model_files = glob.glob(os.path.join(MODELS_DIR, "*.html"))
    for filepath in model_files:
        process_file(filepath, "../", "cars")

if __name__ == "__main__":
    main()
