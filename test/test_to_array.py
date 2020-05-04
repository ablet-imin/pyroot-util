import ROOT
import numpy as np
from context import histUtil
from histUtil.dump_to_array import to_array
hist1 = None
f = ROOT.TFile.Open("~/cernbox/sys_hists_BStar_1000_smoothed.root")
hist1 = f.Get("OneTagBOneProbeB/JET_JER_EffectiveNP_7restTerm__1up")
hist1.SetDirectory(0)
f.Close()

hcontent, _ = to_array(hist1)
print(hcontent)

del hist1, hcontent
