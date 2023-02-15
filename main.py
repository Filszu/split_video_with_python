from moviepy.video.io.VideoFileClip import VideoFileClip

# Define the input video file name and segment duration
input_file = 'src/gf1.mp4'
segment_duration = 2.5 * 60  # in seconds

# Load the video file
video = VideoFileClip(input_file)

# Get the duration of the video in seconds
total_duration = video.duration

# Calculate the number of segments needed
num_segments = int(total_duration // segment_duration) + 1

# Loop through each segment and export with custom name
for i in range(num_segments):
    # Calculate the start and end times for the segment
    start_time = i * segment_duration
    end_time = min((i + 1) * segment_duration, total_duration)
    
    # Create a subclip of the segment
    segment = video.subclip(start_time, end_time)
    
    # Define the output file name
    output_file = f'title_ep{i+1}_part{i+1}.mp4'
    
    # Export the segment with the custom name
    segment.write_videofile(output_file, codec='libx264')