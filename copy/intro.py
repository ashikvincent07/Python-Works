from copy import copy
from copy import deepcopy

ashik_fav_vehicles = [["aerox", "burgman"], ["speed 400", "scram 411"], ["corolla", "verna"]]
# abhi_fav_vehicles = copy(ashik_fav_vehicles) # creates only outer object copy

abhi_fav_vehicles = deepcopy(ashik_fav_vehicles) # createes both outer and inner object

abhi_fav_vehicles[0][0] = (["ola", "qube"])

print(ashik_fav_vehicles)

