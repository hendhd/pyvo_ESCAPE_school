#! /usr/bin/ python
# -*- coding=utf-8 -*- 

# A demo program to show how a TAP query in PyVO works. 


# import the packages we will need
import pyvo
import warnings

# Keep the output of this example "sane".
warnings.simplefilter("ignore")

def main():
  # Make the service object
  service = pyvo.dal.TAPService ("http://dc.zah.uni-heidelberg.de/tap")

  # Query the TAP service with a simple ADQL query.
  result = service.search ("SELECT TOP 1 * FROM ivoa.obscore")

  """ IMPRESS ME WITH REAL SCIENCE HERE """

  # Write the result into a VO-table
  result.votable.to_xml("result_example2.vot")

if __name__=="__main__":
  main()



