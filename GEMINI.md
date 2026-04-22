# SlimChoco - Landing Page de Chocolate Emagrecedor

## 1. Contexto e Propósito
O **SlimChoco** é uma landing page de alta conversão para um chocolate emagrecedor funcional. O projeto demonstra domínio em desenvolvimento web com **Django 5.x**, **Tailwind CSS**, e boas práticas de arquitetura e código Python.

- **Objetivo Principal:** Converter visitantes em compradores e capturar leads.
- **Público-Alvo:** Mulheres de 25-50 anos interessadas em emagrecimento saudável.
- **Interface:** 100% em português brasileiro (PT-BR).
- **Código:** 100% em inglês (variáveis, funções, classes, comentários).

---

## 2. Stack Tecnológica
- **Backend:** Python 3.12+ / Django 5.x
- **Frontend:** Django Template Language (DTL) + Tailwind CSS (via CDN)
- **Banco de Dados:** SQLite (padrão Django)
- **Servidor Dev:** `python manage.py runserver`

---

## 3. Padrões de Código e Convenções
### Python & Django
- **PEP 8:** Obrigatório em todos os arquivos `.py`.
- **Strings:** Usar aspas simples (`'`) em todo o código Python.
- **Naming:** Variáveis e funções em `snake_case`; classes em `PascalCase`.
- **Views:** Priorizar **Class-Based Views (CBVs)** (`TemplateView`, `CreateView`).
- **Forms:** Usar **Django Forms** para validação no servidor.
- **Segurança:** CSRF habilitado em todos os formulários.

### Frontend
- **Design System:** Baseado em Tailwind CSS com paleta de cores chocolate (#2C1A0E, #4A2C17) e dourado (#C9A227).
- **Responsividade:** Mobile-first, seguindo os breakpoints padrão do Tailwind (`sm`, `md`, `lg`).
- **Componentes:** Uso de elementos HTML nativos (ex: `<details>` para FAQ) para manter a simplicidade.

---

## 4. Estrutura do Projeto
```
slimchoco/
├── manage.py
├── requirements.txt
├── slimchoco/              # Configuração do projeto (settings, urls, wsgi)
└── landing/                # App principal
    ├── migrations/
    ├── templates/landing/  # base.html, index.html, thank_you.html
    ├── static/landing/     # imagens e assets
    ├── models.py           # Lead, Testimonial, FAQ
    ├── views.py            # LandingPageView, LeadCreateView, ThankYouView
    ├── forms.py            # LeadForm
    ├── urls.py
    └── admin.py            # Registro dos models no admin
```

---

## 5. Comandos Frequentes
- **Ambiente Virtual:** `source .venv/bin/activate` (Linux/Mac) ou `.venv\Scripts\activate` (Windows)
- **Migrations:** `python manage.py makemigrations` e `python manage.py migrate`
- **Servidor:** `python manage.py runserver`
- **Superusuário:** `python manage.py createsuperuser`
- **Dependências:** `pip freeze > requirements.txt`

---

## 6. Instruções para o Agente (GEMINI CLI)
- **Surgical Updates:** Sempre realize alterações mínimas e precisas, respeitando os padrões de código (aspas simples, inglês no código).
- **Validation:** Após qualquer alteração em models ou views, verifique se as migrations foram geradas/aplicadas e se o servidor sobe sem erros.
- **Templates:** Ao editar templates, certifique-se de manter a herança de `base.html` e o uso de classes Tailwind consistentes com o `docs/design-system.md`.
- **Testes:** Sempre que possível, verifique o fluxo de captura de lead e a renderização dinâmica de `Testimonial` e `FAQ`.

---
*GEMINI.md gerado em 22/04/2026 para o projeto SlimChoco.*
