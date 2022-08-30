frame = tk.Frame(root)
frame.pack()

#def say_hi():
#	print("Hello!!")

button = tk.Button(frame,
					text = "CLICK ME",
					fg = "red",
					command = lambda : print("Hello!!"))

button.pack(side = tk.LEFT)
root.mainloop()