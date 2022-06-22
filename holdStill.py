import libhousy
#You can define helper functions here, make sure to but them *above* the main function
first = True
def main(robot: libhousy.robot):
    global first
    if first:
        robot.rDriveEncoder.ReSet()
        robot.lDriveEncoder.ReSet()
        first = False

    if robot.rDriveEncoder.Get() >4:
        robot.rDrive.Set(-.5)
    elif robot.rDriveEncoder.Get() <-4:
       robot.rDrive.Set(.5) 
    else:
       robot.rDrive.Set(0)

    if robot.lDriveEncoder.Get() > 4:
        robot.lDrive.Set(-.5)
    elif robot.lDriveEncoder.Get() < -4:
        robot.lDrive.Set(.5)
    else:
        robot.lDrive.Set(0)

    return libhousy.DONE
    
    
