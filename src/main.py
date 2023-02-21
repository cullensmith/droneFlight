import geopandas as gpd


# convert the notebook
# add in the weather api calls

def import_data(file):
    hazard = gpd.read_file(file)
    print(f"warning: {hazard['name'][0]}")
    hazard.plot()

def check_projection():
    #check the projections of the incoming data
    pass

def main():
    flight_path = import_data('data/samplePath.gpkg')
    hazard = import_data('data/sampleHazard.geojson')
    

if __name__ == '__main__':
    print('importing the hazard...')
    main()

