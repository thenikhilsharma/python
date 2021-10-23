class rocket:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
    
    def launch(self):
        return "%s has reached %s" %(self.name, self.distance)

class marsRover(rocket):
    def __init__(self, name, distance, maker):
        rocket.__init__(self, name, distance)
        self.maker = maker
    
    def get_maker (self):
        return "%s launched by %s" % (self.name, self.maker)
    
if __name__ == "__main__":
    x = rocket("simple rocket", "till stratosphere")
    y = marsRover("mars_rover", "till mars", "ISRO")
    print(x.launch())
    print(y.launch())
    print(y.get_maker())