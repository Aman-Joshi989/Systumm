<template>
    <div>
      <h2>Add Subtitles</h2>
      <div class="form-container">
        <label for="timestamp">Timestamp:</label>
        <input type="text" v-model="timestamp">
        <label for="subtitle">Subtitle Text:</label>
        <textarea v-model="subtitle"></textarea>
        <button @click="addSubtitle">Add Subtitle</button>
      </div>
    </div>
  </template>
  
  <script>
  import apiClient from '@/api'; // Import the apiClient
  
  export default {
    name: 'AddSubtitles',
    data() {
      return {
        timestamp: '',
        subtitle: ''
      };
    },
    methods: {
      addSubtitle() {
        const subtitleData = {
          timestamp: this.timestamp,
          text: this.subtitle
        };
        apiClient.post('/add-subtitle', subtitleData)
          .then(response => {
            // Handle success, possibly display a success message
          })
          .catch(error => {
            // Handle error, possibly display an error message
          });
      }
    }
  };
  </script>
  
  <style scoped>
  .form-container {
    margin-top: 20px;
  }
  /* Add any other component-specific styles here */
  </style>
  