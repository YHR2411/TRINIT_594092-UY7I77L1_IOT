from time import sleep

# acceleration value along x-axis from sensor
a1 = float(input("Enter the value of acceleration in the multiples of g at t=0.0 sec: "))
a2 = float(input("Enter the value of acceleration in the multiples of g at t=0.1 sec: "))
# Distance values from LiDARs
d1 = float(input("Enter the value of distance recorded in the left LiDAR"))
d2 = float(input("Enter the value of distance recorded in the center LiDAR"))
d3 = float(input("Enter the value of distance recorded in the right LiDAR"))

#a1 = 0.132 # a in terms of g at t = 0.0
#a2 = 0.128 # a in terms of g at t = 0.0

g = 9.8
a1 = a1*g
a2 = a2*g

def acceleration():
    if a1 == 0:
        break 
        # No Acceleration
    elif a1 < 1.4705:
        print("You are accelerating too much. Please go easy with the gas (accelerator)")
    else:
        print("Your acceleration is in the limit for the fuel consumption to be minimum")
    return(a1,a2)

def speed():
    speed = (a2-a1)/0.1
    speed = (speed*3600)/1000
    if speed>=85 and speed<=95:
        if speed>=85 and speed<88:
            print("You are going a bit slower than ideal speed. Consider speeding up and maintaining a speed of about 90Kmph")
        if speed<=95 and speed>92:
            sendWarning()
            print("You are going a bit faster than ideal speed. Consider slowing down and maintaining a speed of about 90Kmph")
        else:
            print("You are maintaining the correct speed to ensure low fuel consumption")
    if speed<85:
        print("Speed up to the ideal speed of 90Kmph for fuel economy")
    if speed>95:
        print("Slow down to the ideal speed of  90Kmph for fuel economy")
    return(speed)

def idling():
    if a1 == 0 and speed == 0:
        sleep(30)
        if speed!=0:
            idling = int(0)
            break
        else:
            print("Your vehicle engine is idling. This consumes fuel. please turn off the vehicle to ensure fuel economy")
            idling - int(1)
    return(idling)
    
def braking():
    return()

def distance():
    d = 10 # Distance Threshold for warning
    if d1>d and d2>d and d3>d:
        print("No obstruction ahead. Go Straight!!")
    if d1<d:
        if d2>d:
            print("Move slightly towards your right to avoid obstacle on the left")
        if d2<d:
            if d3>d:
                print("slow down a bit and turn right to avoid colission with the obstacle on the left")
            if d3<d:
                print("Hit the breaks!! STOP the vehicle!! Huge Obstacle ahead")

    if d2<d:
            if d1>d:
                print("Move slightly towards your left to avoid obstacle on the right")
            if d1<d:
                if d3>d:
                    print("slow down a bit and turn left to avoid colission with the obstacle on the right")
                if d3<d:
                    print("Hit the breaks!! STOP the vehicle!! Huge Obstacle ahead")

