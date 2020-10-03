## Working with files assignment

1. Download file from http://spatialkeydocs.s3.amazonaws.com/FL_insurance_sample.csv.zip or dowload here from data.csv
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
  }
}
```
3. 8888888 is just a dummy value, you should calculate your own.
5. Provide a pull request with script and result.json file. 
6. **Do not include the data.csv file!**
8. Use DictReader and DictWriter methods (https://docs.python.org/3/library/csv.html?highlight=csv#csv.DictReader, https://docs.python.org/3/library/csv.html?highlight=csv#csv.DictWriter)
