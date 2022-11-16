import params

#Class for Pulse Width Modulation
class PWM :
    def __init__(self, fhigh_curr, flow_curr):
        self.fmin = fhigh_curr
        self.fmax = flow_curr
    def __call__(self, u):

        fu = self.fmin + (self.fmax-self.fmin)((u+1)/2)
        f_util = 20*params.Ub   # Assuming f = (f0/U0) U

        for i in range(len(params.supported_freqs)-1):
            if fu > params.supported_freqs[i] and fu<params.supported_freqs[i+1]:
                new_fmin = params.supported_freqs[i]
                new_fmax = params.supported_freqs[i+1]
                break

        if new_fmin<f_util:
            new_fmin = f_util
            new_fmax = f_util+1

        Tsw = params.Ts * (fu - new_fmin)/(new_fmax - new_fmin)
        return [new_fmin, new_fmax, Tsw]
    
        
