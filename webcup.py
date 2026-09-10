import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="CUP OF THE ISLANDS",
    page_icon="🌊",
    layout="wide",
)

MARINE_CREATURES = [
    {"Creatura": "Polpo", "Foto": "🐙", "Valore": 10},
    {"Creatura": "Pesce pagliaccio", "Foto": "🐠", "Valore": 12},
    {"Creatura": "Tonno", "Foto": "🐟", "Valore": 15},
    {"Creatura": "Gambero", "Foto": "🦐", "Valore": 18},
    {"Creatura": "Granchio", "Foto": "🦀", "Valore": 20},
    {"Creatura": "Medusa", "Foto": "🪼", "Valore": 22},
    {"Creatura": "Delfino", "Foto": "🐬", "Valore": 25},
    {"Creatura": "Murena", "Foto": "🐍", "Valore": 28},
    {"Creatura": "Cavaliere di mare", "Foto": "🦑", "Valore": 30},
    {"Creatura": "Squalo bianco", "Foto": "🦈", "Valore": 32},
    {"Creatura": "Mazzancolla", "Foto": "🦐", "Valore": 18},
    {"Creatura": "Riccio di mare", "Foto": "🌵", "Valore": 16},
    {"Creatura": "Seppia", "Foto": "🦑", "Valore": 26},
    {"Creatura": "Orata", "Foto": "🐟", "Valore": 12},
    {"Creatura": "Gattufo di mare", "Foto": "🐡", "Valore": 17},
    {"Creatura": "Anemone", "Foto": "🌊", "Valore": 14},
    {"Creatura": "Piccola razza", "Foto": "🐠", "Valore": 11},
    {"Creatura": "Manta", "Foto": "🦭", "Valore": 33},
    {"Creatura": "Barbo", "Foto": "🐟", "Valore": 13},
    {"Creatura": "Cefalo", "Foto": "🐡", "Valore": 19},
    {"Creatura": "Tartaruga marina", "Foto": "🐢", "Valore": 35},
    {"Creatura": "Calamaro", "Foto": "🦑", "Valore": 24},
    {"Creatura": "Pesce luna", "Foto": "🐠", "Valore": 21},
    {"Creatura": "Sardina", "Foto": "🐟", "Valore": 10},
    {"Creatura": "Balena", "Foto": "🐋", "Valore": 40},
    {"Creatura": "Foca", "Foto": "🦭", "Valore": 27},
    {"Creatura": "Gabbiano marino", "Foto": "🐦", "Valore": 15},
    {"Creatura": "Conchiglia", "Foto": "🐚", "Valore": 9},
    {"Creatura": "Nautilo", "Foto": "🐙", "Valore": 23},
    {"Creatura": "Cavalluccio marino", "Foto": "🐠", "Valore": 16},
    {"Creatura": "Elicide", "Foto": "🐚", "Valore": 14},
    {"Creatura": "Pesce palla", "Foto": "🐡", "Valore": 20},
    {"Creatura": "Stella marina", "Foto": "⭐", "Valore": 13},
    {"Creatura": "Pesce angelo", "Foto": "🐟", "Valore": 24},
    {"Creatura": "Barracuda", "Foto": "🐠", "Valore": 29},
    {"Creatura": "Corallo", "Foto": "🪸", "Valore": 12},
    {"Creatura": "Canocchia", "Foto": "🌿", "Valore": 8},
    {"Creatura": "Rombo", "Foto": "🐟", "Valore": 31},
    {"Creatura": "Sogliola", "Foto": "🐠", "Valore": 18},
    {"Creatura": "Squid", "Foto": "🦑", "Valore": 22},
]

TOURNAMENTS = {
    "Torneo Creature Marine": MARINE_CREATURES,
    "Torneo Di Pesca": [
        {"Creatura": "Pesce 1", "Foto": "🐠", "Valore": 12},
        {"Creatura": "Pesce 2", "Foto": "🐡", "Valore": 18},
        {"Creatura": "Pesce 3", "Foto": "🐟", "Valore": 25},
        {"Creatura": "Pesce 4", "Foto": "🦐", "Valore": 35},
    ],
    "Torneo Caccia all'insetto": [
        {"Creatura": "Insetto 1", "Foto": "🦋", "Valore": 15},
        {"Creatura": "Insetto 2", "Foto": "🐝", "Valore": 22},
        {"Creatura": "Insetto 3", "Foto": "🪲", "Valore": 28},
        {"Creatura": "Insetto 4", "Foto": "🦗", "Valore": 33},
    ],
    "Torneo Mix": [
        {"Creatura": "Mix 1", "Foto": "🦐", "Valore": 16},
        {"Creatura": "Mix 2", "Foto": "🐠", "Valore": 20},
        {"Creatura": "Mix 3", "Foto": "🦋", "Valore": 24},
        {"Creatura": "Mix 4", "Foto": "🐟", "Valore": 32},
    ],
}

if "show_create_menu" not in st.session_state:
    st.session_state.show_create_menu = False
if "creature_points" not in st.session_state:
    st.session_state.creature_points = 1
if "creature_rows" not in st.session_state:
    st.session_state.creature_rows = pd.DataFrame(columns=["Creatura", "Punti", "Foto"])
if "active_hero_button" not in st.session_state:
    st.session_state.active_hero_button = "Tornei"
if "selected_tournament" not in st.session_state:
    st.session_state.selected_tournament = "Torneo Creature Marine"
if "participant_slots" not in st.session_state:
    st.session_state.participant_slots = [
        {"selected": i < 4, "name": ["Luca", "Marco", "Sofia", "Giulia"][i] if i < 4 else f"Giocatore {i + 1}"}
        for i in range(12)
    ]
if "selected_participant" not in st.session_state:
    st.session_state.selected_participant = "Luca"
if "capture_data" not in st.session_state:
    st.session_state.capture_data = {}
if "last_tournament" not in st.session_state:
    st.session_state.last_tournament = None


def get_active_participants():
    active = []
    for slot in st.session_state.participant_slots:
        name = (slot.get("name") or "").strip()
        if slot.get("selected") and name:
            active.append(name)
    return active


def build_capture_frame(tournament_name):
    rows = []
    for item in TOURNAMENTS.get(tournament_name, []):
        rows.append({
            "Creatura": item.get("Creatura", "Creatura"),
            "Foto": item.get("Foto", ""),
            "Valore": int(item.get("Valore", 0)),
            "Quantità": 0,
            "Totale": 0,
        })
    return pd.DataFrame(rows)


if st.session_state.selected_tournament != st.session_state.last_tournament:
    for participant in get_active_participants():
        st.session_state.capture_data[participant] = build_capture_frame(st.session_state.selected_tournament)
    st.session_state.last_tournament = st.session_state.selected_tournament

for participant in get_active_participants():
    if participant not in st.session_state.capture_data:
        st.session_state.capture_data[participant] = build_capture_frame(st.session_state.selected_tournament)

if st.session_state.selected_participant not in get_active_participants():
    active_participants = get_active_participants()
    st.session_state.selected_participant = active_participants[0] if active_participants else ""

st.markdown(
    """
    <style>
        .main {
            background: linear-gradient(180deg, #dffdfb 0%, #d7f7f8 30%, #f3fdfd 100%);
        }

        .hero {
            background: linear-gradient(135deg, rgba(12, 135, 154, 0.96), rgba(18, 190, 204, 0.82));
            border-radius: 24px;
            padding: 2.2rem 2.4rem;
            box-shadow: 0 14px 30px rgba(10, 94, 112, 0.18);
            border: 1px solid rgba(255,255,255,0.25);
            margin-bottom: 1.5rem;
        }

        .eyebrow {
            display: inline-block;
            background: rgba(255,255,255,0.15);
            color: #ecfeff;
            border: 1px solid rgba(255,255,255,0.25);
            border-radius: 999px;
            padding: 0.35rem 0.8rem;
            font-size: 0.76rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 1rem;
        }

        .hero h1 {
            color: white;
            font-size: 3rem;
            line-height: 1.1;
            margin: 0 0 0.8rem 0;
            font-weight: 800;
        }

        .hero p {
            color: rgba(255,255,255,0.9);
            font-size: 1.1rem;
            line-height: 1.6;
            max-width: 700px;
            margin: 0;
        }

        div.stButton > button {
            background: linear-gradient(135deg, #f8dcc0, #efbb7d) !important;
            color: #4d2f12 !important;
            border: 1px solid rgba(129, 92, 42, 0.25) !important;
            border-radius: 999px !important;
            padding: 0.5rem 0.9rem !important;
            font-size: 0.80rem !important;
            font-weight: 700 !important;
            box-shadow: 0 6px 18px rgba(198, 143, 83, 0.2) !important;
        }

        .glass {
            background: rgba(255,255,255,0.56);
            border: 1px solid rgba(13, 146, 167, 0.12);
            border-radius: 18px;
            padding: 1.2rem 1.1rem;
            box-shadow: 0 10px 24px rgba(20, 111, 130, 0.08);
            height: 100%;
        }

        .metric-card {
            background: linear-gradient(180deg, rgba(255,255,255,0.7), rgba(204,251,255,0.5));
            border: 1px solid rgba(12, 135, 154, 0.12);
            border-radius: 18px;
            padding: 1.15rem 1rem;
            text-align: center;
            box-shadow: 0 8px 22px rgba(15, 118, 140, 0.07);
            height: 100%;
        }

        .metric-card .value {
            font-size: 2rem;
            font-weight: 800;
            color: #0f8894;
            margin: 0;
        }

        .metric-card .label {
            font-size: 0.85rem;
            color: #1b5360;
            margin-top: 0.3rem;
            font-weight: 600;
        }

        .section-title {
            color: #0c5964;
            font-size: 1.6rem;
            font-weight: 800;
            margin: 1.8rem 0 1rem 0;
        }

        .feature-box {
            background: rgba(255,255,255,0.65);
            border: 1px solid rgba(9, 129, 146, 0.10);
            border-radius: 18px;
            padding: 1.2rem;
            box-shadow: 0 12px 25px rgba(8, 106, 122, 0.06);
            height: 100%;
        }

        .feature-box h3 {
            color: #0e5a66;
            margin-top: 0.3rem;
            margin-bottom: 0.5rem;
        }

        .feature-box p {
            color: #3f5c63;
            line-height: 1.6;
            margin: 0;
        }

        .icon {
            font-size: 1.8rem;
            display: block;
            margin-bottom: 0.4rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">🌊 CUP OF THE ISLANDS</div>
        <h1>Il tuo torneo da sogno!</h1>
        <p>
            Organizza tornei, monitora i risultati e tieni sempre sotto controllo la classifica!
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

hero_labels = ["Tornei", "Classifiche", "Isole", "Eventi", "Crea", "Invita", "Info"]
hero_columns = st.columns(len(hero_labels))

for col, label in zip(hero_columns, hero_labels):
    with col:
        clicked = st.button(label, key=f"hero_{label.lower()}", use_container_width=True)
        if clicked and label == "Crea":
            st.session_state.show_create_menu = not st.session_state.show_create_menu
            st.session_state.active_hero_button = "Crea"
        elif clicked:
            st.session_state.active_hero_button = label

# Base panels
cols = st.columns(4)
metrics = [
    ("24", "Tornei attivi"),
    ("8.4k", "Partecipanti"),
    ("96%", "Engagement"),
    ("12", "Eventi in corso"),
]
for col, (value, label) in zip(cols, metrics):
    with col:
        st.markdown(
            f'<div class="metric-card"><div class="value">{value}</div><div class="label">{label}</div></div>',
            unsafe_allow_html=True,
        )

st.markdown('<div class="section-title">Cosa puoi fare</div>', unsafe_allow_html=True)
features = [
    ("🏆", "Tornei dinamici", "Crea competizioni personalizzate, impostando regole, date e gruppi di partecipazione in pochi secondi."),
    ("📊", "Classifiche live", "Segui i punteggi in tempo reale e scopri subito chi guida la classifica generale."),
    ("🎯", "Gestione eventi", "Organizza sfide, premi e momenti speciali per coinvolgere tutta la community."),
]
feature_cols = st.columns(3)
for col, (icon, title, text) in zip(feature_cols, features):
    with col:
        st.markdown(
            f"""
            <div class="feature-box">
                <span class="icon">{icon}</span>
                <h3>{title}</h3>
                <p>{text}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<div class="section-title">Panoramica</div>', unsafe_allow_html=True)
left, right = st.columns([1.2, 0.8])
with left:
    st.markdown(
        """
        <div class="glass">
            <h3 style="color:#0c5964; margin-top:0;">La tua isola, in ordine</h3>
            <p style="color:#3f5c63; line-height:1.7; margin:0;">
                Un sistema pensato per tenere organizzati tornei, classifiche e momenti speciali in un unico ambiente.
                Ogni sezione è progettata per essere chiara, veloce e adatta a chi vuole gestire tutto con pochi click.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with right:
    st.markdown(
        """
        <div class="glass">
            <h3 style="color:#0c5964; margin-top:0;">Stato</h3>
            <p style="color:#3f5c63; margin:0 0 0.5rem 0;">✅ Sistema operativo</p>
            <p style="color:#3f5c63; margin:0 0 0.5rem 0;">✅ Dashboard pronta</p>
            <p style="color:#3f5c63; margin:0;">✅ Tema turchese attivo</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

if st.session_state.active_hero_button == "Tornei":
    st.markdown('<div class="section-title">Tornei disponibili</div>', unsafe_allow_html=True)
    tournament_list = list(TOURNAMENTS.keys())
    selected_tournament = st.selectbox(
        "Seleziona un torneo",
        tournament_list,
        index=tournament_list.index(st.session_state.selected_tournament),
    )
    st.session_state.selected_tournament = selected_tournament

    st.markdown("<div style='margin-top: 1rem; color: #0c5964; font-weight: 700; font-size: 1.05rem;'>Partecipanti attivi</div>", unsafe_allow_html=True)
    for idx in range(12):
        slot = st.session_state.participant_slots[idx]
        checkbox_col, name_col = st.columns([0.3, 2.5])
        with checkbox_col:
            slot["selected"] = st.checkbox("", value=slot.get("selected", False), key=f"participant_selected_{idx}", label_visibility="collapsed")
        with name_col:
            slot["name"] = st.text_input(
                "",
                value=slot.get("name", f"Giocatore {idx + 1}"),
                key=f"participant_name_{idx}",
                placeholder=f"Partecipante {idx + 1}",
                label_visibility="collapsed",
            )

    active_participants = get_active_participants()

    if not active_participants:
        st.warning("Seleziona almeno un partecipante attivo per continuare.")
    else:
        st.session_state.selected_participant = st.selectbox(
            "Partecipante attivo",
            active_participants,
            index=active_participants.index(st.session_state.selected_participant) if st.session_state.selected_participant in active_participants else 0,
        )

        selected_name = st.session_state.selected_participant
        if selected_name not in st.session_state.capture_data:
            st.session_state.capture_data[selected_name] = build_capture_frame(st.session_state.selected_tournament)

        table = st.session_state.capture_data[selected_name].copy()
        table["Totale"] = table["Valore"] * table["Quantità"]
        edited = st.data_editor(
            table,
            use_container_width=True,
            hide_index=True,
            disabled=["Creatura", "Foto", "Valore", "Totale"],
            column_config={
                "Creatura": st.column_config.TextColumn("Creatura", width="large"),
                "Foto": st.column_config.TextColumn("Foto", width="small"),
                "Valore": st.column_config.NumberColumn("Valore", format="%d"),
                "Quantità": st.column_config.NumberColumn("Quantità", min_value=0, max_value=999),
                "Totale": st.column_config.NumberColumn("Totale", format="%d"),
            },
        )
        edited["Totale"] = edited["Valore"] * edited["Quantità"]
        st.session_state.capture_data[selected_name] = edited

        total_creature_count = int(edited["Quantità"].sum())
        total_points = int(edited["Totale"].sum())
        score_cols = st.columns(2)
        with score_cols[0]:
            st.metric("Totale creature prese", total_creature_count)
        with score_cols[1]:
            st.metric("Totale punti", total_points)

elif st.session_state.active_hero_button == "Classifiche":
    st.markdown('<div class="section-title">Classifica del torneo</div>', unsafe_allow_html=True)
    active_participants = get_active_participants()
    if not active_participants:
        st.warning("Nessun partecipante attivo. Seleziona i giocatori nel pannello Tornei.")
    else:
        leaderboard_rows = []
        for participant in active_participants:
            capture_df = st.session_state.capture_data.get(participant)
            if capture_df is None:
                capture_df = build_capture_frame(st.session_state.selected_tournament)
                st.session_state.capture_data[participant] = capture_df
            qty = int(capture_df["Quantità"].sum())
            total = int((capture_df["Valore"] * capture_df["Quantità"]).sum())
            leaderboard_rows.append({
                "Nome partecipante": participant,
                "Quantità": qty,
                "Totale punti": total,
            })

        leaderboard = pd.DataFrame(leaderboard_rows)
        leaderboard = leaderboard.sort_values(["Totale punti", "Quantità"], ascending=[False, False]).reset_index(drop=True)
        leaderboard.insert(0, "Posizione", range(1, len(leaderboard) + 1))
        st.dataframe(
            leaderboard[["Posizione", "Nome partecipante", "Quantità", "Totale punti"]],
            use_container_width=True,
            hide_index=True,
            column_config={
                "Posizione": st.column_config.NumberColumn("Posizione", format="%d"),
                "Nome partecipante": st.column_config.TextColumn("Nome partecipante"),
                "Quantità": st.column_config.NumberColumn("Quantità", format="%d"),
                "Totale punti": st.column_config.NumberColumn("Totale punti", format="%d"),
            },
        )

if st.session_state.show_create_menu:
    st.markdown('<div class="section-title">Crea nuova creatura</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="glass">
            <p style="color:#1f4f5d; font-weight:600; margin:0 0 0.7rem 0;">
                Aggiungi una foto e personalizza i punti! Fallo qui:
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    points_title = "<div style='margin-top: 1rem; color: #0c5964; font-weight: 700; font-size: 1.05rem;'>Valore Punti:</div>"
    st.markdown(points_title, unsafe_allow_html=True)

    points_col1, points_col2, points_col3 = st.columns([1, 2, 1])
    with points_col1:
        if st.button("-", key="decrease_points", use_container_width=True):
            st.session_state.creature_points = max(0, st.session_state.creature_points - 1)
    with points_col2:
        st.markdown(
            f"<div style='text-align:center; padding: 0.7rem 0; border-radius: 12px; background: rgba(255,255,255,0.7); border: 1px solid rgba(12,135,154,0.15); font-size: 2rem; font-weight: 800; color: #0c5964;'>{st.session_state.creature_points}</div>",
            unsafe_allow_html=True,
        )
    with points_col3:
        if st.button("+", key="increase_points", use_container_width=True):
            st.session_state.creature_points = st.session_state.creature_points + 1

    uploaded_file = st.file_uploader(
        "Carica foto PNG o JPEG",
        type=["png", "jpg", "jpeg"],
        help="Puoi caricare un'immagine della creatura da associare alla riga.",
    )

    if uploaded_file is not None:
        st.image(uploaded_file, caption=uploaded_file.name, width=220)

    if st.button("Aggiungi alla tabella in basso", use_container_width=True):
        new_row = {
            "Creatura": "Creatura personalizzata",
            "Punti": int(st.session_state.creature_points),
            "Foto": uploaded_file.name if uploaded_file is not None else "Nessuna foto",
        }
        st.session_state.creature_rows = pd.concat(
            [st.session_state.creature_rows, pd.DataFrame([new_row])],
            ignore_index=True,
        )
        st.success("Creatura aggiunta alla tabella!")
        st.session_state.creature_points = 1

    st.markdown('<div class="section-title">Tabella creatura</div>', unsafe_allow_html=True)
    st.dataframe(st.session_state.creature_rows, use_container_width=True, hide_index=True)

st.caption("Prototipo homepage - CUP OF THE ISLANDS")
