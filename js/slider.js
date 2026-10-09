window.initSlider = function() {
    const containers = document.querySelectorAll('.review-slider-container');

    containers.forEach(container => {
        let isDragging = false;
        let startX;
        let scrollLeft;
        
        let autoScrollInterval;
        let isHovered = false;

        const checkAndResetScroll = () => {
            // gap-8 is 32px
            const shiftD = (container.scrollWidth + 32) / 3;
            
            // If scrolled into Set 3, snap back to Set 2
            if (container.scrollLeft >= 2 * shiftD) {
                container.scrollLeft -= shiftD;
                if (isDragging) scrollLeft -= shiftD; // adjust drag anchor
            } 
            // If scrolled into Set 1, snap forward to Set 2
            else if (container.scrollLeft <= 0) {
                container.scrollLeft += shiftD;
                if (isDragging) scrollLeft += shiftD;
            }
        };

        const startAutoScroll = () => {
            stopAutoScroll();
            autoScrollInterval = setInterval(() => {
                // Pause auto-scroll if any card is currently expanded
                const isExpanded = Array.from(container.querySelectorAll('.review-card')).some(card => card.style.maxHeight === '3000px');

                if (!isDragging && !isHovered && !isExpanded) {
                    container.scrollLeft += 1;
                    checkAndResetScroll();
                }
            }, 20); // ~50fps
        };

        const stopAutoScroll = () => {
            if (autoScrollInterval) {
                clearInterval(autoScrollInterval);
            }
        };

        const dragStart = (e) => {
            isDragging = true;
            container.classList.add('cursor-grabbing');
            container.classList.remove('cursor-grab');
            startX = e.pageX - container.offsetLeft;
            scrollLeft = container.scrollLeft;
        };

        const dragMove = (e) => {
            if (!isDragging) return;
            e.preventDefault(); // Prevent text selection
            const x = e.pageX - container.offsetLeft;
            const walk = (x - startX) * 1.5; // Drag sensitivity
            container.scrollLeft = scrollLeft - walk;
            checkAndResetScroll();
        };

        const dragEnd = () => {
            if (!isDragging) return;
            isDragging = false;
            container.classList.remove('cursor-grabbing');
            container.classList.add('cursor-grab');
        };

        // Hover events for auto-scroll pause
        container.addEventListener('mouseenter', () => {
            isHovered = true;
        });

        container.addEventListener('mouseleave', () => {
            isHovered = false;
            dragEnd(); // Also end drag if mouse leaves container
        });

        // Mouse events
        container.addEventListener('mousedown', dragStart);
        container.addEventListener('mousemove', dragMove);
        container.addEventListener('mouseup', dragEnd);
        
        // Touch events for mobile compatibility
        container.addEventListener('touchstart', (e) => {
            isHovered = true;
            dragStart(e.touches[0]);
        }, { passive: true });
        
        container.addEventListener('touchmove', (e) => {
            dragMove(e.touches[0]);
        }, { passive: false });
        
        container.addEventListener('touchend', () => {
            isHovered = false;
            dragEnd();
        });

        // Initial setup
        container.classList.add('cursor-grab');
        
        // Wait for layout to settle, then shift to the middle set (Set 2) to allow bidirectional scrolling immediately
        requestAnimationFrame(() => {
            requestAnimationFrame(() => {
                const shiftD = (container.scrollWidth + 32) / 3;
                container.scrollLeft = shiftD;
                startAutoScroll();
            });
        });
    });
};
