const fs = require('fs');
const content = fs.readFileSync('c:/Users/user/Downloads/public_html/bezza.html','utf8');
const regex = /(<section[^>]*>[\s\S]*?<script>[\s\S]*?<\/script>\s*<\/section>)([\s\S]*?)<\/body>/i;
const m = content.match(regex);
console.log('matched?', !!m);
if (m) {
  console.log('group1 len', m[1].length);
  console.log('group2 start', m[2].slice(0,200).replace(/\n/g,' '));
}
console.log('body index', content.indexOf('</body>'));
