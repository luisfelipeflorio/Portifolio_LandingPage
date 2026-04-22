# Agentes de IA — SlimChoco

Índice dos agentes disponíveis para o projeto. Cada agente é especialista em uma camada da stack e deve ser invocado para tarefas dentro do seu domínio.

---

## Agentes

| Agente | Arquivo | Domínio |
|---|---|---|
| Backend | [backend.md](backend.md) | Django: models, views, forms, admin, URLs, migrations |
| Frontend | [frontend.md](frontend.md) | Django Templates (DTL) + Tailwind CSS |
| QA | [qa.md](qa.md) | Testes funcionais e visuais com Playwright |

---

## Quando usar cada agente

### Backend — `backend.md`

Use para qualquer tarefa que envolva código Python ou configuração do Django:

- Criar ou alterar models (`Lead`, `Testimonial`, `FAQ`)
- Implementar ou corrigir views CBVs
- Configurar formulários e validações (`LeadForm`, `clean_email`)
- Definir ou atualizar rotas de URL
- Configurar o admin do Django
- Gerar e aplicar migrations
- Ajustar `settings.py`

Usa o MCP **context7** para consultar a documentação do Django antes de implementar.

---

### Frontend — `frontend.md`

Use para qualquer tarefa que envolva HTML, CSS ou a camada de apresentação:

- Criar ou editar templates (`base.html`, `index.html`, `thank_you.html`)
- Implementar ou ajustar seções da landing page (hero, benefícios, FAQ, formulário, etc.)
- Aplicar ou corrigir estilos Tailwind CSS
- Garantir responsividade nos breakpoints definidos
- Renderizar dados do contexto Django nos templates (`{{ testimonials }}`, `{{ faqs }}`, `{{ form }}`)
- Corrigir desvios visuais em relação ao design system

Usa o MCP **context7** para consultar a documentação do Tailwind CSS e das tags DTL antes de implementar.

---

### QA — `qa.md`

Use para validar que o sistema funciona e está visualmente correto:

- Verificar o fluxo completo de captura de lead
- Testar validação e exibição de erros no formulário
- Confirmar responsividade nos três breakpoints (320px, 768px, 1280px)
- Validar o acordeão de FAQ
- Checar fidelidade visual ao design system (cores, gradientes, tipografia)
- Testar após qualquer alteração de backend ou frontend para detectar regressões

Usa o MCP **Playwright** para controlar o navegador e interagir com a aplicação em execução.

---

## Fluxo recomendado

```
Backend → Frontend → QA
```

1. **Backend** implementa models, views e forms
2. **Frontend** constrói os templates e aplica o design
3. **QA** valida o resultado no navegador com o servidor rodando

Para correções pontuais, invocar diretamente o agente do domínio afetado.
