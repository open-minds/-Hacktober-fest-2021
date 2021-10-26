<template>
  <div class="teams">
    <h1 class="subtitle-1 grey--text text-uppercase">Teams page</h1>

    <v-row justify="center" class="my-5">
      <v-col cols="8" xs="12" sm="6" md="4" lg="3" v-for="member in team" :key="member.name">
        <v-card flat class="text-center">
          <v-responsive class="pt-4">
            <v-avatar size="100" class="ma-4 grey lighten-2">
              <img :src="member.avatar">
            </v-avatar>
          </v-responsive>
          <v-card-text>
            <div class="subtitle-2">{{member.name}}</div>
            <div class="grey--text text-uppercase">{{member.role}}</div>
          </v-card-text>
          <v-card-actions>
             <v-btn text color="primary">
              <v-icon left small >mdi-send</v-icon>
              <span class="caption">Invite</span>
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn text color="grey">
              <v-icon left small >mdi-message</v-icon>
              <span class="caption">Message</span>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  data: () => ({
    team: [
      {
        name: "Sagemodeboy",
        role: "backend developer",
        avatar:"/sagemode.jfif"
      },
      {
        name: "Zakiuchiha",
        role: "frontend developer",
        avatar:"/zaki.jfif"
      },
      {
        name: "MohammedChapeau",
        role: "database admin",
        avatar:"/moh.jfif"
      },
      {
        name: "AeroD",
        role: "Dev-ops specialist",
        avatar:"/aerod.png"
      },
    ],
  }),
};
</script>

<style>
</style>