from tkinter import*
root = Tk()
root.title("Title")
root.geometry("1000x1000")


d = {'Apple' : 'A fruit which grows in a tree',
     'Gouva' : 'A second fruit which grows in a tree',
     'Pineapple' : 'A third fruit which grows in a tree'}

a = Label(root)
g = Label(root)
p = Label(root)

def ab():
    a["text"] = d['Apple']
    
def gh():
    g["text"] = d['Gouva']
    
def pq():
    p["text"] = d['Pineapple']


a1 = Button(root,text = "Text1",command = ab)
g1 = Button(root,text = "Text2",command = gh)
p1 = Button(root,text = "Text3",command = pq)

a.place(relx = 0.5 , rely = 0.2,anchor = CENTER)
g.place(relx = 0.5 , rely = 0.4,anchor = CENTER)
p.place(relx = 0.5 , rely = 0.6,anchor = CENTER)

a1.place(relx = 0.5 , rely = 0.1,anchor = CENTER)
g1.place(relx = 0.5 , rely = 0.3,anchor = CENTER)
p1.place(relx = 0.5 , rely = 0.5,anchor = CENTER)

root.mainloop()