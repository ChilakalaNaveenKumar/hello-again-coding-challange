<template>
    <div class="animate-spin h-5 w-5 text-blue-600 border-blue-200 border-4 border-t-transparent rounded-full"></div>
  </template>
  
  <script>
  export default {
    name: 'Spinner',
  };
  </script>
  
  <style scoped>
  .animate-spin {
    border-style: solid;
    border-radius: 9999px;
    border-right-color: transparent;
  }
  </style>
  