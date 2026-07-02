const fs = require('fs');
const path = require('path');

const models = {
    alza: {
        name: 'ALZA',
        image: 'alza-brown.jpg',
        colors: [
            { name: 'Vintage Brown', hex: '#5d4037', img: 'gambar/brown.png' },
            { name: 'Elegant Black', hex: '#1a1a1a', img: 'gambar/black.png' },
            { name: 'Garnet Red', hex: '#9e2a2b', img: 'gambar/red.png' },
            { name: 'Glittering Silver', hex: '#c0c0c0', img: 'gambar/silver.png' },
            { name: 'Ivory White', hex: '#f8f9fa', img: 'gambar/white.png' }
        ]
    },
    aruz: {
        name: 'ARUZ',
        image: 'aruz-red.jpg',
        colors: [
            { name: 'Passion Red', hex: '#d62828', img: 'gambar/red.png' },
            { name: 'Electric Blue', hex: '#0077b6', img: 'gambar/ocean.png' },
            { name: 'Granite Grey', hex: '#5c5c5c', img: 'gambar/grey.png' },
            { name: 'Glittering Silver', hex: '#c0c0c0', img: 'gambar/silver.png' },
            { name: 'Ivory White', hex: '#f8f9fa', img: 'gambar/white.png' }
        ]
    },
    myvi: {
        name: 'MYVI',
        image: 'myvi-red.jpg',
        colors: [
            { name: 'Cranberry Red', hex: '#9e2a2b', img: 'gambar/red.png' },
            { name: 'Glittering Silver', hex: '#c0c0c0', img: 'gambar/silver.png' },
            { name: 'Electric Blue', hex: '#0077b6', img: 'gambar/ocean.png' },
            { name: 'Lava Red', hex: '#e63946', img: 'gambar/red.png' },
            { name: 'Ivory White', hex: '#f8f9fa', img: 'gambar/white.png' },
            { name: 'Granite Grey', hex: '#5c5c5c', img: 'gambar/grey.png' }
        ]
    },
    ativa: {
        name: 'ATIVA',
        image: 'ativa-red.jpg',
        colors: [
            { name: 'Pearl Delima Red', hex: '#b71c1c', img: 'gambar/red.png' },
            { name: 'Pearl Diamond White', hex: '#ffffff', img: 'gambar/white.png' },
            { name: 'Cobalt Blue', hex: '#1e3a8a', img: 'gambar/ocean.png' },
            { name: 'Glittering Silver', hex: '#c0c0c0', img: 'gambar/silver.png' },
            { name: 'Granite Grey', hex: '#5c5c5c', img: 'gambar/grey.png' }
        ]
    },
    axia: {
        name: 'AXIA',
        image: 'axia-blue.jpg',
        colors: [
            { name: 'Coral Blue', hex: '#5bc0be', img: 'gambar/ocean.png' },
            { name: 'Granite Grey', hex: '#5c5c5c', img: 'gambar/grey.png' },
            { name: 'Lava Red', hex: '#e63946', img: 'gambar/red.png' },
            { name: 'Glittering Silver', hex: '#c0c0c0', img: 'gambar/silver.png' },
            { name: 'Ivory White', hex: '#f8f9fa', img: 'gambar/white.png' }
        ]
    },
    bezza: {
        name: 'BEZZA',
        image: 'bezza-red.jpg',
        colors: [
            { name: 'Garnet Red', hex: '#9e2a2b', img: 'gambar/red.png' },
            { name: 'Sugar Brown', hex: '#a0522d', img: 'gambar/brown.png' },
            { name: 'Ocean Blue', hex: '#0077b6', img: 'gambar/ocean.png' },
            { name: 'Granite Grey', hex: '#5c5c5c', img: 'gambar/grey.png' },
            { name: 'Glittering Silver', hex: '#c0c0c0', img: 'gambar/silver.png' },
            { name: 'Ivory White', hex: '#f8f9fa', img: 'gambar/white.png' }
        ]
    }
};

function generateColorHTML(modelInfo) {
    const defaultColor = modelInfo.colors[0];
    let html = `
        <!-- Color Selection Section -->
        <div class="mb-16 bg-white rounded-3xl shadow-[0_8px_30px_rgb(0,0,0,0.08)] border border-gray-100 p-6 md:p-10 overflow-hidden relative">
            <div class="text-center mb-10 relative z-10">
                <span class="text-perodua text-xs font-extrabold tracking-widest uppercase bg-perodua/10 px-4 py-1.5 rounded-full mb-4 inline-block">Pilihan Warna</span>
                <h2 class="text-3xl md:text-4xl font-black text-gray-900 tracking-tight uppercase">Pilih Warna ${modelInfo.name} Anda</h2>
            </div>

            <div class="flex flex-col lg:flex-row items-center gap-12 relative z-10">
                <!-- Main Car Image -->
                <div class="w-full lg:w-3/5 flex justify-center items-center bg-gradient-to-b from-gray-50 to-gray-100 rounded-3xl p-8 h-[350px] md:h-[450px] relative shadow-inner border border-gray-100">
                    <img id="main-car-image" src="gambar/${modelInfo.image}" alt="Perodua ${modelInfo.name}" class="max-w-full max-h-full object-contain drop-shadow-2xl transition-all duration-300 ease-in-out scale-100" onerror="this.src='${defaultColor.img}'">
                    
                    <!-- Floor shadow effect -->
                    <div class="absolute bottom-10 left-1/2 -translate-x-1/2 w-2/3 h-4 bg-black/20 blur-xl rounded-[100%] z-0"></div>
                    
                    <div class="absolute bottom-6 left-1/2 -translate-x-1/2 bg-white/90 backdrop-blur-md text-gray-900 border border-gray-200 px-6 py-2 rounded-full font-black tracking-wider text-sm shadow-xl flex items-center space-x-2 z-10">
                        <div id="color-indicator" class="w-3 h-3 rounded-full shadow-sm border border-black/10 transition-colors duration-500" style="background-color: ${defaultColor.hex}"></div>
                        <span id="color-name-display" class="transition-all duration-300">${defaultColor.name}</span>
                    </div>
                </div>

                <!-- Color Swatches -->
                <div class="w-full lg:w-2/5 flex flex-col justify-center">
                    <p class="text-sm text-gray-500 font-bold mb-6 text-center lg:text-left uppercase tracking-wider">Terdapat ${modelInfo.colors.length} Pilihan Warna:</p>
                    <div class="grid grid-cols-3 gap-3 md:gap-5">
`;

    modelInfo.colors.forEach((color, index) => {
        const isFirst = index === 0;
        const btnClasses = isFirst 
            ? "color-swatch flex flex-col items-center group ring-2 ring-offset-4 ring-perodua rounded-2xl p-3 transition-all bg-white shadow-sm border border-gray-100" 
            : "color-swatch flex flex-col items-center group ring-0 ring-offset-4 ring-perodua rounded-2xl p-3 transition-all hover:bg-gray-50 border border-transparent";
        
        let colorDisplay = color.name.replace(' ', '<br>');
        
        html += `                        <button onclick="changeCarColor('${color.name}', '${color.img}', '${color.hex}', this)" class="${btnClasses}">
                            <div class="w-12 h-12 md:w-14 md:h-14 rounded-full shadow-inner shadow-black/30 border-4 ${color.hex === '#ffffff' ? 'border-gray-100' : 'border-white'} group-hover:scale-110 transition-transform duration-300 relative" style="background-color: ${color.hex}">
                                <div class="absolute inset-0 rounded-full bg-gradient-to-tr from-black/20 to-transparent"></div>
                            </div>
                            <span class="text-[10px] md:text-xs font-bold text-gray-700 mt-3 text-center leading-tight group-hover:text-perodua transition-colors">${colorDisplay}</span>
                        </button>\n`;
    });

    html += `                    </div>
                </div>
            </div>

            <!-- Background Decorative Element -->
            <div class="absolute -top-24 -right-24 w-96 h-96 bg-perodua/5 rounded-full blur-3xl z-0 pointer-events-none"></div>

            <style>
                /* Setup transition for smooth color changing */
                #main-car-image {
                    will-change: transform, opacity;
                }
            </style>

            <script>
                function changeCarColor(colorName, imageSrc, hexColor, btnElement) {
                    const mainImage = btnElement.closest('.bg-white').querySelector('#main-car-image');
                    const colorDisplay = btnElement.closest('.bg-white').querySelector('#color-name-display');
                    const colorIndicator = btnElement.closest('.bg-white').querySelector('#color-indicator');

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

                    const swatches = btnElement.closest('.bg-white').querySelectorAll('.color-swatch');
                    swatches.forEach(btn => {
                        btn.classList.remove('ring-2', 'bg-white', 'shadow-sm', 'border-gray-100');
                        btn.classList.add('ring-0', 'hover:bg-gray-50', 'border-transparent');
                    });

                    btnElement.classList.remove('ring-0', 'hover:bg-gray-50', 'border-transparent');
                    btnElement.classList.add('ring-2', 'bg-white', 'shadow-sm', 'border-gray-100');
                }
            </script>
        </div>
`;
    return html;
}

const dir = '.'; // run in current directory
for (const model in models) {
    const filename = path.join(dir, model + '.html');
    if (fs.existsSync(filename)) {
        let content = fs.readFileSync(filename, 'utf-8');
        
        // Remove existing color selection section if it exists
        const startComment = '<!-- Color Selection Section -->';
        const endGrid = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">';
        
        let insertIndex = content.indexOf(endGrid);
        
        if (content.indexOf(startComment) !== -1) {
            // Already has color section, replace it
            const startIdx = content.indexOf(startComment);
            const endIdx = content.indexOf(endGrid);
            if(startIdx < endIdx) {
                content = content.substring(0, startIdx) + content.substring(endIdx);
            }
        }
        
        // Find insert point again
        insertIndex = content.indexOf(endGrid);
        if (insertIndex !== -1) {
            const colorHtml = generateColorHTML(models[model]);
            content = content.substring(0, insertIndex) + colorHtml + content.substring(insertIndex);
            fs.writeFileSync(filename, content);
            console.log('Updated colors for ' + filename);
        }
    }
}
