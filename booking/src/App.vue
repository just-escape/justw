<template>
  <div id="app">
    <div style="font-size: 42px; color: white; font-family: 'Big noodle'" @click="click">Ceci est le futur module de paiement ({{counter}})</div>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      counter: 0,
    }
  },
  methods: {
    click() {
      this.counter++
    }
  }
}
</script>

<style>
</style>
