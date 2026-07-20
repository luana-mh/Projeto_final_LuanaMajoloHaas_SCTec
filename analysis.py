"""
Projeto: Visualização de Dados e Business Intelligence
Análise Exploratória de Dados (EDA) - Base HR (FreeSQL)

Este script:
1. Lê os arquivos query_01.csv e query_02.csv (gerados no FreeSQL)
2. Calcula estatísticas descritivas básicas (média, mediana, mínimo, máximo)
3. Gera um Histograma (distribuição de salários)
4. Gera um Boxplot (salário por departamento)

Requisitos:
    pip install pandas matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------------------------
# 1. Carregar os dados exportados do FreeSQL
# -----------------------------------------------------------
df_q1 = pd.read_csv("query_01.csv")  # Salário por Departamento e Cargo
df_q2 = pd.read_csv("query_02.csv")  # Funcionários por Região

print("Query 1 - primeiras linhas:")
print(df_q1.head())

print("\nQuery 2 - primeiras linhas:")
print(df_q2.head())

# -----------------------------------------------------------
# 2. Estatísticas descritivas básicas do salário (Query 1)
# -----------------------------------------------------------
media = df_q1["SALARY"].mean()
mediana = df_q1["SALARY"].median()
minimo = df_q1["SALARY"].min()
maximo = df_q1["SALARY"].max()

print("\n--- Estatísticas descritivas do SALARY (Query 1) ---")
print(f"Média:   {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Mínimo:  {minimo:.2f}")
print(f"Máximo:  {maximo:.2f}")

# Média salarial por departamento (apoia a leitura do boxplot)
media_por_departamento = (
    df_q1.groupby("DEPARTMENT_NAME")["SALARY"].mean().sort_values(ascending=False)
)
print("\nMédia salarial por departamento:")
print(media_por_departamento)

# -----------------------------------------------------------
# 3. Histograma - distribuição geral dos salários
# -----------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5))
contagem, faixas, barras = ax.hist(
    df_q1["SALARY"].dropna(), bins=15, color="#4C72B0", edgecolor="black"
)
 
# Escreve o valor de cada barra em cima dela
ax.bar_label(barras, fmt="%.0f", padding=3)
 
ax.set_title("Distribuição de Salários - Query 1")
ax.set_xlabel("Salário")
ax.set_ylabel("Número de Funcionários")
 
# Mostra os limites de cada faixa no eixo X para facilitar a leitura
ax.set_xticks(faixas)
ax.tick_params(axis="x", rotation=45)
 
plt.tight_layout()
plt.savefig("histograma_salarios.png")
plt.close()

# -----------------------------------------------------------
# 4. Boxplot - salário por departamento
# -----------------------------------------------------------
# Dicionário de tradução (apenas para exibição no gráfico -
# os dados originais do DataFrame continuam em inglês, como
# vieram do banco).
traducao_departamentos = {
    "Administration": "Administração",
    "Marketing": "Marketing",
    "Purchasing": "Compras",
    "Human Resources": "Recursos Humanos",
    "Shipping": "Logística",
    "IT": "TI",
    "Public Relations": "Relações Públicas",
    "Sales": "Vendas",
    "Executive": "Diretoria",
    "Finance": "Financeiro",
    "Accounting": "Contabilidade",
}
 
# Usa a mesma ordem de "media_por_departamento" (já calculada na seção 2,
# do maior para o menor salário médio) para que o boxplot fique ordenado.
ordem_departamentos = media_por_departamento.index.tolist()
 
dados_boxplot = [
    df_q1.loc[df_q1["DEPARTMENT_NAME"] == dep, "SALARY"].dropna()
    for dep in ordem_departamentos
]
 
# Rótulo de cada departamento em português + quantidade de funcionários (n=)
rotulos_boxplot = [
    f"{traducao_departamentos.get(dep, dep)}\n(n={len(dados)})"
    for dep, dados in zip(ordem_departamentos, dados_boxplot)
]
 
fig, ax = plt.subplots(figsize=(13, 7))
ax.boxplot(dados_boxplot, tick_labels=rotulos_boxplot)
 
# Escreve média, mediana e máximo em cima de cada caixa
for posicao, dados in enumerate(dados_boxplot, start=1):
    texto = (
        f"média={dados.mean():.0f}\n"
        f"mediana={dados.median():.0f}\n"
        f"máx={dados.max():.0f}"
    )
    ax.text(
        posicao,
        dados.max() + df_q1["SALARY"].max() * 0.03,
        texto,
        ha="center",
        va="bottom",
        fontsize=7,
    )
 
ax.set_title("Salário por Departamento - Query 1 (ordenado pela média)")
ax.set_xlabel("Departamento")
ax.set_ylabel("Salário")
ax.tick_params(axis="x", rotation=45)
 
# Espaço extra no topo para caber o texto das anotações
ax.set_ylim(top=df_q1["SALARY"].max() * 1.30)
 
plt.tight_layout()
plt.savefig("boxplot_salario_departamento.png")
plt.close()
 
print("\nGráficos salvos: histograma_salarios.png e boxplot_salario_departamento.png")

# -----------------------------------------------------------
# 5. Visão geral da Query 2 - distribuição geográfica
# -----------------------------------------------------------
funcionarios_por_regiao = df_q2.groupby("REGION_NAME")["EMPLOYEE_ID"].count()
print("\nQuantidade de funcionários por região (Query 2):")
print(funcionarios_por_regiao)