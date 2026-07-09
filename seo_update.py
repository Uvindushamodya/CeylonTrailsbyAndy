import re
import os

html_files = ['index.html', 'about.html', 'tours.html', 'contact.html']
base_dir = 'd:/Andy/CeylonTrailsbyAndy/'

ga4_script = """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MGP9RHNB6M"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-MGP9RHNB6M');
    </script>
</head>"""

gsc_meta = '    <meta name="google-site-verification" content="PLACEHOLDER_VERIFICATION_CODE" />\n    <!-- SEO & Social Meta Tags -->'

for file in html_files:
    filepath = os.path.join(base_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Domain replace
    content = content.replace('andysrilankatours.com', 'discoverceylonbyandy.com')
    
    # 2. GA4 insert (before </head>)
    if 'G-MGP9RHNB6M' not in content:
        content = content.replace('</head>', ga4_script)
    
    # 3. GSC insert (only in index.html)
    if file == 'index.html' and 'google-site-verification' not in content:
        content = content.replace('    <!-- SEO & Social Meta Tags -->', gsc_meta)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Update reviews.js
reviews_js_path = os.path.join(base_dir, 'js/reviews.js')
with open(reviews_js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

new_api_base = """// Replace PLACEHOLDER_SCRIPT_ID with your actual Google Apps Script Web App Deployment ID
const API_BASE_URL = 'https://script.google.com/macros/s/PLACEHOLDER_SCRIPT_ID/exec';"""

# Replace the first 4 lines that defined API_BASE_URL before
js_content = re.sub(r"const API_BASE_URL = .*?;\n", new_api_base + "\n", js_content, flags=re.DOTALL)

with open(reviews_js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("SEO update script completed.")
