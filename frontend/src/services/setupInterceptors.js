import axiosInstance from "./api";
import TokenService from "./token.service";
import axios from "axios";
import {API_URL} from "@/constants";

const setup = (store) => {
    axiosInstance.interceptors.request.use(
        (config) => {
            const token = TokenService.getLocalAccessToken();
            if (token) {
                config.headers["Authorization"] = 'Bearer ' + token;  // for Spring Boot back-end
            }
            return config;
        },
        (error) => {
            return Promise.reject(error);
        }
    );

    axiosInstance.interceptors.response.use(
        (res) => {
            return res;
        },
        async (err) => {
            const originalConfig = err.config;
            if (originalConfig.url !== "/auth/token/" && err.response) {
                // Access Token was expired
                if (err.response.status === 401 && !originalConfig._retry) {
                    originalConfig._retry = true;

                    try {
                        const rs = await axios.post(API_URL + "/auth/token/refresh/", {
                            refresh: TokenService.getLocalRefreshToken(),
                        });
                        console.log(rs)
                        const { access, refresh } = rs.data;

                        store.dispatch('auth/refreshToken', access);
                        TokenService.updateLocalAccessToken(access);
                        TokenService.updateLocalRefreshToken(refresh);
                        return axiosInstance(originalConfig);
                    } catch (_error) {
                        console.log('error!!!')
                        console.log(_error)
                        return Promise.reject(_error);
                    }
                }
            }

            return Promise.reject(err);
        }
    );
};

export default setup;
