const fs = require('fs');
const path = require('path');

const dir = __dirname;
const htmlFiles = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

const oldContentRegex = /<div class="bg-white p-2 rounded-md">[\s\S]*?<\/div>\s*<\/div>\s*<\/div>\s*<\/div>\s*<div class="max-w-7xl mx-auto mt-12 pt-6/m;

const replacement = `<a href="https://www.facebook.com" target="_blank" class="block overflow-hidden rounded-md border border-gray-700 hover:border-gray-500 transition-colors group">
                <img src="letak-gambar-facebook-anda.png" alt="Facebook Page" class="w-full h-auto object-cover group-hover:scale-105 transition-transform duration-500" onerror="this.src='https://placehold.co/600x400/1e293b/ffffff?text=Letak+Gambar+Facebook+Sini'">
            </a>
        </div>
    </div>
    
    <div class="max-w-7xl mx-auto mt-12 pt-6`;

for (const file of htmlFiles) {
    const filepath = path.join(dir, file);
    const content = fs.readFileSync(filepath, 'utf-8');

    const newContent = content.replace(oldContentRegex, replacement);

    if (newContent !== content) {
        fs.writeFileSync(filepath, newContent, 'utf-8');
        console.log(`Updated FB image placeholder in ${file}`);
    } else {
        console.log(`Could not find replace point in ${file}`);
    }
}
