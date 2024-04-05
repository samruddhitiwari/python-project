from tkinter import *
import random
import ctypes
import sys
GRID_SIZE=36
class Cell:
    all=[]
    cell_count=GRID_SIZE
    cell_count_label_object=None
    def __init__(self,x,y,is_mine=False):
        self.is_mine=is_mine
        self.is_opened=False
        self.is_mine_candidate=False
        self.cell_btn_object=None
        self.x= x 
        self.y= y 
        


        Cell.all.append(self)

    def create_btn_object(self,location):
        btn=Button(
            location,width=6,height=2
        )
        btn.bind('<Button-1>',self.left_click_actions)
        btn.bind('<Button-3>',self.right_click_actions)
        self.cell_btn_object=btn

    @staticmethod
    def create_cell_count_label(location):
        lbl=Label(
            location,
            text=f"Cells Left:{Cell.cell_count}",font=("",15),
            bg='black',
            fg='white'

        )
        Cell.cell_count_label_object= lbl

    
    def left_click_actions(self,event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length==0:
                for cell_obj in self.surrounnded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            if Cell.cell_count==9:
                ctypes.windll.user32.MessageBoxW(0,'Congratulations!You won the Game!!','Game Over',0)
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x==x and cell.y==y:
                return cell
    @property
    def surrounnded_cells(self):
        cells=[self.get_cell_by_axis(self.x-1,self.y-1),
                          self.get_cell_by_axis(self.x-1,self.y),
                          self.get_cell_by_axis(self.x-1,self.y+1),
                          self.get_cell_by_axis(self.x,self.y-1),
                          self.get_cell_by_axis(self.x+1,self.y-1),
                          self.get_cell_by_axis(self.x+1,self.y),
                          self.get_cell_by_axis(self.x+1,self.y+1),
                          self.get_cell_by_axis(self.x,self.y+1)]
        cells=[cell for cell in cells if cell is not None]
        return cells
    @property
    def surrounded_cells_mines_length(self):
        counter=0
        for cell in self.surrounnded_cells:
            if cell.is_mine:
                counter+=1
        return counter
    
    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count-=1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f"Cells Left:{Cell.cell_count}")
            self.cell_btn_object.configure(bg='SystemButtonFace')   
        self.is_opened=True

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0,'You Clicked on a Mine!!','Game Over',0)
        sys.exit()
        
    def right_click_actions(self,event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg='orange')
            self.is_mine_candidate=True
        else:
            self.cell_btn_object.configure(bg='SystemButtonFace')
            self.is_mine_candidate=False 
        
    @staticmethod
    def randomize_mines():
        picked_cells=random.sample(Cell.all,9)
        for picked_cell in picked_cells:
            picked_cell.is_mine=True
     
    def __repr__(self):
        return f"Cell({self.x},{self.y})"
    



root=Tk()
#override the settings of the window
root.configure(bg="black")
root.geometry('720x600')
root.title("Minesweeper Game")
root.resizable(False,False)

top_frame=Frame(
    root,
    bg="black",
    width=720,
    height=180
    )
top_frame.place(x=0,y=0)

game_title=Label(top_frame,
                 bg='black',
                 fg='white',
                 text='Minesweeper Game',
                 font=('',30)
                 )
game_title.place(x=180,y=0)

left_frame=Frame(
    root,
    bg="black",
    width=360,
    height=540
)
left_frame.place(x=0,y=180)
center_frame=Frame(
    root,
    bg='black',
    width=540,
    height=450
)
center_frame.place(x=180,y=180)


for x in range(6):
    for y in range(6):
        c=Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
         column=y,
         row=x)

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0,y=0)
Cell.randomize_mines()

#run the window
root.mainloop()