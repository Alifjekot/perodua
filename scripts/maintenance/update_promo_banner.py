import os
import glob
import re

MODELS_DIR = r"c:\xampps\htdocs\public_html\models"

# The new highly impressive Uiverse-style promo card
NEW_PROMO_HTML = """            <div class="relative overflow-hidden rounded-[2.5rem] bg-slate-950/90 backdrop-blur-xl border border-emerald-500/10 shadow-[0_0_50px_rgba(16,185,129,0.1)] group/card">
                <!-- Glowing decorative background circles -->
                <div class="absolute -top-40 -right-40 w-[500px] h-[500px] bg-emerald-500/10 rounded-full blur-[140px] transition-transform duration-1000 group-hover/card:scale-110 pointer-events-none"></div>
                <div class="absolute -bottom-40 -left-40 w-[500px] h-[500px] bg-emerald-600/10 rounded-full blur-[140px] pointer-events-none"></div>

                <!-- Animated Background Glow -->
                <div class="absolute inset-0 bg-gradient-to-r from-emerald-500/5 via-transparent to-emerald-500/5 opacity-50 pointer-events-none"></div>

                <div class="px-8 md:px-16 py-16 flex flex-col lg:flex-row items-center justify-between gap-12 relative z-10">
                    <!-- LEFT: Content -->
                    <div class="lg:w-2/3 space-y-6 text-center lg:text-left">
                        <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-bold tracking-[0.2em] uppercase mb-2 animate-pulse">
                            <i class="fa-solid fa-gift"></i>
                            Special Promotion
                        </div>
                        
                        <h2 class="text-4xl md:text-5xl lg:text-6xl font-black text-white tracking-tight leading-tight">
                            Amazing Deals <br class="hidden sm:inline">
                            <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 via-teal-300 to-emerald-500">
                                & Free Gifts
                            </span>
                        </h2>
                        
                        <p class="text-slate-300 text-base md:text-lg leading-relaxed max-w-2xl">
                            Every Perodua car booking with <span class="text-emerald-400 font-bold">Ahmad Farhan</span> will receive exclusive free gifts. We also accept <span class="inline-block text-white font-extrabold bg-gradient-to-r from-emerald-500 to-teal-500 px-3.5 py-1 rounded-xl shadow-md shadow-emerald-500/20">TRADE-IN</span> with high value for your old car.
                        </p>
                        
                        <!-- Uiverse Glassmorphism Tags -->
                        <div class="flex flex-wrap gap-4 mt-8 justify-center lg:justify-start">
                            <div class="flex items-center gap-2.5 px-5 py-2.5 rounded-2xl bg-white/5 border border-white/5 hover:border-emerald-500/30 hover:bg-emerald-500/5 transition duration-300">
                                <span class="text-lg">🎁</span>
                                <span class="text-slate-300 text-sm font-semibold">Free Gifts</span>
                            </div>
                            <div class="flex items-center gap-2.5 px-5 py-2.5 rounded-2xl bg-white/5 border border-white/5 hover:border-emerald-500/30 hover:bg-emerald-500/5 transition duration-300">
                                <span class="text-lg">🚗</span>
                                <span class="text-slate-300 text-sm font-semibold">Trade-In Available</span>
                            </div>
                            <div class="flex items-center gap-2.5 px-5 py-2.5 rounded-2xl bg-white/5 border border-white/5 hover:border-emerald-500/30 hover:bg-emerald-500/5 transition duration-300">
                                <span class="text-lg">⚡</span>
                                <span class="text-slate-300 text-sm font-semibold">Fast Approval</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- RIGHT: Uiverse Button -->
                    <div class="lg:w-1/3 flex justify-center lg:justify-end w-full">
                        <a href="https://wa.me/60193650861?text=Hi%2C%20saya%20berminat%20untuk%20membeli%20kereta%20Perodua." 
                           class="relative overflow-hidden flex items-center gap-5 bg-slate-900 border-2 border-emerald-500 text-white font-extrabold py-5 px-8 rounded-3xl shadow-[0_0_30px_rgba(16,185,129,0.15)] hover:shadow-[0_0_50px_rgba(16,185,129,0.35)] transition duration-500 group/btn w-full sm:w-auto">
                            <!-- Button Hover Overlay -->
                            <div class="absolute inset-0 bg-emerald-500 opacity-0 group-hover/btn:opacity-10 transition duration-300"></div>
                            
                            <div class="w-12 h-12 rounded-xl bg-emerald-500 flex items-center justify-center text-slate-950 group-hover/btn:scale-110 group-hover/btn:rotate-6 transition duration-300 shadow-md">
                                <i class="fa-brands fa-whatsapp text-2xl"></i>
                            </div>
                            
                            <div class="text-left">
                                <p class="text-[9px] text-emerald-400 font-extrabold uppercase tracking-widest leading-none mb-1">WhatsApp Now</p>
                                <p class="text-lg font-black text-white leading-none">019-365 0861</p>
                            </div>
                        </a>
                    </div>
                </div>
            </div>"""

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Target the inner div wrapper block directly
    pattern = r'<div class="relative overflow-hidden rounded-\[45px\] bg-gradient-to-r from-slate-950 via-slate-900 to-slate-950 shadow-\[0_40px_120px_rgba\(0,0,0,0\.6\)\]">.*?Amazing Deals &.*?</a>\s*</div>\s*</div>\s*</div>'
    
    new_content, count = re.subn(pattern, NEW_PROMO_HTML, content, flags=re.DOTALL)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated promo div in {os.path.basename(filepath)}")
    else:
        # Fallback regex matching just the inner div wrapper
        pattern_fallback = r'<div class="relative overflow-hidden rounded-\[45px\] bg-gradient-to-r from-slate-950 via-slate-900 to-slate-950 shadow-\[0_40px_120px_rgba\(0,0,0,0\.6\)\]">.*?Amazing Deals &.*?</div>\s*</div>'
        new_content_fb, count_fb = re.subn(pattern_fallback, NEW_PROMO_HTML, content, flags=re.DOTALL)
        if count_fb > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content_fb)
            print(f"Updated promo div (fallback) in {os.path.basename(filepath)}")
        else:
            # Let's try matching via simple container class if already updated or has minor variants
            print(f"No div match found in {os.path.basename(filepath)}")

def main():
    html_files = glob.glob(os.path.join(MODELS_DIR, "*.html"))
    for filepath in html_files:
        update_file(filepath)

if __name__ == "__main__":
    main()
