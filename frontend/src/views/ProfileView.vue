<template>
  <div>

  </div>
</template>

<script>
  import UserService from "@/services/user.service";

  export default {
      name: 'ProfileView',
      data() {
        return {
            user: {
                username: this.$store.state.auth.status.user.username,
                password: '',
                password1: ''
            }
        }
      },
      methods: {
          getData() {
              UserService.getUserData().then(
                  resp => {
                    this.user.username = resp.data.username;
                  },
                  error => {

                  }
              )
          },
          updateData() {

          }
      }
  }
</script>

<style scoped>

</style>
