const fs = require('fs');
const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

const scriptToInject = `
<script>
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
</script>
`;

let count = 0;
files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    
    // Check if script is already present
    if (!content.includes("mobileMenuBtn.addEventListener('click'")) {
        if (content.includes('</body>')) {
            content = content.replace('</body>', scriptToInject + '</body>');
        } else {
            content = content + '\n' + scriptToInject;
        }
        fs.writeFileSync(file, content, 'utf8');
        count++;
        console.log(`Updated ${file}`);
    }
});

console.log(`Update complete. Modified ${count} files.`);
