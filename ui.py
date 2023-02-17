import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Movie Converter")

# Create the text edit for entering the movie name
movie_label = tk.Label(window, text="Enter Movie Name:")
movie_label.pack()

movie_entry = tk.Entry(window)
movie_entry.pack()

# Create the radio buttons for selecting the conversion option
option_label = tk.Label(window, text="Select Conversion Option:")
option_label.pack()

option = tk.StringVar(value="Option 1")

option_1 = tk.Radiobutton(window, text="Option 1", variable=option, value="Option 1")
option_1.pack()

option_2 = tk.Radiobutton(window, text="Option 2", variable=option, value="Option 2")
option_2.pack()

# Create the convert button and function
def convert_movie():
    movie_name = movie_entry.get()
    conversion_option = option.get()
    print(f"Converting '{movie_name}' using {conversion_option}")

convert_button = tk.Button(window, text="Convert", command=convert_movie)
convert_button.pack()

# Start the main event loop
window.mainloop()