import os
import sys
import yaml

class SetConfig:
    def __init__(self, fname: str):
        with open(fname, "r") as f:
            args = yaml.safe_load(f)
            self.amino_train_path = args["amino_train_path"]
            self.amino_test_path = args["amino_test_path"]
            self.family_info_path = args["family_info_path"]
            self.aaindex1_path = args["aaindex1_path"]

            self.output_path = args["output_path"]
            self.coordinates_path = self.path_join(dnames=[self.output_path, "coordinates"])
            
    def path_join(self, dnames: list) -> str:
        dname = ""
        print(dnames)
        for name in dnames:
            if not dname:
                dname = name 
                continue 
            dname = os.path.join(dname, name)
            self.make_path(dname)
            print(dname)
        return dname
        
    def make_path(self, dname):
        if not os.path.exists(dname): 
            os.mkdir(dname)
        return dname

        
