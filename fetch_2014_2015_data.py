import urllib2
import json

years = ['Deaths2015', 'Deaths_2014_Final']
data = []
for year in years:
    data.append(json.loads(urllib2.urlopen("https://services.arcgis.com/Zs2aNLFN00jrS4gG/arcgis/rest/services/" + year + "/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=true&spatialRel=esriSpatialRelIntersects&outFields=*&outSR=102100&resultOffset=0&resultRecordCount=2000").read()))


print json.dumps(data)

