import os
from moviepy.editor import ImageSequenceClip

# Specify the directory containing your frames
img_dir = './output/'

# Get a sorted list of all frame file paths in img_dir
img_files = sorted([os.path.join(img_dir, img) for img in os.listdir(img_dir) if img.endswith(".jpg")], reverse=True)

# Create a movie clip from the image files
clip = ImageSequenceClip(img_files, fps=10)  # Adjust fps as desired

# Save the clip as a mp4 file
clip.write_videofile('./output/mandelbrot_zoom.mp4')
