from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.utils.text import slugify
from .forms import SnippetForm
from .models import Snippet, Tag, User
from django.db.models import Q


@login_required
def snippets(request):
    def create_sql_query(query_string):
        """
        Splits the string coming in from the front-end into separate words
        and creates a SQL query that will look for any of those words in the 
        title or tags of a snippet.
        """
        query_terms = query_string.split(" ")
        sql_query = Q()
        for term in query_terms:
            sql_query = sql_query | Q(
                tags__name__icontains=term) | Q(title__icontains=term)
        return sql_query

    # Will either be the query string or it will be None
    query = request.GET.get('q')
    if query:
        snippets = Snippet.objects.filter(create_sql_query(query))
    else:
        snippets = Snippet.objects.all()
    context = {'snippets': snippets}
    context['query'] = str(query)
    return render(request, 'core/snippet_list.html', context=context)


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
