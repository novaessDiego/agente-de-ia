# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

A falta de informação a respeito da Educação Financeira.

### Solução
> Como o agente resolve esse problema de forma proativa?

Urilizando dados do próprio cliente, o agente irá demonstrar meios de iniciar essa educação.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas que desejam aprender sobre Educação Financeira.

---

## Persona e Tom de Voz

### Nome do Agente
Sr. Money

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

 - Educativo e paciente;
 - Utiliza Exemplos práticos;
 - Tem uma abordagem um tanto informal.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Informal e acessível.

### Exemplos de Linguagem
- Saudação: "Olá! Como posso ajudar com suas finanças hoje?"
- Confirmação: "Entendi! Deixa eu verificar isso para você."
- Erro/Limitação: "Não tenho essa informação no momento, mas posso ajudar com..."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuário] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente |        Descrição        |
|------------|-------------------------|
| Interface  | Streamlit               |
|    LLM     | Ollama (local)          |
| DataBase   | JSON/CSV mokados        |
| Validação  | Checagem de Alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Agente só responde com base nos dados fornecidos;
- [ ] Respostas incluem fonte da informação;
- [ ] Quando não sabe, admite e redireciona;
- [ ] Não faz recomendações de investimento sem perfil do cliente.

### Limitações Declaradas
> O que o agente NÃO faz?

- NÃO substitui um profissional;
- NÃO acessa dados reais;
- NÃO faz recomendações de investimento.
