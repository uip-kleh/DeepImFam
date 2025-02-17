import yaml

class SecConfig:
    def __init__(self, fname):
        with open(fname, "r") as f:
            args = yaml.safe_load(f)

            self.train_data_fname = args["train_data_fname"]
            self.test_data_fname = args["test_data_fname"]