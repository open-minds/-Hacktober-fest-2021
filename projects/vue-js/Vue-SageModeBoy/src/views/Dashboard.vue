<template>
  <div class="home">
    <h1 class="subtitle-1 grey--text text-uppercase">Dashboard</h1>

    <v-row justify="center">
      <v-col cols="8">
        <v-row class="mb-3 ml-3">
          <v-tooltip top>
            <template v-slot:activator="{on, attrs}">
              <v-btn small text color="grey" @click="sortBy('title')" v-on="on" v-bind="attrs">
                <v-icon small left>mdi-folder</v-icon>
                <span class="caption text-lowercase">by title</span>
              </v-btn>
            </template>
            <span>Order by project title</span>
          </v-tooltip>

          <v-tooltip top>
            <template v-slot:activator="{on, attrs}">
              <v-btn small text color="grey" @click="sortBy('selected_team')" v-on="on" v-bind="attrs">
                <v-icon small left>mdi-account</v-icon>
                <span class="caption text-lowercase">by person</span>
              </v-btn>
            </template>
            <span>Order by person name</span>
          </v-tooltip>
        </v-row>
        <v-card class="px-3" v-for="project in projects" :key="project.id" flat>
          <v-row :class="`pa-3 project ${project.status}`">
            <v-col xs="12" md="6">
              <div class="caption grey--text">Project title</div>
              <div>{{project.title}}</div>
            </v-col>
            <v-col xs="6" sm="4" md="2">
              <div class="caption grey--text">Person</div>
              <div>{{project.selected_team[0]}}</div>
            </v-col>
            <v-col xs="6" sm="4" md="2">
              <div class="caption grey--text">Due date</div>
              <div>{{project.date}}</div>
            </v-col>
            <v-col xs="2" sm="4" md="2">
              <div class="text-right">
                <v-chip
                  small
                  :class="`caption white--text my-2 ${project.status}`"
                >{{project.status}}</v-chip>
              </div>
            </v-col>
          </v-row>
          <v-divider></v-divider>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from "axios";
import { bus } from "@/main";

export default {
  name: "Home",
  data: () => ({
    projects: [],
  }),
  methods: {
    sortBy(filter) {
      this.projects.sort((a, b) => (a[filter] < b[filter] ? -1 : 1));
    },
  },
  created() {
    bus.$on("refreshData", () => {
      axios
        .get("https://todo-sagemodeboy.firebaseio.com/projects.json")
        .then((response) => {
          for (let key in response.data) {
            var found = this.projects.some((el) => el.id === key);
            if (!found) {
              this.projects.push({
                ...response.data[key],
                id: key,
              });
            }
          }
        });
    });
    axios
      .get("https://todo-sagemodeboy.firebaseio.com/projects.json")
      .then((response) => {
        for (let key in response.data) {
          this.projects.push({
            ...response.data[key],
            id: key,
          });
        }
      });
  },
};
</script>

<style>
.project.completed {
  border-left: 4px solid #3cd1c1;
}
.project.pending {
  border-left: 4px solid tomato;
}
.project.ongoing {
  border-left: 4px solid orange;
}

.v-chip.completed {
  background: #3cd1c1 !important;
}

.v-chip.pending {
  background: tomato !important;
}

.v-chip.ongoing {
  background: orange !important;
}
</style>