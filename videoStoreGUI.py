'''
Program: videoStoreGUI.py
Author: Mike Horan
Date: 10/21/20

GUI based application that calculates the total cost of a customer's video rental purchases
'''

from breezypythongui import EasyFrame
from tkinter.font import Font

class VideoStore(EasyFrame):
	#Displays Displays window with widgets

	def __init__(self):
		#sets up window and constants
		EasyFrame.__init__(self, title = 'Five Star Retro Video', background = '#f0f0f0')
		self.newRental = 3
		self.oldRental = 2
		#create font objects
		titleFont = Font(family = 'Courier New', size = 24, weight = 'bold')
		labelFont = Font(family = 'Courier New', size = 12, weight = 'normal')
		outputFont = Font(family = 'Courier New', size = 14, weight = 'bold')
		#adds labels and entry fields
		self.titleLabel = self.addLabel(text = 'Five Star Retro Video', row = 0, column = 0, columnspan = 2, sticky = 'NSEW', background = '#f0f0f0', font = titleFont)
		self.newLabel = self.addLabel(text = 'New videos being rented:', row = 1, column = 0, font = labelFont, sticky = 'E', background = '#f0f0f0')
		self.newField = self.addIntegerField(value = 0, row = 1, column = 1, sticky = 'W')
		self.oldLabel = self.addLabel(text = 'Old videos being rented:', row = 2, column = 0, font = labelFont, sticky = 'E', background = '#f0f0f0')
		self.oldField = self.addIntegerField(value = 0, row = 2, column = 1, sticky = 'W')
		self.outputLabel = self.addLabel(text = 'Total Cost:', row = 4, column = 0, font = labelFont, sticky = 'E', background = '#f0f0f0')
		self.totalLabel = self.addLabel(text = '$0', row = 4, column = 1, sticky = 'W', font = outputFont, background = '#f0f0f0', foreground = 'red')
		#add command button
		self.addButton(text = 'Calculate Cost', row = 3, column = 0, columnspan = 2, command = self.totalCost)
		#dark mode toggle
		self.darkCB = self.addCheckbutton(text = 'Dark Mode', row = 5, column = 0, sticky = 'W')
		self.darkCB.bind('<Button-1>', lambda event: self.darkMode())

	def totalCost(self):
		#get user input and calculate cost
		newNum = self.newField.getNumber()
		oldNum = self.oldField.getNumber()
		totalCost = ((self.newRental * newNum) + (self.oldRental * oldNum))
		#output cost
		self.totalLabel['text'] = '$' + str(totalCost)

	def darkMode(self):
		#changes color scheme to darkmode using checkbutton
		if self.darkCB.isChecked():
			self.setBackground('#f0f0f0')
			self.titleLabel['background'] = '#f0f0f0'
			self.titleLabel['foreground'] = 'black'
			self.newLabel['background'] = '#f0f0f0'
			self.newLabel['foreground'] = 'black'
			self.oldLabel['background'] = '#f0f0f0'
			self.oldLabel['foreground'] = 'black'
			self.outputLabel['background'] = '#f0f0f0'
			self.outputLabel['foreground'] = 'black'
			self.totalLabel['background'] = '#f0f0f0'
		else:
			self.setBackground('#1e1e1e')
			self.titleLabel['background'] = '#1e1e1e'
			self.titleLabel['foreground'] = 'white'
			self.newLabel['background'] = '#1e1e1e'
			self.newLabel['foreground'] = 'white'
			self.oldLabel['background'] = '#1e1e1e'
			self.oldLabel['foreground'] = 'white'
			self.outputLabel['background'] = '#1e1e1e'
			self.outputLabel['foreground'] = 'white'
			self.totalLabel['background'] = '#1e1e1e'

			
def main():
	#instantiates and pops up window
	VideoStore().mainloop()

main()