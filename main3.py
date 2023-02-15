from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def split_video_by_time(input_file, segment_duration):
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
        output_file = f'{video_title}_ep{i+1}_part{i+1}.mp4'

        # Export the segment with the custom name
        segment.write_videofile(os.path.join(video_title, output_file), codec='libx264')

def cut_video_in_specific_time(input_file, segment_times):
    # Load the video file
    video = VideoFileClip(input_file)

    # Loop through each segment time and export with custom name
    for i, segment_time in enumerate(segment_times):
        # Calculate the start and end times for the segment
        start_time = segment_time[0]
        end_time = segment_time[1]

        # Create a subclip of the segment
        segment = video.subclip(start_time, end_time)

        # Define the output file name
        output_file = f'{video_title}_ep{i+1}_part{i+1}.mp4'

        # Export the segment with the custom name
        segment.write_videofile(os.path.join(video_title, output_file), codec='libx264')

# Get input from user
print(f"HELLO\n#############################\nPUT file to src folder\nNOTE: The video title u input in the next step have to be equal with the file name in the src folder\n\n")
video_title = input('Enter video title: ')
split_method = input('Enter split method: \n     1. by_time \n     2. specific_time\n->')

# Load the video file
input_file = os.path.join('src', f'{video_title}.mp4')

if split_method == 'by_time' or split_method == '1':
    segment_duration = float(input('Enter segment duration in minutes: ')) * 60
    # Calculate the number of segments
    video = VideoFileClip(input_file)
    total_duration = video.duration
    num_segments = int(total_duration // segment_duration) + 1
    print(f'Predicted number of exported files: {num_segments}')
    # Split the video by time
    split_video_by_time(input_file, segment_duration)
elif split_method == 'specific_time' or split_method == '2':
    num_segments = int(input('Enter number of segments: '))
    segment_times = []
    for i in range(num_segments):
        start_time = float(input(f'Enter start time for segment {i+1}: '))
        end_time = float(input(f'Enter end time for segment {i+1}: '))
        segment_times.append((start_time, end_time))
    print(f'Predicted number of exported files: {num_segments}')
    # Cut the video at specific times
    cut_video_in_specific_time(input_file, segment_times)
else:
    print("are u stupid dude?")
# Create output folder if it doesn't exist
output_folder = os.path.join(os.getcwd(), video_title)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)