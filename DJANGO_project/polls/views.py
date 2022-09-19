from django.shortcuts import render


def index_html(request):
    return render(request, 'polls/index.html')

