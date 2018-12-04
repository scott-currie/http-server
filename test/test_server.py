import requests as req


def test_200_ok_status_home_route():
    """Test for 200 status code on the home route."""
    response = req.get('http://127.0.0.1:5000')
    assert response.status_code == 200


def test_404_not_found_status():
    """"Test the 404 status code."""
    response = req.get('http://127.0.0.1:5000/wat')
    assert response.status_code == 400


def test_response_body_of_home_route():
    """Test the home route body."""
    response = req.get('http://127.0.0.1:5000')
    assert b'Welcome to our site' in response.content
