<template>
    <div>
      <h2>Upload Video</h2>
      <div class="upload-container">
        <input type="file" @change="handleFileChange" accept="video/*">
        <button @click="uploadVideo">Upload</button>
      </div>
    </div>
  </template>
  
  <script>
  import apiClient from '@/api'; // Import the apiClient
  
  export default {
    name: 'UploadVideo',
    data() {
      return {
        selectedVideoFile: null // Initialize selectedVideoFile
      };
    },
    methods: {
      handleFileChange(event) {
        this.selectedVideoFile = event.target.files[0]; // Set selected video file
      },
      uploadVideo() {
        const formData = new FormData();
        formData.append('video', this.selectedVideoFile); // Use the selected video file
        apiClient.post('/upload-video', formData)
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
  .upload-container {
    margin-top: 20px;
  }
  /* Add any other component-specific styles here */
  </style>
  