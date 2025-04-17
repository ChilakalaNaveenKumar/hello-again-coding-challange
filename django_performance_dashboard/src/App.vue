<template>
  <div class="min-h-screen bg-gray-100">
    <header class="bg-blue-600 text-white shadow-md">
      <div class="max-w-7xl mx-auto py-4 px-4 sm:px-6 lg:px-8">
        <h1 class="text-2xl font-bold">Django Benchmark Dashboard</h1>
      </div>
    </header>
    <main>
      <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <ApiBenchmarkDashboard />
      </div>
    </main>
  </div>
</template>

<script>
import ApiBenchmarkDashboard from './components/ApiDashboard.vue'

export default {
  name: 'App',
  components: {
    ApiBenchmarkDashboard
  }
}
</script>