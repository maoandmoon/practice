from django.db import models
from django.utils.safestring import mark_safe
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize
from salon.validators import validate_phone_number


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Название')
    description = models.CharField(max_length=300, verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


def get_del_cat():
    return Category.objects.get_or_create(title='DELETED')


class SubCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.SET(get_del_cat), verbose_name='Категория')
    description = models.CharField(max_length=300, verbose_name='Описание', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Подкатегории'
        verbose_name = 'Подкатегория'

    def __str__(self):
        return self.title




def get_del_subcat():
    return SubCategory.objects.get_or_create(title='DELETED')


class PriceItem(models.Model):
    title = models.CharField(max_length=400, verbose_name='Наименование')
    description = models.CharField(max_length=300, verbose_name='Описание', blank=True, null=True)
    price = models.CharField(max_length=150, verbose_name='Цена', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET(get_del_cat), verbose_name='Категория',
                                 related_name='category_linked_models')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET(get_del_subcat), verbose_name='Подкатегория', null=True, blank=True,
                                    related_name='related_subcategory_models')
    for_inline = models.ForeignKey('self', models.CASCADE, related_name='inline_price_models', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Прайс'
        verbose_name = 'Артикл'


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    message = models.TextField(max_length=1000, verbose_name='Сообщение', blank=True, null=True)
    phone = models.CharField(max_length=100, verbose_name="Номер телефона", validators=[validate_phone_number])
    created = models.DateTimeField(verbose_name='Создана', auto_now_add=True)

    def __str__(self):
        return "%s | %s | %s " % (self.created.strftime("%d.%m | %H:%M"), self.name, self.phone)

    def clean(self):
        return super(Contact, self).clean()

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class ImageCard(models.Model):
    image = models.ImageField(verbose_name='Фотография', upload_to='images', blank=True, null=True)
    thumb = ImageSpecField(source='image', options={'quality': 100}, processors=[SmartResize(900, 375)])

    def __str__(self):
        return self.thumbnail()

    def thumbnail(self):
        if self.image:
            return mark_safe(
                '<img style="height:180px;width:400px;" src="{0}"/>'.format(self.thumb.url))
        return mark_safe('<p>=(</p>')

    thumbnail.short_description = 'Миниатюра'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class InstagramLink(models.Model):
    image = models.ImageField(verbose_name='Обложка паблика', upload_to='images', blank=True, null=True)
    thumb = ImageSpecField(source='image', options={'quality': 80}, processors=[SmartResize(225, 225)])
    link = models.CharField(max_length=250, verbose_name='Ссылка на паблик',
                            default='https://www.instagram.com/praktikabeauty/')

    def __str__(self):
        return self.thumbnail()

    def thumbnail(self):
        if self.image:
            return mark_safe(
                '<img style="height:180px;width:180px;" src="{0}"/>'.format(self.thumb.url))
        return mark_safe('<p>=(</p>')

    thumbnail.short_description = 'Миниатюра'

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
