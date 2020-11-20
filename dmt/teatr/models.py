from django.db import models
from PIL import Image

from django.core.files.base import ContentFile

from .utils import repertoire_image_path, repertoire_thumbnail_path, get_image_thumbnail, get_optimize_image, actor_image_path


class Actor(models.Model):
    """Актер театра."""

    first_name = models.CharField('Имя', max_length=100, help_text='Введите имя актера')
    last_name = models.CharField('Фамилия', max_length=100, help_text='Введите фамилию актера')
    photo = models.ImageField('Фото', upload_to=actor_image_path)

    class Meta:
        ordering = ['id']
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'
    
    def __str__(self):
        return f"{self.last_name} {self.first_name}"
    
    def save(self, *args, **kwargs):
        self.photo.save('new-resize-photo.jpg', get_image_thumbnail(self.photo, 'actor') , False)
        super().save(*args, **kwargs)
    

class Repertoire(models.Model):
    """Репертуар."""

    title = models.CharField('Заголовок', max_length=200, help_text='Введите название постановки')
    description = models.TextField('Описание', help_text='Введите описание постановки')
    poster = models.ImageField('Постер', upload_to=repertoire_image_path, max_length=250)
    poster_thumbnail = models.ImageField('Миниатюра постера', upload_to=repertoire_thumbnail_path, blank=True, max_length=250)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Репертуар'
        verbose_name_plural = 'Репертуар'
    
    def __str__(self):
        return str(self.title)
    
    def save(self, *args, **kwargs):
        self.poster.save('new-resize-poster.jpg', get_optimize_image(self.poster) , False)
        self.poster_thumbnail.save('new-poster-thumbnail.jpg', get_image_thumbnail(self.poster, "repertoire") , False)
        super().save(*args, **kwargs)


class RepertoirePhoto(models.Model):
    """Фотография репертуара."""

    repertoire = models.ForeignKey('Repertoire', on_delete=models.CASCADE, verbose_name='Постановка', help_text='Выбирете постановку из вашего репертуара')
    description = models.CharField('Описание',  max_length=200, blank=True, help_text='Можете указать описание для фото (не более 200 символов) или оставить пустым')
    image = models.ImageField('Фото', upload_to=repertoire_image_path, max_length=250)
    thumbnail = models.ImageField('Миниатюра', upload_to=repertoire_thumbnail_path, blank=True, max_length=250)
    
    class Meta:
        verbose_name = 'Фотография постановки'
        verbose_name_plural = 'Фотографии постановок'
    
    def __str__(self):
        return f"Фотография постановки {self.repertoire.title}"

    def save(self, *args, **kwargs):
        original_name = str(self.image.name).split('/')[-1]
        self.image.save(original_name, get_optimize_image(self.image) , False)
        self.thumbnail.save(original_name, get_image_thumbnail(self.image, "repertoire") , False)
        super().save(*args, **kwargs)