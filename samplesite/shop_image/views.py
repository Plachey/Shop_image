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
                return HttpResponse('Order is processed!')
        else:
            form = BuyForm()
        return render(request, 'form_buy.html', {'form': form})
