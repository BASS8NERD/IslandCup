import streamlit as st

st.set_page_config(
    page_title="Island Cup",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Chewy&family=Patrick+Hand&display=swap');

        html, body {
            margin: 0;
            padding: 0;
            background: #d8edf6;
            height: 100%;
        }

        .stApp {
            background: linear-gradient(#d8edf6 0%, #cfeaf5 100%);
        }

        .block-container {
            padding-top: 0 !important;
            padding-left: 0 !important;
            padding-right: 0 !important;
            max-width: 100% !important;
        }

        .page-wrap {
            width: 100%;
            min-height: 100vh;
            background: #d4edf4;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            padding: 0;
        }

        .top-strip {
            width: 100%;
            height: 34px;
            background: repeating-linear-gradient(
                90deg,
                #46a5d6 0 24px,
                #f3d778 24px 48px,
                #84d490 48px 72px,
                #e76b6b 72px 96px,
                #72c2d6 96px 120px,
                #f8c07a 120px 144px,
                #86d7a6 144px 168px,
                #d1a2e8 168px 192px,
                #75cbea 192px 216px,
                #f7da7e 216px 240px
            );
            border-bottom: 2px solid rgba(0, 0, 0, 0.08);
            box-shadow: inset 0 -1px 0 rgba(255, 255, 255, 0.4);
            opacity: 0.95;
        }

        .header {
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 36px;
            margin-bottom: 24px;
        }

        .title-box {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 22px;
            min-width: 620px;
            padding: 0 35px;
        }

        .palm {
            font-size: 46px;
            line-height: 1;
            display: inline-block;
            filter: drop-shadow(0 2px 0 rgba(0,0,0,0.65));
        }

        .title {
            font-family: 'Chewy', 'Comic Sans MS', cursive;
            color: #1f1f1f;
            font-size: 62px;
            letter-spacing: 2px;
            line-height: 1.1;
            text-shadow: 3px 3px 0 rgba(0,0,0,0.23);
            position: relative;
            white-space: nowrap;
        }

        .title::before {
            content: "";
            position: absolute;
            left: 0;
            right: 0;
            bottom: -4px;
            height: 2px;
            background: rgba(25, 25, 25, 0.18);
        }

        .menu-panel {
            width: min(94vw, 980px);
            margin: 0 auto 10px auto;
        }

        .menu-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .menu-item {
            display: flex;
            align-items: center;
            height: 58px;
            border-radius: 14px;
            background: rgba(255,255,255,0.24);
            border: 1px solid rgba(70, 80, 90, 0.1);
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.35);
            color: #1f2a2f;
            font-family: 'Patrick Hand', 'Segoe Print', cursive;
            font-size: 22px;
            font-weight: 700;
            letter-spacing: 1.2px;
            text-transform: uppercase;
            padding: 0 18px;
            text-decoration: none;
            user-select: none;
        }

        .menu-item .arrow {
            font-size: 24px;
            color: #2c2c2c;
            opacity: 0.85;
            margin-right: 14px;
        }

        .menu-item .icon {
            width: 28px;
            display: inline-flex;
            justify-content: center;
            align-items: center;
            font-size: 24px;
            margin-right: 12px;
        }

        .menu-item .label {
            line-height: 1;
            transform: translateY(1px);
        }

        .bottom-bar {
            width: min(94vw, 980px);
            margin: 18px auto 0 auto;
            background: rgba(134, 201, 224, 0.25);
            border-top: 1px solid rgba(60, 90, 100, 0.14);
            border-bottom: 1px solid rgba(60, 90, 100, 0.14);
            min-height: 58px;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 0 18px;
            text-align: center;
            color: #1f2a2f;
            font-family: 'Patrick Hand', 'Segoe Print', cursive;
            font-size: 28px;
            line-height: 1.2;
        }

        .bottom-bar .mini-icon {
            font-size: 30px;
            margin-right: 10px;
        }

        .bottom-bar strong {
            font-weight: 700;
        }

        @media (max-width: 700px) {
            .title-box {
                min-width: 0;
                gap: 12px;
                flex-wrap: wrap;
            }

            .title {
                font-size: 40px;
            }

            .palm {
                font-size: 32px;
            }

            .menu-item {
                font-size: 18px;
                height: 52px;
            }

            .bottom-bar {
                font-size: 20px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="page-wrap">
        <div class="top-strip"></div>

        <div class="header">
            <div class="title-box">
                <span class="palm">🌴</span>
                <span class="title">ISLAND CUP</span>
                <span class="palm">🌴</span>
            </div>
        </div>

        <div class="menu-panel">
            <div class="menu-list">
                <div class="menu-item">
                    <span class="arrow">›</span>
                    <span class="icon">🏆</span>
                    <span class="label">TORNEO SALVATO</span>
                </div>

                <div class="menu-item">
                    <span class="arrow">›</span>
                    <span class="icon">🏅</span>
                    <span class="label">TORNEI ISOLANI</span>
                </div>

                <div class="menu-item">
                    <span class="arrow">›</span>
                    <span class="icon">🎮</span>
                    <span class="label">ISOLANI</span>
                </div>

                <div class="menu-item">
                    <span class="arrow">›</span>
                    <span class="icon">⚙️</span>
                    <span class="label">TORNEO FAI DA TE</span>
                </div>
            </div>
        </div>

        <div class="bottom-bar">
            <span class="mini-icon">🏆</span>
            <span>Apri il pannello <strong>TORNEI ISOLANI</strong> in alto per iniziare!</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
