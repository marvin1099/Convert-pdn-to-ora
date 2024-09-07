Persistent
SetTitleMatchMode(2)  ; Partial match for window titles
DetectHiddenWindows(true)
CoordMode("Mouse", "Screen")

; Get folder to process PDN files
pdnFolder := A_Args.Length > 0 ? A_Args[1] :A_InitialWorkingDir  ; Use argument if provided or current directory

; Check if the folder exists
if !FileExist(pdnFolder) {
    MsgBox("Folder not found: " . pdnFolder)
    ExitApp
}

; Default path to Paint.NET executable
paintDotNetPath := "C:\Program Files\paint.net\paintdotnet.exe"

; Check if Paint.NET exists
if !FileExist(paintDotNetPath) {
    ; Prompt user to enter the Paint.NET path
    IB := InputBox("Paint.NET executable not found at the default location.`nPlease enter the path to the Paint.NET executable.", "Paint.NET Path", "", "C:\Program Files\paint.net\paintdotnet.exe")
    if (IB.Result = "Cancel") {
        MsgBox("Operation cancelled. Exiting script.")
        ExitApp
    }
    paintDotNetPath := IB.Value

    ; Validate the entered path
    if !FileExist(paintDotNetPath) {
        MsgBox("Paint.NET executable not found at the provided path.`nExiting script.")
        ExitApp
    }
}

deleteFiles := MsgBox("Do you want to delete the PDN files after conversion?", "Delete PDN Files", 4) ; 4 = Yes/No

;DllCall("AllocConsole")
;ST := FileOpen("*", "w")
; Recursively search for all PDN files
Loop Files, pdnFolder . "\*.pdn", "RF"
{
    ; Get corresponding .ora file path
    oraFile := SubStr(A_LoopFileFullPath, 1,-3) . "ora"
    ;ST.WriteLine(oraFile)

    ; Only process if the .ora file does not exist
    if !FileExist(oraFile) {
        ;ST.WriteLine("Processing: " . A_LoopFileName)

        ; Open the .pdn file in Paint.NET
        Run '"' paintDotNetPath '" "' A_LoopFileFullPath '"'
        ; Wait for Paint.NET to become active
        WinWaitActive("paint.net")
        Sleep(1000) ; Wait for Paint.NET to fully load the file

        ; Automate the saving process as OpenRaster (.ora)
        Send("^+s")          ; Control+Shift+S (Save As)
        Sleep(1000)          ; Wait for Save As dialog
        Send("{Tab}")        ; Move to file type selector
        Sleep(500)
        Send("o")            ; Select OpenRaster (.ora)
        Sleep(500)
        Send("{Enter}")      ; Confirm Save
        Sleep(1000)
        Send("{Enter}")      ; Confirm overwrite if prompted
        Sleep(4000)

        ; Close Paint.NET window
        WinClose("paint.net")
        Sleep(2000) ; Wait for the window to close before the next file
    } else {
        tmp := ""
        ;ST.WriteLine("Skipping: " . A_LoopFileName . " (ORA file exists)")
    }
    if FileExist(oraFile) and (deleteFiles = "Yes") {
        FileDelete(A_LoopFileFullPath)
    }
}

MsgBox("All PDN files processed.")
ExitApp
