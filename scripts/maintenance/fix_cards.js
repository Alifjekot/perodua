const fs = require('fs');

const dir = 'c:/Users/user/Downloads/akmal perodua';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

// Update regex to handle line breaks between tags and inside classes/tags
const pattern = /<div class="bg-gray-50 rounded-2xl p-6 border border-gray-100 hover:shadow-lg transition-shadow">\s*<div\s+class="[^"]*w-12 h-12[^"]*">\s*<i class="([^"]+)"><\/i>\s*<\/div>\s*<h3 class="font-bold text-gray-900 mb-2">([^<]+)<\/h3>\s*<p class="text-sm text-gray-500">([\s\S]*?)<\/p>\s*<\/div>/g;

let totalReplacements = 0;

for (const file of files) {
    const filepath = dir + '/' + file;
    let content = fs.readFileSync(filepath, 'utf8');
    
    let count = 0;
    const newContent = content.replace(pattern, (match, iconClass, title, desc) => {
        count++;
        // Clean up desc spacing
        desc = desc.replace(/\s+/g, ' ').trim();
        // Try to make a nice filename
        const filename = title.toLowerCase().replace(/ /g, '-').replace(/"/g, '').replace(/\//g, '-') + '.jpg';
        
        return '<div class="bg-white rounded-2xl border border-gray-100 hover:shadow-xl transition-all overflow-hidden group flex flex-col h-full">\n' +
               '    <div class="w-full h-40 bg-gray-50 relative flex items-center justify-center border-b border-gray-100 overflow-hidden">\n' +
               '        <!-- Placeholder Icon -->\n' +
               '        <i class="' + iconClass.replace('text-xl', 'text-4xl text-gray-300') + ' absolute z-0"></i>\n' +
               '        <!-- Actual Image (hidden if not found) -->\n' +
               '        <img src="gambar/' + filename + '" alt="' + title + '" class="w-full h-full object-cover relative z-10 transition-transform duration-500 group-hover:scale-105" onerror="this.style.opacity=\'0\'">\n' +
               '    </div>\n' +
               '    <div class="p-6 flex-grow">\n' +
               '        <h3 class="font-bold text-gray-900 mb-2">' + title + '</h3>\n' +
               '        <p class="text-sm text-gray-500">' + desc + '</p>\n' +
               '    </div>\n' +
               '</div>';
    });
    
    if (count > 0) {
        fs.writeFileSync(filepath, newContent, 'utf8');
        console.log('Updated ' + file + ' (' + count + ' replacements)');
        totalReplacements += count;
    }
}

console.log('Total feature cards updated: ' + totalReplacements);
