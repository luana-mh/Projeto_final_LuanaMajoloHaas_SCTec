# Visualização de Dados e Business Intelligence - Base HR

**Aluno(a):** Luana Majolo Haas
**Turma:** QAVDBI1

## Objetivo do Trabalho

Analisar dados de Recursos Humanos (esquema HR do FreeSQL) para entender a distribuição de salários por departamento e cargo, e a distribuição
geográfica dos funcionários por cidade, estado, país e região.

## Tabelas Utilizadas

- **EMPLOYEES**: dados dos funcionários (nome, salário, cargo, departamento).
- **DEPARTMENTS**: departamentos da empresa e sua localização.
- **JOBS**: cargos e faixas salariais associadas.
- **LOCATIONS**: endereço físico de cada departamento.
- **COUNTRIES**: países associados às localizações.
- **REGIONS**: regiões geográficas que agrupam os países.

## Resumo das Consultas SQL

### Query 1 — Salário por Departamento e Cargo

Relaciona `EMPLOYEES` com `DEPARTMENTS` e `JOBS` usando `LEFT JOIN`, filtrando funcionários com `SALARY > 3000`.

Objetivo: entender como o salário varia entre departamentos e cargos.

### Query 2 — Funcionários por Região

Relaciona `EMPLOYEES` com `DEPARTMENTS`, `LOCATIONS`, `COUNTRIES` e `REGIONS` usando `LEFT JOIN`, filtrando registros

com `REGION_NAME IS NOT NULL`.
Objetivo: entender a distribuição geográfica dos funcionários.

Os códigos completos estão em [`queries.sql`](./queries.sql).

## Análise em Python

O script [`analysis.py`](./analysis.py) lê os arquivos `query_01.csv` e `query_02.csv`, calcula estatísticas descritivas (média, mediana, mínimo e
máximo do salário) e gera dois gráficos:

- Histograma da distribuição de salários.
- Boxplot de salário por departamento.

## Principais Resultados

### Estatísticas descritivas (Query 1 — Salário)

| Medida  | Valor     |
| ------- | --------- |
| Média  | 7.696,49  |
| Mediana | 7.500,00  |
| Mínimo | 3.100,00  |
| Máximo | 24.000,00 |

A média e a mediana são próximas, mas o valor máximo (24.000) está muito acima das duas — sinal de que a distribuição é assimétrica à direita, puxada por poucos salários bem altos. Isso é confirmado pelo histograma: 53 dos 81 funcionários (65%) ganham entre 3.100 e 8.673, enquanto apenas 1 funcionário ganha próximo do valor máximo (22.607–24.000).

### Salário médio por departamento

| Departamento          | Salário Médio |
| --------------------- | --------------- |
| Diretoria (Executive) | 19.333,33       |
| Contabilidade         | 10.154,00       |
| Relações Públicas  | 10.000,00       |
| Marketing             | 9.500,00        |
| Vendas                | 8.955,88        |
| Financeiro            | 8.601,33        |
| Compras               | 7.050,00        |
| Recursos Humanos      | 6.500,00        |
| TI                    | 5.760,00        |
| Administração       | 4.400,00        |
| Logística            | 4.313,04        |

A **Diretoria** tem, de longe, o maior salário médio (quase o dobro do segundo colocado, Contabilidade), o que explica por que sua caixa aparece
isolada no topo do boxplot. Já **Logística** e **Administração** têm as médias mais baixas, com salários bastante concentrados (caixas estreitas no
boxplot), além de outliers identificados em **Logística**. O **Marketing** apresenta alta dispersão salarial, enquanto que a área de **Recursos Humanos** praticamente não possui variação. Ainda, o setor **Financeiro** possui um funcionário com salário significativamente superior aos demais.

O boxplot também mostra **outliers** (pontos fora da caixa) nos departamentos de **Logística** e **TI** — funcionários que recebem valores
bem diferentes da maioria dos colegas do mesmo setor, o que pode indicar cargos de nível sênior dentro de equipes majoritariamente juniores, ou
exceções na política salarial.

### Distribuição geográfica (Query 2 — Região)

| Região  | Funcionários |
| -------- | ------------- |
| Americas | 70            |
| Europe   | 36            |

A grande maioria dos funcionários está concentrada na região **Americas **(cerca de 66% do total), o que é coerente com a sede da empresa em Seattle, identificada nos registros da Diretoria e de TI.

## Como Executar o Projeto

1. Rodar as consultas em `queries.sql` no FreeSQL (esquema HR) e exportar os resultados como `query_01.csv` e `query_02.csv`.
2. Colocar os dois CSVs na mesma pasta de `analysis.py`.
3. Instalar as dependências:
   ```bash
   pip install pandas matplotlib
   ```
4. Executar o script:
   ```bash
   python analysis.py
   ```
5. Os gráficos serão salvos como `histograma_salarios.png` e
   `boxplot_salario_departamento.png`.

## Sugestões de Melhoria para Futuras Versões

* **Salário x tempo de casa** : cruzar `EMPLOYEES` com `JOB_HISTORY` (`START_DATE` e `END_DATE`) para calcular o tempo de casa/no cargo de cada
  funcionário e verificar se existe relação entre tempo de empresa e salário — por exemplo, se funcionários mais antigos tendem a ganhar mais
  dentro do mesmo departamento.
* **Análise de comissões (`COMMISSION_PCT`)** : identificar quais cargos recebem comissão (majoritariamente ligados a vendas) e quais os
  percentuais praticados, calculando também a remuneração total estimada (salário-base + comissão) para comparar com cargos sem comissão.
* **Dashboard interativo** : transformar as análises estáticas (histograma e boxplot) em um dashboard interativo (ex: Power BI, Tableau), permitindo filtrar por departamento, região ou cargo em tempo real.
