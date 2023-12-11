<template>
    <div class="row justify-content-center">
        <div class="col-4">
            <b-form @submit.prevent="handleLogin">
                <b-form-group label="Логин" label-for="username">
                    <b-form-input name="username" id="username" placeholder="Введите логин..." v-model="user.username" required>
                    </b-form-input>
                </b-form-group>
                <b-form-group label="Пароль" label-for="password">
                    <b-form-input id="password" type="password" name="password" placeholder="Введите пароль..." v-model="user.password" required>

                    </b-form-input>
                </b-form-group>
                <div v-if="message" class="alert alert-danger" role="alert">{{message}}</div>
                <div class="text-center">
                    <b-button pill variant="primary" type="submit">Войти</b-button>
                </div>
            </b-form>
        </div>
    </div>
</template>

<script>
    import User from "@/models/user";

    export default {
        name: 'LoginView',
        data() {
            return {
                user: new User('', ''),
                loading: false,
                message: ''
            }
        },
        computed: {
            loggedIn() {
                return this.$store.state.auth.status.loggedIn
            }
        },
        created() {
            if (this.loggedIn) {
                this.$router.push({name: 'home'})
            }
        },
        methods: {
            handleLogin() {
                this.loading = true;
                this.$store.dispatch('auth/login', this.user).then(
                    () => {
                        let to;
                        if (this.$route.query.next) {
                            to = this.$route.query.next;
                        } else {
                            to = {name: 'home'}
                        }
                        this.$router.push(to)
                    },
                    () => {
                        this.loading = false;
                        this.message = 'Логин или пароль неверны'
                    }
                );
            }
        }
    }
</script>
<style scoped>

</style>
