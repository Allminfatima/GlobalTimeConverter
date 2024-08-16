import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz
import math

# Function to draw the clock and update it
def draw_clock():
    # Clear the canvas
    canvas.delete("all")

    # Get the current time in IST
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata'))

    # Clock center and radius
    center_x = 150
    center_y = 150
    radius = 100

    # Draw the clock circle
    canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline="black", width=2)

    # Draw the clock numbers
    for number in range(1, 13):
        angle = math.radians(number * 30 - 90)
        x = center_x + int(radius * 0.8 * math.cos(angle))
        y = center_y + int(radius * 0.8 * math.sin(angle))
        canvas.create_text(x, y, text=str(number), font=("Helvetica", 12))

    # Calculate hand positions
    second_angle = math.radians(ist_time.second * 6 - 90)
    minute_angle = math.radians(ist_time.minute * 6 - 90)
    hour_angle = math.radians((ist_time.hour % 12) * 30 + ist_time.minute / 2 - 90)

    # Draw the hour hand
    hour_x = center_x + int(radius * 0.5 * math.cos(hour_angle))
    hour_y = center_y + int(radius * 0.5 * math.sin(hour_angle))
    canvas.create_line(center_x, center_y, hour_x, hour_y, fill="black", width=4)

    # Draw the minute hand
    minute_x = center_x + int(radius * 0.7 * math.cos(minute_angle))
    minute_y = center_y + int(radius * 0.7 * math.sin(minute_angle))
    canvas.create_line(center_x, center_y, minute_x, minute_y, fill="blue", width=3)

    # Draw the second hand
    second_x = center_x + int(radius * 0.9 * math.cos(second_angle))
    second_y = center_y + int(radius * 0.9 * math.sin(second_angle))
    canvas.create_line(center_x, center_y, second_x, second_y, fill="red", width=2)

    # Update the time display labels
    ist_time_str = ist_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    ist_label.config(text=f"IST Time: {ist_time_str}")

    # Convert the IST time to the selected time zone
    selected_timezone = timezone_combobox.get()
    if selected_timezone:
        target_timezone = pytz.timezone(selected_timezone)
        target_time = ist_time.astimezone(target_timezone)
        target_time_str = target_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
        converted_label.config(text=f"Time in {selected_timezone}: {target_time_str}")
    else:
        converted_label.config(text="Select a time zone")

    # Schedule the draw_clock function to run again after 1000ms (1 second)
    root.after(1000, draw_clock)

# Function to handle time zone selection
def on_timezone_change(event):
    draw_clock()

# Create the main window
root = tk.Tk()
root.title("Time Zone Converter")

# Create a Canvas widget for the clock
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.grid(row=0, column=0, rowspan=2, padx=10, pady=10)

# Create labels to display the time
ist_label = ttk.Label(root, text="", font=("Helvetica", 14))
ist_label.grid(row=0, column=1, padx=10, pady=10)

# Create a combobox to select the time zone
timezone_combobox = ttk.Combobox(root, values=pytz.all_timezones, width=30, font=("Helvetica", 12))
timezone_combobox.grid(row=1, column=1, padx=10, pady=10)
timezone_combobox.bind("<<ComboboxSelected>>", on_timezone_change)

# Create a label to display the converted time
converted_label = ttk.Label(root, text="", font=("Helvetica", 14))
converted_label.grid(row=2, column=1, padx=10, pady=10)

# Start drawing the clock
draw_clock()

# Start the Tkinter event loop
root.mainloop()
