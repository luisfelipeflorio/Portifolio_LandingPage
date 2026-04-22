### Sprint 1 — Setup e Estrutura Base

#### Tarefa 1.1 — Configuração do Projeto Django
- [X] 1.1.1 Criar ambiente virtual Python (`python -m venv venv`)
- [X] 1.1.2 Instalar Django (`pip install django`)
- [X] 1.1.3 Criar projeto Django (`django-admin startproject slimchoco .`)
- [X] 1.1.4 Criar app `landing` (`python manage.py startapp landing`)
- [X] 1.1.5 Registrar app `landing` em `INSTALLED_APPS` no `settings.py`
- [X] 1.1.6 Configurar `LANGUAGE_CODE = 'pt-br'` e `TIME_ZONE = 'America/Sao_Paulo'` no `settings.py`
- [X] 1.1.7 Configurar diretório de templates em `settings.py` (`TEMPLATES[0]['DIRS']`)
- [X] 1.1.8 Configurar `STATICFILES_DIRS` e `STATIC_ROOT` no `settings.py`
- [X] 1.1.9 Gerar arquivo `requirements.txt`

#### Tarefa 1.2 — Estrutura de Arquivos e Templates Base
- [X] 1.2.1 Criar estrutura de pastas: `landing/templates/landing/`
- [X] 1.2.2 Criar `base.html` com blocos `{% block title %}`, `{% block content %}`, `{% block extra_js %}`
- [X] 1.2.3 Adicionar CDN do Tailwind CSS no `<head>` do `base.html`
- [X] 1.2.4 Adicionar meta tags de responsividade (`viewport`) no `base.html`
- [X] 1.2.5 Criar `index.html` extendendo `base.html`
- [X] 1.2.6 Criar `thank_you.html` extendendo `base.html`
- [X] 1.2.7 Copiar imagens do produto para `landing/static/landing/images/`

#### Tarefa 1.3 — Configuração de URLs
- [X] 1.3.1 Criar `landing/urls.py` com rota para a view da landing page (`/`)
- [X] 1.3.2 Criar rota para a página de agradecimento (`/obrigado/`)
- [X] 1.3.3 Incluir `landing.urls` no `slimchoco/urls.py` com `include()`
- [X] 1.3.4 Verificar que o servidor sobe sem erros (`python manage.py runserver`)

---

### Sprint 2 — Models, Forms e Views [X]

#### Tarefa 2.1 — Model `Lead`
- [X] 2.1.1 Criar model `Lead` em `landing/models.py` com campos: `name (CharField)`, `email (EmailField)`, `phone (CharField, blank=True)`, `created_at (auto_now_add)`, `updated_at (auto_now)`
- [X] 2.1.2 Gerar migration (`python manage.py makemigrations`)
- [X] 2.1.3 Aplicar migration (`python manage.py migrate`)
- [X] 2.1.4 Registrar `Lead` no `landing/admin.py` com `list_display = ['name', 'email', 'phone', 'created_at']`

#### Tarefa 2.2 — Model `Testimonial`
- [X] 2.2.1 Criar model `Testimonial` com campos: `author_name`, `author_city`, `content (TextField)`, `rating (IntegerField, 1–5)`, `is_active (BooleanField)`, `created_at`, `updated_at`
- [X] 2.2.2 Gerar e aplicar migration
- [X] 2.2.3 Registrar `Testimonial` no `admin.py` com `list_display` e `list_filter` por `is_active`
- [X] 2.2.4 Criar 3 depoimentos fictícios via Django Admin para teste

#### Tarefa 2.3 — Model `FAQ`
- [X] 2.3.1 Criar model `FAQ` com campos: `question (CharField)`, `answer (TextField)`, `order (IntegerField)`, `is_active (BooleanField)`, `created_at`, `updated_at`
- [X] 2.3.2 Adicionar `class Meta` com `ordering = ['order']`
- [X] 2.3.3 Gerar e aplicar migration
- [X] 2.3.4 Registrar `FAQ` no `admin.py`
- [X] 2.3.5 Criar 5 perguntas fictícias via Django Admin para teste

#### Tarefa 2.4 — Formulário de Lead
- [X] 2.4.1 Criar `landing/forms.py` com classe `LeadForm(forms.ModelForm)` baseada no model `Lead`
- [X] 2.4.2 Definir `fields = ['name', 'email', 'phone']` no `Meta` da `LeadForm`
- [X] 2.4.3 Adicionar `widgets` para cada campo com classes Tailwind CSS no `__init__` ou diretamente no `widgets` do `Meta`
- [X] 2.4.4 Adicionar validação customizada do e-mail para evitar duplicatas (método `clean_email`)

#### Tarefa 2.5 — Views
- [X] 2.5.1 Criar `LandingPageView(TemplateView)` em `landing/views.py` que passa para o contexto: `testimonials` (ativos), `faqs` (ativos), `form` (instância de `LeadForm`)
- [X] 2.5.2 Criar `LeadCreateView(CreateView)` que processa o POST do formulário, salva o lead e redireciona para `thank_you`
- [X] 2.5.3 Definir `success_url` na `LeadCreateView` apontando para a URL `thank_you`
- [X] 2.5.4 Criar `ThankYouView(TemplateView)` para a página de confirmação
- [X] 2.5.5 Mapear as três views em `landing/urls.py`

---

### Sprint 3 — Desenvolvimento do Template (Seções da Página)

#### Tarefa 3.1 — Navbar
- [ ] 3.1.1 Implementar navbar fixa no topo com logo "SlimChoco" em texto dourado
- [ ] 3.1.2 Adicionar botão CTA na navbar ("Quero agora") visível apenas em desktop
- [ ] 3.1.3 Aplicar efeito `backdrop-blur` e fundo semi-transparente na navbar
- [ ] 3.1.4 Garantir que o navbar tem z-index alto o suficiente para ficar acima de todos os elementos

#### Tarefa 3.2 — Hero Section
- [ ] 3.2.1 Criar seção hero com gradiente de fundo escuro (`from-[#2C1A0E] via-[#4A2C17] to-[#2C1A0E]`)
- [ ] 3.2.2 Adicionar badge "NOVO!" com estilo dourado no topo da seção
- [ ] 3.2.3 Implementar headline principal ("Menos medidas. Mais autoestima.") em tipografia grande e bold
- [ ] 3.2.4 Adicionar subheadline com slogan em itálico dourado
- [ ] 3.2.5 Inserir imagem do produto com `{% static %}` e estilo responsivo
- [ ] 3.2.6 Adicionar botão CTA primário com gradiente dourado e efeito hover
- [ ] 3.2.7 Incluir lista de checkmarks ("Para todas as dietas", "Prático e delicioso", "Resultados de verdade")
- [ ] 3.2.8 Garantir layout responsivo: empilhado no mobile, lado a lado no desktop (`md:flex-row`)

#### Tarefa 3.3 — Seção de Benefícios
- [ ] 3.3.1 Criar grid de 4 cards de benefício (2×2 mobile, 4×1 desktop)
- [ ] 3.3.2 Implementar card "Acelera o Metabolismo" com ícone de chama e descrição
- [ ] 3.3.3 Implementar card "Controle do Apetite" com ícone de folha e descrição
- [ ] 3.3.4 Implementar card "Saúde Intestinal" com ícone de intestino e descrição
- [ ] 3.3.5 Implementar card "Sem Açúcar" com ícone de açúcar cortado e descrição
- [ ] 3.3.6 Adicionar borda e hover suave dourado nos cards
- [ ] 3.3.7 Aplicar fundo alternado bege/creme na seção para contraste com o hero

#### Tarefa 3.4 — Seção "Como Funciona"
- [ ] 3.4.1 Criar seção com fundo escuro e título centralizado
- [ ] 3.4.2 Implementar timeline ou steps horizontais com 3 passos numerados
- [ ] 3.4.3 Passo 1: "Consuma 1 tablete ao dia" com ícone e descrição
- [ ] 3.4.4 Passo 2: "Os ingredientes agem no seu metabolismo" com ícone e descrição
- [ ] 3.4.5 Passo 3: "Veja os resultados em semanas" com ícone e descrição
- [ ] 3.4.6 Adicionar linha conectora entre os steps (visível apenas no desktop)

#### Tarefa 3.5 — Seção de Depoimentos
- [ ] 3.5.1 Criar seção com fundo creme/areia e título centralizado
- [ ] 3.5.2 Iterar sobre `testimonials` do contexto com `{% for testimonial in testimonials %}`
- [ ] 3.5.3 Renderizar cada card de depoimento com: nome, cidade, estrelas (rating) e texto
- [ ] 3.5.4 Implementar estrelas com loop `{% for i in "12345" %}` condicionando cor pelo rating
- [ ] 3.5.5 Aplicar grid 1 coluna no mobile, 3 colunas no desktop

#### Tarefa 3.6 — Seção FAQ
- [ ] 3.6.1 Criar seção com fundo escuro e título centralizado
- [ ] 3.6.2 Iterar sobre `faqs` do contexto com `{% for faq in faqs %}`
- [ ] 3.6.3 Renderizar cada item do FAQ como acordeão com `<details>` e `<summary>` HTML nativo
- [ ] 3.6.4 Estilizar `<summary>` com cursor pointer, ícone de seta e hover dourado
- [ ] 3.6.5 Garantir que o conteúdo expandido tem padding e separador suave

#### Tarefa 3.7 — Seção do Formulário de Lead
- [ ] 3.7.1 Criar seção with gradiente dourado-para-escuro de fundo
- [ ] 3.7.2 Adicionar título de urgência/oferta acima do formulário
- [ ] 3.7.3 Renderizar `{{ form.name }}`, `{{ form.email }}`, `{{ form.phone }}` com labels
- [ ] 3.7.4 Renderizar erros do formulário com `{{ form.field.errors }}` em estilo vermelho inline
- [ ] 3.7.5 Adicionar token CSRF `{% csrf_token %}` no formulário
- [ ] 3.7.6 Configurar `action` do form apontando para a URL da `LeadCreateView`
- [ ] 3.7.7 Adicionar botão de envio com estilo dark e hover

#### Tarefa 3.8 — Seção de Oferta/Preço
- [ ] 3.8.1 Criar seção com destaque para o preço e condições
- [ ] 3.8.2 Adicionar preço riscado (de) e preço promocional (por) com tipografia grande
- [ ] 3.8.3 Adicionar botão CTA de compra with link externo (configurável)
- [ ] 3.8.4 Adicionar selos de garantia/confiança (pagamento seguro, entrega garantida)

#### Tarefa 3.9 — Footer
- [ ] 3.9.1 Criar footer com fundo `#2C1A0E` e texto `#D2B48C`
- [ ] 3.9.2 Adicionar copyright e nome do produto
- [ ] 3.9.3 Adicionar texto de disclaimer ("Resultados podem variar. Consulte um médico...")
- [ ] 3.9.4 Adicionar links básicos (Política de Privacidade placeholder)

#### Tarefa 3.10 — Página de Agradecimento
- [ ] 3.10.1 Criar `thank_you.html` com mensagem de confirmação de lead registrado
- [ ] 3.10.2 Adicionar ícone de check e headline de agradecimento em dourado
- [ ] 3.10.3 Adicionar botão de voltar para a página inicial
- [ ] 3.10.4 Manter estilo visual consistente com a landing page

---

### Sprint 4 — Refinamento e Ajustes

#### Tarefa 4.1 — Responsividade e Cross-browser
- [ ] 4.1.1 Testar e ajustar layout em viewport 320px (mobile pequeno)
- [ ] 4.1.2 Testar e ajustar layout em viewport 768px (tablet)
- [ ] 4.1.3 Testar e ajustar layout em viewport 1280px (desktop)
- [ ] 4.1.4 Corrigir espaçamentos e tamanhos de fonte em cada breakpoint

#### Tarefa 4.2 — Polimento Visual
- [ ] 4.2.1 Revisar consistência de cores e gradientes em todas as seções
- [ ] 4.2.2 Adicionar transições `transition-all duration-300` nos elementos interativos
- [ ] 4.2.3 Verificar contraste de texto para acessibilidade básica
- [ ] 4.2.4 Ajustar espaçamentos entre seções para ritmo visual adequado

#### Tarefa 4.3 — Admin e Dados Iniciais
- [ ] 4.3.1 Criar superusuário Django (`python manage.py createsuperuser`)
- [ ] 4.3.2 Verificar que todos os models aparecem corretamente no admin
- [ ] 4.3.3 Popular banco com dados de exemplo via Django Admin
- [ ] 4.3.4 Testar fluxo completo de submissão de lead e visualização no admin

#### Tarefa 4.4 — Revisão de Código
- [ ] 4.4.1 Verificar conformidade com PEP 8 em todos os arquivos `.py`
- [ ] 4.4.2 Garantir uso de aspas simples em todo o código Python
- [ ] 4.4.3 Confirmar que todo código (variáveis, funções, classes) está em inglês
- [ ] 4.4.4 Confirmar que toda interface com o usuário está em português brasileiro
- [ ] 4.4.5 Remover imports não utilizados e código comentado

---

### Sprint 5 — Entregas Futuras (Backlog)

> Estas tarefas ficam para fases posteriores do projeto:

- [ ] 5.1 Configurar Tailwind CSS via CLI (substituir CDN)
- [ ] 5.2 Implementar Docker e docker-compose
- [ ] 5.3 Escrever testes unitários e de integração
- [ ] 5.4 Configurar deploy em servidor (ex: Railway, Heroku, VPS)
- [ ] 5.5 Integrar com serviço de e-mail para notificar leads
- [ ] 5.6 Adicionar Google Analytics ou equivalente
- [ ] 5.7 Implementar rate limiting no formulário de lead

---
