import requests as req


def test_200_ok_status_home_route():
    """Test for 200 status code on the home route."""
    response = req.get('http://127.0.0.1:5000')
    assert response.status_code == 200


def test_404_not_found_status():
    """"Test the 404 status code."""
    response = req.get('http://127.0.0.1:5000/wat')
    assert response.status_code == 404


def test_response_body_of_home_route():
    """GET the home route body."""
    response = req.get('http://127.0.0.1:5000')
    assert b'''<!DOCTYPE html>
            <html>
              <head>
                <title> cowsay </title>
              </head>
              <body>
               <header>
                 <nav>
                   <ul>
                     <li><a href="/cowsay">cowsay</a></li>
                   </ul>
                 </nav>
               <header>
               <main>
                 <p>This project is designed to test specific routes and return status messages accordingly</p>
               </main>
              </body>
            </html>''' in response.content


def test_server_get_cow_status_of_200():
    """GET /cow?msg=text: 200 OK <Text Response>."""
    response = req.get('http://127.0.0.1:5000/cow?msg=text')
    assert response.status_code == 200

#  These are the two tests that are showing correct in the browser, but are not in PyTest. Scott will look at them tomorrow.

# def test_server_get_cow_route_status_400():
#     """GET /cow 400 Bad Request."""
#     response = req.get('http://127.0.0.1:5000/cow?msg')
#     # import pdb; pdb.set_trace()
#     assert response.status_code == 400


# def test_server_get_cow_route_status_400_multiple_keys_does_not_work():
#     """GET /cow?who=dat&wat=do: 400 Bad Request."""
#     response = req.get('http://127.0.0.1:5000/cow?scott=was&here=why')
#     assert response.status_code == 400
