from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify

from page.models import Carousel, Page
from django.contrib import messages
from .forms import CarouselModelForm, PageModelForm

from product.models import Category, Product

STATUS = "published"


def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(status=STATUS).exclude(cover_image="")
    context['products'] = Product.objects.filter(is_home=True, status=STATUS, )
    return render(request, 'page/index.html', context)


def manage_list(request):
    context = dict()
    return render(request, 'manage/manage.html', context)


def page_show(request, slug):
    context = dict()
    context['page'] = get_object_or_404(Page, slug=slug)
    return render(request, 'page/page.html', context)


# PAGE PART

@staff_member_required
def page_list(request):
    context = dict()
    context['items'] = Page.objects.all().order_by('-pk')
    return render(request, 'manage/page_list.html', context)


def page_create(request):
    if request.method == 'POST':
        form = PageModelForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.slug = slugify(item.title.replace('ı', 'i'))
            item.save()
            messages.add_message(request, messages.INFO, 'Kaydınız başarı ile alınmıştır')
        return redirect('/page/create/')
    else:
        context = dict()
        context['form'] = PageModelForm()
        context['title'] = "Page Create Form"
        return render(request, 'manage/form.html', context)


def page_update(request, pk):
    context = dict()
    item = Page.objects.get(pk=pk)
    context['title'] = f"{item.title} - pk:{item.pk} - Page Update Form"
    context['form'] = PageModelForm(instance=item)
    if request.method == "POST":
        form = PageModelForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            if item.slug == "":
                item.slug = slugify(item.title.replace('ı', 'i'))
            item.save()
            messages.warning(request, 'Başarılı şekilde güncellediniz')
            return redirect('page:page_update', pk)
    return render(request, 'manage/form.html', context)


def page_delete(request, pk):
    item = Page.objects.get(pk=pk)
    item.status = "deleted"
    item.save()
    return redirect('page:page_list')


# CAROUSEL PART
def carousel_list(request):
    context = dict()
    context['carousel'] = Carousel.objects.all().order_by('-pk')
    return render(request, 'manage/carousel_list.html', context)


def carousel_create(request):
    if request.method == 'POST':
        form = CarouselModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Kaydınız başarı ile alınmıştır')
        return redirect('/carousel/create/')
    else:
        context = dict()
        context['form'] = CarouselModelForm()
        context['title'] = "Carousel Create Form"
        return render(request, 'manage/form.html', context)


def carousel_update(request, pk):
    context = dict()
    item = Carousel.objects.get(pk=pk)
    context['title'] = f"{item.title} - pk:{item.pk} - Carousel Update  Form"
    context['form'] = CarouselModelForm(instance=item)
    if request.method == "POST":
        form = CarouselModelForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.warning(request, 'Başarılı şekilde güncellediniz')
            return redirect('page:carousel_update', pk)
    return render(request, 'manage/form.html', context)
