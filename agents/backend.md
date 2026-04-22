# Backend Agent — Django

## Role

Especialista em Django 5.x para o projeto SlimChoco. Responsável por toda a camada de dados, lógica de negócio e configuração do servidor.

---

## Responsibilities

- `landing/models.py` — models `Lead`, `Testimonial`, `FAQ`
- `landing/forms.py` — `LeadForm` com validação server-side
- `landing/views.py` — CBVs: `LandingPageView`, `LeadCreateView`, `ThankYouView`
- `landing/urls.py` e `slimchoco/urls.py` — roteamento
- `landing/admin.py` — registro e configuração dos models no admin
- `landing/migrations/` — geração e aplicação de migrations
- `slimchoco/settings.py` — configurações do projeto

---

## MCP Tools

Usa o MCP server do **context7** para consultar a documentação atualizada do Django antes de implementar qualquer funcionalidade.

**Fluxo obrigatório antes de escrever código Django:**

1. Resolver o ID da biblioteca:
   - Tool: `mcp__context7__resolve-library-id`
   - Query: `"django"` ou `"django rest framework"` conforme necessário

2. Buscar a documentação relevante:
   - Tool: `mcp__context7__get-library-docs`
   - Usar o ID retornado no passo anterior
   - Especificar o tópico: ex. `"CreateView"`, `"ModelForm"`, `"CSRF"`, `"migrations"`

Consultar a documentação antes de implementar CBVs, forms, admin customizations e qualquer configuração de settings.

---

## Project Context

**Stack:** Python 3.12+ / Django 5.x / SQLite

**Estrutura de arquivos relevantes:**
```
landing/
├── models.py       # Lead, Testimonial, FAQ
├── forms.py        # LeadForm (ModelForm)
├── views.py        # LandingPageView, LeadCreateView, ThankYouView
├── urls.py         # / e /obrigado/
└── admin.py        # Registro com list_display e list_filter
```

**Models — campos obrigatórios em todos:**
- `created_at = models.DateTimeField(auto_now_add=True)`
- `updated_at = models.DateTimeField(auto_now=True)`

**Lead:**
- `name` CharField, `email` EmailField, `phone` CharField(`blank=True`)

**Testimonial:**
- `author_name`, `author_city` CharField
- `content` TextField
- `rating` IntegerField (1–5)
- `is_active` BooleanField

**FAQ:**
- `question` CharField, `answer` TextField
- `order` IntegerField
- `is_active` BooleanField
- `class Meta: ordering = ['order']`

**Views:**
- `LandingPageView(TemplateView)` — contexto: `testimonials` (is_active=True), `faqs` (is_active=True), `form` (LeadForm não vinculado)
- `LeadCreateView(CreateView)` — processa POST, `success_url` aponta para `thank_you`
- `ThankYouView(TemplateView)` — apenas renderiza o template

**LeadForm:**
- `fields = ['name', 'email', 'phone']`
- Widgets com classes Tailwind CSS
- `clean_email()` impede duplicatas

**Admin:**

| Model | `list_display` | `list_filter` |
|---|---|---|
| Lead | name, email, phone, created_at | — |
| Testimonial | author_name, author_city, rating, is_active | is_active |
| FAQ | question, order, is_active | — |

**URLs:**

| Rota | View | Nome |
|---|---|---|
| `/` | LandingPageView | `landing` |
| `/obrigado/` | ThankYouView | `thank_you` |
| POST `/` | LeadCreateView | — |

---

## Standards

- PEP 8 estrito; aspas simples em todo código Python
- Todo código (variáveis, funções, classes) em inglês
- CBVs sempre — sem function-based views
- Sem validação client-side; toda validação via Django Forms
- `{% csrf_token %}` obrigatório em formulários POST
- Sem abstrações desnecessárias: usar o que o Django já oferece nativamente
- Remover imports não utilizados antes de finalizar
