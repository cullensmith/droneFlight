import geopandas as gpd

def main():
    hazard = gpd.read_file('data/sampleHazard.geojson')
    print(f"warning: {hazard['name'][0]}")
    hazard.plot()

def check_projection():
    #check the projections of the incoming data
    pass

if __name__ == '__main__':
    print('importing the hazard...')
    main()

