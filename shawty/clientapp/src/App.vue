<template>
  <div id="app-root">This is a component! Here's {{ adjective }} message!</div>
</template>

<script lang="ts">
import Vue from 'vue';
import Component from 'vue-class-component';

@Component({})
export default class App extends Vue {
    get adjective() : string {
        return "a blah";
    }
};
</script>

