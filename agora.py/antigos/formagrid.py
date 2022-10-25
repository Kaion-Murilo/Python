
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def inserir():
    if vid.get()=="" or vnome.get()=="" or vfone.get()=="":
        messagebox.showinfo(title="ERRO",message="digiti todos os dados")
        return
    tv.insert("","end",values=(vid.get(),vnome.get(),vfone.get(),vidade.get(),vsexo.get(),))
    vid.focus()
    
Janela = Tk()
Janela.title("interface - mangar")
Janela.geometry("700x500")
Janela.configure(background="#55626b")
# v=['2','kain','2222','20','2','sexo'],['1','murilo','33333','30','2','masc'],['3','lau','1111','40','3','femi']
tv=ttk.Treeview(Janela,columns=('id','nome','numero','idade','sexo'),show='headings')
tv.column('id',minwidth=0,width=50)
tv.column('nome',minwidth=0,width=120)
tv.column('numero',minwidth=0,width=100)
tv.column('idade',minwidth=0,width=150)
tv.column('sexo',minwidth=0,width=200)
tv.heading('id',text='ID')
tv.heading('nome',text='nome')
tv.heading('numero',text='numero')
tv.heading('idade',text='Idede')
tv.heading('sexo',text='sexo')
tv.place(relx=0.9, rely=0.9,relwidth=1 ,relheight=98)
# print("oi")

btn_inserir=Button(Janela,text="inserir",command=inserir )
btn_deleta=Button(Janela,text="deletar",)
btn_obter=Button(Janela,text="obter",)

ibid=Label(Janela,text="id",)
vid=Entry(Janela)
ibnome=Label(Janela,text="nome",)
vnome=Entry(Janela)
ibfone=Label(Janela,text="fone")
vfone=Entry(Janela)
ibmatricula=Label(Janela,text="matricula",anchor=W)
vmatricula=Entry(Janela)
ibidade=Label(Janela,text="idade",anchor=W)
vidade=Entry(Janela)
ibsexo=Label(Janela,text="sexo",anchor=W)
vsexo=Entry(Janela)
ibcpf=Label(Janela,text="cpf",anchor=W)
vcpf=Entry(Janela)
ibid.grid(column=0,row=0,stick='W')
vid.grid(column=0,row=1)
ibnome.grid(column=1,row=0,stick='W')
vnome.grid(column=1,row=1)
ibfone.grid(column=2,row=0,stick='W')
vfone.grid(column=2,row=1)
ibmatricula.grid(column=3,row=0,stick='W')
vmatricula.grid(column=3,row=1)
ibidade.grid(column=4,row=0,stick='W')
vidade.grid(column=4,row=1)
ibsexo.grid(column=5,row=0,stick='W')
vsexo.grid(column=5,row=1)
ibcpf.grid(column=6,row=0,stick='W')
vcpf.grid(column=6,row=1)

tv.grid(column=0,row=3,columnspan=5,pady=9)

btn_inserir.grid(column=0,row=4)
btn_deleta.grid(column=1,row=4)
btn_obter.grid(column=2,row=4)

Janela.mainloop()