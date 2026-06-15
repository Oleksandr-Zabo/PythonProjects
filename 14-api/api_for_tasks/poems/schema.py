import random
import graphene
from graphene_django import DjangoObjectType
from .models import Poem, Author, Theme

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ("id", "name", "poems")

class ThemeType(DjangoObjectType):
    class Meta:
        model = Theme
        fields = ("id", "name", "poems")

class PoemType(DjangoObjectType):
    class Meta:
        model = Poem
        fields = ("id", "title", "text", "author", "theme")

class Query(graphene.ObjectType):
    random_poem = graphene.Field(PoemType)
    random_poem_by_author = graphene.Field(PoemType, author_id=graphene.Int(required=True))
    random_poem_by_theme = graphene.Field(PoemType, theme_id=graphene.Int(required=True))

    poems_by_author = graphene.List(graphene.String, author_id=graphene.Int(required=True))
    all_authors = graphene.List(graphene.String)
    all_themes = graphene.List(graphene.String)
    poems_by_theme = graphene.List(graphene.String, theme_id=graphene.Int(required=True))

    def resolve_random_poem(root, info):
        return random.choice(Poem.objects.all())

    def resolve_random_poem_by_author(root, info, author_id):
        author = Author.objects.get(id=author_id)
        return random.choice(author.poems.all())

    def resolve_random_poem_by_theme(root, info, theme_id):
        theme = Theme.objects.get(id=theme_id)
        return random.choice(theme.poems.all())

    def resolve_poems_by_author(root, info, author_id):
        author = Author.objects.get(id=author_id)
        return list(author.poems.values_list("title", flat=True))

    def resolve_all_authors(root, info):
        return list(Author.objects.values_list("name", flat=True))

    def resolve_all_themes(root, info):
        return list(Theme.objects.values_list("name", flat=True))

    def resolve_poems_by_theme(root, info, theme_id):
        theme = Theme.objects.get(id=theme_id)
        return list(theme.poems.values_list("title", flat=True))
