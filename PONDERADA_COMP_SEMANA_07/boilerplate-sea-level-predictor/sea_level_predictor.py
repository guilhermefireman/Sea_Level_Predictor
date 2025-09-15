import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from pathlib import Path

def draw_plot():
    # Caminho robusto para o CSV (funciona rodando de qualquer pasta)
    data_path = Path(__file__).resolve().parent / "epa-sea-level.csv"
    df = pd.read_csv(data_path)

    # Figura e eixos
    fig, ax = plt.subplots(figsize=(10, 6))

    # Pontos (scatter)
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Linha de melhor ajuste (toda a série) 1880→2050
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_all = pd.Series(range(1880, 2051))
    ax.plot(years_all, res_all.slope * years_all + res_all.intercept, color="red")

    # Linha de melhor ajuste (desde 2000) 2000→2050
    df_2000 = df[df["Year"] >= 2000]
    res_2000 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    years_00 = pd.Series(range(2000, 2051))
    ax.plot(years_00, res_2000.slope * years_00 + res_2000.intercept, color="green")

    # Título e rótulos (exatamente como o FCC pede)
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")

    # Salvar a figura com o nome exigido
    fig.savefig("sea_level_plot.png")

    # ⚠️ Retorne o AXES (não a figure)
    return ax
