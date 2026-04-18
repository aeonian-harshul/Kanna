import os
import sys
import shutil
import subprocess
import threading
import customtkinter as ctk
from tkinter import filedialog, messagebox

# ---------- CONFIG ----------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# ---------- RESOURCE PATH ----------
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ---------- FUNCTIONS ----------
def browse_input():
    folder = filedialog.askdirectory()
    input_entry.delete(0, "end")
    input_entry.insert(0, folder)

def browse_output():
    folder = filedialog.askdirectory()
    output_entry.delete(0, "end")
    output_entry.insert(0, folder)

def compress():
    def run_compression():
        exe_dir = os.getcwd()

        input_path = exe_dir if input_same.get() else input_entry.get()
        if not input_path:
            messagebox.showerror("Error", "Select input folder")
            return

        output_base = exe_dir if output_same.get() else output_entry.get()
        name = os.path.basename(input_path.rstrip("\\/"))
        output_path = os.path.join(output_base, name + "_compressed")

        if os.path.exists(output_path):
            shutil.rmtree(output_path)
        shutil.copytree(input_path, output_path)

        pingo = resource_path("pingo.exe")

        for root_dir, _, files in os.walk(output_path):
            for f in files:
                path = os.path.join(root_dir, f)

                try:
                    if png_var.get() and f.lower().endswith(".png"):
                        subprocess.run(
                            [pingo, f"-s{png_level.get()}", path],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL,
                            creationflags=subprocess.CREATE_NO_WINDOW
                        )

                    if jpg_var.get() and f.lower().endswith((".jpg", ".jpeg")):
                        subprocess.run(
                            [pingo, f"-quality={jpg_quality.get()}", path],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL,
                            creationflags=subprocess.CREATE_NO_WINDOW
                        )
                except:
                    pass

        messagebox.showinfo("Done", f"Saved to:\n{output_path}")

    threading.Thread(target=run_compression).start()

# ---------- UI ----------
app = ctk.CTk()
app.title("Pingo Image Compressor")
app.geometry("560x600")

# ICON
try:
    app.iconbitmap(resource_path("icon.ico"))
except:
    pass

main = ctk.CTkFrame(app, corner_radius=15)
main.pack(padx=15, pady=15, fill="both", expand=True)

ctk.CTkLabel(main, text="Image Compressor", font=("Segoe UI", 20, "bold")).pack(pady=10)

# ---------- PNG ----------
png_var = ctk.BooleanVar(value=True)
ctk.CTkCheckBox(main, text="PNG Compression", variable=png_var).pack(anchor="w", padx=10)

png_level = ctk.IntVar(value=3)

png_container = ctk.CTkFrame(main, fg_color="transparent")
png_container.pack(fill="x", padx=10)

png_value_label = ctk.CTkLabel(png_container, text="s3", font=("Segoe UI", 14, "bold"))
png_value_label.pack()

def update_png(val):
    val = int(float(val))
    png_value_label.configure(text=f"s{val}")

ctk.CTkSlider(
    png_container,
    from_=1,
    to=4,
    number_of_steps=3,
    variable=png_level,
    command=update_png
).pack(fill="x", pady=(0,10))

# ---------- JPG ----------
jpg_var = ctk.BooleanVar(value=True)
ctk.CTkCheckBox(main, text="JPG Compression", variable=jpg_var).pack(anchor="w", padx=10)

jpg_quality = ctk.IntVar(value=80)

jpg_container = ctk.CTkFrame(main, fg_color="transparent")
jpg_container.pack(fill="x", padx=10)

jpg_value_label = ctk.CTkLabel(jpg_container, text="80%", font=("Segoe UI", 14, "bold"))
jpg_value_label.pack()

def update_jpg(val):
    val = int(float(val))
    jpg_value_label.configure(text=f"{val}%")

ctk.CTkSlider(
    jpg_container,
    from_=50,
    to=100,
    number_of_steps=50,
    variable=jpg_quality,
    command=update_jpg
).pack(fill="x", pady=(0,10))

# ---------- INPUT ----------
ctk.CTkLabel(main, text="Input Folder").pack(anchor="w", padx=10)

input_same = ctk.BooleanVar(value=True)
ctk.CTkCheckBox(main, text="Use EXE folder", variable=input_same).pack(anchor="w", padx=10)

input_entry = ctk.CTkEntry(main)
input_entry.pack(fill="x", padx=10, pady=5)

ctk.CTkButton(main, text="Browse", command=browse_input).pack(padx=10, pady=(0,10))

# ---------- OUTPUT ----------
ctk.CTkLabel(main, text="Output Folder").pack(anchor="w", padx=10)

output_same = ctk.BooleanVar(value=True)
ctk.CTkCheckBox(main, text="Save in EXE folder", variable=output_same).pack(anchor="w", padx=10)

output_entry = ctk.CTkEntry(main)
output_entry.pack(fill="x", padx=10, pady=5)

ctk.CTkButton(main, text="Browse", command=browse_output).pack(padx=10, pady=(0,10))

# ---------- RUN ----------
ctk.CTkButton(
    main,
    text="Compress Images",
    height=45,
    corner_radius=10,
    command=compress
).pack(pady=20, padx=10, fill="x")

app.mainloop()