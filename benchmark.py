import time
import requests

API_ENDPOINTS = [
    ("Optimized - Paginated Page 1", "http://127.0.0.1:8000/api/optimized-users/?page=1"),
    ("Optimized - Filter Gender Male", "http://127.0.0.1:8000/api/optimized-users/?gender=M"),
    ("Optimized - Filter Customer ID", "http://127.0.0.1:8000/api/optimized-users/?customer_id=abc-123"),
    ("Optimized - Birthday After 1980", "http://127.0.0.1:8000/api/optimized-users/?birthday_after=1980-01-01"),
    ("Optimized - Birthday Between", "http://127.0.0.1:8000/api/optimized-users/?birthday_after=1980-01-01&birthday_before=2000-01-01"),
    ("Optimized - Filter City", "http://127.0.0.1:8000/api/optimized-users/?address__city=Berlin"),
    ("Optimized - Filter Country", "http://127.0.0.1:8000/api/optimized-users/?address__country=Germany"),
    ("Optimized - Points Greater Than 1000", "http://127.0.0.1:8000/api/optimized-users/?customerrelationship__points__gte=1000"),
    ("Optimized - Last Activity After 2023", "http://127.0.0.1:8000/api/optimized-users/?customerrelationship__last_activity_after=2023-01-01"),
    ("Optimized - Order by First Name", "http://127.0.0.1:8000/api/optimized-users/?ordering=first_name"),
    ("Optimized - Order by City", "http://127.0.0.1:8000/api/optimized-users/?ordering=address__city"),
    ("Optimized - Order by Points", "http://127.0.0.1:8000/api/optimized-users/?ordering=customerrelationship__points"),
    ("Unoptimized - Paginated Page 1", "http://127.0.0.1:8000/api/users/?page=1"),
    ("Unoptimized - Filter Gender Male", "http://127.0.0.1:8000/api/users/?gender=M"),
    ("Unoptimized - Filter Customer ID", "http://127.0.0.1:8000/api/users/?customer_id=abc-123"),
    ("Unoptimized - Filter Birthday", "http://127.0.0.1:8000/api/users/?birthday=2000-01-01"),
    ("Unoptimized - Filter City", "http://127.0.0.1:8000/api/users/?address__city=Berlin"),
    ("Unoptimized - Filter Country", "http://127.0.0.1:8000/api/users/?address__country=Germany"),
    ("Unoptimized - Filter Points", "http://127.0.0.1:8000/api/users/?customerrelationship__points=1000"),
    ("Unoptimized - Filter Last Activity", "http://127.0.0.1:8000/api/users/?customerrelationship__last_activity=2023-01-01"),
    ("Unoptimized - Order by First Name", "http://127.0.0.1:8000/api/users/?ordering=first_name"),
    ("Unoptimized - Order by City", "http://127.0.0.1:8000/api/users/?ordering=address__city"),
    ("Unoptimized - Order by Points", "http://127.0.0.1:8000/api/users/?ordering=customerrelationship__points"),
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
