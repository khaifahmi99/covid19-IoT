#******************************************************************
#% FILENAME:        tx_device.py
#% AUTHOR:          Sam Golding 
#% VERSION:         1.0
#% VERSION DATE:    14/10/2020
#%
#% #% DESCRIPTION: This function constructs a dictionary data type 
#% to send trigger results from an IoT device to a security module
#% for encryption processing.
#%
#% 1st argument is the trigger as a string (fall, no_dist, no_mask)
#% 2nd argument is the confidence value from the model for the 
#% trigger decision.
#% 
#% v1.0 simulates that a security device is connected by printing
#% the results string to the devices serial port.
#% Future versions will output data to an external security module
#% via an available communications channel.
#%
#% USAGE: 
#% 1. import tx_device, tx_device.transfer(string, float)
#% 2. python tx_device trigger confidence
#******************************************************************

#=== Import Modules ===#
import sys
import utime as time

#== Define Functions ==#
def transfer(trigger, conf):
    time_current = time.localtime()
    time_s = '{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}'.format(time_current[0],time_current[1],time_current[2],time_current[3], time_current[4], time_current[5])

    data = {'data': str(time_s) + ", " + trigger + ", " + str(conf)}
    print(data['data'])
    return

#==== Main routine ====#
def main():    
    args = sys.argv

    args_l = args[1:]
    transfer(args_l[0], args_l[1])


if __name__ == '__main__':
    main()