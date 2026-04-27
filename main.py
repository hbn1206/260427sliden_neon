
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="🎉 응원 문구",
    page_icon="📣",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 샘플 문구
SAMPLE_MESSAGES = {
    "직접 입력": "",
    "에듀테크AI(고) 분임 - 화이팅": "🔥 에듀테크AI(고) 분임 화이팅! 🔥",
    "에듀테크AI(고) 분임 - 최고": "⭐ 에듀테크AI(고) 분임 최고! ⭐",
    "에듀테크AI(고) 분임 - 응원": "📣 에듀테크AI(고) 분임 힘내세요! 📣",
    "수학 분임 - 화이팅": "🔥 수학 분임 화이팅! 🔥",
    "수학 분임 - 최고": "⭐ 수학 분임 최고! ⭐",
    "수학 분임 - 응원": "📣 수학 분임 힘내세요! 📣",
    "모두 화이팅": "🎉 모두 화이팅! 우리는 할 수 있다! 🎉",
}

# 배경색과 최적의 글자색 매핑
COLOR_SCHEMES = {
    "🖤 검정": {"bg": "#000000", "text": "#FFFFFF", "neon": "#00FFFF", "neon_shadow": "0 0 10px #00FFFF, 0 0 20px #00FFFF, 0 0 40px #00FFFF, 0 0 80px #0099FF"},
    "❤️ 빨강": {"bg": "#CC0000", "text": "#FFFF00", "neon": "#FFFF00", "neon_shadow": "0 0 10px #FFFF00, 0 0 20px #FFFF00, 0 0 40px #FFFF00, 0 0 80px #FFD700"},
    "💙 파랑": {"bg": "#0033AA", "text": "#FFFFFF", "neon": "#00FF88", "neon_shadow": "0 0 10px #00FF88, 0 0 20px #00FF88, 0 0 40px #00FF88, 0 0 80px #00CC66"},
    "💚 초록": {"bg": "#006633", "text": "#FFFFFF", "neon": "#FF88FF", "neon_shadow": "0 0 10px #FF88FF, 0 0 20px #FF88FF, 0 0 40px #FF88FF, 0 0 80px #FF44FF"},
    "💜 보라": {"bg": "#660099", "text": "#00FFFF", "neon": "#00FFFF", "neon_shadow": "0 0 10px #00FFFF, 0 0 20px #00FFFF, 0 0 40px #00FFFF, 0 0 80px #00CCCC"},
    "🤍 흰색": {"bg": "#FFFFFF", "text": "#FF0066", "neon": "#FF0066", "neon_shadow": "0 0 10px #FF0066, 0 0 20px #FF0066, 0 0 40px #FF0066, 0 0 80px #CC0055"},
}

# 사이드바 설정
with st.sidebar:
    st.title("⚙️ 설정")

    st.subheader("📝 문구 선택")
    selected_sample = st.selectbox(
        "샘플 문구 선택",
        list(SAMPLE_MESSAGES.keys())
    )

    if selected_sample == "직접 입력":
        custom_message = st.text_area(
            "응원 문구 입력",
            placeholder="응원 문구를 입력하세요!",
            height=100
        )
        display_message = custom_message if custom_message else "응원 문구를 입력하세요! 📣"
    else:
        display_message = SAMPLE_MESSAGES[selected_sample]

    st.markdown("---")

    st.subheader("🎨 스타일 설정")

    # 배경색 선택
    bg_choice = st.selectbox("배경 색상", list(COLOR_SCHEMES.keys()))
    colors = COLOR_SCHEMES[bg_choice]

    # 효과 선택
    use_neon = st.checkbox("✨ 네온싸인 효과", value=True)
    use_slide = st.checkbox("🎬 슬라이드 효과", value=False)

    # 글자 크기
    font_size = st.slider("글자 크기", 30, 150, 80)

    st.markdown("---")

    # 전체화면 버튼
    st.subheader("📺 전체화면")
    st.markdown("""
    <button onclick="
        var elem = document.documentElement;
        if (elem.requestFullscreen) {
            elem.requestFullscreen();
        } else if (elem.webkitRequestFullscreen) {
            elem.webkitRequestFullscreen();
        } else if (elem.msRequestFullscreen) {
            elem.msRequestFullscreen();
        }
    " style="
        width: 100%;
        padding: 15px;
        font-size: 18px;
        font-weight: bold;
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        margin-top: 10px;
    ">
        📺 전체화면 보기
    </button>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.info("💡 전체화면 종료: ESC 키")

# 애니메이션 CSS
if use_slide and use_neon:
    animation_css = f"""
        animation: slideRight 15s linear infinite, neonFlicker 1.5s ease-in-out infinite alternate;
        text-shadow: {colors['neon_shadow']};
        color: {colors['neon']};
    """
elif use_slide:
    animation_css = f"""
        animation: slideRight 15s linear infinite;
        color: {colors['text']};
    """
elif use_neon:
    animation_css = f"""
        animation: neonFlicker 1.5s ease-in-out infinite alternate;
        text-shadow: {colors['neon_shadow']};
        color: {colors['neon']};
    """
else:
    animation_css = f"""
        color: {colors['text']};
    """

# 메인 CSS
main_css = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@900&display=swap');

    /* 전체 페이지 스타일 */
    .stApp {{
        background-color: {colors['bg']} !important;
    }}

    /* 메인 영역 */
    .main .block-container {{
        padding: 0 !important;
        max-width: 100% !important;
    }}

    /* 응원 문구 컨테이너 */
    .cheer-container {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: {colors['bg']};
        overflow: hidden;
        z-index: 1000;
    }}

    /* 응원 문구 텍스트 */
    .cheer-text {{
        font-family: 'Noto Sans KR', sans-serif;
        font-size: {font_size}px;
        font-weight: 900;
        text-align: center;
        white-space: nowrap;
        padding: 20px 50px;
        {animation_css}
    }}

    /* 슬라이드 애니메이션 - 오른쪽에서 왼쪽으로, 천천히 */
    @keyframes slideRight {{
        0% {{
            transform: translateX(100vw);
        }}
        100% {{
            transform: translateX(-100%);
        }}
    }}

    /* 네온 깜빡임 애니메이션 */
    @keyframes neonFlicker {{
        0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {{
            opacity: 1;
        }}
        20%, 24%, 55% {{
            opacity: 0.8;
        }}
    }}

    /* 사이드바 스타일 */
    section[data-testid="stSidebar"] {{
        background-color: #1a1a2e !important;
        z-index: 2000;
    }}

    section[data-testid="stSidebar"] * {{
        color: white !important;
    }}

    /* 헤더 숨기기 */
    header[data-testid="stHeader"] {{
        display: none;
    }}

    /* 모바일 최적화 */
    @media (max-width: 768px) {{
        .cheer-text {{
            font-size: {max(font_size - 30, 30)}px !important;
            padding: 10px 20px;
        }}
    }}

    /* 태블릿 최적화 */
    @media (min-width: 769px) and (max-width: 1024px) {{
        .cheer-text {{
            font-size: {max(font_size - 15, 40)}px !important;
        }}
    }}
</style>
"""

# CSS 적용
st.markdown(main_css, unsafe_allow_html=True)

# 응원 문구 표시
st.markdown(f"""
<div class="cheer-container">
    <div class="cheer-text">
        {display_message}
    </div>
</div>
""", unsafe_allow_html=True)
