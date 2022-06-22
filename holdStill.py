import libhousy
#You can define helper functions here, make sure to but them *above* the main function
first = True
def main(robot: libhousy.robot):
    if first:
        robot.rDriveEncoder.Reset()
        robot.lDriveEncoder.Reset()
        first = False

    if robot.rDriveEncoder.Get() >4:
        robot.rDrive.set(-.5)
    elif robot.rDriveEncoder.Get() <-4:
       robot.rDrive.set(.5) 
    else:
       robot.rDrive.set(0)

    if robot.lDriveEncoder.Get() > 4:
        robot.lDrive.set(-.5)
    elif robot.lDriveEncoder.Get() < -4:
        robot.lDrive.set(.5)
    else:
        robot.lDrive.set(0)

    return libhousy.DONE
    
    
