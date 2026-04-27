import streamlit as st
from urllib.parse import urlencode, parse_qs
import base64

# 페이지 설정
st.set_page_config(
    page_title="🎉 응원 문구 만들기",
    page_icon="📣",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 배경색별 글자색 및 네온 효과색 매핑
COLOR_SCHEMES = {
    "🖤 검정": {"bg": "#000000", "text": "#FFFFFF", "neon": "#00FFFF", "name": "black"},
    "❤️ 빨강": {"bg": "#CC0000", "text": "#FFFF00", "neon": "#FFFF00", "name": "red"},
    "💙 파랑": {"bg": "#0066CC", "text": "#FFFFFF", "neon": "#00FF00", "name": "blue"},
    "💚 초록": {"bg": "#006633", "text": "#FFFFFF", "neon": "#FF69B4", "name": "green"},
    "💜 보라": {"bg": "#663399", "text": "#00FFFF", "neon": "#00FFFF", "name": "purple"},
    "🤍 흰색": {"bg": "#FFFFFF", "text": "#FF1493", "neon": "#FF1493", "name": "white"}
}

# 글꼴 옵션
FONT_OPTIONS = {
    "Black Han Sans (굵고 강렬)": "Black Han Sans",
    "Jua (둥글고 친근)": "Jua", 
    "Do Hyeon (레트로 감성)": "Do Hyeon",
    "Gugi (독특한 디자인)": "Gugi"
}

# 샘플 문구 - 분임별 4가지씩
SAMPLE_MESSAGES = {
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

def create_fullscreen_html(message, color_scheme, font_family, use_neon, use_slide, use_blink):
    """전체화면용 HTML 생성"""
    bg_color = color_scheme["bg"]
    text_color = color_scheme["text"]
    neon_color = color_scheme["neon"]

    # 효과별 CSS
    neon_style = ""
    if use_neon:
        neon_style = f"""
            text-shadow:
                0 0 10px {neon_color},
                0 0 20px {neon_color},
                0 0 40px {neon_color},
                0 0 80px {neon_color};
            animation: neonPulse 1.5s ease-in-out infinite alternate;
        """

    slide_style = ""
    slide_keyframes = ""
    if use_slide:
        slide_style = "animation: slideText 15s linear infinite;"
        slide_keyframes = """
            @keyframes slideText {
                0% { transform: translateX(100%); }
                100% { transform: translateX(-100%); }
            }
        """

    blink_style = ""
    blink_keyframes = ""
    if use_blink:
        blink_style = "animation: blinkText 1s ease-in-out infinite;"
        blink_keyframes = """
            @keyframes blinkText {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.3; }
            }
        """

    # 여러 애니메이션 조합
    animations = []
    if use_neon:
        animations.append("neonPulse 1.5s ease-in-out infinite alternate")
    if use_slide:
        animations.append("slideText 15s linear infinite")
    if use_blink:
        animations.append("blinkText 1s ease-in-out infinite")

    animation_style = f"animation: {', '.join(animations)};" if animations else ""

    html_content = f"""
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>응원 문구</title>
        <link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Jua&family=Do+Hyeon&family=Gugi&display=swap" rel="stylesheet">
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
                background-color: {bg_color};
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                min-height: -webkit-fill-available;
                cursor: pointer;
                touch-action: manipulation;
            }}

            .message {{
                font-family: '{font_family}', sans-serif;
                font-size: 18vw;
                color: {text_color};
                text-align: center;
                padding: 20px;
                white-space: nowrap;
                {f"text-shadow: 0 0 10px {neon_color}, 0 0 20px {neon_color}, 0 0 40px {neon_color}, 0 0 80px {neon_color};" if use_neon else ""}
                {animation_style}
            }}

            @keyframes neonPulse {{
                from {{
                    text-shadow:
                        0 0 10px {neon_color},
                        0 0 20px {neon_color},
                        0 0 40px {neon_color};
                }}
                to {{
                    text-shadow:
                        0 0 20px {neon_color},
                        0 0 40px {neon_color},
                        0 0 80px {neon_color},
                        0 0 120px {neon_color};
                }}
            }}

            {slide_keyframes}
            {blink_keyframes}

            .guide {{
                position: fixed;
                bottom: 30px;
                left: 50%;
                transform: translateX(-50%);
                color: {text_color};
                opacity: 0.6;
                font-size: 14px;
                font-family: sans-serif;
            }}
        </style>
    </head>
    <body onclick="toggleFullscreen()">
        <div class="message">{message}</div>
        <div class="guide">👆 화면을 터치하면 전체화면 ON/OFF</div>

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

            // 페이지 로드 시 자동 전체화면
            document.addEventListener('click', function() {{
                toggleFullscreen();
            }}, {{ once: true }});
        </script>
    </body>
    </html>
    """
    return html_content

def create_preview_html(message, color_scheme, font_family, use_neon, use_slide, use_blink):
    """미리보기용 HTML 생성"""
    bg_color = color_scheme["bg"]
    text_color = color_scheme["text"]
    neon_color = color_scheme["neon"]

    # 애니메이션 조합
    animations = []
    if use_neon:
        animations.append("neonPulse 1.5s ease-in-out infinite alternate")
    if use_slide:
        animations.append("slideText 8s linear infinite")
    if use_blink:
        animations.append("blinkText 1s ease-in-out infinite")

    animation_style = f"animation: {', '.join(animations)};" if animations else ""

    neon_shadow = ""
    if use_neon:
        neon_shadow = f"text-shadow: 0 0 5px {neon_color}, 0 0 10px {neon_color}, 0 0 20px {neon_color}, 0 0 40px {neon_color};"

    preview_html = f"""
    <div style="
        background-color: {bg_color};
        border-radius: 15px;
        padding: 40px 20px;
        text-align: center;
        min-height: 200px;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        position: relative;
    ">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Jua&family=Do+Hyeon&family=Gugi&display=swap');

            @keyframes neonPulse {{
                from {{
                    text-shadow: 0 0 5px {neon_color}, 0 0 10px {neon_color}, 0 0 20px {neon_color};
                }}
                to {{
                    text-shadow: 0 0 10px {neon_color}, 0 0 20px {neon_color}, 0 0 40px {neon_color}, 0 0 60px {neon_color};
                }}
            }}

            @keyframes slideText {{
                0% {{ transform: translateX(100%); }}
                100% {{ transform: translateX(-100%); }}
            }}

            @keyframes blinkText {{
                0%, 100% {{ opacity: 1; }}
                50% {{ opacity: 0.3; }}
            }}

            .preview-message {{
                font-family: '{font_family}', sans-serif;
                font-size: 2.5rem;
                color: {text_color};
                white-space: nowrap;
                {neon_shadow}
                {animation_style}
            }}
        </style>
        <div class="preview-message">{message}</div>
    </div>
    """
    return preview_html

def main():
    st.title("🎉 응원 문구 만들기")
    st.markdown("**모바일/태블릿에서 전체화면 응원 문구를 띄워보세요!**")

    st.markdown("---")

    # 1. 문구 선택
    st.subheader("📝 문구 선택")

    col1, col2 = st.columns([1, 2])

    with col1:
        selected_sample = st.selectbox(
            "샘플 문구 선택",
            options=list(SAMPLE_MESSAGES.keys()),
            index=1,
            label_visibility="collapsed"
        )

    with col2:
        if selected_sample == "직접 입력하기":
            message = st.text_input(
                "문구 입력",
                value="화이팅! 💪",
                placeholder="응원 문구를 입력하세요",
                label_visibility="collapsed"
            )
        elif SAMPLE_MESSAGES.get(selected_sample) is None:
            message = st.text_input(
                "문구 입력",
                value="화이팅! 💪",
                placeholder="응원 문구를 입력하세요",
                label_visibility="collapsed"
            )
        else:
            message = SAMPLE_MESSAGES[selected_sample]
            st.markdown(f"### {message}")

    st.markdown("---")

    # 2. 배경색 선택
    st.subheader("🎨 배경색 선택")
    selected_color = st.radio(
        "배경색",
        options=list(COLOR_SCHEMES.keys()),
        horizontal=True,
        label_visibility="collapsed"
    )
    color_scheme = COLOR_SCHEMES[selected_color]

    st.markdown("---")

    # 3. 글꼴 선택
    st.subheader("🔤 글꼴 선택")
    selected_font = st.radio(
        "글꼴",
        options=list(FONT_OPTIONS.keys()),
        horizontal=True,
        label_visibility="collapsed"
    )
    font_family = FONT_OPTIONS[selected_font]

    st.markdown("---")

    # 4. 효과 선택
    st.subheader("✨ 효과 선택")
    col1, col2, col3 = st.columns(3)

    with col1:
        use_neon = st.checkbox("💡 네온싸인 효과", value=True)
    with col2:
        use_slide = st.checkbox("🎬 슬라이드 효과", value=False)
    with col3:
        use_blink = st.checkbox("⚡ 깜빡깜빡 효과", value=False)

    st.markdown("---")

    # 5. 미리보기
    st.subheader("👀 미리보기")

    if message and message.strip():
        preview_html = create_preview_html(
            message, color_scheme, font_family, 
            use_neon, use_slide, use_blink
        )
        st.components.v1.html(preview_html, height=250)
    else:
        st.warning("문구를 입력해주세요!")

    st.markdown("---")

    # 6. 전체화면 모드
    st.subheader("📺 전체화면 모드")

    if message and message.strip():
        html_content = create_fullscreen_html(
            message, color_scheme, font_family,
            use_neon, use_slide, use_blink
        )

        # HTML 파일 다운로드
        b64 = base64.b64encode(html_content.encode()).decode()

        st.markdown(f"""
            <a href="data:text/html;base64,{b64}" download="cheer_screen.html" style="
                display: inline-block;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 15px 40px;
                font-size: 1.3rem;
                font-weight: bold;
                text-decoration: none;
                border-radius: 10px;
                text-align: center;
                width: 100%;
                box-sizing: border-box;
            ">
                📥 응원 화면 다운로드 (HTML)
            </a>
        """, unsafe_allow_html=True)

        st.markdown("")
        st.info("""
        **📱 사용 방법:**
        1. 위 버튼을 눌러 파일을 다운로드하세요
        2. 다운로드된 `cheer_screen.html` 파일을 브라우저로 열어주세요
        3. 화면을 터치하면 전체화면으로 전환됩니다!
        """)
    else:
        st.warning("문구를 입력해주세요!")

if __name__ == "__main__":
    main()
