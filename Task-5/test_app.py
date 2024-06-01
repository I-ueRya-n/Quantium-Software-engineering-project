import pytest
from dash.testing.application_runners import import_app

# Import the Dash app from app.py
from app import app

@pytest.fixture
def dash_duo(dash_duo):
    dash_duo.start_server(app)
    return dash_duo

def test_header_present(dash_duo):
    header = dash_duo.find_element('h1')
    assert header is not None
    assert header.text == "Sales Data Visualization"

def test_visualisation_present(dash_duo):
    time_series = dash_duo.find_element('#sales-time-series')
    distribution = dash_duo.find_element('#sales-distribution')
    assert time_series is not None
    assert distribution is not None

def test_region_picker_present(dash_duo):
    region_picker = dash_duo.find_element('#region-radio')
    assert region_picker is not None
