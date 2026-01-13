"""
유튜브 멤버십 동영상 다운로드 스크립트
- 브라우저 쿠키를 사용하여 멤버십 인증

사용법:
    python download_membership.py <URL> [--browser BROWSER] [--playlist] [--cookies FILE]

예시:
    python download_membership.py "https://www.youtube.com/watch?v=xxxxx"
    python download_membership.py "https://www.youtube.com/watch?v=xxxxx" --browser edge
    python download_membership.py "https://www.youtube.com/playlist?list=xxxxx" --playlist
    python download_membership.py "https://www.youtube.com/watch?v=xxxxx" --cookies cookies.txt
"""

import argparse
import subprocess
import sys


def download_video(video_url: str, browser: str = "chrome", cookies_file: str = None):
    """
    유튜브 멤버십 동영상 다운로드

    Args:
        video_url: 다운로드할 유튜브 URL
        browser: 쿠키를 가져올 브라우저 (chrome, firefox, edge, brave 등)
        cookies_file: 쿠키 파일 경로 (Netscape 형식)
    """

    # yt-dlp 명령어 구성
    cmd = [
        sys.executable, "-m", "yt_dlp",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "-o", "%(title)s.%(ext)s",
        "--merge-output-format", "mp4",
    ]

    # 쿠키 옵션 추가
    if cookies_file:
        cmd.extend(["--cookies", cookies_file])
        print(f"쿠키 파일 사용: {cookies_file}")
    else:
        cmd.extend(["--cookies-from-browser", browser])
        print(f"브라우저 쿠키 사용: {browser}")

    cmd.append(video_url)

    print(f"다운로드 시작: {video_url}")
    print("-" * 50)

    try:
        subprocess.run(cmd, check=True)
        print("-" * 50)
        print("다운로드 완료!")
    except subprocess.CalledProcessError as e:
        print(f"다운로드 실패: {e}")
        sys.exit(1)


def download_playlist(playlist_url: str, browser: str = "chrome", cookies_file: str = None):
    """
    유튜브 멤버십 재생목록 다운로드

    Args:
        playlist_url: 다운로드할 재생목록 URL
        browser: 쿠키를 가져올 브라우저
        cookies_file: 쿠키 파일 경로 (Netscape 형식)
    """

    cmd = [
        sys.executable, "-m", "yt_dlp",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "-o", "%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s",
        "--merge-output-format", "mp4",
        "--yes-playlist",
    ]

    # 쿠키 옵션 추가
    if cookies_file:
        cmd.extend(["--cookies", cookies_file])
        print(f"쿠키 파일 사용: {cookies_file}")
    else:
        cmd.extend(["--cookies-from-browser", browser])
        print(f"브라우저 쿠키 사용: {browser}")

    cmd.append(playlist_url)

    print(f"재생목록 다운로드 시작: {playlist_url}")
    print("-" * 50)

    try:
        subprocess.run(cmd, check=True)
        print("-" * 50)
        print("재생목록 다운로드 완료!")
    except subprocess.CalledProcessError as e:
        print(f"다운로드 실패: {e}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="유튜브 멤버십 동영상 다운로드 (브라우저 쿠키 인증)"
    )
    parser.add_argument(
        "url",
        help="다운로드할 유튜브 영상 또는 재생목록 URL"
    )
    parser.add_argument(
        "--browser", "-b",
        default="chrome",
        choices=["chrome", "firefox", "edge", "brave", "opera", "vivaldi"],
        help="쿠키를 가져올 브라우저 (기본값: chrome)"
    )
    parser.add_argument(
        "--playlist", "-p",
        action="store_true",
        help="재생목록 전체 다운로드"
    )
    parser.add_argument(
        "--cookies", "-c",
        help="쿠키 파일 경로 (브라우저 실행 중일 때 사용)"
    )

    args = parser.parse_args()

    print("=" * 60)
    print("유튜브 멤버십 동영상 다운로드")
    print("=" * 60)

    if args.playlist:
        download_playlist(args.url, args.browser, args.cookies)
    else:
        download_video(args.url, args.browser, args.cookies)
