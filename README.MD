# Video Encoding Converter

This Python script is designed to automate the process of converting video files to the h264 codec using FFmpeg. It performs the following steps:

1. **Get a list of video files:** Scans a specified directory for video files with extensions '.mp4', '.mkv', and '.avi'.
2. **Get the encoding of the files:** Utilizes FFprobe to determine the video codec of each file.
3. **Print encoding and file count:** Displays the encoding and the number of files using that encoding.
4. **Filter out h264 encoded files:** Removes files already encoded with h264 from the list.
5. **Convert non-h264 files to h264:** Converts non-h264 files to h264 using FFmpeg with specified parameters.

## Prerequisites

- Python 3.x
- FFmpeg installed and added to system PATH

## Usage

1. Copy the convert.py file to the folder containing your video files
2. Open a command prompt in the directory
3. Run: 
```
python convert.py
```
