import matplotlib.pyplot as plt
from time import sleep
from IPython.display import clear_output

class City:
    def __init__(self, country_code, name, region, population, latitude, longitude):
        self.country_code = country_code
        self.name = name
        self.region = region
        self.population = float(population)
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        
    def __str__(self):
        output = self.name + "," + str(self.population) + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)
        return output
    
    def get_population(self):
        return self.population
        
    def get_latitude(self):
        return self.latitude
        
    def get_name(self):
        return self.name

def test_City():
	country_code = "LON"
	name = "London"
	region = "test"
	population = "1000"
	latitude = "106.6777"
	longitude = "-980.9876"
	london = City(country_code, name, region, population, latitude, longitude)
	print(london)
	london.__str__()

	return None

def write_sorted_to_file(L, file_name):
    with open(file_name, 'a') as the_file:
        for line in L: 
            the_file.write(line.__str__())
            
    the_file.close() 

    return None


def create_animation(w=720, h=360, dpi=60, cities):
	'''
	w: image (world.png) width
	h: image height
	dpi: display image at this dots-per-inch resolution
	'''

	for i in range(0, 30):
	    img = plt.imread("world.jpg")
	    plt.figure(figsize=(w/dpi,h/dpi))
	    plt.imshow(img) # Display the image
	    plt.axis('off')
	    x, y = longlat_to_pixel(cities[i].latitude, int(cities[i].longitude))
	    name = cities[i].name
	    plt.plot(x, y, 'ro') # plot one red data point
	    for j in range(0, i):
	        x_j, y_j = longlat_to_pixel(cities[j].latitude, int(cities[j].longitude))
	        plt.plot(x_j, y_j, 'bo')
	    plt.text(x=x, y=y, s=name)
	    sleep(0.5)
	    clear_output(wait=True)
	    plt.show()




