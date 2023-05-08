from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import MyUser

UserAdmin.fieldsets += (
    # Добавляем кортеж, где первый элемент — это название раздела в админке,
    # а второй элемент — словарь, где под ключом fields можно указать нужные поля.
    ('Extra Fields', {'fields': ('bio',)}),
)
# Регистрируем модель в админке:
admin.site.register(MyUser, UserAdmin)