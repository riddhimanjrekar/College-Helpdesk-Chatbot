from tkinter import *
from tkinter import scrolledtext
import re

# Optional personalization
user_name = None

# Updated response generation logic
def generate_response(user_input):
    global user_name
    user_input_lower = user_input.lower()

    # Detect name if provided
    name_match = re.search(r"i am (\w+)", user_input, re.IGNORECASE)
    if name_match:
        user_name = name_match.group(1).capitalize()
        return f"Nice to meet you, {user_name}! How can I assist you today?"

    # Keyword-response pairs
    keyword_map = {
        "hi|hello|hey": "Hi there!  Welcome to BVCOE HelpDesk Chatbot. How can I help you?",
        "course duration|duration": "Our BE courses are 4 years long, split into 8 semesters.",
        "placement": "Top companies visit our campus and placements are excellent!",
        "visit|visiting hours|opens": "The college is open from 9 AM to 5 PM, Monday to Friday.",
        "eligible|eligibility": "Eligibility: 10+2 with PCM subjects.",
        "documents": "You'll need marksheets, ID proof, photos, and other certificates.",
        "application form|apply": "You can apply through our online portal on the website.",
        "semester|semesters": "We have 8 semesters in total, each about 6 months.",
        "about your college|about the college": "We focus on Social Transformation through Dynamic Education with lectures, tutorials, and workshops.",
        "deadline|last date": "Application deadlines are usually in June. Check our website for the exact date.",
        "courses": "We offer BE in Computer, IT, Mechanical, Civil, Chemical, and E&TC.",
        "fees|fee structure": "Visit www.bharatividyapeethfees.com for fee details.",
        "admission|process": "Admissions are based on JEE Main or MHT CET scores.",
        "location|where|address": "The college is located in CBD Belapur, Navi Mumbai.",
        "facilities": "Modern labs, WiFi, library, canteen, and sports complex are available.",
        "founder": "The founder of Bharati Vidyapeeth is Dr. Patangrao Kadam.",
        "ok|okay": "Can I help you with anything else?",
        "no|thank you|thanks": "Have a great day ahead!",
        "bye|exit": "Goodbye! Feel free to message me anytime."
    }

    # Match and collect all keywords with their positions
    matches = []
    for pattern, response in keyword_map.items():
        match = re.search(pattern, user_input_lower)
        if match:
            matches.append((match.start(), response))  # (position, response)

    # Sort responses by order of keyword appearance
    matches.sort(key=lambda x: x[0])

    if matches:
        responses_in_order = [resp for _, resp in matches]
        return "\n\n".join(responses_in_order)
    else:
        return "Hmm.. I'm not sure how to answer that. Can you try asking in a different way?"

# Send message function
def send_message():
    user_msg = entry.get()
    if user_msg.strip() == "":
        return
    chat_window.insert(END, "You: " + user_msg + "\n")
    bot_reply = generate_response(user_msg)
    if user_name:
        bot_reply = bot_reply.replace("Hi there!", f"Hi {user_name}!")
    chat_window.insert(END, "Bot: " + bot_reply + "\n\n")
    entry.delete(0, END)
    chat_window.see(END)

# GUI setup
root = Tk()
root.title("BVCOE Chatbot")
root.geometry("550x600")

chat_window = scrolledtext.ScrolledText(root, wrap=WORD, font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=BOTH, expand=True)

entry = Entry(root, font=("Arial", 14))
entry.pack(padx=10, pady=10, fill=X)
entry.bind("<Return>", lambda event: send_message())

send_button = Button(root, text="Send", font=("Arial", 12), command=send_message)
send_button.pack(pady=5)

# Welcome message
chat_window.insert(END, "Bot: Hello! I’m BVCOE HelpDesk Chatbot.\nHow can I help you?\n\n")

root.mainloop()
