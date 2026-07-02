const fs = require('fs'); 
const path = require('path'); 
const files = fs.readdirSync('.').filter(f => f.endsWith('.html')); 

const floatingBtn = `
    <!-- Floating WhatsApp Button -->
    <a href="https://wa.me/60176503339" target="_blank"
        class="fixed bottom-6 right-6 bg-emerald-500 hover:bg-emerald-600 text-white rounded-full p-4 shadow-[0_4px_14px_0_rgba(16,185,129,0.39)] hover:shadow-[0_6px_20px_rgba(16,185,129,0.23)] hover:-translate-y-1 transition-all duration-300 z-50 flex items-center justify-center"
        aria-label="WhatsApp">
        <i class="fa-brands fa-whatsapp text-3xl"></i>
    </a>
`; 

files.forEach(file => { 
    let content = fs.readFileSync(file, 'utf8'); 
    let modified = false; 

    if (!content.includes('Floating WhatsApp Button')) { 
        content = content.replace('</body>', floatingBtn + '</body>'); 
        modified = true; 
    } 
    
    if (content.includes('class="bg-slate-50 text-slate-800 font-sans"')) { 
        content = content.replace('class="bg-slate-50 text-slate-800 font-sans"', 'class="bg-slate-50 text-slate-800 font-sans overflow-x-hidden"'); 
        modified = true; 
    } else if (content.includes('class="bg-slate-50 text-gray-800 flex flex-col min-h-screen"')) { 
        content = content.replace('class="bg-slate-50 text-gray-800 flex flex-col min-h-screen"', 'class="bg-slate-50 text-gray-800 flex flex-col min-h-screen overflow-x-hidden"'); 
        modified = true; 
    } 

    if (content.includes('h-[350px] md:h-[450px]')) { 
        content = content.replace(/h-\[350px\] md:h-\[450px\]/g, 'h-[250px] sm:h-[300px] md:h-[350px] lg:h-[450px]'); 
        modified = true; 
    } 
    
    if (content.includes('rounded-3xl p-8')) { 
        content = content.replace(/rounded-3xl p-8/g, 'rounded-3xl p-4 md:p-8'); 
        modified = true; 
    } 
    
    if (content.includes('>Utama<')) { 
        content = content.replace(/>Utama</g, '>Home<'); 
        modified = true; 
    } 
    
    if (modified) { 
        fs.writeFileSync(file, content, 'utf8'); 
        console.log('Updated ' + file); 
    } 
});

