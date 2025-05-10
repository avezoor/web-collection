document.addEventListener('DOMContentLoaded', function() {
    // Theme toggle functionality
    const themeToggle = document.getElementById('themeToggle');
    const body = document.body;
    
    // Check local storage for saved theme preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'light') {
        body.classList.add('light-theme');
    }
    
    // Theme toggle click handler
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            // Toggle light theme class
            body.classList.toggle('light-theme');
            
            // Save preference to localStorage
            if (body.classList.contains('light-theme')) {
                localStorage.setItem('theme', 'light');
            } else {
                localStorage.setItem('theme', 'dark');
            }
            
            // Reapply syntax highlighting with new theme
            if (typeof Prism !== 'undefined') {
                Prism.highlightAll();
            }
        });
    }
    
    // Add syntax highlighting to code blocks when page loads
    if (typeof Prism !== 'undefined') {
        Prism.highlightAll();
    }
    
    // Make cards with links clickable
    const codeItems = document.querySelectorAll('.code-item');
    codeItems.forEach(item => {
        const link = item.querySelector('a[href]');
        if (link) {
            const linkHref = link.getAttribute('href');
            item.addEventListener('click', function(e) {
                // Don't navigate if clicking on a tag or button
                if (!e.target.closest('.badge') && !e.target.closest('.btn')) {
                    window.location.href = linkHref;
                }
            });
            
            // Add pointer cursor to indicate clickable
            item.style.cursor = 'pointer';
        }
    });
    
    // Tag search functionality
    const tagSearchInput = document.getElementById('tagSearch');
    const clearTagSearchBtn = document.getElementById('clearTagSearch');
    const tagLinks = document.querySelectorAll('.toc-tags .tag-link');
    
    if (tagSearchInput && clearTagSearchBtn) {
        // Search as you type
        tagSearchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase().trim();
            filterTags(searchTerm);
        });
        
        // Clear search button
        clearTagSearchBtn.addEventListener('click', function() {
            tagSearchInput.value = '';
            filterTags('');
            tagSearchInput.focus();
        });
        
        // Function to filter tags
        function filterTags(searchTerm) {
            let hasVisibleTags = false;
            
            tagLinks.forEach(link => {
                const tagText = link.textContent.toLowerCase().trim();
                if (tagText.includes(searchTerm)) {
                    link.style.display = '';
                    hasVisibleTags = true;
                } else {
                    link.style.display = 'none';
                }
            });
            
            // Show a message if no tags match
            const noTagsMessage = document.getElementById('noTagsMessage');
            if (!hasVisibleTags && searchTerm) {
                if (!noTagsMessage) {
                    const message = document.createElement('div');
                    message.id = 'noTagsMessage';
                    message.className = 'alert alert-info mt-2 small';
                    message.textContent = 'No tags found matching: "' + searchTerm + '"';
                    document.querySelector('.toc-tags').appendChild(message);
                }
            } else if (noTagsMessage) {
                noTagsMessage.remove();
            }
        }
    }
    
    // Automatically detect language in code blocks
    document.querySelectorAll('pre code').forEach((block) => {
        if (!block.classList.contains('language-')) {
            // Try to detect language from the content
            const content = block.textContent.trim();
            
            if (content.includes('function') || content.includes('var ') || content.includes('const ') || content.includes('let ')) {
                block.classList.add('language-javascript');
            } else if (content.includes('def ') || content.includes('import ') || content.includes('class ') && content.includes(':')) {
                block.classList.add('language-python');
            } else if (content.includes('<html') || content.includes('<!DOCTYPE') || (content.includes('<') && content.includes('>'))) {
                block.classList.add('language-html');
            } else if (content.includes('{') && content.includes('}') && content.includes(':')) {
                block.classList.add('language-css');
            } else {
                block.classList.add('language-plaintext');
            }
        }
    });
});
