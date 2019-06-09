from django import forms
from django.forms import ModelForm
from .models import Order, Comment


class ImageFilterForm(forms.Form):
    filter_category = forms.ChoiceField(label='filter_category', required=False, choices=[
        ['all', 'All'],
        ['winter', 'Winter'],
        ['autumn', 'Autumn'],
        ['spring', 'Spring'],
        ['summer', 'Summer'],
        ['common', 'Common'],
        ['family', 'Family'],
        ['nature', 'Nature'],
        ['girl', 'Girl'],
        ['joy', 'Joy'],
        ['animals', 'Animals']
    ])

    order_date = forms.ChoiceField(label='sorted', required=False, choices=[
        ['-date', 'date old to new'],
        ['date', 'date new to old'],
        ['price', 'price low to high'],
        ['-price', 'price high to low']
    ])


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class BuyForm(forms.Form):
    email = forms.CharField(
        label='Email',
        max_length=100,
        error_messages={'required': 'Укажите email'})
    id_image = forms.CharField(label='your image')
    name = forms.CharField(label='name')
    phone = forms.CharField(label='phone')

    class Meta:
        model = Order
        fields = '__all__'

    # Валидация проходит в этом методе
    def clean(self):
        # Определяем правило валидации
        if self.cleaned_data.get('password') != self.cleaned_data.get('password_again'):
            # Выбрасываем ошибку, если пароли не совпали
            raise forms.ValidationError('Пароли должны совпадать!')
        return self.cleaned_data
