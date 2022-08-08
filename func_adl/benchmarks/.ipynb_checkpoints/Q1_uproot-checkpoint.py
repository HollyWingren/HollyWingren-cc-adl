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
    def time_pt_all_jets(self):
        jet_pT = self.ds.SelectMany(lambda event: event.Jet_pt).value()
    def peakmem_pt_all_jets(self):
        jet_pT = self.ds.SelectMany(lambda event: event.Jet_pt).value()
    def time_met_two_jets_under_1(self):
        filtered_jet_pT = self.ds.SelectMany(lambda event: {'pT': event.Jet_pt, 'eta': event.Jet_eta}.Zip()
                                              .Where(lambda jet: abs(jet.eta) < 1)
                                              .Select(lambda jet: jet.pT)).value()
    def peakmem_met_two_jets_under_1(self):
        filtered_jet_pT = self.ds.SelectMany(lambda event: {'pT': event.Jet_pt, 'eta': event.Jet_eta}.Zip()
                                              .Where(lambda jet: abs(jet.eta) < 1)
                                              .Select(lambda jet: jet.pT)).value()
    def time_met_two_jets_over_40(self):
        filtered_missing_ET_4 = self.ds.Where(lambda event: event.Jet_pt.Where(lambda pT: pT > 40).Count() >= 2)\
                          .Select(lambda event: event.MET_pt).value()
    def peakmem_met_two_jets_over_40(self):
        filtered_missing_ET_4 = self.ds.Where(lambda event: event.Jet_pt.Where(lambda pT: pT > 40).Count() >= 2)\
                          .Select(lambda event: event.MET_pt).value()
    def time_opposite_charge_60_to_120_GeV(self):
        filtered_missing_ET_5 = self.ds.Where(lambda event: Zip({'p4': Zip({'pt':   event.Muon_pt,
                                                               'eta':  event.Muon_eta,
                                                               'phi':  event.Muon_phi,
                                                               'mass': event.Muon_mass}).ToFourMomenta(),
                                                    'charge': event.Muon_charge})
                                               .Choose(2)
                                               .Where(lambda pair: pair[0].charge * pair[1].charge < 0)
                                               .Select(lambda pair: (pair[0].p4 + pair[1].p4).mass)
                                               .Where(lambda mass: 60 < mass and mass < 120)
                                               .Count() > 0
                                ).Select(lambda event: event.MET_pt).value()
    def peakmem_opposite_charge_60_to_120_GeV(self):
        filtered_missing_ET_5 = self.ds.Where(lambda event: Zip({'p4': Zip({'pt':   event.Muon_pt,
                                                               'eta':  event.Muon_eta,
                                                               'phi':  event.Muon_phi,
                                                               'mass': event.Muon_mass}).ToFourMomenta(),
                                                    'charge': event.Muon_charge})
                                               .Choose(2)
                                               .Where(lambda pair: pair[0].charge * pair[1].charge < 0)
                                               .Select(lambda pair: (pair[0].p4 + pair[1].p4).mass)
                                               .Where(lambda mass: 60 < mass and mass < 120)
                                               .Count() > 0
                                ).Select(lambda event: event.MET_pt).value()
    def time_trijet_four_momentum_over_3(self):
        best_trijet_pt_6 = self.ds.Where(lambda event: event.nJet >= 3)\
                     .Select(lambda event: {'pt': event.Jet_pt,
                                            'eta': event.Jet_eta,
                                            'phi': event.Jet_phi,
                                            'mass': event.Jet_mass}.Zip().ToFourMomenta()
                                           .Choose(3)
                                           .Select(lambda triplet: triplet[0] + triplet[1] + triplet[2])
                                           .OrderBy(lambda trijet: abs(trijet.m - 172.5))
                                           .First()
                                           .Select(lambda best_trijet: best_trijet.pt)).value()
    def peakmem_trijet_four_momentum_over_3(self):
        best_trijet_pt_6 = self.ds.Where(lambda event: event.nJet >= 3)\
                     .Select(lambda event: {'pt': event.Jet_pt,
                                            'eta': event.Jet_eta,
                                            'phi': event.Jet_phi,
                                            'mass': event.Jet_mass}.Zip().ToFourMomenta()
                                           .Choose(3)
                                           .Select(lambda triplet: triplet[0] + triplet[1] + triplet[2])
                                           .OrderBy(lambda trijet: abs(trijet.m - 172.5))
                                           .First()
                                           .Select(lambda best_trijet: best_trijet.pt)).value()