# hello-again-coding-challange

## Backend Optimization: List & Search APIs

This project compares optimized vs unoptimized Django REST API queries with a Vue.js dashboard visualizing their performance.

## Getting Started

### 1. Clone the project
```bash
git clone https://github.com/your-username/hello-again-coding-challange.git
cd hello-again-coding-challange
```

### 2. Run Backend & Frontend

Use the provided script to setup the environment, populate data (if missing), and launch both servers:

```bash
chmod +x run_all.sh
./run_all.sh
```
> Note It takes `20-30 min` to load `3 million data`, so please bear with it

- This will:
  - Set up Python virtualenv
  - Install backend dependencies
  - Run Django migrations
  - Generate fake data if not present (which usually takes 20-30 min if not data found)
  - Start Django backend server
  - Load `nvm` (if available)
  - Start the Vue frontend dashboard from `django_performance_dashboard`

> Note: The backend runs on `http://127.0.0.1:8000`, and the frontend runs on `http://localhost:5173`

## Vue Dashboard Features

- View and compare response time for different types of queries:
  - Pagination
  - Filtering (gender, birthday, city, country, points, etc.)
  - Ordering
  - Complex queries
- Side-by-side results comparison (first 3 rows per API)
- Performance improvement calculation

## Tech Stack
- **Backend**: Django, DRF, Faker
- **Frontend**: Vue 3, TailwindCSS, Vite
- **Database**: SQLite (default)
