import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="🎉 응원 문구 만들기",
    page_icon="🎉",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Google Fonts 로드 (전체 페이지에 적용)
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Do+Hyeon&family=Gugi&family=Jua&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# 앱 제목
st.markdown("""
<h1 style="text-align: center; margin-bottom: 30px;">🎉 응원 문구 만들기</h1>
""", unsafe_allow_html=True)

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
    "Black Han Sans (굵은 고딕)": "'Black Han Sans', sans-serif",
    "Jua (둥근 고딕)": "'Jua', sans-serif",
    "Do Hyeon (네모 고딕)": "'Do Hyeon', sans-serif",
    "Gugi (독특한 고딕)": "'Gugi', sans-serif"
}

# 배경색 및 글자색 조합
color_schemes = {
    "🖤 검정": {"bg": "#000000", "text": "#FFFFFF", "neon": "#00FFFF"},
    "❤️ 빨강": {"bg": "#CC0000", "text": "#FFFF00", "neon": "#FFFF00"},
    "💙 파랑": {"bg": "#0033AA", "text": "#FFFFFF", "neon": "#00FF00"},
    "💚 초록": {"bg": "#006600", "text": "#FFFFFF", "neon": "#FF69B4"},
    "💜 보라": {"bg": "#4B0082", "text": "#00FFFF", "neon": "#00FFFF"},
    "🤍 흰색": {"bg": "#FFFFFF", "text": "#FF1493", "neon": "#FF1493"}
}

# ===== 1. 문구 선택 =====
st.markdown("### 📝 문구 선택")
selected_option = st.selectbox(
    "샘플 문구를 선택하거나 직접 입력하세요",
    options=list(sample_messages.keys()),
    label_visibility="collapsed"
)

# 직접 입력 처리
if selected_option == "직접 입력하기":
    cheer_text = st.text_input("응원 문구를 입력하세요", value="우리 팀 화이팅! 💪")
elif sample_messages.get(selected_option) is None:
    cheer_text = ""
    st.info("👆 위에서 문구를 선택해주세요")
else:
    cheer_text = sample_messages[selected_option]

st.markdown("---")

# ===== 2. 글꼴 선택 =====
st.markdown("### 🔤 글꼴 선택")
selected_font_name = st.selectbox(
    "글꼴을 선택하세요",
    options=list(fonts.keys()),
    label_visibility="collapsed"
)
selected_font = fonts[selected_font_name]

st.markdown("---")

# ===== 3. 배경색 선택 =====
st.markdown("### 🎨 배경색 선택")
selected_color_name = st.radio(
    "배경색을 선택하세요",
    options=list(color_schemes.keys()),
    horizontal=True,
    label_visibility="collapsed"
)
colors = color_schemes[selected_color_name]

st.markdown("---")

# ===== 4. 효과 선택 =====
st.markdown("### ✨ 효과 선택")
col1, col2, col3 = st.columns(3)
with col1:
    neon_effect = st.checkbox("💡 네온싸인", value=True)
with col2:
    slide_effect = st.checkbox("🎬 슬라이드")
with col3:
    blink_effect = st.checkbox("⚡ 깜빡깜빡")

st.markdown("---")

# ===== 5. 미리보기 =====
st.markdown("### 👀 미리보기")

if cheer_text:
    # CSS 애니메이션 생성
    animations = []
    animation_css = ""

    if neon_effect:
        animation_css += f"""
        @keyframes neonPulse {{
            0%, 100% {{
                text-shadow:
                    0 0 10px {colors['neon']},
                    0 0 20px {colors['neon']},
                    0 0 40px {colors['neon']};
            }}
            50% {{
                text-shadow:
                    0 0 20px {colors['neon']},
                    0 0 40px {colors['neon']},
                    0 0 80px {colors['neon']};
            }}
        }}
        """
        animations.append("neonPulse 1.5s ease-in-out infinite")

    if slide_effect:
        animation_css += """
        @keyframes slideText {
            0% { transform: translateX(100%); }
            100% { transform: translateX(-100%); }
        }
        """
        animations.append("slideText 15s linear infinite")

    if blink_effect:
        animation_css += """
        @keyframes blinkText {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.3; }
        }
        """
        animations.append("blinkText 1s ease-in-out infinite")

    animation_style = f"animation: {', '.join(animations)};" if animations else ""

    # 미리보기 HTML (Google Fonts 포함)
    preview_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Do+Hyeon&family=Gugi&family=Jua&display=swap" rel="stylesheet">
        <style>
            {animation_css}

            body {{
                margin: 0;
                padding: 0;
                background-color: {colors['bg']};
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100%;
                overflow: hidden;
            }}

            .cheer-text {{
                font-family: {selected_font};
                font-size: 8vw;
                color: {colors['text']};
                text-align: center;
                white-space: nowrap;
                {animation_style}
            }}
        </style>
    </head>
    <body>
        <div class="cheer-text">{cheer_text}</div>
    </body>
    </html>
    """

    # 미리보기 표시
    components.html(preview_html, height=200)
else:
    st.warning("문구를 선택해주세요")

st.markdown("---")

# ===== 6. 전체화면 모드 =====
st.markdown("### 📺 전체화면 모드")

if cheer_text:
    # CSS 애니메이션 생성 (전체화면용)
    animations_full = []
    animation_css_full = ""

    if neon_effect:
        animation_css_full += f"""
        @keyframes neonPulse {{
            0%, 100% {{
                text-shadow:
                    0 0 10px {colors['neon']},
                    0 0 20px {colors['neon']},
                    0 0 40px {colors['neon']},
                    0 0 80px {colors['neon']};
            }}
            50% {{
                text-shadow:
                    0 0 20px {colors['neon']},
                    0 0 40px {colors['neon']},
                    0 0 80px {colors['neon']},
                    0 0 120px {colors['neon']};
            }}
        }}
        """
        animations_full.append("neonPulse 1.5s ease-in-out infinite")

    if slide_effect:
        animation_css_full += """
        @keyframes slideText {
            0% { transform: translateX(100%); }
            100% { transform: translateX(-100%); }
        }
        """
        animations_full.append("slideText 15s linear infinite")

    if blink_effect:
        animation_css_full += """
        @keyframes blinkText {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.3; }
        }
        """
        animations_full.append("blinkText 1s ease-in-out infinite")

    animation_style_full = f"animation: {', '.join(animations_full)};" if animations_full else ""

    # 전체화면 HTML 파일 생성
    fullscreen_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <title>🎉 응원 문구</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Do+Hyeon&family=Gugi&family=Jua&display=swap" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        {animation_css_full}

        html, body {{
            width: 100%;
            height: 100%;
            overflow: hidden;
        }}

        body {{
            background-color: {colors['bg']};
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
        }}

        .container {{
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        }}

        .cheer-text {{
            font-family: {selected_font};
            font-size: 18vw;
            color: {colors['text']};
            text-align: center;
            white-space: nowrap;
            padding: 20px;
            {animation_style_full}
        }}

        .hint {{
            position: fixed;
            bottom: 20px;
            left: 0;
            right: 0;
            text-align: center;
            color: {colors['text']};
            opacity: 0.5;
            font-size: 14px;
            font-family: {selected_font};
        }}
    </style>
</head>
<body>
    <div class="container" onclick="toggleFullscreen()">
        <div class="cheer-text">{cheer_text}</div>
    </div>
    <div class="hint">👆 화면을 터치하여 전체화면 ON/OFF</div>

    <script>
        // 화면 꺼짐 방지
        async function keepAwake() {{
            try {{
                if ('wakeLock' in navigator) {{
                    await navigator.wakeLock.request('screen');
                }}
            }} catch (err) {{
                console.log('Wake Lock error:', err);
            }}
        }}
        keepAwake();

        // 전체화면 토글
        function toggleFullscreen() {{
            if (!document.fullscreenElement && !document.webkitFullscreenElement) {{
                if (document.documentElement.requestFullscreen) {{
                    document.documentElement.requestFullscreen();
                }} else if (document.documentElement.webkitRequestFullscreen) {{
                    document.documentElement.webkitRequestFullscreen();
                }}
            }} else {{
                if (document.exitFullscreen) {{
                    document.exitFullscreen();
                }} else if (document.webkitExitFullscreen) {{
                    document.webkitExitFullscreen();
                }}
            }}
        }}

        // 페이지 로드 시 자동 전체화면 시도
        document.addEventListener('click', function() {{
            toggleFullscreen();
        }}, {{ once: true }});
    </script>
</body>
</html>"""

    # 다운로드 버튼
    st.download_button(
        label="📥 응원 화면 다운로드 (HTML)",
        data=fullscreen_html,
        file_name="cheer_screen.html",
        mime="text/html",
        use_container_width=True
    )

    st.info("""
    **📱 사용 방법:**
    1. 위 버튼을 눌러 HTML 파일 다운로드
    2. 다운로드된 파일을 브라우저로 열기
    3. 화면을 터치하면 전체화면 ON/OFF
    """)
else:
    st.warning("문구를 선택해주세요")
