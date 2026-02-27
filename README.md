# ⚽ Análise de Dados do Brasileirão 2024

Projeto de análise exploratória e construção de métricas de performance de jogadores do **Campeonato Brasileiro 2024**, utilizando **Python, Pandas, NumPy e Matplotlib**.

O objetivo principal foi transformar dados brutos em um dataset analítico, gerar métricas avançadas e produzir visualizações capazes de responder perguntas relevantes sobre desempenho individual na competição.

---

## 🎯 Objetivos do projeto

* Construir um dataset consolidado por jogador
* Criar métricas totais e normalizadas (por 90 minutos)
* Avaliar eficiência ofensiva, criação e progressão de jogo
* Identificar destaques estatísticos da temporada
* Produzir gráficos analíticos para storytelling com dados

---

## 📊 Principais métricas desenvolvidas

### 🔥 Produção ofensiva

* Gols totais
* Assistências totais
* Participações em gol (G+A)
* G/90, A/90 e G+A/90

### 🎯 Métricas esperadas (expected stats)

* xG (expected goals)
* npxG (non-penalty expected goals)
* xAG (expected assists)
* xG+xAG
* G-xG (over/underperformance)

### 🧠 Criação de jogadas

* SCA (Shot Creating Actions)
* GCA (Goal Creating Actions)

### 🚀 Progressão

* Passes progressivos (PrgP)
* Conduções progressivas (PrgC)

### 🎭 Drible

* Tentativas
* Sucessos
* Taxa de sucesso (Drible%)

### 🟨 Disciplina

* Cartões amarelos
* Cartões vermelhos

---

## 📈 Visualizações produzidas

* Rankings por 90 minutos (gols, assistências, criação, progressão)
* Conversão de chances (Gols/xG)
* Eficiência criativa (Assistências/xAG)
* Overperformance ofensiva
* Scatter plots:

  * xG/90 vs G/90
  * xAG/90 vs A/90
  * xG+xAG/90 vs G+A/90

---


---

## ⚙️ Pipeline do projeto

### 1️⃣ Tratamento e feature engineering

* Leitura dos datasets
* Limpeza e padronização
* Agregação por jogador
* Criação de métricas derivadas
* Export do dataset final (`metricas.csv`)

### 2️⃣ Visualização

* Leitura do dataset analítico
* Aplicação de filtros (ex.: mínimo de minutos)
* Geração de rankings e gráficos

---


