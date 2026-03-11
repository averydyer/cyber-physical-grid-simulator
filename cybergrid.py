

class Substation:
    # substation name, capacity, current load, connected regions, and status set by user
    # default values provided if user does not set data
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

    # prints substation's load data
    def display_sub(self):
        # if status is false, substation is offline
        if not self.status:
            print(
                f"{self.name:6} {"[OFFLINE]":22} {f"0/{self.capacity}":7} MW")
            return
        # check for overloaded substation
        if self.check_overload():
            print(
                f"{self.name:6} {"[OVERLOADED]":22} {f"{self.current_load:.0f}/{self.capacity}":7} MW")
            return
        bar_len = 20
        # calculates how much of the capacity is being utilized (>1 = overloaded)
        load_ratio = self.current_load / self.capacity
        # how many sections of the bar should be filled based on load ratio
        filled = int(load_ratio * bar_len)
        # creating bar string
        bar = "█" * filled + "░" * (bar_len - filled)
        # :6 = print name using 6 characters of space
        print(
            f"{self.name:6} [{bar}] {f"{self.current_load:.0f}/{self.capacity}":7} MW")


class Region:
    # default Region object: name = "Reg0", demand = 50, no connected substations
    def __init__(self, name="Reg0", demand=50, connected_substations=None):
        self.name = name
        self.demand = demand
        self.connected_substations = connected_substations if connected_substations is not None else []

    def distribute_load(self):
        # guard against having no connected substations
        if not self.connected_substations:
            print(f"{self.name} has no connected substations\n")
            return
        active_subs = 0
        for sub in self.connected_substations:
            # if the substation is online
            if sub.status:
                active_subs += 1
        if active_subs == 0:
            print(f"All substations connected to {self.name} are offline")
        else:
            # equal distribution of load between connected, active substations
            load = self.demand / active_subs
            # add load amount to each substation
            for sub in self.connected_substations:
                if sub.status:
                    sub.add_load(load)


class GridController:
    # initialized with a list of all substations and list of all regions
    def __init__(self, substations=None, regions=None):
        self.substations = substations if substations is not None else []
        self.regions = regions if regions is not None else []

    # sets current load for all substations to 0
    def reset_loads(self):
        for sub in self.substations:
            sub.current_load = 0

    # distributes load for every region
    def distribute_loads(self):
        for reg in self.regions:
            reg.distribute_load()

    # runs the entire system (reset and distribute loads, check overload, display grid)
    def simulation_step(self):
        self.reset_loads()
        self.distribute_loads()
        self.display_grid()

    # prints out all substations in the grid and their status
    def display_grid(self):
        print("\nGrid Status")
        print("-----------------------------------------")
        for sub in self.substations:
            sub.display_sub()
        print("-----------------------------------------\n")


S1 = Substation("S1", 100, 50, True)
S2 = Substation("S2", 200, 0, True)
S3 = Substation("S3", 150, 150, True)

city = Region("City", 100, [S1, S2])
neighborhood = Region("Neighborhood", 50, [S3])
data_center = Region("Data Center", 100, [S1, S2])
water = Region("Water Treatment Plant", 80, [S3])

grid = GridController([S1, S2, S3], [city, neighborhood, data_center, water])
grid.simulation_step()

# when S2 goes offline, S1 is overloaded
S2.status = False
grid.simulation_step()
