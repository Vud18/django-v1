from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import SliderImage


@admin.register(SliderImage)
class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('admin_thumbnail', 'title', 'order')  # Порядок добавлен для наглядности
    list_display_links = ('admin_thumbnail', 'title')  # Делаем кликабельными миниатюру и название
    search_fields = ('title', 'description')  # Поиск по названию и описанию
    list_per_page = 10  # Количество записей на странице

    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'description'),
            'description': "Добавьте изображение, которое будет отображаться в слайдере.",
        }),
    )
