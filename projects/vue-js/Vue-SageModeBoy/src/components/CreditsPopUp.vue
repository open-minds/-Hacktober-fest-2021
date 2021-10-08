<template>
  <v-dialog max-width="600" v-model="dialog">
    <template v-slot:activator="{on,attrs}">
      <v-btn depressed color="primary text-uppercase" v-on="on" v-bind="attrs">
        <span>Credits</span>
      </v-btn>
    </template>
    <v-card flat>
      <v-card-title
        class="headline white--text text-uppercase text-center primary"
      >Made by Jetlight studio</v-card-title>
      <v-card-text class="mt-3 text-subtitle-1 font-weight-bold">
        This software was created by the awesome team <span class="primary--text">@Jetlight_Studio</span> with
        <v-icon color="error">mdi-cards-heart</v-icon>
      </v-card-text>
      <v-divider></v-divider>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text color="primary" @click="dialog = false">Contact us</v-btn>
        <v-btn text  @click="dialog = false">Close</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  data: () => ({
    dialog: false,
  }),
};
</script>

<style>
</style>