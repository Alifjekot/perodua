const fs = require('fs');
const path = require('path');

const dir = __dirname;

const cars = [
    {
        filename: 'alza.html',
        name: 'ALZA',
        image: 'letak-gambar-alza.png',
        variants: [
            { name: 'ALZA 1.5 X', otr: '64,589.87', down: '6,489.87', loan: '58,100.00', mth: '659.00', full: '733.00' },
            { name: 'ALZA 1.5 H', otr: '70,250.35', down: '7,050.35', loan: '63,200.00', mth: '717.00', full: '797.00' },
            { name: 'ALZA 1.5 AV', otr: '77,988.15', down: '7,888.15', loan: '70,100.00', mth: '796.00', full: '889.00' }
        ]
    },
    {
        filename: 'aruz.html',
        name: 'ARUZ',
        image: 'letak-gambar-aruz.png',
        variants: [
            { name: 'ARUZ 1.5 X [AUTO]', otr: '75,250.35', down: '7,550.35', loan: '67,700.00', mth: '768.00', full: '853.00' },
            { name: 'ARUZ 1.5 AV [AUTO]', otr: '80,338.15', down: '8,088.15', loan: '72,300.00', mth: '821.00', full: '911.00' }
        ]
    },
    {
        filename: 'ativa.html',
        name: 'ATIVA',
        image: 'letak-gambar-ativa.png',
        variants: [
            { name: 'ATIVA 1000 - X TURBO [METALLIC]', otr: '64,398.88', down: '6,498.88', loan: '57,900.00', mth: '657.00', full: '730.00' },
            { name: 'ATIVA 1000 - H TURBO [METALLIC]', otr: '69,296.93', down: '6,996.93', loan: '62,300.00', mth: '707.00', full: '785.00' },
            { name: 'ATIVA 1000 - AV TURBO [METALLIC]', otr: '74,745.31', down: '7,545.31', loan: '67,200.00', mth: '763.00', full: '848.00' }
        ]
    },
    {
        filename: 'bezza.html',
        name: 'BEZZA',
        image: 'letak-gambar-bezza.png',
        variants: [
            { name: 'BEZZA 1.0 G [MANUAL]', otr: '35,859.71', down: '3,659.71', loan: '32,200.00', mth: '387.00', full: '430.00' },
            { name: 'BEZZA 1.0 G [AUTO]', otr: '37,916.83', down: '3,816.83', loan: '34,100.00', mth: '410.00', full: '456.00' },
            { name: 'BEZZA 1.3 X [AUTO]', otr: '45,511.44', down: '4,611.44', loan: '40,900.00', mth: '492.00', full: '547.00' },
            { name: 'BEZZA 1.3 AV [AUTO]', otr: '51,682.89', down: '5,182.89', loan: '46,500.00', mth: '559.00', full: '620.00' }
        ]
    },
    {
        filename: 'myvi.html',
        name: 'MYVI',
        image: 'letak-gambar-myvi.png',
        variants: [
            { name: 'MYVI 1.3 G [AUTO]', otr: '48,105.75', down: '4,905.75', loan: '43,200.00', mth: '519.00', full: '578.00' },
            { name: 'MYVI 1.3 G [AUTO] + ASA', otr: '50,173.27', down: '5,073.27', loan: '45,100.00', mth: '542.00', full: '602.00' },
            { name: 'MYVI 1.5 X [AUTO] + ASA', otr: '52,684.42', down: '5,284.42', loan: '47,400.00', mth: '570.00', full: '632.00' },
            { name: 'MYVI 1.5 H [AUTO] + ASA', otr: '56,796.22', down: '5,696.22', loan: '51,100.00', mth: '614.00', full: '681.00' },
            { name: 'MYVI 1.5 AV [AUTO] + ASA', otr: '61,934.63', down: '6,234.63', loan: '55,700.00', mth: '669.00', full: '743.00' }
        ]
    },
    {
        filename: 'axia.html',
        name: 'AXIA',
        image: 'letak-gambar-axia.png',
        variants: [
            { name: 'AXIA 1.0 E [MANUAL]', otr: '22,900.00', down: '2,300.00', loan: '20,600.00', mth: '253.00', full: '283.00' },
            { name: 'AXIA 1.0 G [CVT]', otr: '39,983.64', down: '4,083.64', loan: '35,900.00', mth: '432.00', full: '481.00' },
            { name: 'AXIA 1.0 SE [CVT]', otr: '45,531.44', down: '4,631.44', loan: '40,900.00', mth: '492.00', full: '547.00' },
            { name: 'AXIA 1.0 AV [CVT]', otr: '51,202.89', down: '5,202.89', loan: '46,000.00', mth: '553.00', full: '615.00' }
        ]
    }
];

const getHtml = (car) => {
    let cards = car.variants.map((v, i) => `
            <!-- Card ${i + 1} -->
            <div class="bg-white rounded-2xl shadow-[0_8px_30px_rgb(0,0,0,0.08)] border border-gray-100 overflow-hidden flex flex-col hover:-translate-y-1 transition-transform duration-300">
                <div class="bg-slate-900 px-6 py-4 flex items-center justify-center min-h-[80px] text-center">
                    <h3 class="text-lg leading-tight font-black text-white tracking-wide uppercase">${v.name}</h3>
                </div>
                
                <div class="w-full h-44 bg-gray-50 flex items-center justify-center p-4 relative group">
                    <img src="${car.image}" alt="${v.name}" class="max-h-full object-contain relative z-10 transition-transform group-hover:scale-105" onerror="this.style.display='none'; document.getElementById('ph-${car.name.toLowerCase()}-${i}').style.display='flex';">
                    <div id="ph-${car.name.toLowerCase()}-${i}" class="absolute inset-0 hidden flex-col items-center justify-center bg-gray-50 border-b border-gray-100 text-center p-2 z-0">
                        <i class="fa-solid fa-car-side text-gray-300 text-4xl mb-2"></i>
                        <span class="text-[10px] text-gray-500 font-mono bg-gray-200 px-2 py-1 rounded">src="${car.image}"</span>
                    </div>
                </div>
                
                <div class="p-6 flex-grow flex flex-col space-y-3 bg-white">
                    <div class="flex justify-between items-center border-b border-dashed border-gray-200 pb-2">
                        <span class="text-gray-500 text-xs font-bold uppercase tracking-wider">OTR Price</span>
                        <span class="text-gray-900 font-black">RM ${v.otr}</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-dashed border-gray-200 pb-2">
                        <span class="text-gray-500 text-xs font-bold uppercase tracking-wider">Deposit (10%)</span>
                        <span class="text-gray-700 font-semibold">RM ${v.down}</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-dashed border-gray-200 pb-2">
                        <span class="text-gray-500 text-xs font-bold uppercase tracking-wider">Loan (90%)</span>
                        <span class="text-gray-700 font-semibold">RM ${v.loan}</span>
                    </div>
                    
                    <div class="pt-4 grid grid-cols-2 gap-3 mb-4">
                        <div class="bg-blue-50 p-3 rounded-xl text-center border border-blue-100">
                            <div class="text-[9px] text-blue-600 font-extrabold uppercase mb-1">Monthly (10% Dep)</div>
                            <div class="text-base text-blue-800 font-black">RM ${v.mth}</div>
                            <div class="text-[8px] text-blue-400 font-bold uppercase mt-1">9 Years</div>
                        </div>
                        <div class="bg-emerald-50 p-3 rounded-xl text-center border border-emerald-100">
                            <div class="text-[9px] text-emerald-600 font-extrabold uppercase mb-1">Full Loan</div>
                            <div class="text-base text-emerald-800 font-black">RM ${v.full}</div>
                            <div class="text-[8px] text-emerald-400 font-bold uppercase mt-1">9 Years</div>
                        </div>
                    </div>
                    
                    <div class="pt-2 mt-auto">
                        <a href="https://wa.me/60176503339" class="w-full flex items-center justify-center bg-perodua hover:bg-peroduaDark text-white font-bold py-3.5 px-4 rounded-xl transition-all shadow-md hover:shadow-lg">
                            <i class="fa-brands fa-whatsapp text-xl mr-2"></i> Booking Now
                        </a>
                    </div>
                </div>
            </div>`).join('');

    return `
    <section class="max-w-7xl mx-auto px-4 py-16 bg-slate-50">
        <div class="text-center mb-16">
            <span class="text-perodua text-xs font-extrabold tracking-widest uppercase bg-perodua/10 px-4 py-1.5 rounded-full mb-4 inline-block">Senarai Harga Terkini 2026</span>
            <h1 class="text-4xl md:text-5xl font-black text-gray-900 tracking-tight uppercase">PERODUA ${car.name}</h1>
            <p class="text-gray-500 mt-4 max-w-2xl mx-auto">Choose the Perodua ${car.name} variant that best suits your needs and budget. We offer very affordable monthly installments with a fast and easy loan approval process.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
${cards}
        </div>
    </section>

    <!-- Free Gift Banner -->
    <section class="max-w-7xl mx-auto px-4 pb-16">
        <div class="bg-gradient-to-r from-slate-900 to-slate-800 rounded-3xl p-8 md:p-12 shadow-2xl flex flex-col md:flex-row items-center justify-between overflow-hidden relative">
            <div class="absolute top-0 right-0 w-64 h-64 bg-perodua rounded-full opacity-10 blur-3xl transform translate-x-1/2 -translate-y-1/2"></div>
            
            <div class="text-center md:text-left z-10 md:w-2/3 mb-8 md:mb-0">
                <h2 class="text-3xl md:text-4xl font-black text-white mb-4">Tawaran Hebat & Free Gift!</h2>
                <p class="text-gray-300 text-lg">Setiap tempahan didatangkan dengan pelbagai hadiah percuma menarik. Kami juga menerima <span class="text-white font-bold bg-perodua px-2 py-0.5 rounded">TRADE-IN</span> kenderaan lama anda dengan harga yang tinggi.</p>
            </div>
            
            <div class="z-10 md:w-1/3 flex justify-center md:justify-end w-full">
                <a href="https://wa.me/60176503339" class="w-full sm:w-auto bg-white text-slate-900 hover:bg-gray-100 font-black py-4 px-8 rounded-full text-center transition-transform hover:scale-105 shadow-xl flex items-center justify-center">
                    <i class="fa-brands fa-whatsapp text-emerald-500 text-2xl mr-3"></i> 017-650 3339
                </a>
            </div>
        </div>
    </section>

        <footer class="bg-[#1f2125] text-white py-12 px-4 mt-auto">
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
};

for (const car of cars) {
    const filepath = path.join(dir, car.filename);
    if (!fs.existsSync(filepath)) {
        console.log(`File not found: ${car.filename}`);
        continue;
    }
    const content = fs.readFileSync(filepath, 'utf-8');

    // Replace everything between </header> and <script> (at the bottom)
    const regex = /(<\/header>)([\s\S]*?)(<script>)/;

    const match = content.match(regex);
    if (match) {
        const newContent = content.replace(regex, `$1\n${getHtml(car)}\n\n    $3`);
        fs.writeFileSync(filepath, newContent, 'utf-8');
        console.log(`Updated layout with full details for ${car.filename}`);
    } else {
        console.log(`Could not find replace point in ${car.filename}`);
    }
}

