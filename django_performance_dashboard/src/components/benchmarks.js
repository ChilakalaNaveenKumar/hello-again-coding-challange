export const benchmarks = [
    {
      title: "Paginated Results (Page 1)",
      optimizedUrl: "/api/optimized-users/?page=1",
      unoptimizedUrl: "/api/users/?page=1",
      loading: false,
      optimizedResults: [],
      unoptimizedResults: [],
      optimizedDuration: 0,
      unoptimizedDuration: 0
    },
    {
      title: "Filter Gender (Male)",
      optimizedUrl: "/api/optimized-users/?gender=M",
      unoptimizedUrl: "/api/users/?gender=M",
      loading: false,
      optimizedResults: [],
      unoptimizedResults: [],
      optimizedDuration: 0,
      unoptimizedDuration: 0
    },
    {
      title: "Filter Customer ID",
      optimizedUrl: "/api/optimized-users/?customer_id=c5b3d2a8-2c9e-482b-ba14-8b03ac88f5ea",
      unoptimizedUrl: "/api/users/?customer_id=c5b3d2a8-2c9e-482b-ba14-8b03ac88f5ea",
      loading: false,
      optimizedResults: [],
      unoptimizedResults: [],
      optimizedDuration: 0,
      unoptimizedDuration: 0
    },
    {
      title: "Filter Birthday Range",
      optimizedUrl: "/api/optimized-users/?birthday_after=1980-01-01&birthday_before=2000-01-01",
      unoptimizedUrl: "/api/users/?birthday_after=1980-01-01&birthday_before=2000-01-01",
      loading: false,
      optimizedResults: [],
      unoptimizedResults: [],
      optimizedDuration: 0,
      unoptimizedDuration: 0
    },
    {
      title: "Filter City (Welchport)",
      optimizedUrl: "/api/optimized-users/?address__city=Welchport",
      unoptimizedUrl: "/api/users/?address__city=Welchport",
      loading: false,
      optimizedResults: [],
      unoptimizedResults: [],
      optimizedDuration: 0,
      unoptimizedDuration: 0
    },
    {
      title: "Filter Country (Germany)",
      optimizedUrl: "/api/optimized-users/?address__country=Germany",
      unoptimizedUrl: "/api/users/?address__country=Germany",
      loading: false,
      optimizedResults: [],
      unoptimizedResults: [],
      optimizedDuration: 0,
      unoptimizedDuration: 0
    },
    {
      title: "Filter Points (≥ 1000)",
      optimizedUrl: "/api/optimized-users/?customerrelationship__points__gte=1000",
      unoptimizedUrl: "/api/users/?customerrelationship__points__gte=1000",
      loading: false,
      optimizedResults: [],
      unoptimizedResults: [],
      optimizedDuration: 0,
      unoptimizedDuration: 0
    },
    {
      title: "Filter Activity (After 2025-04-16)",
      optimizedUrl: "/api/optimized-users/?customerrelationships__last_activity_before=2025-04-16",
      unoptimizedUrl: "/api/users/?customerrelationships__last_activity_before=2025-04-16",
      loading: false,
      optimizedResults: [],
      unoptimizedResults: [],
      optimizedDuration: 0,
      unoptimizedDuration: 0
    },
    {
      title: "Order by First Name",
      optimizedUrl: "/api/optimized-users/?ordering=first_name",
      unoptimizedUrl: "/api/users/?ordering=first_name",
      loading: false,
      optimizedResults: [],
      unoptimizedResults: [],
      optimizedDuration: 0,
      unoptimizedDuration: 0
    },
    {
      title: "Order by City",
      optimizedUrl: "/api/optimized-users/?ordering=address__city",
      unoptimizedUrl: "/api/users/?ordering=address__city",
      loading: false,
      optimizedResults: [],
      unoptimizedResults: [],
      optimizedDuration: 0,
      unoptimizedDuration: 0
    },
    {
      title: "Order by Points",
      optimizedUrl: "/api/optimized-users/?ordering=customerrelationship__points",
      unoptimizedUrl: "/api/users/?ordering=customerrelationship__points",
      loading: false,
      optimizedResults: [],
      unoptimizedResults: [],
      optimizedDuration: 0,
      unoptimizedDuration: 0
    },
    {
      title: "Complex Query",
      optimizedUrl: "/api/optimized-users/?gender=O&address__country=Iraq&ordering=-customerrelationship__points",
      unoptimizedUrl: "/api/users/?gender=O&address__country=Iraq&ordering=-customerrelationship__points",
      loading: false,
      optimizedResults: [],
      unoptimizedResults: [],
      optimizedDuration: 0,
      unoptimizedDuration: 0
    }
  ];