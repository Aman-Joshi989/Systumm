import Vue from 'vue';
import VueRouter from 'vue-router';

import UploadVideo from './components/UploadVideo.vue';
import AddSubtitles from './components/AddSubtitles.vue';
import PlayVideo from './components/PlayVideo.vue';
import DisplaySubtitles from './components/DisplaySubtitles.vue';


Vue.use(VueRouter);

const routes = [
  { path: '/upload', component: UploadVideo },
  { path: '/add-subtitles', component: AddSubtitles },
  { path: '/play-video', component: PlayVideo },
  { path: '/display-subtitles', component: DisplaySubtitles },
  { path: '/', redirect: '/upload' } // Default redirect to /upload
];

const router = new VueRouter({
  routes
});

export default router;
