import os
import re
import glob

ROOT_DIR = r"c:\xampps\htdocs\public_html"
MODELS_DIR = os.path.join(ROOT_DIR, "models")

def replace_owner_details(content, is_model_page):
    prefix = "../" if is_model_page else ""
    
    # 1. Phone number replacements
    content = content.replace("60176503339", "60193650861")
    content = content.replace("017-650 3339", "019-365 0861")
    content = content.replace("017 650 3339", "019-365 0861")
    
    # 2. Website title/branding
    content = content.replace("Akmal Sales Online", "Ahmad Farhan Sales Online")
    
    # 3. Standardize contact name in strings
    content = content.replace("Contact Akmal", "Contact Farhan")
    content = content.replace("Contact Darundin", "Contact Farhan")
    content = content.replace("CONTACT AKMAL", "CONTACT FARHAN")
    
    # 4. Social Card replacements
    new_social_card = f"""<!-- Social Card -->
        <div>
            <h4 class="text-lg font-bold mb-6 text-white">
                Follow Ahmad Farhan
            </h4>
            <div class="bg-white/5 backdrop-blur-xl rounded-3xl p-5 border border-white/10">
                <img src="{prefix}customer/farhan.png"
                     class="rounded-2xl w-full object-cover"
                     alt="Ahmad Farhan"
                     onerror="this.src='https://placehold.co/300x300/1e293b/ffffff?text=Ahmad+Farhan'">
                <div class="mt-5">
                    <h5 class="font-bold text-lg text-center">
                        Ahmad Farhan
                    </h5>
                    <p class="text-slate-400 text-sm mt-1 mb-5 text-center">
                        Sales Advisor • Perodua Glenmarie
                    </p>
                    <ul class="example-2 mt-4">
                      <li class="icon-content">
                        <a
                          data-social="tiktok"
                          aria-label="TikTok"
                          href="https://vt.tiktok.com/ZSCu9fLnT/"
                          target="_blank"
                        >
                          <div class="filled"></div>
                          <i class="fa-brands fa-tiktok"></i>
                        </a>
                        <div class="tooltip">TikTok</div>
                      </li>
                      <li class="icon-content">
                        <a
                          data-social="instagram"
                          aria-label="Instagram"
                          href="https://www.instagram.com/farhann_1311?igsh=MW5lZHlpbTM5ams2cw=="
                          target="_blank"
                        >
                          <div class="filled"></div>
                          <i class="fa-brands fa-instagram"></i>
                        </a>
                        <div class="tooltip">Instagram</div>
                      </li>
                      <li class="icon-content">
                        <a
                          data-social="facebook"
                          aria-label="Facebook"
                          href="https://www.facebook.com/share/1DLLEJvmoB/?mibextid=wwXIfr"
                          target="_blank"
                        >
                          <div class="filled"></div>
                          <i class="fa-brands fa-facebook"></i>
                        </a>
                        <div class="tooltip">Facebook</div>
                      </li>
                      <li class="icon-content">
                        <a
                          data-social="whatsapp"
                          aria-label="WhatsApp"
                          href="https://wa.me/60193650861"
                          target="_blank"
                        >
                          <div class="filled"></div>
                          <i class="fa-brands fa-whatsapp"></i>
                        </a>
                        <div class="tooltip">WhatsApp</div>
                      </li>
                    </ul>
                </div>
            </div>
        </div>"""

    pattern = r'<!--\s*Social Card\s*-->\s*<div>\s*<h4[^>]*>\s*Follow Ahmad Farhan\s*</h4>.*?</div>\s*</div>\s*</div>'
    content, count = re.subn(pattern, new_social_card, content, flags=re.DOTALL)
    if count > 0:
        print(f"Replaced social card in a file.")
        
    # 5. General name replacements in context
    content = content.replace("Darudin Perodua", "Farhan Perodua")
    content = content.replace("Follow Darudin", "Follow Ahmad Farhan")
    content = content.replace("booking with Darudin", "booking with Ahmad Farhan")
    content = content.replace("alt=\"Darudin\"", "alt=\"Ahmad Farhan\"")
    content = content.replace("Darudin", "Ahmad Farhan")
    content = content.replace("Darundin", "Ahmad Farhan")
    content = content.replace("Akmal", "Ahmad Farhan")
    
    return content

def process_file(filepath, is_model_page):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content = replace_owner_details(content, is_model_page)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated owner details in {filepath}")
    else:
        print(f"No changes in {filepath}")

def main():
    # Root pages
    process_file(os.path.join(ROOT_DIR, "index.html"), False)
    process_file(os.path.join(ROOT_DIR, "about.html"), False)
    process_file(os.path.join(ROOT_DIR, "feedback.html"), False)
    
    # Model pages
    model_files = glob.glob(os.path.join(MODELS_DIR, "*.html"))
    for filepath in model_files:
        process_file(filepath, True)

if __name__ == "__main__":
    main()
