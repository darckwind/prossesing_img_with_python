import landsatxplore.api
import urllib.request

class Satelite:
    #apriori
    #metodo encargado de la descarga desde el satelite LANDSAT_8_C1
    @staticmethod
    def descarga():
        api = landsatxplore.api.API("f.bunout01@ufromail.cl", "Pokemon22300")

        # Request
        scenes = api.search(
            dataset='LANDSAT_8_C1',
            latitude=-38.680782,
            longitude=-71.2800889,
            start_date='2019-01-24',
            end_date='2019-02-01',
            max_cloud_cover=1)

        #print('{} scenes found.'.format(len(scenes)))

        #print(scenes)

        for scene in scenes:
            #print(scene['displayId'])
            url = 'https://earthexplorer.usgs.gov/browse/full/landsat_8/' + scene['displayId']
            url_ir = 'https://earthexplorer.usgs.gov/browse/full/landsat_8/' + scene['displayId'] +'_TIR'
            #print(url)
            urllib.request.urlretrieve(url,'/Users/franciscolagos/PycharmProjects/untitled/satelital_img/satelital_org_img.jpg')
            urllib.request.urlretrieve(url_ir,'/Users/franciscolagos/PycharmProjects/untitled/satelital_img/satelital_org_ir_img.jpg')
        api.logout()
        return True

Satelite.descarga()