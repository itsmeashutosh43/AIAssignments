from tkinter import *

class MainClass:
	def __init__(self,master):
		self.master=master
		self.frame=Frame(self.master,width=1200,height=800)
		self.frame.grid()

	def LoadHomePage(self):
		



		send1M = Button(
            self.frame, text="Send 1 Missionary", command=self.send1Mi)
		send1M.grid(row=0, column=0)

<<<<<<< HEAD

=======
>>>>>>> 9c71c4dd6e9d8bb3d3937618dc379b5dc2bfb242
		send1C = Button(self.frame, text="Send 1 Cannibal", command=self.send1Ca)
		send1C.grid(row=0, column=1)

		send2M = Button(
            self.frame, text="Send 2 Missionary", command=self.send2Mi)
		send2M.grid(row=0, column=3)

		send2C = Button(self.frame, text="Send 2 Cannibal", command=self.send2Ca)
		send2C.grid(row=0, column=4)

		send1B = Button(self.frame, text="Send 1-1 Both", command=self.send1Bo)
		send1B.grid(row=0, column=5)



		canvas=Canvas(self.frame,width=1200,height=800)
		canvas.grid()
		canvas.create_rectangle(400,100,800,800,fill='blue')
		canvas.create_rectangle(0,100,400,800,fill='green')
		canvas.create_rectangle(800,100,1200,800,fill='green')


	def send1Mi():
<<<<<<< HEAD
		# destroy all image
		# state + 1

=======
>>>>>>> 9c71c4dd6e9d8bb3d3937618dc379b5dc2bfb242
		pass

	def send1Ca():
		pass

	def send2Mi():
		pass

	def send2Ca():
		pass

	def send1Bo():
		pass



root=Tk()
mainObject=MainClass(root)

mainObject.LoadHomePage()

root.mainloop()



