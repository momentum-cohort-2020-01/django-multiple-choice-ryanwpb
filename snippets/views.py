from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.utils.text import slugify
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
            form.save_m2m()
            return redirect('snippet-list')
    else:
        form = SnippetForm()
    return render(request, 'core/snippets_edit.html', {'form': form})


def snippet_details(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    return render(request, "core/snippet_details.html", {'snippet': snippet, 'pk': pk})


def snippets_edit(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.save()
            form.save_m2m()
            return redirect('snippet-details', snippet.pk)
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'core/snippets_edit.html', {'form': form})


def snippets_delete(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    snippet.delete()
    return redirect('snippet-list')
