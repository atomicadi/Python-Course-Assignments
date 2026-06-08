from app import app


def test_home_page():

    tester = app.test_client()

    response = tester.get("/")

    assert response.status_code == 200


def test_calculation():

    tester = app.test_client()

    response = tester.post(
        "/",
        data={
            "mass": "5",
            "temperature": "300",
            "volume": "1"
        }
    )

    assert response.status_code == 200
