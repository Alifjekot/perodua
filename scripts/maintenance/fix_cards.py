import os
import re
import glob

# The pattern we want to match is roughly:
# <div class="bg-gray-50 rounded-2xl p-6 border border-gray-100 hover:shadow-lg transition-shadow">
#     <div class="w-12 h-12 bg-white rounded-full flex items-center justify-center shadow-sm mb-4 text-perodua">
#         <i class="fa-solid fa-[icon] text-xl"></i>
#     </div>
#     <h3 class="font-bold text-gray-900 mb-2">[Title]</h3>
#     <p class="text-sm text-gray-500">[Desc]</p>
# </div>

html_files = glob.glob('c:/Users/user/Downloads/akmal perodua/*.html')

pattern = re.compile(
    r'<div class="bg-gray-50 rounded-2xl p-6 border border-gray-100 hover:shadow-lg transition-shadow">\s*'
    r'<div class="[^"]*w-12 h-12[^"]*">\s*'
    r'<i class="([^"]+)"></i>\s*'
    r'</div>\s*'
    r'<h3 class="font-bold text-gray-900 mb-2">([^<]+)</h3>\s*'
    r'<p class="text-sm text-gray-500">([^<]*)</p>\s*'
    r'</div>'
)

def replacer(match):
    icon_class = match.group(1)
    title = match.group(2)
    desc = match.group(3)
    
    # Try to make a nice filename
    filename = title.lower().replace(' ', '-').replace('"', '').replace('/', '-') + '.jpg'
    
    new_html = f'''<div class="bg-white rounded-2xl border border-gray-100 hover:shadow-xl transition-all overflow-hidden group flex flex-col h-full">
                        <div class="w-full h-40 bg-gray-50 relative flex items-center justify-center border-b border-gray-100 overflow-hidden">
                            <!-- Placeholder Icon -->
                            <i class="{icon_class.replace("text-xl", "text-4xl text-gray-300")} absolute z-0"></i>
                            <!-- Actual Image (hidden if not found) -->
                            <img src="gambar/{filename}" alt="{title}" class="w-full h-full object-cover relative z-10 transition-transform duration-500 group-hover:scale-105" onerror="this.style.opacity='0'">
                        </div>
                        <div class="p-6 flex-grow">
                            <h3 class="font-bold text-gray-900 mb-2">{title}</h3>
                            <p class="text-sm text-gray-500">{desc}</p>
                        </div>
                    </div>'''
    return new_html

total_replacements = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content, count = pattern.subn(replacer, content)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath} ({count} replacements)")
        total_replacements += count

print(f"Total feature cards updated: {total_replacements}")
