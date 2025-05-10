document.addEventListener('DOMContentLoaded', function() {
    const content = document.querySelector('.post-content');
    const toc = document.querySelector('.toc-list');
    
    if (!content || !toc) return;

    const headings = content.querySelectorAll('h1, h2, h3');
    const tocItems = [];

    headings.forEach((heading, index) => {
        if (!heading.id) {
            heading.id = `heading-${index}`;
        }

        const li = document.createElement('li');
        const a = document.createElement('a');
        a.href = `#${heading.id}`;
        a.textContent = heading.textContent;
        a.style.paddingLeft = `${(heading.tagName[1] - 1) * 15}px`;
        
        li.appendChild(a);
        toc.appendChild(li);

        a.addEventListener('click', (e) => {
            e.preventDefault();
            heading.scrollIntoView({ behavior: 'smooth' });
        });
    });
});
