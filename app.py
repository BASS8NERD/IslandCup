Classifica_ordinata = sorted(
    classifica.items(), key=lambda x: x[1][0], reverse=True
)

for i, (nome_reale, (punti_totali, player_id)) in enumerate(
    classifica_ordinata, 1
):
    emoji = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "👤"
    if player_id == giocatore_utente:
        st.markdown(f"### 👉 {emoji} {i}° {nome_reale}: {punti_totali} PT")
    else:
        st.markdown(f"### {emoji} {i}° {nome_reale}: {punti_totali} PT")

st.write("---")
st.subheader("📝 Inserisci Catture")

# Gestione aggiornamento punteggio
def aggiorna_punteggio(g_id, c_idx, key):
    st.session_state.punteggi_giocatori[g_id][c_idx] = st.session_state[key]


# Generazione a SCHEDE VERTICALI (Card) usandi i container
for idx, creatura in enumerate(st.session_state.creature):
    with st.container(border=True):  # Usa i container nativi per le card
        if creatura["immagine"] is not None:
            try:
                st.image(creatura["immagine"], width=95)
            except Exception:
                st.write(f"🖼️ Creatura #{creatura['id']}")
        else:
            st.write(f"✨ #{creatura['id']}")

        quantita_corrente = st.session_state.punteggi_giocatori[
            giocatore_utente
        ][idx]
        totale_riga = creatura["punti"] * quantita_corrente
        st.markdown(
            f"Valore: {creatura['punti']} Pt | Totale: {totale_riga} Pt"
        )

        input_key = f"qta_{giocatore_utente}_{idx}"
        st.number_input(
            f"Quantità per #{creatura['id']}",
            min_value=0,
            value=quantita_corrente,
            key=input_key,
            label_visibility="collapsed",
            on_change=aggiorna_punteggio,  # Aggiorna lo stato in modo nativo
            args=(giocatore_utente, idx, input_key),
        )
