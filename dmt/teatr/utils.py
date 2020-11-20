import uuid
from io import BytesIO

from transliterate import translit
from django.utils import timezone
from PIL import Image
from django.core.files.base import ContentFile
from django.utils.text import slugify


SIZE_FOR_IMAGE_TYPE = {
    'actor': (400, 400),
    'repertoire': (450, 450),
    'large': (1920, 1080)
}
## генерация пути и названия изображения

def _generate_repertoire_images_path(instance, filename, thumbnail=False):
    if hasattr(instance, 'repertoire'):
        repertoire_title = instance.repertoire.title
    elif hasattr(instance, 'title'):
        repertoire_title = instance.title
    if thumbnail:
        image_type = 'thumbnail'
    else:
        image_type = 'large'
    repertoire_folder_name = slugify(translit(repertoire_title.lower().replace(' ', '-'), 'ru', reversed=True))
    current_date = timezone.now().strftime("%Y-%m-%d")
    file_format = filename.split('.')[-1]
    return f"repertoire/{repertoire_folder_name}/large/{repertoire_folder_name}-{current_date}-{uuid.uuid4().hex}.{file_format}"

def repertoire_image_path(instance, filename):
    file_path = _generate_repertoire_images_path(instance, filename)
    return file_path

def repertoire_thumbnail_path(instance, filename):
    file_path = _generate_repertoire_images_path(instance, filename, thumbnail=True)
    return file_path

def _generate_actor_image_path(instance, filename):
    actor_full_name = slugify(translit(str(instance).lower().replace(' ', '-'), 'ru', reversed=True))
    current_date = timezone.now().strftime("%Y-%m-%d")
    file_format = filename.split('.')[-1]
    return f"actor/thumbnail/{actor_full_name}-{current_date}-{uuid.uuid4().hex}.{file_format}"

def actor_image_path(instance, filename):
    file_path = _generate_actor_image_path(instance, filename)
    return file_path

## Оптимизация изображения и создание миниатюры

def _resize_image(original_image, size):
    img = Image.open(original_image)
    img.thumbnail(size)
    imgIO = BytesIO()
    img.save(imgIO, 'JPEG')
    return imgIO

def get_optimize_image(original_image):
    size = SIZE_FOR_IMAGE_TYPE['large']
    return ContentFile(_resize_image(original_image, size).getvalue())

def get_image_thumbnail(original_image, type:str):
    """type = 'actor' or 'repertoire'"""

    size = SIZE_FOR_IMAGE_TYPE.get(type)
    if not size:
        pass
    return ContentFile(_resize_image(original_image, size).getvalue())
    