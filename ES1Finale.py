import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1) GENERAZIONE DEI DATI
np.random.seed(42)  # Per ottenere risultati riproducibili (opzionale)

num_giorni = 365
media = 2000
dev_std = 500

# Generiamo i visitatori con distribuzione normale
visitatori = np.random.normal(loc=media, scale=dev_std, size=num_giorni)

# Creiamo un trend crescente: ad es. aggiungiamo una crescita lineare da 0 a 200
trend_crescente = np.linspace(0, 200, num_giorni)

# Sommiamo il trend ai visitatori
visitatori_con_trend = visitatori + trend_crescente

# Evitiamo valori negativi (in caso di outlier estremi)
visitatori_con_trend = np.clip(visitatori_con_trend, a_min=0, a_max=None)

# Arrotondiamo a interi
visitatori_con_trend = visitatori_con_trend.astype(int)

# Creiamo un intervallo di 365 giorni, ad esempio dal 1° gennaio di un certo anno
date_range = pd.date_range(start='2023-01-01', periods=num_giorni, freq='D')

# 2) CREAZIONE DEL DATAFRAME
df = pd.DataFrame({
    'Data': date_range,
    'Visitatori': visitatori_con_trend
})

# Mettiamo la colonna 'Data' come indice (opzionale ma spesso utile)
df.set_index('Data', inplace=True)

# 3) ANALISI DEI DATI
# Calcoliamo il numero medio di visitatori per mese e la deviazione standard
df['Mese'] = df.index.month  # estraiamo il numero di mese dalla data
media_mensile = df.groupby('Mese')['Visitatori'].mean()
std_mensile = df.groupby('Mese')['Visitatori'].std()

print("Media mensile dei visitatori:")
print(media_mensile)
print("\nDeviazione standard mensile dei visitatori:")
print(std_mensile)

# 4) VISUALIZZAZIONE DEI DATI

# 4a) Grafico a linee del numero di visitatori giornalieri
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Visitatori'], label='Visitatori giornalieri')

# Aggiunta della media mobile a 7 giorni
df['Media_mobile_7'] = df['Visitatori'].rolling(window=7).mean()
plt.plot(df.index, df['Media_mobile_7'], color='red', label='Media mobile 7 giorni')

plt.title('Andamento giornaliero dei visitatori (con trend crescente)')
plt.xlabel('Data')
plt.ylabel('Numero di Visitatori')
plt.legend()
plt.grid(True)
plt.show()

# 4b) Secondo grafico: la media mensile dei visitatori
plt.figure(figsize=(8, 5))
media_mensile.plot(kind='bar', color='skyblue')
plt.title('Media mensile dei visitatori')
plt.xlabel('Mese')
plt.ylabel('Visitatori (media)')
plt.grid(True)
plt.show()
