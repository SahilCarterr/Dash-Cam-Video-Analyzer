import math

import math

def findpoints(lat, lon):
    radius = 0.15
    N = 50 
    circlePoints = []
    for k in range(N):
        angle = math.pi*2*k/N
        dx = radius*math.cos(angle)
        dy = radius*math.sin(angle)
        point = [0, 0]
        point[0]= lat + (180/math.pi)*(dy/6371) # Earth Radius
        point[1]= lon + (180/math.pi)*(dx/6371)/math.cos(lon*math.pi/180) # Earth Radius
        circlePoints.append(point)
    return circlePoints


points = findpoints(28.3671055, 77.3176535)
# for point in points:
#     print(f"{point['lat']},{point['lon']}")
# Example coordinates (New York City)
for point in points:
    print(point[0])

