import yt_dlp
import os
import re
import requests
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
from tqdm import tqdm
import re

def sanitize_title(title):
    return re.sub(r'[\\/*?:"<>|]', "", title)

def download_thumbnail(thumbnail_url):
    try:
        response = requests.get(thumbnail_url, stream=True)
        response.raise_for_status()
        return response.content
    except Exception as e:
        print(f"❌ Erro ao baixar thumbnail: {e}")
        return None

def add_cover_to_mp3(mp3_file, image_data):
    try:
        audio = MP3(mp3_file, ID3=ID3)
        try:
            audio.add_tags()
        except error:
            pass

        audio.tags.add(
            APIC(
                encoding=3,
                mime='image/jpeg',
                type=3,  
                desc='Cover',
                data=image_data
            )
        )
        audio.save()
        print(f"✅ Capa adicionada ao MP3: {mp3_file}")
    except Exception as e:
        print(f"❌ Erro ao adicionar capa: {e}")

def strip_ansi_codes(text):
    return re.sub(r'\x1B\[[0-?]*[ -/]*[@-~]', '', text)

def download_audio(url, quality):
    url = url.replace("music.youtube.com", "www.youtube.com")

    save_directory = os.path.join(os.getcwd(), 'Musics')
    os.makedirs(save_directory, exist_ok=True)

    quality_audio = '320' if quality == 1 else '64'
    
    input("Pressione ENTER para confirmar o download...")
    print("🎵 Baixando...")

    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(url, download=False)

        # Verifica se é uma playlist ou um único vídeo
        if 'entries' in info:
            videos = info['entries']
        else:
            videos = [info]

    for video in videos:
        title = sanitize_title(video.get('title', 'Untitled'))
        thumbnail_url = video.get('thumbnail') or (video.get('thumbnails', [{}])[-1].get('url'))

        with tqdm(total=100, bar_format='\033[92m[{bar}] {n_fmt}/{total_fmt}%\033[0m') as pbar:
            def progress_hook(d):
                if d['status'] == 'downloading':
                    percent_str = strip_ansi_codes(d['_percent_str']).strip('%')
                    try:
                        percent = float(percent_str)
                        pbar.n = percent
                        pbar.refresh()
                    except ValueError:
                        pass
                elif d['status'] == 'finished':
                    pbar.n = 100
                    pbar.refresh()

            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': quality_audio,
                }],
                'outtmpl': os.path.join(save_directory, f'{title}.%(ext)s'),
                'quiet': True,
                'progress_hooks': [progress_hook]
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video['webpage_url']])

        print("✅ Conversão finalizada...")

        mp3_file = os.path.join(save_directory, f"{title}.mp3")
        if os.path.exists(mp3_file) and thumbnail_url:
            image_data = download_thumbnail(thumbnail_url)
            if image_data:
                add_cover_to_mp3(mp3_file, image_data)

        print(f"✅ Download concluído: {title}")

def main():
    while True:
        try:
            print("Pressione CTRL + C para sair a qualquer momento.")
            url = input("\nDigite o link do vídeo/playlist: ").strip()
            if not url:
                continue

            quality = int(input("Qualidade: 1 - Alta | 2 - Baixa: ").strip())
            if quality not in [1, 2]:
                print("❌ Opção inválida!")
                continue

            download_audio(url, quality)
        except KeyboardInterrupt:
            print("\n❌ Saindo...")
            break

if __name__ == "__main__":
    main()
