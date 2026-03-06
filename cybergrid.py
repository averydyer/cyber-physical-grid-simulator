

class Substation:
    # default constructor
    # substation name, capacity, current load, connected regions, and status set by user
    # if user does not set values, default name = "Sub0", capacity = 150, current load = 0, status = True
    def __init__(self, name="Sub0", capacity=150, current_load=0, status=True):
        self.name = name
        self.capacity = capacity
        self.current_load = current_load
        self.status = status

    # adds load amount entered by user to current load
    def add_load(self, amount):
        # if the substation is active
        if self.status:
            self.current_load += amount

    # returns true if overload (current load > capacity)
    def check_overload(self):
        return self.current_load > self.capacity


class Region:
    # default Region object: name = "Reg0", demand = 50, no connected substations
    def __init__(self, name="Reg0", demand=50, connected_substations=None):
        self.name = name
        self.demand = demand
        self.connected_substations = connected_substations if connected_substations is not None else []

    def distribute_load(self):
        # guard against having no connected substations
        if not self.connected_substations:
            print("No substations connected to this region\n")
            return
        # equal distribution of load between connected substations
        load = self.demand / len(self.connected_substations)
        # add load amount to each substation
        for sub in self.connected_substations:
            sub.add_load(load)


# Substations/Regions Test
# initializing substations
S1 = Substation()
S2 = Substation("Sub2", 200, 50, True)
S3 = Substation("Sub3", 300, 100, True)
# initializing regions
city = Region("City", 80, [S1, S2])
data_center = Region("Data Center", 120, [S1, S2])
water = Region("Water Treatment", 40, [S1, S3])
neighborhood = Region("Neighborhood", 25, [S3])

# distributing loads
city.distribute_load()
data_center.distribute_load()
water.distribute_load()
neighborhood.distribute_load()
# printing current loads of substations
print(S1.current_load)
print(S2.current_load)
print(S3.current_load)
