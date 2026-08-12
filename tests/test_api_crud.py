import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts(request_context):
    response = request_context.get(f"{BASE_URL}/posts")
    print("GET Response JSON:", response.json()[:2])   
    assert response.ok
    assert response.status == 200       

def test_create_post(request_context):
    response = request_context.post(
        f"{BASE_URL}/posts",
        data={"title": "foo", "body": "bar", "userId": 1}
    )
    print("POST Response JSON:", response.json())
    assert response.ok
    assert response.status == 201      
    data = response.json()
    assert data["title"] == "foo"
    assert data["body"] == "bar"
    assert data["userId"] == 1

def test_update_post(request_context):
    response = request_context.put(
        f"{BASE_URL}/posts/1",
        data={"id": 1, "title": "updated title", "body": "updated body", "userId": 1}
    )
    print("PUT Response JSON:", response.json())
    assert response.ok
    assert response.status == 200        
    data = response.json()
    assert data["title"] == "updated title"
    assert data["body"] == "updated body"

def test_delete_post(request_context):
    response = request_context.delete(f"{BASE_URL}/posts/1")
    print("DELETE Response JSON:", response.text())
    assert response.ok
    assert response.status == 200       
