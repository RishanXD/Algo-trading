from tkinter import messagebox
from customtkinter import *  # type: ignore
from PIL import Image, ImageTk
def get_enctocken():



    image=Image.open("side-img.png")
    app=CTk()
    app.geometry("800x600")
    app._set_appearance_mode("dark")
    app.title("Insert Enctoken ")
    app.resizable(width=False,height=False)
    left_frame=CTkFrame(master=app,width=400, height=600)
    left_frame.grid(row=0, column=0, sticky="nsew")
    right_frame = CTkFrame(app, width=400, height=600)
    right_frame.grid(row=0, column=1, sticky="nsew")




    label=CTkLabel(master=app,
                text="Enter the enctoken: ",
                font=("Chiller",35),
                bg_color="transparent",
                fg_color="transparent",
                )


    entry=CTkEntry(master=app,
                width=325,
                height=50,
                placeholder_text="Insert Enctoken here",
                font=("Aerial",15)
                )
    enctoken_var = StringVar()

    def get_data_from_input_box():
        enctoken_var.set(entry.get())
        app.destroy()
        app.quit()


    btn=CTkButton(master=app,
                text="Confirm",
                hover_color="Grey",
                corner_radius=23,
                command=get_data_from_input_box
                #   background_corner_colors=['transparent', 'transparent', 'transparent', 'transparent']
                )

    resized_image = image.resize((400, 600), Image.ANTIALIAS)   # type: ignore
    photo_image = ImageTk.PhotoImage(resized_image)

    image_label = CTkLabel(left_frame,text=" ", image=photo_image)#type:ignore
    image_label.pack(fill="both", expand=True)

    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)
    app.grid_rowconfigure(0, weight=1)

    label.place(relx=0.55,rely=0.4,anchor="w")
    entry.place(relx=0.55,rely=0.5,anchor="w")
    btn.place(relx=0.55,rely=0.6,anchor="w")




    app.mainloop()

    return enctoken_var.get().strip()
def errorbox(msg):
    app=CTk()
    app.geometry("800x600")
    app._set_appearance_mode("dark")
    messagebox.showerror(title="Error",message=msg)





