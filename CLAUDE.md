# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Status

The Django project has not been scaffolded yet. The planning phase is complete — `PRD.md`, `TASKS.md`, and `docs/` define the full spec. Sprint 1 of `TASKS.md` is the next step.

---

## Commands

All commands run from the project root with the virtual environment activated (`.venv`).

```bash
# Activate venv (Windows)
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Bootstrap the project (Sprint 1 — run once)
django-admin startproject slimchoco .
python manage.py startapp landing

# Development server
python manage.py runserver

# Database migrations (after any model change)
python manage.py makemigrations
python manage.py migrate

# Create admin superuser
python manage.py createsuperuser

# Freeze dependencies
pip freeze > requirements.txt
```

No test runner or linter is configured yet. PEP 8 compliance is enforced manually (see code standards below).

---

## Architecture

Single Django app (`landing`) inside the `slimchoco` project. There is no second app and no shared app — everything lives in `landing/`.

**Request flow:**
- `GET /` → `LandingPageView` renders `index.html` with `testimonials`, `faqs`, and an unbound `LeadForm` in context
- `POST /` → `LeadCreateView` validates and saves the lead, then redirects to `/obrigado/`
- `GET /obrigado/` → `ThankYouView` renders `thank_you.html`

**Three models** in `landing/models.py`:
- `Lead` — form submissions (name, email, phone optional)
- `Testimonial` — filtered by `is_active=True` before passing to context
- `FAQ` — filtered by `is_active=True`, ordered by `order` field (`Meta.ordering = ['order']`)

**Templates** extend `base.html`, which holds the Tailwind CDN `<script>` tag and defines three blocks: `title`, `content`, `extra_js`. No JS framework — the FAQ accordion uses native `<details>/<summary>`.

**Admin** (`landing/admin.py`) is the only management interface for leads, testimonials, and FAQs. All three models must be registered.

---

## Code Standards

- **PEP 8** strict; **single quotes** for all Python strings
- **Code in English** (variables, functions, classes); **UI in Portuguese (PT-BR)** (all template text)
- **CBVs always** — no function-based views
- **No client-side validation** — Django Forms handles all validation server-side
- **No abstractions without immediate use** — follow the existing flat structure

---

## Design

Tailwind CSS via CDN — no build step, no `tailwind.config.js`. All colors are applied as inline arbitrary values (`text-[#C9A227]`, `bg-[#2C1A0E]`). Full color palette, gradients, button patterns, and component classes are in `docs/design-system.md`.

---

## Reference

- Full product spec → `PRD.md`
- Task breakdown by sprint → `TASKS.md`
- Architecture details → `docs/architecture.md`
- Design tokens and component patterns → `docs/design-system.md`
- Coding rules → `docs/code-standards.md`
