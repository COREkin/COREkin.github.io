# corekin.github.io

GitHub Pages 사용자 사이트. 빌드 없이 정적 파일을 그대로 서비스한다 (main 브랜치 루트, `.nojekyll`).

| 경로 | URL | 내용 |
|---|---|---|
| `index.html` | https://corekin.github.io/ | 소개와 링크 |
| `kinboard/privacy/index.html` | https://corekin.github.io/kinboard/privacy/ | Kin Board 개인정보처리방침 (ko·ja·en) |
| `assets/style.css` | | 공통 스타일 |

## 수정 규칙

- 개인정보처리방침 URL은 Play Console과 앱(`task-kanban-board/app/platform/usePlatform.ts`의 `PRIVACY_POLICY_URL`)에 등록돼 있다. 경로를 바꾸지 않는다
- 방침은 앱의 실제 동작과 Play Console 데이터 보안 답변에 맞춘다. 앱 동작이 바뀌면(권한·SDK·백업 설정 등) 세 언어 섹션을 함께 고치고 시행일을 갱신한다
- 미리보기: `python3 -m http.server 8000` 후 http://localhost:8000
