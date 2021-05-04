from tkinter import *
import random
root = Tk()
lbl = Label(root, text='')
def generate():
	global lbl
	enemy = random.choice (["dog", "cat", "rat", "mouse", "spider"])
	name = random.choice (["Jack", "Donald", "Alex", "Zack", "Steve", "Bob"])
	adj = random.choice(["grimy", "muddy", "awful", "grotesque", "hideous", "adorable", "cute"])
	first1 = "A young man " + name + " was sitting in front of a window in his apartment and dreaming about success.\n"
	first2 = name + " was thinking about his accumulated issues, the weather was rainy and this helped him to stay calm and find right way.\n"
	first3 = "It was a beautiful sunny day, " + name + " came home after college and prepared to play with his friends in online game.\n"
	second = "Suddenly he noticed a small movement out of the corner of the eye and heard some noise.\n"
	third1 = name + " came there and saw a " + adj + " " + enemy + "\n"
	third2 = "He went to this sound and found a " + adj + " " + enemy + "\n"
	third3 = name + " was very interesting to know what was that and he went to this noise, finally he met " + adj + " " + enemy + "\n"
	fourth1 = name + " was surprised, how did it enter into his house? He thought what to do with it.\n"
	fourth2 = "He was scared a little bit, but decided to do one thing.\n"
	fourth3 = name + " was confused, what the hell is that? However he made a decision instantly.\n"
	last1 = "He killed it very fast and got rid of a corpse by throwing it in the trash.\n"
	last2 = "He didn't want someone live with him so he gently kicked him out on the street.\n"
	last3 = "He was very kind person so he sheltered him and they became friends.\n"
	end = "That day " + name + " opened his real personality and this occasion will affect on his future."
	begin = [first1, first2, first3]
	middle = [third1, third2, third3]
	before_last = [fourth1, fourth2, fourth3]
	last = [last1, last2, last3]
	r1 = random.choice(begin)
	r2 = random.choice(middle)
	r3 = random.choice(before_last)
	r4 = random.choice(last)
	story = r1 + second + r2 + r3 + r4 + end
	lbl.destroy()
	lbl = Label(root, text=story)
	lbl.pack()
btn = Button(root, text='Generate story', command=generate)
btn.pack()
root.mainloop()