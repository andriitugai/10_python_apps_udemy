import argparse
from PIL import Image
from PIL.ExifTags import TAGS

import googlemaps
from datetime import datetime
from pprint import pprint

def getMetaData(imgname, out):
    try:
        metaData = {}
        imgFile = Image.open(imgname)
        print("Getting metadata...")
        info = imgFile._getexif()
        if info:
            print("Found metadata")
            pprint (info)

            for (tag, value) in info.items():
                tagname = TAGS.get(tag, tag)
                if tagname in ["GPSInfo", "DateTime"]:
                    metaData[tagname] = value
                    if not out:
                        print(tagname, value)

            # if out:
            #     print("Outputting to file...")
            #     with open(out, 'w') as f:
            #         for(tagname, value) in metaData.items():
            #             f.write(str(tagname)+"\t"+str(value)+"\n")


        if metaData["GPSInfo"]:
            print("Parsed GPS:")

            dlat = int(metaData["GPSInfo"][2][0][0]) + (int(metaData["GPSInfo"][2][1][0])/60.0) + (int(metaData["GPSInfo"][2][2][0])/3600.0)
            dlon = int(metaData["GPSInfo"][4][0][0]) + (int(metaData["GPSInfo"][4][1][0])/60.0) + (int(metaData["GPSInfo"][4][2][0])/3600.0)

            if metaData["GPSInfo"][1] == 'S':
                dlat = -dlat
            if metaData["GPSInfo"][1] == 'W':
                dlon = -dlon

            print("( %f, %f )" % (dlat, dlon))

            gmaps = googlemaps.Client(key = "AIzaSyBHwzjDTwec95YZ6a1p1ts0Ygr5LVw5wCk")

            reverse_geocode_result = gmaps.reverse_geocode((dlat, dlon))

            address =  reverse_geocode_result[0]

            pprint(address)

            pprint(address['formatted_address'])
            pprint(address['place_id'])

    except:
        print("Failed")

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("img", help="name of an image file.")
    parser.add_argument("--output", "-o", help="dump data out to file")
    args = parser.parse_args()
    if args.img:
        getMetaData(args.img, args.output)
    else:
        print(parser.usage)

if __name__ == '__main__':
    Main()
