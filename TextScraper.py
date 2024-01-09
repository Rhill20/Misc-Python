import tkinter as tk
from tkinter import filedialog

def filter_text():
    # Get the selected text file path
    file_path = file_path_entry.get()

    # Get the search term
    search_term = search_entry.get()

    # Perform the filtering
    filtered_lines = []
    with open(file_path, 'r') as file:
        for line in file:
            if search_term.lower() in line.lower():
                filtered_lines.append(line)

    # Display the filtered lines in the text area
    text_area.delete('1.0', tk.END)
    for line in filtered_lines:
        text_area.insert(tk.END, line)

def select_file():
    # Open a file dialog to select the text file
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])

    # Update the file path entry with the selected file path
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(tk.END, file_path)

# Create the main window
root = tk.Tk()
root.title("Text Scraper")

# Create a label and entry for the file path
file_path_label = tk.Label(root, text="Text File Path:")
file_path_label.pack()
file_path_entry = tk.Entry(root)
file_path_entry.pack()

# Create a button to select the text file
select_file_button = tk.Button(root, text="Select File", command=select_file)
select_file_button.pack()

# Create a label and entry for the search term
search_label = tk.Label(root, text="Search Term:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()

# Create a button to filter the text file
filter_button = tk.Button(root, text="Filter", command=filter_text)
filter_button.pack()

# Create a text area to display the filtered lines
text_area = tk.Text(root, height=10, width=50)
text_area.pack()

# Start the main event loop
root.mainloop()
