import yt_dlp
import os
import re
import requests
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
from io import BytesIO

def sanitize_title(title):
    return re.sub(r'[\\/*?:"<>|]', "", title)

def download_thumbnail(thumbnail_url):
    try:
        response = requests.get(thumbnail_url)
        response.raise_for_status()
        return response.content
    except Exception as e:
        print(f"Error downloading thumbnail: {e}")
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
        print(f"✅ Cover added to MP3: {mp3_file}")
    except Exception as e:
        print(f"❌ Error adding cover: {e}")

def download_media(url, download_type, quality):
    save_directory = os.path.join(os.getcwd(), 'Musics')  
    os.makedirs(save_directory, exist_ok=True)

    if download_type == 1: 
        format_audio = 'bestaudio/best'
        quality_audio = '320' if quality == 1 else '64'
        postprocessors = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': quality_audio,
        }]
    else:
        format_video = 'bestvideo+bestaudio/best' if quality == 1 else 'bestvideo[height<=144]+bestaudio/best'
        postprocessors = []

    ydl_opts = {
        'format': format_audio if download_type == 1 else format_video,
        'postprocessors': postprocessors,
        'outtmpl': os.path.join(save_directory, '%(title)s.%(ext)s'),
        'quiet': False,
        'noplaylist': False, 
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        if 'entries' in info: 
            for entry in info['entries']:
                process_download(entry, download_type, save_directory, ydl)
        else:  
            process_download(info, download_type, save_directory, ydl)

def process_download(info, download_type, save_directory, ydl):
    title = sanitize_title(info.get('title', 'Untitled'))
    thumbnail_url = info.get('thumbnail', None)

    ydl.download([info['webpage_url']])

    if download_type == 1 and thumbnail_url:
        mp3_file = os.path.join(save_directory, f"{title}.mp3")
        if os.path.exists(mp3_file):
            image_data = download_thumbnail(thumbnail_url)
            if image_data:
                add_cover_to_mp3(mp3_file, image_data)

def main():
    url = input("Enter the video/playlist link: ").strip()
    if not url:
        return

    download_type = int(input("Format: 1 - Audio | 2 - Video: ").strip())
    if download_type not in [1, 2]:
        print("Invalid option!")
        return

    quality = int(input("Quality: 1 - High | 2 - Low: ").strip())
    if quality not in [1, 2]:
        print("Invalid option!")
        return

    input("Press ENTER to confirm and start downloading...")

    download_media(url, download_type, quality)

if __name__ == "__main__":
    main()
