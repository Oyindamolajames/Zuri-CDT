import math
class TimeDurationModule:
    """A class to simulate time duration module"""
    def __init__(self):
        self.sim_time = 70

class RouteObstructionDetector:
    """A module to detect obstruction and type"""
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b
        self.speed = 0.7
        self.distance = self.distance()
        self.exp_time = self.distance / self.speed
        self.obs_time = TimeDurationModule().sim_time

    def distance(self):
         #Radius of the Earth in miles
         earth_radius = 3958.8

         # Extracting latitude and longitude from coordinates
         lat1, lon1 = self.point_a
         lat2, lon2 = self.point_b

         # Converting degrees to radians
         lat1 = math.radians(lat1)
         lon1 = math.radians(lon1)
         lat2 = math.radians(lat2)
         lon2 = math.radians(lon2)

         # Haversine formula
         dlat = lat2 - lat1
         dlon = lon2 - lon1
         a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
         c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
         distance = earth_radius * c

         return distance

    def check_result(self):
        """A method to check result whether the rock is penetrable or not"""
        if (self.obs_time - self.exp_time) >= 60:
            return True
        else:
            return False

# create the Obstruction object and usee the check_result method to determine the result
y = RouteObstructionDetector(point_a = [53.5872,-2.4138], point_b = [53.474,-2.2388])
print(y.check_result())