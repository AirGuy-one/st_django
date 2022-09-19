from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News, Category
from .forms import NewsForm, CategoryForm


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'title': 'Список новостей',
        'news': news,
        'category': category
    }
    return render(request, 'news/category.html', context)


def add_new_news(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была заполнена неверно'

    form = NewsForm()

    data = {
        'form': form
    }

    return render(request, 'news/add.html', data)


def add_new_category(request):
    error = ''
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is incorrect'

    form = CategoryForm()

    data = {
        'form': form
    }

    return render(request, 'news/add_category.html', data)


def settings_of_news(request):
    return render(request, 'news/settings.html')


def delete_news_method(request):
    news = News.objects.all()
    context = {
        'title': 'just_title',
        'news': news
    }
    return render(request, 'news/delete_news.html', context)


def delete_category_method(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'news/delete_category.html', context)


def test(request):
    return HttpResponse('<h1>TEST PAGE</h1>')

