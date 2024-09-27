import numpy as np
import pytest
from fastapi.testclient import TestClient
from app.ml_model import predict
from app.main import app

client = TestClient(app)

@pytest.mark.parametrize("features, result", [([42] * 7, np.ndarray)])
def test_predict_input_type_good(features, result):
    pred = predict(features)
    assert type(pred) == result

@pytest.mark.parametrize("features, result", [(42, Exception),
                                              ("42", Exception),
                                              (-42, Exception),
                                              (0.42, Exception),
                                              ((42, ) * 7, Exception),
                                              ([42] * 5, Exception)])
def test_predict_input_type_bad(features, result):
    with pytest.raises(result):
        predict(features)

@pytest.mark.parametrize("features", [([42] * 7),
                                      ([-42] * 7),
                                      ([0] * 7),
                                      ([0.42] * 7)])
def test_predict_output_type_good(features):
    pred = predict(features)
    assert type(pred) == np.ndarray

@pytest.mark.parametrize("user_id, result", [({"user_id": 1}, 200)])
def test_root_input_type_good(user_id, result):
    response = client.post("/get_predict", json=user_id)
    assert response.status_code == result

@pytest.mark.parametrize("user_id, result", [({"user_id": 0}, 402),
                                             ({"user_id": -1}, 402),
                                             ({"user_id": -0.42}, 402),
                                             ({"user_id": 0.42}, 402),
                                             (42, 402),
                                             (-0.42, 402),
                                             ("42", 402)])
def test_root_input_type_bad(user_id, result):
    response = client.post("/get_predict", json=user_id)
    assert response.status_code == result