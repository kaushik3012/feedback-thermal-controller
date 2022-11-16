import params

#Proportional Control and Saturation
class PCS:      
    def __init__(self):
        self.kp = params.kp
    def __call__(self, error):
        u = self.kp * error 
        if(u > 1):
            u=1
        elif(u < -1):
            u=-1
        return u