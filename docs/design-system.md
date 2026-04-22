# Design System

Tailwind CSS via CDN. Todas as cores são aplicadas com valores inline (`text-[#hex]`, `bg-[#hex]`) — não há arquivo de configuração customizado.

---

## Paleta de Cores

| Nome | Hex | Uso |
|---|---|---|
| Chocolate Escuro | `#2C1A0E` | Fundo hero, navbar, footer |
| Chocolate Médio | `#4A2C17` | Cards, seções alternadas |
| Dourado | `#C9A227` | CTAs, destaques, bordas, badges |
| Dourado Claro | `#E8C84A` | Hover, ícones |
| Bege Areia | `#D2B48C` | Fundo de seções claras |
| Creme | `#F5EDD6` | Fundo alternado |
| Branco | `#FFFFFF` | Texto principal em fundo escuro |
| Cinza Escuro | `#1A1A1A` | Texto em fundo claro |

---

## Gradientes

```html
<!-- Hero -->
<div class="bg-gradient-to-br from-[#2C1A0E] via-[#4A2C17] to-[#2C1A0E]">

<!-- CTA / botão primário -->
<div class="bg-gradient-to-r from-[#C9A227] to-[#E8C84A]">

<!-- Seções claras -->
<div class="bg-gradient-to-b from-[#F5EDD6] to-[#D2B48C]">
```

---

## Tipografia

| Papel | Classes Tailwind |
|---|---|
| Título principal | `font-bold text-4xl md:text-6xl` |
| Subtítulo | `font-semibold text-xl md:text-2xl` |
| Corpo | `text-base leading-relaxed` |
| Slogan / destaque | `font-bold italic text-[#C9A227]` |

---

## Botões

### CTA Primário (dourado)

```html
<button class="bg-gradient-to-r from-[#C9A227] to-[#E8C84A] text-[#2C1A0E]
               font-bold py-4 px-8 rounded-full text-lg uppercase tracking-wider
               hover:shadow-lg hover:scale-105 transition-all duration-300">
  Quero meu SlimChoco
</button>
```

### CTA Secundário (outline)

```html
<button class="border-2 border-[#C9A227] text-[#C9A227]
               font-semibold py-3 px-6 rounded-full
               hover:bg-[#C9A227] hover:text-[#2C1A0E]
               transition-all duration-300">
  Saiba mais
</button>
```

---

## Formulário

### Input

```html
<input type="text"
  class="w-full bg-white/10 border border-[#C9A227]/40 rounded-lg
         px-4 py-3 text-white placeholder-white/50
         focus:outline-none focus:border-[#C9A227] focus:ring-1 focus:ring-[#C9A227]
         transition-all duration-200">
```

### Label

```html
<label class="block text-white/80 text-sm font-medium mb-1">
```

### Erro inline

Erros do Django Forms exibidos com texto vermelho abaixo do campo (`{{ form.field.errors }}`).

---

## Cards de Benefício

```html
<div class="bg-white/5 border border-[#C9A227]/20 rounded-2xl p-6 text-center
            hover:border-[#C9A227]/60 hover:bg-white/10
            transition-all duration-300">
  <!-- ícone + título + descrição -->
</div>
```

---

## Navbar

```html
<nav class="fixed top-0 w-full bg-[#2C1A0E]/95 backdrop-blur-sm z-50
            border-b border-[#C9A227]/20">
  <div class="max-w-6xl mx-auto px-4 py-3 flex justify-between items-center">
    <!-- Logo + CTA (CTA visível apenas no desktop) -->
  </div>
</nav>
```

---

## Grid e Container

```html
<!-- Container principal -->
<div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">

<!-- Grid de benefícios -->
<div class="grid grid-cols-2 md:grid-cols-4 gap-6">

<!-- Grid de depoimentos -->
<div class="grid grid-cols-1 md:grid-cols-3 gap-8">
```

---

## FAQ — Acordeão

Usa elementos HTML nativos `<details>` e `<summary>`, sem JavaScript.

```html
<details class="border-b border-[#C9A227]/20">
  <summary class="cursor-pointer py-4 font-semibold text-white hover:text-[#C9A227]
                  transition-colors duration-200">
    Pergunta aqui
  </summary>
  <p class="pb-4 text-white/70 leading-relaxed">Resposta aqui</p>
</details>
```

---

## Breakpoints

Seguem os breakpoints padrão do Tailwind CSS:

| Prefixo | Largura mínima |
|---|---|
| *(sem prefixo)* | 0px (mobile-first) |
| `sm:` | 640px |
| `md:` | 768px |
| `lg:` | 1024px |

Layout empilhado no mobile; lado a lado a partir de `md:`.
