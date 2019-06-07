import landsatxplore.api
import urllib.request

api = landsatxplore.api.API("f.bunout01@ufromail.cl", "Pokemon22300")

# Request
scenes = api.search(
    dataset='LANDSAT_8_C1',
    latitude=-38.680782,
    longitude=-71.2800889,
    start_date='2019-01-24',
    end_date='2019-02-01',
    max_cloud_cover=1)

print('{} scenes found.'.format(len(scenes)))

print(scenes)

for scene in scenes:
    print(scene['displayId'])
    url = 'https://earthexplorer.usgs.gov/browse/full/landsat_8/'+scene['displayId']
    print(url)
    urllib.request.urlretrieve(url, '/Users/franciscolagos/PycharmProjects/untitled/satelital_img/satelital_org_img.jpeg')
api.logout()