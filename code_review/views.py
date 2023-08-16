from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    template = 'main/index.html'
    page_title = 'Последние файлы на проверку'
    context = {
        'title': page_title,
    }

    return render(request, template, context)


@login_required
def upload(request):
    template = 'main/upload.html'
    return render(request, template)
