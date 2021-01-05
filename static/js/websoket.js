const roomName = JSON.parse(document.getElementById('room-name').textContent);

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);
let chatLog = document.getElementById("chat-log");
const nowDate = new Date();
const nowHour = nowDate.getHours()
const nowMin = nowDate.getMinutes()
chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    // const newErement = document.createElement('p');

    if (data.is_todo == false) {
        // newErement.textContent = `${data.username}:${data.message}`;
        const newErement = `
        <div class="message_container">
        <div class="user_icon">
            <img src="/static/images/user_icon.jpg" alt="user_icon">
        </div>
        <div class="message_content">
            <div class="message_head">
                <span class="message_user_name">
                ${data.username}
                </span>
                <span class="message_create_at">${nowHour}:${nowMin}</span>
            </div>
            <div class="message_body">
            ${data.message}
            </div>
        </div>
    </div>
        `
        chatLog.insertAdjacentHTML('beforeend', newErement);
        chatLog = document.getElementById("chat-log");
        chatLog.scrollTop = chatLog.scrollHeight;

    } else if (data.is_todo == true) {
        console.log(data.message);
        // newErement = `${data.create_user}:${data.what}:${data.how_much}:${data.by_when}:${data.punishment}`;

        const newErement = `
        <div class="message_todo">
        <div class="message_todo-container">
            <div class="todo_create_user">
                <span>${data.message.create_user}</span>
                は
            </div>
            <div class=todo_body>
                <div class="todo_what">
                    <span>${data.message.what}</span>
                    を
                </div>
                <div class="todo_by_when">
                    <span>${data.message.by_when}</span>
                    までに
                </div>
                <div class="todo_how_much">
                    <span>${data.message.how_much}</span>
                    個
                </div>
            </div>
            <div class="todo_punishment">
                出来なければ、
                <span>${data.message.punishment}</span>
            </div>
        </div>
        </div> `;
        chatLog.insertAdjacentHTML('beforeend', newErement);
        chatLog = document.getElementById("chat-log");
        chatLog.scrollTop = chatLog.scrollHeight;
    }
};

chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function (e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function (e) {

    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;

    chatSocket.send(JSON.stringify({
        'message': message,
        'username': username,
        'is_todo': false
    }));
    messageInputDom.value = '';
};


document.querySelector('#todo-form-submit').onclick = function (e) {

    // const todoInputDom = document.querySelector('#todo-form');
    const what = document.querySelector('#id_what').value;
    const how_much = document.querySelector('#id_how_much').value;
    const by_when = document.querySelector('#id_by_when').value;
    const punishment = document.querySelector('#id_punishment').value;

    message = {
        'create_user': username,
        'what': what,
        'how_much': how_much,
        'by_when': by_when,
        'punishment': punishment,
    }

    chatSocket.send(JSON.stringify({
        'message': message,
        'username': username,
        'is_todo': true
    }));


};
