## Working with files assignment

1. Download file from http://spatialkeydocs.s3.amazonaws.com/FL_insurance_sample.csv.zip or dowload file data.csv from this repo
2. Write a script that parses data file and as a aresult creates a result.json file with content:

```json
{
  "total_tiv": {
    "2011": 8888,
    "2012": 8888
  },
  "avg_total_tiv": {
    "2011": 4444,
    "2012": 4444
  }
}
```
3. 8888 and 4444 are just a dummy values, you should calculate your own.
5. Provide a pull request with script and result.json file. 
6. **Do not include the data.csv file!**
8. Use DictReader and DictWriter methods (https://docs.python.org/3/library/csv.html?highlight=csv#csv.DictReader, https://docs.python.org/3/library/csv.html?highlight=csv#csv.DictWriter)
