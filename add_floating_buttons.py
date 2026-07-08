import os
import re

floating_buttons_html = """
    <!-- Floating Contact Buttons -->
    <div class="fixed bottom-6 right-6 flex flex-col space-y-4 z-50">
        <!-- WeChat Button -->
        <button id="open-wechat-modal" class="w-14 h-14 rounded-full flex items-center justify-center text-white shadow-lg hover:scale-110 transition-transform duration-300" style="background-color: #07C160;" aria-label="Contact on WeChat">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="28" height="28" fill="currentColor"><path d="M8.618 1.492c-4.757 0-8.618 3.252-8.618 7.258 0 2.217 1.157 4.195 2.973 5.53-.223 1.127-.728 2.458-.871 2.825-.035.088-.047.168.01.218.064.054.146.037.218.006 0 0 1.954-.852 3.14-1.666a9.421 9.421 0 003.148.544c.404 0 .798-.024 1.185-.067-.282-.573-.44-1.212-.44-1.882 0-3.87 3.655-7.005 8.164-7.005.109 0 .216.004.323.01C16.92 3.425 13.044 1.492 8.618 1.492zm1.68 3.99c.563 0 1.018.397 1.018.887 0 .491-.455.888-1.018.888-.562 0-1.018-.397-1.018-.888 0-.49.456-.887 1.018-.887zm-4.324 0c.563 0 1.018.397 1.018.887 0 .491-.455.888-1.018.888-.562 0-1.018-.397-1.018-.888 0-.49.456-.887 1.018-.887zm10.021 2.906c-3.645 0-6.6 2.502-6.6 5.589 0 3.087 2.955 5.589 6.6 5.589.923 0 1.802-.178 2.597-.504 1.002.686 2.64 1.353 2.64 1.353.059.025.127.042.179-.001.047-.04.037-.105.01-.177-.118-.306-.532-1.385-.717-2.302 1.547-1.127 2.491-2.8 2.491-4.664 0-3.087-2.955-5.589-6.6-5.589zm-1.895 2.673c.47 0 .85.333.85.742 0 .41-.38.742-.85.742-.469 0-.85-.332-.85-.742 0-.41.381-.742.85-.742zm3.79 0c.47 0 .85.333.85.742 0 .41-.38.742-.85.742-.469 0-.85-.332-.85-.742 0-.41.381-.742.85-.742z"/></svg>
        </button>
        <!-- LINE Button -->
        <button id="open-line-modal" class="w-14 h-14 rounded-full flex items-center justify-center shadow-lg hover:scale-110 transition-transform duration-300 overflow-hidden" aria-label="Contact on LINE">
            <img src="images/line_button_bg.png" alt="LINE Chat" class="w-full h-full object-cover">
        </button>
        <!-- WhatsApp Button -->
        <a href="https://wa.me/94775414668" target="_blank" class="w-14 h-14 rounded-full flex items-center justify-center text-white shadow-lg hover:scale-110 transition-transform duration-300" style="background-color: #25D366;" aria-label="Contact on WhatsApp">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="28" height="28" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
        </a>
    </div>

    <!-- WeChat Modal -->
    <div id="wechat-modal" class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50 hidden backdrop-blur-sm px-4">
        <div class="bg-white rounded-2xl shadow-xl w-full max-w-sm overflow-hidden text-center">
            <div class="bg-[#07C160] text-white p-6 relative">
                <h3 class="text-xl font-bold font-sans">Connect on WeChat</h3>
                <button id="close-wechat-modal" class="absolute top-6 right-6 text-white/80 hover:text-white transition-colors">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                </button>
            </div>
            <div class="p-8">
                <p class="text-slate-600 mb-6">Scan the QR code below or add our WeChat ID to start chatting!</p>
                <div class="w-48 h-48 bg-slate-100 mx-auto rounded-lg mb-6 flex items-center justify-center border border-slate-200 p-2">
                    <img src="images/qr_wechat.jpg" alt="WeChat QR Code" class="w-full h-full object-contain">
                </div>
                <div class="bg-slate-50 p-4 rounded-lg flex items-center justify-between border border-slate-200">
                    <div>
                        <p class="text-xs text-slate-500 font-semibold uppercase tracking-wider text-left">WeChat ID</p>
                        <p id="wechat-id" class="font-bold text-slate-800 text-lg">guideanda</p>
                    </div>
                    <button onclick="navigator.clipboard.writeText(document.getElementById('wechat-id').innerText); alert('WeChat ID copied!');" class="text-[#07C160] hover:text-[#069e4f] font-bold text-sm bg-[#07C160]/10 px-3 py-2 rounded-md transition-colors">
                        Copy
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- LINE Modal -->
    <div id="line-modal" class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50 hidden backdrop-blur-sm px-4">
        <div class="bg-white rounded-2xl shadow-xl w-full max-w-sm overflow-hidden text-center">
            <div class="bg-[#00C300] text-white p-6 relative">
                <h3 class="text-xl font-bold font-sans">Connect on LINE</h3>
                <button id="close-line-modal" class="absolute top-6 right-6 text-white/80 hover:text-white transition-colors">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                </button>
            </div>
            <div class="p-8">
                <p class="text-slate-600 mb-6">Scan the QR code below to add us on LINE!</p>
                <div class="w-48 h-48 bg-slate-100 mx-auto rounded-lg flex items-center justify-center border border-slate-200 p-2">
                    <img src="images/qr_line.jpeg" alt="LINE QR Code" class="w-full h-full object-contain">
                </div>
            </div>
        </div>
    </div>
"""

for file in ['index.html', 'about.html', 'tours.html', 'contact.html']:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove old floating buttons and wechat modal
    content = re.sub(r'<!-- Floating Contact Buttons -->.*?(?=<script src="js/translations\.js">)', '', content, flags=re.DOTALL)
    
    # 2. Remove inline wechat logic if it exists (in index.html)
    content = re.sub(r'<script>\s*// WeChat Modal Logic.*?</script>', '', content, flags=re.DOTALL)
    
    # 3. Add modals script before </body>
    if '<script src="js/modals.js"></script>' not in content:
        content = content.replace('</body>', '    <script src="js/modals.js"></script>\n</body>')
        
    # 4. Inject new floating buttons right before <script src="js/translations.js">
    # Wait, the best place is to put it right before <script src="js/translations.js">
    # because that's where the old one was removed.
    if "<!-- Floating Contact Buttons -->" not in content:
        content = content.replace('<script src="js/translations.js">', floating_buttons_html + '\n    <script src="js/translations.js">')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Floating buttons updated in all HTML files.")
