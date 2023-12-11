<template>
  <div id="app">
      <div>
          <b-navbar toggleable="lg" type="dark" variant="primary">
              <b-navbar-brand :to="{name: 'home'}">Главная</b-navbar-brand>

              <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

              <b-collapse id="nav-collapse" is-nav>
<!--                  <b-navbar-nav>-->
<!--                      <b-nav-item href="#">Link</b-nav-item>-->
<!--                      <b-nav-item href="#" disabled>Disabled</b-nav-item>-->
<!--                  </b-navbar-nav>-->

                  <!-- Right aligned nav items -->
                  <b-navbar-nav class="ml-auto">
<!--                      <b-nav-form>-->
<!--                          <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>-->
<!--                          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>-->
<!--                      </b-nav-form>-->

<!--                      <b-nav-item-dropdown text="Lang" right>-->
<!--                          <b-dropdown-item href="#">EN</b-dropdown-item>-->
<!--                          <b-dropdown-item href="#">ES</b-dropdown-item>-->
<!--                          <b-dropdown-item href="#">RU</b-dropdown-item>-->
<!--                          <b-dropdown-item href="#">FA</b-dropdown-item>-->
<!--                      </b-nav-item-dropdown>-->
                      <b-nav-item-dropdown right v-if="$store.state.auth.status.loggedIn">
                          <!-- Using 'button-content' slot -->
                          <template #button-content>
                              <em>{{ $store.state.auth.status.user.first_name }} {{$store.state.auth.status.user.last_name}}</em>
                          </template>
                          <b-dropdown-item href="#">Профиль</b-dropdown-item>
                          <b-dropdown-item :to="{name: 'logout'}">Выйти</b-dropdown-item>
                      </b-nav-item-dropdown>
                      <b-nav-item :to="{name: 'login'}" v-else>Войти</b-nav-item>
                  </b-navbar-nav>
              </b-collapse>
          </b-navbar>
      </div>
      <div id="content-wrapper" class="container">
          <router-view :key="$route.path"/>
      </div>
  </div>
</template>

<script>
import EventBus from "../common/EventBus";

export default {
    methods: {
        logout() {
            this.$store.dispatch('auth/logout');
            this.$router.push({name: 'login'});
        }
    },
    mounted() {
        EventBus.on('logout', () => {
            this.logout();
        })
    },
    beforeDestroy() {
        EventBus.remove('logout');
    }
}
</script>
<style scoped>
#content-wrapper {
    background-color: #f0f8ff;
    min-height: 80vh;
}
</style>

