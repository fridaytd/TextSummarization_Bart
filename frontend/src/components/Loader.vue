<script setup>
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/css/index.css';
import {ref} from 'vue'
defineProps(['isActive'])
</script>

<template>
    <loading :active="isActive" :can-cancel="false" :s-full-page="true" />
</template>

<style scoped></style>
