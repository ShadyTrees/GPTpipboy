# ChatGPT Interface by ShadyTrees
# V 1.0

import tkinter as tk
import pandas as pd #installed
import numpy as np
import os
import openai #installed
from datetime import datetime

openai.api_key = ("API KEY GOES HERE")

#Main function that transmits to and receives from API.
def promptScrape():
    promptBody = txtInput.get("1.0", tk.END)
    txtInput.delete("1.0", tk.END)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[
                                                    {"role":"system","content":"You are a creative assistant."},
                                                    {"role":"user", "content":f"{promptBody}"}
                                                      ],
                                            temperature = 0.2,
                                            max_tokens=500
                                            )
    cleanResponse = parse_response(response)
    clayFrame = pd.read_csv("archive.csv", index_col=[0])
    babyFrame = pd.DataFrame(
        {"Prompt":[promptBody],
         "Solution":[cleanResponse],
         "Date/Time":[f"{datetime.now():%X, %x}"],
        }
    )
    clayFrame = clayFrame._append(babyFrame, ignore_index=True)
    clayFrame.to_csv("archive.csv")
    txtDisplay.insert(tk.END, "\n\n")
    txtDisplay.insert(tk.END, promptBody)
    txtDisplay.insert(tk.END, "\n\n")
    txtDisplay.insert(tk.END, cleanResponse)
    txtDisplay.insert(tk.END, "\n\n")

#Function that parses output from API to readable text format.
def parse_response(response):
    choices = response.get('choices')
    if choices and len(choices) > 0:
        first_choice = choices[0]
        message = first_choice.get('message')
        if message:
            content = message.get('content')
            if content:
                return content.strip()
    return None

#Moves to the next element in the dataframe and displays it.
def archivePull():
    global countArchive
    countArchive +=1
    txtDisplay.delete("1.0", tk.END)
    archiveFrame = pd.read_csv("archive.csv", index_col=[0])
    if countArchive < len(archiveFrame):
        archivePage = archiveFrame.iloc[countArchive,0:3]
        txtDisplay.insert(tk.END, archivePage["Prompt"])
        txtDisplay.insert(tk.END, "\n\n\n")
        txtDisplay.insert(tk.END, archivePage["Solution"])
    else:
        txtDisplay.insert(tk.END, "END")
        countArchive = len(archiveFrame)
        
#Moves to the previous element in the dataframe and displays it.
def archivePush():
    global countArchive
    countArchive -=1
    txtDisplay.delete("1.0", tk.END)
    archiveFrame = pd.read_csv("archive.csv", index_col=[0])
    if countArchive >= 0:
        archivePage = archiveFrame.iloc[countArchive,0:3]
        txtDisplay.insert(tk.END, archivePage["Prompt"])
        txtDisplay.insert(tk.END, "\n\n\n")
        txtDisplay.insert(tk.END, archivePage["Solution"])
    else:
        txtDisplay.insert(tk.END, "START")
        countArchive = -1

#Displays the last element in the dataframe
def archiveLast():
    global countArchive
    txtDisplay.delete("1.0", tk.END)
    archiveFrame = pd.read_csv("archive.csv", index_col=[0])
    inlaidCount = len(archiveFrame)-1
    archivePage = archiveFrame.iloc[inlaidCount,0:3]
    txtDisplay.insert(tk.END, archivePage["Prompt"])
    txtDisplay.insert(tk.END, "\n\n\n")
    txtDisplay.insert(tk.END, archivePage["Solution"])
    countArchive = inlaidCount

#Transfers the display text to the input box
def memSwap():
    memHolder = txtDisplay.get("1.0", tk.END)
    txtInput.insert("1.0", memHolder)

#Clears display textbox
def clrTop():
    txtDisplay.delete("1.0", tk.END)

#Clears input textbox
def clrBtm():
    txtInput.delete("1.0", tk.END)

#Global counter used in archive functions    
countArchive = -1

window = tk.Tk()
window.title("ChatGPT Interface")


#Basic data structure framework.
chatArchive = pd.DataFrame(
    {
        "Prompt":["QuestionOne","QuestionTwo","QuestionThree",],
        "Solution":["AnswerOne","AnswerTwo","AnswerThree",],
        "Date/Time":[0,0,0,]
    }
)

#Initializes dataFrame with basic data structure- uncomment and run script to build new dataframe!
#WILL WIPE PREVIOUS DATA IF ACTIVE ON RUN, MAKE SURE TO RE-COMMENT AFTER SETUP
#chatArchive.to_csv("archive.csv")



#Frames
frmButtons = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frmText = tk.Frame(master=window, borderwidth=5)
#Text Boxes
txtDisplay = tk.Text(master=frmText, width=120)
txtInput = tk.Text(master=frmText, width=120, height=10)
#Buttons
btnArchive = tk.Button(master=frmButtons, text="Archive+", command=archivePull)
btnArchiveOpp = tk.Button(master=frmButtons, text="Archive-", command=archivePush)
btnSend = tk.Button(master=frmText, text="Send", width=8, command=promptScrape)
btnLast = tk.Button(master=frmButtons, text="Last", command=archiveLast)
btnMemory = tk.Button(master=frmButtons, text="Memory", command=memSwap)
btnClrTop = tk.Button(master=frmButtons, text="ClrTop", command=clrTop)
btnClrBtm = tk.Button(master=frmButtons, text="ClrBtm", command=clrBtm)
#Text Box Placement
txtDisplay.grid(row=0,column=0, pady=5)
txtInput.grid(row=1,column=0,pady=5)
#Button Placement
btnArchive.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btnArchiveOpp.grid(row=1, column=0, sticky="ew", padx=5)
btnLast.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btnMemory.grid(row=3, column=0, sticky="ew", padx=5, pady=15)
btnClrTop.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
btnClrBtm.grid(row=5, column=0, sticky="ew", padx=5)
btnSend.grid(row=1, column=1, sticky="ew", padx=5)
#Frame Placement
frmText.grid(row=0, column=0, sticky="nsew")
frmButtons.grid(row=0, column=1, sticky="nsew")



window.mainloop()
