const API_BASE_URL = 'https://script.google.com/macros/s/AKfycbzz5GryK4hU4JVbqfgFYA19VHqvjGvihxTNI22IuB7BBwhLUeDSB4HvoJKIq0R0Ydj5/exec';

document.addEventListener('DOMContentLoaded', () => {
    fetchReviews();
    setupReviewModal();
});

// Helper functions for dynamic UI
const colors = ['bg-brand-primary', 'bg-emerald-500', 'bg-amber-500', 'bg-rose-500', 'bg-indigo-500', 'bg-purple-500'];

function getInitials(name) {
    if (!name) return 'A';
    const parts = name.trim().split(' ');
    if (parts.length === 1) return parts[0].charAt(0).toUpperCase();
    return (parts[0].charAt(0) + parts[parts.length - 1].charAt(0)).toUpperCase();
}

function getColor(name) {
    if (!name) return colors[0];
    let hash = 0;
    for (let i = 0; i < name.length; i++) {
        hash = name.charCodeAt(i) + ((hash << 5) - hash);
    }
    const index = Math.abs(hash) % colors.length;
    return colors[index];
}

async function fetchReviews() {
    try {
        // If it's the placeholder, load some mocks to avoid breaking the UI
        if (API_BASE_URL.includes('PLACEHOLDER_SCRIPT_ID')) {
            console.log("Using mock reviews (API_BASE_URL not configured).");
            renderReviews(getMockReviews());
            return;
        }

        const response = await fetch(API_BASE_URL);
        if (!response.ok) throw new Error('Failed to fetch reviews');
        
        const reviews = await response.json();
        
        if (!reviews || reviews.length === 0) {
            renderReviews(getMockReviews());
        } else {
            renderReviews(reviews);
        }
    } catch (error) {
        console.error('Error loading reviews:', error);
        renderReviews(getMockReviews()); // Fallback on error
    }
}

function getMockReviews() {
    return [
        { name: "Sarah & Mike", country: "United Kingdom", text: "Traveling with Andy was the highlight of our trip. His knowledge of the local history and secret spots made our adventure truly exceptional." },
        { name: "James Doe", country: "Australia", text: "We saw 3 leopards in Yala thanks to Andy's eagle eyes! He arranged everything perfectly and we just had to sit back and enjoy." },
        { name: "Anna Lindström", country: "Sweden", text: "The train ride to Ella was magical. Andy took care of our tickets months in advance. Best guide we've ever had on any of our travels!" },
        { name: "Paul Thompson", country: "Canada", text: "Our family of 5 had an incredible time. Andy was so patient with the kids and customized everything to our pace. Highly recommended." },
        { name: "Tour Group CHN251", country: "China", text: "Excellent service! The guide was highly praised for being extremely patient and attentive. We were very satisfied with the meals. The vehicle was comfortable, clean, and tidy, and the flower welcome ceremony was a beautiful touch." }
    ];
}

let currentlyExpandedCard = null;

function renderReviews(reviews) {
    currentlyExpandedCard = null;
    const containers = document.querySelectorAll('.review-slider-track');
    
    containers.forEach(track => {
        track.innerHTML = ''; // Clear existing
        
        // Create a base set of reviews that is large enough
        let baseReviews = [...reviews];
        while (baseReviews.length < 5) {
            baseReviews = [...baseReviews, ...reviews];
        }
        
        // Render 3 identical sets for a seamless bidirectional infinite loop
        const allReviews = [...baseReviews, ...baseReviews, ...baseReviews];
        
        allReviews.forEach((review, index) => {
            const initials = getInitials(review.name);
            const color = getColor(review.name);

            const card = document.createElement('div');
            card.dataset.index = index;
            card.className = 'review-card flex flex-col bg-white shadow-lg p-8 rounded-2xl border border-slate-100 min-w-[320px] max-w-[400px] shrink-0 min-h-[550px] transition-all duration-700 ease-in-out relative overflow-hidden';
            card.style.maxHeight = '550px';
            
            card.innerHTML = `
                <div class="flex-grow flex flex-col justify-start relative">
                    <p class="review-text-content text-slate-600 italic transition-all duration-500" style="display: -webkit-box; -webkit-line-clamp: 15; -webkit-box-orient: vertical; overflow: hidden;">"${review.text}"</p>
                    <button class="read-more-btn text-brand-primary text-sm font-semibold mt-4 text-left hidden focus:outline-none transition-colors hover:text-brand-accent w-max">Read More</button>
                </div>
                <div class="flex items-center space-x-4 mt-8 mt-auto">
                    <div class="w-12 h-12 ${color} text-white rounded-full flex items-center justify-center font-bold flex-shrink-0">${initials}</div>
                    <div>
                        <h5 class="font-bold text-brand-dark">${review.name}</h5>
                        <p class="text-slate-500 text-sm">${review.country}</p>
                    </div>
                </div>
            `;
            track.appendChild(card);

            // Need to check overflow after layout is calculated
            requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                    const textContent = card.querySelector('.review-text-content');
                    const readMoreBtn = card.querySelector('.read-more-btn');
                    
                    if (textContent.scrollHeight > textContent.clientHeight) {
                        readMoreBtn.classList.remove('hidden');
                    }

                    readMoreBtn.addEventListener('click', () => {
                        const isExpanded = card.style.maxHeight === '3000px';

                        if (!isExpanded) {
                            // Collapse previously expanded card
                            if (currentlyExpandedCard && currentlyExpandedCard !== card) {
                                const prevBtn = currentlyExpandedCard.querySelector('.read-more-btn');
                                const prevContent = currentlyExpandedCard.querySelector('.review-text-content');
                                
                                currentlyExpandedCard.style.maxHeight = '550px';
                                prevContent.style.webkitLineClamp = '15';
                                prevBtn.textContent = 'Read More';
                            }

                            // Expand this card
                            card.style.maxHeight = '3000px';
                            textContent.style.webkitLineClamp = 'unset';
                            readMoreBtn.textContent = 'Show Less';
                            currentlyExpandedCard = card;
                        } else {
                            // Collapse this card
                            card.style.maxHeight = '550px';
                            textContent.style.webkitLineClamp = '15';
                            readMoreBtn.textContent = 'Read More';
                            if (currentlyExpandedCard === card) {
                                currentlyExpandedCard = null;
                            }
                        }
                    });
                });
            });
        });
    });

    // Re-initialize slider logic now that cards exist
    if (window.initSlider) {
        window.initSlider();
    }
}

function setupReviewModal() {
    const modal = document.getElementById('review-modal');
    const openBtns = document.querySelectorAll('.open-review-modal');
    const closeBtn = document.getElementById('close-review-modal');
    const form = document.getElementById('review-form');
    const submitBtn = document.getElementById('submit-review-btn');

    if (!modal || !form) return;

    openBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            modal.classList.remove('hidden');
        });
    });

    closeBtn.addEventListener('click', () => {
        modal.classList.add('hidden');
    });

    // Close on click outside
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.add('hidden');
        }
    });

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        submitBtn.disabled = true;
        submitBtn.textContent = 'Submitting...';

        const formData = new FormData(form);
        const data = {
            name: formData.get('name'),
            country: formData.get('country'),
            text: formData.get('text')
        };

        try {
            if (API_BASE_URL.includes('PLACEHOLDER_SCRIPT_ID')) {
                alert('Success! (Mock mode - script URL not configured)');
                form.reset();
                modal.classList.add('hidden');
                submitBtn.disabled = false;
                submitBtn.textContent = 'Submit Review';
                return;
            }

            // Using text/plain prevents CORS preflight OPTIONS request
            const response = await fetch(API_BASE_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'text/plain;charset=utf-8' },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                form.reset();
                modal.classList.add('hidden');
                alert('Thank you for your review!');
                fetchReviews(); // Instantly update the reviews on the website
            } else {
                alert('Failed to submit review. Please try again.');
            }
        } catch (error) {
            console.error('Error submitting review:', error);
            alert('A network error occurred. Please try again.');
        } finally {
            submitBtn.disabled = false;
            submitBtn.textContent = 'Submit Review';
        }
    });
}
