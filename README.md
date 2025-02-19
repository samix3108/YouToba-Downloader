### Description for GitHub Repository: **YouToba Downloader**

**YouToba Downloader** is a simple and effective tool for downloading videos and music from platforms like YouTube, converting them into MP3 or video formats. The standout feature of **YouToba Downloader** is that when downloading music in MP3 format, it automatically adds the video’s thumbnail as the cover image to the audio file, providing better organization and aesthetics for your music files.

**Main Features:**
- **Audio or Video Download**: Choose between downloading a full video or just the audio (MP3) in either high or low quality.
- **Cover Art for MP3**: If downloading as audio, the video’s thumbnail (cover image) will be added to the MP3 file.
- **Quality Adjustable**: Select the download quality for audio or video, with options for high or low quality.

**Required Dependencies:**
1. **yt-dlp**: Used for downloading content from YouTube and other compatible platforms.
2. **mutagen**: A library required for handling audio file metadata, including adding cover art to MP3 files.
3. **requests**: Used for downloading the video’s thumbnail (cover image).

**How to Install Dependencies**:
To install the required dependencies, run the following command:
```bash
pip install yt-dlp mutagen requests
```

**Recommendation for Best MP3 Quality**:
To ensure that the MP3 file has a cover image, it's recommended to download music directly from YouTube Music. When you find the desired song or video on YouTube Music, use the link to download it. This increases the chance of the MP3 file having the album cover added during the conversion.

**Usage Instructions**:
1. Run the script.
2. Enter the video or playlist link.
3. Choose whether to download as **Audio** (MP3) or **Video**.
4. If selecting audio, choose the quality (high or low).
5. The script will download the content and, if it's audio, automatically add the cover art to the MP3 file.

---

**YouToba Downloader** provides a quick and easy way to download videos and music, with the bonus of organizing audio files with album cover art. It’s a fast solution for those who want to enjoy their favorite music with great quality and neat organization!
