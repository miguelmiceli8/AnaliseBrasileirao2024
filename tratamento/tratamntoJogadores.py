# %% 
import pandas as pd 

# %%
dfjogadores = pd.read_csv("../data_base_jogadores/database.csv", sep=",") 
dfjogadores.head() #lendo os dados 
# %% 
dfjogadores.info() #contem dados nulos
# %%
dfjogadores.dropna()#dropando nulas 
# %%
metricas = dfjogadores.groupby(
    ["Jogador"], as_index=False
).agg(
    gols_totais = ("Gols", "sum"),
    ass_totais = ("Assis.", "sum"),
    xG_totais = ("xG", "sum"),
    npxG_totais = ("npxG", "sum"),
    xAG_totais = ("xAG", "sum"),
    SCA_totais = ("SCA", "sum"),
    GCA_totais = ("GCA", "sum"),
    PrgP_totais = ("PrgP", "sum"),
    PrgC_totais = ("PrgC", "sum"),
    conducoes_totais = ("Conduções", "sum"),
    tent_drible_totais = ("Tent", "sum"),
    suc_drible_totais = ("Suc", "sum"),
    bloqueios_totais = ("Bloqueios", "sum"),
    amarelos_totais = ("CrtsA", "sum"),
    vermelhos_totais = ("CrtV", "sum"),
    minutos_totais = ("Min.", "sum")
)
# %%
#gols / 90 
metricas["G/90"] = metricas["gols_totais"] / metricas["minutos_totais"] * 90
# %% 
#ass / 90
metricas["A/90"] = metricas["ass_totais"] / metricas["minutos_totais"] * 90 

# %%
#xG / 90
metricas["xG/90"] = metricas["xG_totais"] / metricas["minutos_totais"] * 90 

# %%
#npxG / 90
metricas["npxG/90"] = metricas["npxG_totais"] / metricas["minutos_totais"] * 90

# %%
#xAG / 90
metricas["xAG/90"] = metricas["xAG_totais"] / metricas["minutos_totais"] * 90

# %%
#SCA / 90
metricas["SCA/90"] = metricas["SCA_totais"] / metricas["minutos_totais"] * 90

# %%
#GCA / 90
metricas["GCA/90"] = metricas["GCA_totais"] / metricas["minutos_totais"] * 90

# %%
#PrgP / 90
metricas["PrgP/90"] = metricas["PrgP_totais"] / metricas["minutos_totais"] * 90

# %%
#PrgC / 90
metricas["PrgC/90"] = metricas["PrgC_totais"] / metricas["minutos_totais"] * 90

# %%
#conduções / 90
metricas["Conducoes/90"] = metricas["conducoes_totais"] / metricas["minutos_totais"] * 90

# %%
#tentativas de drible / 90
metricas["Tent/90"] = metricas["tent_drible_totais"] / metricas["minutos_totais"] * 90

# %%
#dribles certos / 90
metricas["Suc/90"] = metricas["suc_drible_totais"] / metricas["minutos_totais"] * 90

# %%
#bloqueios / 90
metricas["Bloq/90"] = metricas["bloqueios_totais"] / metricas["minutos_totais"] * 90

# %%
#cartões amarelos / 90
metricas["Am/90"] = metricas["amarelos_totais"] / metricas["minutos_totais"] * 90

# %%
#cartões vermelhos / 90
metricas["Vm/90"] = metricas["vermelhos_totais"] / metricas["minutos_totais"] * 90 
# %%
#participações em gol totais
metricas["G+A"] = metricas["gols_totais"] + metricas["ass_totais"]

# %%
#participações em gol / 90
metricas["G+A/90"] = metricas["G+A"] / metricas["minutos_totais"] * 90

# %%
#performece de finalização
metricas["G-xG"] = metricas["gols_totais"] - metricas["xG_totais"]

# %%
#contribuição ofensiva esperada
metricas["xG+xAG"] = metricas["xG_totais"] + metricas["xAG_totais"]

# %%
#contribuição esperada / 90
metricas["xG+xAG/90"] = metricas["xG+xAG"] / metricas["minutos_totais"] * 90

# %%
# taxa sucesso no drible
metricas["Drible%"] = metricas["suc_drible_totais"] / metricas["tent_drible_totais"]
# %% 
#ordenando por maior numero de gols
metricas = metricas.sort_values(by="gols_totais", ascending=False)
# %%
metricas.head(10)
# %%
metricas.columns
# %%
metricas.to_csv("metricas.csv", sep=";", index=False)
# %%
