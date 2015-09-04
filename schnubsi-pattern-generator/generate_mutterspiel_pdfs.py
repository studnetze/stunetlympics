#!/usr/bin/env python
# -*- coding: utf-8 -*-



import numpy
import os


header1 = """

digraph G {


ratio="fill";
size="8.3,11.7!";
margin=0.1;

graph [label="Blatt """


header2 = """ ", labelloc=t, fontsize=30];


nodesep=1;
ranksep=0.1;
node [shape=rectangle];


edge[style=invis];

node[group=a];
"""

footer = """
}
"""



for blatt in range(1,19):
    
    dotFile = open("dotfile.dot","w")
    fileContent = header1 + str(blatt)+ header2

    blackBlocks = numpy.random.permutation(range(1,46))[1:31]


    for block in range(1,46):
        
        fileContent = fileContent + " "+ str(block) +"->"
        
    fileContent = fileContent[0:-2] + "\n"

    for block in range(1,46):
        fileContent = fileContent + str(block) + ' [label="'+str(block)+'"]\n'



    for block in blackBlocks:
        
        fileContent = fileContent + str(block) + " [style=filled,fillcolor = red]\n"

        
    fileContent = fileContent + "\n\nnode[group=b]; \n\n"




    for block in range(46,91):
        
        fileContent = fileContent + " "+ str(block) +"->"
        
    fileContent = fileContent[0:-2]+"\n"

    i=1
    for block in range(46,91):
        fileContent = fileContent + str(block) + ' [label="'+str(i)+'"]\n'
        i = i+1


    blackBlocks = numpy.random.permutation(range(46,91))[1:31]

    for block in blackBlocks:
        
        fileContent = fileContent + str(block) + " [style=filled,fillcolor = red]\n"
        

    fileContent = fileContent + footer

    dotFile.write(fileContent)
    dotFile.close()
    
    os.system("dot -Tpdf dotfile.dot -o test_"+ str(blatt)+".pdf")
    
