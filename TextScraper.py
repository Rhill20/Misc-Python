import tkinter as tk
from tkinter import filedialog

def filter_text():
    
    file_path = file_path_entry.get()

   
    search_term = search_entry.get()

   
    filtered_lines = []
    with open(file_path, 'r') as file:
        for line in file:
            if search_term.lower() in line.lower():
                filtered_lines.append(line)

    
    text_area.delete('1.0', tk.END)
    for line in filtered_lines:
        text_area.insert(tk.END, line)

def select_file():
    
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])

    
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(tk.END, file_path)

# Create the main window
root = tk.Tk()
root.title("Text Scraper")


file_path_label = tk.Label(root, text="Text File Path:")
file_path_label.pack()
file_path_entry = tk.Entry(root)
file_path_entry.pack()


select_file_button = tk.Button(root, text="Select File", command=select_file)
select_file_button.pack()


search_label = tk.Label(root, text="Search Term:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()


filter_button = tk.Button(root, text="Filter", command=filter_text)
filter_button.pack()


text_area = tk.Text(root, height=10, width=50)
text_area.pack()

# Start the main event loop
root.mainloop()
