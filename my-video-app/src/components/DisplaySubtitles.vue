<template>
    <div>
      <h2>Display Subtitles</h2>
      <video ref="videoPlayer" controls @timeupdate="handleTimeUpdate">
        <source :src="videoUrl" type="video/mp4">
      </video>
      <div class="subtitles">
        <p v-for="subtitle in subtitles" :key="subtitle.timestamp">{{ subtitle.text }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import apiClient from '@/api';
  
  export default {
    name: 'DisplaySubtitles',
    props: ['videoUrl'],
    data() {
      return {
        subtitles: []
      };
    },
    methods: {
      handleTimeUpdate() {
        const currentTime = this.$refs.videoPlayer.currentTime;
        // Find the subtitle that matches the current time and update display
        // You need to implement this logic to synchronize subtitles with video playback
      }
    },
    created() {
      // Fetch subtitles data from the backend API
      apiClient.get('/get-subtitles')
        .then(response => {
          this.subtitles = response.data; // Update the component's data with subtitles
        })
        .catch(error => {
          // Handle error
        });
    }
  };
  </script>
  
  <style scoped>
  .subtitles {
    margin-top: 20px;
  }
  /* Add any other component-specific styles here */
  </style>
  