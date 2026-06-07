# Authors HW

Django web application for managing authors and their books.

## Models

### Author
- `name`: CharField (max_length=100)
- `slug`: SlugField (unique=True)
- `bio`: TextField
- `birth_year`: IntegerField
- `death_year`: IntegerField (nullable, blankable)

### Book
- `title`: CharField (max_length=200)
- `slug`: SlugField (unique=True)
- `author`: ForeignKey to Author (on_delete=models.CASCADE, related_name='books')
- `year`: IntegerField
- `description`: TextField
- `rating`: IntegerField (default=0)

## Setup and Run

1.  **Navigate to the project directory:**
    ```bash
    cd C:/Users/ADNIN/PycharmProjects/PythonProjects/11/authors_hw
    ```

2.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

3.  **Create a superuser (if you haven't already):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create an admin user.

4.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000/`.

## Admin Panel

Access the Django admin interface at:
- `http://127.0.0.1:8000/admin/`

You can use the superuser credentials created in step 3 of the "Setup and Run" section to log in.

### Adding Data via Admin

1.  **Add Authors:**
    - Go to `/admin/`
    - Under **Authors**, click **Authors**
    - Click **Add author +**
    - Fill in the author's details (Name, Slug, Bio, Birth Year, Death Year)
    - Click **Save**

2.  **Add Books:**
    - Go to `/admin/`
    - Under **Authors**, click **Books**
    - Click **Add book +**
    - Fill in the book's details (Title, Slug, Author, Year, Description, Rating)
    - Select an existing author from the dropdown.
    - Click **Save**
