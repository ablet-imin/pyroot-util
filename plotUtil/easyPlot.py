import ROOT


#create a class to plot single hist,
#plot stack hists, plot aditional hist
#top on existing hist.

class histplot():
    # do I need static variable?
    def __init__(self, name = "canv", size=[800,500],):
        self.name = name
        if isinstance(size, list):
            self.canv = self._create_canvas(size)
        else:
            raise "size must be a list of length 2"
        self.labels = ROOT.TLegend(0.5, 0.7, 0.8, 0.9)
    def _create_canvas(self, size):
        return ROOT.TCanvas(self.name, self.name, size[0], size[1])
    
    def legend(self, x, y, option='brNDC'):
        self.canv.cd()
        self.labels.SetX1(x[0])
        self.labels.SetX2(x[1])
        self.labels.SetY1(y[0])
        self.labels.SetY2(y[1])
        self.labels.SetFillColorAlpha(19, 0.5)
        self.labels.SetLineColorAlpha(19, 1)
        self.labels.Draw()
        self.canv.Update()
    def plot(self, hist, label=None, option='hist', color=None, legend_option='lp'):
        if not isinstance(hist,list):
            hist = [hist]
        if label and not isinstance(label,list) :
            label = [label]
        if color and not isinstance(color,list) :
            color = [color]
        self.canv.cd()
        for i, _h in enumerate(hist):
            if color:
                _h.SetLineColor(color[i])
                _h.SetMarkerColor(color[i])
            _h.Draw(option)
            
            if label:
                self.labels.AddEntry(_h, label[i],legend_option)
            
        self.canv.Update()
        
        return self.canv
    
    def grid(self, axis=""):
        axis=axis.lower()
        if 'x' in axis:
            self.canv.SetGridx(1)
        if 'y' in axis:
            self.canv.SetGridy(1)
            
    def log(self, axis=""):
        axis=axis.lower()
        if 'x' in axis:
            self.canv.SetLogx(1)
        if 'y' in axis:
            self.canv.SetLogy(1)
        if 'z' in axis:
            self.canv.SetLogz(1)
            
     #create stack hists
    def gst(self, hist=[], color=[]):
        if len(hist)<2:
            return
        for i in range(len(hist)-1):
            hist[i].SetFillColor(color[i])
            for _h in hist[i+1:]:
                hist[i].Add(_h)
        #fill out last one
        hist[len(hist)-1].SetFillColor(color[len(hist)-1])
        return hist
    
    def stack(self, hist, label=None, option='same hist', color=None, legend_option='f'):
        if not isinstance(hist,list):
            hist = [hist]
        if label and not isinstance(label,list) :
            label = [label]
        if color and not isinstance(color,list) :
            color = [color]
            
        #we get reverse orderded hist
        hist = self.gst(hist[::], color[::])
        self.plot( hist[-1:])
        self.plot( hist=hist, label=label, option=option, legend_option=legend_option)
        
        self.canv.Update()
        
        return self.canv
