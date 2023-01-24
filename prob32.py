"""How will you find the nearest value in a given numpy array?"""
import numpy as np
def find_nearest_value(arr, value):
    arr = np.asarray(arr)
    idx = (np.abs(arr - value)).argmin()
    return arr[idx]
arr = np.array([ 0.21169, 0.61391, 0.6341, 0.0131, 0.16541, 0.5645, 0.5742])
value = 0.52
print(find_nearest_value(arr, value))
