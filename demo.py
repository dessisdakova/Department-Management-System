import os
filename = "demo.json"
full_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data", filename)

print(filename)