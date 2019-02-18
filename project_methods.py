import tkinter
#from class_file import *


# loads the stats for a player's username
def load_stats():
    username= Load.username_entry.get()

    # open save file
    save_file= open('saved_data.txt' , 'r')
    find(username)



