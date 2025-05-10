// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize animations
    initAnimations();
    
    // Initialize navigation active state
    setActiveNavItem();

    // Initialize lightbox if on gallery or hall of fame page
    if (document.querySelector('.gallery-item') || document.querySelector('.hof-item')) {
        initLightbox();
    }

    // Initialize search functionality if on people page
    if (document.querySelector('#searchInput')) {
        initSearch();
    }
});

// Function to initialize animations
function initAnimations() {
    const elementsToAnimate = document.querySelectorAll('.card, .section-title, .profile-card, .org-card');
    
    // Create an Intersection Observer
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    
    // Observe each element
    elementsToAnimate.forEach(element => {
        observer.observe(element);
    });
}

// Function to set active navigation item based on current page
function setActiveNavItem() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        if (currentPath === linkPath || 
            (linkPath !== '/' && currentPath.includes(linkPath))) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

// Function to handle back to top button
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Function to toggle mobile navigation
function toggleMobileNav() {
    const navbarCollapse = document.querySelector('.navbar-collapse');
    if (navbarCollapse.classList.contains('show')) {
        navbarCollapse.classList.remove('show');
    } else {
        navbarCollapse.classList.add('show');
    }
}
