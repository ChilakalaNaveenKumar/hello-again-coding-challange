<template>
  <div class="min-h-screen bg-gray-100 p-6">
    <div class="max-w-7xl mx-auto">
      <DashboardHeader />
      <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
        <BenchmarkCard
          v-for="(benchmark, index) in benchmarks"
          :key="index"
          :benchmark="benchmark"
          :index="index"
          :optimized-result-columns="optimizedResultColumns"
          :unoptimized-result-columns="unoptimizedResultColumns"
          @run="fetchBenchmarkResults"
        />
      </div>
    </div>
  </div>
</template>

<script>
import DashboardHeader from './DashboardHeader.vue';
import BenchmarkCard from './BenchmarkCard.vue';
import { benchmarks as initialBenchmarks } from './benchmarks';

export default {
  name: 'ApiBenchmarkDashboard',
  components: {
    DashboardHeader,
    BenchmarkCard
  },
  data() {
    return {
      baseUrl: 'http://127.0.0.1:8000',
      optimizedResultColumns: [
        'id', 'customer_id', 'first_name', 'last_name', 'gender',
        'address_city', 'address_country', 'points'
      ],
      unoptimizedResultColumns: [
        'id',
        'customer_id',
        'first_name',
        'last_name',
        'gender',
        'address.city',
        'address.country',
        'customerrelationships.points'
      ],
      benchmarks: initialBenchmarks
    };
  },
  methods: {
    async fetchBenchmarkResults(index) {
      const benchmark = this.benchmarks[index];
      benchmark.loading = true;
      try {
        const startOpt = performance.now();
        const resOpt = await fetch(`${this.baseUrl}${benchmark.optimizedUrl}`);
        const dataOpt = await resOpt.json();
        benchmark.optimizedDuration = Math.round(performance.now() - startOpt);
        benchmark.optimizedResults = dataOpt.results || dataOpt || [];

        const startUnopt = performance.now();
        const resUnopt = await fetch(`${this.baseUrl}${benchmark.unoptimizedUrl}`);
        const dataUnopt = await resUnopt.json();
        benchmark.unoptimizedDuration = Math.round(performance.now() - startUnopt);
        benchmark.unoptimizedResults = dataUnopt.results || dataUnopt || [];
      } catch (e) {
        console.error('Benchmark fetch failed', e);
      } finally {
        benchmark.loading = false;
      }
    }
  },
  mounted() {
    this.benchmarks.forEach((_, index) => this.fetchBenchmarkResults(index));
  }
}
</script>

<style scoped>
</style>
