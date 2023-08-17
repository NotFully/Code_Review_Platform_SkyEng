from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import FileForm, ReviewCommentForm
from .models import User, File, ReviewComment
from django.core.paginator import Paginator


def index(request):
    template = 'main/index.html'
    page_title = 'Последние файлы на проверку'
    context = {
        'title': page_title,
    }

    return render(request, template, context)


def reviewlist(request, username):
    template = 'main/reviewlist.html'
    user = get_object_or_404(User, username=username)
    file_list = user.files.filter()
    paginator = Paginator(file_list, 10)
    page_number = request.GET.get('page')
    page_files = paginator.get_page(page_number)
    context = {
        'user': user,
        'page_files': page_files,
    }
    return render(request, template, context)


@login_required
def upload(request):
    template = 'main/upload.html'
    form = FileForm(
        request.POST or None,
        files=request.FILES or None
    )
    if form.is_valid():
        temp_form = form.save(commit=False)
        temp_form.user = request.user
        temp_form.save()
        return redirect(
            'main:reviewfileslist', temp_form.user
        )

    return render(request, template, {'form': form})


def post_edit(request, file_id):
    template = 'main/upload.html'
    file = get_object_or_404(File, pk=file_id)
    if file.user != request.user:
        return redirect(
            'posts:post_detail', file_id
        )
    form = FileForm(
        request.POST or None,
        files=request.FILES or None,
        instance=file
    )
    if form.is_valid():
        form.save()
        return redirect(
            'main:review_detail', file_id
        )
    return render(request, template, {
        'form': form, 'is_edit': True, 'file': file
    })
