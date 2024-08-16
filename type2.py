import tkinter as tk
from tkinter import ttk
from datetime import datetime
from PIL import Image, ImageTk
import pytz

# Function to convert IST time to the selected time zone
def convert_time():
    try:
        # Get user input for date and time
        ist_input = ist_time_entry.get()
        # Convert the input string to a datetime object
        ist_time = datetime.strptime(ist_input, '%Y-%m-%d %H:%M:%S')

        # Localize the datetime object to IST
        ist = pytz.timezone('Asia/Kolkata')
        localized_ist_time = ist.localize(ist_time)

        # Get the selected timezone
        selected_timezone = timezone_combobox.get()

        # Convert to the selected timezone
        target_timezone = pytz.timezone(selected_timezone)
        target_time = localized_ist_time.astimezone(target_timezone)

        # Update the label with the converted time
        result_label.config(text=f"Converted time in {selected_timezone}: {target_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")
    except Exception as e:
        result_label.config(text="Error: Please enter a valid date and time in the format 'YYYY-MM-DD HH:MM:SS'")

# Create the main window
root = tk.Tk()
root.title("IST to Time Zone Converter")

# Load and display the image
image = Image.open("images.png")
image = image.resize((100, 100), Image.Resampling.LANCZOS)
image_tk = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=image_tk)
image_label.grid(row=0, column=0, rowspan=6, padx=10, pady=10)

# Create and place widgets in the window
ist_time_label = tk.Label(root, text="Enter IST Date and Time (YYYY-MM-DD HH:MM:SS):", font=('Helvetica', 12))
ist_time_label.grid(row=0, column=1, padx=10, pady=10, sticky='w')

ist_time_entry = tk.Entry(root, width=30, font=('Helvetica', 12))
ist_time_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')

timezone_label = tk.Label(root, text="Select Time Zone:", font=('Helvetica', 12))
timezone_label.grid(row=2, column=1, padx=10, pady=10, sticky='w')

timezone_combobox = ttk.Combobox(root, values=pytz.all_timezones, width=30, font=('Helvetica', 12))
timezone_combobox.grid(row=3, column=1, padx=10, pady=10, sticky='w')

convert_button = tk.Button(root, text="Convert", command=convert_time, font=('Helvetica', 12))
convert_button.grid(row=4, column=1, padx=10, pady=10, sticky='w')

result_label = tk.Label(root, text="", font=('Helvetica', 12))
result_label.grid(row=5, column=1, padx=10, pady=10, sticky='w')

# Start the GUI loop
root.mainloop()
