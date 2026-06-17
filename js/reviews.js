const API_BASE_URL = (window.location.hostname === '127.0.0.1' || window.location.hostname === 'localhost') && window.location.port !== '5000'
    ? 'http://127.0.0.1:5000'
    : '';

document.addEventListener('DOMContentLoaded', () => {
    fetchReviews();
    setupReviewModal();
});

async function fetchReviews() {
    try {
        const response = await fetch(`${API_BASE_URL}/api/reviews`);
        if (!response.ok) throw new Error('Failed to fetch reviews');
        
        let reviews = await response.json();
        
        // If API returns nothing, maybe we should show mock reviews or just nothing
        if (!reviews || reviews.length === 0) {
            reviews = [
                {
                    name: "Sarah & Mike", country: "United Kingdom",
                    text: "Traveling with Andy was the highlight of our trip. His knowledge of the local history and secret spots made our adventure truly exceptional.",
                    initials: "SM", color: "bg-brand-primary"
                },
                {
                    name: "James Doe", country: "Australia",
                    text: "We saw 3 leopards in Yala thanks to Andy's eagle eyes! He arranged everything perfectly and we just had to sit back and enjoy.",
                    initials: "JD", color: "bg-emerald-500"
                },
                {
                    name: "Anna Lindström", country: "Sweden",
                    text: "The train ride to Ella was magical. Andy took care of our tickets months in advance. Best guide we've ever had on any of our travels!",
                    initials: "AL", color: "bg-amber-500"
                },
                {
                    name: "Paul Thompson", country: "Canada",
                    text: "Our family of 5 had an incredible time. Andy was so patient with the kids and customized everything to our pace. Highly recommended.",
                    initials: "PT", color: "bg-rose-500"
                }
            ];
        }

        renderReviews(reviews);
    } catch (error) {
        console.error('Error loading reviews:', error);
        // On error, we could render fallback mock reviews here too
    }
}

function renderReviews(reviews) {
    const containers = document.querySelectorAll('.review-slider-track');
    
    containers.forEach(track => {
        track.innerHTML = ''; // Clear existing
        
        // We need to render the original set, and then duplicate it for the infinite slider
        const allReviews = [...reviews, ...reviews];
        
        allReviews.forEach(review => {
            const card = document.createElement('div');
            card.className = 'review-card flex flex-col bg-white shadow-lg p-8 rounded-2xl border border-slate-100 min-w-[320px] max-w-[400px] shrink-0';
            
            card.innerHTML = `
                <p class="text-slate-600 italic mb-8 flex-grow">"${review.text}"</p>
                <div class="flex items-center space-x-4 mt-auto">
                    <div class="w-12 h-12 ${review.color || 'bg-brand-primary'} text-white rounded-full flex items-center justify-center font-bold flex-shrink-0">${review.initials || 'A'}</div>
                    <div>
                        <h5 class="font-bold text-brand-dark">${review.name}</h5>
                        <p class="text-slate-500 text-sm">${review.country}</p>
                    </div>
                </div>
            `;
            track.appendChild(card);
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
            const response = await fetch(`${API_BASE_URL}/api/reviews`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                form.reset();
                modal.classList.add('hidden');
                // Refresh reviews
                await fetchReviews();
                alert('Thank you for your review!');
            } else {
                const resData = await response.json();
                alert(resData.error || 'Failed to submit review. Please try again.');
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
