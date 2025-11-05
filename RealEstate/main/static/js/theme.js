document.addEventListener("DOMContentLoaded", () => {
  const heroTitle = document.querySelector('.hero-title');

  function replayAnimation(element, animationName) {
    element.style.animation = 'none';
    element.offsetHeight;
    element.style.animation = `${animationName} 1.6s ease-out forwards`;
  }

 
  if (heroTitle) {
    replayAnimation(heroTitle, 'slideZoomIn');
  }

 
  if (heroTitle) {
    heroTitle.addEventListener('click', () => {
      replayAnimation(heroTitle, 'slideZoomIn');
    });
  }
});
