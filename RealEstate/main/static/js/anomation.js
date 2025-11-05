document.addEventListener("DOMContentLoaded", () => {
  const title = document.querySelector(".motion-on-click");
  if (title) {
    title.addEventListener("click", () => {
      title.classList.remove("clicked");
      void title.offsetWidth; // تعيد تشغيل الأنيميشن
      title.classList.add("clicked");
    });
  }
});


document.addEventListener("DOMContentLoaded", () => {
  const logo = document.querySelector(".logo-link");
  const title = document.querySelector(".animate-text");

  // 🎥 إعادة تشغيل أنيميشن العنوان عند تحميل الصفحة
  if (title) {
    title.classList.remove("animate-text");
    void title.offsetWidth; // يعيد تشغيل الأنيميشن
    title.classList.add("animate-text");
  }

  // 🌀 عند الضغط على HOME
  if (logo) {
    logo.addEventListener("click", () => {
      logo.classList.remove("clicked-home");
      void logo.offsetWidth;
      logo.classList.add("clicked-home");
    });
  }
});







