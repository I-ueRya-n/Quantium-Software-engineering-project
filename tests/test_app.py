import pytest
from dash.testing.application_runners import import_app
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def dash_app(dash_duo):
    # Manually install and use the correct ChromeDriver version
    service = Service(ChromeDriverManager().install())
    dash_duo.driver = webdriver.Chrome(service=service)

    app = import_app("data.app")  # Ensure correct import path
    dash_duo.start_server(app)

    return dash_duo

# Test 1: Check if the header is present
def test_header_exists(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsel Sales Visualizer"

# Test 2: Check if the graph (visualization) is present
def test_graph_exists(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    graph = dash_duo.find_element("#sales-graph")
    assert graph is not None

# Test 3: Check if the region picker (radio buttons) is present
def test_region_picker_exists(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    radio_buttons = dash_duo.find_element("#region-selector")
    assert radio_buttons is not None
