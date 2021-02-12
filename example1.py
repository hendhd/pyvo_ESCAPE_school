#! /usr/bin/ python
# -*- coding=utf-8 -*- 

# A demo program to show how a SIA query in PyVO works. 

import pyvo
import warnings

warnings.simplefilter("ignore")


def main():
  # Set the service url
  access_url = "http://dc.g-vo.org/lswscans/res/positions/siap/siap.xml?"
  
  # Make the service object
  service = pyvo.sia.SIAService(access_url)
  
  # Search the Service for images at a given position (ra,dec)
  # and a given rectangle (height, width) in degrees
  results = service.search((10.0, 35.0), (0.5, 0.5))
  
  # Some user defined "logic" for the sake of the presentation
  for image_desc in results:
    print(image_desc.title, image_desc.dateobs, image_desc.filesize)

  # Select an image to download
  image=results[0]
  # Download the image
  image.cachedataset()


if __name__=="__main__":
  main()


