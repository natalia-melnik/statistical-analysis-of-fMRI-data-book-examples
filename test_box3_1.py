# Test Box 3_1.py

import unittest, os
import scipy.io

def load_matlab_data_file(directory, filename):
    return scipy.io.loadmat(directory + filename) # load MATLAB file into dict

class TestBoxValues(unittest.TestCase):
      
    # Test all dict keys 
    def test_values_via_keys(self):
        current_file_name = 'box3_1' # TODO: Generalize to all files
        
        # Load MATLAB data, aka the ground truth
        directory = os.getcwd()  + '/matlab_files/'
        matlab_data = load_matlab_data_file(directory, current_file_name) 
        
        # Load Python data
        python_data = __import__(current_file_name)
        # TODO: turn off plot upon import
    
        for k in matlab_data.keys():
            if not k.startswith('__'): # ignore class attributes
                if matlab_data[k].shape[1] == 1: # test scalar values
                    current_python_variable_value = eval("python_data." + k)
                    self.assertEqual(matlab_data[k], 
                                     current_python_variable_value)
                elif matlab_data[k].shape[1] > 1:  # test vector values
                   """ This part will be tricky.
                   python_data.hrf is a function that return a vector
                   """
                   pass
#                   current_python_variable_value = eval("python_data." + k)
#                   self.assertEqual(matlab_data[k], 
#                                     current_python_variable_value)

if __name__== "__main__":
    unittest.main()
    
# TODO: move tests to separate folder