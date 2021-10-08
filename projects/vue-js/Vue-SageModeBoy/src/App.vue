<template>
  <v-app style="background: #f5f5f5">
    <NavBar></NavBar>
    <v-main class="ma-4">
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import NavBar from '@/components/NavBar'

export default {
  name: "App",
  components: {
    NavBar
  },
  data: () => ({
    //
  }),
};
</script>
