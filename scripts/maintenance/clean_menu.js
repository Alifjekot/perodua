const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

const myInjectedScript = `<script>
document.addEventListener("DOMContentLoaded", function () {
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            mobileMenu.classList.toggle('hidden');
        });
        
        document.addEventListener('click', function(e) {
            if (!mobileMenu.classList.contains('hidden') && !mobileMenu.contains(e.target) && !mobileMenuBtn.contains(e.target)) {
                mobileMenu.classList.add('hidden');
            }
        });
    }
});
</script>`;

const cleanScript = `
<script>
    // Unified Mobile Menu Toggle
    document.addEventListener("DOMContentLoaded", function () {
        const btn = document.getElementById('mobile-menu-btn');
        const menu = document.getElementById('mobile-menu');
        if (btn && menu) {
            // override any existing click listeners by cloning
            const newBtn = btn.cloneNode(true);
            btn.parentNode.replaceChild(newBtn, btn);
            
            newBtn.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                menu.classList.toggle('hidden');
            });
            
            document.addEventListener('click', function(e) {
                if (!menu.classList.contains('hidden') && !menu.contains(e.target) && !newBtn.contains(e.target)) {
                    menu.classList.add('hidden');
                }
            });
        }
    });
</script>
`;

let count = 0;
files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    let modified = false;

    // Remove my previously injected script
    if (content.includes(myInjectedScript)) {
        content = content.replace(myInjectedScript, '');
        modified = true;
    }
    
    // Check if the clean script is already there, if not, add it
    if (!content.includes('Unified Mobile Menu Toggle')) {
        // Append to end of file, or before </body> if it exists
        if (content.includes('</body>')) {
            // Find last </body>
            const lastBodyIndex = content.lastIndexOf('</body>');
            content = content.substring(0, lastBodyIndex) + cleanScript + content.substring(lastBodyIndex);
        } else {
            content += '\\n' + cleanScript;
        }
        modified = true;
    }

    if (modified) {
        fs.writeFileSync(file, content, 'utf8');
        count++;
        console.log('Fixed ' + file);
    }
});

console.log('Cleaned and fixed ' + count + ' files.');
