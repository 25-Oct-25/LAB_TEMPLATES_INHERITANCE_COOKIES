function zoomLeft(el) {
    el.style.transformOrigin = "left center"; 
    el.style.transition = "transform 2s ease";
    el.style.transform = "scale(1.3)";
    setTimeout(() => {
      el.style.transform = "scale(1)";
    }, 2000);
  }