## Working with files assingment

1. Download file from http://spatialkeydocs.s3.amazonaws.com/FL_insurance_sample.csv.zip or dowload from this folder data.zip
2. Write a script that parses this data file and aas aa aresult creates a result.json file with content:

```json
{
  "total_tiv": {
    "2011": 8888888,
    "2012": 8888888
  },
  "avg_total_tiv": {
    "2011": 8888888,
    "2012": 8888888
  },
  "counties": [
    {
      "name": "CLAY", 
      "data": {
          "total_tiv": 8888888,
          "avg_tiv": 8888888,
          "years": {
            "2011": {
              "total_tiv": 8888888,
              "avg_tiv": 8888888
            },
            "2012": {
              "total_tiv": 8888888,
              "avg_tiv": 8888888
            }
          }
      }
    },
    {
      "name": "SUWANNEE",
      ...
    }
  ]
}
```
3. 8888888 is just a dummy value, you should calculate your own.
4. you should ccalculate data for each county in dataa set.
5. Provide a pull request with script and result.json file. 
6. **Do not include the data.csv file!**
7. Note that word COUNTY **should not be included** in name of county item.
