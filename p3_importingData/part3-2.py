# # Import pickle package
# import pickle
#
# # Open pickle file and load data: d
# with open('data.pkl', 'rb') as file:
#     d = pickle.load(file)
# ;
#
# # Print d
# print(d)
#
# # Print datatype of d
# print(type(d))
# ---------------------------------------------------------
# # https://www.prio.org/data
# ---------------------------------------------------------
# sas econometrics data
# http://www.principlesofeconometrics.com/poe5/poe5sas.html
# ---------------------------------------------------------
# # Import pandas
# import pandas as pd
#
# # Assign spreadsheet filename: file
# file = 'battledeath.xlsx'
#
# # Load spreadsheet: xls
# xls = pd.ExcelFile(file)
#
# # Print sheet names
# print(xls.parse('0'))
# ---------------------------------------------------------
# Import sas7bdat package
from sas7bdat import SAS7BDAT

# Save file to a DataFrame: df_sas
with SAS7BDAT('nels.sas7bdat') as file:
    df_sas = to_data_frame(file)

# Print head of DataFrame
print(df_sas.head())

# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()
# ---------------------------------------------------------
# dta file read
df = pd.read_stata('disarea.dta')
# ---------------------------------------------------------
# Import pandas
import pandas as pd

# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('disarea.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
plt.show()
# ---------------------------------------------------------
In [6]:
h5py.File(h5py_file,'r')
Out[6]:
<HDF5 file "LIGO_data.hdf5" (mode r)>
In [7]:
a=h5py.File(h5py_file,'r')
In [8]:
print(a)
<HDF5 file "LIGO_data.hdf5" (mode r)>
In [9]:
print(a.head())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(a.head())
AttributeError: 'File' object has no attribute 'head'
In [10]:
print(a.keys())
<KeysViewHDF5 ['meta', 'quality', 'strain']>
In [11]:
print(a['meta'].keys())
<KeysViewHDF5 ['Description', 'DescriptionURL', 'Detector', 'Duration', 'GPSstart', 'Observatory', 'Type', 'UTCstart']>
In [12]:
print(a['quality'].keys())
<KeysViewHDF5 ['detail', 'injections', 'simple']>
In [13]:
print(a['strain'].keys())
<KeysViewHDF5 ['Strain']>
In [14]:
print(a['strain']['Strain'])
<HDF5 dataset "Strain": shape (131072,), type "<f8">

# gravity wave research data
# https://www.gw-openscience.org/GW150914data/LOSC_Event_tutorial_GW150914.html

# -------------------------------------------------------------
# Import packages
import numpy as np
import h5py

# Assign filename: file
file = 'LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)
# -------------------------------------------------------------
# import data set from hdf5
# Get the HDF5 group: group
group = data['strain']

# Check out keys of group
for key in group:
    print(key)

# Set variable equal to time series data: strain
strain = data['strain']['Strain'].value

# Set number of time points to sample: num_samples
num_samples=10_000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()
# -------------------------------------------------------------
# importing matlab files (act like dicts, keys = matlab objects, vals = their respective value)
# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')

# Print the datatype type of mat
print(type(mat))
# -------------------------------------------------------------
# open source gene expresson data from Albeck Lab at UCDavis:
# https://www.mcb.ucdavis.edu/faculty-labs/albeck/workshop.htm
# Print the keys of the MATLAB dictionary
print(mat.keys())

# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['CYratioCyt']))

# Print the shape of the value corresponding to the key 'CYratioCyt'
print(mat['CYratioCyt'].shape)


# Subset the array and plot it
data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()
