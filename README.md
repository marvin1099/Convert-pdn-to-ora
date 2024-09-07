# Convert-pdn-to-ora

This script uses Paint.NET, the OpenRaster export plugin for Paint.NET,  
and AutoHotkey v2 to automatically convert `.pdn` (Paint.NET) layer files in a folder  
and its subfolders to `.ora` (OpenRaster) format, which can be opened in applications like Krita.

## Requirements

To run this script, you will need the following:

- **Windows 11** (can be a virtual machine)  
  Paint.NET does not function on Windows 10
  
- **Paint.NET**  
  You can install Paint.NET via `winget` or download it from [dotpdn downloads](https://www.dotpdn.com/downloads/pdn.html):
  ```sh
  winget install dotPDN.PaintDotNet
  ```

- **Paint.NET OpenRaster Export Plugin**  
  Download the OpenRaster plugin from [Paint.NET OpenRaster Filetype](https://forums.getpaint.net/topic/20984-openraster-filetype/) and place it in the Paint.NET filetypes folder.

- **AutoHotkey v2** (Only needed if you use the `.ahk` file; if you use the `.exe`, you can skip this)  
  Install AutoHotkey v2 via `winget` or download it from [AutoHotkey website](https://www.autohotkey.com/):
  ```sh
  winget install AutoHotkey.AutoHotkey
  ```

## Download

Visit [the releases section](https://codeberg.org/marvin1099/Convert-pdn-to-ora/releases) to download the latest `.ahk` or `.exe` file.

## Setup

1. **Prepare Your Environment**  
   Close all unnecessary windows.

2. **Place and Run the Script**  
   Place the script file in the folder containing the `.pdn` files you want to convert.

3. **Delete PDN Files Option**  
   When you run the script, it will prompt you to choose whether to delete the `.pdn` files after conversion. Select "Yes" if you want to delete them, or "No" if you want to keep them.

4. **Conversion Process**  
   The script will recursively search all folders within the specified directory. It will:
   - Open each `.pdn` file in Paint.NET
   - Save it as `.ora` using Paint.NET's Save As functionality
   - Close Paint.NET
   - Move on to the next file

5. **Command Line Usage**  
   You can also run the script from the command line:
   ```sh
   cd "C:\CONVERSION\PATH"
   "C:\PATH\TO\pdn-to-ora.ahk"
   ```
   Or with a specific folder path:
   ```sh
   "C:\PATH\TO\pdn-to-ora.ahk" "C:\CONVERSION\PATH"
   ```
   Replace `"C:\CONVERSION\PATH"` and `"C:\PATH\TO\pdn-to-ora.ahk"` with the actual paths on your system.

## Linux Compatibility

If you want to run this script on Linux,
you will need to use a Windows 11 virtual machine or a Windows installation,
as Paint.NET does not work under Wine. 
The `.pdn` format has not been reverse-engineered for native Linux support.
