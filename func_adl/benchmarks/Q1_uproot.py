from func_adl_uproot import UprootDataset
import os


class Q1Suite:
    
    timeout = 3600 
    
    def setup(self):
        self.ds = UprootDataset('https://raw.githubusercontent.com/masonproffitt/func-adl-demo/master/Run2012B_SingleMu_10000.root', 'Events')

    def time_servicex_q1(self):
        missing_ET_query = self.ds.Select(lambda event: event.MET_pt).value()

    def peakmem_servicex_q1(self):
        missing_ET_query = self.ds.Select(lambda event: event.MET_pt).value()
