import streamlit as st
import base64

# 페이지 설정
st.set_page_config(
    page_title="🎉 응원 문구 만들기",
    page_icon="🎉",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 샘플 문구 (분임별 4가지씩)
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
    "직접 입력하기": "직접 입력",
}

# 배경색 옵션
COLORS = {
    "🖤 검정": {"bg": "#000000", "text": "#FFFFFF", "neon": "#00FFFF", "neon2": "#FF00FF"},
    "❤️ 빨강": {"bg": "#CC0000", "text": "#FFFF00", "neon": "#FFFF00", "neon2": "#FFFFFF"},
    "💙 파랑": {"bg": "#0033AA", "text": "#FFFFFF", "neon": "#00FF00", "neon2": "#FFFF00"},
    "💚 초록": {"bg": "#006600", "text": "#FFFFFF", "neon": "#FF69B4", "neon2": "#FFFF00"},
    "💜 보라": {"bg": "#660099", "text": "#00FFFF", "neon": "#00FFFF", "neon2": "#FF69B4"},
    "🤍 흰색": {"bg": "#FFFFFF", "text": "#FF1493", "neon": "#FF1493", "neon2": "#8B00FF"},
}

# 글꼴 옵션
FONTS = {
    "Black Han Sans (굵고 강렬)": "Black Han Sans",
    "Jua (둥글고 친근)": "Jua",
    "Do Hyeon (레트로 느낌)": "Do Hyeon",
    "Gugi (독특한 디자인)": "Gugi",
}

# 메인 타이틀
st.markdown("""
    <h1 style='text-align: center; margin-bottom: 30px;'>
        🎉 응원 문구 만들기
    </h1>
""", unsafe_allow_html=True)

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
    if SAMPLE_MESSAGES.get(selected_sample) == "직접 입력":
        message = st.text_input("문구 입력", value="우리 분임 최고! 🎉", label_visibility="collapsed")
    elif SAMPLE_MESSAGES.get(selected_sample) is None:
        message = ""
        st.info("👆 위에서 문구를 선택하세요")
    else:
        message = SAMPLE_MESSAGES[selected_sample]
        st.success(f"✅ {message}")

st.markdown("---")

# 2. 배경색 선택 섹션
st.markdown("### 🎨 배경색 선택")
color_choice = st.radio(
    "배경색",
    options=list(COLORS.keys()),
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("---")

# 3. 글꼴 선택 섹션
st.markdown("### 🔤 글꼴 선택")
font_choice = st.radio(
    "글꼴",
    options=list(FONTS.keys()),
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("---")

# 4. 효과 선택 섹션
st.markdown("### ✨ 효과 선택")
col1, col2, col3 = st.columns(3)
with col1:
    neon_effect = st.checkbox("💡 네온싸인", value=True)
with col2:
    slide_effect = st.checkbox("🎬 슬라이드")
with col3:
    blink_effect = st.checkbox("⚡ 깜빡깜빡")

st.markdown("---")

# 5. 미리보기 섹션
st.markdown("### 👀 미리보기")

if message:
    colors = COLORS[color_choice]
    font_family = FONTS[font_choice]

    # 미리보기용 CSS
    preview_style = f"""
        background-color: {colors['bg']};
        color: {colors['text']};
        font-family: '{font_family}', sans-serif;
        font-size: 8vw;
        font-weight: bold;
        text-align: center;
        padding: 60px 20px;
        border-radius: 20px;
        margin: 20px 0;
    """

    if neon_effect:
        preview_style += f"""
            text-shadow: 
                0 0 10px {colors['neon']},
                0 0 20px {colors['neon']},
                0 0 40px {colors['neon2']};
        """

    st.markdown(f"""
        <link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Do+Hyeon&family=Gugi&family=Jua&display=swap" rel="stylesheet">
        <div style="{preview_style}">
            {message}
        </div>
    """, unsafe_allow_html=True)

    # 효과 표시
    effects = []
    if neon_effect:
        effects.append("💡 네온싸인")
    if slide_effect:
        effects.append("🎬 슬라이드")
    if blink_effect:
        effects.append("⚡ 깜빡깜빡")

    if effects:
        st.caption(f"적용된 효과: {', '.join(effects)}")
else:
    st.warning("👆 위에서 문구를 선택해주세요!")

st.markdown("---")

# 6. 전체화면 다운로드 섹션
st.markdown("### 📺 전체화면 모드")

if message:
    colors = COLORS[color_choice]
    font_family = FONTS[font_choice]

    # 애니메이션 CSS 생성
    animations = []
    animation_css = ""

    if neon_effect:
        animation_css += f"""
            @keyframes neonPulse {{
                0%, 100% {{
                    text-shadow: 
                        0 0 10px {colors['neon']},
                        0 0 20px {colors['neon']},
                        0 0 40px {colors['neon2']},
                        0 0 80px {colors['neon2']};
                }}
                50% {{
                    text-shadow: 
                        0 0 5px {colors['neon']},
                        0 0 10px {colors['neon']},
                        0 0 20px {colors['neon2']},
                        0 0 40px {colors['neon2']};
                }}
            }}
        """
        animations.append("neonPulse 2s ease-in-out infinite")

    if slide_effect:
        animation_css += """
            @keyframes slideText {
                0% {
                    transform: translateX(100vw);
                }
                100% {
                    transform: translateX(-100%);
                }
            }
        """
        animations.append("slideText 15s linear infinite")

    if blink_effect:
        animation_css += """
            @keyframes blinkText {
                0%, 100% {
                    opacity: 1;
                }
                50% {
                    opacity: 0.3;
                }
            }
        """
        animations.append("blinkText 1s ease-in-out infinite")

    animation_property = f"animation: {', '.join(animations)};" if animations else ""

    # 전체화면 HTML 생성
    html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="mobile-web-app-capable" content="yes">
    <title>🎉 응원 화면</title>
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
            background-color: {colors['bg']};
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: '{font_family}', sans-serif;
            cursor: pointer;
            -webkit-user-select: none;
            user-select: none;
            -webkit-tap-highlight-color: transparent;
        }}

        {animation_css}

        .message {{
            color: {colors['text']};
            font-size: 18vw;
            font-weight: bold;
            text-align: center;
            padding: 20px;
            white-space: nowrap;
            {animation_property}
        }}

        .hint {{
            position: fixed;
            bottom: 30px;
            left: 0;
            right: 0;
            text-align: center;
            color: {colors['text']};
            opacity: 0.5;
            font-size: 14px;
            font-family: sans-serif;
        }}

        /* 전체화면일 때 힌트 숨기기 */
        :fullscreen .hint,
        :-webkit-full-screen .hint {{
            display: none;
        }}
    </style>
</head>
<body onclick="toggleFullscreen()">
    <div class="message">{message}</div>
    <div class="hint">👆 화면을 터치하면 전체화면 전환</div>

    <script>
        // 전체화면 전환 함수
        function toggleFullscreen() {{
            if (!document.fullscreenElement && !document.webkitFullscreenElement) {{
                // 전체화면 진입
                if (document.documentElement.requestFullscreen) {{
                    document.documentElement.requestFullscreen();
                }} else if (document.documentElement.webkitRequestFullscreen) {{
                    document.documentElement.webkitRequestFullscreen();
                }}
            }} else {{
                // 전체화면 해제
                if (document.exitFullscreen) {{
                    document.exitFullscreen();
                }} else if (document.webkitExitFullscreen) {{
                    document.webkitExitFullscreen();
                }}
            }}
        }}

        // 화면 꺼짐 방지
        async function keepAwake() {{
            try {{
                if ('wakeLock' in navigator) {{
                    await navigator.wakeLock.request('screen');
                }}
            }} catch (err) {{
                console.log('Wake Lock not supported');
            }}
        }}

        // 페이지 로드 시 실행
        document.addEventListener('DOMContentLoaded', function() {{
            keepAwake();

            // 로드 후 자동 전체화면 시도 (사용자 상호작용 필요할 수 있음)
            setTimeout(function() {{
                document.querySelector('.hint').style.animation = 'blinkText 2s ease-in-out infinite';
            }}, 1000);
        }});

        // 전체화면 변경 감지
        document.addEventListener('fullscreenchange', keepAwake);
        document.addEventListener('webkitfullscreenchange', keepAwake);
    </script>
</body>
</html>"""

    # 다운로드 버튼
    b64 = base64.b64encode(html_content.encode()).decode()
    href = f'data:text/html;base64,{b64}'

    st.markdown(f"""
        <a href="{href}" download="cheer_screen.html" style="
            display: block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px 40px;
            text-align: center;
            text-decoration: none;
            font-size: 24px;
            font-weight: bold;
            border-radius: 15px;
            margin: 20px 0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        ">
            📥 응원 화면 다운로드
        </a>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; margin-top: 20px;">
        <h4>📱 사용 방법</h4>
        <ol>
            <li><strong>다운로드 버튼</strong>을 눌러 파일 저장</li>
            <li>다운로드된 <strong>cheer_screen.html</strong> 파일 열기</li>
            <li><strong>화면 터치</strong>하면 전체화면 전환!</li>
            <li>다시 터치하면 전체화면 해제</li>
        </ol>
        <p style="margin-top: 10px; color: #666;">
            💡 <strong>iOS 팁:</strong> Safari에서 "홈 화면에 추가"하면 앱처럼 사용 가능!
        </p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.warning("👆 위에서 문구를 선택해야 다운로드할 수 있습니다!")

# 푸터
st.markdown("---")
st.markdown("""
    <p style="text-align: center; color: #888; font-size: 14px;">
        Made with ❤️ for 에듀테크AI(고) 분임 & 수학 분임
    </p>
""", unsafe_allow_html=True)
