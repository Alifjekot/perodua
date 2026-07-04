import os
import glob
import re

ROOT_DIR = r"c:\xampps\htdocs\public_html"
MODELS_DIR = os.path.join(ROOT_DIR, "models")

# List of files to process
TARGET_FILES = [
    os.path.join(MODELS_DIR, "alza.html"),
    os.path.join(MODELS_DIR, "ativa.html"),
    os.path.join(MODELS_DIR, "axia.html"),
    os.path.join(MODELS_DIR, "axia1.html"),
    os.path.join(MODELS_DIR, "bezza.html"),
    os.path.join(MODELS_DIR, "traz.html"),
]

def redesign_slide(slide_content):
    # Parse image info
    img_match = re.search(r'<img\s+([^>]+)>', slide_content)
    if not img_match:
        return slide_content
    img_attrs = img_match.group(1)
    
    # Extract src
    src_match = re.search(r'src="([^"]+)"', img_attrs)
    img_src = src_match.group(1) if src_match else ""
    
    # Extract alt
    alt_match = re.search(r'alt="([^"]+)"', img_attrs)
    img_alt = alt_match.group(1) if alt_match else ""
    
    # Extract onerror
    onerror_match = re.search(r'onerror="([^"]+)"', img_attrs)
    img_onerror = onerror_match.group(1) if onerror_match else ""
    onerror_attr = f' onerror="{img_onerror}"' if img_onerror else ''

    # Extract badge
    badge_match = re.search(r'<span class="bg-slate-700 text-white[^"]*">([^<]+)</span>', slide_content)
    if not badge_match:
        badge_match = re.search(r'<span class="bg-gradient-to-r[^"]*">([^<]+)</span>', slide_content)
    badge = badge_match.group(1).strip() if badge_match else "VARIANT"
    
    # Extract Title and Transmission
    title_match = re.search(r'<h2 class="[^"]*">([^<]+)(?:<span class="[^"]*">([^<]+)</span>)?</h2>', slide_content)
    title_without_trans = "Variant Title"
    transmission = ""
    if title_match:
        title_full = title_match.group(1).strip()
        transmission_raw = title_match.group(2).strip() if title_match.group(2) else ""
        
        # Clean title_full if it contains the span already (due to regex overlap)
        if "<span" in title_full:
            title_parts = title_full.split("<span")
            title_without_trans = title_parts[0].strip()
            # Try to get transmission from the inner span
            trans_match = re.search(r'>([^<]+)</span>', title_full)
            if trans_match:
                transmission = trans_match.group(1).strip()
        else:
            title_without_trans = title_full
            transmission = transmission_raw
            
    # Clean brackets from transmission
    transmission = transmission.replace("[", "").replace("]", "").strip()

    # Extract Subtitle
    sub_match = re.search(r'<p class="text-gray-400[^"]*">([^<]+)</p>', slide_content)
    subtitle = sub_match.group(1).strip() if sub_match else ""
    
    # Extract Table rows
    row_pattern = r'<div class="flex justify-between border-b[^"]*">(.*?)</div>'
    rows_data = []
    
    for row_content in re.findall(row_pattern, slide_content, re.DOTALL):
        spans = re.findall(r'<span[^>]*>(.*?)</span>', row_content, re.DOTALL)
        if len(spans) >= 2:
            label = re.sub('<[^<]+?>', '', spans[0]).strip()
            value = re.sub('<[^<]+?>', '', spans[1]).strip()
            # Remove trailing double spans or junk tags
            label = label.replace("</span>", "").strip()
            value = value.replace("</span>", "").strip()
            rows_data.append((label, value))

    # Format Table rows HTML beautifully
    table_rows_html = ""
    for i, (label, val) in enumerate(rows_data):
        is_otr = "otr" in label.lower()
        if is_otr:
            # Highlight OTR Price in a special row
            table_rows_html += f"""          <div class="flex justify-between items-center py-3 border-b border-white/5">
              <span class="text-slate-300 font-bold text-xs uppercase tracking-wider">{label}</span>
              <span class="font-black text-emerald-400 text-sm md:text-base tracking-tight">{val}</span>
          </div>\n"""
        else:
            # Standard row
            is_last = (i == len(rows_data) - 1)
            border_cls = "" if is_last else "border-b border-white/5"
            table_rows_html += f"""          <div class="flex justify-between items-center py-2.5 {border_cls}">
              <span class="text-slate-400 text-xs font-semibold tracking-wide uppercase">{label}</span>
              <span class="font-bold text-white text-xs md:text-sm">{val}</span>
          </div>\n"""

    # Extract Monthly values
    monthly_match = re.search(r'Monthly \([^)]+\)</div>\s*<div class="[^"]*">([^<]+)</div>', slide_content, re.IGNORECASE)
    if not monthly_match:
        monthly_match = re.search(r'Monthly \([^)]+\)</div>\s*<p class="[^"]*">([^<]+)</p>', slide_content, re.IGNORECASE)
    monthly_val = monthly_match.group(1).strip() if monthly_match else "RM 0.00"
    
    # Extract Full Loan values
    full_match = re.search(r'Full Loan</div>\s*<div class="[^"]*">([^<]+)</div>', slide_content, re.IGNORECASE)
    if not full_match:
        full_match = re.search(r'Full Loan</div>\s*<p class="[^"]*">([^<]+)</p>', slide_content, re.IGNORECASE)
    full_val = full_match.group(1).strip() if full_match else "RM 0.00"

    # Extract Links
    details_link_match = re.search(r'<a\s+href="([^"]+)"[^>]*>View Details</a>', slide_content)
    details_link = details_link_match.group(1) if details_link_match else "#"
    
    book_link_match = re.search(r'<a\s+href="([^"]+)"[^>]*>Book Now</a>', slide_content)
    book_link = book_link_match.group(1) if book_link_match else "#"

    # Format Transmission Badge if present
    trans_badge_html = ""
    if transmission:
        trans_badge_html = f"""<span class="inline-block px-2 py-0.5 rounded text-[10px] font-bold font-mono tracking-wider bg-white/10 text-slate-300 border border-white/5 uppercase">{transmission}</span>"""

    # Build the brand new premium slide HTML
    new_html = f"""                        <div class="swiper-slide">
                            <div class="flex flex-col lg:grid lg:grid-cols-2 gap-6 lg:gap-12 items-center">
                                
                                <!-- Right image panel (Clean visual container) -->
                                <div class="w-full lg:order-2 relative flex items-center justify-center p-6 bg-slate-950/40 backdrop-blur-md border border-white/10 rounded-[2.5rem] overflow-hidden group min-h-[180px] sm:min-h-[240px] md:min-h-[300px] shadow-2xl">
                                    <div class="absolute w-60 h-60 bg-emerald-500/10 rounded-full blur-[80px] -z-10 group-hover:scale-115 transition duration-700 pointer-events-none"></div>
                                    <img src="{img_src}" alt="{img_alt}" class="w-full max-h-[160px] sm:max-h-[220px] md:max-h-[280px] object-contain transition duration-500 group-hover:scale-105 relative z-10"{onerror_attr}>
                                </div>

                                <!-- Left info panel (Sleek specs & payment plans) -->
                                <div class="w-full lg:order-1 space-y-6">
                                    <div class="flex items-center gap-3">
                                        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-[10px] font-bold tracking-wider uppercase">
                                            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                                            {badge}
                                        </span>
                                        {trans_badge_html}
                                    </div>
                                    
                                    <div>
                                        <h3 class="text-3xl sm:text-4xl md:text-5xl font-black text-white tracking-tight leading-none">{title_without_trans}</h3>
                                        <p class="text-slate-400 mt-2 text-xs sm:text-sm font-medium">{subtitle}</p>
                                    </div>

                                    <!-- Specs Table -->
                                    <div class="space-y-2.5 bg-white/5 border border-white/10 rounded-[2rem] p-5 md:p-6 shadow-inner">
{table_rows_html}                                    </div>

                                    <!-- Payment Plan Cards (Premium glass look) -->
                                    <div class="grid grid-cols-2 gap-4">
                                        <div class="relative overflow-hidden bg-white/5 border border-white/10 rounded-2xl p-4 transition-all duration-300 hover:bg-white/10">
                                            <div class="absolute left-0 top-0 bottom-0 w-1 bg-perodua"></div>
                                            <div class="text-[9px] text-slate-400 font-extrabold uppercase tracking-widest">Monthly (10% Dep)</div>
                                            <div class="text-xl text-white font-black mt-1">{monthly_val}</div>
                                            <div class="text-[9px] text-perodua font-bold uppercase mt-1 tracking-wider">9 Years Tenure</div>
                                        </div>
                                        
                                        <div class="relative overflow-hidden bg-white/5 border border-white/10 rounded-2xl p-4 transition-all duration-300 hover:bg-white/10">
                                            <div class="absolute left-0 top-0 bottom-0 w-1 bg-emerald-400"></div>
                                            <div class="text-[9px] text-slate-400 font-extrabold uppercase tracking-widest">Full Loan Option</div>
                                            <div class="text-xl text-white font-black mt-1">{full_val}</div>
                                            <div class="text-[9px] text-emerald-400 font-bold uppercase mt-1 tracking-wider">9 Years Tenure</div>
                                        </div>
                                    </div>

                                    <!-- Actions -->
                                    <div class="grid grid-cols-2 gap-4 pt-2">
                                        <a href="{details_link}" class="w-full flex items-center justify-center bg-transparent border border-white/20 text-white hover:bg-white hover:text-slate-950 font-bold py-3.5 px-4 rounded-full text-center text-xs md:text-sm transition duration-300 shadow-md">
                                            View Details
                                        </a>
                                        <a href="{book_link}" class="w-full flex items-center justify-center bg-perodua text-slate-950 hover:bg-emerald-400 font-black py-3.5 px-4 rounded-full text-center text-xs md:text-sm transition duration-300 shadow-lg shadow-perodua/10 hover:shadow-perodua/20">
                                            Book Now
                                        </a>
                                    </div>
                                </div>

                            </div>
                        </div>"""
    return new_html

def process_file(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (file does not exist)")
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find all swiper-slides
    # Since swiper-slide spans across lines, we can match from <div class="swiper-slide"> to next matching closure.
    # To do this reliably, we can search for blocks of slides.
    pattern = r'(<div class="swiper-slide">.*?</div>\s*</div>\s*</div>\s*</div>)'
    
    # A cleaner way is matching from <div class="swiper-slide"> to next <div class="swiper-slide"> or </div> (end of swiper-wrapper)
    # Let's locate the swiper-wrapper content
    wrapper_match = re.search(r'<div class="swiper-wrapper">(.*?)</div>\s*</div>\s*<!-- Pagination -->', content, re.DOTALL)
    if not wrapper_match:
        # try without comments
        wrapper_match = re.search(r'<div class="swiper-wrapper">(.*?)</div>\s*</div>\s*<div class="swiper-pagination">', content, re.DOTALL)
    if not wrapper_match:
        wrapper_match = re.search(r'<div class="swiper-wrapper">(.*?)</div>\s*</div>', content, re.DOTALL)
        
    if not wrapper_match:
        print(f"Could not find swiper-wrapper in {os.path.basename(filepath)}")
        return
        
    wrapper_html = wrapper_match.group(1)
    
    # Split slide blocks
    slides = re.split(r'<div class="swiper-slide">', wrapper_html)[1:] # drop prefix
    
    new_slides_html = ""
    for slide in slides:
        # Reconstruct slide markup for parser
        full_slide = '<div class="swiper-slide">' + slide
        # Parse and redesign
        try:
            redesigned = redesign_slide(full_slide)
            new_slides_html += redesigned + "\n\n"
        except Exception as e:
            print(f"Error parsing a slide in {os.path.basename(filepath)}: {e}")
            new_slides_html += full_slide + "\n\n"
            
    # Assemble back
    # We replace the old wrapper content with new slides html
    # To be extremely precise, replace wrapper_html directly
    new_wrapper_content = f'<div class="swiper-wrapper">\n\n{new_slides_html}</div>'
    
    # Replace in original content
    target_wrapper_pattern = r'<div class="swiper-wrapper">.*?</div>'
    new_content, count = re.subn(target_wrapper_pattern, new_wrapper_content, content, count=1, flags=re.DOTALL)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully redesigned variant cards in {os.path.basename(filepath)}")
    else:
        print(f"Failed to apply changes to {os.path.basename(filepath)}")

def main():
    for f in TARGET_FILES:
        process_file(f)

if __name__ == "__main__":
    main()
