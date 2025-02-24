import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Per avere numeri casuali ripetibili (opzionale)
np.random.seed(42)

# 1) GENERAZIONE DEI DATI
num_giorni = 305
media = 1200
dev_std = 900

# Generiamo i visitatori con distribuzione normale
visitatori = np.random.normal(loc=media, scale=dev_std, size=num_giorni)

# Creiamo un trend decrescente (opzionalmente aumenta o riduci la pendenza)
trend_decrescente = np.linspace(0, -100, num_giorni)

# Sommiamo il trend ai visitatori
visitatori_con_trend = visitatori + trend_decrescente

# Evitiamo valori negativi (casi estremi della distribuzione)
visitatori_con_trend = np.clip(visitatori_con_trend, a_min=0, a_max=None)

# Arrotondiamo a interi
visitatori_con_trend = visitatori_con_trend.astype(int)

# Creiamo un range di date per 305 giorni consecutivi
# Ad esempio, partiamo dal 1° gennaio 2023
date_range = pd.date_range(start='2023-01-01', periods=num_giorni, freq='D')

# 2) CREAZIONE DEL DATAFRAME
# Scegliamo casualmente la patologia tra 3 possibili
patologie = np.random.choice(['ossa', 'cuore', 'testa'], size=num_giorni)

df = pd.DataFrame({
    'Data': date_range,
    'Visitatori': visitatori_con_trend,
    'Patologia': patologie
})

# Mettiamo la colonna Data come indice (opzionale ma spesso comodo)
df.set_index('Data', inplace=True)

# 3) ANALISI DEI DATI

# 3a) Numero medio di visitatori per mese
# Creiamo una colonna 'Mese' partendo dalla Data
df['Mese'] = df.index.month
media_mensile = df.groupby('Mese')['Visitatori'].mean()

# 3b) Deviazione standard per mese
std_mensile = df.groupby('Mese')['Visitatori'].std()

# 3c) Patologia più e meno trovata
conteggio_patologie = df['Patologia'].value_counts()
patologia_piu_frequente = conteggio_patologie.idxmax()
patologia_meno_frequente = conteggio_patologie.idxmin()

print("Media mensile dei visitatori:")
print(media_mensile)
print("\nDeviazione standard mensile dei visitatori:")
print(std_mensile)
print("\nPatologia più frequente:", patologia_piu_frequente)
print("Patologia meno frequente:", patologia_meno_frequente)

# 4) VISUALIZZAZIONE DEI DATI

# 4a) Grafico a linee dei visitatori giornalieri + media mobile a 7 giorni
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Visitatori'], label='Visitatori giornalieri')

# Calcolo della media mobile a 7 giorni
df['media_mobile_7'] = df['Visitatori'].rolling(window=7).mean()
plt.plot(df.index, df['media_mobile_7'], color='red', label='Media mobile 7 giorni')

plt.title('Andamento giornaliero dei visitatori')
plt.xlabel('Data')
plt.ylabel('Numero di visitatori')
plt.legend()
plt.grid(True)
plt.show()

# 4b) Secondo grafico: media mensile dei visitatori
# Per comodità, riutilizziamo media_mensile (già calcolata)
plt.figure(figsize=(8, 5))
media_mensile.plot(kind='bar', color='skyblue')
plt.title('Media mensile dei visitatori')
plt.xlabel('Mese')
plt.ylabel('Visitatori (media)')
plt.grid(True)
plt.show()

# 4c) Grafico che mostri la divisione fra le 3 patologie (ad es. a torta)
plt.figure(figsize=(5, 5))
conteggio_patologie.plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribuzione delle patologie')
plt.ylabel('')  # Rimuoviamo l’etichetta "Patologia"
plt.show()
