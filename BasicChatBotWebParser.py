import requests
from bs4 import BeautifulSoup
import tkinter as tk
import certifi


# List of preset URLs
URLS = [
    "https://silicophilic.com/microphone-is-not-working/",
    "https://example.org",
    "https://example.net"
]

def scrape_website(url):
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')

    paragraphs = soup.find_all('p')

    return paragraphs

def generate_response(question, paragraphs):
    for paragraph in paragraphs:
        if question.lower() in paragraph.text.lower():
            return paragraph.text
    
    return "I'm sorry, but I couldn't find any relevant information."

def get_response():
    user_question = user_input.get()

    for url in URLS:
        paragraphs = scrape_website(url)
        response = generate_response(user_question, paragraphs)
        
        if response is not None:
            response_text.delete(1.0, tk.END)
            response_text.insert(tk.END, response)
            return

    response_text.delete(1.0, tk.END)
    response_text.insert(tk.END, "I'm sorry, but I couldn't find any relevant information.")

# Create the UI
root = tk.Tk()
root.title("Web Scraping Chatbot")

# Question Entry
question_label = tk.Label(root, text="Enter your question:")
question_label.pack()

user_input = tk.Entry(root, width=50)
user_input.pack()

# Response Text
response_label = tk.Label(root, text="Response:")
response_label.pack()

response_text = tk.Text(root, height=10, width=50)
response_text.pack()

# Submit Button
submit_button = tk.Button(root, text="Submit", command=get_response)
submit_button.pack()

root.mainloop()
