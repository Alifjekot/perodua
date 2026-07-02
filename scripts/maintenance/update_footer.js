const fs = require('fs');

const newFooter = `    <footer class="bg-[#1f2125] text-white py-12 px-4 mt-auto">
        <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-12">
            <!-- Column 1: ALL PERODUA CARS -->
            <div>
                <h4 class="text-sm font-bold tracking-wider mb-6 border-b-2 border-white inline-block pb-1">ALL PERODUA
                    CARS</h4>
                <ul class="space-y-3 text-sm text-gray-300 font-medium">
                    <li><a href="ativa.html" class="hover:text-white transition-colors">PERODUA ATIVA</a></li>
                    <li><a href="myvi.html" class="hover:text-white transition-colors">PERODUA MYVI</a></li>
                    <li><a href="aruz.html" class="hover:text-white transition-colors">PERODUA ARUZ</a></li>
                    <li><a href="axia.html" class="hover:text-white transition-colors">PERODUA AXIA</a></li>
                    <li><a href="bezza.html" class="hover:text-white transition-colors">PERODUA BEZZA</a></li>
                    <li><a href="alza.html" class="hover:text-white transition-colors">PERODUA ALZA</a></li>
                </ul>
            </div>

            <!-- Column 2: CONTACT US -->
            <div>
                <h4 class="text-sm font-bold tracking-wider mb-6 border-b-2 border-white inline-block pb-1">CONTACT
                    AKMAL</h4>
                <div class="space-y-5 text-sm text-gray-300">
                    <div class="flex items-start space-x-4">
                        <i class="fa-solid fa-location-dot mt-1 text-xl text-white"></i>
                        <p class="leading-relaxed">14 & 16, Jalan Juruhebah U1/50, Temasya Industrial Park Phase 2,
                            40150 Shah Alam, Selangor</p>
                    </div>
                    <div class="flex items-center space-x-4">
                        <i class="fa-solid fa-phone text-xl text-white"></i>
                        <p>+60 19-365 0861</p>
                    </div>
                    <div class="flex items-center space-x-4">
                        <i class="fa-brands fa-whatsapp text-xl text-white"></i>
                        <p>+60 19-365 0861</p>
                    </div>
                </div>
            </div>

            <!-- Column 3: TIKTOK PAGE -->
            <div>
                <h4 class="text-sm font-bold tracking-wider mb-6 border-b-2 border-white inline-block pb-1">TIKTOK
                    PAGE</h4>
                <a href="https://www.tiktok.com" target="_blank"
                    class="block overflow-hidden rounded-md border border-gray-700 hover:border-gray-500 transition-colors group relative">
                    <img src="gambar/tiktok-page.png" alt="TikTok Page"
                        class="w-full h-auto object-cover group-hover:scale-105 transition-transform duration-500"
                        onerror="this.src='https://placehold.co/600x400/1e293b/ffffff?text=Letak+Gambar+TikTok+Sini'">
                    <div class="absolute inset-0 flex items-center justify-center bg-black/30 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                         <i class="fa-brands fa-tiktok text-4xl text-white"></i>
                    </div>
                </a>
            </div>
        </div>

        <div class="max-w-7xl mx-auto mt-12 pt-6 border-t border-gray-700 text-center text-xs text-gray-500">
            &copy; 2026 Perodua Glenmarie Sales Online. Designed for Performance.
        </div>
    </footer>`;

const files = fs.readdirSync('.').filter(f => f.endsWith('.html') || f === 'update_pages_detailed.js');

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    
    // Using a regex to match the entire footer tag and its content
    // <footer ...>...</footer>
    const footerRegex = /<footer[\s\S]*?<\/footer>/i;
    
    if (footerRegex.test(content)) {
        content = content.replace(footerRegex, newFooter);
        fs.writeFileSync(file, content, 'utf8');
        console.log('Updated footer in ' + file);
    }
});
