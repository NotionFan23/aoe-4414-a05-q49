# full_ops.py
# Usage: python3 full_ops.py c_in n_wv
# Text explaining script usage
# Parameters: c_in n_wv
# Output:
# A description of the script output
#
# Written by Devon Throckmorton

# import Python modules
import math # math module
import sys # argv
# initialize script arguments
c_in = float('nan')    
n_wv = float('nan')        
if len(sys.argv) == 3:
    c_in = sys.argv[1]    
    n_wv = sys.argv[2]        
else:
    print('Usage: python3 full_ops.py c_in n_wv')
    exit()
c_out = 0
h_out = 0
w_out = 0
adds = n_wv*c_in
muls = n_wv*c_in
divs = 0
print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed