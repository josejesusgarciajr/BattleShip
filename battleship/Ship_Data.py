class Ship_Data:
    def __init__(self, id, name, top_x, top_y):
        self.id = id
        self.name = name
        self.top_x = top_x
        self.top_y = top_y

        print("Ship added with id ", self.id, " ", self.name, " ", self.top_x, " ", self.top_y)