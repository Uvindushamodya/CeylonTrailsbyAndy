// WeChat Modal Logic
const wechatBtn = document.getElementById('open-wechat-modal');
const wechatModal = document.getElementById('wechat-modal');
const closeWechatBtn = document.getElementById('close-wechat-modal');

if(wechatBtn && wechatModal) {
    wechatBtn.addEventListener('click', (e) => {
        e.preventDefault();
        wechatModal.classList.remove('hidden');
    });
    
    closeWechatBtn.addEventListener('click', () => {
        wechatModal.classList.add('hidden');
    });

    wechatModal.addEventListener('click', (e) => {
        if (e.target === wechatModal) {
            wechatModal.classList.add('hidden');
        }
    });
}

// LINE Modal Logic
const lineBtn = document.getElementById('open-line-modal');
const lineModal = document.getElementById('line-modal');
const closeLineBtn = document.getElementById('close-line-modal');

if(lineBtn && lineModal) {
    lineBtn.addEventListener('click', (e) => {
        e.preventDefault();
        lineModal.classList.remove('hidden');
    });
    
    closeLineBtn.addEventListener('click', () => {
        lineModal.classList.add('hidden');
    });

    lineModal.addEventListener('click', (e) => {
        if (e.target === lineModal) {
            lineModal.classList.add('hidden');
        }
    });
}
