

class Substation:
    
    # default constructor
    # substation is active with capacity, current load, and connected regions set by user
    # if user does not set values, default capacity = 150, current load = 0, connected regions = []
    def __init__(self, capacity = 150, current_load = 0, connected_regions = None):
        self.capacity = capacity
        self.current_load = current_load
        self.status = True
        self.connected_regions = connected_regions if connected_regions is not None else []

    # adds load amount entered by user to current load
    def add_load(self, amount):
        # if the substation is active
        if self.status:
            self.current_load = self.current_load + amount

    # returns true if overload (current load > capacity)
    def check_overload(self):
        return self.current_load > self.capacity



# creates a new active substation called S1 with capacity = 150, current load = 0, connected regions = []
S1 = Substation()
# creates a new active substaion called S2 with capacity = 200, current load = 50, connected regions = ["City, Data center"]
S2 = Substation(200, 50, ["City", "Data center"])

# adds 50 to current load in S2
S2.add_load(50)
# checks if S2 is overloaded
overloaded = S2.check_overload