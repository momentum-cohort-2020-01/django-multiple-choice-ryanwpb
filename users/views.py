from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import SnippetForm

from .models import Snippet, Tag, User


@login_required
def snippets(request):
    snippets = Snippet.objects.all()
    return render(request, 'core/snippet_list.html', {'snippets': snippets})
