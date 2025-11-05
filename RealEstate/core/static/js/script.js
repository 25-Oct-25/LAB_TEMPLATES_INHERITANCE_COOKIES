document.addEventListener("DOMContentLoaded", () => {
    const body = document.body;
    const themeBtns = document.querySelectorAll(".theme-btn");
    const savedTheme = localStorage.getItem("theme") || "light-mode";
    body.className = savedTheme;
    updateActive();
    applyHeroBackground();
      themeBtns.forEach((btn) => {
      btn.addEventListener("click", () => {
        const newTheme = btn.dataset.theme === "dark" ? "dark-mode" : "light-mode";
        body.className = newTheme;
        localStorage.setItem("theme", newTheme);
        updateActive();
        applyHeroBackground();
        document.dispatchEvent(new CustomEvent("themechange"));
      });
    });
      function updateActive() {
      const isDark = body.classList.contains("dark-mode");
      themeBtns.forEach((b) => b.classList.remove("active"));
      document
        .querySelector(`.theme-btn[data-theme="${isDark ? "dark" : "light"}"]`)
        ?.classList.add("active");
    }
      function applyHeroBackground() {
      const hero = document.querySelector(".hero-section");
      if (!hero) return;
  
      const isDark = body.classList.contains("dark-mode");

      const imagePath = isDark
        ? "/static/images/skyscraper-dark.jpg"
        : "/static/images/skyscraper.jpeg";
  
      hero.style.backgroundImage = `url("${imagePath}")`;
    }
  });
  