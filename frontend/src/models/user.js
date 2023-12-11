export default class User {
    constructor(username = '', password = '', loggedIn = false) {
        this.username = username;
        this.password = password;
        this.loggedIn = loggedIn;
    }
}
