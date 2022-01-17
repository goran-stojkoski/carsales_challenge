# Carsales Data team - Data engineer coding assignment

### Requirement:
To generate reports to measure and track conversions metrcis of the products.

### Reports:
1. Report Number of page views aggregated by day
2. Report Number of purchases by day
3. % Report conversions by the day. Conversion = Number of purchases / page views 
4. % Revenue Conversion by the day. Revenue Conversion =  Total Purchase Amount / pageviews 


### Coding test

Create a data pipeline to generate the reports. 
Explain the ratioanale of the approached used. 
Share the SQL queries to generate the reports.

#### Source data: 
The location of the source data is in S3

1. _weblog.txt_ : 
   1. Web log for page views
   2. Location : s:\\<bucketname>\weblogs
2. _transactions.csv_ : export of transactions events
   1. Transaction data from database
   2. Location : s:\\<bucketname>\transactions


#### Reporting data: 
The reporting data should be stored in S3.  

#### Data pipeline:
* The transformations could be in any coding language, or even completely sql based. 
* Best practices should be used.
* This code will be referred in the interview to assess approach for improvements and enhancements.
* The candidate will have to demo the assignment.   
  