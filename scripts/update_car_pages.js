const fs = require('fs');
const path = require('path');

const BASE_DIR = path.resolve('c:/Users/user/Downloads/public_html');

const TAILWIND_CONFIG = `<script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        perodua: '#38bdf8',
                        peroduaDark: '#0284c7',
                        brandSlate: '#0f172a'
                    }
                }
            }
        }
    </script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css"/>
    <style>
        .showroom-container {
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            box-sizing: border-box;
        }

        .showroom-container *, .showroom-container ::before, .showroom-container ::after {
            box-sizing: border-box;
        }

        .mySwiper {
            width: 100%;
            height: auto;
        }

        .swiper-slide {
            height: auto;
            display: block;
        }

        .mySwiper .swiper-pagination-bullet {
            background: #ffffff !important;
            opacity: 0.3;
        }

        .mySwiper .swiper-pagination-bullet-active {
            background: #38bdf8 !important;
            opacity: 1;
            width: 24px;
            border-radius: 4px;
            transition: all 0.3s ease;
        }
    </style>`;

const SWIPER_INIT_SCRIPT = `<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', function() {
        new Swiper('.mySwiper', {
            loop: true,
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
        });
    });
</script>`;

const HEADER_HTML = `    <div class="bg-brandSlate text-white text-xs py-2 px-4 text-center sm:text-right sm:px-8 font-medium">
        <i class="fa-solid fa-location-dot text-perodua mr-1"></i> Glenmarie Branch
        <a href="https://wa.me/60176503339?text=Hi%2C%20saya%20berminat%20untuk%20membeli%20kereta%20Perodua.%20Boleh%20saya%20dapatkan%20maklumat%20lanjut%20mengenai%20model%20dan%20promosi%20terkini%3F" class="hover:text-perodua ml-2"><i class="fa-brands fa-whatsapp text-emerald-400 mr-1"></i> Contact Sales Advisor</a>
    </div>

    <header class="bg-white shadow-md sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-20 items-center">
                <div class="flex items-center space-x-3">
                    <a href="index.html" class="flex-shrink-0">
                        <img src="gambar/logo-perodua.png" alt="Perodua Logo" class="h-10 w-auto object-contain"
                            onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Perodua_logo.svg/512px-Perodua_logo.svg.png'">
                    </a>
                    <div class="hidden lg:block pl-3 border-l-2 border-slate-100">
                        <span class="font-bold text-base block text-brandSlate leading-none">Glenmarie Sales</span>
                        <span class="text-[10px] text-slate-400 font-bold uppercase tracking-widest">Authorized Branch</span>
                    </div>
                </div>

                <nav class="hidden md:flex space-x-8 items-center">
                    <a href="index.html" class="text-slate-600 hover:text-perodua font-medium">Home</a>

                    <div class="relative group">
                        <button class="text-perodua font-bold border-b-2 border-perodua flex items-center space-x-1 py-2 focus:outline-none transition-colors">
                            <span>Our Cars</span>
                            <i class="fa-solid fa-chevron-down text-[10px] transition-transform group-hover:rotate-180"></i>
                        </button>
                        <div class="absolute left-0 mt-0 w-60 bg-white border border-slate-100 rounded-xl shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50 py-2">
                            <a href="alza.html" class="flex items-center px-4 py-2.5 text-sm font-medium text-slate-700 hover:bg-slate-50 hover:text-perodua"><i class="fa-solid fa-car-side mr-3 text-slate-400"></i> NEW PERODUA ALZA</a>
                            <a href="ativa.html" class="flex items-center px-4 py-2.5 text-sm font-medium text-slate-700 hover:bg-slate-50 hover:text-perodua"><i class="fa-solid fa-car-side mr-3 text-slate-400"></i> PERODUA ATIVA</a>
                            <a href="myvi.html" class="flex items-center px-4 py-2.5 text-sm font-medium text-slate-700 hover:bg-slate-50 hover:text-perodua"><i class="fa-solid fa-car-side mr-3 text-slate-400"></i> PERODUA MYVI</a>
                            <a href="aruz.html" class="flex items-center px-4 py-2.5 text-sm font-medium text-slate-700 hover:bg-slate-50 hover:text-perodua"><i class="fa-solid fa-car-side mr-3 text-slate-400"></i> PERODUA ARUZ</a>
                            <a href="axia.html" class="flex items-center px-4 py-2.5 text-sm font-medium text-slate-700 hover:bg-slate-50 hover:text-perodua"><i class="fa-solid fa-car-side mr-3 text-slate-400"></i> PERODUA AXIA</a>
                            <a href="bezza.html" class="flex items-center px-4 py-2.5 text-sm font-medium text-slate-700 hover:bg-slate-50 hover:text-perodua"><i class="fa-solid fa-car-side mr-3 text-slate-400"></i> PERODUA BEZZA</a>
                            <a href="traz.html" class="flex items-center px-4 py-2.5 text-sm font-medium text-slate-700 hover:bg-slate-50 hover:text-perodua"><i class="fa-solid fa-car-side mr-3 text-slate-400"></i> PERODUA TRAZ</a>
                        </div>
                    </div>

                    <a href="feedback.html" class="text-slate-600 hover:text-perodua font-medium">Feedback Customer</a>
                    <a href="about.html" class="text-slate-600 hover:text-perodua font-medium">About Me</a>

                    <a href="https://wa.me/60176503339?text=Hi%2C%20saya%20berminat%20untuk%20membeli%20kereta%20Perodua.%20Boleh%20saya%20dapatkan%20maklumat%20lanjut%20mengenai%20model%20dan%20promosi%20terkini%3F" target="_blank"
                        class="bg-emerald-500 hover:bg-emerald-600 text-white font-bold px-5 py-2.5 rounded-xl flex items-center space-x-2 shadow-sm transition">
                        <i class="fa-brands fa-whatsapp text-lg"></i> <span>017-650 3339</span>
                    </a>
                </nav>

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

const SECTION_TEMPLATE = `
<section class="max-w-7xl mx-auto px-4 py-12">
            <div class="text-center mb-12">
                <span class="text-perodua text-xs font-extrabold tracking-widest uppercase bg-perodua/10 px-4 py-1.5 rounded-full mb-4 inline-block">Latest 2026 Price List</span>
                <h1 class="text-4xl md:text-5xl font-black text-gray-900 tracking-tight uppercase">PERODUA {model}</h1>
                <p class="text-gray-500 mt-4 max-w-2xl mx-auto">Choose the Perodua {model} variant that best suits your needs and budget. We offer very affordable monthly installments with a fast and easy loan approval process.</p>
            </div>

            <div class="relative overflow-hidden py-12 bg-gradient-to-tr from-cyan-50 via-sky-50 to-blue-100 rounded-[2.5rem] mb-12">
                <div class="absolute inset-0 bg-[radial-gradient(circle_at_top_right,_rgba(186,230,253,0.4),_transparent_50%)] pointer-events-none"></div>
                <div class="relative z-20 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div class="bg-white/80 backdrop-blur-xl rounded-[2.5rem] shadow-[0_40px_80px_rgba(14,165,233,0.08)] border border-white p-6 md:p-12 overflow-hidden relative">
                        <div class="text-center mb-12 relative z-10">
                            <span class="text-sky-600 text-xs font-black tracking-[0.25em] uppercase bg-white px-5 py-2 rounded-full mb-4 inline-block border border-sky-100 shadow-sm">Visualizer</span>
                            <h2 class="text-3xl md:text-5xl font-black text-slate-900 tracking-tight uppercase">Pilih Warna <span class="text-sky-500">{model}</span> Anda</h2>
                            <div class="w-16 h-1 bg-gradient-to-r from-sky-300 to-sky-500 mx-auto mt-4 rounded-full"></div>
                        </div>

                        <div class="flex flex-col lg:flex-row items-center gap-10 lg:gap-16 relative z-10">
                            <div class="w-full lg:w-3/5 flex justify-center items-center bg-white rounded-[2rem] p-6 md:p-12 h-[280px] sm:h-[350px] md:h-[400px] lg:h-[460px] relative shadow-[0_15px_40px_rgba(14,165,233,0.04)] border border-slate-100 overflow-hidden group">
                                <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,_rgba(14,165,233,0.03),_transparent_70%)] pointer-events-none z-0"></div>
                                <img id="main-car-image" src="{default_image}" alt="Perodua {model}" class="max-w-[90%] max-h-[85%] object-contain relative z-10 drop-shadow-[0_20px_40px_rgba(15,23,42,0.15)] transition-all duration-500 ease-out" onerror="this.src='{fallback_image}'">
                                <div class="absolute bottom-12 left-1/2 -translate-x-1/2 w-4/5 h-6 bg-slate-900/10 blur-2xl rounded-[100%] z-0"></div>
                                <div class="absolute bottom-6 left-1/2 -translate-x-1/2 bg-slate-900/90 backdrop-blur-md text-white border border-slate-800 px-6 py-2.5 rounded-full font-bold tracking-wider text-xs sm:text-sm shadow-2xl flex items-center space-x-3 z-20">
                                    <div id="color-indicator" class="w-3.5 h-3.5 rounded-full shadow-[0_0_10px_currentColor] border border-white/20 transition-all duration-500" style="background-color: {initial_hex}; color: {initial_hex};"></div>
                                    <span id="color-name-display" class="transition-all duration-300 uppercase tracking-widest text-slate-200">{initial_label}</span>
                                </div>
                            </div>

                            <div class="w-full lg:w-2/5 flex flex-col justify-center">
                                <div class="mb-4 flex items-center space-x-2.5 justify-center lg:justify-start">
                                    <span class="w-1.5 h-4 bg-sky-400 rounded-full"></span>
                                    <p class="text-xs text-sky-700/80 font-extrabold uppercase tracking-widest">{swatch_count} Pilihan Warna Premium:</p>
                                </div>
                                <div class="grid grid-cols-5 lg:grid-cols-1 gap-3 sm:gap-4 lg:space-y-2">
                                    {button_html}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <section class="max-w-7xl mx-auto px-4">
                <div class="showroom-container relative overflow-hidden rounded-[30px] bg-gradient-to-br from-slate-900 via-slate-950 to-slate-900 p-4 sm:p-6 md:p-10 shadow-2xl my-10 text-white">
                    <div class="text-center mb-6 md:mb-8">
                        <span class="bg-perodua text-slate-950 px-4 py-1.5 rounded-full text-[11px] font-bold tracking-widest uppercase shadow-md shadow-perodua/20">PERODUA {model} PREMIUM SHOWROOM</span>
                        <p class="text-gray-400 mt-2 text-xs md:text-sm">Slide kiri atau kanan untuk melihat varian penuh</p>
                    </div>

                    <div class="swiper mySwiper pb-10">
                        <div class="swiper-wrapper">
                            {showroom_slides}
                        </div>
                        <div class="swiper-pagination !bottom-0"></div>
                    </div>
                </div>
            </section>

            <style>
                #main-car-image {
                    will-change: transform, opacity;
                }
            </style>

            <script>
                function changeCarColor(colorName, imageSrc, hexColor, btnElement) {
                    const section = btnElement.closest('.bg-white');
                    const mainImage = section.querySelector('#main-car-image');
                    const colorDisplay = section.querySelector('#color-name-display');
                    const colorIndicator = section.querySelector('#color-indicator');

                    mainImage.style.transform = 'scale(0.96)';
                    mainImage.style.opacity = '0';
                    colorDisplay.style.opacity = '0';

                    setTimeout(() => {
                        mainImage.src = imageSrc;
                        colorDisplay.innerText = colorName;
                        colorIndicator.style.backgroundColor = hexColor;

                        mainImage.style.transform = 'scale(1)';
                        mainImage.style.opacity = '1';
                        colorDisplay.style.opacity = '1';
                    }, 200);

                    const swatches = section.querySelectorAll('.color-swatch-btn, .color-swatch');
                    swatches.forEach(btn => {
                        btn.classList.remove('ring-2', 'bg-white', 'shadow-sm', 'border-gray-100');
                        btn.classList.add('ring-0', 'hover:bg-gray-50', 'border-transparent');
                    });

                    btnElement.classList.remove('ring-0', 'hover:bg-gray-50', 'border-transparent');
                    btnElement.classList.add('ring-2', 'bg-white', 'shadow-sm', 'border-gray-100');
                }
            </script>
            {recovery_html}
        </section>`;

const PAGE_CONFIGS = {
    'bezza.html': {
        model: 'BEZZA',
        default_image: 'gambar/red bezza.png',
        fallback_image: 'gambar/red.png',
        initial_label: 'Garnet Red',
        initial_hex: '#9e2a2b',
        swatches: [
            ['Garnet Red', 'gambar/red bezza.png', '#9e2a2b'],
            ['Sugar Brown', 'gambar/brown bezza.png', '#a0522d'],
            ['Ocean Blue', 'gambar/ocean bezza.png', '#0077b6'],
            ['Granite Grey', 'gambar/grey bezza.png', '#5c5c5c'],
            ['Glittering Silver', 'gambar/silver bezza.png', '#c0c0c0'],
            ['Ivory White', 'gambar/white bezza.png', '#f8f9fa'],
        ],
    },
    'ativa.html': {
        model: 'ATIVA',
        default_image: 'gambar/ativa red.png',
        fallback_image: 'gambar/red.png',
        initial_label: 'Pearl Delima Red',
        initial_hex: '#b71c1c',
        swatches: [
            ['Pearl Delima Red', 'gambar/ativa red.png', '#b71c1c'],
            ['Pearl Diamond White', 'gambar/ativa white.png', '#ffffff'],
            ['Cobalt Blue', 'gambar/ativa blue.png', '#1e3a8a'],
            ['Glittering Silver', 'gambar/ativa silver.png', '#c0c0c0'],
            ['Granite Grey', 'gambar/ativa black.png', '#5c5c5c'],
        ],
    },
    'aruz.html': {
        model: 'ARUZ',
        default_image: 'gambar/aruz red.png',
        fallback_image: 'gambar/red.png',
        initial_label: 'Passion Red',
        initial_hex: '#d62828',
        swatches: [
            ['Passion Red', 'gambar/aruz red.png', '#d62828'],
            ['Granite Grey', 'gambar/aruz grey.png', '#5c5c5c'],
            ['Glittering Silver', 'gambar/aruz silver.png', '#c0c0c0'],
            ['Ivory White', 'gambar/aruz white.png', '#f8f9fa'],
            ['Midnight Black', 'gambar/aruz black.png', '#111111'],
            ['Bronze Brown', 'gambar/aruz brown.png', '#5c4033'],
        ],
    },
    'alza.html': {
        model: 'ALZA',
        default_image: 'gambar/alza brown.png',
        fallback_image: 'gambar/brown.png',
        initial_label: 'Vintage Brown',
        initial_hex: '#5d4037',
        swatches: [
            ['Vintage Brown', 'gambar/alza brown.png', '#5d4037'],
            ['Elegant Black', 'gambar/alza black.png', '#1a1a1a'],
            ['Garnet Red', 'gambar/alza red.png', '#9e2a2b'],
            ['Glittering Silver', 'gambar/alza silver.png', '#c0c0c0'],
            ['Ivory White', 'gambar/alza white.png', '#f8f9fa'],
        ],
    },
    'myvi.html': {
        model: 'MYVI',
        default_image: 'gambar/myvi grey.png',
        fallback_image: 'gambar/grey.png',
        initial_label: 'Glittering Silver',
        initial_hex: '#c0c0c0',
        swatches: [
            ['Glittering Silver', 'gambar/myvi grey.png', '#c0c0c0'],
            ['Electric Blue', 'gambar/myvi blue.png', '#0077b6'],
            ['Lava Red', 'gambar/myvi red.png', '#e63946'],
            ['Ivory White', 'gambar/myvi white.png', '#f8f9fa'],
            ['Granite Grey', 'gambar/myvi black.png', '#5c5c5c'],
        ],
    },
    'traz.html': {
        model: 'TRAZ',
        default_image: 'car/white.png',
        fallback_image: 'gambar/placeholder.png',
        initial_label: 'Ivory White',
        initial_hex: '#f5f0e6',
        swatches: [
            ['Electric Blue', 'car/blue.png', '#1976d2'],
            ['Cranberry Red', 'car/red.png', '#b71c1c'],
            ['Granite Grey', 'car/grey.png', '#455a64'],
            ['Glittering Silver', 'car/silver.png', '#c0c0c0'],
            ['Ivory White', 'car/white.png', '#f5f0e6'],
        ],
    },
};

function buildSwatches(swatches) {
    return swatches
        .map(([label, src, hex]) => {
            return `<button onclick="changeCarColor('${label}', '${src}', '${hex}', this)" class="color-swatch-btn group flex flex-col lg:flex-row items-center p-3 rounded-xl lg:rounded-2xl border border-slate-100 bg-slate-50/50 transition-all duration-300 hover:bg-white hover:border-sky-100">\n                                        <div class="w-10 h-10 sm:w-11 sm:h-11 rounded-full border-2 border-white shadow-md relative overflow-hidden flex-shrink-0" style="background-color: ${hex}"></div>\n                                        <span class="hidden lg:block text-sm font-bold text-slate-700 ml-4 tracking-tight">${label}</span>\n                                    </button>`;
        })
        .join('\n                                    ');
}

function buildShowroomSlides(config) {
    const slides = config.swatches.slice(0, 4);
    const slideItems = slides.length ? slides : [[config.model, config.default_image, config.initial_hex]];
    return slideItems
        .map(([label, src]) => {
            const message = encodeURIComponent(`Hi, saya berminat dengan Perodua ${config.model} ${label}.`);
            return `
                        <div class="swiper-slide">
                            <div class="flex flex-col lg:grid lg:grid-cols-2 gap-6 lg:gap-12 items-center">
                                <div class="w-full lg:order-2 relative flex items-center justify-center p-4 md:p-6 bg-white rounded-2xl shadow-xl border border-slate-100/10 transition-all duration-300 hover:shadow-2xl group min-h-[180px] sm:min-h-[240px] md:min-h-[300px]">
                                    <div class="absolute w-48 h-48 bg-perodua/10 blur-[50px] rounded-full z-0"></div>
                                    <img src="${src}" alt="${config.model} ${label}" class="w-10/12 sm:w-8/12 lg:w-full max-w-[400px] h-auto object-contain transition-transform duration-500 ease-out transform group-hover:scale-105 group-hover:-translate-y-2 relative z-10" onerror="this.src='gambar/placeholder.png';">
                                </div>

                                <div class="w-full lg:order-1">
                                    <span class="bg-slate-700 text-white px-3 py-1 rounded-full text-[10px] font-bold tracking-widest uppercase">SHOWROOM VARIAN</span>
                                    <h2 class="text-2xl sm:text-3xl md:text-5xl font-black text-white mt-3 tracking-tight">${config.model} ${label}</h2>
                                    <p class="text-gray-400 mt-1 text-xs sm:text-sm md:text-base font-medium">Lihat pilihan warna dan ciri utama untuk model ini.</p>

                                    <div class="mt-5 space-y-2 text-xs sm:text-sm">
                                        <div class="flex justify-between border-b border-slate-800 pb-1.5">
                                            <span class="text-gray-400">Model</span>
                                            <span class="font-medium text-gray-300">${config.model}</span>
                                        </div>
                                        <div class="flex justify-between border-b border-slate-800 pb-1.5">
                                            <span class="text-gray-400">Warna</span>
                                            <span class="font-medium text-gray-300">${label}</span>
                                        </div>
                                        <div class="flex justify-between border-b border-slate-800 pb-1.5">
                                            <span class="text-gray-400">Ketersediaan</span>
                                            <span class="font-medium text-gray-300">Stok terhad</span>
                                        </div>
                                    </div>

                                    <div class="grid grid-cols-2 gap-3 sm:gap-4 mt-5">
                                        <a href="https://wa.me/60176503339?text=${message}" class="w-full flex items-center justify-center bg-emerald-500 text-white hover:bg-emerald-600 font-bold py-3 px-4 rounded-full text-center text-xs md:text-sm shadow-md">Book Now</a>
                                    </div>
                                </div>
                            </div>
                        </div>`;
        })
        .join('');
}

function extractRecoveryHtml(content) {
    const recoveryMatch = content.match(/<section[^>]*>[\s\S]*?<script>[\s\S]*?<\/script>([\s\S]*?)<\/section>/i);
    return recoveryMatch ? recoveryMatch[1] : '';
}

function buildSection(config) {
    const buttonHtml = buildSwatches(config.swatches);
    const showroomSlides = buildShowroomSlides(config);
    return SECTION_TEMPLATE.replaceAll('{model}', config.model)
        .replaceAll('{default_image}', config.default_image)
        .replaceAll('{fallback_image}', config.fallback_image)
        .replaceAll('{initial_label}', config.initial_label)
        .replaceAll('{initial_hex}', config.initial_hex)
        .replaceAll('{swatch_count}', String(config.swatches.length))
        .replaceAll('{button_html}', buttonHtml)
        .replaceAll('{showroom_slides}', showroomSlides)
        .replaceAll('{recovery_html}', '');
}

function updateFile(fileName, config) {
    const filePath = path.join(BASE_DIR, fileName);
    if (!fs.existsSync(filePath)) {
        console.warn(`File missing: ${fileName}`);
        return;
    }

    let content = fs.readFileSync(filePath, 'utf8');
    const backupPath = filePath + '.bak';
    if (!fs.existsSync(backupPath)) {
        fs.writeFileSync(backupPath, content, 'utf8');
        console.log(`Backup created: ${path.basename(backupPath)}`);
    }

    const tailwindRegex = /<script>\s*tailwind\.config[\s\S]*?<\/script>/i;
    content = content.replace(tailwindRegex, TAILWIND_CONFIG);

    const bodyRegex = /<body[^>]*>/i;
    content = content.replace(bodyRegex, '<body class="bg-gray-50 text-gray-800 flex flex-col min-h-screen overflow-x-hidden">');

    if (/<\/body>/i.test(content)) {
        content = content.replace(/<\/body>/i, `${SWIPER_INIT_SCRIPT}\n</body>`);
    }

    const topNoticeRegex = /<div class="bg-brandSlate text-white text-xs py-2 px-4 text-center sm:text-right sm:px-8 font-medium">[\s\S]*?<\/div>\s*(?=<header)/gi;
    content = content.replace(topNoticeRegex, '');

    const headerRegex = /<header[^>]*>[\s\S]*?<\/header>/i;
    content = content.replace(headerRegex, HEADER_HTML);

    const sectionReplaceRegex = /<\/header>[\s\S]*?(?=<footer)/i;
    const sectionHtml = buildSection(config);
    if (!sectionReplaceRegex.test(content)) {
        console.warn(`Page content block not found in ${fileName}`);
    } else {
        content = content.replace(sectionReplaceRegex, '</header>\n' + sectionHtml + '\n');
    }

    // Remove duplicate Swiper imports / initialization from old page content without crossing script boundaries
    content = content.replace(/<link rel="stylesheet" href="https:\/\/cdn\.jsdelivr\.net\/npm\/swiper@11\/swiper-bundle\.min\.css"\/?><\/style>?\s*/gi, '');
    content = content.replace(/<script src="https:\/\/cdn\.jsdelivr\.net\/npm\/swiper@11\/swiper-bundle\.min\.js"><\/script>\s*/gi, '');
    content = content.replace(/<script\b[^>]*>(?:[^<]|<(?!\/script>))*?new Swiper[\s\S]*?<\/script>\s*/gi, '');
    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`Updated ${fileName}`);
}

Object.entries(PAGE_CONFIGS).forEach(([fileName, config]) => {
    updateFile(fileName, config);
});


