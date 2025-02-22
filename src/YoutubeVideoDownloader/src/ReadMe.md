# YouTube Video Downloader

A simple C++ program that allows users to download YouTube videos using `yt-dlp`. The program checks if `yt-dlp` is installed, prompts the user for a YouTube URL, and offers two download options: 720p or the best available format.

## Features
- Checks if `yt-dlp` is installed.
- Allows users to input a YouTube video URL.
- Provides two download options:
  - 720p resolution.
  - Best available format.
- Uses `system()` to execute the `yt-dlp` command.

## Prerequisites
Ensure you have the following installed:
- `yt-dlp`
- `ffmpeg` (for merging audio and video)

### Installation
#### Install `yt-dlp`:
- **Mac (Homebrew)**: `brew install yt-dlp`
- **Python (Pip)**: `pip install yt-dlp`
- **Manual Download**: [yt-dlp GitHub](https://github.com/yt-dlp/yt-dlp)

#### Install `ffmpeg`:
- **Mac (Homebrew)**: `brew install ffmpeg`
- **Manual Download**: [FFmpeg Official Site](https://ffmpeg.org/download.html)

## Usage
1. Compile the program:
   ```sh
   g++ -o downloader downloader.cpp
   ```
2. Run the executable:
   ```sh
   ./downloader
   ```
3. Follow the prompts to enter a YouTube URL and select a download option.


## Disclaimer
This program is for educational purposes only. Make sure to follow YouTube's terms of service when downloading videos.

---

Happy downloading! 🚀

