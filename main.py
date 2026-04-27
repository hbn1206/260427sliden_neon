import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="응원 문구 만들기",
    page_icon="📣",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 메인 페이지 스타일
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Jua&family=Do+Hyeon&family=Gugi&display=swap');

    [data-testid="collapsedControl"] { display: none; }

    .main-title {
        font-family: 'Black Han Sans', sans-serif;
        font-size: 2.2rem;
        text-align: center;
        color: #FF6B6B;
        margin-bottom: 25px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }

    .section-box {
        background: linear-gradient(135deg, #667eea22, #764ba222);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        border: 1px solid #ddd;
    }

    .section-title {
        font-family: 'Jua', sans-serif;
        font-size: 1.3rem;
        color: #333;
        margin-bottom: 15px;
    }

    .preview-box {
        border-radius: 15px;
        padding: 40px 20px;
        text-align: center;
        min-height: 150px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }

    .preview-text {
        font-size: 2rem;
        font-weight: bold;
        word-break: keep-all;
    }

    .info-text {
        font-family: 'Jua', sans-serif;
        text-align: center;
        color: #666;
        font-size: 1rem;
        margin-top: 10px;
        line-height: 1.8;
    }

    .stDownloadButton > button {
        font-family: 'Jua', sans-serif !important;
        width: 100%;
        padding: 15px 30px !important;
        font-size: 1.3rem !important;
        border-radius: 15px !important;
        background: linear-gradient(135deg, #667eea, #764ba2) !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
    }
</style>
""", unsafe_allow_html=True)

# 샘플 문구
sample_messages = {
    "직접 입력": "",
    "에듀테크AI(고) 분임 - 화이팅": "에듀테크AI(고) 분임 화이팅! 💪",
    "에듀테크AI(고) 분임 - 최고": "에듀테크AI(고) 분임 최고! 🏆",
    "에듀테크AI(고) 분임 - 응원": "에듀테크AI(고) 분임 응원합니다! 📣",
    "수학 분임 - 화이팅": "수학 분임 화이팅! 💪",
    "수학 분임 - 최고": "수학 분임 최고! 🏆",
    "수학 분임 - 응원": "수학 분임 응원합니다! 📣",
}

# 배경색 설정
color_options = {
    "🖤 검정": {"bg": "#000000", "text": "#FFFFFF", "neon": "#00FFFF"},
    "❤️ 빨강": {"bg": "#CC0000", "text": "#FFFF00", "neon": "#FFFF00"},
    "💙 파랑": {"bg": "#0033AA", "text": "#FFFFFF", "neon": "#00FF88"},
    "💚 초록": {"bg": "#006600", "text": "#FFFFFF", "neon": "#FF69B4"},
    "💜 보라": {"bg": "#4B0082", "text": "#00FFFF", "neon": "#00FFFF"},
    "🧡 주황": {"bg": "#FF6600", "text": "#FFFFFF", "neon": "#FFFFFF"},
}

# 글꼴 옵션
font_options = {
    "Black Han Sans (굵은 고딕)": "Black Han Sans",
    "Jua (둥근 고딕)": "Jua",
    "Do Hyeon (네모 고딕)": "Do Hyeon",
    "Gugi (특이한 고딕)": "Gugi",
}

# ===== 메인 페이지 =====
st.markdown('<h1 class="main-title">🎉 응원 문구 만들기</h1>', unsafe_allow_html=True)

# 1. 문구 선택 섹션
st.markdown('<div class="section-box"><p class="section-title">📝 문구 선택</p>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
with col1:
    selected_sample = st.selectbox(
        "샘플 문구",
        list(sample_messages.keys()),
        label_visibility="collapsed"
    )

with col2:
    if selected_sample == "직접 입력":
        custom_text = st.text_input(
            "직접 입력",
            placeholder="응원 문구를 입력하세요",
            label_visibility="collapsed"
        )
        display_text = custom_text if custom_text else "응원 문구를 입력하세요"
    else:
        display_text = sample_messages[selected_sample]
        st.markdown(f"<p style='padding:8px; color:#333;'>{display_text}</p>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# 2. 스타일 설정 섹션
st.markdown('<div class="section-box"><p class="section-title">🎨 스타일 설정</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    selected_color = st.radio(
        "배경색",
        list(color_options.keys()),
        horizontal=False,
        label_visibility="collapsed"
    )

with col2:
    selected_font = st.selectbox(
        "글꼴 선택",
        list(font_options.keys())
    )

st.markdown('</div>', unsafe_allow_html=True)

# 3. 효과 선택 섹션
st.markdown('<div class="section-box"><p class="section-title">✨ 효과 선택</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    neon_effect = st.checkbox("💡 네온싸인 효과", value=True)
with col2:
    slide_effect = st.checkbox("🎬 슬라이드 효과", value=False)

st.markdown('</div>', unsafe_allow_html=True)

# 색상 및 폰트 가져오기
colors = color_options[selected_color]
font_family = font_options[selected_font]

# 4. 미리보기 섹션
st.markdown('<div class="section-box"><p class="section-title">👀 미리보기</p>', unsafe_allow_html=True)

preview_neon = ""
if neon_effect:
    preview_neon = f"text-shadow: 0 0 10px {colors['neon']}, 0 0 20px {colors['neon']}, 0 0 40px {colors['neon']};"

st.markdown(f'''
<div class="preview-box" style="background-color: {colors['bg']};">
    <span class="preview-text" style="color: {colors['text']}; font-family: '{font_family}', sans-serif; {preview_neon}">{display_text}</span>
</div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# 5. 전체화면 HTML 생성 함수
def create_fullscreen_html(text, colors, font_family, neon_effect, slide_effect):
    bg_color = colors['bg']
    text_color = colors['text']
    neon_color = colors['neon']

    neon_style = ""
    neon_keyframes = ""

    if neon_effect:
        neon_style = f"text-shadow: 0 0 10px {neon_color}, 0 0 20px {neon_color}, 0 0 40px {neon_color}, 0 0 80px {neon_color};"
        neon_keyframes = '''
        @keyframes neonPulse {
            from { text-shadow: 0 0 10px ''' + neon_color + ''', 0 0 20px ''' + neon_color + ''', 0 0 40px ''' + neon_color + '''; }
            to { text-shadow: 0 0 20px ''' + neon_color + ''', 0 0 40px ''' + neon_color + ''', 0 0 80px ''' + neon_color + ''', 0 0 120px ''' + neon_color + '''; }
        }
        '''

    slide_keyframes = '''
        @keyframes slideText {
            0% { transform: translateX(100vw); }
            100% { transform: translateX(-100%); }
        }
    '''

    animation_style = ""
    if neon_effect and slide_effect:
        animation_style = "animation: slideText 15s linear infinite, neonPulse 1.5s ease-in-out infinite alternate;"
    elif neon_effect:
        animation_style = "animation: neonPulse 1.5s ease-in-out infinite alternate;"
    elif slide_effect:
        animation_style = "animation: slideText 15s linear infinite;"

    html = '''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="mobile-web-app-capable" content="yes">
    <title>응원 문구</title>
    <link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Jua&family=Do+Hyeon&family=Gugi&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html, body { width: 100%; height: 100%; overflow: hidden; }
        body {
            background-color: ''' + bg_color + ''';
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: "''' + font_family + '''", sans-serif;
            cursor: pointer;
            -webkit-tap-highlight-color: transparent;
            -webkit-touch-callout: none;
            -webkit-user-select: none;
            user-select: none;
        }
        .container {
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }
        .cheer-text {
            color: ''' + text_color + ''';
            font-size: 15vw;
            font-weight: bold;
            text-align: center;
            word-break: keep-all;
            line-height: 1.3;
            padding: 20px;
            white-space: nowrap;
            ''' + neon_style + '''
            ''' + animation_style + '''
        }
        .guide {
            position: fixed;
            bottom: 30px;
            left: 0;
            right: 0;
            text-align: center;
            color: ''' + text_color + ''';
            opacity: 0.4;
            font-size: 14px;
            font-family: sans-serif;
        }
        ''' + neon_keyframes + '''
        ''' + slide_keyframes + '''
    </style>
</head>
<body onclick="toggleFullscreen()">
    <div class="container">
        <div class="cheer-text">''' + text + '''</div>
    </div>
    <div class="guide">👆 터치하여 전체화면 전환</div>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            setTimeout(requestFullscreen, 500);
        });
        function requestFullscreen() {
            var elem = document.documentElement;
            if (elem.requestFullscreen) { elem.requestFullscreen().catch(function(){}); }
            else if (elem.webkitRequestFullscreen) { elem.webkitRequestFullscreen(); }
            else if (elem.msRequestFullscreen) { elem.msRequestFullscreen(); }
        }
        function exitFullscreen() {
            if (document.exitFullscreen) { document.exitFullscreen().catch(function(){}); }
            else if (document.webkitExitFullscreen) { document.webkitExitFullscreen(); }
            else if (document.msExitFullscreen) { document.msExitFullscreen(); }
        }
        function toggleFullscreen() {
            if (!document.fullscreenElement && !document.webkitFullscreenElement) {
                requestFullscreen();
            } else {
                exitFullscreen();
            }
        }
        async function keepScreenOn() {
            if ('wakeLock' in navigator) {
                try { await navigator.wakeLock.request('screen'); } catch (err) {}
            }
        }
        keepScreenOn();
    </script>
</body>
</html>'''
    return html

# 6. 전체화면 버튼 섹션
st.markdown('<div class="section-box"><p class="section-title">📺 전체화면 모드</p>', unsafe_allow_html=True)

html_content = create_fullscreen_html(display_text, colors, font_family, neon_effect, slide_effect)

st.download_button(
    label="📥 응원 화면 다운로드 (HTML)",
    data=html_content,
    file_name="cheer_screen.html",
    mime="text/html"
)

st.markdown('''
<p class="info-text">
📱 <b>사용 방법</b><br>
1. 위 버튼을 눌러 HTML 파일 다운로드<br>
2. 다운로드된 파일을 브라우저로 열기<br>
3. 화면 터치하면 전체화면 전환!
</p>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('''
<p style="text-align:center; color:#999; font-size:0.9rem; margin-top:30px;">
    💡 iOS: "파일" 앱에서 HTML 파일을 Safari로 열어주세요<br>
    💡 Android: 다운로드 폴더에서 파일을 Chrome으로 열어주세요
</p>
''', unsafe_allow_html=True)
