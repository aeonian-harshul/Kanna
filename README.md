# Kanna
Built a lightweight GUI wrapper around Pingo (https://css-ig.net/) to simplify batch image compression for everyday use. The motivation was to reduce large media sizes (e.g., study resources like Anki decks) without noticeable quality loss, while avoiding repetitive command-line usage. 
---

## Motivation

Working with large media collections (e.g., Anki decks, study resources, image folders) often leads to:
- High storage usage
- Slow syncing
- Inefficient file sizes

While Pingo is a powerful optimizer, it is command-line based.  
Kanna was built to provide a simple, one-click interface for efficient image compression while preserving visual quality.

---

## Features

- Batch image compression
- PNG lossless compression (s1–s4 levels)
- JPG lossy compression (adjustable quality 50–100)
- Modern dark-mode GUI
- No command-line usage required
- Creates a separate compressed folder (original files remain untouched)
- Portable executable (no installation required)

---

## Download

Download the latest executable from Releases:

https://github.com/aeonian-harshul/Kanna/blob/main/kanna.exe
<img width="700" height="274" alt="image" src="https://github.com/user-attachments/assets/8d50c450-c062-4869-a9d8-df09416b62d8" />

### ⚠️ Windows SmartScreen Warning
Because Kanna is a newly built, open-source tool without a paid corporate certificate, your browser or Windows Defender may flag the `.exe` as an "unrecognized app."
<img width="225" height="300" alt="image" src="https://github.com/user-attachments/assets/0a0cb58c-65ab-49db-822a-bc97ae47fb77" />
edge showing it me on my own pc

---

## How to Use (EXE)

1. Download the `.exe` from Releases  
2. Place it anywhere (or inside your media folder)  
3. Double-click to run  
4. Select:
   - Compression format (PNG / JPG)
   - Compression level  
5. Choose input/output folders (or use default EXE location)  
6. Click **Compress Images**

Output will be created as:

<original_folder_name>_compressed

---

## Prerequisites to reproduce the .exe

- Python 3.8+
- pip (comes with Python)

You will also need:

- Pingo (image optimizer)  
  Download from: https://css-ig.net/pingo  

- CustomTkinter (modern GUI framework)

---

## Reproduce the .exe

### 1. Clone or download the repository

git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git

OR download ZIP and extract


### 2. Install dependencies

pip install customtkinter


### 3. Add Pingo

- Download `pingo.exe` from the official website  
- Place it in the same folder as `app.py`

Your folder should look like:

app.py  
pingo.exe  
icon.ico  


### 4. Build EXE:
  in the address bar of the folder containing the above mentioned files type cmd and press enter. in cmd window that opens paste following compile command
   
   python -m PyInstaller --onefile --noconsole --icon=icon.ico --add-binary "pingo.exe;." --add-data "icon.ico;." app.py  


### 5. Use the generated executable from `dist/`

#### boop boop
- Ensure `pingo.exe` is always in the same directory as the app  
- If icon does not update, delete `build/`, `dist/`, and rebuild  
- Windows may cache icons — renaming the `.exe` can fix this  

---

---

# Notes

- Only PNG and JPG files are compressed  
- Other file types (GIF, MP4, etc.) remain unchanged  
- Original files are not modified  
- Recommended to keep backups for important data

- Test run on few files to get the feel of the .exe
- it will give pop up on completetion  <img width="528" height="198" alt="image" src="https://github.com/user-attachments/assets/7ac58b2f-a7f6-4432-bc10-2b263fdae03b" />
- if the app doesnt respond, dont panic and wait or just kill the app from task manager (it was compressing the media files in the background)
- dont run the .exe again before the pop up of the previous job comes (for now no way to stop ongoing jop)  

---

## Dependencies

- Pingo (Image Optimizer)  
  https://css-ig.net/pingo  

- CustomTkinter (GUI Framework)  
  https://github.com/TomSchimansky/CustomTkinter  

---

## License & Attribution

This project is a GUI wrapper around Pingo.

Pingo internally uses multiple open-source libraries including:
- Little CMS  
- libdeflate  
- libpng  
- lodepng  
- mozjpeg  
- zlib  
- WebP  


---

## Future Improvements

- Progress bar with live status
- File count and size reduction statistics
- Drag-and-drop folder support
- choose number of threads to use of your cpu

---

## Author

Harshul Sood
