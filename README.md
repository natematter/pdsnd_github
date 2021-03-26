
### Date created
* 03/26/2021

### US Bikeshare Project 
This project was created as part of the Udacity Programming for Data Science Nano-Degree Course

### Setup
I used a python virtual env on my local system with the latest versions of 
numpy and pandas installed via pip.

#### To run it:
```bash
    $ python bikeshare.py
```

### Description
The purpose of this project was to demonstrate how to explore and analyze large 
sets of data using python scripting and the associated numpy and pandas python 
modules.  

The focus was on sets of data related to bike sharing systems used in three 
different major US cities (Chicago, New York City and Washington).

The python script (bikeshare.py) is expected to be run from the command line.

The actually datasets for each city are not provided in this repository.

### Files used

#### Provided
* bikeshare.py - this is the main python script used to perform the analysis on a data set

#### Not Provided (US Bike Share data for three major cities)
* chicago.csv - for the city of Chicago
* new_york_city.csv - for the city of New York City
* washington.csv -for the city of Washington D.C.

### Credits
* for help displaying all the columns of the DataFrame
  * https://stackoverflow.com/questions/49188960/how-to-show-all-of-columns-name-on-pandas-dataframe

* for help to better understand pandas.iloc (and other pandas functions when i was stuck)
  * https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html

* for help creating the START_TITLE string, i used the figlet program
```bash
    $ figlet -c US Bikeshare Data
```

* for help rendering markdown files offline, i used grip (thank you joe!)
  * https://stackoverflow.com/questions/9843609/view-markdown-files-offline
