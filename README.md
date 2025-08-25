# Mini CRM — Django Practice Project

A hands‑on Django learning project built in three stages (Junior → Middle → Advanced).  
Goal: practice real CRUD, forms/validation, auth, media, tests, aggregates, DRF, Celery, Channels, and Docker — step by step.

---

## 🚀 Quick Start

```bash
# Python 3.10+ recommended
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt  # (если есть)
# или минимально необходимое:
pip install django pillow pytest pytest-django djangorestframework django-debug-toolbar

# Инициализация БД
python manage.py migrate
python manage.py createsuperuser

# Запуск
python manage.py runserver
```

`/health/` should return `ok`.

---

## 📦 Tech Stack (planned)

- **Django** (Admin, Auth, ORM, Templates)
- **Pillow** (image handling for `ImageField`)
- **pytest + pytest-django** (tests)
- **DRF** (read‑only API)
- **django-debug-toolbar** (N+1 and query insights)
- **Celery + Redis** (async tasks, later)
- **Channels** (WebSockets, later)
- **Docker / docker-compose** (optional, stage 3)

---

## 🧭 Project Structure (suggested)

```
mini_crm/
├── manage.py
├── mini_crm/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── clients/
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── templates/
    │   └── clients/
    │       ├── client_list.html
    │       ├── client_form.html
    │       └── client_confirm_delete.html
    └── migrations/
```

---

## ✅ Deliverables

- A link to the repository and a short video / screenshots demonstrating functionality.
- **Junior**: ≥ 2 automated tests  
- **Middle**: ≥ 5 automated tests  
- **Advanced**: ≥ 8 automated tests

---

## 📋 Milestones & Tasks

### Stage 1 — Junior (Basics)

- [X] **0) Start**
  - [X] Create project `mini_crm` and app `clients`
  - [X] Add `/health/` → returns `ok`

- [x] **1) Client model**
  - [x] Fields: `name (required)`, `email (unique, lowercased)`, `phone (optional)`, `created_at (auto_now_add)`
  - [x] Admin: `list_display(name, email, created_at)`, search by `name, email`
  - [x] **Check:** created via admin; list sorted by date

- [x] **2) Client CRUD (FBV)**
  - [x] URLs: `/clients/`, `/clients/add/`, `/clients/<id>/edit/`, `/clients/<id>/edit/delete/`
  - [x] Templates in `templates/clients/`
  - [x] Use `messages` for success on save/delete
  - [x] **Check:** redirect to list after create; flash message visible

- [x] **3) Forms & validation**
  - [x] `ClientForm (ModelForm)` with `clean_email`: lowercase + forbid `example.com`
  - [x] Render field & form errors in templates
  - [x] **Check:** `USER@MAIL.COM` → `user@mail.com`; `@example.com` → validation error

- [ ] **4) Search & pagination**
  - [ ] `/clients/?q=...` filters by `name OR email__icontains`
  - [ ] Pagination: 10 per page
  - [ ] **Check:** different `q` changes list; next/prev links work

- [ ] **5) Authentication**
  - [ ] CRUD pages require login
  - [ ] Add `/accounts/login/`, `/accounts/logout/` (built‑in auth views), set `LOGIN_URL`
  - [ ] **Check:** guest → redirected to login

- [ ] **6) Avatar**
  - [ ] Field `avatar = ImageField(upload_to="avatars/", blank=True)`
  - [ ] Configure `MEDIA_URL/MEDIA_ROOT`, show avatar in client list (or fallback)
  - [ ] **Check:** upload works; files served from `MEDIA`

- [ ] **7) Tests (pytest-django)**
  - [ ] Model test: email is lowercased
  - [ ] View test: POST `/clients/add/` creates record & redirects
  - [ ] **Check:** `pytest` is green

---

### Stage 2 — Middle (More complex)

- [ ] **8) Order model**
  - [ ] Fields: `client (FK)`, `title`, `amount (Decimal)`, `status (NEW/IN_PROGRESS/DONE)`, `created_at`
  - [ ] Admin: inline orders on client page
  - [ ] **Check:** orders visible & editable inline

- [ ] **9) Client list with aggregates**
  - [ ] Add columns: “Total amount of orders” & “Number of orders”
  - [ ] Use `annotate(Sum, Count)` + `prefetch_related`
  - [ ] **Check:** correct numbers; no N+1 (debug-toolbar)

- [ ] **10) CBV refactor**
  - [ ] Rewrite Client CRUD using `ListView/CreateView/UpdateView/DeleteView`
  - [ ] Preserve flash messages
  - [ ] **Check:** behavior unchanged

- [ ] **11) Signals**
  - [ ] `post_save` for Client: if email domain is `company.com` → `vip=True` (add boolean)
  - [ ] **Check:** created client with that domain is auto‑VIP

- [ ] **12) Custom manager**
  - [ ] `Client.objects.active()` → clients with ≥1 unfinished order (`status != DONE`)
  - [ ] **Check:** returns correct set

- [ ] **13) CSV export**
  - [ ] `/clients/export.csv` → clients with order totals
  - [ ] Stream via `HttpResponse` (generator), proper headers
  - [ ] **Check:** opens in Excel/LibreOffice

- [ ] **14) API (DRF) — Read Only**
  - [ ] Endpoints: `/api/clients/`, `/api/clients/<id>/`, `/api/orders/`
  - [ ] Filters by `status`, search by `name/email`, pagination
  - [ ] **Check:** JSON OK; filters work

---

### Stage 3 — Advanced (Optional)

- [ ] **15) DRF permissions & throttling**
  - [ ] Read: everyone; Write: staff only
  - [ ] Throttle frequent requests (AnonRate/UserRate)
  - [ ] **Check:** POST by non‑staff is forbidden

- [ ] **16) Caching**
  - [ ] Cache `/clients/` for 60s (`cache_page`) + invalidate on client update
  - [ ] **Check:** list updates without long delay (consider invalidation)

- [ ] **17) Transactions**
  - [ ] “Merge clients” view: move all orders from Client‑B to Client‑A inside `transaction.atomic()` with locking
  - [ ] **Check:** on exception changes roll back

- [ ] **18) Async tasks**
  - [ ] Celery + Redis: monthly CSV order report to manager
  - [ ] **Check:** runs manually & via scheduler (beat)

- [ ] **19) WebSocket (Channels)**
  - [ ] On order create → push “new order” event to `/clients/` page
  - [ ] **Check:** two browsers receive real‑time update

- [ ] **20) Docker**
  - [ ] `docker-compose` with `web`, `postgres`, `redis`
  - [ ] **Check:** `docker compose up` runs the whole stack

---

## 🧪 Testing

```bash
pytest -q
```

Focus on:
- Stage 1: model lowercasing, create view redirect, permissions (login required)
- Stage 2+: aggregates correctness, API filters/pagination, CSV response headers
- Stage 3: permissions (staff‑only write), throttling, transactional merge, Celery tasks (can be unit‑tested with `CELERY_TASK_ALWAYS_EAGER=True`)

---

## 🖼 Media (avatars)

In `settings.py`:

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

In root `urls.py` (dev only):

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 📝 Conventions

- Keep views simple; prefer CBV where it improves clarity.
- Avoid N+1 queries; use `select_related` / `prefetch_related`.
- Commit messages: `feat:`, `fix:`, `test:`, `refactor:`, `docs:`.
- Don’t commit secrets or `.env` files.