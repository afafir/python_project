<template>
    <div class="home">
        <div style="min-height: 1px"></div>
        <div class="chat-wrapper mt-4 d-flex flex-row">
            <div class="chat-list mr-2">
                <div :class="{'chat-item': true, 'mb-2': true, 'clickable': true, 'active': active_chat.id === chat.id, 'justify-content-between': true, 'd-flex': true}" v-for="chat in chats" @click="active_chat = chat">
                    <span>{{chat.title}}</span>
                    <font-awesome-icon :icon="getChatIcon(chat)"/>
                </div>
            </div>
            <div class="messages-container flex-column">
                <div v-for="message in active_chat.messages" :class="{'d-flex': true, 'justify-content-between': true, 'mb-2': true, 'flex-row-reverse': !message.local}">
                    <span :class="{'message-item': true, 'local': message.local}">{{message.text}}</span>
                    <span style="font-size: 8pt">{{message.sent_at | dateParse('YYYY-MM-DDTHH:mm:ss') | dateFormat('DD.MM HH:mm')}}</span>
                </div>
                <div class="send-message">
                    <b-form @submit.prevent="sendMessage">
                        <b-form-input type="text" placeholder="Введите сообщение" v-model="text"></b-form-input>
                    </b-form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import {WEBSOCKET_URL} from "@/constants";
import ChatService from "@/services/chat.service";
import EventBus from "../../common/EventBus";

const CHAT_TYPE_MAPPING = {
    'TELEGRAM': ['fab', 'telegram'],
    'VK': ['fab', 'vk'],
    'EMAIL': ['fas', 'envelope']
}
export default {
    name: 'HomeView',
    data() {
        return {
            socket: null,
            text: '',
            messages: [],
            chats: [
                {
                    title: '',
                    messages: []
                }
            ],
            active_chat: {
                id: null,
                messages: []
            },
        }
    },
    mounted() {
        ChatService.getChats().then(
            resp => {this.chats = resp.data},
            error => {
                if (error.response && error.response.status === 401) {
                    EventBus.dispatch('logout');
                }
            }
        );
        let socket = new WebSocket(WEBSOCKET_URL);
        socket.onopen = (event) => {
            console.log('opened')
            console.log(event);
            this.sendJSON({
                type: 'auth.user',
                token: this.$store.state.auth.status.user['access']
            });
        }
        socket.onmessage = (event) => {
            let data = JSON.parse(event.data);
            console.log(data);
            console.log(this.chats.map(chat => chat.id))
            let chat = this.chats.find(chat => chat.id === data.message.chat_id)
            chat.messages.push(data.message)
        }
        socket.onerror = (event) => {
            console.log('error occurred')
            console.log(event)
        }
        socket.onclose = (event) => {
            console.log('closed')
            console.log(event)
        }
        this.socket = socket;

    },
    methods: {
        sendMessage() {
            if (!this.text) {
                return;
            }
            const data = {
                'text': this.text,
                'chat_id': this.active_chat.id,
            }
            this.sendJSON(data);
            this.text = ''
        },
        sendJSON(data) {
            this.socket.send(JSON.stringify(data))
        },
        getChatIcon(chat) {
            return CHAT_TYPE_MAPPING[chat.messenger];
        }
    },
    watch: {
        "active_chat.id": function (chat_id) {
            ChatService.getMessages(chat_id).then((resp) => {
                this.active_chat.messages = resp.data;
            })
        }
    }

};
</script>

<style scoped>
 .messages-container {
     background-color: #FFF;
     min-height: 800px;
     width: 100%;
     padding: 8px 4px;
 }
 .chat-list {
     width: 300px;
 }
 .chat-item {
     width: 100%;
     background-color: #f6fcf7;
     border: white 1px solid;
     border-radius: 16px;
     padding: 4px 24px;
 }
 .send-message {
     width: 50vw;
     position: absolute;
     bottom: 50px;
 }

 .message-item {
     background-color: #e5eeff;
     border-radius: 5px;
     padding: 4px 8px;
 }
 .message-item.local {
     background-color: #f7edff;
 }
 .clickable:hover {
     cursor: pointer;
 }
 .chat-item.active {
     background-color: #dcf3de;
 }
</style>
