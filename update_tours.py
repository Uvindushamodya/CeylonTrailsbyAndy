import re

# Tours data for index.html
index_tour_template = """                <!-- Tour Card {idx} -->
                <div class="bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 group">
                    <div class="relative h-64 overflow-hidden">
                        <img src="{image}" alt="Tour Image" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700" />
                        <div class="absolute top-4 right-4 bg-white/90 backdrop-blur px-3 py-1 rounded-full text-sm font-semibold text-brand-dark shadow" data-i18n="index.tours.tour{idx}.days">...</div>
                    </div>
                    <div class="p-8">
                        <div class="flex items-center text-brand-secondary text-sm font-medium mb-3">
                            <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                            <span data-i18n="index.tours.tour{idx}.tag">...</span>
                        </div>
                        <h3 class="text-2xl font-sans font-bold text-brand-dark mb-3" data-i18n="index.tours.tour{idx}.title">...</h3>
                        <p class="text-slate-600 mb-6 line-clamp-2" data-i18n="index.tours.tour{idx}.desc">...</p>
                        <div class="flex items-center justify-between">
                            <span class="text-xl font-bold text-brand-primary" data-i18n="index.tours.tour{idx}.price">...</span>
                            <a href="tours.html" class="text-sm font-semibold text-slate-800 hover:text-brand-primary transition-colors" data-i18n="index.tours.viewdetails">View Details &rarr;</a>
                        </div>
                    </div>
                </div>"""

# Tours data for tours.html
tours_tour_template = """            <!-- Tour {idx} -->
            <div class="bg-white rounded-3xl overflow-hidden shadow-xl flex flex-col md:{flex_dir} group">
                <div class="md:w-2/5 relative overflow-hidden">
                    <img src="{image}" alt="Tour Image" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700 min-h-[300px]" />
                </div>
                <div class="p-8 md:p-12 md:w-3/5 flex flex-col justify-center">
                    <div class="flex justify-between items-start mb-4">
                        <div>
                            <span class="text-brand-secondary font-semibold tracking-wider uppercase text-sm mb-2 block" data-i18n="index.tours.tour{idx}.tag">...</span>
                            <h2 class="text-3xl font-sans font-bold text-brand-dark" data-i18n="index.tours.tour{idx}.title">...</h2>
                        </div>
                        <div class="text-{text_align}">
                            <span class="block text-2xl font-bold text-brand-primary" data-i18n="index.tours.tour{idx}.price">...</span>
                            <span class="text-sm text-slate-500" data-i18n="tours.tour{idx}.price_desc">...</span>
                        </div>
                    </div>
                    <p class="text-slate-600 mb-6 leading-relaxed" data-i18n="tours.tour{idx}.longdesc">...</p>
                    <ul class="mb-8 space-y-2 text-slate-600">
                        <li class="flex items-center"><svg class="w-5 h-5 text-brand-secondary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> <span data-i18n="tours.tour{idx}.li1">...</span></li>
                        <li class="flex items-center"><svg class="w-5 h-5 text-brand-secondary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> <span data-i18n="tours.tour{idx}.li2">...</span></li>
                        <li class="flex items-center"><svg class="w-5 h-5 text-brand-secondary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> <span data-i18n="tours.tour{idx}.li3">...</span></li>
                        <li class="flex items-center"><svg class="w-5 h-5 text-brand-secondary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> <span data-i18n="tours.tour{idx}.li4">...</span></li>
                    </ul>
                    <div>
                        <a href="contact.html" class="inline-block bg-brand-primary text-white px-8 py-3 rounded-full font-semibold hover:bg-sky-600 transition-colors shadow-md" data-i18n="tours.book_btn">Book This Tour</a>
                    </div>
                </div>
            </div>"""

images = [
    "images/sigiriya.png",
    "images/hero_slide_1.png",
    "images/jaffna_nallur.png",
    "images/trincomalee_beach.png",
    "images/yala.png",
    "images/pinnawala_elephants.png"
]

index_tours_html = []
for i in range(6):
    index_tours_html.append(index_tour_template.format(idx=i+1, image=images[i]))

tours_tours_html = []
for i in range(6):
    flex_dir = "flex-row" if i % 2 == 0 else "flex-row-reverse"
    text_align = "right" if i % 2 == 0 else "left md:text-right"
    tours_tours_html.append(tours_tour_template.format(idx=i+1, image=images[i], flex_dir=flex_dir, text_align=text_align))


with open('d:/Andy/CeylonTrailsbyAndy/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

index_pattern = r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">.*?</div>\s*<div class="mt-16 text-center">'
index_replacement = f'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">\n' + '\n\n'.join(index_tours_html) + '\n            </div>\n            <div class="mt-16 text-center">'
index_content = re.sub(index_pattern, index_replacement, index_content, flags=re.DOTALL)

with open('d:/Andy/CeylonTrailsbyAndy/index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)


with open('d:/Andy/CeylonTrailsbyAndy/tours.html', 'r', encoding='utf-8') as f:
    tours_content = f.read()

tours_pattern = r'<section class="py-20">\s*<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-16">.*?</div>\s*</section>'
tours_replacement = f'<section class="py-20">\n        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-16">\n\n' + '\n\n'.join(tours_tours_html) + '\n\n        </div>\n    </section>'
tours_content = re.sub(tours_pattern, tours_replacement, tours_content, flags=re.DOTALL)

with open('d:/Andy/CeylonTrailsbyAndy/tours.html', 'w', encoding='utf-8') as f:
    f.write(tours_content)


with open('d:/Andy/CeylonTrailsbyAndy/contact.html', 'r', encoding='utf-8') as f:
    contact_content = f.read()

contact_pattern = r'<select name="tour" .*?</select>'
contact_replacement = """<select name="tour" class="w-full px-4 py-3 border border-slate-300 rounded-lg focus:ring-2 focus:ring-brand-primary focus:border-brand-primary outline-none transition-all appearance-none bg-white">
                                <option value="" data-i18n="contact.form.tour_opt1">Select a package...</option>
                                <option value="tour1" data-i18n="contact.form.tour_opt2">5 Day Sri Lanka Highlights Tour</option>
                                <option value="tour2" data-i18n="contact.form.tour_opt3">7-Day Cultural Tour</option>
                                <option value="tour3" data-i18n="contact.form.tour_opt4">10-Day Jaffna & Classic Triangle</option>
                                <option value="tour4" data-i18n="contact.form.tour_opt5">8-Day Culture & Trincomalee Beach</option>
                                <option value="tour5" data-i18n="contact.form.tour_opt6">7-Day Culture & Wildlife Tour</option>
                                <option value="tour6" data-i18n="contact.form.tour_opt7">6-Day Scenic Beauty & Wildlife</option>
                                <option value="custom" data-i18n="contact.form.tour_opt8">Custom Itinerary</option>
                            </select>"""
contact_content = re.sub(contact_pattern, contact_replacement, contact_content, flags=re.DOTALL)

with open('d:/Andy/CeylonTrailsbyAndy/contact.html', 'w', encoding='utf-8') as f:
    f.write(contact_content)

print("Updates applied successfully.")
