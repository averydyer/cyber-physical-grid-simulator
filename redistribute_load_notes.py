"""
Goal: redistribute loads to prevent overload if possible

- determine which substations are overloaded and which still have space
- determine which regions are connected to these substations, and if other
connected substations with space exist

if a substation is overloaded, do current_load - capacity to find total_overload.
reg_overload = total_overload / # of connected regions
count = 0

# GOES IN GRID CONTROLLER CLASS
for sub in self.substations:
    # if the substation is active and overloaded
    if sub.status and sub.check_overload():
        # finding connected regions of the substation
        connected_regions = []
        for region in self.regions:
            if sub in region.connected_substations:
            connected_regions.append(region)
        sub.redistribute(connected_regions)


# precondition: the substation we are performing on is overloaded
# connected_regions is all the regions connected to the substation
# postcondition: if possible, loads are redistributed and the 
# substation is no longer overloaded
# GOES IN SUBSTATION CLASS
def redistribute(self, connected_regions):
    total_overload = self.current_load - self.capacity
    added_load = 0

    while added_load != total_overload:
        for region in connected_regions:
            for sub in region.connected_substations:
                if sub.status and not sub.check_overload():
                    sub.add_load(1)
                    added_load += 1
                    if added_load == total_overload:
                        break

    self.current_load = self.capacity
    



while count != # of connected regions:
    for region in connected regions:
        count += redistribute()
for sub in self.connected_substations:
    # if substation is active and not overloaded
    if sub.status & not sub.check_overload():
        sub.add_load(reg_overload)
        return 1

"""
