import ROOT
import numpy as np

"""
Dump histogram content and error
to numpy arrays.
"""

def to_array(hist1D, error=False):
    '''
    hist_content, hist_error = to_array(hist1D, error=True)
    '''
    len_ = hist1D.GetNbinsX()

    content_ = np.array([hist1D.GetBinContent(i) 
                             for i in range(1,len_+1) ] )
    if error :
        error_   = np.array([hist1D.GetBinError(i) 
                             for i in range(1,len_+1) ] )
    else:
        error_ = None

    return content_, error_
