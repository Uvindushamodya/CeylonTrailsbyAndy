document.addEventListener('DOMContentLoaded', () => {
    const defaultLang = 'en';
    let currentLang = localStorage.getItem('site_lang') || defaultLang;

    function applyTranslations(lang) {
        document.querySelectorAll('[data-i18n]').forEach(element => {
            const key = element.getAttribute('data-i18n');
            if (translations[lang] && translations[lang][key]) {
                if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') {
                    if (element.hasAttribute('placeholder')) {
                        element.setAttribute('placeholder', translations[lang][key]);
                    }
                } else {
                    element.innerHTML = translations[lang][key];
                }
            }
        });
        
        // Update language switcher active states if applicable
        document.querySelectorAll('.lang-switch-btn').forEach(btn => {
            if (btn.getAttribute('data-lang') === lang) {
                btn.classList.add('font-bold', 'text-brand-primary');
                btn.classList.remove('text-slate-500');
            } else {
                btn.classList.remove('font-bold', 'text-brand-primary');
                btn.classList.add('text-slate-500');
            }
        });
    }

    // Language switcher setup
    document.querySelectorAll('.lang-switch-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const lang = e.target.getAttribute('data-lang');
            if (lang !== currentLang) {
                currentLang = lang;
                localStorage.setItem('site_lang', currentLang);
                applyTranslations(currentLang);
            }
        });
    });

    // Initial translation application
    applyTranslations(currentLang);
});
