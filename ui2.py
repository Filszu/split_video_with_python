import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
from video import split_video_by_time, cut_video_in_specific_time

class VideoSplitter:
    def __init__(self, master):
        self.master = master
        master.title("Video Splitter")

        # create movie name label and text entry
        self.movie_name_label = tk.Label(master, text="Movie name:")
        self.movie_name_label.pack()

        self.movie_name_entry = tk.Entry(master)
        self.movie_name_entry.pack()

        # create radio buttons for split method
        self.split_method_label = tk.Label(master, text="Split method:")
        self.split_method_label.pack()

        self.split_method = tk.StringVar(value="by_time")

        self.by_time_radio = tk.Radiobutton(master, text="By Time", variable=self.split_method, value="by_time")
        self.by_time_radio.pack()

        self.specific_time_radio = tk.Radiobutton(master, text="Specific Times", variable=self.split_method, value="specific_time")
        self.specific_time_radio.pack()

        # create duration label and text entry
        self.duration_label = tk.Label(master, text="Duration (in minutes):")
        self.duration_label.pack()

        self.duration_entry = tk.Entry(master)
        self.duration_entry.pack()

        # create start/end times label and text entries
        self.start_time_label = tk.Label(master, text="Start Time:")
        self.start_time_entries = []
        self.end_time_label = tk.Label(master, text="End Time:")
        self.end_time_entries = []

        for i in range(5):
            start_entry = tk.Entry(master)
            end_entry = tk.Entry(master)
            self.start_time_entries.append(start_entry)
            self.end_time_entries.append(end_entry)

            self.start_time_label.pack()
            start_entry.pack()
            self.end_time_label.pack()
            end_entry.pack()

        # create convert button
        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.convert_button.pack()

    def convert(self):
        movie_name = self.movie_name_entry.get()
        split_method = self.split_method.get()

        input_file = os.path.join("src", f"{movie_name}.mp4")

        if not os.path.exists(input_file):
            messagebox.showerror("Error", f"No video file named {movie_name}.mp4 found in src folder.")
            return

        if split_method == "by_time":
            try:
                duration = float(self.duration_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Duration must be a number.")
                return

            segment_duration = duration * 60

            # Create output folder if it doesn't exist
            output_folder = os.path.join(os.getcwd(), movie_name)
            if not os.path.exists(output_folder):
                os.makedirs(output_folder, exist_ok=True)

            try:
                split_video_by_time(input_file, segment_duration, movie_name)
                messagebox.showinfo("Success", "Video was successfully split.")
            except Exception as e:
                messagebox.showerror("Error", f"Error splitting video: {str(e)}")

        elif split_method == "specific_time":
            segment_times = []
            for i in range(5):
                start_time = self.start_time_entries[i].get()
                end_time = self.end_time_entries[i].get()

                if not start_time or not end_time:
                    break

                try:
                    start_time = float(start_time)
                    end_time = float(end_time)
                except ValueError:
                    messagebox.showerror("Error")
