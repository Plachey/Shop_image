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
        error_messages={'required': 'Enter email'})
    id_image = forms.CharField(label='your image')
    name = forms.CharField(label='name')
    phone = forms.CharField(label='phone')

    class Meta:
        model = Order
        fields = '__all__'

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password_again'):
            raise forms.ValidationError('Passwords must match!')
        return self.cleaned_data
