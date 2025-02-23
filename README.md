![YouToba Logo](YouToba_logo.png)

**YouTuba Downloader** is a tool for downloading music from YouTube videos with the ability to choose audio quality and add the thumbnail to the MP3 file. Developed in Python, it utilizes the `yt-dlp`, `mutagen`, and `requests` libraries to provide a simple and convenient experience for downloading and customizing music.

### Features:
- **Download Audio**: Allows downloading audio from YouTube videos or playlists, converting them directly to MP3 format.
- **Quality Choice**: Users can choose between two audio qualities: high (320kbps) or low (64kbps).
- **Add Cover to MP3**: After downloading, the script fetches the video's thumbnail image and adds it to the MP3 file.
- **Simple Interface**: The interactive command line interface lets users input the video/playlist link and choose the desired audio quality.

### Requirements:
- Python 3.x
- Python Libraries:
  - `yt-dlp` (for downloading YouTube videos)
  - `mutagen` (for manipulating MP3 files)
  - `requests` (for downloading the cover image)
  - `tqdm` (for displaying the progress bar)

### How to Use:
1. Clone the repository or download the code.
2. Install the dependencies:
   ```
   pip install yt-dlp mutagen requests tqdm
   ```
3. Run the script:
   ```
   python YouToba.py
   ```
4. Enter the video or playlist link when prompted.
5. Choose the audio quality (1 for high, 2 for low).
6. The audio will be downloaded as an MP3 file and the cover will be automatically added, if available.

### Example Usage:
```
Enter the video/playlist link: https://www.youtube.com/watch?v=abcd1234
Quality: 1 - High | 2 - Low: 1
🎵 Downloading...
[██████████████████████████████████████████████████████████████████████████████████] 100/100%
✅ Conversion complete
✅ Cover added to MP3:/path1/path2/path3/Video name
✅ Download completed: Video name
```

### Contribution:

Feel free to contribute to the project by creating a pull request or opening an issue.

## ⚠️ Legal Notice  
This script should be used **only for personal downloads** and within YouTube's guidelines. The developer **is not responsible** for any misuse of the code.  
