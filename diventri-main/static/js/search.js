// Initialize search functionality for people page
function initSearch() {
    const searchInput = document.getElementById('searchInput');
    const peopleCards = document.querySelectorAll('.people-card');
    
    searchInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase().trim();
        
        // If search term is empty, show all cards
        if (searchTerm === '') {
            peopleCards.forEach(card => {
                card.style.display = 'block';
            });
            return;
        }
        
        // Filter cards based on search term
        peopleCards.forEach(card => {
            const name = card.querySelector('.card-title').textContent.toLowerCase();
            const origin = card.querySelector('[data-origin]').getAttribute('data-origin').toLowerCase();
            
            // Show card if name or origin contains search term
            if (name.includes(searchTerm) || origin.includes(searchTerm)) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
        
        // Show message if no results
        const visibleCards = document.querySelectorAll('.people-card[style="display: block"]');
        const noResultsMessage = document.getElementById('noResults');
        
        if (visibleCards.length === 0) {
            if (!noResultsMessage) {
                const message = document.createElement('div');
                message.id = 'noResults';
                message.className = 'col-12 text-center mt-4';
                message.innerHTML = '<h3>No results found</h3><p>Try a different search term</p>';
                document.querySelector('.people-container').appendChild(message);
            }
        } else {
            if (noResultsMessage) {
                noResultsMessage.remove();
            }
        }
    });
}
