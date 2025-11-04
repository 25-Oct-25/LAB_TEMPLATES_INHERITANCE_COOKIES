document.addEventListener('DOMContentLoaded', () => {
  const heroText = document.querySelector('.animate-text');
  
  if (heroText) {
    heroText.addEventListener('click', () => {
      heroText.classList.remove('animate-text');
      void heroText.offsetWidth; 
      heroText.classList.add('animate-text');
    });
  }
});
