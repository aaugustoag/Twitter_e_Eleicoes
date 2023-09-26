import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
plt.rcParams['figure.figsize'] = [15, 5]
pd.set_option('display.max_columns', None)

def visual_plots(df, hue):
    x = mdates.date2num(df.data_pesquisa)
    ax = sns.scatterplot(x=df.data_pesquisa,
                         y=df.percentual,
                         hue=df[hue],
                         data=df,
                         s=40)

    # set plot limits
    ax.set(xlim=(min(x)-10, max(x)+10),
           ylim=(0, 60))
    # move legend outside graph
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2)

# carrega csv e filtra valores de interesse
df_pesquisas = pd.read_csv("dados-eleicao-pocket-completa.csv", sep=';', parse_dates=["data_pesquisa"])
validos_uf = ["BRASIL"]
validos_tipo = ["Espontanea", "Estimulada"] #"Espontanea",
validos_cargo = ["Presidente"]
df_pesquisas = df_pesquisas[df_pesquisas.tipo.isin(validos_tipo) & df_pesquisas.cargo.isin(validos_cargo) & df_pesquisas.unidade_federativa_nome.isin(validos_uf)]

df_alvo = df_pesquisas[['pesquisa_id', 'data_pesquisa', 'percentual', 'instituto', 'voto_tipo', 'tipo']]
df_alvo = df_alvo[df_alvo.voto_tipo == "Votos Totais"]
df_alvo = df_alvo[df_alvo.tipo == "Estimulada"]
df_alvo.drop(columns=["voto_tipo", "tipo"], inplace=True)

# agrupamos dados e calculamos media dos cenarios eleitorais
df_plot = df_alvo.groupby(["data_pesquisa", "instituto"], sort=False).mean()
df_plot.reset_index(level=["instituto"], inplace=True)

# descobrimos quantas pesquisas cada instituto realizou
valid_data = df_plot.groupby('instituto').nunique().sort_values("pesquisa_id", ascending=False).drop(columns=['instituto', 'percentual'])

# baseado nos graficos, decidimos usar os institutos com pelo menos 8 pesquisas feitas
institutos = valid_data.index
institutos8 = valid_data[valid_data.pesquisa_id > 7].index

