import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="응원 문구",
    page_icon="📣",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 샘플 문구 목록
SAMPLE_MESSAGES = {
    "직접 입력": "",
    "에듀테크AI(고) 분임 - 화이팅": "에듀테크AI(고) 분임 화이팅! 💪",
    "에듀테크AI(고) 분임 - 최고": "에듀테크AI(고) 분임 최고! 🏆",
    "에듀테크AI(고) 분임 - 응원": "에듀테크AI(고) 분임 응원합니다! 📣",
    "수학 분임 - 화이팅": "수학 분임 화이팅! 💪",
    "수학 분임 - 최고": "수학 분임 최고! 🏆",
    "수학 분임 - 응원": "수학 분임 응원합니다! 📣",
}

# 배경색과 글자색 조합
COLOR_SCHEMES = {
    "🖤 검정": {"bg": "#000000", "text": "#FFFFFF", "neon": "#00FFFF"},
    "❤️ 빨강": {"bg": "#CC0000", "text": "#FFFF00", "neon": "#FFFF00"},
    "💙 파랑": {"bg": "#0066CC", "text": "#FFFFFF", "neon": "#00FF00"},
    "💚 초록": {"bg": "#006600", "text": "#FFFFFF", "neon": "#FF69B4"},
    "💜 보라": {"bg": "#660099", "text": "#00FFFF", "neon": "#00FFFF"},
    "🤍 흰색": {"bg": "#FFFFFF", "text": "#FF1493", "neon": "#FF1493"},
}

# URL 파라미터 확인
query_params = st.query_params
is_fullscreen = query_params.get("fullscreen", "false") == "true"

if is_fullscreen:
    # 전체화면 모드
    msg = query_params.get("msg", "화이팅!")
    bg_color = query_params.get("bg", "#000000")
    text_color = query_params.get("text", "#FFFFFF")
    neon_color = query_params.get("neon", "#00FFFF")
    use_neon = query_params.get("neon_effect", "false") == "true"
    use_slide = query_params.get("slide_effect", "false") == "true"

    # 애니메이션 스타일 결정
    if use_neon and use_slide:
        animation_style = "animation: neonPulse 1.5s ease-in-out infinite alternate, slideText 15s linear infinite;"
    elif use_neon:
        animation_style = "animation: neonPulse 1.5s ease-in-out infinite alternate;"
    elif use_slide:
        animation_style = "animation: slideText 15s linear infinite;"
    else:
        animation_style = ""

    # 네온 텍스트 쉐도우
    if use_neon:
        neon_shadow = f"text-shadow: 0 0 10px {neon_color}, 0 0 20px {neon_color}, 0 0 40px {neon_color}, 0 0 80px {neon_color};"
    else:
        neon_shadow = ""

    # 전체화면 HTML
    fullscreen_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
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
                cursor: pointer;
                overflow: hidden;
            }}

            .message {{
                font-size: 15vw;
                font-weight: bold;
                color: {text_color};
                text-align: center;
                padding: 20px;
                white-space: nowrap;
                {neon_shadow}
                {animation_style}
            }}

            @keyframes neonPulse {{
                from {{
                    text-shadow: 0 0 10px {neon_color}, 0 0 20px {neon_color}, 0 0 40px {neon_color};
                }}
                to {{
                    text-shadow: 0 0 20px {neon_color}, 0 0 40px {neon_color}, 0 0 80px {neon_color}, 0 0 120px {neon_color};
                }}
            }}

            @keyframes slideText {{
                from {{
                    transform: translateX(100vw);
                }}
                to {{
                    transform: translateX(-100%);
                }}
            }}

            .touch-hint {{
                position: fixed;
                bottom: 30px;
                left: 50%;
                transform: translateX(-50%);
                color: {text_color};
                opacity: 0.7;
                font-size: 16px;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="fullscreen-container" onclick="goBack()">
            <div class="message">{msg}</div>
            <div class="touch-hint">👆 화면을 터치하면 설정 화면으로 돌아갑니다</div>
        </div>
        <script>
            function requestFullscreen() {{
                var elem = document.documentElement;
                if (elem.requestFullscreen) {{
                    elem.requestFullscreen();
                }} else if (elem.webkitRequestFullscreen) {{
                    elem.webkitRequestFullscreen();
                }} else if (elem.msRequestFullscreen) {{
                    elem.msRequestFullscreen();
                }}
            }}

            document.addEventListener('DOMContentLoaded', function() {{
                setTimeout(requestFullscreen, 100);
            }});

            function goBack() {{
                if (document.exitFullscreen) {{
                    document.exitFullscreen();
                }} else if (document.webkitExitFullscreen) {{
                    document.webkitExitFullscreen();
                }} else if (document.msExitFullscreen) {{
                    document.msExitFullscreen();
                }}
                window.location.href = window.location.pathname;
            }}
        </script>
    </body>
    </html>
    """

    st.components.v1.html(fullscreen_html, height=800, scrolling=False)

else:
    # 설정 화면
    st.markdown("""
        <style>
            .main > div { max-width: 800px; margin: 0 auto; }
            .stRadio > div { display: flex; flex-wrap: wrap; gap: 10px; }
            .stRadio > div > label { 
                background: #f0f2f6; 
                padding: 10px 20px; 
                border-radius: 10px;
                cursor: pointer;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>🎉 응원 문구 만들기</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # 1. 문구 선택 섹션
    st.markdown("### 📝 문구 선택")
    col1, col2 = st.columns([1, 2])

    with col1:
        selected_sample = st.selectbox(
            "샘플 문구 선택",
            options=list(SAMPLE_MESSAGES.keys()),
            label_visibility="collapsed"
        )

    with col2:
        if selected_sample == "직접 입력":
            message = st.text_input(
                "응원 문구 입력",
                placeholder="응원 문구를 입력하세요...",
                label_visibility="collapsed"
            )
        else:
            message = SAMPLE_MESSAGES[selected_sample]
            st.text_input(
                "선택된 문구",
                value=message,
                disabled=True,
                label_visibility="collapsed"
            )

    if not message:
        message = "화이팅! 💪"

    st.markdown("---")

    # 2. 배경색 선택 섹션
    st.markdown("### 🎨 배경색 선택")
    selected_color = st.radio(
        "배경색",
        options=list(COLOR_SCHEMES.keys()),
        horizontal=True,
        label_visibility="collapsed"
    )

    colors = COLOR_SCHEMES[selected_color]

    st.markdown("---")

    # 3. 효과 선택 섹션
    st.markdown("### ✨ 효과 선택")
    col1, col2 = st.columns(2)

    with col1:
        use_neon = st.checkbox("💡 네온싸인 효과", value=True)

    with col2:
        use_slide = st.checkbox("🎬 슬라이드 효과 (오른쪽→왼쪽)", value=False)

    st.markdown("---")

    # 4. 미리보기 섹션
    st.markdown("### 👀 미리보기")

    neon_style = ""
    if use_neon:
        neon_style = f"text-shadow: 0 0 10px {colors['neon']}, 0 0 20px {colors['neon']}, 0 0 40px {colors['neon']};"

    slide_style = ""
    slide_keyframes = ""
    if use_slide:
        slide_style = "animation: slidePreview 15s linear infinite;"
        slide_keyframes = """
            @keyframes slidePreview {
                from { transform: translateX(100%); }
                to { transform: translateX(-100%); }
            }
        """

    preview_html = f"""
    <style>
        {slide_keyframes}
    </style>
    <div style="
        background-color: {colors['bg']};
        padding: 60px 20px;
        border-radius: 15px;
        text-align: center;
        overflow: hidden;
        margin: 10px 0;
    ">
        <div style="
            font-size: 2.5rem;
            font-weight: bold;
            color: {colors['text']};
            white-space: nowrap;
            {neon_style}
            {slide_style}
        ">
            {message}
        </div>
    </div>
    """

    st.markdown(preview_html, unsafe_allow_html=True)

    st.markdown("---")

    # 5. 전체화면 버튼 섹션
    st.markdown("### 📺 전체화면 모드")

    import urllib.parse
    params = {
        "fullscreen": "true",
        "msg": message,
        "bg": colors['bg'],
        "text": colors['text'],
        "neon": colors['neon'],
        "neon_effect": "true" if use_neon else "false",
        "slide_effect": "true" if use_slide else "false"
    }
    query_string = urllib.parse.urlencode(params)

    fullscreen_button_html = f"""
    <style>
        .fullscreen-btn {{
            display: block;
            width: 100%;
            padding: 20px;
            font-size: 1.5rem;
            font-weight: bold;
            color: white;
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
            border: none;
            border-radius: 15px;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
            margin: 10px 0;
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        .fullscreen-btn:hover {{
            transform: scale(1.02);
            box-shadow: 0 5px 20px rgba(0,0,0,0.3);
        }}
    </style>
    <a href="?{query_string}" class="fullscreen-btn">
        📺 전체화면으로 보기
    </a>
    """

    st.markdown(fullscreen_button_html, unsafe_allow_html=True)

    st.markdown("---")

    st.info("💡 **사용 방법**: 문구와 옵션을 선택한 후 '전체화면으로 보기' 버튼을 누르세요. 전체화면에서 화면을 터치하면 설정 화면으로 돌아옵니다.")
