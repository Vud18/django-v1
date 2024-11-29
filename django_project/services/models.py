from django.db import models
from filer.fields.image import FilerImageField
from easy_thumbnails.files import get_thumbnailer
from adminsortable.models import SortableMixin


class SliderImage(SortableMixin):
    title = models.CharField(max_length=100, verbose_name="Название")
    image = FilerImageField(
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="slider_images",
        verbose_name="Изображение"
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True, verbose_name="Порядок")

    class Meta:
        ordering = ['order']
        verbose_name = "Изображение слайдера"
        verbose_name_plural = "Изображения слайдера"

    def __str__(self):
        return self.title

    def admin_thumbnail(self):
        """Миниатюра для отображения в админке."""
        if self.image:
            thumbnail_options = {'size': (150, 100), 'crop': True}
            thumbnail_url = get_thumbnailer(self.image).get_thumbnail(thumbnail_options).url
            return f'<img src="{thumbnail_url}" style="max-width: 150px; max-height: 100px;" />'
        return "Нет изображения"
    admin_thumbnail.short_description = "Миниатюра"
    admin_thumbnail.allow_tags = True

