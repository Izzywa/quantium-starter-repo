from dash.testing.application_runners import import_app

def test_app(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    
    # make sure header present
    dash_duo.wait_for_element("#header", timeout=10)
    assert dash_duo.find_element("h1").text == 'Data visualisation on the sales of the Pink Morsels' 
    
    # make sure chart present
    dash_duo.wait_for_element("#filtered-sales-chart", timeout=10)
    assert dash_duo.find_element('#filtered-sales-chart') != None
    
    # make sure selection present
    dash_duo.wait_for_element("#radio_buttons", timeout=10)
    assert dash_duo.find_element("#radio_buttons") != None

    # make sure no error in browser consike
    assert dash_duo.get_logs() == [], "Browser console should contain no error"
    
    return None