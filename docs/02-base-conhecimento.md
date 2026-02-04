# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

---

## Estratégia de Integração

### Como os dados são carregados?
Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt.
É possível carregar os arquivos via código ou simplesmente utilizar Ctrl + C e Ctrl + V

```python
import pandas as pd
import json

#CSVs
historico = pd.read_csv('data/histórico_atendimento.csv')
transacoes = pd.read_csv('data/trancasoces.csv')

#JSONs
with open('data/perfil_investidor.json', 'r', encoding='utf-8') as f:
  perfil = json.load(f)


with open('data/produtos_financeiros.json', 'r', encoding='utf-8') as f:
  perfil = json.load(f)

```

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
