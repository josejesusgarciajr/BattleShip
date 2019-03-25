from tkinter import *
from PIL import Image, ImageTk


class GUI_Board():
    def __init__(self):
        self.window = Tk()
        self.window.title("BattleShip")
        self.window.config(bg="black")
        self.window.geometry("1100x850")

        self.add_logo()

        # create canvas for ships to be placed
        # 4cbdff
        self.canvas = Canvas(self.window, width=1050, height=600, bg="black", highlightbackground="black")

        self.path0 = "../images/ship-569.png"
        self.load0 = Image.open(self.path0)
        self.load0 = self.load0.resize((1050,750), Image.ANTIALIAS)
        self.image0 = ImageTk.PhotoImage(self.load0)
        self.canvas.create_image(500, 400, image=self.image0)
        self.canvas.place(x=20, y=200)


        self.image_path1 = "../images/emptygrid.png"
        self.load1 = Image.open(self.image_path1)
        self.load1 = self.load1.resize((500, 500), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(self.load1)

        self.canvas.create_image(700, 300, image=self.image1)


        # Keeps track of each ship that would be moved
        self._drag_data = {"x": 0, "y": 0, "item": None}

        self.create_ships()



        self.window.bindtags("ButtonPress-1")

        self.canvas.tag_bind("ship", "<ButtonPress-1>", self.on_ship_press)
        self.canvas.tag_bind("ship", "<ButtonRelease-1>", self.on_ship_release)
        self.canvas.tag_bind("ship", "<B1-Motion>", self.on_ship_motion)

        self.window.mainloop()

    def add_logo(self):
        image_path2 = "../images/battleship-logo.jpg"
        load2 = Image.open(image_path2)
        self.render2 = ImageTk.PhotoImage(load2)
        img2 = Label(self.window, image=self.render2, bg=self.window['bg'])
        img2.place(x=250, y=0)

    def create_ships(self):
        self.path = "../images/"
        self.ship_images = ["aircraft carrier.png","battleship.png","cruiser.png","destroyer.png","submarine.png"]

        # List of ships stored to access them when figuring out which one is being moved
        self.ship_names = []

        i=0
        x=100
        y=100
        for ship in self.ship_images:
            self.image_path = self.path+ship
            self.load = Image.open(self.image_path)
            self.load = self.load.resize((50, 200), Image.ANTIALIAS)
            self.ship_names.insert(i, ImageTk.PhotoImage(self.load))
            self.canvas.create_image(x, y, image=self.ship_names.__getitem__(i), tags="ship")

            if y == 500 and x == 100:
                x += 130
                y = 50

            y+=200
            i+=1

    # Keeps track of the position when a particular ship is clicked
        #Track starts from item 2
    def on_ship_press(self, event):
        self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    # Keeps track of the position when a particular ship is released
    def on_ship_release(self, event):
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    # Keeps track of the motion of a particular ship
    def on_ship_motion(self, event):
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]

        self.canvas.move(self._drag_data["item"], delta_x, delta_y)

        # New position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

GUI_Board()