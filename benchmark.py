import time
import requests

API_ENDPOINTS = [
    # Unoptimized View
    ("Unoptimized - Paginated Page 1", "http://127.0.0.1:8000/api/users/?page=1"),
    ("Unoptimized - Full Response (100k)", "http://127.0.0.1:8000/api/users/?page_size=100000"),
    ("Unoptimized - Search 'john'", "http://127.0.0.1:8000/api/users/?search=john"),
    
    # AppUser filters/sorting
    ("Unoptimized - Filter gender", "http://127.0.0.1:8000/api/users/?gender=M"),
    ("Unoptimized - Filter birthday", "http://127.0.0.1:8000/api/users/?birthday=2000-01-01"),
    ("Unoptimized - Filter customer_id", "http://127.0.0.1:8000/api/users/?customer_id=abc-123"),
    ("Unoptimized - Order by first_name", "http://127.0.0.1:8000/api/users/?ordering=first_name"),
    ("Unoptimized - Order by last_name", "http://127.0.0.1:8000/api/users/?ordering=last_name"),
    ("Unoptimized - Order by birthday", "http://127.0.0.1:8000/api/users/?ordering=birthday"),

    # Address filters/sorting
    ("Unoptimized - Filter address__city", "http://127.0.0.1:8000/api/users/?address__city=Berlin"),
    ("Unoptimized - Filter address__country", "http://127.0.0.1:8000/api/users/?address__country=Germany"),
    ("Unoptimized - Order by address__city", "http://127.0.0.1:8000/api/users/?ordering=address__city"),

    # CustomerRelationship filters/sorting
    ("Unoptimized - Filter customerrelationship__points", "http://127.0.0.1:8000/api/users/?customerrelationship__points=100"),
    ("Unoptimized - Order by customerrelationship__points", "http://127.0.0.1:8000/api/users/?ordering=customerrelationship__points"),

    # FullField View
    ("FullField - Paginated Page 1", "http://127.0.0.1:8000/api/users-full/?page=1"),
    ("FullField - Full Response (100k)", "http://127.0.0.1:8000/api/users-full/?page_size=100000"),
    ("FullField - Search 'john'", "http://127.0.0.1:8000/api/users-full/?search=john"),

    # AppUser filters/sorting
    ("FullField - Filter gender", "http://127.0.0.1:8000/api/users-full/?gender=M"),
    ("FullField - Filter birthday", "http://127.0.0.1:8000/api/users-full/?birthday=2000-01-01"),
    ("FullField - Filter customer_id", "http://127.0.0.1:8000/api/users-full/?customer_id=abc-123"),
    ("FullField - Order by first_name", "http://127.0.0.1:8000/api/users-full/?ordering=first_name"),
    ("FullField - Order by last_name", "http://127.0.0.1:8000/api/users-full/?ordering=last_name"),
    ("FullField - Order by birthday", "http://127.0.0.1:8000/api/users-full/?ordering=birthday"),

    # Address filters/sorting
    ("FullField - Filter address__city", "http://127.0.0.1:8000/api/users-full/?address__city=Berlin"),
    ("FullField - Filter address__country", "http://127.0.0.1:8000/api/users-full/?address__country=Germany"),
    ("FullField - Order by address__city", "http://127.0.0.1:8000/api/users-full/?ordering=address__city"),

    # CustomerRelationship filters/sorting
    ("FullField - Filter customerrelationship__points", "http://127.0.0.1:8000/api/users-full/?customerrelationship__points=100"),
    ("FullField - Order by customerrelationship__points", "http://127.0.0.1:8000/api/users-full/?ordering=customerrelationship__points"),

    # Optional: No pagination at all
    ("FullField - No Pagination", "http://127.0.0.1:8000/api/users-full/")
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
