import numpy as np
import matplotlib.pyplot as plt
import hist

import awkward as ak   # version 1
import vector
import wget
import ssl
vector.register_awkward()


class HZZSuite:
    
    timeout = 3600 
    
    def setup(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        file_name = wget.download("https://raw.githubusercontent.com/jpivarski-talks/2022-08-03-codas-hep-columnar-tutorial/main/data/SMHiggsToZZTo4L.parquet", "SMHiggsToZZTo4L.parquet")
        raw_data = ak.from_parquet(file_name)
        {field_name: raw_data[field_name].type for field_name in raw_data.fields}
        self.events = ak.zip({
    "PV": ak.zip({
        "x": raw_data["PV_x"],
        "y": raw_data["PV_y"],
        "z": raw_data["PV_z"],
    }, with_name="Vector3D"),
    "muons": ak.zip({
        "pt": raw_data["Muon_pt"],
        "phi": raw_data["Muon_phi"],
        "eta": raw_data["Muon_eta"],
        "mass": raw_data["Muon_mass"],
        "charge": raw_data["Muon_charge"],
        "pfRelIso03": raw_data["Muon_pfRelIso03_all"],
        "pfRelIso04": raw_data["Muon_pfRelIso04_all"],
    }, with_name="Momentum4D"),
    "electrons": ak.zip({
        "pt": raw_data["Electron_pt"],
        "phi": raw_data["Electron_phi"],
        "eta": raw_data["Electron_eta"],
        "mass": raw_data["Electron_mass"],
        "charge": raw_data["Electron_charge"],
        "pfRelIso03": raw_data["Electron_pfRelIso03_all"],
    }, with_name="Momentum4D"),
    "MET": ak.zip({
        "pt": raw_data["MET_pt"],
        "phi": raw_data["MET_phi"],
    }, with_name="Momentum2D"),
}, depth_limit=1)


    def time_servicex_q1(self):
        first_muons, second_muons = (
    self.events.muons[ak.num(self.events.muons) >= 2, 0],
    self.events.muons[ak.num(self.events.muons) >= 2, 1],
        )
        hist.Hist.new.Regular(100, 0, 150).Double().fill((first_muons + second_muons).mass).plot();

    def peakmem_servicex_q1(self):
        first_muons, second_muons = (
    self.events.muons[ak.num(self.events.muons) >= 2, 0],
    self.events.muons[ak.num(self.events.muons) >= 2, 1],
        )
        hist.Hist.new.Regular(100, 0, 150).Double().fill((first_muons + second_muons).mass).plot();

