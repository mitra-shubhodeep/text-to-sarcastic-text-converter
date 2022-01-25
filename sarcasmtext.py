import tkinter as tk

win = tk.Tk()
win.title('Sarcastic Text Converter')

canvas1=tk.Canvas(win, width=400, height=300)
canvas1.pack()

label2 = tk.Label(win, text='Enter the text you want to convert below')
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (win)
canvas1.create_window(200, 140, window=entry1)

def sarc():
    text = entry1.get()
    sar_text=""
    l=len(text)
    for i in range(l):
        if i%2==0:
            sar_text+=text[i].lower()
        else:
            sar_text+=text[i].upper()

    w = tk.Text(win, height=1, borderwidth=0)
    w.insert(1.0, sar_text)
    w.pack()

    w.configure(state="disabled")
    w.configure(inactiveselectbackground=w.cget("selectbackground"))


    #/label1 = tk.Label(win, text=sar_text)
    #canvas1.create_window(200, 230, window=label1)

button1 = tk.Button(win, text="Convert",command=sarc,bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200,180,window=button1)


win.mainloop()
