import arcpy
import pythonaddins

class button1(object):
    """Implementation for test_addin_addin.button1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.MessageBox("Click Event...","Title for MessageBox",0)
