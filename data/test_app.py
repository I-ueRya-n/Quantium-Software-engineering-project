import pytest
from selenium.webdriver.common.by import By
import dash.testing.wait as wait
from dash.testing.application_runners import import_app

def test_header_presence(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    # Check for header presence by text
    header = dash_duo.find_element("h1")
    assert header.text == "Sales Visualizer for Soul Foods", "The header should be present and correct."


def test_visualisation_presence(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    # Check for the presence of the Plotly graph
    wait.until(
        lambda: dash_duo.find_element("#sales-line-chart"),
        timeout=30,
    ),
    assert dash_duo.find_element("#sales-line-chart"),"The visualization should be present."

@pytest.mark.parametrize("path", ["app"])
def test_region_picker_presence(dash_duo, path):
    # Import the Dash application
    app = import_app(path)
    
    # Start the server with the application
    dash_duo.start_server(app)
    
    # Wait until the page is completely loaded
    dash_duo.wait_for_page(timeout=10)
    
    # Search region selector by ID
    region_selector = dash_duo.find_element("#region-selector")
    
    # Check if the region selector is present
    assert region_selector, "The region picker should be present."