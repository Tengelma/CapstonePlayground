<template>
  <div class="page-container">
    <md-app>
      <md-app-toolbar class="md-primary">
        <span class="md-title">Grapher</span>
      </md-app-toolbar>
      <md-app-content>
        <md-card>
          <md-card-content>
            <md-field>
              <label for="slope">slope</label>
              <md-input name="slope" id="slope" v-model="form.slope"/>
            </md-field>
            <md-field>
              <label for="y-intercept">y-intercept</label>
              <md-input name="y-intercept" id="y-intercept" v-model="form.yIntercept"/>
            </md-field>
            <md-button type="submit" class="md-primary" v-on:click="print">Render</md-button>
          </md-card-content>
        </md-card>
        <md-card>
          <md-card-header>
            {{equation}}
          </md-card-header>
          <md-card-content>
            <img alt="Vue logo" src="../assets/logo.png">
          </md-card-content>
        </md-card>    
      </md-app-content>
    </md-app>
  </div>
</template>

<style scoped>
  .md-card {
    width: 320px;
    height: 320px;
    margin: 4px;
    display: inline-block;
    vertical-align: top;
  }
</style>

<script>
  export default {
    name: 'Calculator',
    data: () => ({
      form: {
        yIntercept: 0,
        slope: 1
      },
       equation: "y = 1x + 0"
    }),
    methods: {
      print() {
        this.equation = "y = " + this.form.slope + "x" + " + " + this.form.yIntercept   
        console.log(this.equation)    
      }
    }
  }
</script>



