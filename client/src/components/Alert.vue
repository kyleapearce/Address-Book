<template>
    <div>
        <b-alert variant="success" show>{{ message }}</b-alert>
        <br>
    </div>
</template>

<script>
// alert component to be used to display different messages at top of screen
export default {
    props: ['message'],
};
</script>