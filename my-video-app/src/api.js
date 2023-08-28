import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://your-backend-api-url' // Replace with your backend API URL
});

export default apiClient;
