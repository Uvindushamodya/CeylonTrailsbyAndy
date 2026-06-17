window.initSlider = function() {
    const containers = document.querySelectorAll('.review-slider-container');

    containers.forEach(container => {
        const track = container.querySelector('.review-slider-track');
        if (!track) return;
        
        const cards = track.querySelectorAll('.review-card');
        if (cards.length === 0) return;

        // We assume exactly half the cards are the original set, and half are duplicates
        const halfCount = Math.floor(cards.length / 2);
        let loopPoint = 0;
        let isDragging = false;
        let animationId;
        let idleTimeoutId;
        let speed = 0.5; // pixels per frame

        function calculateLoopPoint() {
            if (cards.length > halfCount) {
                // The exact width of one complete set including gaps
                loopPoint = cards[halfCount].offsetLeft - cards[0].offsetLeft;
            }
        }
        
        window.addEventListener('resize', calculateLoopPoint);
        
        // Wait a tiny bit for CSS flex layout to settle before calculating
        setTimeout(() => {
            calculateLoopPoint();
            startAutoScroll();
        }, 100);

        function autoScroll() {
            if (!isDragging && loopPoint > 0) {
                container.scrollLeft += speed;
                
                // Infinite loop forward
                if (container.scrollLeft >= loopPoint) {
                    container.scrollLeft -= loopPoint;
                }
            }
            animationId = requestAnimationFrame(autoScroll);
        }

        function startAutoScroll() {
            if (!animationId) {
                animationId = requestAnimationFrame(autoScroll);
            }
        }

        function stopAutoScroll() {
            if (animationId) {
                cancelAnimationFrame(animationId);
                animationId = null;
            }
        }

        function resetIdleTimer() {
            clearTimeout(idleTimeoutId);
            idleTimeoutId = setTimeout(() => {
                if (!isDragging) {
                    startAutoScroll();
                }
            }, 2500); // Resume auto-scroll after 2.5 seconds of idle
        }

        // --- Mouse Drag Events ---
        let startX;
        let scrollLeft;

        const dragStart = (e) => {
            isDragging = true;
            stopAutoScroll();
            clearTimeout(idleTimeoutId);
            container.classList.add('cursor-grabbing');
            container.classList.remove('cursor-grab');
            startX = e.pageX - container.offsetLeft;
            scrollLeft = container.scrollLeft;
        };

        const dragMove = (e) => {
            if (!isDragging) return;
            e.preventDefault(); // Prevent text selection while dragging
            
            const x = e.pageX - container.offsetLeft;
            const walk = (x - startX) * 1.5; // Drag sensitivity
            let newScrollLeft = scrollLeft - walk;
            
            // Loop instantly while dragging if we cross boundaries
            if (newScrollLeft >= loopPoint) {
                newScrollLeft -= loopPoint;
                startX = x;
                scrollLeft = newScrollLeft;
            } else if (newScrollLeft <= 0) {
                newScrollLeft += loopPoint;
                startX = x;
                scrollLeft = newScrollLeft;
            }
            
            container.scrollLeft = newScrollLeft;
        };

        const dragEnd = () => {
            if (!isDragging) return;
            isDragging = false;
            container.classList.remove('cursor-grabbing');
            container.classList.add('cursor-grab');
            resetIdleTimer();
        };

        container.addEventListener('mousedown', dragStart);
        container.addEventListener('mousemove', dragMove);
        container.addEventListener('mouseup', dragEnd);
        
        // --- Leave Event for Dragging ---
        container.addEventListener('mouseleave', () => {
            if (isDragging) {
                dragEnd();
            }
        });

        // For mobile/touch, we let the native overflow-x scroll handle the movement,
        // but we still want to pause auto-scroll and handle looping.
        container.addEventListener('touchstart', () => {
            stopAutoScroll();
            clearTimeout(idleTimeoutId);
        }, {passive: true});

        container.addEventListener('touchend', () => {
            resetIdleTimer();
        });
        
        container.addEventListener('scroll', () => {
            // Check for loop boundaries during native scrolling (e.g. mobile swipe)
            if (loopPoint > 0 && !isDragging) {
                if (container.scrollLeft >= loopPoint) {
                    container.scrollLeft -= loopPoint;
                } else if (container.scrollLeft <= 0) {
                    // Prevent hitting absolute zero when swiping left
                    container.scrollLeft += loopPoint;
                }
            }
        });
    });
};
