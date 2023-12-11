import {API_URL} from "@/constants";
import api from "@/services/api";

const CHAT_API_URL = API_URL + '/messaging'
class ChatService {
    getChats() {
        return api.get(CHAT_API_URL + '/chats')
    }

    getMessages(chat_id) {
        return api.get(
            CHAT_API_URL + '/messages',
            {
                params: {chat_id: chat_id}
            }
        )
    }
}

export default new ChatService();
