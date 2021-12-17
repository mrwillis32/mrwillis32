


# Importing necessary packages
import shutil
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
	

# Defining CreateWidgets() function to
# create necessary tkinter widgets
def CreateWidgets():
	link_Label = Label(root, text ="Select The File To Copy : ",
					bg = "#E8D579")
	link_Label.grid(row = 1, column = 0,
					pady = 5, padx = 5)
	
	root.sourceText = Entry(root, width = 50,
							textvariable = sourceLocation)
	root.sourceText.grid(row = 1, column = 1,
						pady = 5, padx = 5,
						columnspan = 2)
	
	source_browseButton = Button(root, text ="Browse",
								command = SourceBrowse, width = 15)
	source_browseButton.grid(row = 1, column = 3,
							pady = 5, padx = 5)
	
	destinationLabel = Label(root, text ="Select The Destination : ",
							bg ="#E8D579")
	destinationLabel.grid(row = 2, column = 0,
						pady = 5, padx = 5)
	
	root.destinationText = Entry(root, width = 50,
								textvariable = destinationLocation)
	root.destinationText.grid(row = 2, column = 1,
							pady = 5, padx = 5,
							columnspan = 2)
	
	dest_browseButton = Button(root, text ="Browse",
							command = DestinationBrowse, width = 15)
	dest_browseButton.grid(row = 2, column = 3,
						pady = 5, padx = 5)
	
	copyButton = Button(root, text ="Copy File",
						command = CopyFile, width = 15)
	copyButton.grid(row = 3, column = 1,
					pady = 5, padx = 5)
	
	moveButton = Button(root, text ="Move File",
						command = MoveFile, width = 15)
	moveButton.grid(row = 3, column = 2,
					pady = 5, padx = 5)

def SourceBrowse():
	
	# Opening the file-dialog directory prompting
	# the user to select files to copy using
	# filedialog.askopenfilenames() method. Setting
	# initialdir argument is optional Since multiple
	# files may be selected, converting the selection
	# to list using list()
	root.files_list = list(filedialog.askopenfilenames(initialdir ="/Users/mr.willis / Desktop /Daily Files"))
	
	# Displaying the selected files in the root.sourceText
	# Entry using root.sourceText.insert()
	root.sourceText.insert('1', root.files_list)
	
def DestinationBrowse():
	# Opening the file-dialog directory prompting
	# the user to select destination folder to
	# which files are to be copied using the
	# filedialog.askopendirectory() method.
	# Setting initialdir argument is optional
	destinationdirectory = filedialog.askdirectory(initialdir ="/Users/mr.willis/Desktop/Daily Files")

	# Displaying the selected directory in the
	# root.destinationText Entry using
	# root.destinationText.insert()
	root.destinationText.insert('1', destinationdirectory)
	
def CopyFile():
	# Retrieving the source file selected by the
	# user in the SourceBrowse() and storing it in a
	# variable named files_list
	files_list = root.files_list

	# Retrieving the destination location from the
	# textvariable using destinationLocation.get() and
	# storing in destination_location
	destination_location = destinationLocation.get()

	# Looping through the files present in the list
	for f in files_list:
		
		# Copying the file to the destination using
		# the copy() of shutil module copy take the
		# source file and the destination folder as
		# the arguments
		shutil.copy(f, destination_location)

	messagebox.showinfo("SUCCESSFUL")
	
def MoveFile():
	
	# Retrieving the source file selected by the
	# user in the SourceBrowse() and storing it in a
	# variable named files_list'''
	files_list = root.files_list

	# Retrieving the destination location from the
	# textvariable using destinationLocation.get() and
	# storing in destination_location
	destination_location = destinationLocation.get()

	# Looping through the files present in the list
	for f in files_list:
		
		# Moving the file to the destination using
		# the move() of shutil module copy take the
		# source file and the destination folder as
		# the arguments
		shutil.move(f, destination_location)

	messagebox.showinfo("SUCCESSFUL")

# Creating object of tk class
root = tk.Tk()
	
# Setting the title and background color
# disabling the resizing property
root.geometry("830x120")
root.title("Copy-Move GUI")
root.config(background = "black")
	
# Creating tkinter variable
sourceLocation = StringVar()
destinationLocation = StringVar()
	
# Calling the CreateWidgets() function
CreateWidgets()
	
# Defining infinite loop
root.mainloop()


# Import the following modules
import os
import time
import shutil
import datetime
import glob


# Change the directory and jump to the location
# where you want to arrange the files
os.chdir(r"/Users/mr.willis/Desktop/Home Office Files")

# List the directories and make a list
all_files = list(os.listdir())

# Get the current working directory
outputs = os.getcwd()

# Run a loop for traversing through all the
# files in the current directory
for files in all_files:
	try:
		
		# Jump to the directories files
		inputs = glob.glob(files+"\\*")
		
		# Now again run a loop for travering through
		# all the files inside the folder
		for ele in inputs:
			
			# Now, move the files one-by-one
			shutil.move(ele, outputs)
		
		# After extracting files from the folders,
		# delete that folder
		shutil.rmtree(files)
	except:
		pass

# Again run a loop for traversing through all the
# files in the current directory
for files in os.listdir('/Users/mr.willis/Desktop/Daily Files'):
	
	# Get all the details of the file creation
	# and modification
	time_format = time.getmtime(os.path.getmtime(files))
	
	# Now, extract only the Year, Month, and Day
	datetime_object = datetime.datetime.strptime(str(time_format.tm_mon), "%m")
	
	# Provide the number and find the month
	full_month_name = datetime_object.strftime(
		"%b")
	
	# Give the name of the folder
	dir_name = full_month_name + 'Daily Files' + \
		str(time_format.tm_mday) + "Daily Files" + \
		str(time_format.tm_year)

	# Check if the folder exists or not
	if not os.path.isdir(dir_name):
		
		# If not then make the new folder
		os.mkdir(dir_name)
	dest = dir_name
	
	# Move all the files to their respective folders
	shutil.move(files, dest)
	
print("successfully moved...")

