<template>
  <child :model="model" v-model="model"/>
</template>

<script>
import Child from './Child.vue';

export default {
  name: 'Parent',
  data: () => ({
    model: 
      {
        a: 4,
        b: 5,
      },
  }),
  components: {
    Child,
  },
  watch: {
    model: {
      deep: true,
      handler() {
        console.log( this.model );
      }
    }
  },
}
</script>