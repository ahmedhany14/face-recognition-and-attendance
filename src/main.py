# Importing the necessary modules

# Importing the tkinter module for the GUI
import tkinter as tk

# Importing the interface module
import interface as itf

# Importing the OpenCV module
import cv2

# Importing the PIL module
from PIL import Image, ImageTk

import os


import face_recognition


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

        # creating the login window

        self.login_window = tk.Toplevel(self.root)
        self.login_window.title("login")
        self.login_window.geometry("1050x600+120+350")

        # Creating web cam image label
        self.webcam_label = itf.get_img_label(self.login_window)
        self.webcam_label.place(x=10, y=0, width=720, height=550)

        # Adding webcam image
        self.add_to_label(self.webcam_label)

        self.accept_button = itf.get_button(
            self.login_window,
            "Accept",
            "green",
            self.accept_login,
            fg="black",
        )
        self.accept_button.place(x=750, y=300)

        self.try_again_button = itf.get_button(
            self.login_window, "Try Again", "red", self.try_again_login, fg="black"
        )
        self.try_again_button.place(x=750, y=400)

    def try_again_login(self):
        path = "/home/hany_jr/Ai/Data sets/FaceRecog/RecProjectDB/unknown"
        os.remove(os.path.join(path, "unknown.jpg"))

        self.login_window.destroy()

    def accept_login(self):
        # Check if the person is a member or not
        path = "/home/hany_jr/Ai/Data sets/FaceRecog/RecProjectDB/unknown"
        cv2.imwrite(os.path.join(path, "unknown.jpg"), self.photo)

        results = self.predict()

        self.new_window_login = tk.Toplevel(self.login_window)
        self.new_window_login.title("New Member")
        self.new_window_login.geometry("400x300")

        if results != "Unknown":
            new_label = itf.get_text_label(self.new_window_login, f"Welcome {results}")
            new_label.place(x=50, y=50)

        else:
            new_label = itf.get_text_label(self.new_window_login, f"Unknown User")
            new_label.place(x=50, y=50)

        exit_button = itf.get_button(
            self.new_window_login, "Exit", "red", self.exit_login
        )
        exit_button.place(x=150, y=150)

    def predict(self):

        train_image_path = "//home/hany_jr/Ai/Data sets/FaceRecog/RecProjectDB/known"
        train_data = os.listdir(train_image_path)

        test_image_path = "/home/hany_jr/Ai/Data sets/FaceRecog/RecProjectDB/unknown"
        test_data = os.listdir(test_image_path)

        print(test_data)
        print(train_data)

        for img in test_data:
            print(img)
            test_image = face_recognition.load_image_file(test_image_path + "/" + img)
            test_face_encoding = face_recognition.face_encodings(test_image)
            if len(test_face_encoding) == 0:
                return "Unknown"
            test_face_encoding = test_face_encoding[0]
            for img2 in train_data:
                train_image = face_recognition.load_image_file(
                    train_image_path + "/" + img2
                )
                print("ssss")
                train_face_encoding = face_recognition.face_encodings(train_image)[0]

                results = face_recognition.compare_faces(
                    [test_face_encoding], train_face_encoding
                )
                if results[0]:
                    return str(img2).split(".")[0]

        return "Unknown"

    def exit_login(self):
        # remove the unknown image
        path = "/home/hany_jr/Ai/Data sets/FaceRecog/RecProjectDB/unknown"
        os.remove(os.path.join(path, "unknown.jpg"))
        self.new_window_login.destroy()
        self.login_window.destroy()

    # -----------------------------------------------------------------------------------------------
    def register(self):
        # This function will be implemented later
        print("Register")

        # creating the register window

        self.register_window = tk.Toplevel(self.root)
        self.register_window.title("Register")
        self.register_window.geometry("1050x600+120+350")

        # Creating the buttons

        self.accept_button = itf.get_button(
            self.register_window,
            "Accept",
            "green",
            self.accept,
            fg="black",
        )
        self.accept_button.place(x=750, y=300)

        self.try_again_button = itf.get_button(
            self.register_window, "Try Again", "red", self.try_again, fg="black"
        )
        self.try_again_button.place(x=750, y=400)

        # Creating web cam image label
        self.webcam_label = itf.get_img_label(self.register_window)
        self.webcam_label.place(x=10, y=0, width=720, height=550)

        # Adding webcam image
        self.add_to_label(self.webcam_label)

        # Creating the name label
        self.name_label = itf.get_text_label(self.register_window, "Name:")
        self.name_label.place(x=750, y=100)
        self.text_label = itf.get_entry_text(self.register_window)
        self.text_label.place(x=750, y=130)

    def accept(self):
        name = self.text_label.get("1.0", "end-1c")
        if name == "":
            name = "Unknown"

        # adding the new member to the dictionary of members
        path = "/home/hany_jr/Ai/Data sets/FaceRecog/RecProjectDB/known"
        cv2.imwrite(os.path.join(path, f"{name}.jpg"), self.photo)

        self.new_window = tk.Toplevel(self.register_window)
        self.new_window.title("New Member")
        self.new_window.geometry("400x300")
        new_label = itf.get_text_label(self.new_window, f"New member {name} added")
        new_label.place(x=50, y=50)
        exit_button = itf.get_button(self.new_window, "Exit", "red", self.exit)
        exit_button.place(x=150, y=150)

    def exit(self):
        self.new_window.destroy()
        self.register_window.destroy()

    def try_again(self):
        self.register_window.destroy()

    def add_to_label(self, label):

        # Take a picture, and store it in the label to be a new photo in the model, or as a new member
        imgtk = ImageTk.PhotoImage(image=self.most_rescent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        self.photo = self.most_rescent_capture.copy()

    # -----------------------------------------------------------------------------------------------
    def start_app(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Application()
    app.start_app()
