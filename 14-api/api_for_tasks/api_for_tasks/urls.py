from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('poems/', include('poems.urls')),
    path('predictions/', include('predictions.urls')),
    path("graphql/", GraphQLView.as_view(graphiql=True)),  # GraphiQL IDE
]
