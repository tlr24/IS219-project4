"""Testing our song management"""

def test_retrieve_song(client, add_user, write_test_csv):
    """Test viewing an uploaded song"""
    # login to be able to upload a csv
    client.post("/login", data={'email': 'a@a.com', 'password': '123La!'})

    file = open("music.csv", 'rb')
    # upload the csv
    client.post('/songs/upload', data={'file': file})

    # assert that we get the song's information on it's view page
    response = client.get('api/song/1')
    assert b"Song Information" in response.data
    assert b"Title: Move" in response.data
    assert b"Artist: TobyMac" in response.data

    # assert that our spotify api worked
    # if it was able to get the track id with the api, it should have loaded the embedded iframe element
    assert b"iframe" in response.data