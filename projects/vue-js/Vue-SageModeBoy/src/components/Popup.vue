<template>
  <v-dialog max-width="600" v-model="dialog">
    <template v-slot:activator="{on,attrs}">
      <v-btn depressed color="success text-uppercase" v-on="on" v-bind="attrs">
        <v-icon left>mdi-plus</v-icon>
        <span>Add new project</span>
      </v-btn>
    </template>
    <v-card flat>
      <v-card-title
        class="headline white--text text-uppercase text-center primary"
      >Made by Jetlight studio</v-card-title>
      <v-card-text class="mt-3">
        <v-form v-model="valid_form" class="px-3">
          <v-text-field
            v-model="project.title"
            label="Title"
            :rules="inputRules"
            hint="This is the title of your new project"
            prepend-icon="mdi-folder"
          ></v-text-field>
          <v-textarea
            v-model="project.content"
            label="information"
            :rules="inputRules"
            hint="This includes any details about the new project"
            rows="3"
            prepend-icon="mdi-lead-pencil"
          ></v-textarea>
          <v-row>
            <v-col cols="6">
              <v-menu offset-y>
                <template v-slot:activator="{on,attrs}">
                  <v-text-field
                    v-model="project.date"
                    v-on="on"
                    v-bind="attrs"
                    label="Date"
                    :rules="inputRules"
                    hint="This is the due date of the new project"
                    prepend-icon="mdi-calendar"
                  ></v-text-field>
                </template>
                <v-date-picker no-title v-model="project.date"></v-date-picker>
              </v-menu>
            </v-col>
            <v-col cols="6">
              <v-select
                :items="['ongoing', 'pending', 'completed']"
                v-model="project.status"
                label="Select status"
                prepend-icon="mdi-clipboard-list-outline"
              ></v-select>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-select
                :items="team"
                v-model="project.selected_team"
                chips
                multiple
                label="Select team"
                prepend-icon="mdi-account-multiple"
              ></v-select>
            </v-col>
          </v-row>
        </v-form>
      </v-card-text>
      <v-divider></v-divider>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          :disabled="!valid_form"
          text
          color="primary"
          @click="submit"
          :loading="uploading"
        >Create</v-btn>
        <v-btn text @click="dialog = false">Cancel</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from "axios";
import {bus} from "@/main.js"

export default {
  data: () => ({
    dialog: false,
    uploading: false,
    project: {
      title: "",
      content: "",
      date: new Date().toISOString().substr(0, 10),
      selected_team: [],
      status: "ongoing",
    },
    team: ["Sagemodeboy", "Zakiuchiha", "MohammedChapeau", "AeroD"],
    inputRules: [
      (v) => v.length >= 3 || "Value must have at least 3 characters",
    ],
    valid_form: false,
  }),
  methods: {
    submit() {
      this.uploading = true;
      axios
        .post(
          "https://todo-sagemodeboy.firebaseio.com/projects.json",
          this.project
        )
        .then(() => {
          this.uploading = false;
          this.dialog = false;
          this.$emit('projectAdded');
          bus.$emit('refreshData');
        });
    },
  },
};
</script>

<style>
</style>