import streamlit as st

# Configurazione della pagina ottimizzata per smartphone
st.set_page_config(page_title="Island Cup Tracker", page_icon="🏝️", layout="centered")

# --- STILE GRAFICO APPOSITAMENTE STRUTTURATO PER CELLULARI ---
st.markdown(
    """
    <style>
    /* Sfondo e colori generali dell'isola */
    .stApp { background-color: #fcf8f2; }
    h1, h2, h3, p, label, .stMarkdown, span, div { color: #4a3728 !important; }
    
    /* Riquadri dei menu espandibili */
    .stExpander, div[data-baseweb="select"] { 
        background-color: #f4ebd9 !important; 
        border-radius: 12px; 
    }
    
    /* Pulsanti verdi grandi, facili da premere col pollice */
    div.stButton > button {
        background-color: #78b159 !important; 
        color: white !important;
        border: none !important; 
        border-radius: 10px !important; 
        font-weight: bold !important;
        padding: 10px !important;
        font-size: 1.1rem !important;
    }
    
    /* Stile speciale per i riquadri delle singole creature marine */
    .creature-card {
        background-color: #f4ebd9;
        border: 2px solid #e2d4b7;
        border-radius: 15px;
        padding: 12px;
        margin-bottom: 15px;
        text-align: center;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; letter-spacing: 1px;'>🌴 ISLAND CUP 🌴</h1>", unsafe_allow_html=True)
st.write("---")

# Inizializzazione variabili di sessione nel browser locale
if "creature" not in st.session_state:
    st.session_state.creature = []
if "nomi_giocatori" not in st.session_state:
    st.session_state.nomi_giocatori = {f"Player {i}": f"Player {i}" for i in range(1, 13)}
if "punteggi_giocatori" not in st.session_state:
    st.session_state.punteggi_giocatori = {f"Player {i}": [] for i in range(1, 13)}
if "giocatori_attivi" not in st.session_state:
    st.session_state.giocatori_attivi = []
if "tipo_torneo_precedente" not in st.session_state:
    st.session_state.tipo_torneo_precedente = ""

# --- 🏆 SELEZIONE DEL TORNEO PRESTABILITO 🏆 ---
st.subheader("📊 Seleziona il Torneo")
tipo_torneo = st.selectbox(
    "Scegli quale competizione avviare:",
    ["🗺️ Scegli un torneo...", "🌊 Torneo Creature Marine (40 Creature)", "🎣 Torneo di Pesca", "🦋 Torneo Insetti"]
)

if tipo_torneo != st.session_state.tipo_torneo_precedente:
    st.session_state.tipo_torneo_precedente = tipo_torneo
    if tipo_torneo == "🌊 Torneo Creature Marine (40 Creature)":
        punti_creature = {
            1: 2, 2: 2, 3: 3, 4: 9, 5: 3, 6: 4, 7: 6, 8: 2, 9: 3, 10: 3,
            11: 6, 12: 4, 13: 4, 14: 4, 15: 4, 16: 4, 17: 6, 18: 9, 19: 6, 20: 5,
            21: 7, 22: 9, 23: 4, 24: 6, 25: 6, 26: 8, 27: 9, 28: 2, 29: 8, 30: 6,
            31: 4, 32: 6, 33: 6, 34: 7, 35: 9, 36: 5, 37: 5, 38: 4, 39: 3, 40: 7
        }
        st.session_state.creature = [
            {"id": i, "punti": punti_creature[i], "immagine": f"{i}.png"} for i in range(1, 41)
        ]
    elif tipo_torneo == "🎣 Torneo di Pesca":
        st.session_state.creature = [{"id": "P1", "punti": 3, "immagine": None}]
    elif tipo_torneo == "🦋 Torneo Insetti":
        st.session_state.creature = [{"id": "I1", "punti": 2, "immagine": None}]
    else:
        st.session_state.creature = []
        
    for player_id in st.session_state.punteggi_giocatori:
        st.session_state.punteggi_giocatori[player_id] = [0] * len(st.session_state.creature)

# --- PANNELLI DI CONFIGURAZIONE COMPATTI ---
with st.expander("⚙️ Configura Giocatori (Spunta e Rinomina)"):
    st.write("Seleziona chi partecipa al torneo attuale:")
    partecipanti_scelti = []
    for i in range(1, 13):
        id_p = f"Player {i}"
        col_chk, col_txt = st.columns([1, 5])
        with col_chk:
            if st.checkbox("", key=f"check_{id_p}", value=(id_p in st.session_state.giocatori_attivi)):
                partecipanti_scelti.append(id_p)
        with col_txt:
            nuovo_nome = st.text_input(f"Nome per {id_p}", value=st.session_state.nomi_giocatori[id_p], key=f"edit_{id_p}", label_visibility="collapsed")
            if nuovo_nome.strip():
                st.session_state.nomi_giocatori[id_p] = nuovo_nome.strip()
    st.session_state.giocatori_attivi = partecipanti_scelti

st.write("---")

# --- SCHERMATA PRINCIPALE OTTIMIZZATA PER MOBILE ---
if tipo_torneo == "🗺️ Scegli un torneo...":
    st.info("👋 Scegli un torneo dal menu in alto per iniziare!")
elif not st.session_state.giocatori_attivi:
    st.info("👋 Apri il pannello '⚙️ Configura Giocatori' per attivare i partecipanti di oggi!")
else:
    # Selettore Giocatore molto grande
    opzioni_menu = {id_p: st.session_state.nomi_giocatori[id_p] for id_p in st.session_state.giocatori_attivi}
    giocatore_utente = st.selectbox(
        "📱 Di chi sono le catture che stai inserendo?", 
        list(opzioni_menu.keys()),
        format_func=lambda x: opzioni_menu[x],
        key="utente_locale"
    )
    
    nome_visualizzato = st.session_state.nomi_giocatori[giocatore_utente]
    st.write(f"### 🎣 Tabellone di: **{nome_visualizzato}**")
    
    # Su mobile mostriamo prima la Classifica e poi il Registro, messi in colonna verticale!
    with st.container():
        st.subheader("🏆 Classifica Torneo")
        classifica = {}
        for player_id in st.session_state.giocatori_attivi:
            lista_qta = st.session_state.punteggi_giocatori[player_id]
            totale_player = sum(st.session_state.creature[i]["punti"] * lista_qta[i] for i in range(len(st.session_state.creature)))
            nome_reale = st.session_state.nomi_giocatori[player_id]
            classifica[nome_reale] = (totale_player, player_id)
            
        classifica_ordinata = sorted(classifica.items(), key=lambda x: x[1][0], reverse=True)
        
        # Classifica a elenco verticale compatta
        for i, (nome_reale, (punti_totali, player_id)) in enumerate(classifica_ordinata, 1):
            emoji = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "👤"
            if player_id == giocatore_utente:
                st.markdown(f"👉 **{emoji} {i}° {nome_reale}: {punti_totali} PT**")
            else:
                st.write(f"{emoji} {i}° {nome_reale}: {punti_totali} PT")
                
    st.write("---")
    st.subheader("📝 Inserisci Catture")
    
    # Generazione a SCHEDE VERTICALI (Card) perfetta per i pollici e gli schermi dei telefoni
    for idx, creatura in enumerate(st.session_state.creature):
        # Apriamo un riquadro per ogni creatura
        st.markdown(f'<div class="creature-card">', unsafe_allow_html=True)
        
        # 1. Mostriamo l'immagine centrata e leggibile
        if creatura["immagine"] is not None:
            try:
                st.image(creatura["immagine"], width=90) # Più grande rispetto a prima
            except Exception:
                st.write(f"🖼️ Creatura #{creatura['id']}")
        else:
            st.write(f"✨ #{creatura['id']}")
            
        # 2. Mostriamo il valore in punti e il totale parziale di questa creatura
        quantita_corrente = st.session_state.punteggi_giocatori[giocatore_utente][idx]
        totale_riga = creatura["punti"] * quantita_corrente
        st.markdown(f"**Valore:** {creatura['punti']} Pt | **Totale:** {totale_riga} Pt")
        
        # 3. Casella numerica grande per aumentare la quantità comodamente da smartphone
        nuova_qta = st.number_input(
            f"Quantità per #{creatura['id']}", 
            min_value=0, 
            value=quantita_corrente, 
            key=f"qta_{giocatore_utente}_{creatura['id']}",
            label_visibility="collapsed"
        )
        st.session_state.punteggi_giocatori[giocatore_utente][idx] = nuova_qta
        
        st.markdown('</div>', unsafe_allow_html=True)

