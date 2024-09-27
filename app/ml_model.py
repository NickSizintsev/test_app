import numpy as np
import os

def predict(features: list) -> np.ndarray | None:
    # with open("config.yml", "r") as file:
    #     config = yaml.safe_load(file)
    # np.random.seed(config["seed"])

    if not isinstance(features, list):
        raise Exception
    if len(features) != 7:
        raise CustomException(message="Need 7 features")
    # if not features:
    #     raise CustomException(message="ID not in table")
    return np.random.rand(7)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print(ROOT_DIR)
print(os.path.join(ROOT_DIR, 'requirements.txt'))