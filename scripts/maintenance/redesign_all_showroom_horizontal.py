import os
import re

ROOT_DIR = r"c:\xampps\htdocs\public_html"
MODELS_DIR = os.path.join(ROOT_DIR, "models")

SLIDER_FILES = [
    os.path.join(MODELS_DIR, "bezza.html"),
    os.path.join(MODELS_DIR, "axia.html"),
    os.path.join(MODELS_DIR, "axia1.html"),
    os.path.join(MODELS_DIR, "traz.html"),
]

GRID_FILES = [
    os.path.join(MODELS_DIR, "myvi.html"),
    os.path.join(MODELS_DIR, "ativa.html"),
    os.path.join(MODELS_DIR, "aruz.html"),
    os.path.join(MODELS_DIR, "aruzz.html"),
]

def clean_html(text):
    text = re.sub(r'<[^<]+?>', '', text) # strip tags
    text = text.replace("&nbsp;", " ").replace("&amp;", "&")
    return text.strip()

def extract_loan_val(card_html, term):
    term_idx = card_html.lower().find(term.lower())
    if term_idx == -1:
        return "RM 0.00"
    text_after = card_html[term_idx:]
    val_match = re.search(r'>\s*((?:RM\s*)?\d+(?:,\d+)*(?:\.\d+)?)\s*</', text_after)
    if val_match:
        val = val_match.group(1).strip()
        if not val.startswith("RM"):
            val = "RM " + val
        return val
    digit_match = re.search(r'(?:RM\s*)?(\d+(?:,\d+)*(?:\.\d+)?)', text_after)
    if digit_match:
        return "RM " + digit_match.group(1).strip()
    return "RM 0.00"

def build_horizontal_panel(var_data):
    trans_badge_html = ""
    if var_data['transmission']:
        trans_badge_html = f"<span class=\"inline-block px-2 py-0.5 rounded text-[9px] font-bold font-mono tracking-wider bg-white/10 text-slate-300 border border-white/5 mt-1 uppercase\">{var_data['transmission']}</span>"

    specs_html = ""
    for i, (label, val) in enumerate(var_data['specs']):
        is_otr = "otr" in label.lower()
        if is_otr:
            continue
        
        specs_html += f"""                                <div class="flex justify-between py-1 border-b border-white/5">
                                    <span class="text-slate-400">{label}</span>
                                    <span class="font-bold text-white">{val}</span>
                                </div>\n"""

    otr_label, otr_val = "OTR Price", "RM 0.00"
    for label, val in var_data['specs']:
        if "otr" in label.lower():
            otr_label = label
            otr_val = val
            break

    panel_markup = f"""                    <!-- Panel: {var_data['title']} -->
                    <div class="bg-slate-950/40 backdrop-blur-md border border-white/10 rounded-[2.5rem] p-6 lg:p-8 hover:border-emerald-500/20 transition duration-300 shadow-2xl flex flex-col lg:flex-row gap-6 lg:gap-10 items-center justify-between group">
                        
                        <!-- Col 1: Title, Badge & Car Image (Left) -->
                        <div class="w-full lg:w-1/4 flex flex-col items-center lg:items-start text-center lg:text-left space-y-4">
                            <div>
                                <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-[10px] font-bold tracking-wider uppercase">
                                    <span class="w-1 h-1 rounded-full bg-emerald-400 animate-pulse"></span>
                                    {var_data['badge']}
                                </span>
                                <h3 class="text-2xl font-black text-white mt-2 tracking-tight">{var_data['title']}</h3>
                                {trans_badge_html}
                            </div>
                            
                            <!-- Image Container -->
                            <div class="relative w-full h-36 bg-slate-950/60 border border-white/5 rounded-2xl p-2 flex items-center justify-center overflow-hidden">
                                <div class="absolute w-24 h-24 bg-emerald-500/10 rounded-full blur-[40px] -z-10 group-hover:scale-115 transition duration-700 pointer-events-none"></div>
                                <img src="{var_data['img_src']}" alt="{var_data['title']}" class="max-h-full object-contain transition duration-500 group-hover:scale-105 relative z-10" onerror="this.src='https://via.placeholder.com/450x280/151921/ffffff?text={var_data['title'].replace(' ', '+')}';">
                            </div>
                            <p class="text-slate-400 text-[11px] font-medium">{var_data['subtitle']}</p>
                        </div>

                        <!-- Col 2: Specs Grid (Middle) -->
                        <div class="w-full lg:w-5/12 bg-white/5 border border-white/10 rounded-[2rem] p-5 md:p-6 shadow-inner text-xs space-y-3.5">
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-x-6 gap-y-2.5 text-slate-300">
{specs_html}                            </div>
                            
                            <div class="flex justify-between items-center pt-2.5 border-t border-white/10">
                                <span class="text-slate-300 font-extrabold uppercase tracking-wider text-[10px]">{otr_label}</span>
                                <span class="font-black text-emerald-400 text-base md:text-lg tracking-tight">{otr_val}</span>
                            </div>
                        </div>

                        <!-- Col 3: Loan Estimators & Actions (Right) -->
                        <div class="w-full lg:w-1/4 flex flex-col justify-between space-y-4">
                            <!-- Loan Plans -->
                            <div class="grid grid-cols-2 lg:grid-cols-1 gap-3">
                                <div class="relative overflow-hidden bg-white/5 border border-white/10 rounded-xl p-3 text-left">
                                    <div class="absolute left-0 top-0 bottom-0 w-1 bg-perodua"></div>
                                    <div class="text-[8px] text-slate-400 font-extrabold uppercase tracking-widest">Monthly (10% Dep)</div>
                                    <div class="text-base text-white font-black mt-0.5">{var_data['monthly_val']}</div>
                                    <div class="text-[8px] text-perodua font-bold uppercase mt-0.5 tracking-wider">9 Years Tenure</div>
                                </div>
                                <div class="relative overflow-hidden bg-white/5 border border-white/10 rounded-xl p-3 text-left">
                                    <div class="absolute left-0 top-0 bottom-0 w-1 bg-emerald-400"></div>
                                    <div class="text-[8px] text-slate-400 font-extrabold uppercase tracking-widest">Full Loan Option</div>
                                    <div class="text-base text-white font-black mt-0.5">{var_data['full_val']}</div>
                                    <div class="text-[8px] text-emerald-400 font-bold uppercase mt-0.5 tracking-wider">9 Years Tenure</div>
                                </div>
                            </div>

                            <!-- CTAs -->
                            <div class="grid grid-cols-2 gap-3">
                                <a href="{var_data['details_link']}" class="w-full flex items-center justify-center bg-transparent border border-white/20 text-white hover:bg-white hover:text-slate-950 font-bold py-2.5 px-3 rounded-full text-center text-xs transition duration-300">
                                    Details
                                </a>
                                <a href="{var_data['book_link']}" class="w-full flex items-center justify-center bg-perodua text-slate-950 hover:bg-emerald-400 font-black py-2.5 px-3 rounded-full text-center text-xs transition duration-300 shadow-md">
                                    Book Now
                                </a>
                            </div>
                        </div>

                    </div>"""
    return panel_markup

def parse_slider_slide(slide_html):
    img_match = re.search(r'<img\s+([^>]+)>', slide_html)
    img_src = ""
    if img_match:
        src_match = re.search(r'src="([^"]+)"', img_match.group(1))
        img_src = src_match.group(1) if src_match else ""
        
    badge_match = re.search(r'<span class="bg-slate-700 text-white[^"]*">([^<]+)</span>', slide_html)
    if not badge_match:
        badge_match = re.search(r'<span class="bg-gradient-to-r[^"]*">([^<]+)</span>', slide_html)
    if not badge_match:
        badge_match = re.search(r'<span class="bg-perodua text-slate-950[^"]*">([^<]+)</span>', slide_html)
    badge = badge_match.group(1).strip() if badge_match else "Variant"

    title_match = re.search(r'<h2 class="[^"]*">([^<]+)(?:<span class="[^"]*">([^<]+)</span>)?</h2>', slide_html)
    title = "Model"
    transmission = ""
    if title_match:
        title_full = title_match.group(1).strip()
        if "<span" in title_full:
            parts = title_full.split("<span")
            title = parts[0].strip()
            trans_match = re.search(r'>([^<]+)</span>', title_full)
            transmission = trans_match.group(1).strip() if trans_match else ""
        else:
            title = title_full
            transmission = title_match.group(2).strip() if title_match.group(2) else ""
            
    transmission = transmission.replace("[", "").replace("]", "").strip()

    sub_match = re.search(r'<p class="text-gray-400[^"]*">([^<]+)</p>', slide_html)
    subtitle = sub_match.group(1).strip() if sub_match else ""

    row_pattern = r'<div class="flex justify-between border-b[^"]*">(.*?)</div>'
    specs = []
    for row_content in re.findall(row_pattern, slide_html, re.DOTALL):
        spans = re.findall(r'<span[^>]*>(.*?)</span>', row_content, re.DOTALL)
        if len(spans) >= 2:
            label = clean_html(spans[0])
            value = clean_html(spans[1])
            if not value:
                text_after = re.sub(r'<span[^>]*>.*?</span>', '', row_content, count=2)
                value = clean_html(text_after)
            specs.append((label, value))
        elif len(spans) == 1:
            label = clean_html(spans[0])
            text_after = re.sub(r'<span[^>]*>.*?</span>', '', row_content, count=1)
            value = clean_html(text_after)
            specs.append((label, value))

    monthly_val = extract_loan_val(slide_html, "Monthly")
    full_val = extract_loan_val(slide_html, "Full Loan")

    details_link_match = re.search(r'<a\s+href="([^"]+)"[^>]*>View Details</a>', slide_html)
    details_link = details_link_match.group(1) if details_link_match else "#"
    
    book_link_match = re.search(r'<a\s+href="([^"]+)"[^>]*>Book Now</a>', slide_html)
    book_link = book_link_match.group(1) if book_link_match else "#"

    return {
        "img_src": img_src,
        "badge": badge,
        "title": title,
        "transmission": transmission,
        "subtitle": subtitle,
        "specs": specs,
        "monthly_val": monthly_val,
        "full_val": full_val,
        "details_link": details_link,
        "book_link": book_link
    }

def parse_grid_card(card_html):
    img_match = re.search(r'<img\s+([^>]+)>', card_html)
    img_src = ""
    if img_match:
        src_match = re.search(r'src="([^"]+)"', img_match.group(1))
        img_src = src_match.group(1) if src_match else ""

    badge_match = re.search(r'<span class="bg-slate-700 px-4 py-1 rounded-full text-\[10px\] font-bold uppercase">\s*([^<]+)\s*</span>', card_html)
    if not badge_match:
        badge_match = re.search(r'<span class="bg-emerald-500 text-black px-4 py-1 rounded-full text-\[10px\] font-black uppercase">\s*([^<]+)\s*</span>', card_html)
    badge = badge_match.group(1).strip() if badge_match else "Variant"

    title_match = re.search(r'<h3 class="[^"]*">\s*([^\s<][^<]*)\s*</h3>', card_html, re.DOTALL)
    title = "Model"
    transmission = ""
    if title_match:
        title_full = title_match.group(1).strip()
        title_full = re.sub(r'\s+', ' ', title_full)
        if "[" in title_full:
            parts = title_full.split("[")
            title = parts[0].strip()
            transmission = parts[1].replace("]", "").strip()
        elif "CVT" in title_full:
            title = title_full.replace("CVT", "").strip()
            transmission = "CVT"
        else:
            title = title_full

    sub_match = re.search(r'<p class="text-slate-400 text-sm mt-1">\s*([^<]+)\s*</p>', card_html)
    subtitle = sub_match.group(1).strip() if sub_match else ""

    row_pattern = r'<div class="flex justify-between items-center border-b border-dashed border-gray-200 pb-2">(.*?)</div>'
    matched_rows = re.findall(row_pattern, card_html, re.DOTALL)
    if not matched_rows:
        row_pattern_alt = r'<div class="flex justify-between bg-black/30 p-3 rounded-xl">(.*?)</div>'
        matched_rows = re.findall(row_pattern_alt, card_html, re.DOTALL)
        
    specs = []
    for row_content in matched_rows:
        spans = re.findall(r'<span[^>]*>(.*?)</span>', row_content, re.DOTALL)
        if len(spans) >= 2:
            label = clean_html(spans[0])
            value = clean_html(spans[1])
            specs.append((label, value))
        elif len(spans) == 0:
            plain_spans = re.findall(r'<span>(.*?)</span>', row_content)
            if len(plain_spans) >= 1:
                label = plain_spans[0].strip()
                val_match = re.search(r'<span class="[^"]*">(.*?)</span>', row_content)
                value = val_match.group(1).strip() if val_match else ""
                specs.append((label, value))

    price_block_match = re.search(r'<div class="mt-5 bg-emerald-500 text-black rounded-2xl p-5">.*?<p class="text-3xl font-black">([^<]+)</p>', card_html, re.DOTALL)
    if price_block_match:
        otr_val = price_block_match.group(1).strip()
        specs.append(("OTR Price", otr_val))

    monthly_val = extract_loan_val(card_html, "Monthly")
    full_val = extract_loan_val(card_html, "Full Loan")

    details_link_match = re.search(r'<a\s+href="([^"]+)"[^>]*>View</a>', card_html)
    if not details_link_match:
        details_link_match = re.search(r'<a\s+href="([^"]+)"[^>]*>View Details</a>', card_html)
    details_link = details_link_match.group(1) if details_link_match else "#"
    
    book_link_match = re.search(r'<a\s+href="([^"]+)"[^>]*>Book</a>', card_html)
    if not book_link_match:
        book_link_match = re.search(r'<a\s+href="([^"]+)"[^>]*>Book Now</a>', card_html)
    book_link = book_link_match.group(1) if book_link_match else "#"

    return {
        "img_src": img_src,
        "badge": badge,
        "title": title,
        "transmission": transmission,
        "subtitle": subtitle,
        "specs": specs,
        "monthly_val": monthly_val,
        "full_val": full_val,
        "details_link": details_link,
        "book_link": book_link
    }

def process_slider_file(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    wrapper_match = re.search(r'<div class="swiper-wrapper">(.*?)</div>\s*</div>\s*<!-- Pagination -->', content, re.DOTALL)
    if not wrapper_match:
        wrapper_match = re.search(r'<div class="swiper-wrapper">(.*?)</div>\s*</div>\s*<div class="swiper-pagination">', content, re.DOTALL)
    if not wrapper_match:
        wrapper_match = re.search(r'<div class="swiper-wrapper">(.*?)</div>\s*</div>', content, re.DOTALL)
        
    if not wrapper_match:
        print(f"Skipping {os.path.basename(filepath)} - no swiper-wrapper found")
        return

    wrapper_html = wrapper_match.group(1)
    
    slides = re.split(r'<div class="swiper-slide">', wrapper_html)[1:]
    
    new_panels_html = ""
    for slide in slides:
        full_slide = '<div class="swiper-slide">' + slide
        try:
            var_data = parse_slider_slide(full_slide)
            panel_html = build_horizontal_panel(var_data)
            new_panels_html += panel_html + "\n\n"
        except Exception as e:
            print(f"Error parsing slider in {os.path.basename(filepath)}: {e}")
            return

    showroom_container_start = content.find('<div class="showroom-container')
    if showroom_container_start == -1:
        print(f"Could not find showroom-container in {os.path.basename(filepath)}")
        return
        
    showroom_section_end = content.find('</section>', showroom_container_start)
    if showroom_section_end == -1:
        print(f"Could not find closing section of showroom in {os.path.basename(filepath)}")
        return

    header_match = re.search(r'(<div class="text-center mb-[68]">.*?</div>)', content[showroom_container_start:showroom_section_end], re.DOTALL)
    header_html = header_match.group(1) if header_match else ""
    if not header_html:
        header_match = re.search(r'(<div class="text-center mb-[^"]*">.*?</div>)', content[showroom_container_start:showroom_section_end], re.DOTALL)
        header_html = header_match.group(1) if header_match else ""

    new_showroom_content = f"""<div class="showroom-container relative overflow-hidden rounded-[30px] bg-gradient-to-br from-slate-900 via-slate-950 to-slate-900 p-4 sm:p-6 md:p-10 shadow-2xl my-10 text-white">
                {header_html}
                
                <!-- Horizontal Panel Showcase (Spacious, Fully Visible, High-End Layout) -->
                <div class="space-y-8 mt-8">
{new_panels_html}                </div>
            </div>"""

    sub_content = content[showroom_container_start:showroom_section_end]
    last_div_idx = sub_content.rfind('</div>')
    if last_div_idx != -1:
        replace_target = content[showroom_container_start:showroom_container_start + last_div_idx + 6]
        new_content = content.replace(replace_target, new_showroom_content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully converted {os.path.basename(filepath)} to horizontal panels layout!")

def process_grid_file(filepath):
    if not os.path.exists(filepath):
        print(f"File {filepath} does not exist")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find grid container
    grid_match = re.search(r'(<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">.*?</div>\s*</div>\s*</section>)', content, re.DOTALL)
    if not grid_match:
        grid_match = re.search(r'(<div class="grid md:grid-cols-2 gap-10 relative z-10">.*?</div>\s*</section>)', content, re.DOTALL)
    if not grid_match:
        grid_match = re.search(r'(<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">.*?</div>\s*</div>)', content, re.DOTALL)
        
    if not grid_match:
        print(f"Could not find cards grid in {os.path.basename(filepath)}")
        return
        
    grid_html = grid_match.group(1)
    
    card_parts = re.split(r'<!--\s*Card', grid_html, flags=re.IGNORECASE)
    
    new_panels_html = ""
    for i, part in enumerate(card_parts[1:]):
        subparts = part.split('-->', 1)
        card_content_raw = subparts[1].strip()
        
        start_idx = card_content_raw.find('<div')
        end_idx = card_content_raw.rfind('</div>')
        if start_idx != -1 and end_idx != -1:
            card_div_html = card_content_raw[start_idx:end_idx + len('</div>')]
            try:
                var_data = parse_grid_card(card_div_html)
                panel_html = build_horizontal_panel(var_data)
                new_panels_html += panel_html + "\n\n"
            except Exception as e:
                print(f"Error parsing grid card in {os.path.basename(filepath)}: {e}")
                return

    # Check for showroom container (standard) or Aruz style <section>
    showroom_container_start = content.find('<div class="showroom-container')
    is_aruz_section = False
    if showroom_container_start == -1:
        showroom_container_start = content.find('<!-- SHOWROOM SECTION (NO SLIDER / PREMIUM GRID LAYOUT) -->')
        if showroom_container_start != -1:
            is_aruz_section = True
            showroom_container_start = content.find('<section', showroom_container_start)

    if showroom_container_start != -1:
        showroom_section_end = content.find('</section>', showroom_container_start)
        sub_content = content[showroom_container_start:showroom_section_end]
        last_div_idx = sub_content.rfind('</div>')
        if last_div_idx != -1:
            replace_target = content[showroom_container_start:showroom_container_start + last_div_idx + 6]
            
            header_match = re.search(r'(<div class="text-center mb-[^"]*">.*?</div>)', sub_content, re.DOTALL)
            header_html = header_match.group(1) if header_match else ""
            
            if is_aruz_section:
                new_showroom_content = f"""<section class="relative overflow-hidden rounded-[35px] bg-gradient-to-br from-slate-950 via-slate-900 to-black p-6 md:p-12 text-white my-10 shadow-2xl">
                    <!-- GLOW EFFECT -->
                    <div class="absolute top-[-180px] right-[-180px] w-[500px] h-[500px] bg-emerald-400/10 blur-[140px] rounded-full"></div>
                    <div class="absolute bottom-[-180px] left-[-180px] w-[500px] h-[500px] bg-emerald-300/10 blur-[160px] rounded-full"></div>
                    
                    {header_html}
                    
                    <!-- Horizontal Panel Showcase (Spacious, Fully Visible, High-End Layout) -->
                    <div class="space-y-8 mt-8">
{new_panels_html}                    </div>
                </section>"""
                replace_target = content[showroom_container_start:showroom_section_end + 10]
            else:
                new_showroom_content = f"""<div class="showroom-container relative overflow-hidden rounded-[30px] bg-gradient-to-br from-slate-900 via-slate-950 to-slate-900 p-4 sm:p-6 md:p-10 shadow-2xl my-10 text-white">
                    {header_html}
                    
                    <!-- Horizontal Panel Showcase (Spacious, Fully Visible, High-End Layout) -->
                    <div class="space-y-8 mt-8">
{new_panels_html}                    </div>
                </div>"""
                
            new_content = content.replace(replace_target, new_showroom_content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Successfully converted grid {os.path.basename(filepath)} to horizontal panels layout!")
    else:
        header_text = ""
        heading_match = re.search(r'(<div class="text-center mb-[^"]*">.*?</div>)\s*<div class="grid', content, re.DOTALL)
        if not heading_match:
            heading_match = re.search(r'(<div class="text-center mb-[^"]*">.*?</div>)\s*<!-- GRID', content, re.DOTALL)
            
        if heading_match:
            header_text = heading_match.group(1)
            content_without_header = content.replace(header_text, "")
            grid_match_updated = re.search(r'(<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">.*?</div>\s*</div>)', content_without_header, re.DOTALL)
            if grid_match_updated:
                grid_html_updated = grid_match_updated.group(1)
                new_showroom_content = f"""<div class="showroom-container relative overflow-hidden rounded-[30px] bg-gradient-to-br from-slate-900 via-slate-950 to-slate-900 p-4 sm:p-6 md:p-10 shadow-2xl my-10 text-white">
                    {header_text}
                    
                    <!-- Horizontal Panel Showcase (Spacious, Fully Visible, High-End Layout) -->
                    <div class="space-y-8 mt-8">
{new_panels_html}                    </div>
                </div>"""
                new_content = content_without_header.replace(grid_html_updated, new_showroom_content)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Successfully converted grid {os.path.basename(filepath)} to wrapped horizontal panels layout!")
        else:
            new_showroom_content = f"""<div class="showroom-container relative overflow-hidden rounded-[30px] bg-gradient-to-br from-slate-900 via-slate-950 to-slate-900 p-4 sm:p-6 md:p-10 shadow-2xl my-10 text-white">
                <div class="text-center mb-10">
                    <span class="bg-perodua text-slate-950 px-4 py-1.5 rounded-full text-[11px] font-bold tracking-widest uppercase shadow-md shadow-perodua/20">PREMIUM SHOWROOM</span>
                </div>
                
                <!-- Horizontal Panel Showcase (Spacious, Fully Visible, High-End Layout) -->
                <div class="space-y-8 mt-8">
{new_panels_html}                </div>
            </div>"""
            new_content = content.replace(grid_html, new_showroom_content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Successfully converted grid {os.path.basename(filepath)} to fallback horizontal panels layout!")

def main():
    for f in SLIDER_FILES:
        process_slider_file(f)
    for f in GRID_FILES:
        process_grid_file(f)

if __name__ == "__main__":
    main()
