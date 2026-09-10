import base64
from pathlib import Path

import streamlit as st


def to_data_uri_from_file(file_or_path):
    if file_or_path is None:
        return None

    if hasattr(file_or_path, "read"):
        raw = file_or_path.read()
        filename = getattr(file_or_path, "name", "image")
    else:
        path = Path(file_or_path)
        if not path.is_absolute():
            path = Path(__file__).resolve().parent / path
        if not path.exists():
            return None
        raw = path.read_bytes()
        filename = path.name

    if filename.lower().endswith(".png"):
        mime = "image/png"
    elif filename.lower().endswith((".jpg", ".jpeg")):
        mime = "image/jpeg"
    elif filename.lower().endswith(".webp"):
        mime = "image/webp"
    else:
        mime = "image/png"

    encoded = base64.b64encode(raw).decode("utf-8")
    return f"data:{mime};base64,{encoded}"


def resolve_image_source(value, creature_id):
    if value is None:
        return None

    if hasattr(value, "read"):
        return value

    if isinstance(value, Path):
        path = value if value.is_absolute() else Path(__file__).resolve().parent / value
        return path if path.exists() else None

    if isinstance(value, str):
        raw_name = value.strip()
        candidates = [raw_name]

        if not raw_name.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            candidates.extend([
                f"{raw_name}.png",
                f"{raw_name}.jpg",
                f"{raw_name}.jpeg",
                f"{raw_name}.webp",
                f"{creature_id}.png",
                f"{creature_id}.jpg",
                f"{creature_id}.jpeg",
                f"{creature_id}.webp",
            ])

        for candidate in candidates:
            path = Path(candidate)
            if not path.is_absolute():
                path = Path(__file__).resolve().parent / candidate
            if path.exists():
                return path

        if isinstance(creature_id, int):
            for pattern in [
                f"*{creature_id}*.png",
                f"*{creature_id}*.jpg",
                f"*{creature_id}*.jpeg",
                f"*{creature_id}*.webp",
            ]:
                matches = list(Path(__file__).resolve().parent.glob(pattern))
                if matches:
                    return matches[0]

    return None


st.set_page_config(page_title="Island Cup Tracker", page_icon="🏝️", layout="centered")

st.markdown(
    """
    <style>
        .stApp {
            background-color: #e0f7fa;
        }

        h1, h2, h3, p, label, .stMarkdown, span, div {
            color: #4a3728 !important;
        }

        .stExpander, div[data-baseweb="select"] {
            background-color: #f4ebd9 !important;
            border-radius: 12px;
        }

        div.stButton > button {
            background-color: #78b159 !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            font-weight: bold !important;
            padding: 10px !important;
            font-size: 1.1rem !important;
        }

        .page {
            max-width: 440px;
            margin: 0 auto;
        }

        .item {
            margin: 12px 0;
            padding: 8px 0;
            border-bottom: 1px solid rgba(74, 55, 40, 0.12);
        }

        .row {
            display: flex;
            align-items: center;
            gap: 12px;
            width: 100%;
            min-height: 72px;
        }

        .img-wrap {
            flex: 0 0 64px;
            width: 64px;
            height: 64px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 12px;
            overflow: hidden;
            background: #f4ebd9;
        }

        .img-wrap img {
            width: 64px;
            height: 64px;
            object-fit: contain;
            display: block;
            margin: 0;
        }

        .name {
            flex: 1;
            font-size: 0.95rem;
            font-weight: 700;
            line-height: 1.2;
            text-align: left;
            color: #4a3728;
        }

        .bottom {
            display: flex;
            justify-content: center;
            gap: 18px;
            font-size: 0.8rem;
            margin-top: 6px;
            color: #4a3728;
        }

        div[data-testid="stNumberInput"] {
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
        }

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
            font-size: min(6.5vw, 32px);
        }

        .title-emoji {
            font-size: min(7vw, 34px);
            display: inline-block;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

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

tipo_torneo_attuale = st.session_state.get("tipo_torneo_precedente", "🗺️ Scegli un torneo...")
nome_torneo_pulito = tipo_torneo_attuale.split(" ", 1)[-1] if " " in tipo_torneo_attuale else tipo_torneo_attuale
if nome_torneo_pulito == "Scegli un torneo...":
    nome_torneo_pulito = "ISLAND CUP"

st.markdown(
    f"""
    <div class="title-container">
        <span class="title-emoji">🌴</span>
        <span class="title-text">{nome_torneo_pulito.upper()}</span>
        <span class="title-emoji">🌴</span>
    </div>
    """,
    unsafe_allow_html=True,
)
st.write("---")

with st.expander("🏆 TORNEI ISOLANI"):
    st.write("Scegli quale competizione avviare:")
    tipo_torneo = st.selectbox(
        "Seleziona torneo:",
        [
            "🗺️ Scegli un torneo...",
            "🌊 Torneo Creature Marine (40 Creature)",
            "🎣 Torneo di Pesca",
            "🦋 Torneo Insetti",
        ],
        label_visibility="collapsed",
        index=[
            "🗺️ Scegli un torneo...",
            "🌊 Torneo Creature Marine (40 Creature)",
            "🎣 Torneo di Pesca",
            "🦋 Torneo Insetti",
        ].index(tipo_torneo_attuale),
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
            {"id": 40, "nome": "Cestello Di Venere", "punti": 7, "immagine": "40.png"},
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

with st.expander("🛠️ TORNEO FAI DA TE"):
    st.write("Aggiungi una creatura manuale:")
    punti_nuova_creatura = st.number_input("Valore in Punti:", min_value=0, max_value=100, value=2, key="nuovi_punti_c")
    file_foto_nuovo = st.file_uploader("Foto:", type=["png", "jpg", "jpeg"], key="nuovo_upload_c")

    if st.button("✨ AGGIUNGI ALLA TABELLA", use_container_width=True):
        nuovo_id = len(st.session_state.creature) + 1
        st.session_state.creature.append({
            "id": nuovo_id,
            "nome": f"Creatura {nuovo_id}",
            "punti": punti_nuova_creatura,
            "immagine": file_foto_nuovo,
        })
        for player_id in st.session_state.punteggi_giocatori:
            st.session_state.punteggi_giocatori[player_id].append(0)
        st.success("✅ Riga aggiunta!")
        st.rerun()

st.write("---")

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
        key="utente_locale",
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

    st.markdown('<div class="page">', unsafe_allow_html=True)

    for idx, creatura in enumerate(st.session_state.creature):
        nome_creatura = creatura.get("nome", f"Creatura {creatura['id']}")
        image_source = resolve_image_source(creatura.get("immagine"), creatura.get("id"))

        quantita_corrente = st.session_state.punteggi_giocatori[giocatore_utente][idx]
        totale_riga = creatura["punti"] * quantita_corrente

        img_html = ""
        if image_source is not None:
            image_data = to_data_uri_from_file(image_source)
            if image_data:
                img_html = f'<div class="img-wrap"><img src="{image_data}" alt="{nome_creatura}" /></div>'

        st.markdown(
            f"""
            <div class="item">
                <div class="row">
                    {img_html}
                    <div class="name">{nome_creatura}</div>
                </div>
                <div class="bottom">
                    <span>Valore: {creatura["punti"]}</span>
                    <span>Totale: {totale_riga}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        nuova_qta = st.number_input(
            f"Quantità per {nome_creatura}",
            min_value=0,
            value=quantita_corrente,
            key=f"qta_{giocatore_utente}_{idx}",
            label_visibility="collapsed",
        )

        if nuova_qta != quantita_corrente:
            st.session_state.punteggi_giocatori[giocatore_utente][idx] = nuova_qta
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
