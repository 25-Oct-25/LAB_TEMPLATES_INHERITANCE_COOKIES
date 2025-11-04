document.addEventListener("DOMContentLoaded", () => {
  const body = document.body;
  const sunIcon = document.querySelector('.sun-icon');
  const moonIcon = document.querySelector('.moon-icon');
  const heroTitle = document.querySelector('.hero-title');

  function replayAnimation(element, animationName) {
    element.style.animation = 'none';
    element.offsetHeight;
    element.style.animation = `${animationName} 1.6s ease-out forwards`;
  }


  if (heroTitle) {
    replayAnimation(heroTitle, 'slideZoomIn');
  }

  if (sunIcon) {
    sunIcon.addEventListener('click', (e) => {
      e.preventDefault();
      fetch(sunIcon.parentElement.href)
        .then(() => {
          body.classList.remove('dark-mode');
          sunIcon.classList.add('active');
          moonIcon.classList.remove('active');  
          replayAnimation(heroTitle, 'slideZoomIn');
        });
    });
  }

 
  if (moonIcon) {
    moonIcon.addEventListener('click', (e) => {
      e.preventDefault();
      fetch(moonIcon.parentElement.href)
        .then(() => {
          body.classList.add('dark-mode');
          moonIcon.classList.add('active');
          sunIcon.classList.remove('active'); 
          replayAnimation(heroTitle, 'slideZoomIn');
        });
    });
  }

  if (heroTitle) {
    heroTitle.addEventListener('click', () => {
      replayAnimation(heroTitle, 'slideZoomIn');
    });
  }
});
