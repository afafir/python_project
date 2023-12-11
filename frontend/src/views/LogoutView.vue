<template>
    <div>
      <div class="text-center pt-4">
        <h1>Вы уверены, что хотите выйти?</h1>
        <b-button variant="danger" @click.prevent="handleLogout">Выйти</b-button>
      </div>
    </div>
</template>

<script>
  export default {
      name: 'LogoutView',
      methods: {
          handleLogout() {
              this.$store.dispatch('auth/logout').then(() => {
                  this.$router.push({name: 'login'})
              })
          }
      }
  }
</script>
<style scoped>

</style>
