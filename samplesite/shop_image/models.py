from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Image(models.Model):
    title = models.CharField(max_length=40, verbose_name='Title')
    image = models.ImageField(upload_to='images/', verbose_name='Image')
    CHOISE_CATEGORY = [
        ('winter', 'Winter'),
        ('autumn', 'Autumn'),
        ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('common', 'Common'),
        ('family', 'Family'),
        ('nature', 'Nature'),
        ('girl', 'Girl'),
        ('joy', 'Joy'),
        ('animals', 'Animals')
    ]
    category = models.CharField(max_length=20, choices=CHOISE_CATEGORY, default='common')
    date = models.DateTimeField(verbose_name='Date and Time')
    price = models.FloatField(verbose_name='Price')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_view', kwargs={'pk': self.pk})


class Order(models.Model):
    id_image = models.ForeignKey(Image, on_delete=models.CASCADE, verbose_name='purchase')
    name = models.CharField(max_length=30, verbose_name='Name')
    email = models.CharField(max_length=30, verbose_name='Email')
    phone = models.CharField(max_length=30, verbose_name='Phone')


class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(max_length=140)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date comment')

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('image_list')
