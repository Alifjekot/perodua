const fs = require('fs');
const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    let modified = false;

    if (content.includes('<body class="bg-gray-50 text-gray-800 flex flex-col min-h-screen">')) {
        content = content.replace('<body class="bg-gray-50 text-gray-800 flex flex-col min-h-screen">', '<body class="bg-gray-50 text-gray-800 flex flex-col min-h-screen overflow-x-hidden">');
        modified = true;
    }

    if (modified) {
        fs.writeFileSync(file, content, 'utf8');
        console.log('Updated body in ' + file);
    }
});
