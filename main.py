from bridges.data_src_dependent import data_source
import random

#pick a random latitude and longitude value to start with 
base_lat = random.uniform(-83,83)
base_long = random.uniform(-173,173)


# defines the box where we are taking our coordinates 
# box size of 5.3x5.3degrees gets us around 100k data points
bbox = [base_lat, base_long, base_lat+5.3, base_long+5.3]  
ele_obj = data_source.get_elevation_data(bbox)

#now we need to put all of our elevation data into one list 
flat_data = []
for row in ele_obj.data:
    for val in row:
        flat_data.append(val)


print(len(flat_data))

