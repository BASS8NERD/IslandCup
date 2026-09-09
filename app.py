import streamlit as st

# Impostiamo il layout largo per farci stare la tabella e la classifica affiancate
st.set_page_config(page_title="Island Cup Tracker", page_icon="🏝️", layout="wide")

# --- TITOLO CENTRATO ---
st.markdown("<h1 style='text-align: center;'>🏝️ Island Cup - Tabellone di Gara</h1>", unsafe_allow_html=True)
st.write("---")

# 1. DATABASE DELLE CREATURE (Inizia completamente vuoto)
if "creature" not in st.session_state:
    st.session_state.creature = []

# 2. INIZIALIZZAZIONE DEI 12 GIOCATORI
if "nomi_giocatori" not in st.session_state:
    st.session_state.nomi_giocatori = {f"Player {i}": f"Player {i}" for i in range(1, 13)}

# Inizializziamo il dizionario dei punteggi
if "punteggi_giocatori" not in st.session_state:
    st.session_state.punteggi_giocatori = {f"Player {i}": [] for i in range(1, 13)}

# --- PANNELLO DI CONFIGURAZIONE (NOMI E CREAZIONE CREATURE) ---
col_setup_nomi, col_setup_creature = st.columns(2)

with col_setup_nomi:
    with st.expander("⚙️ Gestione Nomi Giocatori"):
        cols_nomi = st.columns(3)
        for i in range(1, 13):
            id_player = f"Player {i}"
            with cols_nomi[(i-1) % 3]:
                nuovo_nome = st.text_input(f"Nome per {id_player}:", value=st.session_state.nomi_giocatori[id_player], key=f"edit_{id_player}")
                if nuovo_nome.strip():
                    st.session_state.nomi_giocatori[id_player] = nuovo_nome.strip()

with col_setup_creature:
    with st.expander("➕ Inserisci Creatura nel Torneo"):
        st.write("Imposta i punti e carica la foto dal tuo PC:")
        
        # Solo punti e file, nessun identificativo di testo!
        punti_nuova_creatura = st.number_input("Valore in Punti:", min_value=0, max_value=100, value=2, key="nuovi_punti_c")
        file_foto_nuovo = st.file_uploader("Carica Foto dal PC:", type=["png", "jpg", "jpeg"], key="nuovo_upload_c")
        
        if st.button("✨ AGGIUNGI ALLA TABELLA", use_container_width=True):
            # Genera un ID numerico progressivo interno automatico
            nuovo_id = len(st.session_state.creature) + 1
            
            # Aggiungiamo la creatura al database
            st.session_state.creature.append({
                "id": नया_id if 'नया_id' in locals() else nuovo_id,
                "punti": punti_nuova_creatura,
                "immagine": file_foto_nuovo
            })
            
            # Aggiungiamo uno slot a '0' quantità per tutti e 12 i giocatori
            for player_id in st.session_state.punteggi_giocatori:
                st.session_state.punteggi_giocatori[player_id].append(0)
                
            st.success("✅ Nuova riga aggiunta al tabellone!")
            st.rarun() if 'st.rarun' in locals() else st.rerun()

st.write("---")

# --- SCHERMATA PRINCIPALE ---
col_griglia, col_classifica = st.columns([3, 1.5], gap="large")

with col_griglia:
    st.subheader("📝 Registro delle Catture")
    
    opzioni_menu = {id_p: nome_p for id_p, nome_p in st.session_state.nomi_giocatori.items()}
    giocatore_attivo_id = st.selectbox(
        "Seleziona il Giocatore da aggiornare:", 
        list(opzioni_menu.keys()),
        format_func=lambda x: opzioni_menu[x]
    )
    
    nome_visualizzato = st.session_state.nomi_giocatori[giocatore_attivo_id]
    st.write(f"### Inserimento dati per: **{nome_visualizzato}**")
    st.write("---")

    if not st.session_state.creature:
        st.info("👋 Il tabellone è vuoto. Apri il pannello in alto a destra '➕ Inserisci Creatura nel Torneo' per aggiungere la tua prima foto!")
    else:
        # INTESTAZIONE DELLA TABELLA COMPATTA
        col_img_h, col_val_h, col_qta_h, col_tot_h = st.columns([1.5, 1.5, 2, 1.5])
        col_img_h.write("**Creatura (Foto)**")
        col_val_h.write("**Valore**")
        col_qta_h.write("**Quantità**")
        col_tot_h.write("**Totale**")
        st.write("---")

        # Generazione della griglia basata solo sulle foto e sui punti
        for idx, creatura in enumerate(st.session_state.creature):
            col_img, col_val, col_qta, col_tot = st.columns([1.5, 1.5, 2, 1.5])
            
            # COLONNA 1: IMMAGINE PROTETTA DA CRASH
            with col_img:
                if creatura["immagine"] is not None:
                    try:
                        st.image(creatura["immagine"], width=55)
                    except Exception:
                        # Se il PC dà l'errore NumPy, mostra questa icona sicura senza bloccarsi
                        st.write(f"🖼️ Rigal #{creatura['id']}" if 'Rigal' in locals() else f"🖼️ Riga #{creatura['id']}")
                else:
                    st.write(f"✨ #{creatura['id']}")

            # COLONNA 2: VALORE IN PUNTI
            with col_val:
                st.write(f"{creatura['punti']} Pt")
                
            # COLONNA 3: INPUT QUANTITÀ
            with col_qta:
                quantita_corrente = st.session_state.punteggi_giocatori[giocatore_attivo_id][idx]
                nuova_qta = st.number_input(
                    f"Q.tà {creatura['id']}", 
                    min_value=0, 
                    value=quantita_corrente, 
                    key=f"qta_{giocatore_attivo_id}_{creatura['id']}",
                    label_visibility="collapsed"
                )
                st.session_state.punteggi_giocatori[giocatore_attivo_id][idx] = nuova_qta
                
            # COLONNA 4: CALCOLO TOTALI
            totale_riga = creatura["punti"] * nuova_qta
            with col_tot:
                st.write(f"**{totale_riga} Pt**")

with col_classifica:
    st.subheader("🏆 Classifica Live")
    
    classifica = {}
    for player_id, lista_qta in st.session_state.punteggi_giocatori.items():
        totale_player = sum(st.session_state.creature[i]["punti"] * lista_qta[i] for i in range(len(st.session_state.creature)))
        nome_reale = st.session_state.nomi_giocatori[player_id]
        classifica[nome_reale] = (totale_player, player_id)
        
    classifica_ordinata = sorted(classifica.items(), key=lambda x: x, reverse=True)
    
    for i, (nome_reale, (punti_totali, player_id)) in enumerate(classifica_ordinata, 1):
        emoji = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "👤"
        if player_id == giocatore_attivo_id:
            st.markdown(f"👉 **{emoji} {i}° {nome_reale}: {punti_totali} PT**")
        else:
            st.write(f"{emoji} {i}° {nome_reale}: {punti_totali} PT")
