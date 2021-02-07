# Follow Us On Twitter @PY4ALL

# Import Required libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
import time

# Class of Main Window
class MainWindow:

    def __init__(self, master):

        # Parameters of the Main Window
        self.myParent = master
        master.title('Game of Life')
        master.resizable(False, False)
        master.configure(background = 'white')

        # Create a Canvas window that will be used to draw the grid
        self.w = Canvas(master, width=600, height=600, bg='white')
        self.w.pack()

        # Create a Frame that will be used to contain the buttons
        self.frame_control = ttk.Frame()
        self.frame_control.pack()


        # Create Start/Stop Buttons
        ttk.Button(self.frame_control, text = 'Run',
                   command = self.start).pack(side = LEFT)
        ttk.Button(self.frame_control, text = 'Stop',
                   command = self.stop).pack(side = LEFT)

        # Empty Arrays will be used to save the grid values
        self.board = []
        self.board_digit = []
        #self.h = []
        #self.v = []
        # Draw the grid
        for i in range(10,590,10):
            temp = []
            temp1 = []
            for j in range(10,590,10):
                temp.append(self.w.create_rectangle(i,j,i+10,j+10))
                temp1.append(0)
            self.board.append(temp)
            self.board_digit.append(temp1)

        # Link the mouse Button click with the method get_loc
        # to change the cell value/color
        self.w.bind("<Button 1>",self.get_loc)

        # Attibutes to save the status of the game
        self.game_end = False
        self.threadStart = False
        



        # Method to change the cell value/color
    def get_loc(self, event):
        if 10 < event.x < 590 and 10 < event.y < 590 :
            if self.board_digit[event.x//10-1][event.y//10-1] == 0:
                self.w.itemconfig(self.board[event.x//10-1][event.y//10-1], fill="blue")
                self.board_digit[event.x//10-1][event.y//10-1] = 1
            else:
                self.w.itemconfig(self.board[event.x//10-1][event.y//10-1], fill="white")
                self.board_digit[event.x//10-1][event.y//10-1] = 0 

        # The main method which represents the game Of Life algorithm
    def gameOfLife(self,arr):
        # Get the size of the input array
        rows = len(arr)
        cols = len(arr[0])
        outarr = []
        # Loop cell by cell within the input array
        for row in range(rows):
            temp = []
            for col in range(cols):
                # Count the total number of live neighbors
                lifecount = 0
                cellStat = 999
                rowp = row+1
                rowm = row-1
                colp = col+1
                colm = col-1
                if rowp <= rows-1:
                    if arr[rowp][col]==1:
                        lifecount += 1
                    if colp <= cols-1:
                        if arr[rowp][colp]==1:
                            lifecount += 1
                        if arr[row][colp]==1:
                            lifecount += 1
                    if colm >= 0:
                        if arr[rowp][colm]==1:
                            lifecount += 1
                        if arr[row][colm]==1:
                            lifecount += 1
                if rowm >= 0:
                    if arr[rowm][col]==1:
                        lifecount += 1
                    if colp <= cols-1:
                        if arr[rowm][colp]==1:
                            lifecount += 1
                    if colm >= 0:
                        if arr[rowm][colm]==1:
                            lifecount += 1
                # Change the status of the current cell based on Game of Life rules
                if arr[row][col] == 1 and 2<=lifecount<=3:
                    cellStat = 1
                elif arr[row][col] == 0 and lifecount==3:
                    cellStat = 1
                else:
                    cellStat = 0
                temp.append(cellStat)
            outarr.append(temp)
        # Return the output array which represents the next generation 
        return outarr

    # Start method 
    def start(self):
        if not self.threadStart:
            self.threadStart = True
            self.game_end = False
            self.run()

    # End method      
    def stop(self):
        self.threadStart = False
        self.game_end = True

    # Run Method:
    # will load the array to gameOfLife to get the next generation  and draw it
    # loop until the user stops  the process
    def run(self):
        while not self.game_end:
            old_board = self.board_digit
            self.board_digit = self.gameOfLife(self.board_digit)
            if old_board == self.board_digit:
                messagebox.showinfo("Stopped", "No changes from the last generation\nSimulation  stopped") 
                self.stop()
                break
            for row in range(58):
                for col in range(58):
                    if self.board_digit[row][col] == 1:
                        self.w.itemconfig(self.board[row][col], fill="blue")
                    else:
                        self.w.itemconfig(self.board[row][col], fill="white")
            time.sleep(0.1)
            self.myParent.update()


            
        
# Main function             
def main():            
    
    root = Tk()
    mainwindow = MainWindow(root)
    root.mainloop()
    
if __name__ == "__main__": main()
