from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import SnippetForm

from .models import Snippet, Tag, User


@login_required
def snippets(request):
    snippets = Snippet.objects.all()
    return render(request, 'core/snippet_list.html', {'snippets': snippets})


def snippets_new(request):
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.author = request.user
            snippet.save()
            return redirect('snippet-list')
    else:
        form = SnippetForm()
    return render(request, 'core/snippets_edit.html', {'form': form})
