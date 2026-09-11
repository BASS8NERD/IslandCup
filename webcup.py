import io

import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="CUP OF THE ISLANDS",
    page_icon="🌊",
    layout="wide",
)

GITHUB_RAW_BASE = "https://raw.githubusercontent.com/BASS8NERD/IslandCup/main"

POINTS_BY_IMAGE = {
    1: 2,
    2: 2,
    3: 3,
    4: 9,
    5: 3,
    6: 4,
    7: 6,
    8: 2,
    9: 3,
    10: 3,
    11: 6,
    12: 4,
    13: 4,
    14: 4,
    15: 4,
    16: 4,
    17: 6,
    18: 9,
    19: 6,
    20: 5,
    21: 7,
    22: 9,
    23: 4,
    24: 6,
    25: 6,
    26: 8,
    27: 9,
    28: 2,
    29: 8,
    30: 6,
    31: 4,
    32: 6,
    33: 6,
    34: 7,
    35: 9,
    36: 5,
    37: 5,
    38: 4,
    39: 3,
    40: 7,
}

MARINE_CREATURES = [
    {"Foto": f"{GITHUB_RAW_BASE}/{image_number}.png", "Valore": POINTS_BY_IMAGE[image_number]}
    for image_number in range(1, 41)
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
if "creature_points" not in st.session_state:
    st.session_state.creature_points = 1
if "creature_rows" not in st.session_state:
    st.session_state.creature_rows = pd.DataFrame(columns=["Foto", "Valore", "Quantità", "Totale"])
if "active_hero_button" not in st.session_state:
    st.session_state.active_hero_button = ""
if "selected_tournament" not in st.session_state:
    st.session_state.selected_tournament = "Torneo Creature Marine"
if "custom_tournament_rows" not in st.session_state:
    st.session_state.custom_tournament_rows = pd.DataFrame(columns=["Foto", "Valore", "Quantità", "Totale"])
if "participant_slots" not in st.session_state:
    st.session_state.participant_slots = [
        {"selected": False, "name": ""}
        for _ in range(12)
    ]
if "selected_participant" not in st.session_state:
    st.session_state.selected_participant = ""
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
    for index, item in enumerate(TOURNAMENTS.get(tournament_name, []), start=1):
        rows.append({
            "Creatura": item.get("Creatura", f"Creatura {index}"),
            "Foto": item.get("Foto", ""),
            "Valore": int(item.get("Valore", 0)),
            "Quantità": 0,
            "Totale": 0,
        })
    return pd.DataFrame(rows)


def make_image_cell(uploaded_file):
    if uploaded_file is None:
        return ""
    try:
        return uploaded_file.getvalue()
    except Exception:
        return str(uploaded_file)


def make_custom_rows_from_uploaded(uploaded_files, points):
    rows = []
    for uploaded_file in uploaded_files or []:
        if uploaded_file is not None:
            rows.append({
                "Foto": make_image_cell(uploaded_file),
                "Valore": int(points),
                "Quantità": 0,
                "Totale": 0,
            })
    return pd.DataFrame(rows, columns=["Foto", "Valore", "Quantità", "Totale"])


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

        .score-box {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            background: linear-gradient(180deg, rgba(255,255,255,0.8), rgba(210,247,250,0.8));
            border: 1px solid rgba(12, 135, 154, 0.14);
            border-radius: 18px;
            padding: 1rem 0.75rem;
            box-shadow: 0 10px 22px rgba(18, 123, 140, 0.08);
            margin-top: 1rem;
            min-height: 120px;
            text-align: center;
        }

        .score-box .value {
            font-size: 2.1rem;
            font-weight: 800;
            color: #0d6d7b;
            line-height: 1.1;
        }

        .score-box .label {
            font-size: 0.82rem;
            color: #285863;
            font-weight: 700;
            margin-top: 0.4rem;
            letter-spacing: 0.02em;
        }

        div[data-testid="stExpander"] {
            border: 1px solid rgba(12, 135, 154, 0.18) !important;
            border-radius: 18px !important;
            background: rgba(255,255,255,0.60) !important;
            box-shadow: 0 12px 24px rgba(20, 111, 130, 0.06) !important;
            overflow: hidden !important;
        }

        div[data-testid="stExpander"] > div {
            background: transparent !important;
        }

        div[data-testid="stDataFrame"],
        div[data-testid="stTable"] {
            overflow-x: auto !important;
            overflow-y: visible !important;
            max-height: none !important;
            height: auto !important;
            width: 100% !important;
        }

        div[data-testid="stDataFrame"] > div,
        div[data-testid="stTable"] > div {
            overflow: visible !important;
        }

        @media (max-width: 768px) {
            div[data-testid="stDataFrame"],
            div[data-testid="stTable"] {
                font-size: 0.82rem !important;
            }
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

hero_labels = ["Tornei", "Classifiche", "Isole", "Eventi", "Invita", "Info"]
hero_columns = st.columns(len(hero_labels))

for col, label in zip(hero_columns, hero_labels):
    with col:
        clicked = st.button(label, key=f"hero_{label.lower()}", use_container_width=True)
        if clicked:
            st.session_state.active_hero_button = label

if st.session_state.active_hero_button == "Info":
    st.markdown('<div class="section-title">Cosa puoi fare</div>', unsafe_allow_html=True)
    features = [
        ("🏆", "Tornei dinamici", "Crea competizioni personalizzate, impostando regole, date e gruppi di partecipazione in pochi secondi."),
        ("📊", "Classifiche live", "Segui i punteggi in tempo reale e scopri subito chi guida la classifica generale."),
    ]
    feature_cols = st.columns(2)
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

if st.session_state.active_hero_button == "Tornei":
    st.markdown('<div class="section-title">Tornei disponibili</div>', unsafe_allow_html=True)
    tournament_list = list(TOURNAMENTS.keys())
    selected_tournament = st.selectbox(
        "Seleziona un torneo",
        tournament_list,
        index=tournament_list.index(st.session_state.selected_tournament) if st.session_state.selected_tournament in tournament_list else 0,
    )
    st.session_state.selected_tournament = selected_tournament

    if selected_tournament == "Torneo Fai Da Te":
        st.markdown(
            """
            <div class="glass">
                <p style="color:#1f4f5d; font-weight:600; margin:0 0 0.7rem 0;">
                    Carica immagini, imposta il valore e scegli chi partecipa al torneo personalizzato.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        uploaded_files = st.file_uploader(
            "Carica foto PNG o JPEG",
            type=["png", "jpg", "jpeg"],
            accept_multiple_files=True,
            help="Puoi caricare più immagini e aggiungerle alla tabella del torneo.",
        )

        if uploaded_files:
            for uploaded_file in uploaded_files:
                if uploaded_file is not None:
                    st.image(uploaded_file, caption=uploaded_file.name, width=120)

        points_title = "<div style='margin-top: 1rem; color: #0c5964; font-weight: 700; font-size: 1.05rem;'>Valore Punti:</div>"
        st.markdown(points_title, unsafe_allow_html=True)

        points_col1, points_col2, points_col3 = st.columns([1, 2, 1])
        with points_col1:
            if st.button("-", key="custom_decrease_points", use_container_width=True):
                st.session_state.creature_points = max(0, st.session_state.creature_points - 1)
        with points_col2:
            st.markdown(
                f"<div style='text-align:center; padding: 0.7rem 0; border-radius: 12px; background: rgba(255,255,255,0.7); border: 1px solid rgba(12,135,154,0.15); font-size: 2rem; font-weight: 800; color: #0c5964;'>{st.session_state.creature_points}</div>",
                unsafe_allow_html=True,
            )
        with points_col3:
            if st.button("+", key="custom_increase_points", use_container_width=True):
                st.session_state.creature_points = st.session_state.creature_points + 1

        if uploaded_files and st.session_state.creature_points > 0 and st.session_state.custom_tournament_rows.empty:
            st.session_state.custom_tournament_rows = make_custom_rows_from_uploaded(uploaded_files, st.session_state.creature_points)

        if st.button("Aggiungi alla tabella in basso", use_container_width=True):
            new_rows = make_custom_rows_from_uploaded(uploaded_files, st.session_state.creature_points)
            if not new_rows.empty:
                st.session_state.custom_tournament_rows = pd.concat(
                    [st.session_state.custom_tournament_rows, new_rows],
                    ignore_index=True,
                )
                st.success("Immagini aggiunte alla tabella del torneo personalizzato!")
                st.session_state.creature_points = 1

        with st.expander("Partecipanti", expanded=False):
            st.markdown(
                "<div style='padding: 0.25rem 0 0.75rem 0; color: #1d5662; font-weight: 700;'>Seleziona i partecipanti attivi</div>",
                unsafe_allow_html=True,
            )
            for idx in range(12):
                slot = st.session_state.participant_slots[idx]
                checkbox_col, name_col = st.columns([0.35, 2.6])
                with checkbox_col:
                    slot["selected"] = st.checkbox("", value=slot.get("selected", False), key=f"custom_participant_selected_{idx}", label_visibility="collapsed")
                with name_col:
                    slot["name"] = st.text_input(
                        "",
                        value=slot.get("name", ""),
                        key=f"custom_participant_name_{idx}",
                        placeholder=f"Partecipante {idx + 1}",
                        label_visibility="collapsed",
                    )

        custom_table = st.session_state.custom_tournament_rows.copy()
        if not custom_table.empty:
            custom_table["Totale"] = custom_table["Valore"] * custom_table["Quantità"]
            custom_table = custom_table[["Foto", "Valore", "Quantità", "Totale"]]
            st.session_state.custom_tournament_rows = custom_table
            st.table(custom_table)

    with st.expander("Partecipanti", expanded=False):
        st.markdown(
            "<div style='padding: 0.25rem 0 0.75rem 0; color: #1d5662; font-weight: 700;'>Seleziona i partecipanti attivi</div>",
            unsafe_allow_html=True,
        )
        for idx in range(12):
            slot = st.session_state.participant_slots[idx]
            checkbox_col, name_col = st.columns([0.35, 2.6])
            with checkbox_col:
                slot["selected"] = st.checkbox("", value=slot.get("selected", False), key=f"participant_selected_{idx}", label_visibility="collapsed")
            with name_col:
                slot["name"] = st.text_input(
                    "",
                    value=slot.get("name", ""),
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
            table[["Foto", "Valore", "Quantità", "Totale"]].copy(),
            hide_index=True,
            num_rows="fixed",
            use_container_width=True,
            disabled=["Totale"],
            column_config={
                "Foto": st.column_config.ImageColumn(
                    "Foto",
                    width="small",
                    help="Miniatura dell'esemplare",
                ),
                "Valore": st.column_config.NumberColumn(
                    "Valore",
                    min_value=0,
                    step=1,
                    format="%d",
                ),
                "Quantità": st.column_config.NumberColumn(
                    "Quantità",
                    min_value=0,
                    step=1,
                    format="%d",
                ),
                "Totale": st.column_config.NumberColumn(
                    "Totale",
                    min_value=0,
                    step=1,
                    format="%d",
                    disabled=True,
                ),
            },
            key=f"editor_{selected_name}_{st.session_state.selected_tournament}".replace(" ", "_"),
        )
        edited["Totale"] = edited["Valore"] * edited["Quantità"]
        st.session_state.capture_data[selected_name] = edited

        total_creature_count = int(edited["Quantità"].sum())
        total_points = int(edited["Totale"].sum())
        qty_col, total_col = st.columns(2)
        with qty_col:
            st.markdown(
                f"""
                <div class="score-box">
                    <div class="value">{total_creature_count}</div>
                    <div class="label">Totale creature prese</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with total_col:
            st.markdown(
                f"""
                <div class="score-box">
                    <div class="value">{total_points}</div>
                    <div class="label">Totale punti</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

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
        leaderboard_display = leaderboard[["Posizione", "Nome partecipante", "Quantità", "Totale punti"]].copy()
        leaderboard_display["Totale punti"] = leaderboard_display["Totale punti"].map(int)
        st.table(leaderboard_display)

elif st.session_state.active_hero_button == "Eventi":
    st.markdown('<div class="section-title">Eventi</div>', unsafe_allow_html=True)
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
    st.info("Qui potrai creare e gestire gli eventi del torneo.")

st.caption("Prototipo homepage - CUP OF THE ISLANDS")
