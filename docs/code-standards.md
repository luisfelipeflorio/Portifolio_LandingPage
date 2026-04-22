# Padrões de Código

---

## Python

- **PEP 8** estrito em todos os arquivos `.py`
- **Aspas simples** em todas as strings Python
- **Código em inglês**: variáveis, funções, classes e comentários
- **Interface em português brasileiro**: todo texto visível ao usuário nos templates

```python
# Correto
class LeadForm(forms.ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        ...

# Errado — aspas duplas e nome em português
class FormularioLead(forms.ModelForm):
    def limpar_email(self):
        email = self.cleaned_data["email"]
        ...
```

---

## Django

- **Class-Based Views (CBVs)** sempre que aplicável (`TemplateView`, `CreateView`)
- **Django Forms** para toda validação — sem validação apenas no cliente
- **CSRF** habilitado em todos os formulários (`{% csrf_token %}`)
- **`auto_now_add` e `auto_now`** nos campos de data de todos os models
- Sem over-engineering: use os recursos nativos do Django antes de criar abstrações

---

## Templates (DTL)

- Todos os templates herdam de `base.html` via `{% extends 'landing/base.html' %}`
- Blocos definidos em `base.html`: `{% block title %}`, `{% block content %}`, `{% block extra_js %}`
- `{% static %}` para todos os assets estáticos
- `{% csrf_token %}` em todo `<form>` com método POST

---

## Settings

Configurações obrigatórias no `settings.py`:

```python
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
```

---

## Admin

- Todos os models do app `landing` devem ser registrados em `landing/admin.py`
- Usar `list_display` para facilitar a visualização dos dados
- Usar `list_filter` onde houver campo booleano (`is_active`)

---

## O que evitar

- Imports não utilizados
- Código comentado
- Abstrações sem uso imediato
- Validação duplicada (servidor + cliente) para campos simples
- Signals desnecessários para fluxos que podem ser tratados diretamente na view
