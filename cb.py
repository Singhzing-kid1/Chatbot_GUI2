from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
from tkinter import * 
from tkinter import ttk
from style.v import *
from ttkthemes import themed_tk as tk
 






#Trains the AI
bot = ChatBot('test')
trainer = ListTrainer(bot)
for _file in os.listdir('context_lib'):
	chats = open('context_lib/' + _file, 'r').readlines()

	trainer.train(chats)






#while True:
#	request = input("You:")
#	response = bot.get_response(request)

	 

#	print('Bot:', response)

#gets user info and gives a response
def respond(event):
    re = ue.get()

    res = bot.get_response(re)



    be.config(state=NORMAL)
    
    
    be.delete(1.0, del_ent)
    ue.delete(0, del_ent)

    be.insert(1.0, res)
    be.config(state=DISABLED)

#Creates the layout and the gui
r = tk.ThemedTk()
r.get_themes()
r.set_theme('clearlooks')
r.title(title)
r.iconbitmap('favicon.ico')




   

ue = ttk.Entry(r)
l = ttk.Label(r, text="")
be = Text(r, width=be_x, height=be_y)
sb = ttk.Button(r, text=sbl)
sb.bind("<Button-1>", respond)
bl = ttk.Label(r, text=bnl)
ul = ttk.Label(r, text=unl)



sb.grid(row=0, column=3)
be.grid(row=4, column=2)
l.grid(row=3, column =2)
ue.grid(row=0, column=2)
bl.grid(row=4, column=1)
ul.grid(row=0, column=1)



r.mainloop()

	 



