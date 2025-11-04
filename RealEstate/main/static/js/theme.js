// Dark Mode Toggle with Cookies

// دالة لحفظ الكوكي
function setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = "expires=" + date.toUTCString();
    document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

// دالة لقراءة الكوكي
function getCookie(name) {
    const nameEQ = name + "=";
    const cookies = document.cookie.split(';');
    for(let i = 0; i < cookies.length; i++) {
        let c = cookies[i];
        while (c.charAt(0) === ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

// دالة لتطبيق الثيم
function applyTheme(theme) {
    const body = document.body;
    const lightBtn = document.getElementById('light-mode-btn');
    const darkBtn = document.getElementById('dark-mode-btn');
    const lightImg = lightBtn ? lightBtn.querySelector('img') : null;
    const darkImg = darkBtn ? darkBtn.querySelector('img') : null;

    if (theme === 'dark') {
        body.classList.add('theme-dark');
        if (darkImg) darkImg.classList.add('active');
        if (lightImg) lightImg.classList.remove('active');
        if (darkBtn) darkBtn.setAttribute('aria-pressed', 'true');
        if (lightBtn) lightBtn.setAttribute('aria-pressed', 'false');
    } else {
        body.classList.remove('theme-dark');
        if (lightImg) lightImg.classList.add('active');
        if (darkImg) darkImg.classList.remove('active');
        if (lightBtn) lightBtn.setAttribute('aria-pressed', 'true');
        if (darkBtn) darkBtn.setAttribute('aria-pressed', 'false');
    }
    console.log('Theme applied:', theme); // للتأكد
}

// تطبيق الثيم المحفوظ فوراً قبل تحميل الصفحة
(function() {
    const savedTheme = getCookie('theme');
    if (savedTheme) {
        applyTheme(savedTheme);
    }
})();

// تطبيق الثيم المحفوظ عند تحميل الصفحة
document.addEventListener('DOMContentLoaded', function() {
    const savedTheme = getCookie('theme');
    if (savedTheme) {
        applyTheme(savedTheme);
    }

    // زر الوضع الفاتح
    const lightBtn = document.getElementById('light-mode-btn');
    if (lightBtn) {
        lightBtn.addEventListener('click', function(e) {
            e.preventDefault(); // منع الانتقال للرابط
            setCookie('theme', 'light', 365);
            applyTheme('light');
            console.log('Light mode activated'); // للتأكد
        });
    }

    // زر الوضع الداكن
    const darkBtn = document.getElementById('dark-mode-btn');
    if (darkBtn) {
        darkBtn.addEventListener('click', function(e) {
            e.preventDefault(); // منع الانتقال للرابط
            setCookie('theme', 'dark', 365);
            applyTheme('dark');
            console.log('Dark mode activated'); // للتأكد
        });
    }
});
