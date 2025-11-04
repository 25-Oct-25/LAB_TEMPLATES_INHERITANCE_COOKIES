# config/settings.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# مفتاح سري للتجارب فقط — لا تستخدمه في الإنتاج
SECRET_KEY = "django-insecure-change-me"

# وضع التطوير: فعّله أثناء البرمجة فقط
DEBUG = True

# قائمة الدومينات المسموح لها بالوصول (خلّه فاضي محليًا)
ALLOWED_HOSTS: list[str] = []

# التطبيقات المفعّلة
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main",  # تطبيقك
]

# الطبقات الوسيطة (Middlewares) الافتراضية
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ملف العناوين الرئيسي
ROOT_URLCONF = "config.urls"

# إعداد القوالب
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],          # نتركها فاضية لأننا نستخدم قوالب داخل التطبيقات
        "APP_DIRS": True,    # يقرأ مجلد templates داخل كل تطبيق تلقائيًا
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# تطبيقات التشغيل
WSGI_APPLICATION = "config.wsgi.application"   # للسيرفرات التقليدية
ASGI_APPLICATION = "config.asgi.application"   # لو استخدمت ASGI/WebSockets

# قاعدة البيانات (SQLite للتجارب)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# (اختياري) مح Validators لكلمات المرور — اتركها كما هي افتراضيًا
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# اللغة والمنطقة الزمنية
LANGUAGE_CODE = "ar"
TIME_ZONE = "Asia/Riyadh"
USE_I18N = True
USE_TZ = True

# الملفات الثابتة (Static)
STATIC_URL = "/static/"
# بما أننا نضع static داخل كل تطبيق، لسنا بحاجة إلى STATICFILES_DIRS هنا.
# للإنتاج لاحقًا:
# STATIC_ROOT = BASE_DIR / "staticfiles"

# ملفات الرفع (Media) — لو احتجتها
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# نوع الحقل التلقائي الافتراضي للموديلات
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
