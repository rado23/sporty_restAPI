import requests


def test_get_poem_by_title():
    """
    Test to verify fetching a poem by title.
    """
    url = "https://poetrydb.org/title/Ozymandias"
    response = requests.get(url)

    print(f"\n🔍 Debug Info: Response Status Code = {response.status_code}")
    print(f"🔍 Debug Info: Response Body = {response.text}")

    assert response.status_code == 200, "Expected HTTP 200 OK"

    data = response.json()
    assert len(data) > 0, "Expected at least one poem in response"

    first_poem = data[0]
    assert first_poem["title"] == "Ozymandias", f"Title does not match expected. Received: {first_poem}"

    # Print actual response content in case of failure
    assert len(first_poem["lines"]) > 0, f"Poem content should not be empty. Received: {first_poem}"


def test_get_poem_by_invalid_author():
    """
    Test to verify API handles non-existent authors correctly.
    """
    url = "https://poetrydb.org/author/UnknownAuthor"
    response = requests.get(url)

    print(f"\n🔍 Debug Info: Response Status Code = {response.status_code}")
    print(f"🔍 Debug Info: Response Body = {response.text}")

    assert response.status_code in [200, 404], "Expected HTTP 200 (empty list) or 404 (not found)"

    data = response.json()

    # API might return a 404 JSON message instead of an empty list
    if isinstance(data, dict):
        assert "status" in data and data["status"] == 404, f"Expected status 404, got {data}"
        assert "reason" in data and data["reason"] == "Not found", f"Expected 'Not found' reason, got {data}"
    else:
        assert isinstance(data, list), f"Expected response to be a list, but got: {data}"
        assert len(data) == 0, f"Expected an empty list for non-existent author, but got: {data}"


