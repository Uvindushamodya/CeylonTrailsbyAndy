import re
import os

files = ['index.html', 'tours.html', 'about.html', 'contact.html']

patterns = [
    # index.html
    (r'(<p[^>]*)(>\s*With over 10 years of experience traversing the diverse landscapes of Sri Lanka, I bring the history, culture, and nature of my beautiful island to life. My passion is to offer authentic, unforgettable experiences tailored to your interests.\s*</p>)', r'\1 data-i18n="index.about.desc1"\2'),
    (r'(<p[^>]*)(>\s*Whether you are an adventure seeker, a history buff, or simply looking to relax by the ocean, I\'ll ensure your journey is seamless, safe, and truly magical.\s*</p>)', r'\1 data-i18n="index.about.desc2"\2'),
    (r'(<p[^>]*)(>\s*"Traveling with Andy was the highlight of our trip. His knowledge of the local history and secret spots that aren\'t in the guidebooks made our Sri Lankan adventure truly exceptional."\s*</p>)', r'\1 data-i18n="index.testi.text"\2'),
    
    # tours.html
    (r'(<p[^>]*)(>\s*Explore hand-crafted itineraries designed to give you the most authentic Sri Lankan experience.\s*</p>)', r'\1 data-i18n="tours.header.desc"\2'),
    (r'(<p[^>]*)(>\s*Journey back in time and discover the ancient kingdoms of Sri Lanka. This tour takes you through the magnificent Sigiriya Rock Fortress, the well-preserved ruins of Polonnaruwa, and the stunning cave temples of Dambulla. Experience the rich history and vibrant culture of the island.\s*</p>)', r'\1 data-i18n="tours.tour1.longdesc"\2'),
    (r'(<p[^>]*)(>\s*Immerse yourself in the wild beauty of southern Sri Lanka. This thrilling safari adventure takes you deep into Yala National Park, home to one of the highest densities of leopards in the world, as well as majestic elephants, sloth bears, and diverse birdlife.\s*</p>)', r'\1 data-i18n="tours.tour2.longdesc"\2'),
    (r'(<p[^>]*)(>\s*Escape to the misty mountains of Sri Lanka. Wind your way through rolling tea estates on one of the world\'s most scenic train rides. Hike to spectacular viewpoints like Little Adam\'s Peak and witness the roaring waterfalls that dot the central highlands.\s*</p>)', r'\1 data-i18n="tours.tour3.longdesc"\2'),
    
    # Check if list items in tours.html are missing
    (r'(<li[^>]*>\s*<svg[^>]*>.*?</svg>\s*)(Sigiriya Lion Rock Climb)(\s*</li>)', r'\1<span data-i18n="tours.tour1.li1">\2</span>\3'),
    (r'(<li[^>]*>\s*<svg[^>]*>.*?</svg>\s*)(Polonnaruwa Ancient City Tour)(\s*</li>)', r'\1<span data-i18n="tours.tour1.li2">\2</span>\3'),
    (r'(<li[^>]*>\s*<svg[^>]*>.*?</svg>\s*)(Dambulla Cave Temple Visit)(\s*</li>)', r'\1<span data-i18n="tours.tour1.li3">\2</span>\3'),
    (r'(<li[^>]*>\s*<svg[^>]*>.*?</svg>\s*)(Minneriya Elephant Safari)(\s*</li>)', r'\1<span data-i18n="tours.tour1.li4">\2</span>\3'),
    (r'(<li[^>]*>\s*<svg[^>]*>.*?</svg>\s*)(Full Day Jeep Safari in Yala)(\s*</li>)', r'\1<span data-i18n="tours.tour2.li1">\2</span>\3'),
    (r'(<li[^>]*>\s*<svg[^>]*>.*?</svg>\s*)(Bundala Bird Sanctuary Visit)(\s*</li>)', r'\1<span data-i18n="tours.tour2.li2">\2</span>\3'),
    (r'(<li[^>]*>\s*<svg[^>]*>.*?</svg>\s*)(Relaxing on Mirissa Beach)(\s*</li>)', r'\1<span data-i18n="tours.tour2.li3">\2</span>\3'),
    (r'(<li[^>]*>\s*<svg[^>]*>.*?</svg>\s*)(Kandy Temple of the Tooth)(\s*</li>)', r'\1<span data-i18n="tours.tour3.li1">\2</span>\3'),
    (r'(<li[^>]*>\s*<svg[^>]*>.*?</svg>\s*)(Nuwara Eliya Tea Factory Tour)(\s*</li>)', r'\1<span data-i18n="tours.tour3.li2">\2</span>\3'),
    (r'(<li[^>]*>\s*<svg[^>]*>.*?</svg>\s*)(Iconic Train Ride to Ella)(\s*</li>)', r'\1<span data-i18n="tours.tour3.li3">\2</span>\3'),
    (r'(<li[^>]*>\s*<svg[^>]*>.*?</svg>\s*)(Nine Arches Bridge &amp; Little Adam\'s Peak)(\s*</li>)', r'\1<span data-i18n="tours.tour3.li4">\2</span>\3'),
    (r'(<li[^>]*>\s*<svg[^>]*>.*?</svg>\s*)(Nine Arches Bridge & Little Adam\'s Peak)(\s*</li>)', r'\1<span data-i18n="tours.tour3.li4">\2</span>\3'),
    
    # about.html
    (r'(<p[^>]*)(>\s*Your dedicated guide to discovering the hidden gems and rich history of Sri Lanka.\s*</p>)', r'\1 data-i18n="about.header.desc"\2'),
    (r'(<p[^>]*)(>\s*Born and raised in the heart of Sri Lanka, my connection to this land goes far beyond knowing the routes. I grew up listening to the ancient tales of kings, exploring the dense jungles, and understanding the rhythm of our vibrant culture.\s*</p>)', r'\1 data-i18n="about.content.p1"\2'),
    (r'(<p[^>]*)(>\s*For over a decade, I have had the privilege of sharing the magic of Sri Lanka with travelers from all corners of the globe. Being a certified National Tourist Guide Lecturer, I combine deep historical knowledge with an adventurous spirit.\s*</p>)', r'\1 data-i18n="about.content.p2"\2'),
    
    # contact.html
    (r'(<p[^>]*)(>\s*Get in touch to customize your itinerary or book one of our popular packages.\s*</p>)', r'\1 data-i18n="contact.header.desc"\2'),
    
    # Any other untranslated spans/divs:
    # "Book This Tour" in tours.html
    (r'(<a[^>]*href="contact.html"[^>]*)(>\s*Book This Tour\s*</a>)', r'\1 data-i18n="tours.book_btn"\2'),
    
    # "Let's Plan Your Trip" in contact.html
    (r'(<h1[^>]*)(>\s*Let\'s Plan Your Trip\s*</h1>)', r'\1 data-i18n="contact.header.title"\2'),
]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    for pattern, repl in patterns:
        new_content = re.sub(pattern, repl, content, flags=re.DOTALL)
        if new_content != content:
            content = new_content
            modified = True
            
    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
