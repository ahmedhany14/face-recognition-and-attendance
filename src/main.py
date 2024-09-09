# Importing the necessary modules

# Importing the tkinter module for the GUI
import tkinter as tk

# Importing the interface module
import interface as itf

# Importing the OpenCV module
import cv2

# Importing the PIL module
from PIL import Image, ImageTk


class Application:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My First App")
        self.root.geometry("1050x600")

        # Creating the buttons

        # Login button, where the command is the login function, will be implemented later
        self.login_button = itf.get_button(self.root, "login", "green", self.login)

        # Customizing the login button
        self.login_button.place(x=750, y=300)

        # Register button, where the command is the register function, will be implemented later
        self.register_button = itf.get_button(
            self.root, "register new user", "gray", self.register, fg="black"
        )
        self.register_button.place(x=750, y=400)

        # Creating web cam image label
        self.webcam_label = itf.get_img_label(self.root)
        self.webcam_label.place(x=10, y=0, width=720, height=550)

        # Adding webcam image

        self.webcam(self.webcam_label)  # This function will be implemented later
        
    # -----------------------------------------------------------------------------------------------
    def webcam(self, label):
        if "cap" not in self.__dict__:
            self.cap = cv2.VideoCapture(0)

        self._label = label
        self.webcam_preview()
        print("Webcam")

    def webcam_preview(self):

        ret, frame = self.cap.read()
        self.most_rescent_capture = frame

        image_rgb = cv2.cvtColor(self.most_rescent_capture, cv2.COLOR_BGR2RGB)

        self.most_rescent_capture_pil = Image.fromarray(image_rgb)
        imgtk = ImageTk.PhotoImage(image=self.most_rescent_capture_pil)
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)

        self._label.after(20, self.webcam_preview)

    # -----------------------------------------------------------------------------------------------
    def login(self):
        # This function will be implemented later
        print("Login")


    # -----------------------------------------------------------------------------------------------
    def register(self):
        # This function will be implemented later
        print("Register")

    # -----------------------------------------------------------------------------------------------
    def start_app(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Application()
    app.start_app()
