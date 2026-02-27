# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%
df = pd.read_csv("metricas.csv", sep=";")
df.head(10)

# %%
#conv de chances criadas
df["G_xG_ratio"] = df["gols_totais"] / df["xG_totais"].replace(0, np.nan)

#eficiencia criativa
df["A_xAG_ratio"] = df["ass_totais"] / df["xAG_totais"].replace(0, np.nan)

#cartões totais
df["cartoes_totais"] = df["amarelos_totais"] + df["vermelhos_totais"]

# %%
#conv de chances
df_conv = df[df["xG_totais"] >= 2]

top = df_conv.sort_values("G_xG_ratio", ascending=False).head(10)

plt.figure()
plt.barh(top["Jogador"], top["G_xG_ratio"])
plt.title("Top 10 conversão de chances (Gols/xG)")
plt.xlabel("Gols/xG")
plt.gca().invert_yaxis()
plt.show()

# %%
#vermelhos
top = df.sort_values("vermelhos_totais", ascending=False).head(10)

plt.figure()
plt.barh(top["Jogador"], top["vermelhos_totais"])
plt.title("Top 10 cartões vermelhos")
plt.xlabel("Vermelhos")
plt.gca().invert_yaxis()
plt.show()

# %%
#gols por 90
df_rank = df[df["minutos_totais"] >= 900]

top = df_rank.sort_values("G/90", ascending=False).head(10)

plt.figure()
plt.barh(top["Jogador"], top["G/90"])
plt.title("Top 10 Gols por 90")
plt.xlabel("G/90")
plt.gca().invert_yaxis()
plt.show()

# %%
#participações por 90
top = df_rank.sort_values("G+A/90", ascending=False).head(10)

plt.figure()
plt.barh(top["Jogador"], top["G+A/90"])
plt.title("Top 10 Participações por 90")
plt.xlabel("G+A/90")
plt.gca().invert_yaxis()
plt.show()

# %%
#xAG por 90 
top = df_rank.sort_values("xAG/90", ascending=False).head(10)

plt.figure()
plt.barh(top["Jogador"], top["xAG/90"])
plt.title("Top 10 xAG por 90 (criação esperada)")
plt.xlabel("xAG/90")
plt.gca().invert_yaxis()
plt.show()
# %%
#SCA por 90
top = df_rank.sort_values("SCA/90", ascending=False).head(10)

plt.figure()
plt.barh(top["Jogador"], top["SCA/90"])
plt.title("Top 10 SCA por 90 (ações que geram finalizações)")
plt.xlabel("SCA/90")
plt.gca().invert_yaxis()
plt.show()
# %%
#GCA por 90
top = df_rank.sort_values("GCA/90", ascending=False).head(10)

plt.figure()
plt.barh(top["Jogador"], top["GCA/90"])
plt.title("Top 10 GCA por 90 (ações que geram gols)")
plt.xlabel("GCA/90")
plt.gca().invert_yaxis()
plt.show()
# %%
#(xG+xAG/90)
top = df_rank.sort_values("xG+xAG/90", ascending=False).head(10)

plt.figure()
plt.barh(top["Jogador"], top["xG+xAG/90"])
plt.title("Top 10 xG+xAG por 90 (contribuição ofensiva esperada)")
plt.xlabel("xG+xAG/90")
plt.gca().invert_yaxis()
plt.show()

# %%
#Gols - xG 
top = df_rank.sort_values("G-xG", ascending=False).head(10)

plt.figure()
plt.barh(top["Jogador"], top["G-xG"])
plt.title("Top 10 Overperformance (Gols - xG)")
plt.xlabel("Gols - xG")
plt.gca().invert_yaxis()
plt.show()

# %%
#ef criativa 
df_cre = df_rank[df_rank["xAG_totais"] >= 2].copy()
top = df_cre.sort_values("A_xAG_ratio", ascending=False).head(10)

plt.figure()
plt.barh(top["Jogador"], top["A_xAG_ratio"])
plt.title("Top 10 Eficiência criativa (Assistências / xAG) | xAG>=2")
plt.xlabel("Assis/xAG")
plt.gca().invert_yaxis()
plt.show()

# %%
#dribles por 90 
top = df_rank.sort_values("Suc/90", ascending=False).head(10)

plt.figure()
plt.barh(top["Jogador"], top["Suc/90"])
plt.title("Top 10 Dribles certos por 90")
plt.xlabel("Suc/90")
plt.gca().invert_yaxis()
plt.show()
# %%
#taxa de dribles filtrado por tentativas 
df_dr = df_rank[df_rank["tent_drible_totais"] >= 20].copy()
top = df_dr.sort_values("Drible%", ascending=False).head(10)

plt.figure()
plt.barh(top["Jogador"], top["Drible%"])
plt.title("Top 10 Taxa de drible (Suc/Tent) | Tent>=20")
plt.xlabel("Drible%")
plt.gca().invert_yaxis()
plt.show()
# %%
#xAG/90 vs A/90  (linha y=x)
plt.figure()
plt.scatter(df_rank["xAG/90"], df_rank["A/90"])
maxv = max(df_rank["xAG/90"].max(), df_rank["A/90"].max())
plt.plot([0, maxv], [0, maxv])
plt.title("xAG/90 vs A/90 (Eficiência criativa) | min>=900")
plt.xlabel("xAG/90")
plt.ylabel("A/90")
plt.show() 
# %%
#xG+xAG/90 vs G+A/90 (linha y=x)
plt.figure()
plt.scatter(df_rank["xG+xAG/90"], df_rank["G+A/90"])
maxv = max(df_rank["xG+xAG/90"].max(), df_rank["G+A/90"].max())
plt.plot([0, maxv], [0, maxv])
plt.title("xG+xAG/90 vs G+A/90 (Produção vs Esperado) | min>=900")
plt.xlabel("xG+xAG/90")
plt.ylabel("G+A/90")
plt.show()
# %%
