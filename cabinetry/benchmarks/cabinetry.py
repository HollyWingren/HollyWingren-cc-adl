import cabinetry

class Q1Suite:
    
    def setup(self):
        self.cabinetry_config = {
            'General': {'Measurement': 'minimal_example',
                        'POI': 'Signal_norm',
                        'HistogramFolder': 'histograms/',
                        'InputPath': '{SamplePath}'},
            'Regions': [{'Name': 'Signal_region',
                         'Variable': 'jet_pt',
                         'Filter': 'lep_charge > 0',
                         'Binning': [200, 300, 400, 500, 600]}],
            'Samples': [{'Name': 'Data',
                         'Tree': 'pseudodata',
                         'SamplePath': 'https://raw.githubusercontent.com/cabinetry/cabinetry-tutorials/master/inputs/data.root',
                         'Data': True},
                        {'Name': 'Signal',
                         'Tree': 'signal',
                         'SamplePath': 'https://raw.githubusercontent.com/cabinetry/cabinetry-tutorials/master/inputs/prediction.root',
                         'Weight': 'weight'},
                        {'Name': 'Background',
                         'Tree': 'background',
                         'SamplePath': 'https://raw.githubusercontent.com/cabinetry/cabinetry-tutorials/master/inputs/prediction.root',
                         'Weight': 'weight'}],
            'Systematics': [{'Name': 'Luminosity',
                             'Up': {'Normalization': 0.05},
                             'Down': {'Normalization': -0.05},
                             'Type': 'Normalization'},
                            {'Name': 'Modeling',
                             'Up': {'SamplePath': 'https://raw.githubusercontent.com/cabinetry/cabinetry-tutorials/master/inputs/prediction.root', 'Tree': 'background_varied'},
                             'Down': {'Symmetrize': True},
                             'Samples': 'Background',
                             'Type': 'NormPlusShape'},
                            {'Name': 'WeightBasedModeling',
                             'Up': {'Weight': 'weight_up'},
                             'Down': {'Weight': '0.7*weight'},
                             'Samples': 'Background',
                             'Type': 'NormPlusShape'}],
            'NormFactors': [{'Name': 'Signal_norm',
                             'Samples': 'Signal',
                             'Nominal': 1,
                             'Bounds': [0, 10]}]
            }

    def time_build_template(self):
        cabinetry.templates.build(self.cabinetry_config, method="uproot")

    def time_build_template(self):
        cabinetry.templates.build(self.cabinetry_config, method="uproot")

