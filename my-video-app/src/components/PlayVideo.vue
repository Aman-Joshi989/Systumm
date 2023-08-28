<template>
    <div>
      <h2>Play Video</h2>
      <video ref="videoPlayer" controls>
        <source :src="videoUrl" type="video/mp4">
      </video>
    </div>
  </template>
  
  <script>
  export default {
    name: 'PlayVideo',
    props: ['videoUrl']
  };
  </script>
  
  <style scoped>
  /* Add any component-specific styles here */
  </style>
  