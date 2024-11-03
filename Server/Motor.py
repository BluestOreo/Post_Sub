import math
from PCA9685 import PCA9685 # LED CONTROLLER I2C 
import time


class Motor:
    def __init__(self):
        self.pwm = PCA9685(0x40, debug=True)
        self.pwm.setPWMFreq(50)



    @staticmethod
    ## MAKING SURE THE DUTY CYCLE IS IN RANGE
    def duty_range(duty1, duty2, duty3, duty4):
        if duty1 > 4095:
            duty1 = 4095
        elif duty1 < -4095:
            duty1 = -4095

        if duty2 > 4095:
            duty2 = 4095
        elif duty2 < -4095:
            duty2 = -4095

        if duty3 > 4095:
            duty3 = 4095
        elif duty3 < -4095:
            duty3 = -4095

        if duty4 > 4095:
            duty4 = 4095
        elif duty4 < -4095:
            duty4 = -4095
        return duty1, duty2, duty3, duty4

    ##=============================================SET DUTY CYCLE AND DIRECTION FOR EACH WHEEL===============================================
    def left_Upper_Wheel(self, duty):
        if duty > 0: ## FORWARD
            self.pwm.setMotorPwm(5, 0) ##RESET DIRECTION 0
            self.pwm.setMotorPwm(6, duty) ## SET SPEED 1
        elif duty < 0: #BACKWARD
            self.pwm.setMotorPwm(5, 0) # RESET DIRECTION 1
            self.pwm.setMotorPwm(6, abs(duty)) # SET SPEED 0
        else: ## IF DUTY IS 0, SET BOTH DIRECTIONS TO maximum 
            self.pwm.setMotorPwm(5, 4095) #
            self.pwm.setMotorPwm(6, 4095)

    def left_Lower_Wheel(self, duty):
        if duty > 0:
            self.pwm.setMotorPwm(7, 0)
            self.pwm.setMotorPwm(8, duty)
        elif duty < 0:
            self.pwm.setMotorPwm(7, 0)
            self.pwm.setMotorPwm(8, abs(duty))
        else:
            self.pwm.setMotorPwm(7, 4095)
            self.pwm.setMotorPwm(8, 4095)

    def right_Upper_Wheel(self, duty): 
        if duty > 0:
            self.pwm.setMotorPwm(9, 0)
            self.pwm.setMotorPwm(10, duty)
        elif duty < 0:
            self.pwm.setMotorPwm(9, 0)
            self.pwm.setMotorPwm(10, abs(duty))
        else:
            self.pwm.setMotorPwm(9, 4095)
            self.pwm.setMotorPwm(10, 4095)

    def right_Lower_Wheel(self, duty):
        if duty > 0:
            self.pwm.setMotorPwm(11, 0)
            self.pwm.setMotorPwm(12, duty)
        elif duty < 0:
            self.pwm.setMotorPwm(11, 0)
            self.pwm.setMotorPwm(12, abs(duty))
        else:
            self.pwm.setMotorPwm(11, 4095)
            self.pwm.setMotorPwm(12, 4095)

    ##GROUP FUCNTION TO SET PWM
    def setMotorModel(self, duty1, duty2, duty3, duty4):
        duty1, duty2, duty3, duty4 = self.duty_range(duty1, duty2, duty3, duty4)
        self.left_Upper_Wheel(duty1)
        self.left_Lower_Wheel(duty2)
        self.right_Upper_Wheel(duty3)
        self.right_Lower_Wheel(duty4)



PWM = Motor()


def loop():
    PWM.setMotorModel(2000, 2000, 2000, 2000)  # Forward
    time.sleep(3)
    PWM.setMotorModel(-2000, -2000, -2000, -2000)  # Back
    time.sleep(3)
    PWM.setMotorModel(-500, -500, 2000, 2000)  # Left
    time.sleep(3)
    PWM.setMotorModel(2000, 2000, -500, -500)  # Right
    time.sleep(3)
    PWM.setMotorModel(0, 0, 0, 0)  # Stop


def destroy():
    PWM.setMotorModel(0, 0, 0, 0)


if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
