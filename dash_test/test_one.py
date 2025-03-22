from dash.testing.application_runners import import_app

def test_app(dash_duo):
    app = import_app("dash_test.app")
    dash_duo.start_server(app)
    
    # make sure header present
    assert dash_duo.find_element("h1").text == 'Data visualisation on the sales of the Pink Morsels' 
    
    # make sure chart present
    assert dash_duo.find_element('#filtered-sales-chart') != None
    
    # make sure selection present
    assert dash_duo.find_element("#radio_buttons") != None

    # make sure no error in browser console
    assert dash_duo.get_logs() == [], "Browser console should contain no error"
    
    return None