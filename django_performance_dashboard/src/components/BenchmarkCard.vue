<template>
    <div class="bg-white rounded-lg shadow-md overflow-hidden">
      <div class="bg-blue-600 p-4">
        <h2 class="text-lg font-bold text-white">{{ benchmark.title }}</h2>
        <p class="text-blue-100 text-sm mt-1 truncate">{{ benchmark.optimizedUrl }}</p>
      </div>
      <div class="p-4 space-y-4">
        <div class="flex justify-center">
          <button
            @click="$emit('run', index)"
            class="bg-blue-600 text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-blue-700"
            :disabled="benchmark.loading"
          >
            <span v-if="benchmark.loading" class="flex items-center">
              <Spinner />
              Running Benchmark...
            </span>
            <span v-else>Run Benchmark</span>
          </button>
        </div>
  
        <ResultTable
          label="Optimized"
          :duration="benchmark.optimizedDuration"
          :results="benchmark.optimizedResults"
          :compare="benchmark.optimizedDuration < benchmark.unoptimizedDuration"
          :columns="optimizedResultColumns"
        />
  
        <ResultTable
          label="Unoptimized"
          :duration="benchmark.unoptimizedDuration"
          :results="benchmark.unoptimizedResults"
          :compare="benchmark.unoptimizedDuration < benchmark.optimizedDuration"
          :columns="unoptimizedResultColumns"
        />
  
        <div v-if="benchmark.optimizedDuration > 0 && benchmark.unoptimizedDuration > 0" class="border border-gray-200 rounded-lg overflow-hidden">
          <div class="bg-gray-50 p-3 border-b border-gray-200">
            <h4 class="font-semibold text-gray-700">Performance Comparison</h4>
          </div>
          <div class="p-3 flex justify-between text-sm">
            <div>
              <div class="font-medium text-gray-700">Improvement:</div>
              <div :class="getImprovementColor">{{ improvementPercent }}%</div>
            </div>
            <div>
              <div class="font-medium text-gray-700">Time Saved:</div>
              <div :class="getImprovementColor">{{ timeSaved }}ms</div>
            </div>
            <div>
              <div class="font-medium text-gray-700">Results:</div>
              <div class="text-gray-700 font-bold">{{ benchmark.optimizedResults.length }} / {{ benchmark.unoptimizedResults.length }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import ResultTable from './ResultTable.vue';
  import Spinner from './Spinner.vue';
  
  export default {
    name: 'BenchmarkCard',
    components: { ResultTable },
    props: {
      benchmark: Object,
      index: Number,
      unoptimizedResultColumns: Array,
      optimizedResultColumns: Array
    },
    computed: {
      improvementPercent() {
        const { optimizedDuration, unoptimizedDuration } = this.benchmark;
        return Math.round(((unoptimizedDuration - optimizedDuration) / unoptimizedDuration) * 100);
      },
      timeSaved() {
        return Math.abs(this.benchmark.unoptimizedDuration - this.benchmark.optimizedDuration);
      },
      getImprovementColor() {
        return this.improvementPercent > 0 ? 'text-green-600' : this.improvementPercent < 0 ? 'text-red-600' : 'text-gray-600';
      }
    }
  };
  </script>
  
  <style scoped>
  </style>
  