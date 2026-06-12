Олександр, ось повний **README.md** для твого проєкту **Crismastree**, оформлений суцільним markdown‑файлом:

```markdown
# Crismastree Application 🎄

Django web application for managing Christmas Trees with voting system. Users can view trees, see details, and vote (like). The tree with the most likes is highlighted and can be viewed separately as the "Winner".

## Setup and Run

1. Navigate to the project directory:
   ```bash
   cd C:\Users\ADNIN\PycharmProjects\PythonProjects\13\cristmas_tree
   ```

2. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Create a superuser (if you haven't already):
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin user.

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

## Project Structure

```
cristmas_tree/
├── manage.py
├── cristmas_tree/        # project settings, urls
├── crismastree/          # main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       └── crismastree_2026/
│           ├── new_crismastree_list.html
│           ├── cristmas_tree_details.html
│           └── winner.html
└── requirements.txt
```

## Features

- Add new trees via Django Admin.
- View all trees with likes count.
- Like a tree (one like per user).
- Highlight the tree with the most likes.
- Separate "Winner" page showing the most popular tree.

## Documentation

- [Django Official Docs](https://docs.djangoproject.com/en/stable/)
```