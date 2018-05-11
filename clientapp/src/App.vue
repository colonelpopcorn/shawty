<template>
  <div id="app-root">This is a component! Here's {{ adjective }} message!</div>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
    computed:{
        adjective() : String {
            return "a blah";            
        }

    }
  
})
</script>

