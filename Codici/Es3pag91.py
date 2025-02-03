def comprimi_stringa(testo):
    # Se la stringa è vuota o nulla, restituisce subito la stessa
    if not testo:
        return testo
    
    # Per costruire la stringa compressa usiamo una lista, così poi la uniamo
    compressa = []
    conteggio = 1  # Conta quante volte lo stesso carattere si ripete
    carattere_attuale = testo[0]
    
    # Scorri il testo a partire dal secondo carattere
    for i in range(1, len(testo)):
        if testo[i] == carattere_attuale:
            # Se il carattere è lo stesso, aumenta il conteggio
            conteggio += 1
        else:
            # Altrimenti “chiudi” il blocco di caratteri precedenti
            compressa.append(carattere_attuale)
            compressa.append(str(conteggio))
            # Aggiorna per il nuovo carattere
            carattere_attuale = testo[i]
            conteggio = 1
    
    # Aggiungi l’ultimo blocco (riguarda l’ultimo carattere)
    compressa.append(carattere_attuale)
    compressa.append(str(conteggio))
    
    # Unisci la lista per ottenere la stringa finale compressa
    stringa_compressa = "".join(compressa)
    
    #for parola in compressa:
    #    stringa_compressa += parola
    
    # Se la versione compressa è più corta, restituiscila; altrimenti la stringa originale
    if len(stringa_compressa) < len(testo):
        return stringa_compressa
    else:
        return testo

# Esempio di utilizzo:
s = "aaabbc"
print(comprimi_stringa(s))  # Risultato: "a3b2c1"
