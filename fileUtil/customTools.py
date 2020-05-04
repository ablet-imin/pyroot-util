
from contextlib import contextmanager

@contextmanager
def open_root(filename, opt='UPDATE'):
    '''
    Other options are CREATE (same as NEW), 
    RECREATE (i.e. replace), UPDATE and READ. 
    '''
    if "ROOT" not in dir():
        import ROOT
    f = ROOT.TFile.Open(filename, opt)
    try:
        yield f
    finally:
        f.Close()

