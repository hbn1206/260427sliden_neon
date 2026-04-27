import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="🎉 응원 문구",
    page_icon="📣",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 배경색별 최적 글자색 매핑
COLOR_SCHEMES = {
    "🖤 검정": {"bg": "#000000", "text": "#FFFFFF", "neon": "#00FFFF"},
    "❤️ 빨강": {"bg": "#FF0000", "text": "#FFFF00", "neon": "#FFFF00"},
    "💙 파랑": {"bg": "#0000FF", "text": "#FFFFFF", "neon": "#00FF00"},
    "💚 초록": {"bg": "#008000", "text": "#FFFFFF", "neon": "#FF69B4"},
    "💜 보라": {"bg": "#800080", "text": "#00FFFF", "neon": "#00FFFF"},
    "🤍 흰색": {"bg": "#FFFFFF", "text": "#FF1493", "neon": "#FF1493"},
}

# 샘플 문구
SAMPLE_MESSAGES = {
    "직접 입력": "",
    "에듀테크AI(고) 분임 - 화이팅!": "에듀테크AI(고) 분임 화이팅! 💪🔥",
    "에듀테크AI(고) 분임 - 최고!": "에듀테크AI(고) 분임 최고! 🏆✨",
    "에듀테크AI(고) 분임 - 응원": "에듀테크AI(고) 분임 우리가 응원합니다! 📣💖",
    "수학 분임 - 화이팅!": "수학 분임 화이팅! 💪🔥",
    "수학 분임 - 최고!": "수학 분임 최고! 🏆✨",
    "수학 분임 - 응원": "수학 분임 우리가 응원합니다! 📣💖",
}

# 세션 상태 초기화
if "show_fullscreen" not in st.session_state:
    st.session_state.show_fullscreen = False

def main():
    # 전체화면 모드가 아닐 때 - 설정 화면 표시
    if not st.session_state.show_fullscreen:
        show_settings_page()
    else:
        show_fullscreen_page()

def show_settings_page():
    """설정 페이지 표시"""
    st.title("🎉 응원 문구 만들기")
    st.markdown("---")

    # 사이드바 설정
    with st.sidebar:
        st.header("⚙️ 설정")

        # 샘플 문구 선택
        st.subheader("📝 문구 선택")
        selected_sample = st.selectbox(
            "샘플 문구 선택",
            list(SAMPLE_MESSAGES.keys()),
            label_visibility="collapsed"
        )

        # 직접 입력
        if selected_sample == "직접 입력":
            custom_message = st.text_area(
                "✏️ 직접 입력",
                placeholder="응원 문구를 입력하세요...",
                height=100
            )
            message = custom_message if custom_message else "화이팅! 💪"
        else:
            message = SAMPLE_MESSAGES[selected_sample]

        st.markdown("---")

        # 배경색 선택
        st.subheader("🎨 배경색 선택")
        bg_color = st.selectbox(
            "배경색",
            list(COLOR_SCHEMES.keys()),
            label_visibility="collapsed"
        )

        st.markdown("---")

        # 효과 선택
        st.subheader("✨ 효과 선택")
        use_neon = st.checkbox("💡 네온싸인 효과", value=True)
        use_slide = st.checkbox("🎬 슬라이드 효과", value=False)

        st.markdown("---")

        # 전체화면 버튼
        if st.button("📺 전체화면으로 보기", use_container_width=True, type="primary"):
            st.session_state.show_fullscreen = True
            st.session_state.message = message
            st.session_state.bg_color = bg_color
            st.session_state.use_neon = use_neon
            st.session_state.use_slide = use_slide
            st.rerun()

    # 메인 영역 - 미리보기
    st.subheader("👀 미리보기")

    colors = COLOR_SCHEMES[bg_color]

    # 미리보기 스타일
    preview_style = f"""
    <div style="
        background-color: {colors['bg']};
        color: {colors['text']};
        padding: 60px 20px;
        border-radius: 20px;
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        margin: 20px 0;
        min-height: 200px;
        display: flex;
        align-items: center;
        justify-content: center;
        {"text-shadow: 0 0 10px " + colors['neon'] + ", 0 0 20px " + colors['neon'] + ", 0 0 30px " + colors['neon'] + ";" if use_neon else ""}
    ">
        {message}
    </div>
    """
    st.markdown(preview_style, unsafe_allow_html=True)

    # 사용 안내
    st.markdown("---")
    st.info("👈 왼쪽 사이드바에서 옵션을 선택한 후 **[📺 전체화면으로 보기]** 버튼을 클릭하세요!")

def show_fullscreen_page():
    """전체화면 페이지 표시"""

    # 저장된 설정 불러오기
    message = st.session_state.get("message", "화이팅! 💪")
    bg_color = st.session_state.get("bg_color", "🖤 검정")
    use_neon = st.session_state.get("use_neon", True)
    use_slide = st.session_state.get("use_slide", False)

    colors = COLOR_SCHEMES[bg_color]

    # 뒤로가기 버튼 (상단에 작게)
    col1, col2, col3 = st.columns([1, 6, 1])
    with col1:
        if st.button("⬅️ 뒤로", key="back_btn"):
            st.session_state.show_fullscreen = False
            st.rerun()

    # 애니메이션 CSS
    if use_slide:
        animation_css = f"""
        @keyframes slideRightToLeft {{
            0% {{ transform: translateX(100%); }}
            100% {{ transform: translateX(-100%); }}
        }}
        .message-text {{
            animation: slideRightToLeft 15s linear infinite;
            white-space: nowrap;
        }}
        """
    else:
        animation_css = ""

    if use_neon:
        neon_css = f"""
        @keyframes neonGlow {{
            0%, 100% {{ 
                text-shadow: 0 0 10px {colors['neon']}, 
                             0 0 20px {colors['neon']}, 
                             0 0 30px {colors['neon']}, 
                             0 0 40px {colors['neon']};
            }}
            50% {{ 
                text-shadow: 0 0 20px {colors['neon']}, 
                             0 0 40px {colors['neon']}, 
                             0 0 60px {colors['neon']}, 
                             0 0 80px {colors['neon']};
            }}
        }}
        .message-text {{
            animation: {"slideRightToLeft 15s linear infinite, " if use_slide else ""}neonGlow 1.5s ease-in-out infinite;
        }}
        """
    else:
        neon_css = ""

    # 전체화면 스타일
    fullscreen_html = f"""
    <style>
        /* Streamlit 기본 요소 숨기기 */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        .stApp > header {{display: none;}}

        {animation_css}
        {neon_css}

        .fullscreen-container {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-color: {colors['bg']};
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 9999;
            overflow: hidden;
        }}

        .message-text {{
            color: {colors['text']};
            font-size: 8vw;
            font-weight: bold;
            text-align: center;
            padding: 20px;
            {"white-space: nowrap;" if use_slide else ""}
        }}

        /* 모바일 최적화 */
        @media (max-width: 768px) {{
            .message-text {{
                font-size: 10vw;
            }}
        }}
    </style>

    <div class="fullscreen-container">
        <div class="message-text">{message}</div>
    </div>
    """

    st.markdown(fullscreen_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
