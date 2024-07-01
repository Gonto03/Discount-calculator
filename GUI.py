import tkinter as tk
from PIL import Image, ImageTk

# GLOBAL VARIABLES
x_spacing = 12
y_spacing = 25
screen = tk.Tk()
screen.title("Calculadora de Descontos")
screen.geometry("800x500")
bg_image = ImageTk.PhotoImage(Image.open('C://Users\gapmd\workspace\Calculadora_de_descontos\current_code\panike.jpg'))


# Helper functions
def set_background(screen):
    background_label = tk.Label(screen, image=bg_image)
    background_label.place(relwidth=1, relheight=1)
    background_label.lower()

    
# Main setup of the app's events
set_background(screen)
str1 = tk.Label(text= "Preço original: ", fg = "white", bg= "black", font=("Calibri", 12))
str1.place(x=x_spacing, y=y_spacing)
str2 = tk.Label(text= "Novo preço: ", fg = "white", bg= "black", font=("Calibri", 12))
y_spacing += 40
str2.place(x=x_spacing, y=y_spacing)

# Start the Tkinter event loop
screen.mainloop()