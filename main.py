
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="🎉 응원 문구",
    page_icon="📣",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 세션 상태 초기화
if 'fullscreen_mode' not in st.session_state:
    st.session_state.fullscreen_mode = False

# 배경색별 글자색 매핑 (눈에 잘 띄는 조합)
COLOR_MAPPING = {
    "🖤 검정": {"bg": "#000000", "text": "#FFFFFF", "neon": "#00FFFF"},
    "❤️ 빨강": {"bg": "#DC143C", "text": "#FFFF00", "neon": "#FFFF00"},
    "💙 파랑": {"bg": "#0066CC", "text": "#FFFFFF", "neon": "#00FF00"},
    "💚 초록": {"bg": "#228B22", "text": "#FFFFFF", "neon": "#FF69B4"},
    "💜 보라": {"bg": "#8B008B", "text": "#00FFFF", "neon": "#00FFFF"},
    "🤍 흰색": {"bg": "#FFFFFF", "text": "#FF1493", "neon": "#FF1493"},
}

# 샘플 문구
SAMPLE_MESSAGES = {
    "직접 입력": "",
    "에듀테크AI(고) 분임 - 화이팅": "🔥 에듀테크AI(고) 분임 화이팅! 🔥",
    "에듀테크AI(고) 분임 - 최고": "⭐ 에듀테크AI(고) 분임 최고! ⭐",
    "에듀테크AI(고) 분임 - 응원": "📣 에듀테크AI(고) 분임 힘내세요! 📣",
    "수학 분임 - 화이팅": "🔥 수학 분임 화이팅! 🔥",
    "수학 분임 - 최고": "⭐ 수학 분임 최고! ⭐",
    "수학 분임 - 응원": "📣 수학 분임 힘내세요! 📣",
}

def get_display_style(bg_color, text_color, neon_color, use_neon, use_slide):
    """효과에 따른 CSS 스타일 생성"""

    neon_effect = ""
    if use_neon:
        neon_effect = f"""
            text-shadow: 
                0 0 10px {neon_color},
                0 0 20px {neon_color},
                0 0 40px {neon_color},
                0 0 80px {neon_color};
            animation: neon-flicker 1.5s infinite alternate;
        """

    slide_effect = ""
    slide_keyframes = ""
    if use_slide:
        slide_effect = "animation: slide-right-to-left 15s linear infinite;"
        slide_keyframes = """
            @keyframes slide-right-to-left {
                0% { transform: translateX(100%); }
                100% { transform: translateX(-100%); }
            }
        """

    return f"""
        <style>
            @keyframes neon-flicker {{
                0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {{
                    opacity: 1;
                }}
                20%, 24%, 55% {{
                    opacity: 0.8;
                }}
            }}
            {slide_keyframes}

            .fullscreen-container {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                background-color: {bg_color};
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 9999;
                overflow: hidden;
                cursor: pointer;
            }}

            .cheer-text {{
                font-size: 15vw;
                font-weight: bold;
                color: {text_color};
                text-align: center;
                white-space: nowrap;
                {neon_effect}
                {slide_effect}
            }}

            .back-button {{
                position: fixed;
                top: 20px;
                left: 20px;
                z-index: 10001;
                background: rgba(255,255,255,0.2);
                border: 2px solid {text_color};
                color: {text_color};
                padding: 15px 25px;
                font-size: 20px;
                border-radius: 10px;
                cursor: pointer;
                transition: all 0.3s;
            }}

            .back-button:hover {{
                background: rgba(255,255,255,0.4);
                transform: scale(1.1);
            }}

            .touch-hint {{
                position: fixed;
                bottom: 30px;
                left: 50%;
                transform: translateX(-50%);
                z-index: 10001;
                color: {text_color};
                font-size: 16px;
                opacity: 0.7;
                text-align: center;
            }}

            .preview-box {{
                background-color: {bg_color};
                padding: 60px 40px;
                border-radius: 20px;
                text-align: center;
                margin: 20px 0;
                min-height: 200px;
                display: flex;
                justify-content: center;
                align-items: center;
                overflow: hidden;
            }}

            .preview-text {{
                font-size: 3rem;
                font-weight: bold;
                color: {text_color};
                white-space: nowrap;
                {neon_effect}
                {slide_effect if use_slide else ""}
            }}

            /* Streamlit 기본 요소 숨기기 (전체화면 모드) */
            .fullscreen-mode header,
            .fullscreen-mode .stSidebar,
            .fullscreen-mode .stApp > div:first-child {{
                display: none !important;
            }}
        </style>
    """

def show_fullscreen(message, colors, use_neon, use_slide):
    """전체화면 표시 - 터치하면 돌아가기"""
    bg_color = colors["bg"]
    text_color = colors["text"]
    neon_color = colors["neon"]

    style = get_display_style(bg_color, text_color, neon_color, use_neon, use_slide)

    # 화면 터치 시 초기화면으로 돌아가는 JavaScript
    touch_script = """
        <script>
            // 컨테이너 클릭 시 돌아가기
            document.addEventListener('DOMContentLoaded', function() {
                const container = document.querySelector('.fullscreen-container');
                if (container) {
                    container.addEventListener('click', function(e) {
                        // 뒤로가기 버튼 클릭은 제외 (버튼은 별도 처리)
                        if (!e.target.classList.contains('back-button')) {
                            window.parent.postMessage({type: 'streamlit:setComponentValue', value: true}, '*');
                            // 페이지 리로드로 초기화
                            window.location.href = window.location.href.split('?')[0] + '?back=true';
                        }
                    });
                }
            });

            // 터치 이벤트도 처리
            document.addEventListener('touchstart', function(e) {
                const container = document.querySelector('.fullscreen-container');
                if (container && container.contains(e.target)) {
                    if (!e.target.classList.contains('back-button')) {
                        window.location.href = window.location.href.split('?')[0] + '?back=true';
                    }
                }
            });
        </script>
    """

    fullscreen_html = f"""
        {style}
        {touch_script}
        <div class="fullscreen-container">
            <div class="cheer-text">{message}</div>
        </div>
        <div class="touch-hint">👆 화면을 터치하면 설정 화면으로 돌아갑니다</div>
    """

    st.markdown(fullscreen_html, unsafe_allow_html=True)

    # 뒤로가기 버튼도 유지
    col1, col2, col3 = st.columns([1, 6, 1])
    with col1:
        if st.button("⬅️ 뒤로", key="back_btn", type="primary"):
            st.session_state.fullscreen_mode = False
            st.rerun()

def show_settings():
    """설정 화면 표시"""

    st.title("🎉 응원 문구 만들기")
    st.markdown("---")

    # 사이드바 설정
    with st.sidebar:
        st.header("⚙️ 설정")

        # 1. 문구 선택
        st.subheader("📝 문구 선택")
        selected_sample = st.selectbox(
            "샘플 문구 선택",
            options=list(SAMPLE_MESSAGES.keys()),
            index=0
        )

        if selected_sample == "직접 입력":
            custom_message = st.text_input(
                "응원 문구 입력",
                placeholder="응원 문구를 입력하세요!",
                value=""
            )
            final_message = custom_message if custom_message else "응원 문구를 입력하세요!"
        else:
            final_message = SAMPLE_MESSAGES[selected_sample]

        st.markdown("---")

        # 2. 배경색 선택
        st.subheader("🎨 배경색 선택")
        selected_color = st.selectbox(
            "배경색",
            options=list(COLOR_MAPPING.keys()),
            index=0
        )
        colors = COLOR_MAPPING[selected_color]

        st.markdown("---")

        # 3. 효과 선택
        st.subheader("✨ 효과 선택")
        use_neon = st.checkbox("💡 네온싸인 효과", value=True)
        use_slide = st.checkbox("🎬 슬라이드 효과 (오른쪽→왼쪽)", value=False)

        st.markdown("---")

        # 4. 전체화면 버튼
        st.subheader("📺 전체화면")
        if st.button("📺 전체화면으로 보기", type="primary", use_container_width=True):
            st.session_state.fullscreen_mode = True
            st.session_state.message = final_message
            st.session_state.colors = colors
            st.session_state.use_neon = use_neon
            st.session_state.use_slide = use_slide
            st.rerun()

    # 메인 영역 - 미리보기
    st.subheader("👀 미리보기")

    style = get_display_style(
        colors["bg"], colors["text"], colors["neon"],
        use_neon, use_slide
    )

    preview_html = f"""
        {style}
        <div class="preview-box">
            <div class="preview-text">{final_message}</div>
        </div>
    """

    st.markdown(preview_html, unsafe_allow_html=True)

    # 색상 정보 표시
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"🎨 배경색: {selected_color}")
    with col2:
        st.info(f"✏️ 글자색: {colors['text']}")
    with col3:
        st.info(f"💡 네온색: {colors['neon']}")

    # 사용 안내
    st.markdown("---")
    st.markdown("""
    ### 📱 사용 방법
    1. **왼쪽 메뉴(☰)** 에서 옵션을 설정하세요
    2. **샘플 문구** 선택 또는 **직접 입력**
    3. **배경색**을 선택하면 글자색이 자동 변경됩니다
    4. **효과**를 선택하세요 (네온싸인, 슬라이드)
    5. **[📺 전체화면으로 보기]** 버튼 클릭!
    6. **화면을 터치**하면 설정 화면으로 돌아옵니다
    """)

# URL 파라미터 확인 (터치로 돌아온 경우)
query_params = st.query_params
if 'back' in query_params:
    st.session_state.fullscreen_mode = False
    # 파라미터 제거
    st.query_params.clear()

# 메인 로직
if st.session_state.fullscreen_mode:
    show_fullscreen(
        st.session_state.get('message', '화이팅!'),
        st.session_state.get('colors', COLOR_MAPPING["🖤 검정"]),
        st.session_state.get('use_neon', True),
        st.session_state.get('use_slide', False)
    )
else:
    show_settings()
