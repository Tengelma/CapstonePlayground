import os
import tempfile
import pytest
import re
import server
from server import get_x, get_y, create_fig, serialize_fig
import numpy as np

@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    with server.app.test_client() as client:
        yield client

def test_get_x():
    test = np.array([0,1,2,3,4])
    assert np.array_equal(get_x(5), test)

def test_get_y():
    test_x = np.array([0,1,2,3,4])
    test_y = np.array([5 * x + 3 for x in test_x])
    assert np.array_equal(test_y, get_y(test_x, 5, 3))

def test_create_fig():
    test_x = np.array([0,1,2,3,4])
    test_y = np.array([5 * x + 3 for x in test_x])
    create_fig(test_x, test_y)
    os.path.exists("./temp/temp.png")

def test_serialize_fig():
    string = serialize_fig()
    assert is_base_64(string)

def test_graph(client):
    req = graph(client, 3, 5)
    assert(is_base_64(req.json["image"]))


def graph(client, slope, y_intercept):
    return client.post('/graph', json={"slope": slope, "yIntercept": y_intercept})

def is_base_64(s: str):
    pattern = re.compile("^b'[a-zA-Z0-9+/]*={0,3}'$")
    return pattern.match(s)




 
