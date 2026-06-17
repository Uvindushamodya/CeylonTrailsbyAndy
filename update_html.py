import re
import os

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Nav
    content = content.replace('>Home</a>', ' data-i18n="nav.home">Home</a>')
    content = content.replace('>Tours</a>', ' data-i18n="nav.tours">Tours</a>')
    content = content.replace('>About Andy</a>', ' data-i18n="nav.about">About Andy</a>')
    content = content.replace('>Book Now</a>', ' data-i18n="nav.book">Book Now</a>')

    # Add language switcher in Desktop Nav
    desktop_nav_book_pattern = r'(<a href="contact.html" class="bg-brand-primary[^>]* data-i18n="nav.book">Book Now</a>\s*</div>)'
    desktop_nav_switcher = r'''<div class="flex items-center space-x-2 text-sm border-l border-slate-300 pl-4">
                        <a href="#" class="lang-switch-btn font-bold text-brand-primary" data-lang="en">EN</a>
                        <span class="text-slate-300">|</span>
                        <a href="#" class="lang-switch-btn text-slate-500 hover:text-brand-primary" data-lang="zh">中文</a>
                    </div>
                    \1'''
    content = re.sub(desktop_nav_book_pattern, desktop_nav_switcher, content, count=1)

    # Add language switcher in Mobile Nav
    mobile_nav_book_pattern = r'(<a href="contact.html" class="block px-3 py-2 text-brand-primary font-medium[^>]* data-i18n="nav.book">Book Now</a>\s*</div>)'
    mobile_nav_switcher = r'''\1
            <div class="px-3 py-2 flex space-x-3 border-t border-gray-100 mt-2 pt-2">
                <a href="#" class="lang-switch-btn font-bold text-brand-primary" data-lang="en">EN</a>
                <a href="#" class="lang-switch-btn text-slate-500" data-lang="zh">中文</a>
            </div>'''
    content = re.sub(mobile_nav_book_pattern, mobile_nav_switcher, content, count=1)

    # Footer
    content = content.replace('Crafting bespoke, unforgettable journeys across the beautiful island of Sri Lanka.</p>', 'Crafting bespoke, unforgettable journeys across the beautiful island of Sri Lanka.</p>'.replace('Crafting', '<span data-i18n="footer.desc">Crafting').replace('Lanka.</p>', 'Lanka.</span></p>'))
    content = content.replace('>Quick Links</h4>', ' data-i18n="footer.links">Quick Links</h4>')
    content = content.replace('>Contact Info</h4>', ' data-i18n="footer.contact">Contact Info</h4>')
    content = content.replace('<p>&copy; 2026 Andy Tours Sri Lanka. All rights reserved.</p>', '<p data-i18n="footer.rights">&copy; 2026 Andy Tours Sri Lanka. All rights reserved.</p>')

    # Scripts
    if '<script src="js/translations.js"></script>' not in content:
        content = content.replace('</body>', '    <script src="js/translations.js"></script>\n    <script src="js/i18n.js"></script>\n</body>')

    # Index specific
    if 'index.html' in filepath:
        content = content.replace('Discover the True <br/>Spirit of Sri Lanka\n                </h1>', 'Discover the True <br/>Spirit of Sri Lanka\n                </h1>'.replace('Discover', '<span data-i18n="index.hero.title">Discover').replace('Lanka', 'Lanka</span>'))
        content = content.replace('Journey through ancient ruins, lush tea plantations, and pristine beaches with Andy, your expert local guide.\n                </p>', 'Journey through ancient ruins, lush tea plantations, and pristine beaches with Andy, your expert local guide.\n                </p>'.replace('Journey', '<span data-i18n="index.hero.desc">Journey').replace('guide.', 'guide.</span>'))
        content = content.replace('>Explore Tours\n                    </a>', ' data-i18n="index.hero.explore">Explore Tours\n                    </a>')
        content = content.replace('>Contact Andy\n                    </a>', ' data-i18n="index.hero.contact">Contact Andy\n                    </a>')
        content = content.replace('>Meet Your Guide</h4>', ' data-i18n="index.about.subtitle">Meet Your Guide</h4>')
        content = content.replace('>Ayubowan! I\'m Andy.</h2>', ' data-i18n="index.about.title">Ayubowan! I\'m Andy.</h2>')
        content = content.replace('>With over 10 years of experience traversing the diverse landscapes of Sri Lanka, I bring the history, culture, and nature of my beautiful island to life. My passion is to offer authentic, unforgettable experiences tailored to your interests.\n                    </p>', ' data-i18n="index.about.desc1">With over 10 years of experience traversing the diverse landscapes of Sri Lanka, I bring the history, culture, and nature of my beautiful island to life. My passion is to offer authentic, unforgettable experiences tailored to your interests.\n                    </p>')
        content = content.replace('>Whether you are an adventure seeker, a history buff, or simply looking to relax by the ocean, I\'ll ensure your journey is seamless, safe, and truly magical.\n                    </p>', ' data-i18n="index.about.desc2">Whether you are an adventure seeker, a history buff, or simply looking to relax by the ocean, I\'ll ensure your journey is seamless, safe, and truly magical.\n                    </p>')
        content = content.replace('Read My Full Story \n                        <svg', '<span data-i18n="index.about.readmore">Read My Full Story</span> \n                        <svg')
        
        content = content.replace('>Popular Journeys</h4>', ' data-i18n="index.tours.subtitle">Popular Journeys</h4>')
        content = content.replace('>Unforgettable Experiences</h2>', ' data-i18n="index.tours.title">Unforgettable Experiences</h2>')
        content = content.replace('>Curated itineraries designed to showcase the very best of Sri Lanka, from the cultural triangle to the wild south.</p>', ' data-i18n="index.tours.desc">Curated itineraries designed to showcase the very best of Sri Lanka, from the cultural triangle to the wild south.</p>')
        
        content = content.replace('>Cultural Triangle\n                        </div>', ' data-i18n="index.tours.tour1.tag">Cultural Triangle\n                        </div>')
        content = content.replace('>5 Days</div>', ' data-i18n="index.tours.tour1.days">5 Days</div>')
        content = content.replace('>Ancient Heritage Tour</h3>', ' data-i18n="index.tours.tour1.title">Ancient Heritage Tour</h3>')
        content = content.replace('>Explore the majestic Sigiriya Rock Fortress, the ancient ruins of Polonnaruwa, and the sacred Dambulla Cave Temple.</p>', ' data-i18n="index.tours.tour1.desc">Explore the majestic Sigiriya Rock Fortress, the ancient ruins of Polonnaruwa, and the sacred Dambulla Cave Temple.</p>')
        content = content.replace('>From $450</span>', ' data-i18n="index.tours.tour1.price">From $450</span>')
        content = content.replace('>View Details &rarr;</a>', ' data-i18n="index.tours.viewdetails">View Details &rarr;</a>')

        content = content.replace('>Southern Wilds\n                        </div>', ' data-i18n="index.tours.tour2.tag">Southern Wilds\n                        </div>')
        content = content.replace('>3 Days</div>', ' data-i18n="index.tours.tour2.days">3 Days</div>')
        content = content.replace('>Yala Leopard Safari</h3>', ' data-i18n="index.tours.tour2.title">Yala Leopard Safari</h3>')
        content = content.replace('>Get up close with Sri Lanka\'s majestic leopards, elephants, and exotic birds in their natural habitat at Yala National Park.</p>', ' data-i18n="index.tours.tour2.desc">Get up close with Sri Lanka\'s majestic leopards, elephants, and exotic birds in their natural habitat at Yala National Park.</p>')
        content = content.replace('>From $320</span>', ' data-i18n="index.tours.tour2.price">From $320</span>')

        content = content.replace('>Hill Country\n                        </div>', ' data-i18n="index.tours.tour3.tag">Hill Country\n                        </div>')
        content = content.replace('>7 Days</div>', ' data-i18n="index.tours.tour3.days">7 Days</div>')
        content = content.replace('>Tea & Train Odyssey</h3>', ' data-i18n="index.tours.tour3.title">Tea & Train Odyssey</h3>')
        content = content.replace('>Experience the world-famous scenic train ride to Ella, hike through lush tea estates, and witness breathtaking waterfalls.</p>', ' data-i18n="index.tours.tour3.desc">Experience the world-famous scenic train ride to Ella, hike through lush tea estates, and witness breathtaking waterfalls.</p>')
        content = content.replace('>From $600</span>', ' data-i18n="index.tours.tour3.price">From $600</span>')

        content = content.replace('>View All Packages\n                </a>', ' data-i18n="index.tours.viewall">View All Packages\n                </a>')

        content = content.replace('>"Traveling with Andy was the highlight of our trip. His knowledge of the local history and secret spots that aren\'t in the guidebooks made our Sri Lankan adventure truly exceptional."\n            </p>', ' data-i18n="index.testi.text">"Traveling with Andy was the highlight of our trip. His knowledge of the local history and secret spots that aren\'t in the guidebooks made our Sri Lankan adventure truly exceptional."\n            </p>')
        content = content.replace('>Sarah & Mike</h5>', ' data-i18n="index.testi.name">Sarah & Mike</h5>')
        content = content.replace('>United Kingdom</p>', ' data-i18n="index.testi.loc">United Kingdom</p>')

    # Tours specific
    elif 'tours.html' in filepath:
        content = content.replace('>Our Tour Packages</h1>', ' data-i18n="tours.header.title">Our Tour Packages</h1>')
        content = content.replace('>Explore hand-crafted itineraries designed to give you the most authentic Sri Lankan experience.</p>', ' data-i18n="tours.header.desc">Explore hand-crafted itineraries designed to give you the most authentic Sri Lankan experience.</p>')
        content = content.replace('>per person / 5 days</span>', ' data-i18n="tours.tour1.price_desc">per person / 5 days</span>')
        content = content.replace('>Journey back in time and discover the ancient kingdoms of Sri Lanka. This tour takes you through the magnificent Sigiriya Rock Fortress, the well-preserved ruins of Polonnaruwa, and the stunning cave temples of Dambulla. Experience the rich history and vibrant culture of the island.\n                    </p>', ' data-i18n="tours.tour1.longdesc">Journey back in time and discover the ancient kingdoms of Sri Lanka. This tour takes you through the magnificent Sigiriya Rock Fortress, the well-preserved ruins of Polonnaruwa, and the stunning cave temples of Dambulla. Experience the rich history and vibrant culture of the island.\n                    </p>')
        content = content.replace('</svg> Sigiriya Lion Rock Climb</li>', '</svg> <span data-i18n="tours.tour1.li1">Sigiriya Lion Rock Climb</span></li>')
        content = content.replace('</svg> Polonnaruwa Ancient City Tour</li>', '</svg> <span data-i18n="tours.tour1.li2">Polonnaruwa Ancient City Tour</span></li>')
        content = content.replace('</svg> Dambulla Cave Temple Visit</li>', '</svg> <span data-i18n="tours.tour1.li3">Dambulla Cave Temple Visit</span></li>')
        content = content.replace('</svg> Minneriya Elephant Safari</li>', '</svg> <span data-i18n="tours.tour1.li4">Minneriya Elephant Safari</span></li>')
        content = content.replace('>Book This Tour</a>', ' data-i18n="tours.book_btn">Book This Tour</a>')

        content = content.replace('>per person / 3 days</span>', ' data-i18n="tours.tour2.price_desc">per person / 3 days</span>')
        content = content.replace('>Immerse yourself in the wild beauty of southern Sri Lanka. This thrilling safari adventure takes you deep into Yala National Park, home to one of the highest densities of leopards in the world, as well as majestic elephants, sloth bears, and diverse birdlife.\n                    </p>', ' data-i18n="tours.tour2.longdesc">Immerse yourself in the wild beauty of southern Sri Lanka. This thrilling safari adventure takes you deep into Yala National Park, home to one of the highest densities of leopards in the world, as well as majestic elephants, sloth bears, and diverse birdlife.\n                    </p>')
        content = content.replace('</svg> Full Day Jeep Safari in Yala</li>', '</svg> <span data-i18n="tours.tour2.li1">Full Day Jeep Safari in Yala</span></li>')
        content = content.replace('</svg> Bundala Bird Sanctuary Visit</li>', '</svg> <span data-i18n="tours.tour2.li2">Bundala Bird Sanctuary Visit</span></li>')
        content = content.replace('</svg> Relaxing on Mirissa Beach</li>', '</svg> <span data-i18n="tours.tour2.li3">Relaxing on Mirissa Beach</span></li>')

        content = content.replace('>per person / 7 days</span>', ' data-i18n="tours.tour3.price_desc">per person / 7 days</span>')
        content = content.replace('>Escape to the misty mountains of Sri Lanka. Wind your way through rolling tea estates on one of the world\'s most scenic train rides. Hike to spectacular viewpoints like Little Adam\'s Peak and witness the roaring waterfalls that dot the central highlands.\n                    </p>', ' data-i18n="tours.tour3.longdesc">Escape to the misty mountains of Sri Lanka. Wind your way through rolling tea estates on one of the world\'s most scenic train rides. Hike to spectacular viewpoints like Little Adam\'s Peak and witness the roaring waterfalls that dot the central highlands.\n                    </p>')
        content = content.replace('</svg> Kandy Temple of the Tooth</li>', '</svg> <span data-i18n="tours.tour3.li1">Kandy Temple of the Tooth</span></li>')
        content = content.replace('</svg> Nuwara Eliya Tea Factory Tour</li>', '</svg> <span data-i18n="tours.tour3.li2">Nuwara Eliya Tea Factory Tour</span></li>')
        content = content.replace('</svg> Iconic Train Ride to Ella</li>', '</svg> <span data-i18n="tours.tour3.li3">Iconic Train Ride to Ella</span></li>')
        content = content.replace('</svg> Nine Arches Bridge & Little Adam\'s Peak</li>', '</svg> <span data-i18n="tours.tour3.li4">Nine Arches Bridge & Little Adam\'s Peak</span></li>')

    # About specific
    elif 'about.html' in filepath:
        content = content.replace('>About Andy</h1>', ' data-i18n="about.header.title">About Andy</h1>')
        content = content.replace('>Your dedicated guide to discovering the hidden gems and rich history of Sri Lanka.</p>', ' data-i18n="about.header.desc">Your dedicated guide to discovering the hidden gems and rich history of Sri Lanka.</p>')
        content = content.replace('>A Passionate Local Expert</h2>', ' data-i18n="about.content.title">A Passionate Local Expert</h2>')
        content = content.replace('>Born and raised in the heart of Sri Lanka, my connection to this land goes far beyond knowing the routes. I grew up listening to the ancient tales of kings, exploring the dense jungles, and understanding the rhythm of our vibrant culture.\n                    </p>', ' data-i18n="about.content.p1">Born and raised in the heart of Sri Lanka, my connection to this land goes far beyond knowing the routes. I grew up listening to the ancient tales of kings, exploring the dense jungles, and understanding the rhythm of our vibrant culture.\n                    </p>')
        content = content.replace('>For over a decade, I have had the privilege of sharing the magic of Sri Lanka with travelers from all corners of the globe. Being a certified National Tourist Guide Lecturer, I combine deep historical knowledge with an adventurous spirit.\n                    </p>', ' data-i18n="about.content.p2">For over a decade, I have had the privilege of sharing the magic of Sri Lanka with travelers from all corners of the globe. Being a certified National Tourist Guide Lecturer, I combine deep historical knowledge with an adventurous spirit.\n                    </p>')
        content = content.replace('>Years Experience</p>', ' data-i18n="about.stats.exp">Years Experience</p>')
        content = content.replace('>Happy Travelers</p>', ' data-i18n="about.stats.happy">Happy Travelers</p>')
        content = content.replace('>SLTDA Guide</p>', ' data-i18n="about.stats.cert">SLTDA Guide</p>')
        content = content.replace('>TripAdvisor</p>', ' data-i18n="about.stats.stars">TripAdvisor</p>')

    # Contact specific
    elif 'contact.html' in filepath:
        content = content.replace(">Let's Plan Your Trip</h1>", ' data-i18n="contact.header.title">Let\'s Plan Your Trip</h1>')
        content = content.replace('>Get in touch to customize your itinerary or book one of our popular packages.</p>', ' data-i18n="contact.header.desc">Get in touch to customize your itinerary or book one of our popular packages.</p>')
        content = content.replace('>Contact Details</h3>', ' data-i18n="contact.details.title">Contact Details</h3>')
        content = content.replace('>Phone & WhatsApp</h4>', ' data-i18n="contact.details.phone">Phone & WhatsApp</h4>')
        content = content.replace('>Email</h4>', ' data-i18n="contact.details.email">Email</h4>')
        content = content.replace('Chat on WhatsApp\n                            </a>', '<span data-i18n="contact.details.chat">Chat on WhatsApp</span>\n                            </a>')
        content = content.replace('>Send an Inquiry</h3>', ' data-i18n="contact.form.title">Send an Inquiry</h3>')
        content = content.replace('>Full Name</label>', ' data-i18n="contact.form.name">Full Name</label>')
        content = content.replace('placeholder="John Doe"', 'placeholder="John Doe" data-i18n="contact.form.name_placeholder"')
        content = content.replace('>Email Address</label>', ' data-i18n="contact.form.email">Email Address</label>')
        content = content.replace('placeholder="john@example.com"', 'placeholder="john@example.com" data-i18n="contact.form.email_placeholder"')
        content = content.replace('>Interested Tour</label>', ' data-i18n="contact.form.tour">Interested Tour</label>')
        content = content.replace('>Select a package...</option>', ' data-i18n="contact.form.tour_opt1">Select a package...</option>')
        content = content.replace('>Cultural Triangle (5 Days)</option>', ' data-i18n="contact.form.tour_opt2">Cultural Triangle (5 Days)</option>')
        content = content.replace('>Yala Leopard Safari (3 Days)</option>', ' data-i18n="contact.form.tour_opt3">Yala Leopard Safari (3 Days)</option>')
        content = content.replace('>Hill Country Odyssey (7 Days)</option>', ' data-i18n="contact.form.tour_opt4">Hill Country Odyssey (7 Days)</option>')
        content = content.replace('>Custom Itinerary</option>', ' data-i18n="contact.form.tour_opt5">Custom Itinerary</option>')
        content = content.replace('>Approximate Date</label>', ' data-i18n="contact.form.date">Approximate Date</label>')
        content = content.replace('>Your Message or Custom Requirements</label>', ' data-i18n="contact.form.message">Your Message or Custom Requirements</label>')
        content = content.replace('placeholder="Tell me about your travel preferences..."', 'placeholder="Tell me about your travel preferences..." data-i18n="contact.form.message_placeholder"')
        content = content.replace('>\n                                Send Inquiry\n                            </button>', ' data-i18n="contact.form.send">\n                                Send Inquiry\n                            </button>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for file in ['index.html', 'tours.html', 'about.html', 'contact.html']:
    update_file(file)
    print(f"Updated {file}")
