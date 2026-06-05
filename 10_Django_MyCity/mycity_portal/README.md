# MyCity Portal

Django web app with routing for city sections and database integration.

## Routes

### Main sections
- `/` - Home
- `/news/` - City news
- `/management/` - City heads
- `/facts/` - Facts about city
- `/services/` - Contact phones of city services
- `/landmarks/` - Notable city landmarks  
- `/people/` - Notable people (with presentation slides from `cityinfo/static/cityinfo/Names/`)
- `/photos/` - Photo albums
- `/history/` - City history
- `/history/people/` - Notable historical residents
- `/history/photos/` - Historical photos
- `/news/<any>`, `/facts/<any>`, etc. — catch-all for subdirs (Task 2)

### Database gallery
- `/gallery/` - Local gallery from database
- Add images via admin panel: `/admin/` → Gallery

## Run

```powershell
cd C:\Users\ADNIN\PycharmProjects\PythonProjects\10_Django_MyCity\mycity_portal
python manage.py migrate
python manage.py runserver
```

## Admin Panel

Create superuser (if needed):
```powershell
python manage.py createsuperuser
```

Access admin at:
- http://127.0.0.1:8000/admin/

### Add Gallery Images via Admin

1. Go to `/admin/`
2. Under **Cityinfo**, click **Galleries**
3. Click **Add Gallery**
4. Fill in:
   - **Назва** (Title): e.g., "My Photo"
   - **Опис** (Description): optional
   - **Зображення** (Image): upload PNG/JPG
   - **Активна** (Active): check to show
   - **Порядок** (Order): sort by this value
5. Click **Save**
6. View uploaded images at: http://127.0.0.1:8000/gallery/

## Features
- Web scraping with built-in HTML parser (no external deps except Pillow)
- Catch-all routes for sections (Task 2)
- Image gallery with database backend
- History section with subsections (Task 3)
- Full navigation between sections (Task 4)
- Custom 404 page
- Admin panel for managing gallery & news
- Full-width presentation slides on "Notable People" page

