<template>
  <div class="projects">
    <h1 class="subtitle-1 grey--text text-uppercase">Projects</h1>

    <v-row justify="center">
      <v-col cols="8">
        <v-expansion-panels flat>
          <v-expansion-panel >
            <v-expansion-panel-header class="text-uppercase">{{project.title}}</v-expansion-panel-header>
            <v-expansion-panel-content class="px-3 grey--text">
              {{project.content}}
            <div class="text-right font-weight-bold">Due by {{project.due}}</div>  
            </v-expansion-panel-content>
            
          </v-expansion-panel>
        </v-expansion-panels>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  data: ()=>({
    project: {
        title: "back-end",
        person: "Sagemodeboy",
        due: "yesterday",
        status: "completed",
        content:
          "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ullam omnis asperiores laudantium aut natus adipisci excepturi! Consectetur iste modi ad, maiores, accusamus magnam quas exercitationem perferendis nam ab tempora illo.",
      },
  })
}
</script>