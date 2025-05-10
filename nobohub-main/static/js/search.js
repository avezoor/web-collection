document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const searchResults = document.getElementById('searchResults');
    
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const query = this.value.toLowerCase();
            const posts = document.querySelectorAll('.card-title');
            const results = [];

            posts.forEach(post => {
                const title = post.textContent.trim().toLowerCase();
                if (title.includes(query)) {
                    const link = post.querySelector('a');
                    if (link) {
                        results.push({
                            title: post.textContent.trim(),
                            url: link.href
                        });
                    }
                }
            });

            displayResults(results);
        });
    }

    function displayResults(results) {
        searchResults.innerHTML = '';
        if (results.length === 0) {
            searchResults.innerHTML = '<p class="text-muted">No results found</p>';
            return;
        }

        const list = document.createElement('ul');
        list.className = 'displayresult-list';
        
        results.forEach(result => {
            const item = document.createElement('li');
            item.className = 'displayresult-item';
            
            const link = document.createElement('a');
            link.href = result.url;
            link.textContent = result.title;
            link.className = 'displayresult-link'; 
            
            item.appendChild(link);
            list.appendChild(item);
        });
        searchResults.appendChild(list);
    }
});
