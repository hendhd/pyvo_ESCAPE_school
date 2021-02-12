#! /usr/bin/ python
# -*- coding=utf-8 -*- 

from astropy.table import Table
import pyvo

import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")

query="""
SELECT
   TOP 50
   *
   FROM ivoa.obscore AS db
   JOIN TAP_UPLOAD.lt AS mine
   ON 1=CONTAINS (POINT('ICRS', db.s_ra, db.s_dec),
                 CIRCLE('ICRS', mine.RA, mine.Decl, mine.Beta))
   AND db.dataproduct_type='image'
"""

def main(query):

  # Try to load table of neutrinos 
  lt = Table.read('neutrinos.vot', format='votable')

  # Make Service Object
  service = pyvo.dal.TAPService ("http://dc.zah.uni-heidelberg.de/tap")

  # Run Search on obscore table on the GAVO dc
  result = service.run_async(query=query, uploads={"lt":lt})

  # Send resulting table to Topcat via SAMP
  result.broadcast_samp("topcat")


if __name__=="__main__":
  main(query)
