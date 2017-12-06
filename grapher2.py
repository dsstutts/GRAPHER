####################--
# File: grapher2.py
# Plots x,y tab-delimited data
# Author: D. S. Stutts
# Associate Professor of Mechanical Engineering
# 282 Toomey Hall
# 400 W. 13th St.
# Rolla, MO 65409-0050
# Email: stutts@mst.edu
# Original release: 9-5-2016
# Language: Python 3.6.2
####################--

"""
Graphs y and x with respect to x where
x,y, and z are tab or comma delimited numerical values
in a text file.

Example call: python grapher2.py inputdatafile.txt

The graph may be saved in PNG format, and the text
may be redirected from stdout to a file like so:

python grapher2.py inputdatafile.txt > outdata.txt

 # This code is copyrighted by the author, but released under the MIT
 # license:

Copyright (c) 2016 -- grapher2.py

S&T and the University of Missouri Board of Curators 
license to you the right to use, modify, copy, and distribute this 
code subject to the MIT license:

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included 
in all copies or substantial portions of the Software. 

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE.

The author kindly requests that any publications benefitting from the use
of this software include the following citation: 

@Misc{grapher_2016,
author =   {Stutts, D. S.},
title = {{grapher2.py}: {Python data plotting script.}},
howpublished = {\\url{https://github.com/dsstutts/GRAPHER.git}},
year = {2016}}

"""

#from pylab import *
import sys
from numpy import array
import matplotlib.pyplot as plt
import time #to allow time stamp on output
import re
# Test for Python version:
cur_version = sys.version_info
# Initialize some lists:
linedat = []
f = []
x = []
y = []
xx = []
yy = []

# Set the desired resolution:
res = 72# Use larger value if plottype = PNG

#plottype = ''# Defaults to PNG
plottype = 'EPS'
# Input data file on command line:	
infile = sys.argv[1]
data = open(infile, "r")  # get array out of input file
numline = 0
# Count the number of lines in the data file:
for line in data:
    numline +=1

# Calculate the number of magnitude data points:

data.seek(0) # Reset file pointer to the beginning

linecount = 0
  # read the 1st through total lines from the data file
  # and fill f, x,y lists with floating point numbers:
if cur_version[0]==3:# This is necesary due to the change in the type
    for line in data:# returned by the map function in Python 3.x.x.
        #linedat = list(map(float, line.re.split(' '|',',str)))
        if linecount >= 1:
            linedat = list(map(float, re.split('\t|,',line)))
            f.append(linedat[0])
            x.append(linedat[1])
            y.append(linedat[2])
        
        linecount += 1

else:
    for line in data:
        if linecount >= 1:
            linedat = re.split('\t|,',line)
            f.append(linedat[0])
            x.append(linedat[1])
            y.append(linedat[2])
        linecount += 1
data.close()
xx = array(x)
yy = array(y)

print ("Number of lines = ",linecount)
# Locate Ymax, xmax, Ymin, and xmin:
Ymax = max(y)
fymax = y.index(Ymax)
Xmax = max(x)
fxmax = x.index(Xmax)
Ymin = min(y)
fymin = y.index(Ymin)
Xmin = min(x)
fxmin = x.index(Xmin)
imax = len(x)
print ("Maximum y = ",Ymax," Located at f = ",fymax)
print ("Minimum y = ",Ymin," Located at x = ",fymin)
print ("Maximum x = ",Xmax," Located at f = ",fxmax)
print ("Minimum yx = ",Xmin," Located at x = ",fxmin)
delx = (x[imax-1]-x[0])/10.0
dely = (Ymax-Ymin)/20.0
notex = 0.5*xx[imax-1]
meanx = (Xmax+Xmin)/2.0
print ("delx = ",delx)
print ("dely = ",dely)
noteymax = 0.75*Ymax
print ("noteymax = ",noteymax)
# Plot the data:
plt.figure(figsize=(8,7),dpi=res)
# Add date and time in plot title:
loctime = time.asctime(time.localtime(time.time()))
plt.plot(xx, yy, 'go', label='data')
# Add appropriate error bars to represent experimental uncertainty:
plt.errorbar(xx, yy, xerr=0.2, yerr=0.4)
plt.annotate(r"$\mathscr{y}_{max}$ = "+'{: 3.3e}'.format(Ymax),xy=(meanx+0.75*meanx,noteymax))
plt.annotate(r"$\mathscr{f}_{ymax}$ = "+'{: 3.3e}'.format(fymax),xy=(meanx,noteymax))
plt.annotate(r"$\mathscr{x}_{max}$ = "+'{: 3.3e}'.format(Xmax),xy=(meanx+0.75*meanx,noteymax-1.4*dely))
plt.annotate(r"$\mathscr{f}_{ymax}$ = "+'{: 3.3e}'.format(fxmax),xy=(meanx,noteymax-1.4*dely))
plt.annotate(r"$\mathscr{y}_{min}$ = "+'{: 3.3e}'.format(Ymin),xy=(meanx+0.75*meanx,noteymax-2.8*dely))
plt.annotate(r"$\mathscr{f}_{ymin}$ = "+'{: 3.3e}'.format(Ymin),xy=(meanx,noteymax-2.8*dely))
plt.annotate(r"$\mathscr{x}_{min}$ = "+'{: 3.3e}'.format(Xmin),xy=(meanx+0.75*meanx,noteymax-4.4*dely))
plt.annotate(r"$\mathscr{f}_{xmin}$ = "+'{: 3.3e}'.format(fxmin),xy=(meanx,noteymax-4.4*dely))
# Add date and time in plot title:
loctime = time.asctime(time.localtime(time.time()))
plt.suptitle('Data File ='+infile+':  '+loctime)

print ("Date and Time =", loctime, "\n")

legend = plt.legend(loc='upper right', shadow=True, fontsize='large')
plt.xlabel(r"$\mathscr{x}$")
plt.ylabel(r"$\mathscr{Y}$")
plt.grid(True)
# Put a nice background color on the legend:
legend.get_frame().set_facecolor('#00FFCC')

if plottype=='PNG' or plottype=='':# Default to PNG
# Save plot as PNG:
    plotname = infile.split('.')[0]+"model"+loctime+".PNG"
    plt.savefig(plotname,format='png', dpi=res)
else:# Save plot as EPS:
    plotname = infile.split('.')[0]+"model"+loctime+".EPS"
    plt.savefig(plotname,format='eps', dpi=res)

plt.show()
