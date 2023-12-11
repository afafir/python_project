import {API_URL} from "@/constants"
import api from "@/services/api";

const USER_API_URL = API_URL + '/users';
class UserService {
    getUserData() {
        return api.get(USER_API_URL + '/me')
    }
}

export default new UserService();
