# --- FFmpeg ---
# pip install ffmpeg-python

import ffmpeg

# 1. Convert Video Format
ffmpeg.input('input.mp4').output('output.avi').run()

# 2. Extract Audio from Video
ffmpeg.input('input.mp4').output('output.mp3').run()

# 3. Remove Metadata
ffmpeg.input('input.mp4').output('output.mp4', map_metadata='-1').run()