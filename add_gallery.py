import re

# 1. Update translations
with open('d:/Andy/CeylonTrailsbyAndy/js/translations.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

en_gallery = '''        "index.gallery.subtitle": "Travel Memories",
        "index.gallery.title": "Moments with Our Guests",
        "index.gallery.desc": "A glimpse into the unforgettable journeys and happy faces from our past tours.",
'''
zh_gallery = '''        "index.gallery.subtitle": "旅行回忆",
        "index.gallery.title": "与客人的美好瞬间",
        "index.gallery.desc": "回顾我们过去旅程中难忘的瞬间和幸福的笑脸。",
'''

js_content = js_content.replace('"index.tours.viewall": "View All Packages",', '"index.tours.viewall": "View All Packages",\n' + en_gallery)
js_content = js_content.replace('"index.tours.viewall": "查看所有套餐",', '"index.tours.viewall": "查看所有套餐",\n' + zh_gallery)

with open('d:/Andy/CeylonTrailsbyAndy/js/translations.js', 'w', encoding='utf-8') as f:
    f.write(js_content)


# 2. Update index.html
with open('d:/Andy/CeylonTrailsbyAndy/index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Fix the broken section tag
html_content = html_content.replace('</sect    <!-- Customer Reviews Slider -->', '</section>\n\n    <!-- Customer Reviews Slider -->')

gallery_html = """
    <!-- Gallery Section -->
    <section class="py-24 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h4 class="text-brand-primary font-semibold tracking-wider uppercase mb-2" data-i18n="index.gallery.subtitle">Travel Memories</h4>
                <h2 class="text-4xl font-sans font-bold text-brand-dark mb-6" data-i18n="index.gallery.title">Moments with Our Guests</h2>
                <p class="text-slate-600 text-lg" data-i18n="index.gallery.desc">A glimpse into the unforgettable journeys and happy faces from our past tours.</p>
            </div>

            <div class="grid grid-cols-2 md:grid-cols-3 gap-4 md:gap-6">
                <div class="overflow-hidden rounded-2xl group">
                    <img src="images/gallery/gallery_1.png" alt="Gallery Image 1" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700 ease-in-out aspect-square">
                </div>
                <div class="overflow-hidden rounded-2xl group">
                    <img src="images/gallery/gallery_2.png" alt="Gallery Image 2" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700 ease-in-out aspect-square">
                </div>
                <div class="overflow-hidden rounded-2xl group">
                    <img src="images/gallery/gallery_3.png" alt="Gallery Image 3" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700 ease-in-out aspect-square">
                </div>
                <div class="overflow-hidden rounded-2xl group">
                    <img src="images/gallery/gallery_4.png" alt="Gallery Image 4" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700 ease-in-out aspect-square">
                </div>
                <div class="overflow-hidden rounded-2xl group">
                    <img src="images/gallery/gallery_5.png" alt="Gallery Image 5" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700 ease-in-out aspect-square">
                </div>
                <div class="overflow-hidden rounded-2xl group">
                    <img src="images/gallery/gallery_6.png" alt="Gallery Image 6" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700 ease-in-out aspect-square">
                </div>
            </div>
        </div>
    </section>
"""

html_content = html_content.replace('<!-- Customer Reviews Slider -->', gallery_html + '\n    <!-- Customer Reviews Slider -->')

with open('d:/Andy/CeylonTrailsbyAndy/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated index.html and translations.js successfully.")
