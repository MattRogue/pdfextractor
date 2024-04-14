import tkinter as tk
from tkinter import filedialog

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Prompt the user to select a file
    file_path = filedialog.askopenfilename(
        title="Select a PDF file", 
        filetypes=[("PDF files", "*.pdf")]
    )
    
    # Check if a file was selected
    if file_path:
        # Verify if the selected file is a PDF
        if file_path.lower().endswith('.pdf'):
            return file_path
        else:
            return None
    else:
        return None
