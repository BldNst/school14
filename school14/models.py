from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField

class News(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    title = models.CharField(verbose_name='Название', max_length=200)
    content = CKEditor5Field(verbose_name='Содержание', config_name='extends')
    pub_date = models.DateField(verbose_name='Дата публикации')


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('title',)
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class MenuItem(MPTTModel):
    id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(verbose_name='Название', max_length=100, unique=True)
    url = models.CharField('Ссылка', max_length=255)
    position = models.PositiveIntegerField('Позиция', default=1)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    content = RichTextUploadingField( verbose_name='Содержание', config_name='extends', null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['position']

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'    

        
class Teacher(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    FIO = models.CharField(max_length=150, verbose_name='ФИО учителя')
    foto = RichTextUploadingField( verbose_name='Фото учителя', null = True, blank = True)
    dolg = models.CharField(max_length=150, verbose_name='Должность')
    pub = RichTextUploadingField(max_length=500, verbose_name='Данные учителя')


    def __str__(self):
        return self.FIO
    
    class Meta:
        ordering = ('FIO',)
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

