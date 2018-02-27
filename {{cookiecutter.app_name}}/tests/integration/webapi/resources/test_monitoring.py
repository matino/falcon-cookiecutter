class TestPing:

    def test_returns_pong_response(self, webapi):
        response = webapi.get('/v1/alert/ping')
        assert response.status_code == 200
        assert response.body == b'pong'
