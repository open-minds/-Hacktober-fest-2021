<template>
  <nav>
    <v-snackbar v-model="snackbar" rounded="pill" top :timeout="4000" color="success">
      Project added successfully! 
      <template v-slot:action="attrs"> 
        <v-btn v-bind="attrs" text color="white" @click="snackbar = false">Close</v-btn>
      </template>
    </v-snackbar>
    <v-app-bar flat app>
      <v-app-bar-nav-icon class="grey--text" @click="drawer=!drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="text-uppercase grey--text">
        <span class="font-weight-light">Todo</span>
        <span>SageModeBoy</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>

      <v-menu offset-y>
        <template v-slot:activator="{on,attrs}">
          <v-btn color="grey" text v-bind="attrs" v-on="on">
            <v-icon>mdi-chevron-down</v-icon>
            <span>Menu</span>
          </v-btn>
        </template>
        <v-list>
          <v-list-item v-for="item in menu_items" :key="item.title">
            <v-icon left>{{item.icon}}</v-icon>
            <v-list-item-title>{{item.title}}</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-row justify="center">
              <CreditsPopUp></CreditsPopUp>
            </v-row>
          </v-list-item>
        </v-list>
      </v-menu>

      <v-btn text color="grey">
        <span>Sign out</span>
        <v-icon color="grey" right>mdi-exit-to-app</v-icon>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app class="primary">
      <v-row class="mt-5 text-center" justify="center">
        <v-col cols="6">
          <v-avatar size="100">
            <img src="/sagemode.jfif" />
          </v-avatar>
          <div class="white--text text-button mt-2">SageModeBoy</div>
        </v-col>
      </v-row>
      <v-row justify="center" class="mb-3">
        
      <Popup @projectAdded="snackbar = true"></Popup>
      </v-row>
      <v-list>
        <v-list-item v-for="(link, index) in links" :key="index" router :to="link.route">
          <v-list-item-action>
            <v-icon color="white">{{link.icon}}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title class="white--text">{{link.text}}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </nav>
</template>

<script>
import Popup from "@/components/Popup.vue"
import CreditsPopUp from "@/components/CreditsPopUp.vue"

export default {
  data: () => ({
    drawer: false,
    snackbar: false,
    links: [
      { icon: "mdi-view-dashboard", text: "Dashboard", route: "/" },
      { icon: "mdi-folder", text: "My projects", route: "/projects" },
      { icon: "mdi-account", text: "Team", route: "/team" },
    ],
    menu_items: [
      { title: "Send feedback", icon: "mdi-comment" },
      { title: "Import projects", icon: "mdi-application-import" },
      { title: "Export projects", icon: "mdi-application-export" },
      { title: "New team", icon: "mdi-account-multiple-plus" },
      ],
  }),
  components: {
    Popup, CreditsPopUp
  }
};
</script>

<style>
</style>