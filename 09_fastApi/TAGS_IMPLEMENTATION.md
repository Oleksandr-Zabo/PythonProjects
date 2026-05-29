# Tags Feature для FastAPI Blog 🏷️

## 📋 Що було реалізовано

Додана повна функціональність для роботи з тегами (мітками) у системі блогу:

### 1. **Backend Changes**

#### Моделі (SQLAlchemy)
- ✅ `src/features/tags/models.py` — модель `Tag` з полями:
  - `id` (int) — унікальний ідентифікатор
  - `name` (str) — назва тега (унікальна, 1-50 символів)
  - `color` (str, optional) — HEX колір (наприклад, #FF5733)
  - `created_at`, `updated_at` — часові мітки
  - Зв'язок Many-to-Many з `Post` через асоціативну таблицю `post_tags`

#### Міграції Alembic
- ✅ `migrations/versions/add_tags_to_posts.py` — міграція для:
  - Створення таблиці `tags`
  - Створення асоціативної таблиці `post_tags`
  - Індексів для оптимізації запитів

#### Pydantic Схеми
- ✅ `src/features/tags/schemas.py`:
  - `TagCreate` — для створення тега
  - `TagUpdate` — для оновлення тега
  - `TagRead` — для читання тега
  - `TagWithPostsCount` — тег з кількістю постів

#### Repository Pattern
- ✅ `src/features/tags/repository.py` — CRUD операції:
  - `create_tag()` — створити тег
  - `get_tags()` — отримати теги з пагінацією
  - `get_tag_by_id()` — отримати тег за ID
  - `get_tag_by_name()` — отримати тег за назвою
  - `update_tag()` — оновити тег
  - `delete_tag()` — видалити тег
  - `search_tags()` — пошук тегів

#### Service Layer
- ✅ `src/features/tags/service.py` — бізнес-логіка:
  - Валідація унікальності назв
  - Обробка помилок
  - Трансформація даних

#### REST API Router
- ✅ `src/features/tags/router.py` — ендпоінти:
  - `POST /tags` — створити тег
  - `GET /tags` — отримати теги з пагінацією
  - `GET /tags/search/?q=...` — пошук тегів
  - `GET /tags/all/` — всі теги без пагінації
  - `GET /tags/{tag_id}` — тег за ID
  - `PUT /tags/{tag_id}` — оновити тег
  - `DELETE /tags/{tag_id}` — видалити тег

#### Post Integration
- ✅ Оновлено `src/features/posts/models.py`:
  - Додано relationship `tags` до моделі `Post`
  - Асоціативна таблиця `post_tags`

- ✅ Оновлено `src/features/posts/schemas.py`:
  - `PostCreate` приймає список ID тегів
  - `PostRead` містить список тегів

- ✅ Оновлено `src/features/posts/repository.py`:
  - `add_tags_to_post()` — додати теги до поста
  - `remove_tag_from_post()` — видалити тег зі поста
  - `get_posts_by_tag()` — пости за тегом
  - Оновити всі GET методи для завантаження тегів через `selectinload`

- ✅ Оновлено `src/features/posts/router.py`:
  - `POST /posts/{post_id}/tags/{tag_id}` — додати тег до поста
  - `DELETE /posts/{post_id}/tags/{tag_id}` — видалити тег зі поста
  - `GET /posts/tags/{tag_id}` — пості з тегом

### 2. **GraphQL Support**
- ✅ Оновлено `src/features/graphql_api/schema.py`:
  - Додано `TagType` — GraphQL тип для тега
  - Оновлено `PostType` — включено поле `tags`
  - Додано query `posts_by_tag()` — пості за тегом
  - Додано query `all_tags()` — всі теги

### 3. **Main Application**
- ✅ Оновлено `src/main.py`:
  - Зареєстровано `tags_router` з префіксом `/tags`

---

## 🚀 Як запустити

### Установка залежностей
```bash
cd 09_fastApi
pip install -r requirements.txt
```

### Запуск PostgreSQL (Docker)
```bash
docker-compose up -d
```

### Запуск міграцій
```bash
alembic upgrade head
```

### Запуск FastAPI сервера
```bash
python -m uvicorn src.main:app --reload --host 127.0.0.1 --port 8000
```

---

## 📚 API Документація

### Tags CRUD

#### 1. Створити тег
```bash
curl -X POST http://127.0.0.1:8000/tags \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Python",
    "color": "#3776AB"
  }'
```

**Response:**
```json
{
  "id": 1,
  "name": "Python",
  "color": "#3776AB",
  "created_at": "2026-05-29T21:50:00",
  "updated_at": "2026-05-29T21:50:00"
}
```

#### 2. Отримати всі теги
```bash
curl http://127.0.0.1:8000/tags?page=1&size=10
```

#### 3. Пошук тегів
```bash
curl "http://127.0.0.1:8000/tags/search/?q=pyth"
```

#### 4. Отримати тег за ID
```bash
curl http://127.0.0.1:8000/tags/1
```

#### 5. Оновити тег
```bash
curl -X PUT http://127.0.0.1:8000/tags/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Python 3.11",
    "color": "#FFD43B"
  }'
```

#### 6. Видалити тег
```bash
curl -X DELETE http://127.0.0.1:8000/tags/1
```

### Posts + Tags

#### 1. Створити пост з тегами
```bash
curl -X POST http://127.0.0.1:8000/posts \
  -H "Authorization: Bearer <token>" \
  -F "content=Гарячий пост" \
  -F "tags=[1, 2, 3]"
```

#### 2. Додати тег до поста
```bash
curl -X POST http://127.0.0.1:8000/posts/1/tags/1 \
  -H "Authorization: Bearer <token>"
```

#### 3. Видалити тег зі поста
```bash
curl -X DELETE http://127.0.0.1:8000/posts/1/tags/1 \
  -H "Authorization: Bearer <token>"
```

#### 4. Отримати пості за тегом
```bash
curl http://127.0.0.1:8000/posts/tags/1?page=1&size=10
```

---

## 🔗 GraphQL Queries

### Отримати всі пості з тегами
```graphql
query {
  allPosts(limit: 10) {
    id
    content
    author {
      id
      email
    }
    tags {
      id
      name
      color
    }
    comments {
      id
      content
    }
  }
}
```

### Отримати пості за тегом
```graphql
query {
  postsByTag(tagId: 1, limit: 10) {
    id
    content
    tags {
      id
      name
    }
  }
}
```

### Отримати всі теги
```graphql
query {
  allTags {
    id
    name
    color
    createdAt
  }
}
```

---

## 📊 Структура БД

### Таблиця `tags`
```sql
CREATE TABLE tags (
  id INTEGER PRIMARY KEY,
  name VARCHAR(50) UNIQUE NOT NULL,
  color VARCHAR(7),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

### Таблиця `post_tags` (Many-to-Many)
```sql
CREATE TABLE post_tags (
  post_id INTEGER FOREIGN KEY REFERENCES posts(id) ON DELETE CASCADE,
  tag_id INTEGER FOREIGN KEY REFERENCES tags(id) ON DELETE CASCADE,
  PRIMARY KEY (post_id, tag_id)
);
```

---

## 🔑 Key Features

✅ **Унікальні теги** — немає дублювання  
✅ **Кольорові теги** — опціональна персоналізація  
✅ **Пошук тегів** — по назві (case-insensitive)  
✅ **Пагінація** — для великих списків  
✅ **GraphQL support** — повна інтеграція  
✅ **OpenAPI docs** — автоматична документація  
✅ **TypeScript-like типізація** — через Pydantic  
✅ **ACID транзакції** — через SQLAlchemy + PostgreSQL  

---

## 🧪 Тестування

### Создать логічну послідовність:
1. Створити користувача (via `/auth/register`)
2. Авторизуватися (via `/auth/login`)
3. Створити теги (via `POST /tags`)
4. Створити пост з тегами (via `POST /posts`)
5. Переглянути пости за тегом (via `GET /posts/tags/{tag_id}`)

---

## 📖 Посилання

- **OpenAPI Docs:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc
- **GraphQL Playground:** http://127.0.0.1:8000/graphql
- **PgAdmin:** http://localhost:5050

---

## ✨ Що далі?

Можна додати:
- [ ] Популярні теги (top tags by posts count)
- [ ] Теги трендів (trending tags)
- [ ] Темні теги (shadow tags for admins)
- [ ] Tag subscriptions (users following tags)
- [ ] Tag analytics (views, posts count per tag)

