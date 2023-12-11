<template>
    <div class="chat-wrapper mt-4 d-flex flex-row">
        <div class="chat-list mr-2">
            <div class="chat-item mb-2">
                <span></span>
            </div>
            <div class="chat-item mb-2">
                <span>Test Test</span>
            </div>
        </div>
        <div class="messages-container flex-column">
            <div v-for="message in messages" :class="{'d-flex': true, 'justify-content-between': true, 'mb-2': true, 'flex-row-reverse': !message.local}">
                <span class="message-item">{{message.text}}</span>
                <span style="font-size: 8pt">{{message.sent_at}}</span>
            </div>
            <div class="send-message">
                <b-form @submit.prevent="sendMessage">
                    <b-form-input type="text" placeholder="Введите сообщение" v-model="text"></b-form-input>
                </b-form>
            </div>
        </div>
    </div>
</template>

<script>

</script>
