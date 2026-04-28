# 📣 분임 응원 LED

모바일 액정에 응원 문구를 큼지막하게 띄워주는 단일 HTML 앱입니다.

## 기능
- 분임별(에듀테크AI(고)/수학) 예시 문구 4종 — 탭 한 번에 입력
- 직접 입력 / 미리보기 / 전체화면
- 효과 4종: **흐르기 / 깜빡임 / 무지개 / 고정**
- 전체화면 시 화면 어디든 탭 → 옵션 그대로 복귀
- 모바일 친화 글꼴 7종 (Black Han Sans, Noto Sans KR, Do Hyeon, Jua, Gugi, Gaegu, Nanum Pen)

## 흐르기 동작
- 오른쪽 화면 밖 → 왼쪽 화면 밖으로 흐름
- 마지막 글자가 사라진 뒤 **2초 대기**
- 다시 오른쪽 끝에서 동일 문구 반복

## 전체화면 글자 높이
- 한 줄 문구는 **화면 높이의 약 70%**로 자동 확대
- 여러 줄/긴 문구는 화면을 넘지 않는 최대 크기로 자동 조정

## GitHub Pages 배포
1. 새 Public 저장소 생성 (예: `cheer-led`)
2. `index.html` 업로드 → Commit
3. Settings → Pages → Branch: `main` / `(root)` → Save
4. 안내 주소(`https://아이디.github.io/cheer-led/`)를 모바일 브라우저로 접속

## 로컬 실행
`index.html` 더블클릭 → 브라우저에서 바로 동작합니다.
