#!/usr/bin/python3

import os, sys, subprocess
import numpy as np
import pandas as pd
#subprocess.call("pip3 install pandas", shell = True)
#import pandas as pd

pd.__version__

pd.Series(['a', 'b', 'c', 'd'])
s1 = pd.Series(['a', 'b', 'c', 'd'])
s2 = pd.Series([2,4,8,16])
pd.DataFrame( { 'letter' : s1, 'number' : s2 } )

subprocess.call('wget -qO eukaryotes.txt "ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/eukaryotes.txt" ' , shell=True)
os.system("wc -l eukaryotes.txt")
os.system("head -3 eukaryotes.txt")
#help(pd.read_csv)
df = pd.read_csv('eukaryotes.txt', sep="\t")
df
df.shape
df.columns
list(df.columns)

#df. #Didn't work
df[3:7]
df.head()
df.describe()
df = pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-'])
df.describe()

df['Organism/Name']
df['#Organism/Name']
len(df['#Organism/Name'].value_counts())
df[ ['#Organism/Name', 'Size (Mb)', 'GC%'] ].head()

df['#Organism/Name'] == 'Arabidopsis thaliana'
(df['#Organism/Name'] == 'Arabidopsis thaliana').value_counts()
df[df['#Organism/Name'].isin(["Arabidopsis thaliana"])].shape
df[df['#Organism/Name'].isin(["Arabidopsis"])].shape
cress = df[df['#Organism/Name'] == 'Arabidopsis thaliana']
cress
cress.to_csv("All_the_Arabidopsis_ones.tsv",sep="\t",header=True)
os.system("head -1 *; wc -l *")

df[df['#Organism/Name'] == 'Arabidopsis thaliana']['Size (Mb)']
sizes = df[df['#Organism/Name'] == 'Arabidopsis thaliana']['Size (Mb)']
sizes
sizes.describe()
df[df['Size (Mb)'] > 10000]
df[ (df['Size (Mb)'] > 10000) & (df['Status'] == 'Scaffold') ]

df.apply(lambda x : x['#Organism/Name'].upper(), axis=1).head()
df.columns
'Birds' in set(df['Group'])
'Birds' in set(df['SubGroup'])
'Mammals' in set(df['SubGroup'])
df[df.apply( lambda x : x['Size (Mb)'] < 500 and x['SubGroup'] in ['Birds'], axis=1 )]
df[df.apply( lambda x : x['Size (Mb)'] < 500 and x['SubGroup'] in ['Birds'], axis=1 )].shape[0] #shape?????or?,?0-?,1-??
df[df.apply( lambda x : x['Size (Mb)'] < 500 and x['SubGroup'] in ['Birds'], axis=1 )].shape[1]
df[df.apply( lambda x : x['Size (Mb)'] < 500 and x['SubGroup'] in ['Mammals'], axis=1 )].shape[0]
birds_n_mammals=df[df.apply( lambda x : x['Size (Mb)'] < 500 and x['SubGroup'] in ['Birds', 'Mammals'], axis=1 )]
birds_n_mammals
birds_n_mammals.shape
birds_n_mammals.shape[0]

df.sort_values('Size (Mb)', ascending=False).head()
df.sort_values('Size (Mb)', ascending=False, inplace=True)
df
df['Size (Mb)']
df.sort_values(['#Organism/Name', 'GC%'], ascending=[True, False]).head()

df['at_content'] = 1 - (df['GC%'] / 100)
df[ ['#Organism/Name', 'GC%', 'at_content'] ].head()
df['genus'] = df['#Organism/Name'].split(' ')[0]
df['genus'] = df.apply(lambda x : x['#Organism/Name'].split(' ')[0], axis=1)
df['#Organism/Name', 'genus'] .head()
df[ ['#Organism/Name', 'genus'] ].head()

print(df[ ['Size (Mb)', 'GC%'] ].mean())
print(df[ ['Size (Mb)', 'GC%'] ].median())
print(df[ ['Size (Mb)', 'GC%'] ].std())
df[ ['Size (Mb)', 'Genes', 'Proteins', 'GC%'] ].corr()

df.head()
df = pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-'], index_col='Assembly Accession').head()
df
df = pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-'], index_col='Assembly Accession')
df['#Organism/Name'].value_counts().head()
df = pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-'], index_col='#Organism/Name')
df.head(2)
df.shape
df = pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-'], index_col='Center')
df.head(16)
df[ ['Center'] ]
df.set_index('BioSample Accession').head(2)
df = pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-'])
df.apply(lambda x : "{} ({})".format(x['#Organism/Name'], x['BioSample Accession']), axis=1)
df.index = df.apply(lambda x : "{} ({})".format(x['#Organism/Name'], x['BioSample Accession']), axis=1)
df
df.shape
df.index.value_counts()
df['TaxID'].head(3)
df[0:3]['TaxID']
df['TaxID'].values[0:3]

df.iloc[0] # first row
df.iloc[-1] # last row
df.iloc[:,0] # first column
df.iloc[:,-1] # last column
# Multiple row and column selections examples
df.iloc[0:5]                 # first five rows of dataframe
df.iloc[:, 0:2]              # first two columns of data frame with all rows
df.iloc[ [0,3,6,24], [0,5,6] ] # 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
df.iloc[0:5, 5:8]            # first 5 rows and 5th 6th 7th columns
# The actual outputs
df.columns
df.columns[5:8]
df.iloc[0:5, 5:8]