1) EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
2) -python manage.py shell 
  -from django.core.mail import send_mail
  -send_mail(
     "От Балакирева",
     "Поздравляем! Вы успешно прошли курс по Django.",
     "root@site.com",
     ["you@mail.com"],
)