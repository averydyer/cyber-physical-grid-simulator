

class Substation:
    # substation name, capacity, current load, and status set by user
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
                f"{self.name:6} {'[OFFLINE]':22} {f"0/{self.capacity}":7} MW")
            return
        # check for overloaded substation
        if self.check_overload():
            print(
                f"{self.name:6} {'[OVERLOADED]':22} {f"{self.current_load:.0f}/{self.capacity}":7} MW")
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
    def __init__(self, name="Reg0", demand=50, connected_substations=None, priority=5):
        self.name = name
        self.demand = demand
        self.connected_substations = connected_substations if connected_substations is not None else []
        self.priority = priority

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
            print(
                f"WARNING: all substations connected to {self.name} are offline")
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
        print("\n BEFORE REDISTRIBUTION:")
        self.display_grid()
        # try to redistribute if a substation is overloaded
        for sub in self.substations:
            if sub.check_overload():
                self.redistribute(sub)
        print("\n AFTER REDISTRIBUTION:")

    # runs the entire system (reset and distribute loads, check overload, display grid)
    def simulation_step(self):
        self.reset_loads()
        self.distribute_loads()
        self.display_grid()
        # if a substation is overloaded, shut it down
        for sub in self.substations:
            if sub.check_overload():
                self.overload_shutdown()

    # prints out all substations in the grid and their status
    def display_grid(self):
        print("\nGrid Status")
        print("-----------------------------------------")
        for sub in self.substations:
            sub.display_sub()
        print("-----------------------------------------\n")

    # shuts down overloaded substations, runs another simulation step
    def overload_shutdown(self):
        for sub in self.substations:
            # if the substation is overloaded
            if sub.check_overload():
                sub.status = False
                print(
                    f"WARNING: {sub.name} is overloaded and is being shut down")
        self.simulation_step()

    # "attacks" the named substation by taking it offline
    def attack_substation(self, name):
        for sub in self.substations:
            if sub.name == name:
                sub.status = False
                print(f"WARNING: cyber attack on {sub.name}")

    # attempts to redistribute load to prevent overload
    def redistribute(self, oSub):
        # overload amount
        overload = oSub.current_load - oSub.capacity
        connected_regions = []
        available_subs = set()
        # find all regions connected to the overloaded substation
        for reg in self.regions:
            if oSub in reg.connected_substations:
                connected_regions.append(reg)
        # find all available substations to transfer load to
        for reg in connected_regions:
            for sub in reg.connected_substations:
                # an available substation is active, is not the overloaded substation, and has load space
                if sub is not oSub and sub.status and not sub.check_overload() and (sub.capacity - sub.current_load > 0):
                    available_subs.add(sub)
        for sub in available_subs:
            # load space is how much more load the substation could take
            load_space = sub.capacity - sub.current_load
            # finding the limiting factor (overload amount or load space)
            transfer = min(overload, load_space)
            oSub.current_load -= transfer
            overload -= transfer
            sub.current_load += transfer
            # if overload is 0, the substation is no longer overloaded
            if overload == 0:
                break


S1 = Substation("S1", 200, 50, True)
S2 = Substation("S2", 150, 0, True)
S3 = Substation("S3", 100, 150, True)
# priority is the last argument given and is a number from 1-5
# with 1 being highest priority and 5 being lowest priority
city = Region("City", 100, [S1, S2], 2)
neighborhood = Region("Neighborhood", 50, [S1, S3], 5)
data_center = Region("Data Center", 150, [S1, S2], 4)
water = Region("Water Treatment Plant", 80, [S2, S3], 1)


grid = GridController([S1, S2, S3], [city, neighborhood, data_center, water])
grid.simulation_step()

# implement priority function
