from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import random
from .models import Poem, Author, Theme

''' Завдання 3 і 4'''

# Випадковий вірш
def random_poem(request):
    poem = random.choice(Poem.objects.all())
    return JsonResponse({'title': poem.title, 'text': poem.text, 'author': poem.author.name, 'theme': poem.theme.name})

# Випадковий вірш автора
def random_poem_by_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    poem = random.choice(author.poems.all())
    return JsonResponse({'title': poem.title, 'text': poem.text, 'author': author.name, 'theme': poem.theme.name})

# Випадковий вірш за тематикою
def random_poem_by_theme(request, theme_id):
    theme = get_object_or_404(Theme, id=theme_id)
    poem = random.choice(theme.poems.all())
    return JsonResponse({'title': poem.title, 'text': poem.text, 'author': poem.author.name, 'theme': theme.name})

# Назви усіх віршів автора
def poems_by_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    titles = list(author.poems.values_list('title', flat=True))
    return JsonResponse({'author': author.name, 'poems': titles})

# Список усіх авторів
def all_authors(request):
    authors = list(Author.objects.values_list('name', flat=True))
    return JsonResponse({'authors': authors})

# Список усіх тематик
def all_themes(request):
    themes = list(Theme.objects.values_list('name', flat=True))
    return JsonResponse({'themes': themes})

# Назви усіх віршів за тематикою
def poems_by_theme(request, theme_id):
    theme = get_object_or_404(Theme, id=theme_id)
    titles = list(theme.poems.values_list('title', flat=True))
    return JsonResponse({'theme': theme.name, 'poems': titles})
