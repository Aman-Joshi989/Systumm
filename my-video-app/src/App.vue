<template>
  <div id="app">
    <header>
      <nav>
        <router-link to="/">Upload Video</router-link>
        <router-link to="/add-subtitles">Add Subtitles</router-link>
        <router-link to="/play-video">Play Video</router-link>
        <router-link to="/display-subtitles">Display Subtitles</router-link>
      </nav>
    </header>

    <main>
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style>
/* Your global styles go here */
</style>
