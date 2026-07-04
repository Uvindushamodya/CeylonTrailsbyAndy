import re

# 1. Update translations
with open('d:/Andy/CeylonTrailsbyAndy/js/translations.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

en_qr_text = '''        "contact.qr.title": "Connect on Social Media",
        "contact.qr.desc": "Scan the QR codes below to add Andy on your preferred platform.",
        "contact.qr.kwai": "Scan to Connect on Kwai",
        "contact.qr.line": "Add on LINE",
        "contact.qr.instagram": "Follow on Instagram",
'''
zh_qr_text = '''        "contact.qr.title": "在社交媒体上联系",
        "contact.qr.desc": "扫描下方二维码，在您偏好的平台上添加安迪。",
        "contact.qr.kwai": "扫码在快手上联系",
        "contact.qr.line": "在LINE上添加",
        "contact.qr.instagram": "在Instagram上关注",
'''

# Insert in english block after contact.info.whatsapp or contact.form.send
# Actually it's easier to append before "    }," at the end of each block.
# English block ends around "    },"
# Let's just insert it after contact.info.whatsapp

js_content = js_content.replace('"contact.info.whatsapp": "Chat on WhatsApp"', '"contact.info.whatsapp": "Chat on WhatsApp",\n' + en_qr_text)
js_content = js_content.replace('"contact.info.whatsapp": "在 WhatsApp 上聊天"', '"contact.info.whatsapp": "在 WhatsApp 上聊天",\n' + zh_qr_text)

with open('d:/Andy/CeylonTrailsbyAndy/js/translations.js', 'w', encoding='utf-8') as f:
    f.write(js_content)


# 2. Update contact.html
with open('d:/Andy/CeylonTrailsbyAndy/contact.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

qr_section_html = """
    <!-- Social QR Codes Section -->
    <section class="py-20 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-3xl font-sans font-bold text-brand-dark mb-4" data-i18n="contact.qr.title">Connect on Social Media</h2>
                <p class="text-slate-600 text-lg" data-i18n="contact.qr.desc">Scan the QR codes below to add Andy on your preferred platform.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Kwai -->
                <div class="bg-slate-50 rounded-2xl p-8 border border-slate-100 flex flex-col items-center text-center hover:shadow-xl transition-shadow duration-300">
                    <h3 class="text-xl font-bold text-brand-dark mb-2">Kwai</h3>
                    <p class="text-slate-500 text-sm mb-6" data-i18n="contact.qr.kwai">Scan to Connect on Kwai</p>
                    <div class="w-48 h-48 bg-white p-2 rounded-xl shadow-sm border border-slate-200">
                        <img src="images/qr_kwai.png" alt="Kwai QR Code" class="w-full h-full object-contain">
                    </div>
                    <p class="mt-6 font-semibold text-brand-primary">@AndyTours</p>
                </div>

                <!-- LINE -->
                <div class="bg-slate-50 rounded-2xl p-8 border border-slate-100 flex flex-col items-center text-center hover:shadow-xl transition-shadow duration-300">
                    <h3 class="text-xl font-bold text-[#00C300] mb-2">LINE</h3>
                    <p class="text-slate-500 text-sm mb-6" data-i18n="contact.qr.line">Add on LINE</p>
                    <div class="w-48 h-48 bg-white p-2 rounded-xl shadow-sm border border-slate-200">
                        <img src="images/qr_line.png" alt="LINE QR Code" class="w-full h-full object-contain">
                    </div>
                    <p class="mt-6 font-semibold text-[#00C300]">AndySriLanka</p>
                </div>

                <!-- Instagram -->
                <div class="bg-slate-50 rounded-2xl p-8 border border-slate-100 flex flex-col items-center text-center hover:shadow-xl transition-shadow duration-300">
                    <h3 class="text-xl font-bold text-[#E1306C] mb-2">Instagram</h3>
                    <p class="text-slate-500 text-sm mb-6" data-i18n="contact.qr.instagram">Follow on Instagram</p>
                    <div class="w-48 h-48 bg-white p-2 rounded-xl shadow-sm border border-slate-200">
                        <img src="images/qr_instagram.png" alt="Instagram QR Code" class="w-full h-full object-contain">
                    </div>
                    <p class="mt-6 font-semibold text-[#E1306C]">@ceylontrailsbyandy</p>
                </div>
            </div>
        </div>
    </section>
"""

# Insert before footer
html_content = html_content.replace('<!-- Footer -->', qr_section_html + '\n    <!-- Footer -->')

with open('d:/Andy/CeylonTrailsbyAndy/contact.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updates applied successfully.")
