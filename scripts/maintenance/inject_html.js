const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

const mobileMenuHTML = `
                <div class="md:hidden flex items-center">
                    <button id="mobile-menu-btn" class="text-slate-700 p-2 rounded-lg hover:bg-slate-100 focus:outline-none">
                        <div class="flex items-center space-x-2">
                            <span class="text-xs font-bold uppercase tracking-wider text-slate-500">Menu</span>
                            <i class="fa-solid fa-bars text-xl"></i>
                        </div>
                    </button>
                </div>
            </div>
        </div>

        <div id="mobile-menu" class="hidden md:hidden bg-white border-t px-4 py-5 space-y-4 shadow-xl">
            <a href="index.html" class="block py-2 text-slate-600 hover:text-perodua font-bold border-b border-slate-50">Home</a>
            <a href="feedback.html" class="block py-2 text-slate-600 hover:text-perodua font-bold border-b border-slate-50">Feedback Customer</a>
            <a href="about.html" class="block py-2 text-slate-600 hover:text-perodua font-bold border-b border-slate-50">About Me</a>
            <div class="text-xs text-slate-400 font-bold tracking-wider uppercase">Car Model Options</div>
            <div class="grid grid-cols-2 gap-2">
                <a href="alza.html" class="bg-slate-50 p-3 rounded-xl text-xs font-semibold text-center text-slate-700 block hover:bg-perodua hover:text-white">Alza</a>
                <a href="ativa.html" class="bg-slate-50 p-3 rounded-xl text-xs font-semibold text-center text-slate-700 block hover:bg-perodua hover:text-white">Ativa</a>
                <a href="myvi.html" class="bg-slate-50 p-3 rounded-xl text-xs font-semibold text-center text-slate-700 block hover:bg-perodua hover:text-white">Myvi</a>
                <a href="aruz.html" class="bg-slate-50 p-3 rounded-xl text-xs font-semibold text-center text-slate-700 block hover:bg-perodua hover:text-white">Aruz</a>
                <a href="axia.html" class="bg-slate-50 p-3 rounded-xl text-xs font-semibold text-center text-slate-700 block hover:bg-perodua hover:text-white">Axia</a>
                <a href="bezza.html" class="bg-slate-50 p-3 rounded-xl text-xs font-semibold text-center text-slate-700 block hover:bg-perodua hover:text-white">Bezza</a>
                <a href="traz.html" class="bg-slate-50 p-3 rounded-xl text-xs font-semibold text-center text-slate-700 block hover:bg-perodua hover:text-white">Traz</a>
            </div>
            <a href="https://wa.me/60176503339?text=Hi%2C%20saya%20berminat%20untuk%20membeli%20kereta%20Perodua.%20Boleh%20saya%20dapatkan%20maklumat%20lanjut%20mengenai%20model%20dan%20promosi%20terkini%3F" class="w-full bg-emerald-500 text-white font-bold py-3 rounded-xl flex items-center justify-center space-x-2 shadow-md">
                <i class="fa-brands fa-whatsapp text-lg"></i> <span>Contact Akmal</span>
            </a>
        </div>
    </header>`;

let count = 0;
files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    
    if (!content.includes('id="mobile-menu"')) {
        // Find the closing nav and header tags and replace them
        const regex = /<\/nav>\s*<\/div>\s*<\/div>\s*<\/header>/g;
        if (regex.test(content)) {
            content = content.replace(regex, '</nav>' + mobileMenuHTML);
            fs.writeFileSync(file, content, 'utf8');
            count++;
            console.log('Fixed ' + file);
        } else {
            console.log('Regex did not match in ' + file);
        }
    }
});

console.log('Fixed ' + count + ' files.');
