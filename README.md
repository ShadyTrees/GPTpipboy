# GPTpipboy
A GUI and Data Structure to interact with the OpenAI API, and store results.


ChatGPT Interface and Data Structure V1.0 by ShadyTrees


DESCRIPTION:


This is a Python script that builds a basic GUI using the tkinter library. The interface is designed to
interact with an OpenAI API, and save the prompts/responses in an indexed and time stamped data structure.
By default, the data is saved as a csv, but the supporting pandas library can utilize various types of file
formats, including JSON.

There is also basic functionality to view elements of the data structure by index, and a memory function
that transfers whatever is in the display to the input, allowing ChatGPT to recollect previous conversation.


REQUIREMENTS:


1) Python 3.10 or similar
2) Installation of Pandas Library
3) Installation of OpenAI Library
4) An OpenAI API key.


SETUP:


1) Ensure Python and Library Dependencies are installed.
2) Ensure either the included csv file is in the same folder, or un-comment line 126 and run script to
   initialize one. Make sure to re-comment line 126 after file is created if using this method.
3) Add your API key to the given field on line 11. It requires quotations.
4) Run the script!


CONTROLS:


						Text Boxes

a) DisplayBox - Upper text box that displays outputs. Is editable, allowing you to modify responses to reduce
		token costs when adding conversation history to the next prompt. 

b) InputBox - 	Lower text box that is used to input prompts to the API.

						Buttons

a) Archive+ - 	Moves forward through the dataframe by one index and displays the Prompt/Solution in the
		DisplayBox

b) Archive- -	Moves backwards through the dataframe by one index and displays the Prompt/Solution in the
		DisplayBox

c) Memory - 	Transers any content from the DisplayBox into the InputBox. Useful for providing the API
		with context from a previous prompt.

d) ClrTop - 	Clears all content from the DisplayBox

e) ClrBtm - 	Clears all content from the InputBox

f) Send - 	Sends the contents of InputBox to the API and displays the results in DisplayBox.


THEORY:


My main objective was to create a simple interface to communicate with the ChatGPT API and store the prompts and
responses in an indexed and time stamped data format. I feel that I have succeeded in this goal. This program
is quite barebones - there is no real text formatting, as you will notice when words parse to the next line in
a text box. My focus was on rapid deployment and functionality, and some bells and whistles were definitely 
spared in that regard.

Another design decision I made, was to not hard code any previous responses into the chat prompt, due to wanting
to make my token usage as slim as possible. I added the memory button to allow me to quickly transfer previous
conversation into the InputBox so that I could provide context when needed. This essentially functions the same 
as adding it into the actual prompt, you just have to preface the previous prompt/responses with Prompt: or
Response:.

This functionality combined with the archive buttons, allows you to quickly display any previous prompt/response
pair, edit or shorten it in the display box to save tokens, and then transfer it to the input box using the
memory button, for contextual use by the API. Simply write your new prompt below this data.


DRAWBACKS:


1) This script was designed for personal use and is not production ready.
2) The API key is visible in the script.
3) The entire csv file is read in numerous functions. If the file size gets too large, it may cause slowdown
   and it is recommended to start a new file if any issues arise.
4) The text that is displayed is not formatted and words may parse to the next line in the text box.



Thank you for your time, and I hope you find my script useful!
