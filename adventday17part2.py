#input data- read files


datadic = {"x_min" : 56, "x_max": 76, "y_min": -162, "y_max": -134}
testdatadic = {"x_min" : 20, "x_max": 30, "y_min": -10, "y_max": -5}


# -- import timing,
import datetime
start_time = datetime.datetime.now()


#---------what data am i testing----------
data= datadic

#-------------
launch_velocity= set()

def positions_calc(target_area):
    for x in range(target_area["x_max"]+1 ):
        for y in range (target_area["y_min"] , 200):
            x_velocity= x
            y_velocity = y
            x_position= 0
            y_position=0
            while x_position <= target_area["x_max"] and y_position >= target_area["y_min"]:
                x_position += x_velocity
                y_position += y_velocity
                if x_velocity > 0:
                    x_velocity -= 1
                y_velocity -= 1
                if x_position >= target_area["x_min"] and y_position <= target_area["y_max"] and x_position <= target_area["x_max"] and y_position >= target_area["y_min"]:
                    launch_velocity.add((x,y))


positions_calc(data)

print("viable launch velocities:", launch_velocity, "\n total viable launch velocities:", len(launch_velocity))


#find maximum Y launch velocity:
'''
y_launch_velocities= [y[1] for y in launch_velocity]

print(" max viable Y hight launch velocities:", max(y_launch_velocities))

def maximum_height_finder(y_launch_velocity):
    y_heights= []
    y_velocity = y_launch_velocity
    y_position=0
    while y_position >= 0:
        y_heights.append(y_position)
        y_position += y_velocity
        y_velocity -= 1
    print("maximum height:", max(y_heights))

maximum_height_finder(max(y_launch_velocities))
'''

# timing
end_time = datetime.datetime.now()
print("total time: ", end_time - start_time)