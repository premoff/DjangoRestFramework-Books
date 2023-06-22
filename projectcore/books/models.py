from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class Book(models.Model):
    def nameFile(instance, filename):
     return '/'.join(['images', str(instance.title), filename])
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    pub_year = models.IntegerField()
    cover_img = models.ImageField(upload_to=nameFile,blank=True,error_messages='upload valid file format',validators=[FileExtensionValidator(allowed_extensions=['png','jpg','jpeg','svg'])])
    book_file = models.FileField(upload_to='files',blank=True,validators=[FileExtensionValidator(allowed_extensions=['pdf'])],error_messages='upload valid file format')
    