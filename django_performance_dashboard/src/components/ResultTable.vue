<template>
    <div class="border border-gray-200 rounded-lg overflow-hidden">
      <div class="bg-gray-50 p-3 border-b border-gray-200">
        <div class="flex justify-between items-center">
          <h4 class="font-semibold text-gray-700">{{ label }}</h4>
          <div
            v-if="duration > 0"
            :class="compare ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'"
            class="text-xs px-2 py-1 rounded-full font-medium"
          >
            {{ duration }}ms
          </div>
        </div>
      </div>
      <div class="p-3 max-h-60 overflow-auto">
        <div v-if="!results.length" class="text-gray-500 text-center py-4">
          No results yet
        </div>
        <div v-else>
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th
                  v-for="column in columns"
                  :key="column"
                  scope="col"
                  class="px-3 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  {{ formatFieldName(column) }}
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="(result, i) in results.slice(0, 3)" :key="i">
                <td
                  v-for="column in columns"
                  :key="`${label}-${i}-${column}`"
                  class="px-3 py-2 whitespace-nowrap text-sm text-gray-500"
                >
                  {{ getNestedValue(result, column) }}
                </td>
              </tr>
            </tbody>
          </table>
          <div v-if="results.length > 3" class="text-center text-sm text-gray-500 mt-2">
            Showing 3 of {{ results.length }} results
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ResultTable',
    props: {
      label: String,
      results: Array,
      duration: Number,
      compare: Boolean,
      columns: Array
    },
    methods: {
        formatFieldName(field) {
            return field
                .replace(/__/g, ' ')
                .replace(/\./g, ' ')
                .replace(/_/g, ' ')
                .replace(/\b\w/g, l => l.toUpperCase());
        },
        getNestedValue(obj, path) {
        // Support both dot notation and __ notation
            const parts = path.includes('.') ? path.split('.') : path.split('__');
            let value = obj;

            for (const part of parts) {
                if (value && typeof value === 'object' && part in value) {
                value = value[part];
                } else {
                return obj[path] !== undefined ? obj[path] : '-'; // fallback for flat key
                }
            }

            return value !== undefined && value !== null ? value : '-';
        }

    }
  };
  </script>
  
  <style scoped>
  </style>
  