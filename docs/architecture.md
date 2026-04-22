# Arquitetura

## Stack

| Camada | Tecnologia |
|---|---|
| Backend | Python 3.12+ / Django 5.x |
| Templates | Django Template Language (DTL) |
| Estilização | Tailwind CSS via CDN |
| Banco de dados | SQLite (padrão Django) |
| Servidor dev | `python manage.py runserver` |

---

## Estrutura de Pastas

```
slimchoco/
├── manage.py
├── requirements.txt
├── slimchoco/                  # Configuração do projeto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── landing/                    # App principal
│   ├── migrations/
│   ├── templates/landing/
│   │   ├── base.html
│   │   ├── index.html
│   │   └── thank_you.html
│   ├── static/landing/images/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
└── static/                     # Arquivos estáticos globais
```

---

## Models

Todos os models ficam em `landing/models.py`. Todos possuem `created_at (auto_now_add)` e `updated_at (auto_now)`.

### Lead

Registra cada lead capturado pelo formulário.

| Campo | Tipo | Observação |
|---|---|---|
| `name` | CharField | Obrigatório |
| `email` | EmailField | Obrigatório |
| `phone` | CharField | `blank=True` |
| `created_at` | DateTimeField | `auto_now_add=True` |
| `updated_at` | DateTimeField | `auto_now=True` |

### Testimonial

Depoimentos exibidos na landing page. Apenas os com `is_active=True` são exibidos.

| Campo | Tipo | Observação |
|---|---|---|
| `author_name` | CharField | |
| `author_city` | CharField | |
| `content` | TextField | |
| `rating` | IntegerField | Valores de 1 a 5 |
| `is_active` | BooleanField | Filtro de exibição |
| `created_at` | DateTimeField | `auto_now_add=True` |
| `updated_at` | DateTimeField | `auto_now=True` |

### FAQ

Perguntas frequentes com ordenação manual. Apenas os com `is_active=True` são exibidos.

| Campo | Tipo | Observação |
|---|---|---|
| `question` | CharField | |
| `answer` | TextField | |
| `order` | IntegerField | Define a ordem de exibição |
| `is_active` | BooleanField | Filtro de exibição |
| `created_at` | DateTimeField | `auto_now_add=True` |
| `updated_at` | DateTimeField | `auto_now=True` |

`class Meta`: `ordering = ['order']`

---

## Views

Todas as views ficam em `landing/views.py` e usam Class-Based Views (CBVs).

| View | Tipo | Responsabilidade |
|---|---|---|
| `LandingPageView` | `TemplateView` | Renderiza `index.html` com `testimonials`, `faqs` e `form` no contexto |
| `LeadCreateView` | `CreateView` | Processa o POST do formulário; salva o lead; redireciona para `thank_you` |
| `ThankYouView` | `TemplateView` | Renderiza `thank_you.html` após envio bem-sucedido do formulário |

---

## Forms

`LeadForm` em `landing/forms.py` — `forms.ModelForm` baseado no model `Lead`.

- Fields: `name`, `email`, `phone`
- Widgets com classes Tailwind CSS aplicadas via `Meta.widgets`
- Validação customizada: `clean_email()` evita cadastro de e-mail duplicado

---

## URLs

### `landing/urls.py`

| Rota | View | Nome |
|---|---|---|
| `/` | `LandingPageView` | `landing` |
| `/obrigado/` | `ThankYouView` | `thank_you` |
| POST para `/` | `LeadCreateView` | — |

### `slimchoco/urls.py`

```python
path('', include('landing.urls'))
```

---

## Seções da Landing Page

Ordem de exibição em `index.html`:

1. Navbar (fixa, `z-50`)
2. Hero Section
3. Benefícios (4 cards)
4. Como Funciona (3 passos)
5. Depoimentos
6. FAQ (acordeão com `<details>/<summary>`)
7. Formulário de Lead
8. Oferta / Preço
9. Footer

---

## Admin

Todos os models são registrados em `landing/admin.py`.

| Model | `list_display` | `list_filter` |
|---|---|---|
| `Lead` | `name`, `email`, `phone`, `created_at` | — |
| `Testimonial` | `author_name`, `author_city`, `rating`, `is_active` | `is_active` |
| `FAQ` | `question`, `order`, `is_active` | — |
