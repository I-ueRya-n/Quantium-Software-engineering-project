import pytest
from my_dash_app import app
from dash.testing import wait_for

@pytest.fixture
def dash_app():
    yield app

def test_header_presence(dash_app):
    dash_duo = dash_app.server
    assert dash_duo.find_element('h1').text == 'Soul Foods Sales Visualizer'

def test_visualization_presence(dash_app):
    dash_duo = dash_app.server
    assert dash_duo.find_element('svg') is not None

def test_region_picker_presence(dash_app):
    dash_duo = dash_app.server
    assert dash_duo.find_element('input[type="radio"]') is not None
