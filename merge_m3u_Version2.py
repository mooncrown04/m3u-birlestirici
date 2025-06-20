import requests
import sys

def fetch_m3u(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return ""

def merge_m3u(url_list, output_file="merged.m3u"):
    all_lines = []
    for url in url_list:
        print(f"Fetching: {url}")
        content = fetch_m3u(url)
        if content:
            lines = content.strip().splitlines()
            if lines and lines[0].strip() == "#EXTM3U":
                lines = lines[1:]
            all_lines.extend(lines)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for line in all_lines:
            f.write(line.strip() + "\n")
    print(f"Merged {len(url_list)} m3u files into {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python merge_m3u.py https://raw.githubusercontent.com/Lunedor/iptvTR/refs/heads/main/FilmArsiv.m3u https://raw.githubusercontent.com/Zerk1903/zerkfilm/refs/heads/main/Diziler.m3u ...")
        sys.exit(1)
    urls = sys.argv[1:]
    merge_m3u(urls)
