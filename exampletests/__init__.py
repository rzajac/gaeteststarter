import os
import sys

# We need to do this to test exampleapp
my_path = os.path.dirname(os.path.realpath(__file__)) + '/../exampleapp'
my_path = os.path.realpath(my_path)
sys.path.insert(0, my_path)
