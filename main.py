#!.\venv\Scripts\python.exe

from extractor.ui import select_file
#from extractor.text import script
from extractor.image import script

def main():
    pdf = select_file()
    if pdf:
        print(f"Selected PDF file: {pdf}")
        script(pdf)
    else:
        print("Please select a valid PDF file.")
    
    
    
    
    
if __name__ == "__main__":
    main()
