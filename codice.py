import streamlit as st

# Configurazione della pagina con stile Cozy/Island
st.set_page_config(page_title="Island Cup Tracker", page_icon="🦋", layout="centered")

st.title("🏝️ Island Cup - Torneo di Cattura")
st.write("Benvenuti all'app di gestione del torneo per l'isola! Registra i partecipanti e calcola i punteggi.")

# Inizializza la lista dei giocatori se non esiste
if "giocatori" not in st.session_state:
    st.session_state.giocatori = {}

# Sezione 1: Registrazione Giocatori
st.subheader("👥 Registrazione Partecipanti")
nuovo_giocatore = st.text_input("Inserisci il nome del giocatore:", placeholder="Es. Alessio")

if st.button("Aggiungi Giocatore"):
    if nuovo_giocatore and nuovo_giocatore not in st.session_state.giocatori:
        st.session_state.giocatori[nuovo_giocatore] = 0
        st.success(f"🌴 {nuovo_giocatore} è entrato in gara!")
    elif nuovo_giocatore in st.session_state.giocatori:
        st.warning("Questo giocatore è già iscritto!")

# Sezione 2: Assegnazione Punti
if st.session_state.giocatori:
    st.subheader("🎣 Inserisci Catture")
    chi_ha_catturato = st.selectbox("Seleziona chi ha fatto la cattura:", list(st.session_state.giocatori.keys()))
    
    # Sistema punti semplice (puoi personalizzarlo!)
    tipo_cattura = st.radio("Cosa ha catturato?", ["Insetto/Pesce Comune (1pt)", "Insetto/Pesce Raro (3pt)"])
    punti = 1 if "Comune" in tipo_cattura else 3
    
    if st.button("Assegna Punti"):
        st.session_state.giocatori[chi_ha_catturato] += punti
        st.balloons() # Fa partire un'animazione di palloncini festosi!
        st.success(f"Assegnati {punti} punti a {chi_ha_catturato}!")

    # Sezione 3: Classifica Live
    st.subheader("🏆 Classifica in Tempo Reale")
    # Ordina i giocatori dal punteggio più alto a quello più basso
    classifica_ordinata = sorted(st.session_state.giocatori.items(), key=lambda x: x[1], reverse=True)
    
    for i, (nome, punteggio) in enumerate(classifica_ordinata, 1):
        st.write(f"**{i}° Posto:** {nome} — 🎯 {punteggio} punti")
else:
    st.info("Nessun giocatore iscritto al momento. Aggiungi il primo partecipante per iniziare!")
