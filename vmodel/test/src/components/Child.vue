<template>
  <div>
    <input v-model="my_model.a"/>
    <input v-model="my_model.b"/>
  </div>
</template>

<script>
export default {
  name: 'Child',
  model: {
    event: 'onChange',
    prop: 'model',
  },
  data() {
    return { my_model: { ...this.model } };
  },
  updated() {
    this.$emit('onChange', this.my_model);
  },
}
</script>