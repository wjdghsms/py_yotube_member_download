# 유튜브 멤버십 동영상 다운로더

유튜브 멤버십 전용 동영상을 다운로드하는 Python 스크립트입니다.

## 요구 사항

- Python 3.8 이상
- yt-dlp

## 설치

```powershell
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
.\venv\Scripts\Activate.ps1

# 의존성 설치
pip install -r requirements.txt
```

## 사용법

### 기본 명령어

```powershell
python src/download_membership.py <URL> [옵션]
```

### 옵션

| 옵션 | 단축 | 설명 | 기본값 |
|------|------|------|--------|
| `--browser` | `-b` | 쿠키를 가져올 브라우저 | chrome |
| `--playlist` | `-p` | 재생목록 전체 다운로드 | - |
| `--cookies` | `-c` | 쿠키 파일 경로 | - |

### 지원 브라우저

- chrome
- firefox
- edge
- brave
- opera
- vivaldi

## 예시

### 단일 영상 다운로드

```powershell
python src/download_membership.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Edge 브라우저 쿠키 사용

```powershell
python src/download_membership.py "https://www.youtube.com/watch?v=VIDEO_ID" --browser edge
```

### 재생목록 전체 다운로드

```powershell
python src/download_membership.py "https://www.youtube.com/playlist?list=PLAYLIST_ID" --playlist
```

### 쿠키 파일 사용

```powershell
python src/download_membership.py "https://www.youtube.com/watch?v=VIDEO_ID" --cookies cookies.txt
```

## 쿠키 설정 방법

### 방법 1: 브라우저에서 직접 가져오기 (권장)

1. 사용할 브라우저에서 유튜브 멤버십 계정으로 로그인
2. 해당 브라우저를 **완전히 종료** (시스템 트레이 포함)
3. 스크립트 실행

```powershell
python src/download_membership.py "URL" --browser chrome
```

> **주의**: 브라우저가 실행 중이면 쿠키 데이터베이스 접근 오류가 발생합니다.

### 방법 2: 쿠키 파일 사용 (브라우저 실행 중에도 가능)

1. Chrome 확장 프로그램 설치: "Get cookies.txt LOCALLY"
2. 유튜브 사이트에서 확장 프로그램 클릭
3. "Export" 버튼으로 `cookies.txt` 저장
4. 스크립트와 같은 폴더에 저장 후 실행

```powershell
python src/download_membership.py "URL" --cookies cookies.txt
```

## 출력 파일

- **단일 영상**: `영상제목.mp4`
- **재생목록**: `재생목록명/번호 - 영상제목.mp4`

## 문제 해결

### "Could not copy Chrome cookie database" 오류

**원인**: 브라우저가 실행 중이어서 쿠키 파일이 잠겨 있음

**해결 방법**:
1. 브라우저 완전 종료 후 재시도
2. 다른 브라우저 사용 (`--browser edge`)
3. 쿠키 파일 방식 사용 (`--cookies cookies.txt`)

### 멤버십 영상 접근 불가

**원인**: 로그인 정보가 없거나 멤버십이 없는 계정

**해결 방법**:
1. 브라우저에서 멤버십 계정으로 로그인 확인
2. 해당 채널의 멤버십이 활성화되어 있는지 확인

## 도움말

```powershell
python src/download_membership.py --help
```
