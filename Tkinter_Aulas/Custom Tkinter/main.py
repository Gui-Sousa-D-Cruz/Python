import tkinter
import customtkinter
import keyboard

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x300")
        self.title("PROJETO RPG")
        self.minsize(300, 200)

        # create 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)
        
        self.bt1='ACT1'
        self.bt2='ACT2'
        self.bt3='Menu'
        self.bt4='Sair'
        
        self.label_1 = customtkinter.CTkLabel(master=self,text='Texto Principal')
        self.label_1.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")
        self.button_1 = customtkinter.CTkButton(master=self, width=100, height=50,text='Botão 1', command= self.btn1)
        self.button_1.grid(row=1, column=0, ipadx=20, padx=5, pady=5, sticky="ew")
        self.button_2 = customtkinter.CTkButton(master=self, width=100, height=50,text='Botão 2', command= self.btn2)
        self.button_2.grid(row=1, column=1, ipadx=20, padx=5, pady=5, sticky="ew")
        self.button_3 = customtkinter.CTkButton(master=self, width=100, height=50,text='Menu', command= self.btn3)
        self.button_3.grid(row=2, column=0, columnspan=2, ipadx=20, padx=5, sticky="ew")
       
        
        #espaçamento
        self.frame_1 = customtkinter.CTkLabel(master=self,text='')
        self.frame_1.grid(row=3, column=1,columnspan=1, sticky="ew")
        
        
        
    #          BOTAO UM
    def btn1(self):
        self.label_1.configure(text="O botão 1 foi pressionado")
        self.act = 1
        
    #          BOTAO DOIS
    def btn2(self):
        self.label_1.configure(text="O botão 2 foi pressionado")
        self. act = 2
        
    #          MENU     
    def btn3(self):
        self.label_1.configure(text="MENU")      
        
    

    

if __name__ == "__main__":
    app = App()
    app.mainloop()
    


