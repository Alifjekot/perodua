const fs = require('fs');
const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));
files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    
    // Add "Feedback Customer" to mobile menu if missing
    if (!content.includes('Feedback Customer</a>\n            <div class="text-xs text-slate-400')) {
        content = content.replace(
            '<div class="text-xs text-slate-400 font-bold tracking-wider uppercase">Car Model Options</div>',
            '<a href="feedback.html" class="block py-2 text-slate-600 hover:text-perodua font-bold border-b border-slate-50">Feedback Customer</a>\n            <div class="text-xs text-slate-400 font-bold tracking-wider uppercase">Car Model Options</div>'
        );
    }
    
    // Also, change hamburger button to show "MENU" text so users know what it is
    if (content.includes('class="text-slate-700 p-2 rounded-lg hover:bg-slate-100 focus:outline-none"')) {
        content = content.replace(
            '<i class="fa-solid fa-bars text-2xl"></i>',
            '<div class="flex items-center space-x-2"><span class="text-xs font-bold uppercase tracking-wider text-slate-500">Menu</span><i class="fa-solid fa-bars text-xl"></i></div>'
        );
    }
    
    fs.writeFileSync(file, content, 'utf8');
});
console.log('Update complete');

