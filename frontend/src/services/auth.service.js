import axios from "axios";
import {API_URL} from "@/constants";
import TokenService from "@/services/token.service";

const AUTH_API_URL = API_URL + '/auth'
class AuthService {
    login({username, password}) {
        const formData = new FormData()
        formData.append('username', username)
        formData.append('password', password)
        const config = {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }
        return axios.post(AUTH_API_URL + '/token/', formData, config)
        .then(resp => {
            if (resp.data.access) {
                TokenService.setUser(resp.data)
            }
            return resp.data;
        });
    }

    logout() {
        TokenService.removeUser();
    }

    register(user) {
        return axios.post(AUTH_API_URL + '/register', {
            username: user.username,
            password: user.password,
            password1: user.password
        })
    }
}

export default new AuthService();
export const LOCAL_STORAGE_KEY = 'user';
