
import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="🎉 응원 문구",
    page_icon="📣",
    layout="wide",
    initial_sidebar_state="expanded"
)

# URL 파라미터로 상태 관리
query_params = st.query_params
is_fullscreen = query_params.get("fullscreen", "false") == "true"

# 샘플 문구 목록
SAMPLE_MESSAGES = {
    "직접 입력": "",
    "에듀테크AI(고) 분임 - 화이팅": "에듀테크AI(고) 분임 화이팅! 💪",
    "에듀테크AI(고) 분임 - 최고": "에듀테크AI(고) 분임 최고! 🏆",
    "에듀테크AI(고) 분임 - 응원": "에듀테크AI(고) 분임을 응원합니다! 📣",
    "수학 분임 - 화이팅": "수학 분임 화이팅! 💪",
    "수학 분임 - 최고": "수학 분임 최고! 🏆",
    "수학 분임 - 응원": "수학 분임을 응원합니다! 📣",
}

# 배경색과 글자색 조합
COLOR_SCHEMES = {
    "🖤 검정": {"bg": "#000000", "text": "#FFFFFF", "neon": "#00FFFF"},
    "❤️ 빨강": {"bg": "#CC0000", "text": "#FFFF00", "neon": "#FFFF00"},
    "💙 파랑": {"bg": "#0066CC", "text": "#FFFFFF", "neon": "#00FF00"},
    "💚 초록": {"bg": "#006633", "text": "#FFFFFF", "neon": "#FF69B4"},
    "💜 보라": {"bg": "#660099", "text": "#00FFFF", "neon": "#00FFFF"},
    "🤍 흰색": {"bg": "#FFFFFF", "text": "#FF1493", "neon": "#FF1493"},
}

# 세션 상태 초기화
if 'selected_sample' not in st.session_state:
    st.session_state.selected_sample = "직접 입력"
if 'custom_message' not in st.session_state:
    st.session_state.custom_message = "화이팅! 💪"
if 'selected_color' not in st.session_state:
    st.session_state.selected_color = "🖤 검정"
if 'neon_effect' not in st.session_state:
    st.session_state.neon_effect = True
if 'slide_effect' not in st.session_state:
    st.session_state.slide_effect = False

# =====================
# 전체화면 모드
# =====================
if is_fullscreen:
    # 저장된 설정 불러오기
    message = query_params.get("msg", "화이팅! 💪")
    color_key = query_params.get("color", "🖤 검정")
    neon = query_params.get("neon", "true") == "true"
    slide = query_params.get("slide", "false") == "true"

    colors = COLOR_SCHEMES.get(color_key, COLOR_SCHEMES["🖤 검정"])
    bg_color = colors["bg"]
    text_color = colors["text"]
    neon_color = colors["neon"]

    # 네온 효과 CSS
    neon_css = ""
    if neon:
        neon_css = f"""
            text-shadow: 
                0 0 10px {neon_color},
                0 0 20px {neon_color},
                0 0 40px {neon_color},
                0 0 80px {neon_color};
            animation: neonPulse 1.5s ease-in-out infinite alternate;
        """

    # 슬라이드 효과 CSS
    slide_css = ""
    slide_animation = ""
    if slide:
        slide_css = "animation: slideText 15s linear infinite;"
        slide_animation = """
            @keyframes slideText {
                0% { transform: translateX(100vw); }
                100% { transform: translateX(-100%); }
            }
        """

    # 전체화면 HTML (터치 시 복귀 + 실제 전체화면)
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
                z-index: 999999;
                overflow: hidden;
            }}

            .message {{
                font-size: clamp(3rem, 12vw, 10rem);
                font-weight: bold;
                color: {text_color};
                text-align: center;
                padding: 20px;
                white-space: nowrap;
                {neon_css}
                {slide_css}
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

            {slide_animation}

            .hint {{
                position: fixed;
                bottom: 30px;
                left: 50%;
                transform: translateX(-50%);
                color: {text_color};
                opacity: 0.6;
                font-size: 1.2rem;
                text-align: center;
                pointer-events: none;
            }}

            .back-btn {{
                position: fixed;
                top: 20px;
                left: 20px;
                background: rgba(255,255,255,0.2);
                border: none;
                color: {text_color};
                padding: 15px 25px;
                font-size: 1.2rem;
                border-radius: 10px;
                cursor: pointer;
                z-index: 1000000;
            }}

            .back-btn:hover {{
                background: rgba(255,255,255,0.4);
            }}
        </style>
    </head>
    <body>
        <div class="fullscreen-container" id="container" onclick="goBack()">
            <div class="message">{message}</div>
            <div class="hint">👆 화면을 터치하면 설정 화면으로 돌아갑니다</div>
        </div>
        <button class="back-btn" onclick="goBack()">⬅️ 뒤로</button>

        <script>
            // 전체화면 API 실행
            function enterFullscreen() {{
                var elem = document.documentElement;
                if (elem.requestFullscreen) {{
                    elem.requestFullscreen();
                }} else if (elem.webkitRequestFullscreen) {{
                    elem.webkitRequestFullscreen();
                }} else if (elem.msRequestFullscreen) {{
                    elem.msRequestFullscreen();
                }}
            }}

            // 페이지 로드 시 전체화면 진입 시도
            document.addEventListener('DOMContentLoaded', function() {{
                // 약간의 딜레이 후 전체화면 시도 (사용자 제스처 필요할 수 있음)
                setTimeout(enterFullscreen, 100);
            }});

            // 클릭으로도 전체화면 진입 (사용자 제스처)
            document.addEventListener('click', function(e) {{
                if (!document.fullscreenElement) {{
                    enterFullscreen();
                }}
            }}, {{once: true}});

            // 뒤로 가기 함수
            function goBack() {{
                // 전체화면 종료
                if (document.exitFullscreen) {{
                    document.exitFullscreen();
                }} else if (document.webkitExitFullscreen) {{
                    document.webkitExitFullscreen();
                }}

                // URL에서 fullscreen 파라미터 제거하고 이동
                var url = new URL(window.parent.location.href);
                url.searchParams.delete('fullscreen');
                url.searchParams.delete('msg');
                url.searchParams.delete('color');
                url.searchParams.delete('neon');
                url.searchParams.delete('slide');
                window.parent.location.href = url.toString();
            }}
        </script>
    </body>
    </html>
    """

    # Streamlit 기본 UI 숨기기
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            .stApp > header {display: none;}
            section[data-testid="stSidebar"] {display: none;}
            .block-container {padding: 0 !important; max-width: 100% !important;}
            .stApp {overflow: hidden;}
        </style>
    """, unsafe_allow_html=True)

    # 전체화면 HTML 렌더링
    components.html(fullscreen_html, height=800, scrolling=False)

# =====================
# 설정 화면 (초기 화면)
# =====================
else:
    st.title("📣 응원 문구 웹페이지")
    st.markdown("---")

    # 사이드바 설정
    with st.sidebar:
        st.header("⚙️ 설정")

        # 샘플 문구 선택
        st.subheader("📝 문구 선택")
        selected = st.selectbox(
            "샘플 문구를 선택하세요",
            options=list(SAMPLE_MESSAGES.keys()),
            key="sample_select"
        )
        st.session_state.selected_sample = selected

        # 직접 입력
        if selected == "직접 입력":
            custom_msg = st.text_input(
                "응원 문구를 입력하세요",
                value=st.session_state.custom_message,
                key="custom_input"
            )
            st.session_state.custom_message = custom_msg
            display_message = custom_msg
        else:
            display_message = SAMPLE_MESSAGES[selected]

        st.markdown("---")

        # 배경색 선택
        st.subheader("🎨 배경색 선택")
        color_choice = st.selectbox(
            "배경색을 선택하세요",
            options=list(COLOR_SCHEMES.keys()),
            key="color_select"
        )
        st.session_state.selected_color = color_choice

        st.markdown("---")

        # 효과 선택
        st.subheader("✨ 효과 선택")
        neon = st.checkbox("💡 네온싸인 효과", value=st.session_state.neon_effect, key="neon_check")
        slide = st.checkbox("🎬 슬라이드 효과 (오른쪽→왼쪽)", value=st.session_state.slide_effect, key="slide_check")
        st.session_state.neon_effect = neon
        st.session_state.slide_effect = slide

    # 현재 색상 가져오기
    colors = COLOR_SCHEMES[st.session_state.selected_color]
    bg_color = colors["bg"]
    text_color = colors["text"]
    neon_color = colors["neon"]

    # 미리보기
    st.subheader("👀 미리보기")

    # 네온 효과 CSS
    neon_style = ""
    if st.session_state.neon_effect:
        neon_style = f"""
            text-shadow: 
                0 0 10px {neon_color},
                0 0 20px {neon_color},
                0 0 40px {neon_color};
            animation: neonPulse 1.5s ease-in-out infinite alternate;
        """

    # 슬라이드 효과 CSS
    slide_style = ""
    slide_keyframes = ""
    if st.session_state.slide_effect:
        slide_style = "animation: slideText 15s linear infinite;"
        slide_keyframes = """
            @keyframes slideText {
                0% { transform: translateX(100%); }
                100% { transform: translateX(-100%); }
            }
        """

    preview_html = f"""
    <style>
        @keyframes neonPulse {{
            from {{ text-shadow: 0 0 10px {neon_color}, 0 0 20px {neon_color}; }}
            to {{ text-shadow: 0 0 20px {neon_color}, 0 0 40px {neon_color}, 0 0 80px {neon_color}; }}
        }}
        {slide_keyframes}
    </style>
    <div style="
        background-color: {bg_color};
        padding: 60px 20px;
        border-radius: 20px;
        text-align: center;
        overflow: hidden;
        margin: 20px 0;
    ">
        <div style="
            font-size: clamp(1.5rem, 5vw, 3rem);
            font-weight: bold;
            color: {text_color};
            white-space: nowrap;
            {neon_style}
            {slide_style}
        ">
            {display_message if display_message else "문구를 입력하세요"}
        </div>
    </div>
    """

    st.markdown(preview_html, unsafe_allow_html=True)

    st.markdown("---")

    # 전체화면 버튼 - URL 파라미터 방식
    st.subheader("📺 전체화면 모드")
    st.info("👆 전체화면에서 화면을 터치하면 설정 화면으로 돌아옵니다.")

    # URL 생성을 위한 파라미터
    import urllib.parse
    msg_encoded = urllib.parse.quote(display_message if display_message else "화이팅! 💪")
    color_encoded = urllib.parse.quote(st.session_state.selected_color)
    neon_str = "true" if st.session_state.neon_effect else "false"
    slide_str = "true" if st.session_state.slide_effect else "false"

    # 전체화면 버튼 (JavaScript로 URL 변경)
    fullscreen_button_html = f"""
    <style>
        .fullscreen-btn {{
            display: block;
            width: 100%;
            padding: 20px 40px;
            font-size: 1.5rem;
            font-weight: bold;
            color: white;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border: none;
            border-radius: 15px;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
            margin: 20px 0;
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        .fullscreen-btn:hover {{
            transform: scale(1.02);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        }}
    </style>
    <button class="fullscreen-btn" onclick="goFullscreen()">
        📺 전체화면으로 보기
    </button>
    <script>
        function goFullscreen() {{
            var url = new URL(window.location.href);
            url.searchParams.set('fullscreen', 'true');
            url.searchParams.set('msg', '{msg_encoded}');
            url.searchParams.set('color', '{color_encoded}');
            url.searchParams.set('neon', '{neon_str}');
            url.searchParams.set('slide', '{slide_str}');
            window.location.href = url.toString();
        }}
    </script>
    """

    components.html(fullscreen_button_html, height=100)

    # 사용 안내
    st.markdown("---")
    st.markdown("""
    ### 📱 사용 방법
    1. **문구 선택**: 샘플 문구를 선택하거나 직접 입력하세요
    2. **배경색 선택**: 원하는 배경색을 선택하세요 (글자색 자동 변경)
    3. **효과 선택**: 네온싸인, 슬라이드 효과를 선택하세요
    4. **전체화면**: 버튼을 누르면 기기 전체화면으로 전환됩니다
    5. **복귀**: 전체화면에서 화면을 터치하면 설정 화면으로 돌아옵니다
    """)
