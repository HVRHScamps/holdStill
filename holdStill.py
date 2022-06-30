# inclue code to help us talk to the robot
import libhousy

def main(robot: libhousy.robot):
    # Here is where your recurring code will go
    if robot.lDriveEncoder.Get() >2:
        robot.lDrive.Set(-0.25)
        
    elif robot.lDriveEncoder.Get() <-2:
        robot.lDrive.Set(0.25)
        
    else: 
        robot.lDrive.Set(0)

    if robot.rDriveEncoder.Get() >2:
        robot.rDrive.Set(-0.25)

    elif robot.rDriveEncoder.Get() <-2:
        robot.rDrive.Set(0)
    else:
        robot.rDrive.Set(0)
    
    # After everything is done, we tell the main program to stop us
    #return libhousy.DONE
