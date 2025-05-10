// Initialize lightbox functionality
function initLightbox() {
    // Create lightbox elements
    const lightbox = document.createElement('div');
    lightbox.className = 'lightbox';
    
    const lightboxImgContainer = document.createElement('div');
    lightboxImgContainer.className = 'lightbox-img-container';
    
    const lightboxImg = document.createElement('img');
    lightboxImg.className = 'lightbox-img';
    
    const lightboxInfo = document.createElement('div');
    lightboxInfo.className = 'lightbox-info';
    
    const lightboxClose = document.createElement('button');
    lightboxClose.className = 'lightbox-close';
    lightboxClose.innerHTML = '&times;';
    
    // Create zoom controls
    const zoomControls = document.createElement('div');
    zoomControls.className = 'zoom-controls';
    
    const zoomIn = document.createElement('button');
    zoomIn.className = 'zoom-btn zoom-in';
    zoomIn.innerHTML = '<i class="fas fa-search-plus"></i>';
    
    const zoomOut = document.createElement('button');
    zoomOut.className = 'zoom-btn zoom-out';
    zoomOut.innerHTML = '<i class="fas fa-search-minus"></i>';
    
    const zoomReset = document.createElement('button');
    zoomReset.className = 'zoom-btn zoom-reset';
    zoomReset.innerHTML = '<i class="fas fa-undo"></i>';
    
    zoomControls.appendChild(zoomIn);
    zoomControls.appendChild(zoomOut);
    zoomControls.appendChild(zoomReset);
    
    // Append all elements
    lightboxImgContainer.appendChild(lightboxImg);
    lightbox.appendChild(lightboxImgContainer);
    lightbox.appendChild(lightboxInfo);
    lightbox.appendChild(lightboxClose);
    lightbox.appendChild(zoomControls);
    document.body.appendChild(lightbox);
    
    // Keep track of zoom level
    let currentZoom = 1;
    const zoomStep = 0.2;
    const maxZoom = 3;
    const minZoom = 0.5;
    
    // Zoom functions
    function updateZoom() {
        lightboxImg.style.transform = `scale(${currentZoom})`;
    }
    
    function zoomInFunc() {
        if (currentZoom < maxZoom) {
            currentZoom += zoomStep;
            updateZoom();
        }
    }
    
    function zoomOutFunc() {
        if (currentZoom > minZoom) {
            currentZoom -= zoomStep;
            updateZoom();
        }
    }
    
    function resetZoom() {
        currentZoom = 1;
        updateZoom();
        // Reset position
        lightboxImg.style.marginLeft = '0';
        lightboxImg.style.marginTop = '0';
    }
    
    // Zoom controls event listeners
    zoomIn.addEventListener('click', zoomInFunc);
    zoomOut.addEventListener('click', zoomOutFunc);
    zoomReset.addEventListener('click', resetZoom);
    
    // Add wheel event for zoom
    lightboxImgContainer.addEventListener('wheel', function(e) {
        e.preventDefault();
        if (e.deltaY < 0) {
            zoomInFunc();
        } else {
            zoomOutFunc();
        }
    });
    
    // Add drag functionality for zoomed image
    let isDragging = false;
    let dragStartX, dragStartY;
    let prevMarginLeft = 0;
    let prevMarginTop = 0;
    
    lightboxImg.addEventListener('mousedown', function(e) {
        if (currentZoom > 1) {
            isDragging = true;
            dragStartX = e.clientX;
            dragStartY = e.clientY;
            prevMarginLeft = parseInt(lightboxImg.style.marginLeft || 0);
            prevMarginTop = parseInt(lightboxImg.style.marginTop || 0);
            lightboxImg.style.cursor = 'grabbing';
        }
    });
    
    document.addEventListener('mousemove', function(e) {
        if (isDragging) {
            const dx = e.clientX - dragStartX;
            const dy = e.clientY - dragStartY;
            
            // Apply margin to move the image
            lightboxImg.style.marginLeft = prevMarginLeft + dx + 'px';
            lightboxImg.style.marginTop = prevMarginTop + dy + 'px';
        }
    });
    
    document.addEventListener('mouseup', function() {
        isDragging = false;
        lightboxImg.style.cursor = 'grab';
    });
    
    // Add click event to gallery/hall of fame items
    const items = document.querySelectorAll('.gallery-item, .hof-item');
    items.forEach(item => {
        item.addEventListener('click', function() {
            const imgSrc = this.querySelector('img').getAttribute('src');
            const title = this.querySelector('.card-title').textContent;
            const description = this.querySelector('.card-text').textContent;
            const date = this.querySelector('.card-footer').textContent;
            
            // Reset zoom and position
            resetZoom();
            
            // Set lightbox content
            lightboxImg.setAttribute('src', imgSrc);
            lightboxInfo.innerHTML = `
                <h3>${title}</h3>
                <p>${description}</p>
                <small>${date}</small>
            `;
            
            // Show lightbox
            lightbox.classList.add('active');
            
            // Prevent body scrolling
            document.body.style.overflow = 'hidden';
        });
    });
    
    // Close lightbox on button click
    lightboxClose.addEventListener('click', closeLightbox);
    
    // Close lightbox when clicking outside the image
    lightbox.addEventListener('click', function(e) {
        if (e.target === lightbox) {
            closeLightbox();
        }
    });
    
    // Close lightbox with Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && lightbox.classList.contains('active')) {
            closeLightbox();
        }
    });
    
    function closeLightbox() {
        lightbox.classList.remove('active');
        document.body.style.overflow = 'auto';
        // Reset zoom and position when closing
        resetZoom();
    }
    
    // Initialize the lightbox when DOM is ready
    if (document.readyState === 'complete' || document.readyState === 'interactive') {
        // Already ready
    } else {
        document.addEventListener('DOMContentLoaded', function() {
            // DOM ready
        });
    }
}
