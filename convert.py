import subprocess
import os
import json

# Step 1: Get a list of files with the specified extensions
def get_video_files(directory, extensions):
    return [f for f in os.listdir(directory) if any(f.endswith(ext) for ext in extensions)]

# Step 2: Get the encoding of the files
def get_file_encoding(file_path):
    try:
        # Using ffprobe to get the video codec
        cmd = ['ffprobe', '-v', 'error', '-select_streams', 'v:0',
               '-show_entries', 'stream=codec_name', '-of', 'default=noprint_wrappers=1:nokey=1',
               file_path]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print(f"Error getting encoding for {file_path}: {result.stderr}")
            return None
    except Exception as e:
        print(f"Exception occurred while getting encoding for {file_path}: {e}")
        return None

# Main process
def process_videos(directory):
    video_files = get_video_files(directory, ['.mp4', '.mkv', '.avi'])
    encodings = {}

    # Gathering encodings
    for file in video_files:
        encoding = get_file_encoding(file)
        if encoding:
            encodings[encoding] = encodings.get(encoding, 0) + 1

    # Step 3: Print the encoding and number of files
    for encoding, count in encodings.items():
        print(f"Encoding: {encoding}, Number of files: {count}")

    # Step 4: Filter out h264 encoded files
    non_h264_files = [file for file in video_files if get_file_encoding(file) != 'h264']

    # Step 5: Convert non h264 files to h264 using ffmpeg
    for file in non_h264_files:
        output_file = f"{os.path.splitext(file)[0]}-h264.mp4"
        print(f"Converting {file} to {output_file}...")
        cmd = ['ffmpeg', '-i', file, '-map', '0:v:0', '-map', '0:a', '-map', '0:s?',
               '-c:v', 'libx264','-crf', '18', '-c:a', 'copy', '-c:s', 'mov_text', output_file]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print(f"Conversion completed: {file} -> {output_file}")
        else:
            print(f"Error converting {file}: {result.stderr}")

if __name__ == "__main__":
    process_videos('.')
