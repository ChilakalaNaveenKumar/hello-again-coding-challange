import time
import requests

API_ENDPOINTS = [
    ("Paginated Page 1", "http://127.0.0.1:8000/api/users/?page=1"),
    ("Full Response (100k)", "http://127.0.0.1:8000/api/users/?page_size=100000"),
    ("Search 'john'", "http://127.0.0.1:8000/api/users/?search=john"),
    ("Order by last_name", "http://127.0.0.1:8000/api/users/?ordering=last_name"),
    ("Full Response (No Pagination)", "http://127.0.0.1:8000/api/users-full/")
]

def benchmark(name, url):
    print(f"\nBenchmarking: {name}")
    start = time.time()
    try:
        response = requests.get(url)
        duration = time.time() - start
        data = response.json()
        if isinstance(data, dict) and "results" in data:
            results = data["results"]
        elif isinstance(data, list):
            results = data
        else:
            results = []
        print(f"Time: {duration:.3f}s | Records: {len(results)} | Status: {response.status_code}")
    except Exception as e:
        print(f"Error on {name}: {str(e)}")

if __name__ == "__main__":
    for name, url in API_ENDPOINTS:
        benchmark(name, url)
