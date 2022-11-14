<template>
  <div class="containter">
    <button type="button" class="btn btn-primary">{{ msg }}</button>
  </div>
</template>

<script>
import axios from 'axios';
// simple test to ensure data is being recieved from backend
export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // disable next line in eslint to eliminate errors
          // otherwise "npm remove @vue/cli-plugin-eslint"
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
