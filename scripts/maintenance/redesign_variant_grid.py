import os
import glob
import re

ROOT_DIR = r"c:\xampps\htdocs\public_html"
MODELS_DIR = os.path.join(ROOT_DIR, "models")

# List of files to process
GRID_FILES = [
    os.path.join(MODELS_DIR, "myvi.html"),
    os.path.join(MODELS_DIR, "ativa.html"),
    os.path.join(MODELS_DIR, "aruz.html"),
    os.path.join(MODELS_DIR, "aruzz.html"),
]

def redesign_grid_card(card_html, placeholder_id):
    # Parse image tag info
    img_match = re.search(r'<img\s+([^>]+)>', card_html)
    if not img_match:
        return card_html
    img_attrs = img_match.group(1)
    
    img_src = re.search(r'src="([^"]+)"', img_attrs)
    img_src = img_src.group(1) if img_src else ""
    
    img_alt = re.search(r'alt="([^"]+)"', img_attrs)
    img_alt = img_alt.group(1) if img_alt else ""
    
    img_onerror = re.search(r'onerror="([^"]+)"', img_attrs)
    img_onerror = img_onerror.group(1) if img_onerror else ""
    onerror_attr = f' onerror="{img_onerror}"' if img_onerror else ''

    # Try to extract the title from the h3 tag
    title_match = re.search(r'<h3 class="[^"]*">([^<]+)(?:<span class="[^"]*">([^<]+)</span>)?</h3>', card_html, re.DOTALL)
    if not title_match:
        title_match = re.search(r'<h3 class="[^"]*">\s*([^\s<][^<]*)\s*</h3>', card_html, re.DOTALL)
    
    title_without_trans = "Variant Title"
    transmission = ""
    if title_match:
        title_full = title_match.group(1).strip()
        # Clean title if it contains newlines or extra tags
        title_full = re.sub(r'\s+', ' ', title_full).strip()
        if "[" in title_full:
            parts = title_full.split("[")
            title_without_trans = parts[0].strip()
            transmission = parts[1].replace("]", "").strip()
        else:
            title_without_trans = title_full
            transmission = ""
            
    # Extract Badge/Badge Text if any
    badge_match = re.search(r'<span class="bg-slate-700 px-4 py-1 rounded-full text-\[10px\] font-bold uppercase">\s*([^<]+)\s*</span>', card_html)
    badge = badge_match.group(1).strip() if badge_match else "VARIANT"

    # Extract Subtitle
    sub_match = re.search(r'<p class="text-slate-400 text-sm mt-1">\s*([^<]+)\s*</p>', card_html)
    subtitle = sub_match.group(1).strip() if sub_match else ""

    # Extract Table rows
    row_pattern = r'<div class="flex justify-between items-center border-b border-dashed border-gray-200 pb-2">(.*?)</div>'
    # Fallback for general flex justify-between inside list
    rows_data = []
    
    matched_rows = re.findall(row_pattern, card_html, re.DOTALL)
    if not matched_rows:
        # try simple bg-black/30 row pattern
        row_pattern_alt = r'<div class="flex justify-between bg-black/30 p-3 rounded-xl">(.*?)</div>'
        matched_rows = re.findall(row_pattern_alt, card_html, re.DOTALL)
        
    for row_content in matched_rows:
        spans = re.findall(r'<span[^>]*>(.*?)</span>', row_content, re.DOTALL)
        if len(spans) >= 2:
            label = re.sub('<[^<]+?>', '', spans[0]).strip()
            value = re.sub('<[^<]+?>', '', spans[1]).strip()
            rows_data.append((label, value))
        elif len(spans) == 0:
            # check simple text split by spans or div
            # like <span>Next Selling Price</span> <span class="font-bold">RM 72,540</span>
            plain_spans = re.findall(r'<span>(.*?)</span>', row_content)
            if len(plain_spans) >= 1:
                label = plain_spans[0].strip()
                # Find second span or value
                val_match = re.search(r'<span class="[^"]*">(.*?)</span>', row_content)
                value = val_match.group(1).strip() if val_match else ""
                rows_data.append((label, value))

    # Format Table rows HTML beautifully
    table_rows_html = ""
    for i, (label, val) in enumerate(rows_data):
        is_otr = "otr" in label.lower()
        if is_otr:
            # Highlight OTR Price in a special row
            table_rows_html += f"""                    <div class="flex justify-between items-center py-2.5 border-b border-slate-100">
                        <span class="text-slate-800 font-bold text-xs uppercase tracking-wider">{label}</span>
                        <span class="font-black text-emerald-600 text-sm md:text-base tracking-tight">{val}</span>
                    </div>\n"""
        else:
            # Standard row
            is_last = (i == len(rows_data) - 1)
            border_cls = "" if is_last else "border-b border-slate-100/80"
            table_rows_html += f"""                    <div class="flex justify-between items-center py-2 {border_cls}">
                        <span class="text-slate-400 text-xs font-semibold tracking-wide uppercase">{label}</span>
                        <span class="font-bold text-slate-700 text-xs md:text-sm">{val}</span>
                    </div>\n"""

    # Extract Monthly values
    monthly_match = re.search(r'Monthly \([^)]+\)</div>\s*<div class="[^"]*">([^<]+)</div>', card_html, re.IGNORECASE)
    if not monthly_match:
        monthly_match = re.search(r'Monthly \([^)]+\)</div>\s*<p class="[^"]*">([^<]+)</p>', card_html, re.IGNORECASE)
    monthly_val = monthly_match.group(1).strip() if monthly_match else "RM 0.00"
    
    # Extract Full Loan values
    full_match = re.search(r'Full Loan</div>\s*<div class="[^"]*">([^<]+)</div>', card_html, re.IGNORECASE)
    if not full_match:
        full_match = re.search(r'Full Loan</div>\s*<p class="[^"]*">([^<]+)</p>', card_html, re.IGNORECASE)
    full_val = full_match.group(1).strip() if full_match else "RM 0.00"

    # Extract Links
    details_link_match = re.search(r'<a\s+href="([^"]+)"[^>]*>View Details</a>', card_html)
    if not details_link_match:
        details_link_match = re.search(r'<a\s+href="([^"]+)"[^>]*>View More</a>', card_html)
    details_link = details_link_match.group(1) if details_link_match else "#"
    
    book_link_match = re.search(r'<a\s+href="([^"]+)"[^>]*>Book Now</a>', card_html)
    if not book_link_match:
        book_link_match = re.search(r'<a\s+href="([^"]+)"[^>]*>Booking Now</a>', card_html)
    book_link = book_link_match.group(1) if book_link_match else "#"

    # Format Transmission Badge if present
    trans_badge_html = ""
    if transmission:
        trans_badge_html = f"""<span class="inline-block px-2 py-0.5 rounded text-[9px] font-bold font-mono tracking-wider bg-slate-100 text-slate-600 border border-slate-200/60 mt-1.5 uppercase">{transmission}</span>"""

    # Build the redesigned card HTML
    new_card_html = f"""            <div class="bg-white rounded-[2rem] border border-slate-100 shadow-[0_12px_40px_rgba(0,0,0,0.04)] overflow-hidden flex flex-col hover:-translate-y-2 transition duration-300">
                
                <!-- Card Image (Clean backdrop) -->
                <div class="w-full h-48 bg-slate-50/80 rounded-t-2xl flex items-center justify-center p-4 relative group overflow-hidden border-b border-slate-100">
                    <div class="absolute w-40 h-40 bg-emerald-400/5 blur-[50px] rounded-full z-0 pointer-events-none"></div>
                    <img src="{img_src}" alt="{img_alt}" class="max-h-full object-contain relative z-10 transition duration-500 group-hover:scale-105"{onerror_attr}>
                </div>

                <!-- Info Body -->
                <div class="p-6 md:p-8 flex-grow flex flex-col space-y-5 bg-white">
                    <div class="flex justify-between items-start">
                        <div>
                            <h3 class="text-xl font-black text-slate-900 tracking-tight">{title_without_trans}</h3>
                            {trans_badge_html}
                        </div>
                        <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-600 text-[9px] font-bold tracking-wider uppercase">
                            <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
                            {badge}
                        </span>
                    </div>

                    <!-- Specs Table -->
                    <div class="space-y-2 bg-slate-50/50 border border-slate-100 rounded-2xl p-4 shadow-inner">
{table_rows_html}                    </div>

                    <!-- Payment Plan Cards (Clean glass look) -->
                    <div class="grid grid-cols-2 gap-3">
                        <div class="relative overflow-hidden bg-slate-50 border border-slate-100 rounded-xl p-3 text-center">
                            <div class="absolute left-0 top-0 bottom-0 w-1 bg-perodua"></div>
                            <div class="text-[8px] text-slate-400 font-extrabold uppercase tracking-widest">Monthly (10% Dep)</div>
                            <div class="text-base text-slate-800 font-black mt-1">{monthly_val}</div>
                            <div class="text-[8px] text-perodua font-bold uppercase mt-1 tracking-wider">9 Years</div>
                        </div>
                        
                        <div class="relative overflow-hidden bg-slate-50 border border-slate-100 rounded-xl p-3 text-center">
                            <div class="absolute left-0 top-0 bottom-0 w-1 bg-emerald-400"></div>
                            <div class="text-[8px] text-slate-400 font-extrabold uppercase tracking-widest">Full Loan Option</div>
                            <div class="text-base text-slate-800 font-black mt-1">{full_val}</div>
                            <div class="text-[8px] text-emerald-600 font-bold uppercase mt-1 tracking-wider">9 Years</div>
                        </div>
                    </div>

                    <!-- Actions -->
                    <div class="grid grid-cols-2 gap-3 pt-2">
                        <a href="{details_link}" class="w-full flex items-center justify-center bg-transparent border border-slate-200 text-slate-700 hover:bg-slate-900 hover:text-white font-bold py-3.5 px-4 rounded-full text-center text-xs md:text-sm transition duration-300">
                            View Details
                        </a>
                        <a href="{book_link}" class="w-full flex items-center justify-center bg-perodua text-slate-950 hover:bg-emerald-400 font-black py-3.5 px-4 rounded-full text-center text-xs md:text-sm transition duration-300 shadow-md">
                            Book Now
                        </a>
                    </div>
                </div>

            </div>"""
    return new_card_html

def process_grid_file(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (file does not exist)")
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the variant cards grid container block
    # It starts with a grid container and has cards inside.
    # We can match all the child blocks between <!-- Card X --> tags
    # Let's locate the outer grid container
    grid_match = re.search(r'(<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">.*?</div>\s*</div>\s*</section>)', content, re.DOTALL)
    if not grid_match:
        # try alternative column count or styles
        grid_match = re.search(r'(<div class="grid md:grid-cols-2 gap-10 relative z-10">.*?</div>\s*</section>)', content, re.DOTALL)
    if not grid_match:
        # general fallback
        grid_match = re.search(r'(<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">.*?</div>\s*</div>)', content, re.DOTALL)
        
    if not grid_match:
        print(f"Could not find cards grid in {os.path.basename(filepath)}")
        return
        
    grid_html = grid_match.group(1)
    
    # Split the grid block by card comments or wrappers
    # We split by '<!-- Card' to isolate each card block
    card_parts = re.split(r'<!--\s*Card', grid_html, flags=re.IGNORECASE)
    header_part = card_parts[0]
    
    new_cards_html = ""
    for i, part in enumerate(card_parts[1:]):
        # part is like '1 --> \n <div class="..." ... </div>'
        # Split number/description prefix
        subparts = part.split('-->', 1)
        comment_header = f"<!-- Card{subparts[0]}-->"
        card_content_raw = subparts[1].strip()
        
        # Find the card div content from first '<div' to last '</div>'
        start_idx = card_content_raw.find('<div')
        end_idx = card_content_raw.rfind('</div>')
        if start_idx != -1 and end_idx != -1:
            card_div_html = card_content_raw[start_idx:end_idx + len('</div>')]
            try:
                # Redesign the card div
                redesigned_card = redesign_grid_card(card_div_html, f"ph-{os.path.basename(filepath).replace('.html','')}-{i}")
                # Replace card_div_html with redesigned_card in card_content_raw
                redesigned_part = card_content_raw.replace(card_div_html, redesigned_card)
                new_cards_html += f"\n\n            {comment_header}\n            {redesigned_part}"
            except Exception as e:
                print(f"Error redesigning grid card in {os.path.basename(filepath)}: {e}")
                new_cards_html += f"\n\n            {comment_header}\n            {card_content_raw}"
        else:
            new_cards_html += f"\n\n            {comment_header}\n            {card_content_raw}"
            
    # Assemble back the grid html
    # Construct the new grid content
    new_grid_html = header_part + new_cards_html
    
    # Replace in original content
    new_content, count = content.replace(grid_html, new_grid_html), 1
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully redesigned grid cards in {os.path.basename(filepath)}")
    else:
        print(f"Failed to apply grid changes to {os.path.basename(filepath)}")

def main():
    for filepath in GRID_FILES:
        process_grid_file(filepath)

if __name__ == "__main__":
    main()
