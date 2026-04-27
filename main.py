import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="🎉 응원 문구 만들기",
    page_icon="📣",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Google Fonts 로드
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Do+Hyeon&family=Gugi&family=Jua&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# 기본 스타일
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    .section-box {
        background: #f8f9fa;
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
    }
    .section-title {
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 15px;
    }
    .stButton > button {
        width: 100%;
        height: 60px;
        font-size: 1.3rem;
        border-radius: 15px;
    }
</style>
""", unsafe_allow_html=True)

# 타이틀
st.markdown('<h1 class="main-title">🎉 응원 문구 만들기</h1>', unsafe_allow_html=True)

# 샘플 문구 목록
sample_messages = {
    "── 🤖 에듀테크AI(고) 분임 ──": None,
    "에듀테크AI(고) 분임 최고! 🏆": "에듀테크AI(고) 분임 최고! 🏆",
    "에듀테크AI(고) 분임이 짱이다! 💪": "에듀테크AI(고) 분임이 짱이다! 💪",
    "에듀테크AI(고) 분임 넘버원! 🥇": "에듀테크AI(고) 분임 넘버원! 🥇",
    "에듀테크AI(고) 우리가 최고! ⭐": "에듀테크AI(고) 우리가 최고! ⭐",
    "── 🔢 수학 분임 ──": None,
    "수학 분임 최고! 🏆": "수학 분임 최고! 🏆",
    "수학 분임이 짱이다! 💪": "수학 분임이 짱이다! 💪",
    "수학 분임 넘버원! 🥇": "수학 분임 넘버원! 🥇",
    "수학 분임 우리가 최고! ⭐": "수학 분임 우리가 최고! ⭐",
    "── ✏️ 직접 입력 ──": None,
    "직접 입력하기": "직접 입력"
}

# 글꼴 목록
fonts = {
    "Black Han Sans (굵은 고딕)": "Black Han Sans",
    "Jua (둥근 고딕)": "Jua", 
    "Do Hyeon (레트로 고딕)": "Do Hyeon",
    "Gugi (독특한 고딕)": "Gugi"
}

# 배경색 목록
colors = {
    "🖤 검정": {"bg": "#000000", "text": "#FFFFFF", "neon": "#00FFFF"},
    "❤️ 빨강": {"bg": "#FF0000", "text": "#FFFF00", "neon": "#FFFF00"},
    "💙 파랑": {"bg": "#0066FF", "text": "#FFFFFF", "neon": "#00FF00"},
    "💚 초록": {"bg": "#00AA00", "text": "#FFFFFF", "neon": "#FF69B4"},
    "💜 보라": {"bg": "#8B00FF", "text": "#00FFFF", "neon": "#00FFFF"},
    "🤍 흰색": {"bg": "#FFFFFF", "text": "#FF1493", "neon": "#FF1493"}
}

# ===== 문구 선택 =====
st.markdown('<div class="section-box"><p class="section-title">📝 문구 선택</p></div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    selected_sample = st.selectbox(
        "샘플 문구",
        options=list(sample_messages.keys()),
        label_visibility="collapsed"
    )

with col2:
    if selected_sample == "직접 입력하기":
        message = st.text_input("응원 문구 입력", value="화이팅!", label_visibility="collapsed")
    elif sample_messages.get(selected_sample):
        message = sample_messages[selected_sample]
        st.markdown(f"**선택된 문구:** {message}")
    else:
        message = "문구를 선택하세요"
        st.markdown("*↑ 문구를 선택해주세요*")

# ===== 배경색 선택 =====
st.markdown('<div class="section-box"><p class="section-title">🎨 배경색 선택</p></div>', unsafe_allow_html=True)
selected_color = st.radio(
    "배경색",
    options=list(colors.keys()),
    horizontal=True,
    label_visibility="collapsed"
)

# ===== 글꼴 선택 =====
st.markdown('<div class="section-box"><p class="section-title">🔤 글꼴 선택</p></div>', unsafe_allow_html=True)
selected_font = st.radio(
    "글꼴",
    options=list(fonts.keys()),
    horizontal=True,
    label_visibility="collapsed"
)

# ===== 효과 선택 =====
st.markdown('<div class="section-box"><p class="section-title">✨ 효과 선택</p></div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    neon_effect = st.checkbox("💡 네온싸인", value=True)
with col2:
    slide_effect = st.checkbox("🎬 슬라이드")
with col3:
    blink_effect = st.checkbox("⚡ 깜빡깜빡")

# 색상 정보 가져오기
color_info = colors[selected_color]
font_family = fonts[selected_font]

# CSS 애니메이션 생성
def get_animations_css():
    css = """
    @keyframes neonPulse {
        0%, 100% { opacity: 1; text-shadow: 0 0 10px NEON_COLOR, 0 0 20px NEON_COLOR, 0 0 40px NEON_COLOR; }
        50% { opacity: 0.8; text-shadow: 0 0 5px NEON_COLOR, 0 0 10px NEON_COLOR, 0 0 20px NEON_COLOR; }
    }
    @keyframes slideText {
        0% { transform: translateX(100vw); }
        100% { transform: translateX(-100%); }
    }
    @keyframes blinkText {
        0%, 50%, 100% { opacity: 1; }
        25%, 75% { opacity: 0.3; }
    }
    """.replace("NEON_COLOR", color_info['neon'])
    return css

# 애니메이션 스타일 적용
def get_animation_style():
    animations = []
    if neon_effect:
        animations.append("neonPulse 1.5s ease-in-out infinite")
    if blink_effect:
        animations.append("blinkText 1s ease-in-out infinite")
    if slide_effect:
        animations.append("slideText 12s linear infinite")

    if animations:
        return f"animation: {', '.join(animations)};"
    return ""

# ===== 미리보기 =====
st.markdown('<div class="section-box"><p class="section-title">👀 미리보기</p></div>', unsafe_allow_html=True)

# 슬라이드 여부에 따른 스타일 분기
if slide_effect:
    # 슬라이드 모드: 고정 크기, 가로 스크롤
    text_style = f"""
        font-family: '{font_family}', sans-serif;
        font-size: 12vh;
        color: {color_info['text']};
        white-space: nowrap;
        display: inline-block;
        {get_animation_style()}
    """
    container_style = """
        display: flex;
        align-items: center;
        height: 100%;
        overflow: hidden;
    """
else:
    # 일반 모드: 자동 크기 조절
    text_style = f"""
        font-family: '{font_family}', sans-serif;
        color: {color_info['text']};
        text-align: center;
        word-break: keep-all;
        line-height: 1.2;
        padding: 5%;
        {get_animation_style()}
    """
    container_style = """
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
    """

preview_html = f"""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Do+Hyeon&family=Gugi&family=Jua&display=swap" rel="stylesheet">
<style>
    {get_animations_css()}
</style>
<div style="
    width: 100%;
    height: 200px;
    background-color: {color_info['bg']};
    border-radius: 15px;
    overflow: hidden;
    {container_style}
">
    <div id="previewText" style="{text_style}">
        {message}
    </div>
</div>
"""

if not slide_effect:
    preview_html += """
    <script>
        function adjustPreviewSize() {
            const container = document.querySelector('div[style*="height: 200px"]');
            const text = document.getElementById('previewText');
            if (!container || !text) return;

            let fontSize = 50;
            text.style.fontSize = fontSize + 'px';

            while ((text.scrollWidth > container.clientWidth * 0.9 || text.scrollHeight > container.clientHeight * 0.9) && fontSize > 10) {
                fontSize -= 2;
                text.style.fontSize = fontSize + 'px';
            }
        }
        adjustPreviewSize();
        window.addEventListener('resize', adjustPreviewSize);
    </script>
    """

components.html(preview_html, height=220)

# ===== 전체화면 다운로드 =====
st.markdown('<div class="section-box"><p class="section-title">📺 전체화면 모드</p></div>', unsafe_allow_html=True)

# 슬라이드 여부에 따른 전체화면 HTML
if slide_effect:
    fullscreen_text_style = f"""
        font-family: '{font_family}', sans-serif;
        font-size: 15vh;
        color: {color_info['text']};
        white-space: nowrap;
        display: inline-block;
        {get_animation_style()}
    """
    fullscreen_container_style = """
        display: flex;
        align-items: center;
        height: 100vh;
        overflow: hidden;
    """
    auto_resize_script = ""
else:
    fullscreen_text_style = f"""
        font-family: '{font_family}', sans-serif;
        color: {color_info['text']};
        text-align: center;
        word-break: keep-all;
        line-height: 1.2;
        padding: 5%;
        max-width: 90vw;
        {get_animation_style()}
    """
    fullscreen_container_style = """
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    """
    auto_resize_script = """
    <script>
        function adjustTextSize() {
            const text = document.getElementById('cheerText');
            if (!text) return;

            const maxWidth = window.innerWidth * 0.9;
            const maxHeight = window.innerHeight * 0.8;
            let fontSize = Math.min(window.innerWidth, window.innerHeight) * 0.3;

            text.style.fontSize = fontSize + 'px';

            while ((text.scrollWidth > maxWidth || text.scrollHeight > maxHeight) && fontSize > 20) {
                fontSize -= 5;
                text.style.fontSize = fontSize + 'px';
            }
        }

        window.addEventListener('load', adjustTextSize);
        window.addEventListener('resize', adjustTextSize);
        adjustTextSize();
    </script>
    """

fullscreen_html = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>응원 문구</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Do+Hyeon&family=Gugi&family=Jua&display=swap" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        html, body {{
            width: 100%;
            height: 100%;
            overflow: hidden;
        }}
        body {{
            background-color: {color_info['bg']};
            {fullscreen_container_style}
        }}
        #cheerText {{
            {fullscreen_text_style}
        }}
        {get_animations_css()}
        .hint {{
            position: fixed;
            bottom: 20px;
            left: 0;
            right: 0;
            text-align: center;
            color: {color_info['text']};
            opacity: 0.5;
            font-size: 14px;
            font-family: sans-serif;
        }}
    </style>
</head>
<body onclick="toggleFullscreen()">
    <div id="cheerText">{message}</div>
    <div class="hint">👆 화면을 터치하면 전체화면 ON/OFF</div>

    <script>
        // 화면 꺼짐 방지
        async function keepAwake() {{
            try {{
                if ('wakeLock' in navigator) {{
                    await navigator.wakeLock.request('screen');
                }}
            }} catch (e) {{}}
        }}
        keepAwake();

        // 전체화면 토글
        function toggleFullscreen() {{
            if (!document.fullscreenElement) {{
                document.documentElement.requestFullscreen().catch(e => {{}});
            }} else {{
                document.exitFullscreen().catch(e => {{}});
            }}
        }}

        // 페이지 로드 시 전체화면 시도
        document.addEventListener('click', function() {{
            if (!document.fullscreenElement) {{
                document.documentElement.requestFullscreen().catch(e => {{}});
            }}
        }}, {{ once: true }});
    </script>
    {auto_resize_script}
</body>
</html>
"""

st.download_button(
    label="📥 응원 화면 다운로드 (HTML)",
    data=fullscreen_html,
    file_name="cheer_screen.html",
    mime="text/html",
    use_container_width=True
)

st.markdown("""
<div style="background: #e8f4f8; padding: 15px; border-radius: 10px; margin-top: 10px;">
    <strong>📱 사용 방법:</strong><br>
    1. 위 버튼을 눌러 HTML 파일 다운로드<br>
    2. 다운로드된 파일을 브라우저로 열기<br>
    3. 화면을 터치하면 전체화면 ON/OFF<br>
    4. 응원 시작! 🎉
</div>
""", unsafe_allow_html=True)
