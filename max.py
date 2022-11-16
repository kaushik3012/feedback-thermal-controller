import params

#Class to find maximum temperature of all cores
class Max_temp:
    
    def __init__(self):
        self.max_temp = params.max_temp_supported
    def __call__(self, temp_arr):
        max_temp = max(temp_arr)
        if max_temp < self.max_temp:
            self.max_temp = max_temp
        return self.max_temp

