'''
Log 12th September 2016 - 

Log 4th July 2016 - Sim 1,2,3,4,5 folders are when TRN to TCR connectivity weight is 2
Sim 1a, 2a, 3a, 4a, 5a folders are when the same is 4.

Log: 8th June 2016
This file is for removing the header files from the data generated with simulating SysManCyberB_Tonic_June16.py
Each .dat file is opened, read, the header files removed, and data re-written on to another folder, which needs to be
named and prepared prior to running this file; else an error will be generated.
For example, I am storing data from each simulation in subfolders called Sim1, Sim2, etc. So I create these first prior
to running this file.

The number of header lines generated with SpiNNaker is currently 5, hence inputted as a fixed number here.
For details on other parameters, please see comments for file SysManCyberB_Tonic_June16.py

Code Copyright of Akash Bhattacharya, 2nd Year Student, MSc Course in Chemistry with Molecular Physics, Imperial College London, 2015-2016.
'''
# Setting number of lines in header.
num_header_lines = 5 ### DO NOT CHANGE WHEN RUNNING ON DATA GENERATED WITH SPINNAKER COMPUTER
#filenameapp='tonic'
loop=0
print('now working on spike source array inputs')

while loop < 1:
    loop = loop+1
    print loop
    
    ######################################
    ######################################
    ######------------THALAMIC RELAY NEURONS-----------------
    # Opening original data file.
    infile = open('./Sim1_3hz_0916/TCRmempot_'+`loop`+'.dat', "r")

    # Storing lines in file in a list
    lines = infile.readlines()

    # Closing file.
    infile.close()

    # Creating output file...
    with open('./matlabFiles/SysManCyberB_Sep16/PeriodicSpikeTrain/exp3hz/Sim1/TCRmempot_'+`loop`+'.dat', "w") as outfile:
        # Writing to output file all data except headers.
        for i in range(num_header_lines, len(lines)):
            outfile.write(lines[i])

    # Closing output file.
    outfile.close()


    ######################################
    ######################################
    ######------------INTERNEURONS-----------------
    # Opening original data file.
    infile = open('./Sim1_3hz_0916/INmempot_'+`loop`+'.dat', "r")

    # Storing lines in file in a list
    lines = infile.readlines()

    # Closing file.
    infile.close()

    # Creating output file...
    with open('./matlabFiles/SysManCyberB_Sep16/PeriodicSpikeTrain/exp3hz/Sim1/INmempot_'+`loop`+'.dat', "w") as outfile:
        # Writing to output file all data except headers.
        for i in range(num_header_lines, len(lines)):
            outfile.write(lines[i])

    # Closing output file.
    outfile.close()


    # ######################################
    # ######################################
    # ######------------THALAMIC RETICULAR NUCLEUS-----------------
    # Opening original data file.
    infile = open('./Sim1_3hz_0916/TRNmempot_'+`loop`+'.dat', "r")

    # Storing lines in file in a list
    lines = infile.readlines()

    # Closing file.
    infile.close()

    # Creating output file...
    with open('./matlabFiles/SysManCyberB_Sep16/PeriodicSpikeTrain/exp3hz/Sim1/TRNmempot_'+`loop`+'.dat', "w") as outfile:
        # Writing to output file all data except headers.
        for i in range(num_header_lines, len(lines)):
            outfile.write(lines[i])

    # Closing output file.
    outfile.close()
