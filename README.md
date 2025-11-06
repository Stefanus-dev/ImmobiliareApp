# 🏠 ImmobiliareApp

**ImmobiliareApp** è una semplice applicazione Python che consente la gestione di immobili per agenzie o privati.  
Permette di memorizzare, visualizzare e cercare case utilizzando un **database SQLite**.

---

## ✨ Funzionalità

| Funzione | Descrizione |
|--------|-------------|
| ➕ Inserire una nuova casa | Aggiunge un nuovo immobile con tutti i dati del proprietario |
| ❌ Eliminare una casa | Cancella una casa tramite il suo codice identificativo |
| 🔍 Cercare case per prezzo | Permette di trovare case in un intervallo di prezzo |
| 📄 Visualizzare tutte le case | Mostra tutti gli immobili attualmente in gestione |
| 💾 Salvataggio automatico | I dati vengono memorizzati nel database `case.db` |

---

## 🗂 Struttura del Database

Il programma utilizza **SQLite** e crea automaticamente il file `case.db` con la tabella:

| Campo | Tipo | Descrizione |
|------|------|-------------|
| codice | TEXT (PK) | Identificativo unico della casa |
| prezzo | REAL | Prezzo dell’immobile |
| n_vani | INTEGER | Numero dei vani |
| mq | REAL | Metri quadri |
| ascensore | TEXT (S/N) | Presenza dell’ascensore |
| condominio | TEXT (S/N) | Se fa parte di condominio |
| garage | TEXT (S/N) | Presenza garage |
| indirizzo | TEXT | Via / indirizzo |
| cap | TEXT | Codice postale |
| comune | TEXT | Comune |
| provincia | TEXT | Sigla provincia (es. MI, TO, RM) |
| nome_prop | TEXT | Nome proprietario |
| cognome_prop | TEXT | Cognome proprietario |
| tel_prop | TEXT | Telefono fisso |
| cell_prop | TEXT | Cellulare |

---

## 🚀 Requisiti

- Python **3.9 o superiore**
- Nessuna libreria esterna (SQLite è già integrato in Python)

---

## ▶️ Come avviare il programma

Apri il terminale nella cartella del progetto e lancia:

```bash
python main.py
