document.addEventListener('DOMContentLoaded', () => {
    const totalImages = 15;
    const galleryContainer = document.querySelector('.grid.grid-cols-2.md\\:grid-cols-3');
    
    if (!galleryContainer) return;

    const slotDivs = galleryContainer.querySelectorAll('.overflow-hidden.rounded-2xl.group');
    const imagePaths = [];
    
    for (let i = 1; i <= totalImages; i++) {
        imagePaths.push(`images/gallery/${i}.jpeg`);
    }

    // Function to get a random item from array
    const getRandomImage = (excludeImages) => {
        let candidate;
        do {
            candidate = imagePaths[Math.floor(Math.random() * imagePaths.length)];
        } while (excludeImages.includes(candidate));
        return candidate;
    };

    let currentDisplayedImages = [];
    let tempPaths = [...imagePaths];
    for (let i = tempPaths.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [tempPaths[i], tempPaths[j]] = [tempPaths[j], tempPaths[i]];
    }

    // Initialize slots with 2 image tags for crossfading
    const slots = [];
    slotDivs.forEach((div, index) => {
        const imgPath = tempPaths[index];
        currentDisplayedImages.push(imgPath);

        div.classList.add('relative', 'aspect-square');
        div.innerHTML = ''; // Clear existing img

        const img1 = document.createElement('img');
        img1.src = imgPath;
        img1.className = 'absolute inset-0 w-full h-full object-cover transform group-hover:scale-110 z-10';
        img1.style.transition = 'opacity 1s ease-in-out, filter 1s ease-in-out, transform 0.7s ease-in-out';
        img1.style.opacity = '1';
        img1.style.filter = 'blur(0px)';
        
        const img2 = document.createElement('img');
        img2.className = 'absolute inset-0 w-full h-full object-cover transform group-hover:scale-110 z-0';
        img2.style.transition = 'opacity 1s ease-in-out, filter 1s ease-in-out, transform 0.7s ease-in-out';
        img2.style.opacity = '0';
        img2.style.filter = 'blur(8px)'; // Start blurred

        div.appendChild(img2);
        div.appendChild(img1);

        slots.push({
            div,
            activeImg: img1,
            nextImg: img2
        });
    });

    // Interval to swap one random image every few seconds
    setInterval(() => {
        const slotIndex = Math.floor(Math.random() * slots.length);
        const slot = slots[slotIndex];
        
        const newImage = getRandomImage(currentDisplayedImages);
        currentDisplayedImages[slotIndex] = newImage;
        
        const outgoingImg = slot.activeImg;
        const incomingImg = slot.nextImg;

        // Prepare incoming image
        incomingImg.src = newImage;
        
        incomingImg.onload = () => {
            // Apply crossfade and blur
            outgoingImg.style.opacity = '0';
            outgoingImg.style.filter = 'blur(8px)';
            outgoingImg.style.zIndex = '0';
            
            incomingImg.style.opacity = '1';
            incomingImg.style.filter = 'blur(0px)';
            incomingImg.style.zIndex = '10';
            
            // Swap roles
            slot.activeImg = incomingImg;
            slot.nextImg = outgoingImg;
        };
    }, 3000);
});
