# Time Zone Converter Applications

This repository contains two distinct Time Zone Converter applications built using Tkinter and Python. Each application serves a unique purpose and features a different graphical user interface (GUI).

## Application 1: Real-Time Clock and Converter

### Description
The first application displays a real-time clock that shows the current IST (Indian Standard Time) and allows users to convert this time to a selected time zone. The clock is visually represented with hour, minute, and second hands, and updates every second.

### Features
- **Real-Time Clock**: Shows current IST time with a graphical clock.
- **Time Zone Conversion**: Converts IST time to any selected time zone from a list.

### GUI Components
- **Clock**: Displays a real-time analog clock with hour, minute, and second hands.
- **Time Zone Combobox**: Allows users to select a target time zone for conversion.
- **Labels**: Show the current IST time and the converted time in the selected time zone.

### Example Output
- **IST Time**: `2024-08-16 14:30:45 IST+0530`
- **Time in New York**: `2024-08-16 05:00:45 EDT-0400`

  
   ![Screenshot 2024-08-16 151102](https://github.com/user-attachments/assets/aa23cc65-333b-4283-bca1-657fb045b730)



### Running the Application
1. Ensure you have Python and the required packages installed (`tkinter`, `pytz`, `math`).
2. Save the script as `type1.py`.
3. Run the script using `python type1.py`.

## Application 2: Manual Time Zone Converter

### Description
The second application allows users to manually input a date and time in IST and convert it to a selected time zone. This is useful for converting specific historical or future times rather than real-time updates.

### Features
- **Manual Input**: Enter a specific date and time in IST.
- **Time Zone Conversion**: Convert the manually entered IST time to any selected time zone from a list.
- **Image Display**: Displays an image in the GUI for visual enhancement.

### GUI Components
- **Entry Field**: For users to input a specific IST date and time.
- **Time Zone Combobox**: Allows users to select a target time zone for conversion.
- **Convert Button**: Initiates the conversion process.
- **Result Label**: Displays the converted time or an error message.
- **Image Label**: Shows an image related to the application.

### Example Output
- **Input IST Time**: `2024-08-16 14:30:00`
- **Converted Time in London**: `2024-08-16 09:00:00 BST+0100`

![Screenshot 2024-08-16 151713](https://github.com/user-attachments/assets/0b75e445-6ae1-4bfd-88f7-9ad2e43fb2ef)


### Running the Application
1. Ensure you have Python and the required packages installed (`tkinter`, `pytz`, `PIL`).
2. Save the script as `type2.py`.
3. Place the image file `images.png` in the same directory.
4. Run the script using `python type2.py`.

## Differences Between the Two Applications

1. **Real-Time vs. Manual Conversion**:
   - **Real-Time Clock and Converter**: Continuously displays the current time and converts it in real-time.
   - **Manual Time Zone Converter**: Converts a manually entered date and time.

2. **GUI Layout**:
   - **Real-Time Clock and Converter**: Features a graphical clock and dynamic conversion display.
   - **Manual Time Zone Converter**: Includes input fields and an image for enhanced user interaction.

3. **Use Case**:
   - **Real-Time Clock and Converter**: Best for seeing current time and immediate conversion.
   - **Manual Time Zone Converter**: Ideal for converting specific past or future times.

## Requirements
- **Python 3.x**
- **Packages**: `tkinter`, `pytz`, `PIL` (for the second application)

## Contact
For any questions or issues, please contact allminfatima.2709@gmail.com

---
Happy cooding 🎉💻
