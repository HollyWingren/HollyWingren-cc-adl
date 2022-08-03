import servicex as sx
from func_adl_servicex import ServiceXSourceUpROOT


class Q1Suite:
    
    timeout = 3600 
    
    def setup(self):
        dataset_name = ["root://eospublic.cern.ch//eos/root-eos/benchmark/Run2012B_SingleMu.root"]
        sx_dataset = sx.ServiceXDataset(dataset_name, "uproot", ignore_cache=True)
        self.ds = ServiceXSourceUpROOT(sx_dataset, "Events")

    def time_servicex_q1(self):
        missing_ET = self.ds.Select(lambda event: event.MET_pt).AsAwkwardArray().value()

    def peakmem_servicex_q1(self):
        missing_ET = self.ds.Select(lambda event: event.MET_pt).AsAwkwardArray().value()
