import streamlit as st

# Configurazione della pagina
st.set_page_config(page_title="Island Cup Tracker", page_icon="🏝️", layout="wide")

# --- STILE GRAFICO COZY ISLAND ---
st.markdown(
    """
    <style>
    .stApp { background-color: #fcf8f2; }
    h1, h2, h3, p, label, .stMarkdown, span { color: #4a3728 !important; }
    .stExpander, div[data-baseweb="select"] { background-color: #f4ebd9 !important; border-radius: 10px; }
    div.stButton > button {
        background-color: #78b159 !important; color: white !important;
        border: none !important; border-radius: 8px !important; font-weight: bold !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; letter-spacing: 2px;'>🌴 ISLAND CUP 🌴</h1>", unsafe_allow_html=True)
st.write("---")

# --- CONFIGURAZIONE CONDIVISIONE LIVE ---
st.sidebar.subheader("🔗 Condivisione Live")
sheet_url = st.sidebar.text_input(
    "Incolla il link di Google Fogli (Accesso aperto a tutti):", 
    placeholder="https://google.com..."
)

if not sheet_url:
    st.info("👋 Benvenuto! Per attivare la sincronizzazione live, incolla il link di un Google Foglio (condiviso come 'Editor per chiunque') nella barra laterale a sinistra.")
    st.stop()

# Inizializzazione variabili di sessione
if "creature" not in st.session_state:
    punti_creature = {
        1: 2, 2: 2, 3: 3, 4: 9, 5: 3, 6: 4, 7: 6, 8: 2, 9: 3, 10: 3,
        11: 6, 12: 4, 13: 4, 14: 4, 15: 4, 16: 4, 17: 6, 18: 9, 19: 6, 20: 5,
        21: 7, 22: 9, 23: 4, 24: 6, 25: 6, 26: 8, 27: 9, 28: 2, 29: 8, 30: 6,
        31: 4, 32: 6, 33: 6, 34: 7, 35: 9, 36: 5, 37: 5, 38: 4, 39: 3, 40: 7
    }
    st.session_state.creature = [
        {"id": i, "punti": punti_creature[i], "immagine": f"{i}.png"} for i in range(1, 41)
    ]

if "nomi_giocatori" not in st.session_state:
    st.session_state.nomi_giocatori = {f"Player {i}": f"Player {i}" for i in range(1, 13)}
if "punteggi_giocatori" not in st.session_state:
    st.session_state.punteggi_giocatori = {f"Player {i}": [0] * len(st.session_state.creature) for i in range(1, 13)}
if "giocatori_attivi" not in st.session_state:
    st.session_state.giocatori_attivi = []
if "tipo_torneo_precedente" not in st.session_state:
    st.session_state.tipo_torneo_precedente = ""

# --- 🏆 SELEZIONE DEL TORNEO PRESTABILITO 🏆 ---
st.subheader("📊 Seleziona il Torneo della Partita")
tipo_torneo = st.selectbox(
    "Scegli quale competizione avviare ora:",
    ["🗺️ Scegli un torneo...", "🌊 Torneo Creature Marine (40 Creature)", "🎣 Torneo di Pesca (Pronto per la tua lista)", "🦋 Torneo Insetti (Pronto per la tua lista)"]
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
    elif tipo_torneo == "🎣 Torneo di Pesca (Pronto per la tua lista)":
        st.session_state.creature = [{"id": "P1", "punti": 3, "immagine": None}]
    elif tipo_torneo == "🦋 Torneo Insetti (Pronto per la tua lista)":
        st.session_state.creature = [{"id": "I1", "punti": 2, "immagine": None}]
    else:
        st.session_state.creature = []
        
    for player_id in st.session_state.punteggi_giocatori:
        st.session_state.punteggi_giocatori[player_id] = [0] * len(st.session_state.creature)

st.write("---")

# --- PANNELLI DI CONFIGURAZIONE AVANZATA ---
col_setup_nomi, col_setup_creature = st.columns(2)

with col_setup_nomi:
    with st.expander("⚙️ Selezione e Personalizzazione Giocatori"):
        st.write("Spunta i partecipanti per la partita attuale e scrivi i loro nomi:")
        partecipanti_scelti = []
        for i in range(1, 13):
            id_p = f"Player {i}"
            col_chk, col_txt = st.columns([0.5, 5])
            with col_chk:
                if st.checkbox("", key=f"check_{id_p}", value=(id_p in st.session_state.giocatori_attivi), label_visibility="collapsed"):
                    partecipanti_scelti.append(id_p)
            with col_txt:
                nuovo_nome = st.text_input(f"Nome per {id_p}", value=st.session_state.nomi_giocatori[id_p], key=f"edit_{id_p}", label_visibility="collapsed")
                if nuovo_nome.strip():
                    st.session_state.nomi_giocatori[id_p] = nuovo_nome.strip()
        st.session_state.giocatori_attivi = partecipanti_scelti

with col_setup_creature:
    with st.expander("➕ Inserisci Creatura Extra a Mano (Opzionale)"):
        st.write("Vuoi aggiungere una creatura imprevista fuori catalogo? Caricala qui:")
        punti_nuova_creatura = st.number_input("Valore in Punti:", min_value=0, max_value=100, value=2, key="nuovi_punti_c")
        file_foto_nuovo = st.file_uploader("Carica Foto dal PC:", type=["png", "jpg", "jpeg"], key="nuovo_upload_c")
        
        if st.button("✨ AGGIUNGI AL TORNEO CORRENTE", use_container_width=True):
            nuovo_id = len(st.session_state.creature) + 1
            st.session_state.creature.append({
                "id": nuovo_id,
                "punti": punti_nuova_creatura,
                "immagine": file_foto_nuovo
            })
            for player_id in st.session_state.punteggi_giocatori:
                st.session_state.punteggi_giocatori[player_id].append(0)
            st.success("✅ Nuova riga aggiunta al tabellone!")
            st.rerun()

st.write("---")

# --- SCHERMATA PRINCIPALE ---
col_griglia, col_classifica = st.columns([3, 1.5], gap="large")

with col_griglia:
    st.subheader("📝 Il Tuo Registro delle Catture")
    
    if tipo_torneo == "🗺️ Scegli un torneo...":
        st.info("👋 Per iniziare, seleziona il tipo di torneo dal menu a tendina in alto!")
    elif not st.session_state.giocatori_attivi:
        st.info("👋 Nessun giocatore in gara. Attiva i partecipanti nel pannello in alto a sinistra '⚙️ Selezione e Personalizzazione Giocatori'!")
    else:
        opzioni_menu = {id_p: st.session_state.nomi_giocatori[id_p] for id_p in st.session_state.giocatori_attivi}
        giocatore_utente = st.selectbox(
            "📱 Chi sta usando questo telefono? (Seleziona il tuo nome):", 
            list(opzioni_menu.keys()),
            format_func=lambda x: opzioni_menu[x],
            key="utente_locale"
        )
        
        nome_visualizzato = st.session_state.nomi_giocatori[giocatore_utente]
        st.write(f"### 🎣 Tabellone personale di: **{nome_visualizzato}**")
        st.write("---")

        if not st.session_state.creature:
            st.info("👋 Il tabellone è vuoto.")
        else:
            col_img_h, col_val_h, col_qta_h, col_tot_h = st.columns([1.5, 1.5, 2, 1.5])
            col_img_h.write("**Creatura (Foto)**")
            col_val_h.write("**Valore**")
            col_qta_h.write("**Quantità**")
            col_tot_h.write("**Totale**")
            st.write("---")

            for idx, creatura in enumerate(st.session_state.creature):
                col_img, col_val, col_qta, col_tot = st.columns([1.5, 1.5, 2, 1.5])
                
                with col_img:
                    if creatura["immagine"] is not None:
                        try:
                            st.image(creatura["immagine"], width=55)
                        except Exception:
                            st.write(f"🖼️ # {creatura['id']}")
                    else:
                        st.write(f"✨ #{creatura['id']}")

                with col_val:
                    st.write(f"{creatura['punti']} Pt")
                    
                with col_qta:
                    quantita_corrente = st.session_state.punteggi_giocatori[giocatore_utente][idx]
                    nuova_qta = st.number_input(
                        f"Q.tà {creatura['id']}", 
                        min_value=0, 
                        value=quantita_corrente, 
                        key=f"qta_{giocatore_utente}_{creatura['id']}", 
                        label_visibility="collapsed"
                    )
                    st.session_state.punteggi_giocatori[giocatore_utente][idx] = nuova_qta
                    
                totale_riga = creatura["punti"] * nuova_qta
                with col_tot:
                    st.write(f"**{totale_riga} Pt**")

with col_classifica:
    st.subheader("🏆 Classifica Generale Live")
    
    if tipo_torneo == "🗺️ Scegli un torneo..." or not st.session_state.giocatori_attivi:
        st.write("*In attesa dei partecipanti...*")
    else:
        classifica = {}
        for player_id in st.session_state.giocatori_attivi:
            lista_qta = st.session_state.punteggi_giocatori[player_id]
            totale_player = sum(st.session_state.creature[i]["punti"] * lista_qta[i] for i in range(len(st.session_state.creature)))
            nome_reale = st.session_state.nomi_giocatori[player_id]
            classifica[nome_reale] = (totale_player, player_id)
            
        classifica_ordinata = sorted(classifica.items(), key=lambda x: x, reverse=True)
        
        for i, (nome_reale, (punti_totali, player_id)) in enumerate(classifica_ordinata, 1):
            emoji = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "👤"
            is_utente_corrente = (player_id == giocatore_utente)
                
            if is_utente_corrente:
                st.markdown(f"### 👉 {emoji} {i}° {nome_reale}: **{punti_totali} PT**")
            else:
                st.markdown(f"### {emoji} {i}° {nome_reale}: {punti_totali} PT")
