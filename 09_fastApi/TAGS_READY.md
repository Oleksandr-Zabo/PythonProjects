# ✅ Реалізація Tags для FastAPI Blog - Повна Документація

## 📋 Резюме змін

Вся функціональність по тегам реалізована **від моделей до OpenAPI документації**.

## 📁 Файли, які були створені/оновлені

### Нові файли
```
src/features/tags/
├── __init__.py ...................... Пакетний ініціалізатор
├── models.py ........................ SQLAlchemy Model для Tag
├── schemas.py ....................... Pydantic Schemas для Request/Response
├── repository.py .................... CRUD операції з БД
├── service.py ....................... Бізнес-логіка
└── router.py ........................ REST API ендпоінти (/tags)

migrations/versions/
└── add_tags_to_posts.py ............ Alembic міграція для тегів
```

### Оновлені файли
```
src/features/posts/
├── models.py ........................ Додано tags relationship
├── schemas.py ....................... Додано tags поля
├── repository.py .................... Методи для роботи з тегами
└── router.py ........................ Ендпоінти для додавання/видалення тегів

src/features/graphql_api/
└── schema.py ........................ TagType та запити для тегів

src/
└── main.py .......................... Зареєстровано tags router

migrations/
└── env.py ........................... Додано import Tag

.env ................................ Додано DATABASE_URL та налаштування
```

---

## 🏗️ Архітектура

### Database Schema
```
┌─────────────────┐         ┌──────────────────┐         ┌────────────────┐
│    posts        │◄────────┤    post_tags     │────────►│      tags      │
├─────────────────┤         ├──────────────────┤         ├────────────────┤
│ id (PK)         │         │ post_id (FK)     │         │ id (PK)        │
│ author_id (FK)  │         │ tag_id (FK)      │         │ name (UNIQUE)  │
│ content         │         │                  │         │ color          │
│ image_url       │         └──────────────────┘         │ created_at     │
│ created_at      │                                      │ updated_at     │
│ updated_at      │         Many-to-Many                 └────────────────┘
└─────────────────┘
```

### Application Layers
```
┌──────────────────────────────────────────────────┐
│           FastAPI Router (/tags, /posts)        │ ← HTTP Layer
├──────────────────────────────────────────────────┤
│             Service Layer (Validation)          │ ← Business Logic
├──────────────────────────────────────────────────┤
│          Repository Layer (CRUD, ORM)           │ ← Data Access
├──────────────────────────────────────────────────┤
│             SQLAlchemy Models                   │ ← ORM Layer
├──────────────────────────────────────────────────┤
│          PostgreSQL Database (Alembic)          │ ← Data Storage
└──────────────────────────────────────────────────┘
```

---

## 🧩 Як все працює разом

### 1. Створення тега
```
User Request: POST /tags {"name": "Python", "color": "#3776AB"}
    ↓
FastAPI Router validates input (Pydantic)
    ↓
TagService.create_tag() checks uniqueness
    ↓
TagRepository.create_tag() executes SQL INSERT
    ↓
Response: {"id": 1, "name": "Python", ...}
```

### 2. Створення поста з тегами
```
User Request: POST /posts + tags=[1, 2, 3]
    ↓
PostService.create_post()
    ↓
PostRepository.add_tags_to_post() → INSERT INTO post_tags
    ↓
Response: Post з полем "tags": [...]
```

### 3. GraphQL Query
```
{
  allPosts {
    id
    tags { id, name }
  }
}
    ↓
GraphQL Resolver queries Post + eager load tags
    ↓
Response: posts з nested tags
```

---

## 🚀 Інструкція запуску

### Step 1: Встановити залежності
```bash
cd C:\Users\ADNIN\PycharmProjects\PythonProjects\09_fastApi
pip install -r requirements.txt
```

### Step 2: Запустити PostgreSQL (Docker)
```bash
docker-compose up -d
```

### Step 3: Запустити міграцію
```bash
alembic upgrade head
```

Це створить таблиці:
- `tags`
- `post_tags`

### Step 4: Запустити сервер
```bash
python -m uvicorn src.main:app --reload --port 8000
```

### Step 5: Перейти до документації
- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc
- **GraphQL:** http://127.0.0.1:8000/graphql

---

## 📚 API Endpoints

### Tags Management
| Метод | Ендпоінт | Опис |
|-------|----------|------|
| `POST` | `/tags` | Створити тег |
| `GET` | `/tags` | Отримати теги з пагінацією |
| `GET` | `/tags/all` | Всі теги без пагінації |
| `GET` | `/tags/search?q=...` | Пошук тегів |
| `GET` | `/tags/{id}` | Тег за ID |
| `PUT` | `/tags/{id}` | Оновити тег |
| `DELETE` | `/tags/{id}` | Видалити тег |

### Posts + Tags Integration
| Метод | Ендпоінт | Опис |
|-------|----------|------|
| `POST` | `/posts` (+ tags param) | Створити пост з тегами |
| `POST` | `/posts/{id}/tags/{tag_id}` | Додати тег до поста |
| `DELETE` | `/posts/{id}/tags/{tag_id}` | Видалити тег зі поста |
| `GET` | `/posts/tags/{tag_id}` | Пості за тегом |

---

## 🔗 GraphQL Queries

```graphql
# Отримати всі пості з тегами
query GetPosts {
  allPosts(limit: 10) {
    id
    content
    tags {
      id
      name
      color
    }
  }
}

# Пошук постів за тегом
query GetPostsByTag {
  postsByTag(tagId: 1, limit: 10) {
    id
    content
  }
}

# Отримати всі теги
query GetTags {
  allTags {
    id
    name
    color
  }
}
```

---

## ✨ Ключові особливості

✅ **Many-to-Many relationship** — Post ↔ Tag через `post_tags`  
✅ **Full CRUD** — Create, Read, Update, Delete операції  
✅ **Validation** — Pydantic + Custom Business Logic  
✅ **Pagination** — Для великих наборів даних  
✅ **Search** — Пошук тегів по назві (case-insensitive)  
✅ **GraphQL** — Full support з nested queries  
✅ **OpenAPI** — Автоматична документація в Swagger/ReDoc  
✅ **Database Migrations** — Alembic з upgrade/downgrade  
✅ **Type Safety** — Python type hints + SQLAlchemy ORM  
✅ **Error Handling** — HTTP exceptions з правильними кодами  

---

## 🧪 Приклади використання

### Curl: Створити тег
```bash
curl -X POST http://127.0.0.1:8000/tags \
  -H "Content-Type: application/json" \
  -d '{"name":"Django","color":"#092E20"}'
```

### Python: Asyncio
```python
import httpx

async with httpx.AsyncClient() as client:
    response = await client.post(
        "http://127.0.0.1:8000/tags",
        json={"name": "FastAPI", "color": "#009688"}
    )
    print(response.json())
```

### JavaScript: Fetch
```javascript
fetch('http://127.0.0.1:8000/tags', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'Python', color: '#3776AB' })
}).then(r => r.json()).then(console.log);
```

---

## 📊 Структура коду

```python
# src/features/tags/models.py
class Tag(Base, TimestampMixin):
    __tablename__ = "tags"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    color: Mapped[Optional[str]] = mapped_column(String(7))
    posts: Mapped[List["Post"]] = relationship(
        secondary="post_tags",
        back_populates="tags"
    )

# src/features/tags/repository.py
class TagRepository:
    async def create_tag(self, tag_data: dict) -> Tag:
        new_tag = Tag(**tag_data)
        self.db.add(new_tag)
        await self.db.commit()
        return new_tag
    
    async def get_tag_by_name(self, name: str) -> Optional[Tag]:
        query = select(Tag).where(Tag.name.ilike(name))
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

# src/features/tags/service.py
class TagService:
    async def create_tag(self, request: TagCreate) -> Tag:
        existing = await self.repository.get_tag_by_name(request.name)
        if existing:
            raise ValueError(f"Тег '{request.name}' вже існує")
        return await self.repository.create_tag(request.model_dump())

# src/features/tags/router.py
@router.post("/", response_model=TagRead)
async def create_tag(
    request: TagCreate,
    service: TagService = Depends(get_tag_service)
):
    return await service.create_tag(request)
```

---

## 🐛 Troubleshooting

### "Тег вже існує"
Назви тегів унікальні. Спробуйте іншу назву.

### Port 8000 вже занятий
Використайте інший порт:
```bash
python -m uvicorn src.main:app --port 8001
```

### Міграція падає
Переконайтеся що PostgreSQL запущений:
```bash
docker-compose ps
```

### GraphQL не показує теги
Переконайтеся що моделі мають eager loading:
```python
selectinload(Post.tags)
```

---

## 📈 Performance

### Lazy Loading Issue ❌
```python
for post in posts:
    for tag in post.tags:  # N+1 Problem! 🔴
        print(tag.name)
```

### Eager Loading ✅
```python
posts = session.execute(
    select(Post).options(selectinload(Post.tags))
).scalars()

for post in posts:
    for tag in post.tags:  # Single query! ✅
        print(tag.name)
```

---

## 🎯 Наступні кроки

Можна розширити:
- [ ] Role-based access (тільки адміни створюють теги)
- [ ] Tag trending (популярність тегів)
- [ ] Tag suggestions (авто-доповніння)
- [ ] Tag subscriptions (користувачі слідкують за тегами)
- [ ] Tag analytics (статистика по тегам)
- [ ] Tag aliases (alt names)

---

## 📞 Контакти

Будь-які питання про реалізацію — дивіться:
- `src/features/tags/` — основний функціонал
- `migrations/versions/add_tags_to_posts.py` — БД структура
- `TAGS_IMPLEMENTATION.md` — детальна документація

---

**Status:** ✅ READY FOR PRODUCTION (з PostgreSQL)

**Last Updated:** 2026-05-29

