from django.db import models


class Actor(models.Model):
    """Актер театра."""

    first_name = models.CharField('Имя', max_length=100, help_text='Введите имя актера')
    last_name = models.CharField('Фамилия', max_length=100, help_text='Введите фамилию актера')
    photo = models.ImageField('Фото', upload_to ='photo/actors/')

    class Meta:
        ordering = ['id']
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Repertoire(models.Model):
    """Репертуар."""

    title = models.CharField('Заголовок', max_length=200, help_text='Введите название постановки')
    description = models.TextField('Описание', help_text='Введите описание постановки')
    poster = models.ImageField('Постер', upload_to='photo/repertoire/')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Репертуар'
        verbose_name_plural = 'Репертуар'
    
    def __str__(self):
        return str(self.title)


class RepertoirePhoto(models.Model):
    """Фотография репертуара."""

    repertoire = models.ForeignKey('Repertoire', on_delete=models.CASCADE, verbose_name='Постановка', help_text='Выбирете постановку из вашего репертуара')
    description = models.CharField('Описание',  max_length=200, blank=True, help_text='Можете указать описание для фото (не более 200 символов) или оставить пустым')
    image = models.ImageField('Фото', upload_to='photo/repertoire/')
    
    class Meta:
        verbose_name = 'Фотография постановки'
        verbose_name_plural = 'Фотографии постановок'
    
    def __str__(self):
        return f"Фотография постановки {self.repertoire.title}"
