// Initialize Lucide Icons
lucide.createIcons();

// Scroll Header Effect
window.addEventListener('scroll', () => {
    const header = document.querySelector('header');
    if (window.scrollY > 50) {
        header.style.boxShadow = '0 5px 20px rgba(0,0,0,0.2)';
    } else {
        header.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
    }
});

// Smooth Scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            window.scrollTo({
                top: target.offsetTop - 80,
                behavior: 'smooth'
            });
        }
    });
});

document.addEventListener('DOMContentLoaded', () => {
    initSectorFilter();
    initExcellenceSlider();
    initMobileMenu();
    initProductFilter();
    initPDFReader();
    initSpecTileTilt();
});

// Reveal animations on scroll
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

document.querySelectorAll('.product-card, .feature-item, .industry-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'all 0.6s ease-out';
    observer.observe(el);
});



// Hero Slider
const slides = document.querySelectorAll('.hero-slide');
const dots = document.querySelectorAll('.dot');
let currentSlide = 0;
let slideInterval;

function showSlide(index) {
    slides[currentSlide].classList.remove('active');
    dots[currentSlide].classList.remove('active');
    currentSlide = (index + slides.length) % slides.length;
    slides[currentSlide].classList.add('active');
    dots[currentSlide].classList.add('active');
}

function nextSlide() {
    showSlide(currentSlide + 1);
}

function startSlideTimer() {
    clearInterval(slideInterval);
    slideInterval = setInterval(nextSlide, 6000);
}

if (slides.length > 1) {
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            showSlide(index);
            startSlideTimer();
        });
    });

    // Auto start
    startSlideTimer();
}

// Marquee Center Focus Effect
const marqueeContainer = document.querySelector('.marquee-container');
const marqueeLogos = document.querySelectorAll('.client-logo');

function updateMarqueeFocus() {
    if (!marqueeContainer) return;

    const containerRect = marqueeContainer.getBoundingClientRect();
    const centerX = containerRect.left + containerRect.width / 2;

    marqueeLogos.forEach(logo => {
        const rect = logo.getBoundingClientRect();
        const logoCenter = rect.left + rect.width / 2;
        const distance = Math.abs(centerX - logoCenter);

        // Adjust tolerance for center detection
        if (distance < 100) { 
            logo.classList.add('is-focused');
        } else {
            logo.classList.remove('is-focused');
        }
    });
    requestAnimationFrame(updateMarqueeFocus);
}

// Start focus tracking
if (marqueeContainer) {
    updateMarqueeFocus();
}

// Sector Tab Filtering
function initSectorFilter() {
    const tabs = document.querySelectorAll('.sector-tab');
    const tiles = document.querySelectorAll('.ind-tile');

    if (!tabs.length || !tiles.length) return;

    let isTransitioning = false;

    function filterSectors(category) {
        if (isTransitioning) return;
        isTransitioning = true;

        const currentActive = Array.from(tiles).filter(t => t.classList.contains('active'));
        
        // Phase 1: Snappier EXIT
        const transitionDelay = currentActive.length > 0 ? 300 : 0;
        
        if (currentActive.length > 0) {
            currentActive.forEach(tile => {
                tile.style.opacity = '0';
                tile.style.transform = 'translateY(-20px)';
            });
        }

        // Phase 2: SWITCH with mechanical precision
        setTimeout(() => {
            tiles.forEach(tile => {
                tile.classList.remove('active');
                tile.style.opacity = '0';
                tile.style.transform = 'translateY(30px)';

                if (tile.dataset.category === category) {
                    tile.classList.add('active');
                }
            });

            // Phase 3: STAGGERed Solid Entrance
            const newActive = Array.from(tiles).filter(t => t.classList.contains('active'));
            
            newActive.forEach((tile, index) => {
                setTimeout(() => {
                    tile.style.opacity = '1';
                    tile.style.transform = 'translateY(0)';
                }, index * 60); // Snappier stagger for precision feel
            });

            setTimeout(() => {
                isTransitioning = false;
            }, (newActive.length * 60) + 400); 

        }, transitionDelay);
    }

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            if (isTransitioning || tab.classList.contains('active')) return;

            const filter = tab.dataset.filter;
            
            // Update tabs
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            
            filterSectors(filter);
        });
    });

    // Initialize with default view
    filterSectors('industrial');
}

// Excellence Tactical Slider
function initExcellenceSlider() {
    const viewport = document.querySelector('.ex-slider-viewport');
    const nextBtn = document.querySelector('.ex-btn.next');
    const prevBtn = document.querySelector('.ex-btn.prev');
    const seekerBar = document.querySelector('.ex-seeker-bar');
    
    if (!viewport || !nextBtn || !prevBtn || !seekerBar) return;

    const scrollAmount = 560; // Card width (520) + Gap (40)

    nextBtn.addEventListener('click', () => {
        viewport.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    });

    prevBtn.addEventListener('click', () => {
        viewport.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
    });

    viewport.addEventListener('scroll', () => {
        const scrollLeft = viewport.scrollLeft;
        const maxScroll = viewport.scrollWidth - viewport.clientWidth;
        const scrollPercent = (scrollLeft / maxScroll) * 75; // Total bar is 100, handle segment width
        
        seekerBar.style.left = `${scrollPercent}%`;
    });
}

// Product Table Filtering (Product Finder)
function initProductFilter() {
    const filterInput = document.getElementById('productSearch') || document.getElementById('shaftFilter');
    const resultsGrid = document.getElementById('resultsGrid');
    const noResults = document.createElement('div');
    noResults.className = 'no-results';
    noResults.innerHTML = '<i data-lucide="search-x"></i><p>No matching technical specifications found.</p>';
    
    if (resultsGrid) {
        resultsGrid.parentNode.insertBefore(noResults, resultsGrid.nextSibling);
    }

    if (!filterInput || !resultsGrid) return;

    filterInput.addEventListener('input', () => {
        const value = filterInput.value.trim().toLowerCase();
        // Target individual cards again
        const tiles = resultsGrid.querySelectorAll('.spec-tile');
        let hasMatches = false;

        tiles.forEach(tile => {
            const shaftText = tile.dataset.shaft.toLowerCase();
            const designationText = tile.dataset.designation.toLowerCase();
            
            const isNumerical = !isNaN(value) && value !== '';
            
            if (isNumerical) {
                const shaftMatches = shaftText.startsWith(value) || shaftText === value;
                if (shaftMatches) {
                    tile.style.display = '';
                    hasMatches = true;
                } else {
                    tile.style.display = 'none';
                }
            } else {
                if (designationText.includes(value) || shaftText.includes(value)) {
                    tile.style.display = '';
                    hasMatches = true;
                } else {
                    tile.style.display = 'none';
                }
            }
        });

        // Show/Hide No Results State & Grid
        if (hasMatches) {
            resultsGrid.style.display = 'grid';
            noResults.style.display = 'none';
        } else {
            resultsGrid.style.display = 'none';
            noResults.style.display = 'block';
            lucide.createIcons(); 
        }
    });
}

// Mobile Menu Toggle
function initMobileMenu() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            const icon = menuToggle.querySelector('i');
            if (navLinks.classList.contains('active')) {
                icon.setAttribute('data-lucide', 'x');
            } else {
                icon.setAttribute('data-lucide', 'menu');
            }
            lucide.createIcons();
        });

        // Close menu when clicking a link
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                if (!link.classList.contains('dropdown-item') && !link.classList.contains('mega-item')) {
                    navLinks.classList.remove('active');
                    const icon = menuToggle.querySelector('i');
                    icon.setAttribute('data-lucide', 'menu');
                    lucide.createIcons();
                }
            });
        });
    }
}

// Ensure dropdowns and mega menu work on mobile via click if needed
document.querySelectorAll('.has-dropdown > a, .has-mega > a').forEach(dropdownMain => {
    dropdownMain.addEventListener('click', (e) => {
        if (window.innerWidth <= 992) {
            e.preventDefault();
            const parent = dropdownMain.parentElement;
            parent.classList.toggle('mobile-open');
        }
    });
});
// [PDF Reader] Eclipse Immersive Viewer Logic
const initPDFReader = () => {
    const modal = document.getElementById('pdfModal');
    const frame = document.getElementById('pdfFrame');
    const title = document.getElementById('pdfTitle');
    const loadingHud = document.getElementById('pdfLoading');
    const statusText = document.getElementById('readerStatus');
    const closeBtn = document.getElementById('closePdf');
    const readBtns = document.querySelectorAll('.btn-read');

    if (!modal || !frame) return;

    readBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const pdfUrl = btn.getAttribute('data-pdf');
            const pdfTitle = btn.getAttribute('data-title') || 'Newsletter';
            
            // 1. Setup UI
            title.textContent = pdfTitle;
            loadingHud.style.display = 'flex';
            frame.classList.remove('loaded');
            if (statusText) statusText.textContent = 'Loading Document...';
            
            // 2. Open Modal
            document.body.classList.add('modal-open');
            modal.classList.add('active');

            // 3. Inject Source
            setTimeout(() => {
                frame.src = pdfUrl;
            }, 300);
        });
    });

    // Detect Iframe Loading Completion
    frame.addEventListener('load', () => {
        setTimeout(() => {
            loadingHud.style.display = 'none';
            frame.classList.add('loaded');
            if (statusText) statusText.textContent = 'Document Loaded';
        }, 800);
    });

    const closeModal = () => {
        modal.classList.remove('active');
        document.body.classList.remove('modal-open');
        setTimeout(() => {
            frame.src = '';
            frame.classList.remove('loaded');
        }, 400);
    };

    closeBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => {
        if (e.target === modal) closeModal();
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) closeModal();
    });
};

// [Events] Scroll Reveal Logic
const initTimelineReveal = () => {
    const events = document.querySelectorAll('.timeline-event');
    
    if (!events.length) return;

    const observerOption = {
        threshold: 0.25,
        rootMargin: "0px 0px -50px 0px"
    };

    const eventObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('reveal');
                // Optional: Stop observing after reveal
                // eventObserver.unobserve(entry.target);
            }
        });
    }, observerOption);

    events.forEach(event => {
        eventObserver.observe(event);
    });
};

// Global Initialization
document.addEventListener('DOMContentLoaded', () => {
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
    
    initPDFReader();
    initTimelineReveal();
    initSpecTileTilt();
});

// ==========================================================================
// SCHEMATIC 3D TILT ENGINE - Tactical HUD Technical Drawing Interaction
// ==========================================================================
function initSpecTileTilt() {
    const wrap = document.getElementById('schematic3dWrap');
    if (!wrap) return;

    const MAX_TILT = 14;

    wrap.addEventListener('mousemove', (e) => {
        const rect = wrap.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width  - 0.5; // -0.5 to 0.5
        const y = (e.clientY - rect.top)  / rect.height - 0.5;

        const rotX = (-y * MAX_TILT * 2).toFixed(2);
        const rotY = ( x * MAX_TILT * 2).toFixed(2);

        requestAnimationFrame(() => {
            wrap.style.transform = `perspective(1200px) rotateX(${rotX}deg) rotateY(${rotY}deg) scale3d(1.02, 1.02, 1.02)`;
            // Brighten the image under the cursor
            const img = wrap.querySelector('img');
            if (img) {
                const brightness = (1.2 + Math.abs(x) * 0.3 + Math.abs(y) * 0.3).toFixed(2);
                img.style.filter = `invert(1) brightness(${brightness}) sepia(1) hue-rotate(180deg) saturate(3)`;
            }
        });
    });

    wrap.addEventListener('mouseleave', () => {
        requestAnimationFrame(() => {
            wrap.style.transition = 'transform 0.6s cubic-bezier(0.19, 1, 0.22, 1)';
            wrap.style.transform = '';
            const img = wrap.querySelector('img');
            if (img) {
                img.style.transition = 'filter 0.5s ease';
                img.style.filter = 'invert(1) brightness(1.2) sepia(1) hue-rotate(180deg) saturate(3)';
            }
            // Re-enable transition for tilt on next hover
            setTimeout(() => { wrap.style.transition = 'transform 0.08s linear'; }, 650);
        });
    });

    wrap.addEventListener('mouseenter', () => {
        wrap.style.transition = 'transform 0.08s linear';
    });
}
