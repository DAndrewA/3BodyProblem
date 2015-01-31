from tkinter import *
import math
import time

app = Tk()
c = Canvas(app,height="750",width="750")
c.pack()

# Defines the body object. It will store the position and velocity vector for the body, aswell as its mass and the ability to calculate specific values.
class body:
    # This is the function that runs when the object is instantiated.
    def __init__(self,startPosition,startVelocity,mass,id):
        self.position = startPosition
        self.velocity = startVelocity
        self.mass = mass
        self.id = id

# Calculates the distance between two points. This will be used for getting the distance from a body to the COG.
def calcDistance(pos1,pos2):
    distanceV = []
    # Takes the biggest smallest one from the biggest one
    if pos1[0] > pos2[0]:
        distanceV.append(pos1[0] - pos2[0])
    else:
        distanceV.append(pos2[0] - pos1[0])

    if pos1[1] > pos2[1]:
        distanceV.append(pos1[1] - pos2[1])
    else:
        distanceV.append(pos2[1] - pos1[1])

    distance = math.sqrt(distanceV[0]**2 + distanceV[1]**2)
    return distance

# Instantiating the objects and setting their positions and velocities
body1 = body([350,150],[-10,-30],200,0)
body2 = body([150,250],[30,10],100,1)
body3 = body([350,350],[-20,40],200,2)
body4 = body([500,350],[0,0],2000,3)

# Drawing the bodies onto the canvas
c.create_oval(body1.position[0]-5,body1.position[1]-5,body1.position[0]+5,body1.position[1]+5,tag="body1Circle",fill="#FFFF00")
c.create_oval(body2.position[0]-5,body2.position[1]-5,body2.position[0]+5,body2.position[1]+5,tag="body2Circle",fill="#0000FF")
c.create_oval(body3.position[0]-5,body3.position[1]-5,body3.position[0]+5,body3.position[1]+5,tag="body3Circle",fill="#00FF00")
c.create_oval(body4.position[0]-5,body4.position[1]-5,body4.position[0]+5,body4.position[1]+5,tag="body4Circle",fill="#FF0000")

#global lastFrame
#lastFrame = time.time()
gravityConstant = 500

# Makes the program run forever (or until it is closed)
while True:
    # Updates the bodies variable with the current objects
    bodies = [body1,body2,body3,body4]
    # Gets the time frame to multiply by and sets the frame values
    deltaTime =  0.0005
    # Goes through all bodies
    for i in bodies:
        # Calculates the accelaration for all of the bodies before moving them
        for x in bodies:
            if i.id != x.id:
                COG = x.position
                # Force = G * ((M1*M2)/distance^2)
                F = gravityConstant*((i.mass*x.mass)/(calcDistance(COG,i.position)**2))
                # Break down force into x and y components
                        # THE INTERNET IS A REALLY USEFULL THING
                # Calculate angle theta with equation in equation sheet
                deltaX = COG[0] - i.position[0]
                deltaY = COG[1] - i.position[1]
                thetaRad = math.atan2(deltaX,deltaY)
                # Using trig.
                Fx = math.sin(thetaRad)*F
                Fy = math.cos(thetaRad)*F
                # Calculating x and y accelaration
                Ax = Fx/i.mass
                Ay = Fy/i.mass
                # Calculate final velocity vector by using v=u+at
                i.velocity[0] += Ax*deltaTime
                i.velocity[1] += Ay*deltaTime

    # Moving all of the bodies after calculations
    for i in range(len(bodies)):
        # Moves the canvas object and the bodies coordinates
        c.move("body" + str(i + 1) + "Circle",bodies[i].velocity[0]*deltaTime,bodies[i].velocity[1]*deltaTime)
        bodies[i].position = [bodies[i].position[0] + bodies[i].velocity[0]*deltaTime,
                                        bodies[i].position[1] + bodies[i].velocity[1]*deltaTime]

    c.update()
    #time.sleep(2)


mainloop()
