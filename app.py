# test_app.py

import pytest
from dash import Dash
from dash import html, dcc
from dash.testing import DashR

# Import your Dash app from the module
from Quantium import app  # replace 'your_dash_app' with the name of your file

@pytest.fixture
def dash_app():
    """Fixture to create a Dash app instance for testing."""
    app.testing = True
    yield app

def test_header_is_present(dash_app):
    """Test that the header is present in the app."""
    # Use Dash testing to simulate a client
    app_client = DashR(dash_app)
    
    # Start the app client
    app_client.start()
    
    # Check if header is present
    header = app_client.find_element('h1')
    assert header.text == 'Pink Morsel Sales Dashboard'

def test_visualization_is_present(dash_app):
    """Test that the visualization is present in the app."""
    app_client = DashR(dash_app)
    app_client.start()
    
    # Check if the graph is present
    graph = app_client.find_element('#sales-graph')
    assert graph is not None  # Check if the graph element exists

def test_region_picker_is_present(dash_app):
    """Test that the region picker is present in the app."""
    app_client = DashR(dash_app)
    app_client.start()
    
    # Check if the region selector is present
    region_picker = app_client.find_element('#region-selector')
    assert region_picker is not None  # Check if the region selector exists

if __name__ == "__main__":
    pytest.main()

