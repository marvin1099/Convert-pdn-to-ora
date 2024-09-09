import pyautogui
import time
import os
import subprocess
from tkinter import Tk, simpledialog, messagebox
import pygetwindow as gw  # For window management

# Helper function to get input from user via a dialog
def get_input(prompt, title, default=""):
    root = Tk()
    root.withdraw()
    user_input = simpledialog.askstring(title, prompt, initialvalue=default)
    root.destroy()
    return user_input

# Function to bring the window of Paint.NET to focus by matching the window title
def focus_paint_net_window_by_title():
    tout=10
    while tout > 0:
        try:
            # Get all windows
            all_windows = gw.getAllWindows()
            for window in all_windows:
                # Match the window title with "paint.net"
                if "paint.net" in window.title.lower():
                    window.activate()  # Focus the window
                    return True
        except Exception as e:
            print(f"Error focusing window: {e}")
        time.sleep(1)
        tout -= 1
    if tout <= 0:
        print("Window timeout, paint.net not found")
        exit()

# Get folder to process PDN files
pdn_folder = os.getcwd()  # Default to current directory
if len(os.sys.argv) > 1:
    pdn_folder = os.sys.argv[1]  # Use argument if provided

# Check if the folder exists
if not os.path.exists(pdn_folder):
    messagebox.showerror("Error", f"Folder not found: {pdn_folder}")
    exit()

# Default path to Paint.NET executable
paint_dot_net_path = r"C:\Program Files\paint.net\paintdotnet.exe"

# Check if Paint.NET exists, if not, prompt user to enter the path
if not os.path.exists(paint_dot_net_path):
    paint_dot_net_path = get_input(
        "Paint.NET executable not found at the default location.\nPlease enter the full path to the Paint.NET executable:",
        "Paint.NET Path", paint_dot_net_path
    )
    if not paint_dot_net_path or not os.path.exists(paint_dot_net_path):
        messagebox.showerror("Error", "Paint.NET executable not found. Exiting.")
        exit()

# Ask if the user wants to recreate .ora files
recreate_files = messagebox.askyesno("Recreate ORA Files", "Do you want to recreate the .ora files even if they already exist?", default="no")

# Ask if the user wants to delete PDN files after conversion (default to Yes)
delete_files = messagebox.askyesno("Delete PDN Files", "Do you want to delete the PDN files after conversion?", default="no")

print("Using:")
print(" PDN Folder: " + pdn_folder)
print(" Paintdotnet.exe: " + paint_dot_net_path)
print(" ORA Recreation: " + str(recreate_files))
print(" PDN Deletetion: " + str(delete_files))
print("")

# Recursively search for all PDN files
for root_dir, dirs, files in os.walk(pdn_folder):
    for file_name in files:
        if file_name.endswith(".pdn"):
            pdn_file = os.path.join(root_dir, file_name)
            ora_file = pdn_file[:-3] + "ora"

            # Only process if the .ora file does not exist
            if recreate_files or not os.path.exists(ora_file):
                print(f"Processing: {file_name}")

                # Open the .pdn file in Paint.NET
                process = subprocess.Popen([paint_dot_net_path, pdn_file])

                # Focus the Paint.NET window using the window title
                focus_paint_net_window_by_title()
                time.sleep(1)  # Give extra time for the file to load

                # Automate the saving process as OpenRaster (.ora)
                pyautogui.hotkey('ctrl', 'shift', 's')  # Control+Shift+S (Save As)
                time.sleep(1)
                pyautogui.press('tab')  # Move to file type selector
                time.sleep(0.5)
                pyautogui.press('o')  # Select OpenRaster (.ora)
                time.sleep(0.5)
                pyautogui.press('enter')  # Confirm Save
                time.sleep(0.5)
                pyautogui.press('tab')  # Additional Tab press
                time.sleep(0.5)
                pyautogui.press('enter')  # Confirm overwrite if prompted
                time.sleep(4)

                # Close Paint.NET window
                all_windows = gw.getAllWindows()
                for window in all_windows:
                    if "paint.net" in window.title.lower():
                        window.close()
                time.sleep(1)  # Wait for the window to close before the next file

                # Delete the PDN file if user opted to
                if os.path.exists(ora_file) and delete_files:
                    print(f"File created: {ora_file}")
                    print(f"Deleting: {file_name}")
                    os.remove(pdn_file)
                elif delete_files:
                    print(f"Skipping deletion because of missing: {ora_file}")
                elif os.path.exists(ora_file):
                    print(f"File created: {ora_file}")
                else:
                    print(f"Failed to create: {ora_file}")
            else:
                print(f"Skipping existing file: {file_name}")
            print("")

print("All PDN files processed.")
time.sleep(2)
