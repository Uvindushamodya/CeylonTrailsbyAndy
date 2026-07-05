window.initSlider = function() {
    const containers = document.querySelectorAll('.review-slider-container');

    containers.forEach(container => {
        let isDragging = false;
        let startX;
        let scrollLeft;

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
        };

        const dragEnd = () => {
            if (!isDragging) return;
            isDragging = false;
            container.classList.remove('cursor-grabbing');
            container.classList.add('cursor-grab');
        };

        container.addEventListener('mousedown', dragStart);
        container.addEventListener('mousemove', dragMove);
        container.addEventListener('mouseup', dragEnd);
        container.addEventListener('mouseleave', dragEnd);
    });
};
