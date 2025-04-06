# week 11 - EXTRA: Pandas 
# irene celebrin

## video 1 - input and output file 

pandas is useful to analyse data that is in tabular form, so for many data analytics files 

What is pands useful for? 
ASnalysing data in tabular form -- not just excel sheets 

Objects: 
- Data frame == table with column names (attribute names) and idexes (slightly differents to keys in SQL)
- data series == columms
Each columsn should have the same data type. 
the index identifies a specific of data. 
- Pandas does not do formatting 
- Pandas does not have column names, but you can add it. 

Information on pandas official documentation 
Getting started tutorial 
Comparison with other tools like using SQL on pandas 

Real Python, w3school (not as sueful)

**Reading and Writing data**

you can use a lot of formtas, put in a dataframe, do the manipulation and outpul to different formats (you can do the same with python dict, list, arrays )

To format cells, you can't use python 

READ IN DATA 

1) you can think of the tabular form as a pyhton type and just use python
2) import that into pandas and convert to data frame 
3) you can also add indices and change them 

- you can use dict objects of lists 
- you can use dict objects 
- you can use lists 

Reading in from files
use pd.read_table()

df.to.excel() to overwrite an excel book 
it overrides by default. to append you need to specify mode='a'
also to create the new tab you need to use openpyxl 

## video 2 -- data manipulation 

- accessing data
- remove nan
- formatting (add remove / columns)
- replacing values 

CHECK IF VALUES ARE UNIQUE 

SHUFFLE IDS to change them 

SHUFFLE part of the modules 

most of the times when you do data manipulation you do it in the whole column 

check messingWithDataManipulation.py 

1) read files 
- read from the tsv. you can print just the first row (print(df.head))
(print(df.['module ID'].head(2))) first 2 values in the column moduleID 
you can pass list in the square brackets you can access multiple columns 
- you can use loc -- check docum 

2) create a column 
you can create the column and programmatically add data from other colums, calculating from other columsn or probably fro, external sources as well. 

3) 
example: randomise data in a column. Shuffle data, but also replace a given sequence of characters with other characters 

check documentation in to_replace 
also data maniuplation nice stuff on w3 schools 

## video 3  -- pandas for data analytics 

what pandas is good at, compared to other tools: 
- built in stat functions (max, min..)
- sampling in ranges 
- group data 
- plot data 

check pandas documentation 
in particular comparison with other tools 

1) import csv to dataframe. specify that col 0 is indices 

2) cleanup data to remove nan
df.dropna (inplace=True)
df.drop_duplicates (inplace=True)

3) get average grades 

df.groupby('subject').mean
fr.groupby('name).mean

meanvalues are also dataframes 

4) remove duplicate grades for same person/subject 
you create a pivot table where index taks in name and subject and aggregate function max and reset index. 
documetnation on pivot tableas

5) PLOT 
df.plot.bar()
plt.show()

you make a pivot table to chane the data shape so that the bar is more meaningful more documentation on dataframe.plot 

6) correlation 
correlation bewteen different values 
df.corr()

