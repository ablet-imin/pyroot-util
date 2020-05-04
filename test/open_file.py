
from context import  fileUtil
import fileUtil.customTools as ctools
import os, sys
from random import gauss
import ROOT



with ctools.open_root("test_open_root.root", "recreate") as rf:
    print("type of return: ", type(rf))
    if rf.IsOpen(): 
        print ("test succeeded!")
        th1f = ROOT.TH1F("testHist", "", 20, -3, 3)
        for i in range(2000):
            th1f.Fill(gauss(0., 1.))
        th1f.Write()

    else:
        print("test Failed!")

