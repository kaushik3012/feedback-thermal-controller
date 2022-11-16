# Import required Libraries
import params
from max import Max_temp
from pcs import PCS
from pwm import PWM
from CPU_model import CPU

# Driver Function
def main():

    print("Thermal Control Simulation")

    # Set initial values for flow_curr and fhigh_curr
    flow_curr = params.supported_freqs[0]   #flow(0)
    fhigh_curr = params.supported_freqs[1]  #fhigh(0)

    # Create block objects
    max_temp_block = Max_temp()
    pcs_block = PCS()
    pwm_block = PWM(fhigh_curr, flow_curr)
    cpu = CPU()
    
    # Create empty lists for storing the data
    time = []
    utilisation = []
    temperature = []

    #Sampling the temperature and utilisation 1000 times with a period of 1
    for i in range(1000):

        # Acquire the max temperature from all cores of CPU
        max_temp = max_temp_block(cpu.get_temp())  

        # Calculate the error
        error = params.temp_set - max_temp

        # Output of the PCS Block
        u = pcs_block(error)    

        # Output of the PWM Block
        pwm_out = pwm_block(u)  

        # Switch the frequency of CPU as per the switching time
        flow_next = pwm_out[0]  
        fhigh_next = pwm_out[1]
        Tsw = pwm_out[2]
        cpu.switchFreq(flow_next, fhigh_next, Tsw)

        # New Frequency becomes the current frequency of the CPU
        flow_curr = flow_next
        fhigh_curr = fhigh_next

        # Collect the data for visualisation
        time.append(i)
        temperature.append(cpu.get_temp())
        utilisation.append(cpu.get_util())


if __name__ == '__main__':
    main()