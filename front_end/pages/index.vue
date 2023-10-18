<template>
    <div>
      <p>Tag 12 Value: {{ tag12 }}</p>
      <p>Data: {{ data }}</p>
    </div>
  </template>
  
  <script>
  import { io } from 'socket.io-client';
  
  export default {
    data() {
      return {
        tag12: null,
        data: null
      };
    },
    mounted() {
      const socket = io('http://127.0.0.1:5000');
      socket.on('after connect', (details) => {
        this.tag12 = details.tag12;
        this.data = details.data;
      });
    }
  };
  </script>