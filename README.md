# CondorJobs

## Make text files for the input files

``` python crabListMaker.py inputpath outputFolder ```

## Changes to be done in executing files.

Copy the output folder of the above command to ```line 2``` of ```MultiSubmit.py``` file.

Change the number of file per jobs in ```line 4``` of ```MultiSubmit.py``` file.

Open the ```runAnalysis.sh``` file, and in line 22 change the year for which you are running(by default it is 2017).

Open the ```runAnalysis.sh``` file, and in line 26 change the location of output files.

Open the ```SkimTree.py``` file from above directory and change ```isCondor = False``` to ```isCondor = True```.

## Submit the condor jobs

Finally run

```. submitjobs.ch```

Condor Jobs will be submitted with this file.

Run the following command to see the status:

```tail -f logsubmit.txt```