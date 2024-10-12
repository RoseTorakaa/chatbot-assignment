import pyttsx3
import config
import os
import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import google.generativeai as genai   









genai.configure(api_key='AIzaSyBtNl-QuQPfF7jCyv8kKSVcGMlmsfSQCzg')

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dr dele api\dr-dele-chatbot-assignment-8ee161ea2fbc.json"

def Speech_to_Text():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.3)
        try:
            audio = r.listen(source)
            my_text = r.recognize_google(audio)
            txtSpeech.insert(tk.END, "ROSE: " + my_text + "\n\n")
        except sr.UnknownValueError:
            txtSpeech.insert(tk.END, "Could not understand audio\n\n")
        except sr.RequestError as e:
            txtSpeech.insert(tk.END, "Error: {0}\n".format(e))


    
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    chat = model.start_chat(history=[])

    while(True):
        # language= 'en'
        if(my_text.strip()==''):
            break
        else:
            response = chat.send_message(my_text)
            # speech = BytesIO()
            gemini_text=response.text
            txtSpeech.insert(tk.END, "AI Rose: " + gemini_text + "\n") 
            engine=pyttsx3.init()
            engine.setProperty('rate', 220)
            voices = engine.getProperty('voices')       #getting details of current voice
            engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
            engine.say(gemini_text)
            engine.runAndWait()
            
            break


def exit_speech():
    iExit=messagebox.askquestion("Exit","confirm if you want to exit")
    if iExit=="yes":
        messagebox.showinfo("exit speech","goodbye")
        root.destroy()

def reset_speech():
    txtSpeech.delete("1.0", tk.END)

root = tk.Tk()
root.title="speech to text"

RootFrame=tk.Frame(root,width=800, height=600, bd=20, bg="black")
RootFrame.pack()

MainFrame=tk.Frame(RootFrame,width=950, height=500, bd=20)

lbltitle = tk.Label(MainFrame, font= ('Arial',50,'bold'),width=20, text= "Torakaa Rose Chatbot")
lbltitle.pack()

txtSpeech= tk.Text(MainFrame, font= ('calibri',20,'italic','bold'),width=70, height=13)
txtSpeech.pack()

bconvert= tk.Button(MainFrame, font=('arial',10,'bold'),width=10, height=2, text="Convert", command=Speech_to_Text)
bconvert.pack(side='bottom', padx=2)

breset= tk.Button(MainFrame, font=('arial',10,'bold'),width=10, height=2, text="Reset", command=reset_speech)
breset.pack(side='bottom', padx=2)

bexit= tk.Button(MainFrame, font=('arial',10,'bold'),width=10, height=2, text="Exit", command=exit_speech)
bexit.pack(side='bottom', padx=2)
MainFrame.pack()

root.mainloop()



