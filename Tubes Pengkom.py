
from tkinter import*
from tkinter import ttk

list_nim = ["1602020","1602021","1602022"]
list_PIN = ["12345","54321","12332"]
saldo_akun = [10000000,5000000,1000000]
PIN = None
akun = None
akun_penerima = None



class atm:
        def __init__(self,root):
                self.root=root
                blank_space=" "
                self.root.title(130*blank_space+"ATM FTI 22")
                self.root.geometry("774x760+280+0")
                self.root.configure(background ='red')
#Frame    
                MainFrame= Frame(self.root,bd=20, width=784, height=700, relief=RIDGE)
                MainFrame.grid()
                
                TopFrame1= Frame(MainFrame,bd=5, width=740, height=300, relief=RIDGE)
                TopFrame1.grid(row=1,column=0,padx=12)

                TopFrame2= Frame(MainFrame,bd=5, width=600, height=300, relief=RIDGE)
                TopFrame2.grid(row=0,column=0,padx=8)
                
                TopFrame2Kiri= Frame(TopFrame2,bd=5, width=70, height=60, relief=RIDGE)
                TopFrame2Kiri.grid(row=0,column=0,padx=8)
                TopFrame2Tengah= Frame(TopFrame2,bd=10, width=320, height=320, relief=RIDGE)
                TopFrame2Tengah.grid(row=0,column=1,padx=15)
                TopFrame2Kanan= Frame(TopFrame2,bd=5, width=70, height=60, relief=RIDGE)
                TopFrame2Kanan.grid(row=0,column=2,padx=8)
                TopFrame2TengahBawah=Frame(TopFrame2,bd=0, width=100, height=5, relief=RIDGE)
                TopFrame2TengahBawah.grid(row=0,column=1)
                TopFrame2TengahBawah.place(x=260,y=200)
        
        #Fungsi Angka
                def angka_1():
                        angka1=1
                        self.textReceipt.insert(END,angka1)
                def angka_2():
                        angka2=2
                        self.textReceipt.insert(END,angka2)       
                def angka_3():
                        angka3=3
                        self.textReceipt.insert(END,angka3)
                def angka_4():
                        angka4=4
                        self.textReceipt.insert(END,angka4)
                def angka_5():
                        angka5=5
                        self.textReceipt.insert(END,angka5)
                def angka_6():
                        angka6=6
                        self.textReceipt.insert(END,angka6)
                def angka_7():
                        angka7=7
                        self.textReceipt.insert(END,angka7)
                def angka_8():
                        angka8=8
                        self.textReceipt.insert(END,angka8)
                def angka_9():
                        angka9=9
                        self.textReceipt.insert(END,angka9)
                def angka_0():
                        angka0=0
                        self.textReceipt.insert(END,angka0)
                def clear():
                        self.textReceipt.delete('1.0','end')             
                
                def cancel():
                        self.root.destroy()
                        return
# Definisi fungsi dari opsi
#Belum buat fungsi untuk input NIM            
# Samakan dengan video tutorial
                

                

                
                def MenuLain():
                        self.img_Widget=PhotoImage(file='FTI.png')
                        self.label=Label(TopFrame2Tengah,image=self.img_Widget)
                        self.label.place(x=0,y=0)
                        self.img_panah_Kiri=PhotoImage( file='lArrow.png')
                        self.btnArrowL1=Button(TopFrame2Kiri, width=80,height=30, state=NORMAL,image=self.img_panah_Kiri).grid(row=0,column=0,padx=5,pady=2) 
                        self.btnArrowL2=Button(TopFrame2Kiri, width=80,height=30, state=NORMAL,image=self.img_panah_Kiri,command=Transfer).grid(row=1,column=0,padx=5,pady=2)
                        self.btnArrowL3=Button(TopFrame2Kiri, width=80,height=30, state=NORMAL,image=self.img_panah_Kiri).grid(row=2,column=0,padx=5,pady=2)
                        self.img_panah_Kanan=PhotoImage( file='rArrow.png')
                        self.btnArrowR1=Button(TopFrame2Kanan, width=80,height=30, state=NORMAL,image=self.img_panah_Kanan).grid(row=0,column=0,padx=5,pady=2) 
                        self.btnArrowR2=Button(TopFrame2Kanan, width=80,height=30, state=NORMAL,image=self.img_panah_Kanan).grid(row=1,column=0,padx=5,pady=2)
                        self.btnArrowR3=Button(TopFrame2Kanan, width=80,height=30, state=NORMAL,image=self.img_panah_Kanan).grid(row=2,column=0,padx=5,pady=2)
                def Transfer():
                        self.img_Widget=PhotoImage(file='Transfer1.png')
                        self.label=Label(TopFrame2Tengah,image=self.img_Widget)
                        self.label.place(x=0,y=0)
                        TopFrame2TengahBawah1=Frame(TopFrame2,bd=0, width=100, height=5, relief=RIDGE)
                        TopFrame2TengahBawah1.grid(row=0,column=1)
                        TopFrame2TengahBawah1.place(x=260,y=250)
                        self.img_panah_Kiri=PhotoImage( file='lArrow.png')
                        self.btnArrowL1=Button(TopFrame2Kiri, width=80,height=30, state=NORMAL,image=self.img_panah_Kiri).grid(row=0,column=0,padx=5,pady=2) 
                        self.btnArrowL2=Button(TopFrame2Kiri, width=80,height=30, state=NORMAL,image=self.img_panah_Kiri,command=Transfer).grid(row=1,column=0,padx=5,pady=2)
                        self.btnArrowL3=Button(TopFrame2Kiri, width=80,height=30, state=NORMAL,image=self.img_panah_Kiri).grid(row=2,column=0,padx=5,pady=2)
                        self.img_panah_Kanan=PhotoImage( file='rArrow.png')
                        self.btnArrowR1=Button(TopFrame2Kanan, width=80,height=30, state=NORMAL,image=self.img_panah_Kanan).grid(row=0,column=0,padx=5,pady=2) 
                        self.btnArrowR2=Button(TopFrame2Kanan, width=80,height=30, state=NORMAL,image=self.img_panah_Kanan).grid(row=1,column=0,padx=5,pady=2)
                        self.btnArrowR3=Button(TopFrame2Kanan, width=80,height=30, state=NORMAL,image=self.img_panah_Kanan).grid(row=2,column=0,padx=5,pady=2)
                            
                def IsiPin():
                        self.img_Widget=PhotoImage(file='FTI (3).png')
                        self.label=Label(TopFrame2Tengah,image=self.img_Widget)
                        self.label.place(x=0,y=0)
                        self.textReceipt=Entry(TopFrame2TengahBawah,height=1,width=10,bd=0,font=('adirek serif semibold',12),fg='white')
                        self.textReceipt.grid(column=2,row=2)
                        self.textReceipt.configure(background='#162886')
                        
                def PIN_Confirm():        
                        global list_PIN
                        global akun
                        global PIN
                        PIN = str(self.textReceipt.get("1.0",'end-1c'))
                        
                        if PIN in list_PIN:
                                akun = list_PIN.index(PIN)
                                enter0=MenuLain
                                self.img_enter=PhotoImage(file='enter.png')
                                self.btn_enter=Button(TopFrame1,width=90,height=50,image=self.img_enter,state=NORMAL,command=enter0).grid(row=3,column=3,padx=5,pady=4)
                                self.textReceipt.delete('1.0','end')
                        else:
                                self.img_enter=PhotoImage(file='enter.png')
                                self.btn_enter=Button(TopFrame1,width=90,height=50,image=self.img_enter,state=NORMAL,command=cancel).grid(row=3,column=3,padx=5,pady=4)  


                
#Belum input dan pastikan pin
                  
                        

        #Widget awal
                self.img_Widget=PhotoImage(file='FTI (2).png')
                self.label=Label(TopFrame2Tengah,image=self.img_Widget)
                self.label.place(x=0,y=0)
                self.textReceipt=Text(TopFrame2TengahBawah,height=1,width=10,bd=0,font=('adirek serif semibold',12),fg='white')
                self.textReceipt.grid(column=2,row=2)
                self.textReceipt.configure(background='#162886')
                

                      
        # Tombol Kiri
                self.img_panah_Kiri=PhotoImage( file='lArrow.png')
                self.btnArrowL1=Button(TopFrame2Kiri, width=80,height=30, state=DISABLED,image=self.img_panah_Kiri).grid(row=0,column=0,padx=5,pady=2) 
                self.btnArrowL2=Button(TopFrame2Kiri, width=80,height=30, state=DISABLED,image=self.img_panah_Kiri).grid(row=1,column=0,padx=5,pady=2)
                self.btnArrowL3=Button(TopFrame2Kiri, width=80,height=30, state=DISABLED,image=self.img_panah_Kiri).grid(row=2,column=0,padx=5,pady=2)
        # Tombol Kanan
                self.img_panah_Kanan=PhotoImage( file='rArrow.png')
                self.btnArrowR1=Button(TopFrame2Kanan, width=80,height=30, state=DISABLED,image=self.img_panah_Kanan).grid(row=0,column=0,padx=5,pady=2) 
                self.btnArrowR2=Button(TopFrame2Kanan, width=80,height=30, state=DISABLED,image=self.img_panah_Kanan).grid(row=1,column=0,padx=5,pady=2)
                self.btnArrowR3=Button(TopFrame2Kanan, width=80,height=30, state=DISABLED,image=self.img_panah_Kanan).grid(row=2,column=0,padx=5,pady=2)       
        #Tombol PIN
                self.img1=PhotoImage(file='one.png')
                self.btn1=Button(TopFrame1,width=90,height=50,image=self.img1,command=angka_1).grid(row=1,column=0,padx=5,pady=4)
                self.img2=PhotoImage(file='two.png')
                self.btn2=Button(TopFrame1,width=90,height=50,image=self.img2,command=angka_2).grid(row=1,column=1,padx=5,pady=4)
                self.img3=PhotoImage(file='three.png')
                self.btn3=Button(TopFrame1,width=90,height=50,image=self.img3,command=angka_3).grid(row=1,column=2,padx=5,pady=4)
                self.img4=PhotoImage(file='four.png')
                self.btn4=Button(TopFrame1,width=90,height=50,image=self.img4,command=angka_4).grid(row=2,column=0,padx=5,pady=4)
                self.img5=PhotoImage(file='five.png')
                self.btn5=Button(TopFrame1,width=90,height=50,image=self.img5,command=angka_5).grid(row=2,column=1,padx=5,pady=4)
                self.img6=PhotoImage(file='six.png')
                self.btn6=Button(TopFrame1,width=90,height=50,image=self.img6,command=angka_6).grid(row=2,column=2,padx=5,pady=4)
                self.img7=PhotoImage(file='seven.png')
                self.btn7=Button(TopFrame1,width=90,height=50,image=self.img7,command=angka_7).grid(row=3,column=0,padx=5,pady=4)
                self.img8=PhotoImage(file='eight.png')
                self.btn8=Button(TopFrame1,width=90,height=50,image=self.img8,command=angka_8).grid(row=3,column=1,padx=5,pady=4)
                self.img9=PhotoImage(file='nine.png')
                self.btn9=Button(TopFrame1,width=90,height=50,image=self.img9,command=angka_9).grid(row=3,column=2,padx=5,pady=4)
                self.img0=PhotoImage(file='zero.png')
                self.btn0=Button(TopFrame1,width=90,height=50,image=self.img0,command=angka_0).grid(row=4,column=1,padx=5,pady=4)
                self.img_cancel=PhotoImage(file='cancel.png')
                self.btn_cancel=Button(TopFrame1,width=90,height=50,image=self.img_cancel,command=cancel).grid(row=1,column=3,padx=5,pady=4)
                self.img_enter=PhotoImage(file='enter.png')
                self.btn_enter=Button(TopFrame1,width=90,height=50,image=self.img_enter,state=NORMAL,command=PIN_Confirm).grid(row=3,column=3,padx=5,pady=4)
                self.img_clear=PhotoImage(file='clear.png')
                self.btn_clear=Button(TopFrame1,width=90,height=50,image=self.img_clear,command=clear).grid(row=2,column=3,padx=5,pady=4)
                self.img_empty=PhotoImage(file='empty.png')
                self.btn_empty=Button(TopFrame1,width=90,height=50,image=self.img_empty).grid(row=4,column=0,padx=5,pady=4)
                self.img_empty_2=PhotoImage(file='empty.png')
                self.btn_empty_2=Button(TopFrame1,width=90,height=50,image=self.img_empty_2).grid(row=4,column=2,padx=5,pady=4)
                self.img_empty=PhotoImage(file='empty.png')
                self.btn_empty=Button(TopFrame1,width=90,height=50,image=self.img_empty,command=IsiPin).grid(row=4,column=3,padx=5,pady=4)
                
if __name__=='__main__':
    root= Tk()
    application=atm(root)
    root.mainloop()
