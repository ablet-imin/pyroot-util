import ROOT

import ROOT.gStyle as gStyle
import ROOT.gPad as gPad

def ATLAS_style(gStyle):
    #use plain black on white colors
    icol=0 #WHITE
    ROOT.gStyle.SetFrameBorderMode(icol)
    ROOT.gStyle.SetFrameFillColor(icol)
    ROOT.gStyle.SetCanvasBorderMode(icol)
    ROOT.gStyle.SetCanvasColor(icol)
    ROOT.gStyle.SetPadBorderMode(icol)
    ROOT.gStyle.SetPadColor(icol)
    ROOT.gStyle.SetStatColor(icol)
    #gStyle.SetFillColor(icol) #don't use: white fill color for *all* objects

    #set the paper & margin sizes
    ROOT.gStyle.SetPaperSize(20,26)

    #set margin sizes
    ROOT.gStyle.SetPadTopMargin(0.05)
    ROOT.gStyle.SetPadRightMargin(0.07)
    ROOT.gStyle.SetPadBottomMargin(0.15)
    ROOT.gStyle.SetPadLeftMargin(0.11)

    #set title offsets (for axis label)
    ROOT.gStyle.SetTitleXOffset(1.2)
    ROOT.gStyle.SetTitleYOffset(1.2)

    #use large fonts
    #font=72 # Helvetica italics
    font=42  # Helvetica
    tsize=0.05
    ROOT.gStyle.SetTextFont(font)

    ROOT.gStyle.SetTextSize(tsize)
    ROOT.gStyle.SetLabelFont(font,"x")
    ROOT.gStyle.SetTitleFont(font,"x")
    ROOT.gStyle.SetLabelFont(font,"y")
    ROOT.gStyle.SetTitleFont(font,"y")
    ROOT.gStyle.SetLabelFont(font,"z")
    ROOT.gStyle.SetTitleFont(font,"z")

    ROOT.gStyle.SetLabelSize(tsize,"x")
    ROOT.gStyle.SetTitleSize(tsize,"x")
    ROOT.gStyle.SetLabelSize(tsize,"y")
    ROOT.gStyle.SetTitleSize(tsize,"y")
    ROOT.gStyle.SetLabelSize(tsize,"z")
    ROOT.gStyle.SetTitleSize(tsize,"z")

    #use bold lines and markers
    ROOT.gStyle.SetMarkerStyle(20)
    ROOT.gStyle.SetMarkerSize(1.2)
    #gStyle.SetHistLineWidth(2)
    ROOT.gStyle.SetLineStyleString(2,"[12 12]") #postscript dashes

    #get rid of X error bars (as recommended in ATLAS figure guidelines)
    #gStyle.SetErrorX(0.0001)
    #get rid of error bar caps
    #gStyle.SetEndErrorSize(0.)

    #do not display any of the standard histogram decorations
    ROOT.gStyle.SetOptTitle(0)
    #gStyle.SetOptStat(1111)
    ROOT.gStyle.SetOptStat(0)
    #gStyle.SetOptFit(1111)
    #Style.SetOptFit(0)

    #put tick marks on top and RHS of plots
    ROOT.gStyle.SetPadTickX(1)
    ROOT.gStyle.SetPadTickY(1)
    ########## Style end ##########

def ATLASLabel(x, y, text, color=ROOT.kBlack):
    l = ROOT.TLatex() #l.SetTextAlign(12) l.SetTextSize(tsize)
    l.SetNDC()
    l.SetTextFont(72)
    l.SetTextColor(color)

    delx = 0.46*(0.4/x)*696*gPad.GetWh()/(472*gPad.GetWw())
    if (x<0.3):
        delx = 0.115*696*gPad.GetWh()/(472*gPad.GetWw())

    l.DrawLatex(x,y,"ATLAS")
    if (text):
        p = ROOT.TLatex()
        p.SetNDC()
        p.SetTextFont(42)
        p.SetTextColor(color)
        p.DrawLatex(x+delx,y,text)
        #p.DrawLatex(x,y,"#sqrt{s}=900GeV")

def energy_lumi(x,y,energy, lumi):
    tsize=0.04
    l=ROOT.TLatex()
    l.SetTextAlign(12)
    l.SetTextSize(tsize)
    l.SetNDC()
    l.SetTextColor(ROOT.kBlack)
    l.DrawLatex(x,y, "#sqrt{s}= %s TeV, #int L dt=%s fb^{-1}"%(energy,lumi))
    
    

def myText(x, y, color, text, tsize=0.05):
  l = ROOT.TLatex() #l.SetTextAlign(12);
  l.SetTextSize(tsize);
  l.SetNDC();
  l.SetTextColor(color);
  l.DrawLatex(x,y,text);



def myBoxText( x,  y, boxsize, mcolor,text):
  tsize = 0.06
        
  l = ROOT.TLatex()
  l.SetTextAlign(12); #l.SetTextSize(tsize);
  l.SetNDC();
  l.DrawLatex(x,y,text);

  y1=y-0.25*tsize
  y2=y+0.25*tsize
  x2=x-0.3*tsize;
  x1=x2-boxsize;
                        

  mbox= ROOT.TPave(x1,y1,x2,y2,0,"NDC")
                            
  mbox.SetFillColor(mcolor)
  mbox.SetFillStyle(1001);
  mbox.Draw()
                        
  mline = ROOT.TLine()
  mline.SetLineWidth(4)
  mline.SetLineColor(1)
  mline.SetLineStyle(1)
  y_new=(y1+y2)/2.
  mline.DrawLineNDC(x1,y_new,x2,y_new)



def myMarkerText( x, y, color, mstyle,text, msize):
  tsize=0.06;
  marker = ROOT.TMarker(x-(0.4*tsize),y,8)
  marker.SetMarkerColor(color);
  marker.SetNDC();
  marker.SetMarkerStyle(mstyle)
  marker.SetMarkerSize(msize)
  marker.Draw()

  l = ROOT.TLatex()
  l.SetTextAlign(12) #l.SetTextSize(tsize);
  l.SetNDC()
  l.DrawLatex(x,y,text);
