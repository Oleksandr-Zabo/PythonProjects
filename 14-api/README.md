
# API for Predictions & Poems 🎭📜

Django web application providing REST and GraphQL APIs for two modules:
- **predictions** — повертає випадкові передбачення та випадкові числа.
- **poems** — працює з віршами, авторами та тематиками.

## Setup and Run

1. Navigate to the project directory:
   ```bash
   cd C:\Users\ADNIN\PycharmProjects\PythonProjects\14-api\api_for_tasks
   ```

2. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Create a superuser (optional, для доступу до Django Admin):
   ```bash
   python manage.py createsuperuser
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

   The application will be accessible at:
   ```
   http://127.0.0.1:8000/
   ```

   Admin panel:
   ```
   http://127.0.0.1:8000/admin/
   ```

   GraphQL IDE:
   ```
   http://127.0.0.1:8000/graphql/
   ```

## Requirements

У файлі `requirements.txt` мають бути:
```text
Django>=5.0
graphene-django
```

Встановлення залежностей:
```bash
pip install -r requirements.txt
```

## Project Structure

```
api_for_tasks/
├── manage.py
├── api_for_tasks/       # project settings, urls, schema
├── predictions/         # app for predictions
│   ├── views.py
│   ├── urls.py
│   └── schema.py
├── poems/               # app for poems
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── schema.py
└── requirements.txt
```

## REST Endpoints

- `/predictions/prediction/` → випадкове пророцтво  
- `/predictions/random-number/` → випадкове число (32 біти)  
- `/predictions/random-range/<start>/<end>/` → випадкове число у діапазоні  
- `/predictions/random-numbers/<start>/<end>/<count>/` → список випадкових чисел  
- `/poems/random/` → випадковий вірш  
- `/poems/random/author/<id>/` → випадковий вірш автора  
- `/poems/random/theme/<id>/` → випадковий вірш за тематикою  
- `/poems/authors/` → список авторів  
- `/poems/themes/` → список тематик  
- `/poems/author/<id>/poems/` → всі вірші автора  
- `/poems/theme/<id>/poems/` → всі вірші за тематикою  

## GraphQL Examples

Використовуй GraphQL IDE за адресою `http://127.0.0.1:8000/graphql/` [(127.0.0.1 in Bing)](https://www.bing.com/search?q="http%3A%2F%2F127.0.0.1%3A8000%2Fgraphql%2F") для виконання запитів:

```graphql
query {
  randomPrediction
  randomNumber
  randomNumberByRange(start: 10, end: 100)
  randomNumbers(start: 1, end: 50, count: 5)
  
  randomPoem {
    title
    text
    author { name }
    theme { name }
  }
  randomPoemByAuthor(authorId: 1) {
    title
    text
  }
  allAuthors
  poemsByTheme(themeId: 2)
}
```

## Features

- REST API для швидких запитів.
- GraphQL API для складних вибірок.
- Моделі Author, Theme, Poem з пов’язаними даними.
- Django Admin для керування записами.
- Випадкові передбачення та генерація чисел.

## Documentation

- [Django Official Docs](https://docs.djangoproject.com/en/stable/)  
- Graphene-Django Docs [(docs.graphene-python.org in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fdocs.graphene-python.org%2Fprojects%2Fdjango%2Fen%2Flatest%2F")
