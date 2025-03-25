import os
import yt_dlp
import time
import subprocess
from PIL import Image
from fpdf import FPDF

def download_youtube_video(youtube_url):
    """Download video from YouTube using yt-dlp."""
    print(f"Downloading video from {youtube_url}...")

    ydl_opts = {
        'format': 'bestvideo[height<=2160]+bestaudio/best',
        'outtmpl': 'downloaded_video.%(ext)s',
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    # Detect downloaded file
    video_path = "downloaded_video.mp4"
    if not os.path.exists(video_path):
        video_path = "downloaded_video.webm"

    return video_path

def extract_screenshots_ffmpeg(youtube_url, interval_sec=10, output_folder="output/screenshots", quality=2, resize_factor=1.0):
    """Extract screenshots efficiently using FFmpeg."""
    # Create output folder
    os.makedirs(output_folder, exist_ok=True)

    # Get the length of the video to estimate time
    video_length_cmd = [
        "ffmpeg", "-i", youtube_url, "-hide_banner"
    ]
    result = subprocess.run(video_length_cmd, capture_output=True, text=True)  # Fixed here
    video_info = result.stderr
    video_length_str = [line for line in video_info.splitlines() if "Duration" in line][0]
    duration = video_length_str.split("Duration: ")[1].split(",")[0]

    # Correct parsing of the duration in HH:MM:SS.mmm format
    h, m, s = duration.split(":")
    seconds, milliseconds = s.split(".")
    total_seconds = int(h) * 3600 + int(m) * 60 + int(seconds) + int(milliseconds) / 1000

    # Estimate total time to extract screenshots
    estimated_time_sec = total_seconds / interval_sec
    estimated_time_min = estimated_time_sec / 60
    print(f"Estimated time to extract screenshots: {estimated_time_min:.2f} minutes")

    start_time = time.time()

    # Use FFmpeg to extract frames directly from YouTube URL
    resize_filter = f",scale=iw*{resize_factor}:ih*{resize_factor}" if resize_factor != 1.0 else ""

    ffmpeg_cmd = [
        "ffmpeg",
        "-i", youtube_url,  # Stream directly from YouTube         
        "-vf", f"fps=1/{interval_sec}{resize_filter}",  # Extract frame every `interval_sec` seconds
        "-q:v", str(quality),                       # Set image quality (lower is better quality)
        os.path.join(output_folder, "screenshot_%04d.jpg"),  # Output pattern
        "-loglevel", "error"                        # Suppress verbose output
    ]

    print("Running FFmpeg extraction...")
    subprocess.run(ffmpeg_cmd)

    end_time = time.time()
    print(f"Screenshot extraction completed in {end_time - start_time:.2f} seconds.")
    print(f"Screenshots saved in '{output_folder}'")

def convert_screenshots_to_pdf(screenshot_folder, output_pdf):
    """Convert screenshots to PDF."""
    # Get all image files in the folder
    screenshot_files = [f for f in os.listdir(screenshot_folder) if f.endswith('.jpg')]

    # Sort files in order (optional, if files are named sequentially)
    screenshot_files.sort()

    # Create PDF instance
    pdf = FPDF()

    for screenshot in screenshot_files:
        screenshot_path = os.path.join(screenshot_folder, screenshot)
        
        # Open the image using Pillow
        img = Image.open(screenshot_path)
        
        # Convert image to RGB mode (if it's not already in that mode)
        img = img.convert('RGB')

        # Get image dimensions to adjust the size properly
        img_width, img_height = img.size
        aspect_ratio = img_height / img_width
        pdf_width = 210  # A4 width in mm
        pdf_height = pdf_width * aspect_ratio

        # Ensure that the image fits within the page
        max_pdf_height = 297  # A4 height in mm
        if pdf_height > max_pdf_height:
            pdf_height = max_pdf_height
            pdf_width = pdf_height / aspect_ratio

        # Add a new page to the PDF for each image
        pdf.add_page()

        # Add the image to the PDF, centered on the page
        pdf.image(screenshot_path, x=(pdf.w - pdf_width) / 2, y=10, w=pdf_width, h=pdf_height)  # Centered image

    # Output PDF to the specified file
    pdf.output(output_pdf)

    print(f"PDF saved as '{output_pdf}'")

def delete_file(file_path):
    """Delete a file if it exists."""
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' deleted.")
    else:
        print(f"File '{file_path}' not found.")

if __name__ == "__main__":
    youtube_url = input("Enter YouTube Video URL: ")

    # Ask the user for the interval between screenshots
    interval_sec = int(input("Enter time interval between screenshots in seconds (e.g., 10): "))

    # Set up the output folder for screenshots and PDF
    output_folder = "output"
    screenshot_folder = os.path.join(output_folder, "screenshots")
    os.makedirs(screenshot_folder, exist_ok=True)

    # Download the video (if you want to download it locally first)
    video_path = download_youtube_video(youtube_url)

    # Extract screenshots quickly using FFmpeg (every user-defined time interval)
    extract_screenshots_ffmpeg(video_path, interval_sec=interval_sec, output_folder=screenshot_folder, quality=2, resize_factor=0.5)

    # Convert screenshots to PDF
    output_pdf = os.path.join(output_folder, "output_screenshots.pdf")
    convert_screenshots_to_pdf(screenshot_folder, output_pdf)

    # Delete the downloaded video file after PDF is created
    delete_file(video_path)

    print(f"Output PDF file saved at: {output_pdf}")
