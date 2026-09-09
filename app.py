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

    /* Contenitore Flexbox per mantenere il titolo fluido, centrato e su una sola riga */
    .title-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 8px;
        width: 100%;
        margin-bottom: 10px;
    }

    .title-text {
        font-family: 'Source Sans Pro', sans-serif;
        font-weight: bold;
        letter-spacing: 1px;
        text-align: center;
        white-space: nowrap;
        /* Usa le unità vw per adattarsi fluidamente alla larghezza dello schermo */
        font-size: min(6.5vw, 32px); 
    }

    .title-emoji {
        font-size: min(7vw, 34px);
        display: inline-block;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
    st.session_state.tipo_torneo_precedente = "🗺️ Scegli un torneo..."

# Recuperiamo il tipo di torneo o usiamo quello predefinito per il titolo iniziale
tipo_torneo_attuale = st.session_state.get("tipo_torneo_precedente", "🗺️ Scegli un torneo...")
nome_torneo_pulito = tipo_torneo_attuale.split(" ", 1)[-1] if " " in tipo_torneo_attuale else tipo_torneo_attuale
if nome_torneo_pulito == "Scegli un torneo...":
    nome_torneo_pulito = "ISLAND CUP"

# --- TITOLO REATTIVO FLUIDO E SEMPRE CENTRATO ---
st.markdown(
    f"""
    <div class="title-container">
        <span class="title-emoji">🌴</span>
        <span class="title-text">{nome_torneo_pulito.upper()}</span>
        <span class="title-emoji">🌴</span>
    </div>
    """, 
    unsafe_allow_html=True
)
st.write("---")

# --- PANNELLI DI CONFIGURAZIONE COMPATTI E SIMMETRICI ---

# 1. TORNEI ISOLANI
with st.expander("🏆 TORNEI ISOLANI"):
    st.write("Scegli quale competizione avviare:")
    tipo_torneo = st.selectbox(
        "Seleziona torneo:",
        ["🗺️ Scegli un torneo...", "🌊 Torneo Creature Marine (40 Creature)", "🎣 Torneo di Pesca", "🦋 Torneo Insetti"],
        label_visibility="collapsed",
        index=["🗺️ Scegli un torneo...", "🌊 Torneo Creature Marine (40 Creature)", "🎣 Torneo di Pesca", "🦋 Torneo Insetti"].index(tipo_torneo_attuale)
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
        
    # Reset corretto delle liste in base al numero di creature caricate
    for player_id in st.session_state.punteggi_giocatori:
        st.session_state.punteggi_giocatori[player_id] = [0] * len(st.session_state.creature)
    st.rerun()

# 2. ISOLANI
with st.expander("🎮 ISOLANI"):
    st.write("Spunta chi partecipa al torneo attuale e scrivi i loro nomi:")
    partecipanti_scelti = []
    for i in range(1, 13):
        id_p = f"Player {i}"
        col_chk, col_txt = st.columns([1, 4])
        with col_chk:
            if st.checkbox("", key=f"check_{id_p}", value=(id_p in st.session_state.giocatori_attivi), label_visibility="collapsed"):
                partecipanti_scelti.append(id_p)
        with col_txt:
            nuovo_nome = st.text_input(f"Nome per {id_p}", value=st.session_state.nomi_giocatori[id_p], key=f"edit_{id_p}", label_visibility="collapsed")
            if nuovo_nome.strip():
                st.session_state.nomi_giocatori[id_p] = nuevo_nome.strip()
    st.session_state.giocatori_attivi = partecipanti_scelti

# 3. TORNEO FAI DA TE
with st.expander("🛠️ TORNEO FAI DA TE"):
    st.write("Vuoi aggiungere a mano una foto o creare una riga personalizzata? Fallo qui:")
    punti_nuova_creatura = st.number_input("Valore in Punti per questa creatura:", min_value=0, max_value=100, value=2, key="nuovi_punti_c")
    file_foto_nuovo = st.file_uploader("Sfoglia e Carica la Foto dal dispositivo:", type=["png", "jpg", "jpeg"], key="nuovo_upload_c")
    
    if st.button("✨ AGGIUNGI ALLA TABELLA IN BASSO", use_container_width=True):
        nuovo_id = len(st.session_state.creature) + 1
        st.session_state.creature.append({
            "id": nuovo_id,
            "punti": punti_nuova_creatura,
            "immagine": file_foto_nuovo
        })
        for player_id in st.session_state.punteggi_giocatori:
            st.session_state.punteggi_giocatori[player_id].append(0)
        st.success("✅ Nuova riga aggiunta con successo al tabellone!")
        st.rerun()

st.write("---")

# --- SCHERMATA PRINCIPALE ---
if tipo_torneo == "🗺️ Scegli un torneo...":
    st.info("👋 Apri il pannello '🏆 TORNEI ISOLANI' in alto per iniziare!")
elif not st.session_state.giocatori_attivi:
    st.info("👋 Apri il pannello '🎮 ISOLANI' per attivare i partecipanti di oggi!")
else:
    opzioni_menu = {id_p: st.session_state.nomi_giocatori[id_p] for id_p in st.session_state.giocatori_attivi}
    giocatore_utente = st.selectbox(
        "📱 Di chi sono le catture che stai inserendo?", 
        list(opzioni_menu.keys()),
        format_func=lambda x: opzioni_menu[x],
        key="utente_locale"
    )
    
    nome_visualizzato = st.session_state.nomi_giocatori[giocatore_utente]
    
    # --- SEZIONE CLASSIFICA IN TEMPO REALE ---
    with st.container():
        st.subheader("🏆 Classifica Torneo")
        classifica = []
        for player_id in st.session_state.giocatori_attivi:
            lista_qta = st.session_state.punteggi_giocatori[player_id]
            
            # Controllo di sicurezza per evitare IndexError se le liste non sono sincronizzate
            if len(lista_qta) < len(st.session_state.creature):
                st.session_state.punteggi_giocatori[player_id] += [0] * (len(st.session_state.creature) - len(lista_qta))
                lista_qta = st.session_state.punteggi_giocatori[player_id]
                
            totale_player = sum(st.session_state.creature[i]["punti"] * lista_qta[i] for i in range(len(st.session_state.creature)))
            nome_reale = st.session_state.nomi_giocatori[player_id]
            classifica.append((totale_player, nome_reale))
            
        # Ordina la classifica dal punteggio più alto
        classifica.sort(key=lambda x: x[0], reverse=True)
        
        # Mostra la classifica in modo compatto
        for pos, (punti, nome) in enumerate(classifica, 1):
            medaglia = "🥇" if pos == 1 else "🥈" if pos == 2 else "🥉" if pos == 3 else "🏅"
            st.write(f"{medaglia} **{pos}° {nome}**: {punti} Punti")

    st.write("---")
    st.write(f"### 🎣 Tabellone di inserimento: **{nome_visualizzato}**")

    # --- INPUT DELLE CATTURE PER IL GIOCATORE SELEZIONATO ---
    for i, c in enumerate(st.session_state.creature):
        # Riquadro estetico per smartphone definito nel CSS in alto
        st.markdown(f'<div class="creature-card"><b>Creatura #{c["id"]}</b> ({c["punti"]} Punti)</div>', unsafe_allow_html=True)
        
        # Gestione dell'immagine personalizzata o di default
        if c["immagine"]:
            if isinstance(c["immagine"], str):
                # Se è un file locale (es. "1.png") proviamo a caricarlo, altrimenti mostriamo un placeholder
                try:
                    st.image(f"images/{c['immagine']}", width=80)
                except:
                    st.caption("📷 [Immagine Temporanea]")
            else:
                # Se è un file caricato dall'utente tramite file_uploader
                st.image(c["immagine"], width=80)
        
