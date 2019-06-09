from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Image, Comment
from .forms import ImageFilterForm, BuyForm, CommentForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect


class MainPageView(ListView):
    model = Image
    template_name = 'home.html'
    context_object_name = 'all_image_list'

    def get(self, request):
        form = ImageFilterForm()
        images = MainPageView.model.objects.all()[:20]
        return render(request, 'home.html', {'form1': form, 'all_image_list': images})

    def post(self, request):
        if 'flt_category' in request.POST:
            form = ImageFilterForm(request.POST)
            if form.is_valid():
                category = form.cleaned_data['filter_category']
                date = form.cleaned_data['order_date']
                if category == 'all':
                    args = {'form1': form,
                            'all_image_list': Image.objects.all().order_by(date)}
                else:
                    args = {'form1': form,
                            'all_image_list': Image.objects.filter(category=category).order_by(date)}
                return render(request, 'home.html', args)
        return render(request, 'home.html', {'form1': form})


def detail_image(request, pk):
    image = get_object_or_404(Image, id=pk)
    comment = Comment.objects.filter(image=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.image = image
            form.save()
            return redirect(detail_image, pk)
    else:
        form = CommentForm()
    return render(request, 'detail_image.html', {'image': image, 'comment': comment, 'form': form})


class FormBuy(TemplateView):
    template_name = 'form_buy.html'

    def get(self, request):
        form = BuyForm()
        return render(request, 'form_buy.html', {'form': form})

    def post(self, request):
        if request.POST:
            form = BuyForm(request.POST)
            if form.is_valid():
                # Просто выводим сообщение о том, что все ОК!
                return HttpResponse('Форма верна!')
        else:
            form = BuyForm()
        return render(request, 'form_buy.html', {'form': form})

'''
from .liqpay3 import LiqPay

from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

class PayView(TemplateView):
    template_name = 'billing/pay.html'

def get(self, request, *args, **kwargs):
    liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
    params = {
        'action': 'pay',
        'amount': '100',
        'currency': 'USD',
        'description': 'Payment for clothes',
        'order_id': 'order_id_1',
        'version': '3',
        'sandbox': 0, # sandbox mode, set to 1 to enable it
        'server_url': 'https://test.com/billing/pay-callback/', # url to callback view
    }
    signature = liqpay.cnb_signature(params)
    data = liqpay.cnb_data(params)
    return render(request, self.template_name, {'signature': signature, 'data': data})

@method_decorator(csrf_exempt, name='dispatch')
class PayCallbackView(View):
    def post(self, request, *args, **kwargs):
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        data = request.POST.get('data')
        signature = request.POST.get('signature')
        sign = liqpay.str_to_sign(settings.LIQPAY_PRIVATE_KEY + data + settings.LIQPAY_PRIVATE_KEY)
        if sign == signature:
            print('callback is valid')
        response = liqpay.decode_data_from_str(data)
        print('callback data', response)
        return HttpResponse()
'''