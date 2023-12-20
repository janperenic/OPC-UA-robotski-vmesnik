<template>
  <div>
    <p>Alarm code value: {{ last_alarm_code }}</p>
    <p>Data: {{ data }}</p>
  </div>
</template>

<script>
import { io } from 'socket.io-client';

export default {
  data() {
    return {
      last_alarm_code: null,
      data: null
    };
  },
  mounted() {
    const socket = io('http://127.0.0.1:5000');
    setInterval(function() {
    socket.emit('time');
    }, 1) 
    socket.on('after connect', (details) => {
      this.last_alarm_code = details.last_alarm_code;
      this.data = details.data;
      console.log(details.last_alarm_code);
    });
  }
};
</script>
