from django.db import models

# Create your models here.
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
    date = models.DateTimeField(db_index=True, verbose_name='Date and Time')
    price = models.FloatField(verbose_name='Price')
    like = models.IntegerField(default=0, db_index=True, verbose_name='Like')

    def __str__(self):
        return self.title

'''
class User(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Name')
    last_name = models.CharField(max_length=30, verbose_name='Surname')
    login = models.CharField(max_length=30, verbose_name='Login')
    password = models.CharField(max_length=30, verbose_name='Password')
    buy = models.ForeignKey(Image, on_delete=models.CASCADE, verbose_name='purchase')
'''
class Order(models.Model):
    id_image = models.ForeignKey(Image, on_delete=models.CASCADE, verbose_name='purchase')
    name = models.CharField(max_length=30, verbose_name='Name')
    email = models.CharField(max_length=30, verbose_name='Email')
    phone = models.CharField(max_length=30, verbose_name='Phone')
