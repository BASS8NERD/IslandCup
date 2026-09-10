import streamlit as st

# Configurazione della pagina ottimizzata per smartphone
st.set_page_config(page_title="Island Cup Tracker", page_icon="🏝️", layout="centered")

# --- STILE GRAFICO APPOSITAMENTE STRUTTURATO PER CELLULARI ---
st.markdown(
    """
    <style>
    /* Sfondo e colori generali dell'isola */
        .stApp { background-color: #e0f7fa; }
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
    }        .creature-card [data-testid="stVerticalBlock"] {
        align-items: center !important;
    }


    /* Centra il testo del Valore */
    div[data-testid="stMarkdownContainer"] {
        text-align: center !important;
    }
    /* Centra il selettore numerico della Quantità */
    div[data-testid="stNumberInput"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
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

    /* Card creature: immagine a sinistra, nome a destra, info sotto */
    .creature-row {
        display: flex;
        align-items: center;
        gap: 12px;
        width: 100%;
        margin-bottom: 8px;
    }

    .creature-image-wrap {
        flex: 0 0 auto;
        display: flex;
        align-items: center;
        justify-content: center;
        min-width: 80px;
    }

    .creature-image-wrap img {
        display: block !important;
        width: min(22vw, 80px) !important;
        height: min(22vw, 80px) !important;
        max-width: 80px !important;
        max-height: 80px !important;
        object-fit: contain !important;
        border-radius: 10px !important;
    }

    .creature-meta {
        flex: 1;
        text-align: left;
        font-weight: 600;
        line-height: 1.3;
    }

    .creature-meta .creature-name {
        font-size: 0.95rem;
        margin: 0;
    }

    .creature-details {
        text-align: center;
        margin-top: 6px;
    }

    div[data-testid="stImageFilter"] { display: flex !important; justify-content: center !important; } img { margin: 0 auto !important; display: block !important; }

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

# --- PANNELLI DI CONFIGURAZIONE COMPATTI E SIMMETRICI CON LE NUOVE EMOTICON ---

# 1. NUOVA ICONA: COPPA
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
        st.session_state.creature = [
            {"id": 1, "nome": "Alga Wakame", "punti": 2, "immagine": "1.png"},
            {"id": 2, "nome": "Vite Di Mare", "punti": 2, "immagine": "2.png"},
            {"id": 3, "nome": "Cetriolo Di Mare", "punti": 3, "immagine": "3.png"},
            {"id": 4, "nome": "Porcellino Di Mare", "punti": 9, "immagine": "4.png"},
            {"id": 5, "nome": "Stella Marina", "punti": 3, "immagine": "5.png"},
            {"id": 6, "nome": "Riccio Di Mare", "punti": 4, "immagine": "6.png"},
            {"id": 7, "nome": "Riccio Matita", "punti": 6, "immagine": "7.png"},
            {"id": 8, "nome": "Anemone Di Mare", "punti": 2, "immagine": "8.png"},
            {"id": 9, "nome": "Medusa Aurelia", "punti": 3, "immagine": "9.png"},
            {"id": 10, "nome": "Nudibranchi", "punti": 3, "immagine": "10.png"},
            {"id": 11, "nome": "Ostrica Pinctada", "punti": 6, "immagine": "11.png"},
            {"id": 12, "nome": "Cozza", "punti": 4, "immagine": "12.png"},
            {"id": 13, "nome": "Ostrica", "punti": 4, "immagine": "13.png"},
            {"id": 14, "nome": "Capasanta", "punti": 4, "immagine": "14.png"},
            {"id": 15, "nome": "Buccino", "punti": 4, "immagine": "15.png"},
            {"id": 16, "nome": "Lumaca Turbante", "punti": 4, "immagine": "16.png"},
            {"id": 17, "nome": "Abalone", "punti": 6, "immagine": "17.png"},
            {"id": 18, "nome": "Tridacna Gigante", "punti": 9, "immagine": "18.png"},
            {"id": 19, "nome": "Nautilus", "punti": 6, "immagine": "19.png"},
            {"id": 20, "nome": "Polpo", "punti": 5, "immagine": "20.png"},
            {"id": 21, "nome": "Polpo Ombrello", "punti": 7, "immagine": "21.png"},
            {"id": 22, "nome": "Calamaro Vampiro", "punti": 9, "immagine": "22.png"},
            {"id": 23, "nome": "Calamaro Lucciola", "punti": 4, "immagine": "23.png"},
            {"id": 24, "nome": "Granchio Gazami", "punti": 6, "immagine": "24.png"},
            {"id": 25, "nome": "Granciporro", "punti": 6, "immagine": "25.png"},
            {"id": 26, "nome": "Granchio Della Neve", "punti": 8, "immagine": "26.png"},
            {"id": 27, "nome": "Granchio Gigante", "punti": 9, "immagine": "27.png"},
            {"id": 28, "nome": "Dente Di Cane", "punti": 2, "immagine": "28.png"},
            {"id": 29, "nome": "Granchio Gigante Del Giappone", "punti": 8, "immagine": "29.png"},
            {"id": 30, "nome": "Gambero Black Tiger", "punti": 6, "immagine": "30.png"},
            {"id": 31, "nome": "Gamberetto Boreale", "punti": 4, "immagine": "31.png"},
            {"id": 32, "nome": "Gambero Mantide", "punti": 6, "immagine": "32.png"},
            {"id": 33, "nome": "Aragosta Mediterranea", "punti": 6, "immagine": "33.png"},
            {"id": 34, "nome": "Astice", "punti": 7, "immagine": "34.png"},
            {"id": 35, "nome": "Isopode Gigante", "punti": 9, "immagine": "35.png"},
            {"id": 36, "nome": "Granchio Ferro Di Cavallo", "punti": 5, "immagine": "36.png"},
            {"id": 37, "nome": "Ananas Di Mare", "punti": 5, "immagine": "37.png"},
            {"id": 38, "nome": "Anguilla Di Giardino", "punti": 4, "immagine": "38.png"},
            {"id": 39, "nome": "Verme Piatto", "punti": 3, "immagine": "39.png"},
            {"id": 40, "nome": "Cestello Di Venere", "punti": 7, "immagine": "40.png"}
        ]
    elif tipo_torneo == "🎣 Torneo di Pesca":
        st.session_state.creature = [{"id": "P1", "nome": "Pesce 1", "punti": 3, "immagine": None}]
    elif tipo_torneo == "🦋 Torneo Insetti":
        st.session_state.creature = [{"id": "I1", "nome": "Insetto 1", "punti": 2, "immagine": None}]
    else:
        st.session_state.creature = []
        
    for player_id in st.session_state.punteggi_giocatori:
        st.session_state.punteggi_giocatori[player_id] = [0] * len(st.session_state.creature)
    st.rerun()

# 2. NUOVA ICONA: JOYPAD
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
                st.session_state.nomi_giocatori[id_p] = nuovo_nome.strip()
    st.session_state.giocatori_attivi = partecipanti_scelti

# 3. NUOVA ICONA: MARTELLO E CHIAVE INGLESE
with st.expander("🛠️ TORNEO FAI DA TE"):
    st.write("Vuoi aggiungere a mano una foto o creare una riga personalizzata? Fallo qui:")
    punti_nuova_creatura = st.number_input("Valore in Punti per questa creatura:", min_value=0, max_value=100, value=2, key="nuovi_punti_c")
    file_foto_nuovo = st.file_uploader("Sfoglia e Carica la Foto dal dispositivo:", type=["png", "jpg", "jpeg"], key="nuovo_upload_c")
    
    if st.button("✨ AGGIUNGI ALLA TABELLA IN BASSO", use_container_width=True):
        nuovo_id = len(st.session_state.creature) + 1
        st.session_state.creature.append({
            "id": nuovo_id,
            "nome": f"Creatura {nuovo_id}",
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
    st.write(f"### 🎣 Tabellone di: **{nome_visualizzato}**")
    
    with st.container():
        st.subheader("🏆 Classifica Torneo")
        classifica = {}
        for player_id in st.session_state.giocatori_attivi:
            lista_qta = st.session_state.punteggi_giocatori[player_id]
            totale_player = sum(st.session_state.creature[i]["punti"] * lista_qta[i] for i in range(len(st.session_state.creature)))
            nome_reale = st.session_state.nomi_giocatori[player_id]
            classifica[nome_reale] = (totale_player, player_id)
            
        classifica_ordinata = sorted(classifica.items(), key=lambda x: x[1][0], reverse=True)
        
        for i, (nome_reale, (punti_totali, player_id)) in enumerate(classifica_ordinata, 1):
            emoji = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "👤"
            if player_id == giocatore_utente:
                st.markdown(f"### 👉 {emoji} {i}° {nome_reale}: **{punti_totali} PT**")
            else:
                st.markdown(f"### {emoji} {i}° {nome_reale}: {punti_totali} PT")
                
    st.write("---")
    st.subheader("📝 Inserisci Catture")
    
   # Generazione a SCHEDE VERTICALI (Card)
    for idx, creatura in enumerate(st.session_state.creature):
        st.markdown(f'<div class="creature-card">', unsafe_allow_html=True)
        
        nome_creatura = creatura.get("nome", f"Creatura {creatura['id']}")
        if creatura["immagine"] is not None:
            try:
                col_img, col_txt = st.columns([1, 3])
                with col_img:
                    st.image(creatura["immagine"], width=80)
                with col_txt:
                    st.markdown(f"### #{creatura['id']} · {nome_creatura}")
            except Exception:
                st.write(f"🖼️ {nome_creatura}")
        else:
            col_txt = st.columns([1, 3])[1]
            with col_txt:
                st.markdown(f"### #{creatura['id']} · {nome_creatura}")

        quantita_corrente = st.session_state.punteggi_giocatori[giocatore_utente][idx]
        totale_riga = creatura["punti"] * quantita_corrente
        st.markdown(
            f'<div class="creature-details"><strong>Valore:</strong> {creatura["punti"]} | <strong>Totale:</strong> {totale_riga}</div>',
            unsafe_allow_html=True,
        )
        
        nuova_qta = st.number_input(
            f"Quantità per {nome_creatura}",
            min_value=0,
            value=quantita_corrente,
            key=f"qta_{giocatore_utente}_{idx}",
            label_visibility="collapsed"
        )
        if nuova_qta != quantita_corrente:
            st.session_state.punteggi_giocatori[giocatore_utente][idx] = nuova_qta
            st.rerun()
            
        st.markdown('</div>', unsafe_allow_html=True)
