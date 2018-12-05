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


def test_do_post_msg_in_response_body():
    """Make a post request to /cow and look for the message in the response body."""
    data = {'msg': 'hello'}
    response = req.post('http://127.0.0.1:5000/cow', params=data)
    assert b'hello' in response.content


def test_do_post_msg_response_201():
    """Make a good post request to /cow and check status code is 201."""
    data = {'msg': 'hello'}
    response = req.post('http://127.0.0.1:5000/cow', params=data)
    assert response.status_code == 201


def test_do_post_no_data_returns_400():
    """Make a POST request to /cow with no data and expect status code 400."""
    response = req.post('http://127.0.0.1:5000/cow')
    assert response.status_code == 400


def test_do_post_invalid_route_returns_404():
    """Make a POST request to nonexistent route and expect status code 404."""
    response = req.post('http://127.0.0.1:5000/fake')
    assert response.status_code == 404
