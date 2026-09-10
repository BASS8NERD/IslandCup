import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="CUP OF THE ISLANDS",
    page_icon="🌊",
    layout="wide",
)

if "show_create_menu" not in st.session_state:
    st.session_state.show_create_menu = False
if "creature_points" not in st.session_state:
    st.session_state.creature_points = 1
if "creature_rows" not in st.session_state:
    st.session_state.creature_rows = pd.DataFrame(columns=["Creatura", "Punti", "Foto"])

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

        .pill-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem;
            margin-top: 1.2rem;
        }

        .pill {
            display: inline-block;
            background: rgba(255,255,255,0.14);
            color: #ecfeff;
            border: 1px solid rgba(255,255,255,0.22);
            border-radius: 999px;
            padding: 0.45rem 0.9rem;
            font-size: 0.80rem;
            font-weight: 600;
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
        <div class="pill-row">
            <span class="pill">Tornei</span>
            <span class="pill">Classifiche</span>
            <span class="pill">Isole</span>
            <span class="pill">Eventi</span>
            <span class="pill">Invita</span>
            <span class="pill">Info</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
        div.stButton > button {
            background: rgba(255,255,255,0.14);
            color: #ecfeff;
            border: 1px solid rgba(255,255,255,0.22);
            border-radius: 999px;
            padding: 0.45rem 0.9rem;
            font-size: 0.80rem;
            font-weight: 600;
            box-shadow: none;
            margin-top: -0.65rem;
            margin-bottom: 1rem;
        }
        div.stButton > button:hover {
            background: rgba(255,255,255,0.22);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

if st.button("Crea", key="toggle_create_menu"):
    st.session_state.show_create_menu = not st.session_state.show_create_menu

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

cols = st.columns(3)
for col, (icon, title, text) in zip(cols, features):
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

if st.session_state.show_create_menu:
    st.markdown('<div class="section-title">Crea nuova creatura</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="glass">
            <p style="color:#1f4f5d; font-weight:600; margin:0 0 0.7rem 0;">
                Vuoi aggiungere a mano una foto o creare una riga personalizzata? Fallo qui:
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    option = st.radio(
        "Tipo di inserimento",
        ["Aggiungi foto", "Crea riga personalizzata"],
        horizontal=True,
        label_visibility="collapsed",
    )

    creature_name = st.text_input(
        "Nome creatura",
        placeholder="Es. Lince, Pipistrello, Anatra...",
    )

    st.markdown(
        "<div style='margin-top: 1rem; color: #0c5964; font-weight: 700; font-size: 1.05rem;'>Valore in Punti per questa creatura:</div>",
        unsafe_allow_html=True,
    )

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
        if creature_name.strip() == "":
            st.warning("Inserisci il nome della creatura prima di aggiungerla.")
        else:
            new_row = {
                "Creatura": creature_name.strip(),
                "Punti": int(st.session_state.creature_points),
                "Foto": uploaded_file.name if uploaded_file is not None else "Nessuna foto",
            }
            st.session_state.creature_rows = pd.concat(
                [st.session_state.creature_rows, pd.DataFrame([new_row])],
                ignore_index=True,
            )
            st.success("Creatura aggiunta alla tabella!")
            st.session_state.creature_points = 1
            creature_name = ""

    st.markdown('<div class="section-title">Tabella creatura</div>', unsafe_allow_html=True)
    st.dataframe(st.session_state.creature_rows, use_container_width=True, hide_index=True)

st.caption("Prototipo homepage - CUP OF THE ISLANDS")
