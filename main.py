
import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="🎉 응원 문구 생성기",
    page_icon="📣",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 샘플 문구 정의
SAMPLE_MESSAGES = {
    "에듀테크AI(고) 분임": [
        "에듀테크AI(고) 분임 화이팅! 💪",
        "우리는 에듀테크AI(고)! 최고야! 🌟",
        "에듀테크AI(고) 분임 파이팅! 🔥",
        "함께하면 할 수 있어! 에듀테크AI(고)! ✨"
    ],
    "수학 분임": [
        "수학 분임 화이팅! 📐",
        "수학의 힘! 우리가 최고! 🧮",
        "수학 분임 파이팅! 💯",
        "계산보다 빠른 열정! 수학 분임! 🚀"
    ]
}

# CSS 스타일
def get_styles():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@700;900&display=swap');

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        .cheer-container {
            width: 100%;
            min-height: 70vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            border-radius: 20px;
            overflow: hidden;
            position: relative;
        }

        .cheer-text {
            font-family: 'Noto Sans KR', sans-serif;
            font-size: clamp(2rem, 8vw, 6rem);
            font-weight: 900;
            text-align: center;
            padding: 40px;
            line-height: 1.4;
        }

        /* 기본 스타일 */
        .style-basic {
            color: #ffffff;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        /* 네온 스타일 */
        .style-neon {
            color: #fff;
            text-shadow:
                0 0 5px #fff,
                0 0 10px #fff,
                0 0 20px #ff00de,
                0 0 30px #ff00de,
                0 0 40px #ff00de,
                0 0 55px #ff00de,
                0 0 70px #ff00de;
            animation: neon-flicker 1.5s infinite alternate;
        }

        @keyframes neon-flicker {
            0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {
                text-shadow:
                    0 0 5px #fff,
                    0 0 10px #fff,
                    0 0 20px #ff00de,
                    0 0 30px #ff00de,
                    0 0 40px #ff00de,
                    0 0 55px #ff00de,
                    0 0 70px #ff00de;
            }
            20%, 24%, 55% {
                text-shadow: none;
            }
        }

        /* 슬라이드 스타일 */
        .style-slide {
            color: #00f5ff;
            animation: slide-in 2s ease-in-out infinite;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.5);
        }

        @keyframes slide-in {
            0% { transform: translateX(-100%); opacity: 0; }
            20% { transform: translateX(0); opacity: 1; }
            80% { transform: translateX(0); opacity: 1; }
            100% { transform: translateX(100%); opacity: 0; }
        }

        /* 네온 + 슬라이드 */
        .style-neon-slide {
            color: #fff;
            text-shadow:
                0 0 5px #fff,
                0 0 10px #fff,
                0 0 20px #00ff88,
                0 0 30px #00ff88,
                0 0 40px #00ff88;
            animation: slide-in 2s ease-in-out infinite, neon-pulse 0.5s ease-in-out infinite alternate;
        }

        @keyframes neon-pulse {
            from {
                text-shadow:
                    0 0 5px #fff,
                    0 0 10px #fff,
                    0 0 20px #00ff88,
                    0 0 30px #00ff88,
                    0 0 40px #00ff88;
            }
            to {
                text-shadow:
                    0 0 10px #fff,
                    0 0 20px #fff,
                    0 0 30px #00ff88,
                    0 0 50px #00ff88,
                    0 0 70px #00ff88;
            }
        }

        /* 전체화면 버튼 */
        .fullscreen-btn {
            position: absolute;
            top: 15px;
            right: 15px;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 30px;
            cursor: pointer;
            z-index: 1000;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        }

        .fullscreen-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
        }

        /* 배경 애니메이션 */
        .bg-animation {
            position: absolute;
            width: 100%;
            height: 100%;
            overflow: hidden;
            z-index: 0;
        }

        .bg-animation span {
            position: absolute;
            display: block;
            width: 20px;
            height: 20px;
            background: rgba(255, 255, 255, 0.1);
            animation: move 25s linear infinite;
            bottom: -150px;
            border-radius: 50%;
        }

        .bg-animation span:nth-child(1) { left: 10%; width: 80px; height: 80px; animation-delay: 0s; }
        .bg-animation span:nth-child(2) { left: 20%; width: 20px; height: 20px; animation-delay: 2s; animation-duration: 12s; }
        .bg-animation span:nth-child(3) { left: 35%; width: 60px; height: 60px; animation-delay: 4s; }
        .bg-animation span:nth-child(4) { left: 50%; width: 40px; height: 40px; animation-delay: 0s; animation-duration: 18s; }
        .bg-animation span:nth-child(5) { left: 65%; width: 20px; height: 20px; animation-delay: 0s; }
        .bg-animation span:nth-child(6) { left: 80%; width: 50px; height: 50px; animation-delay: 3s; }
        .bg-animation span:nth-child(7) { left: 90%; width: 100px; height: 100px; animation-delay: 7s; }

        @keyframes move {
            0% { transform: translateY(0) rotate(0deg); opacity: 1; }
            100% { transform: translateY(-1000px) rotate(720deg); opacity: 0; }
        }

        .text-wrapper {
            z-index: 10;
            position: relative;
        }
    </style>
    """

# 메인 앱
def main():
    st.markdown(get_styles(), unsafe_allow_html=True)

    st.markdown("# 🎉 응원 문구 생성기")
    st.markdown("---")

    # 설정 영역
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### ✏️ 문구 입력")
        input_method = st.radio(
            "입력 방식 선택:",
            ["직접 입력", "샘플 문구 선택"],
            horizontal=True
        )

        if input_method == "직접 입력":
            cheer_text = st.text_area(
                "응원 문구를 입력하세요:",
                value="화이팅! 💪",
                height=100
            )
        else:
            group = st.selectbox(
                "분임 선택:",
                list(SAMPLE_MESSAGES.keys())
            )
            cheer_text = st.selectbox(
                "문구 선택:",
                SAMPLE_MESSAGES[group]
            )

    with col2:
        st.markdown("### ⚙️ 효과 설정")

        use_neon = st.checkbox("✨ 네온싸인 효과", value=True)
        use_slide = st.checkbox("🎬 슬라이드 효과", value=False)

        # 스타일 클래스 결정
        if use_neon and use_slide:
            style_class = "style-neon-slide"
        elif use_neon:
            style_class = "style-neon"
        elif use_slide:
            style_class = "style-slide"
        else:
            style_class = "style-basic"

        st.markdown("### 🎨 배경 색상")
        bg_option = st.selectbox(
            "배경 선택:",
            ["기본 (그라데이션)", "빨강", "파랑", "검정", "보라"]
        )

        bg_colors = {
            "기본 (그라데이션)": "linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%)",
            "빨강": "linear-gradient(135deg, #8B0000 0%, #DC143C 100%)",
            "파랑": "linear-gradient(135deg, #000080 0%, #0066CC 100%)",
            "검정": "linear-gradient(135deg, #000000 0%, #333333 100%)",
            "보라": "linear-gradient(135deg, #4B0082 0%, #9400D3 100%)"
        }
        bg_style = bg_colors[bg_option]

    st.markdown("---")

    # 미리보기 영역
    st.markdown("### 📺 미리보기")

    # HTML 컴포넌트 생성
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        {get_styles()}
        <style>
            body {{
                margin: 0;
                padding: 0;
                font-family: 'Noto Sans KR', sans-serif;
            }}
            .cheer-container {{
                background: {bg_style};
            }}
        </style>
    </head>
    <body>
        <div class="cheer-container" id="cheerContainer">
            <div class="bg-animation">
                <span></span><span></span><span></span>
                <span></span><span></span><span></span><span></span>
            </div>
            <button class="fullscreen-btn" onclick="toggleFullscreen()">📺 전체화면</button>
            <div class="text-wrapper">
                <div class="cheer-text {style_class}">{cheer_text}</div>
            </div>
        </div>

        <script>
            function toggleFullscreen() {{
                const elem = document.getElementById('cheerContainer');
                if (!document.fullscreenElement) {{
                    if (elem.requestFullscreen) {{
                        elem.requestFullscreen();
                    }} else if (elem.webkitRequestFullscreen) {{
                        elem.webkitRequestFullscreen();
                    }} else if (elem.msRequestFullscreen) {{
                        elem.msRequestFullscreen();
                    }}
                }} else {{
                    if (document.exitFullscreen) {{
                        document.exitFullscreen();
                    }}
                }}
            }}

            // 전체화면 상태 변경 시 버튼 텍스트 변경
            document.addEventListener('fullscreenchange', function() {{
                const btn = document.querySelector('.fullscreen-btn');
                if (document.fullscreenElement) {{
                    btn.textContent = '❌ 전체화면 종료';
                }} else {{
                    btn.textContent = '📺 전체화면';
                }}
            }});
        </script>
    </body>
    </html>
    """

    components.html(html_content, height=500, scrolling=False)

    # 사용 안내
    st.markdown("---")
    st.markdown("### 📱 사용 방법")
    st.info("""
    1. **문구 입력**: 직접 입력하거나 샘플 문구를 선택하세요
    2. **효과 선택**: 네온싸인, 슬라이드 효과를 선택하세요
    3. **전체화면**: '📺 전체화면' 버튼을 클릭하면 전체화면으로 표시됩니다
    4. **모바일/태블릿**: 터치 기기에서도 바로 사용 가능합니다!
    """)

if __name__ == "__main__":
    main()

