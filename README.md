# YT2PDF - Convert YouTube Videos into Screenshots and PDFs📄

YT2PDF is a powerful Python-based Script that allows you to extract screenshots from YouTube videos at custom intervals and convert them into a PDF. This is perfect for saving key moments, creating summaries, or generating quick documentation from video content.


## Features 🚀
- **Extract Screenshots** 📸: Capture frames from YouTube videos at a specified time interval.
- **Convert to PDF** 📄: Automatically arrange extracted images into a well-formatted PDF.
- **Automatic Cleanup** 🧹: Deletes temporary video files after processing (only screenshots and PDFs are retained).
- **Lightweight & Fast** ⚡: Uses `ffmpeg` for efficient frame extraction.
- **Future Update** 🔜: Will include an option to convert screenshots into DOCX format and GUI Interface

---

## Installation Guide 🛠️

### 1. Clone the Repository
```bash
# Using Git
git clone https://github.com/HYDRA-01/YT2PDF.git
cd YT2PDF
```

### 2. Install Python Dependencies
Make sure you have Python 3.12+ installed. Then, install the required libraries:
```bash
pip install yt-dlp pillow fpdf
```

### 3. Install FFmpeg (Required for Screenshot Extraction)
#### Windows:
1. Download FFmpeg from [Gyan.dev](https://www.gyan.dev/ffmpeg/builds/)
2. Extract the ZIP file (e.g., `ffmpeg-release-essentials.zip`)
3. Copy the `bin` folder path (e.g., `C:\ffmpeg\bin`)
4. Add it to your **System Environment Variables**:
   - Open *System Properties* → *Advanced* → *Environment Variables*
   - Under *System Variables*, select **Path** → *Edit* → *New*
   - Paste your `C:\ffmpeg\bin` path and click **OK**.
5. Verify installation by running:
```bash
ffmpeg -version
```

#### macOS (via Homebrew):
```bash
brew install ffmpeg
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update && sudo apt install ffmpeg
```

---

## Usage 🖥️

### Running the Tool
```bash
python main.py
```

### Example Workflow
1. **Enter YouTube Video URL** (e.g., `https://www.youtube.com/watch?v=9uscnsbAdQ`)
2. **Choose Time Interval** (e.g., `15 seconds` for capturing frames every 15 seconds)
3. **Process Starts**:
   - Downloads the video (if needed)
   - Extracts screenshots using `ffmpeg`
   - Converts screenshots into a **PDF**
4. **Output PDF is saved in the `output/` folder**

---

## Output 📂
- **Screenshots** → `output/screenshots/`
- **Final PDF** → `output/output_screenshots.pdf`

---

## Roadmap 🛣️
✅ Implement YouTube screenshot extraction
✅ Automatic PDF generation
✅ Automatic video deletion after processing
🔜 Add support for DOCX conversion
🔜 GUI Interface for easier use

---

## License 📜
Mozilla Public License 2.0 (MPL-2.0)

Additional Clause:
This software may be used, modified, and distributed **for personal, non-commercial purposes only**. You may not use, distribute, or modify the software for commercial purposes, including any form of commercial gain, without prior written permission from the copyright holder.

For the purposes of this clause, personal use refers to non-commercial use by individuals or organizations for personal, educational, or research purposes.

---

### Contributors 💡
Feel free to contribute by submitting pull requests or reporting issues!

🌟 **Star this repo if you like it!** 🌟
👨‍💻 Made with ❤️ by Aditya
