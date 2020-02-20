""" Program to read data from file, process it
    and draw graphs using matplotlib
    
    The program should read the input and output 
    file names from system arguements

    Author: Varun Aggarwal
    Username: aggarw82
    Github: https://github.com/Environmental-Informatics/06-graphing-data-with-python-aggarw82
"""

# import library
import numpy as np
import matplotlib.pyplot as plt
import sys
	
# checking for valid arguments
if len(sys.argv) != 3:
	print("Incorrect Syntax")
	print("Usage: python number_visualize.py [Source file] [Destination File] ... ")
	sys.exit()

# reading arguements
inFileName = sys.argv[1]
outFilename = sys.argv[2]

# read file
data  = np.genfromtxt(inFileName, 
					dtype=['int','float','float','float','float','float','float'],
					names=True,
					delimiter='\t',
					autostrip=True)


# reserving space with subplot
fig = plt.figure(figsize=(20,20))														# set figure size
ax1 = fig.add_subplot(311)																# subplot 1
ax2 = fig.add_subplot(312)																# subplot 2
ax3 = fig.add_subplot(313)																# subplot 3

# Plot 1
ax1.plot(data['Year'],data['Mean'],'k')
ax1.plot(data['Year'],data['Max'],'r')
ax1.plot(data['Year'],data['Min'],'b')
ax1.legend(['Mean','Max','Min'])														# legend
ax1.set_xlabel('Year')
ax1.set_ylabel('Streamflow (cfs)')
ax1.set_xticks(data['Year'][np.linspace(0, len(data['Year']) - 1, 12, dtype='int')])	# xticks for year

# Plot 2
ax2.plot(data['Year'],data['Tqmean']*100,'--o')											# symbol is a circle
ax2.set_xlabel('Year')
ax2.set_ylabel('Tqmean (%)')
ax2.set_xticks(data['Year'][np.linspace(0, len(data['Year']) - 1, 12, dtype='int')])	# xticks for year

# Plot 3
ax3.bar(data['Year'],data['RBindex'])
ax3.set_xlabel('Year')
ax3.set_ylabel('R-B Index (ratio)')
ax3.set_xticks(data['Year'][np.linspace(0, len(data['Year']) - 1, 15, dtype='int')])	# xticks for year

# saving figure ad pdf
plt.savefig(outFilename)
