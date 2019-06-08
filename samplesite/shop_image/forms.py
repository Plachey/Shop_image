from django import forms
from .models import Order


class ImageFilterForm(forms.Form):
    filter_category = forms.ChoiceField(label='sorted_category', required=False, choices=[
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

    order_date = forms.ChoiceField(label='sorted_date', required=False, choices=[
        #['default', 'Default'],
        ['-date', 'old to new'],
        ['date', 'new to old']
    ])

    order_price = forms.ChoiceField(label='sorted_price', required=False, choices=[
        #['default', 'Default'],
        ['price', 'low to high'],
        ['-price', 'high to low']
    ])

    order_like = forms.ChoiceField(label='sorted_like', required=False, choices=[
        #['default', 'Default'],
        ['like', 'less to more'],
        ['-like', 'more to less']
    ])


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
        filds = '__all__'

    '''
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        error_messages={'required': 'Укажите пароль'})
    password_again = forms.CharField(
        label='Password (again)',
        widget=forms.PasswordInput(),
        error_messages={'required': 'Укажите пароль еще раз'})
    '''

    # Валидация проходит в этом методе
    def clean(self):
        # Определяем правило валидации
        if self.cleaned_data.get('password') != self.cleaned_data.get('password_again'):
            # Выбрасываем ошибку, если пароли не совпали
            raise forms.ValidationError('Пароли должны совпадать!')
        return self.cleaned_data

#['Winter', 'Autumn', 'Spring', 'Summer', 'Common', 'Family', 'Nature', 'Girl', 'Joy', 'Animals']
