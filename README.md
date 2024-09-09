# Convert-pdn-to-ora

This script uses Paint.NET, the OpenRaster export plugin for Paint.NET,  
and Python to automatically convert `.pdn` (Paint.NET) layer files in a folder  
and its subfolders to `.ora` (OpenRaster) format, which can be opened in applications like Krita.

## Requirements

To run this script, you will need the following:

- **Windows 11 (can be a virtual machine)**  
  Paint.NET does not function on Windows 10

- **Paint.NET**  
  You can install Paint.NET via `winget` or download it from [dotpdn downloads](https://www.dotpdn.com/downloads/pdn.html):
  ```
  winget install dotPDN.PaintDotNet
  ```

- **Paint.NET OpenRaster Export Plugin**  
  Download the OpenRaster plugin from [Paint.NET OpenRaster Filetype](https://forums.getpaint.net/topic/20984-openraster-filetype/) and place it in the Paint.NET filetypes folder.

- **Python 3.8+ (only needed for the .py  not .exe)**  
  Python will be needed to run the script.   
  Install Python from [python.org](https://www.python.org/downloads/).

- **Required Python Packages (only needed for the .py  not .exe)**  
  Install the following packages via pip:
  ```
  pip install pyautogui pygetwindow psutil
  ```

## Download

Visit [the releases section](https://codeberg.org/marvin1099/Convert-pdn-to-ora/releases) to download the latest version of the script.

## Setup

1. **Prepare Your Environment**  
   Close all unnecessary windows to avoid interference with the automation process.

2. **Place and Run the Script**  
   Place the script file in the folder containing the `.pdn` files you want to convert.  
   The script will process all `.pdn` files in the folder and subfolders.

3. **Recreate ORA Files Option**  
   When running the script, it will prompt you whether to recreate `.ora` files, even if they already exist.  
   Select "Yes" to overwrite or "No" to skip existing `.ora` files.

4. **Delete PDN Files Option**  
   After conversion, you will also be prompted to choose whether to delete the `.pdn` files.  
   The script defaults to "Yes" if you close the dialog.

5. **Conversion Process**  
   The script will:
   - Open each `.pdn` file in Paint.NET
   - Save it as `.ora` using Paint.NET's Save As functionality
   - Close Paint.NET after each conversion
   - Move on to the next file

6. **Command Line Usage**  
   You can also run the script from the command line:
   ```
   cd "C:\CONVERSION\PATH"
   python "C:\PATH\TO\convert_pdn_to_ora.py"
   ```
   Or with a specific folder path:
   ```
   python "C:\PATH\TO\convert_pdn_to_ora.py" "C:\CONVERSION\PATH"
   ```
   Replace `"C:\CONVERSION\PATH"` and `"C:\PATH\TO\convert_pdn_to_ora.py"` with the actual paths on your system.

## Linux Compatibility

If you want to run this script on Linux,  
you will need to use a Windows 11 virtual machine or a Windows installation,  
as Paint.NET does not work under Wine.  
The `.pdn` format has not been reverse-engineered for native Linux support.
