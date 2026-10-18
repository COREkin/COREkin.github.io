# corekin.github.io

GitHub Pages 사용자 사이트. 정적 파일을 main 브랜치 루트에서 그대로 서비스한다(`.nojekyll`). 포트폴리오는 MyPortfolio(CloudFront)의 디자인·콘텐츠를 정적 HTML로 옮긴 것이다.

| 경로 | URL | 내용 |
|---|---|---|
| `index.html` · `ja/` · `ko/` | https://corekin.github.io/ · `/ja/` · `/ko/` | 포트폴리오 (en·ja·ko). `scripts/build.py`가 생성한다 |
| `kinboard/privacy/index.html` | https://corekin.github.io/kinboard/privacy/ | Kin Board 개인정보처리방침 (ko·ja·en 한 페이지). 직접 편집한다 |
| `assets/style.css` | | 공통 스타일 (MyPortfolio 디자인 토큰) |
| `images/` · `papers/` | | 프로필 사진, 논문 PDF |

## 포트폴리오 수정

1. `scripts/build.py`의 `CONTENT`(언어별)·`SKILLS`·`certifications()`를 고친다. 콘텐츠 정본은 `MyPortfolio/portfolio-website/content/{en,ja,ko}/*.md`라서 그쪽과 함께 고친다
2. `python3 scripts/build.py`로 세 페이지를 다시 만든다 (Python 3.9 이상, 표준 라이브러리만)
3. 새 아이콘을 쓰면 `ICONS`에 이름을 추가한다. 폰트 요청이 이 목록만 받아 온다

루트(`/`)는 처음 방문한 브라우저 언어가 ko·ja면 `/ko/`·`/ja/`로 보낸다. 언어 메뉴에서 고른 언어는 `localStorage['preferred-language']`에 남아 이후 자동 이동을 멈춘다.

## 개인정보처리방침 수정 규칙

- URL은 Play Console과 앱(`task-kanban-board/app/platform/usePlatform.ts`의 `PRIVACY_POLICY_URL`)에 등록돼 있다. 경로를 바꾸지 않는다
- 방침은 앱의 실제 동작과 Play Console 데이터 보안 답변에 맞춘다. 앱 동작이 바뀌면(권한·SDK·백업 설정 등) 세 언어 섹션을 함께 고치고 시행일을 갱신한다

## 미리보기

```bash
python3 -m http.server 8000   # http://localhost:8000
```
