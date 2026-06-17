import re
import os

files = ['index.html', 'tours.html', 'about.html', 'contact.html']

replacements = [
    # Footer Contact link
    (r'(<a href="contact.html" class="hover:text-brand-primary transition-colors")>Contact</a>', r'\1 data-i18n="footer.contact_link">Contact</a>'),
    
    # Index specific SVG wraps
    (r'(</svg>\s*)Cultural Triangle\s*</div>', r'\1<span data-i18n="index.tours.tour1.tag">Cultural Triangle</span>\n                        </div>'),
    (r'(</svg>\s*)Southern Wilds\s*</div>', r'\1<span data-i18n="index.tours.tour2.tag">Southern Wilds</span>\n                        </div>'),
    (r'(</svg>\s*)Hill Country\s*</div>', r'\1<span data-i18n="index.tours.tour3.tag">Hill Country</span>\n                        </div>'),
    (r'(</svg>\s*)Colombo, Sri Lanka\s*</li>', r'\1<span data-i18n="contact.info.colombo">Colombo, Sri Lanka</span></li>'),
    
    # Tours specific
    (r'(<span class="text-brand-secondary[^>]*?)>Cultural Triangle</span>', r'\1 data-i18n="index.tours.tour1.tag">Cultural Triangle</span>'),
    (r'(<h2 class="text-3xl[^>]*?)>Ancient Heritage Tour</h2>', r'\1 data-i18n="index.tours.tour1.title">Ancient Heritage Tour</h2>'),
    (r'(<span class="text-brand-secondary[^>]*?)>Southern Wilds</span>', r'\1 data-i18n="index.tours.tour2.tag">Southern Wilds</span>'),
    (r'(<h2 class="text-3xl[^>]*?)>Yala Leopard Safari</h2>', r'\1 data-i18n="index.tours.tour2.title">Yala Leopard Safari</h2>'),
    (r'(<span class="text-brand-secondary[^>]*?)>Hill Country</span>', r'\1 data-i18n="index.tours.tour3.tag">Hill Country</span>'),
    (r'(<h2 class="text-3xl[^>]*?)>Tea &amp; Train Odyssey</h2>', r'\1 data-i18n="index.tours.tour3.title">Tea &amp; Train Odyssey</h2>'),
    (r'(<h2 class="text-3xl[^>]*?)>Tea & Train Odyssey</h2>', r'\1 data-i18n="index.tours.tour3.title">Tea & Train Odyssey</h2>'),
    
    # About specific
    (r'(<h2 class="text-3xl[^>]*?)>A Passionate Local Expert</h2>', r'\1 data-i18n="about.content.title">A Passionate Local Expert</h2>'),
    (r'(<p class="text-slate-500[^>]*?)>Years Experience</p>', r'\1 data-i18n="about.stats.exp">Years Experience</p>'),
    (r'(<p class="text-slate-500[^>]*?)>Happy Travelers</p>', r'\1 data-i18n="about.stats.happy">Happy Travelers</p>'),
    (r'(<p class="text-slate-500[^>]*?)>SLTDA Guide</p>', r'\1 data-i18n="about.stats.cert">SLTDA Guide</p>'),
    (r'(<p class="text-slate-500[^>]*?)>TripAdvisor</p>', r'\1 data-i18n="about.stats.stars">TripAdvisor</p>'),
    (r'(<h3 class="text-xl[^>]*?)>Contact Details</h3>', r'\1 data-i18n="contact.details.title">Contact Details</h3>'),
    (r'(<span class="font-medium")>Andy</span>', r'\1 data-i18n="contact.info.andy">Andy</span>'),
    
    # Contact specific
    (r'(<h1 class="text-4xl[^>]*?)>Let\'s Plan Your Trip</h1>', r'\1 data-i18n="contact.header.title">Let\'s Plan Your Trip</h1>'),
    (r'(<p class="text-lg[^>]*?)>Get in touch to customize your itinerary or book one of our popular packages.</p>', r'\1 data-i18n="contact.header.desc">Get in touch to customize your itinerary or book one of our popular packages.</p>'),
    (r'(<h4 class="font-bold[^>]*?)>Phone &amp; WhatsApp</h4>', r'\1 data-i18n="contact.details.phone">Phone &amp; WhatsApp</h4>'),
    (r'(<h4 class="font-bold[^>]*?)>Phone & WhatsApp</h4>', r'\1 data-i18n="contact.details.phone">Phone & WhatsApp</h4>'),
    (r'(<h4 class="font-bold[^>]*?)>Email</h4>', r'\1 data-i18n="contact.details.email">Email</h4>'),
    (r'(<a[^>]*?)>\s*<svg[^>]*>.*?</svg>\s*Chat on WhatsApp\s*</a>', r'\1>\n                                <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.125-.339-.153-.889-.356-1.748-.889-1.229-.762-2.029-2.008-2.091-2.092-.061-.084-.498-.665-.498-1.267 0-.602.316-.897.427-1.013.111-.116.244-.146.326-.146.082 0 .163.003.235.006.085.004.197-.033.308.232.116.279.395.964.431 1.036.036.073.061.159.006.269-.055.109-.083.176-.165.271-.083.095-.175.205-.247.288-.083.095-.171.199-.071.371.099.172.441.731.95 1.185.656.586 1.206.767 1.376.842.171.074.27.061.371-.055.102-.116.438-.512.556-.688.117-.176.234-.146.391-.088.156.059.988.467 1.157.552.171.084.285.127.327.198.041.072.041.423-.103.828z"/></svg>\n                                <span data-i18n="contact.info.whatsapp">Chat on WhatsApp</span>\n                            </a>'),
    
    # Missing tags in index.html like tours
    (r'(<h3 class="text-2xl[^>]*?)>Ancient Heritage Tour</h3>', r'\1 data-i18n="index.tours.tour1.title">Ancient Heritage Tour</h3>'),
    (r'(<h3 class="text-2xl[^>]*?)>Yala Leopard Safari</h3>', r'\1 data-i18n="index.tours.tour2.title">Yala Leopard Safari</h3>'),
    (r'(<h3 class="text-2xl[^>]*?)>Tea &amp; Train Odyssey</h3>', r'\1 data-i18n="index.tours.tour3.title">Tea &amp; Train Odyssey</h3>'),
    (r'(<h3 class="text-2xl[^>]*?)>Tea & Train Odyssey</h3>', r'\1 data-i18n="index.tours.tour3.title">Tea & Train Odyssey</h3>'),
]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for pattern, repl in replacements:
        # Avoid double-adding if already added
        if 'data-i18n' in repl and repl in content:
            continue
        content = re.sub(pattern, repl, content, flags=re.DOTALL)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Fixed missing translations in HTML files.")
