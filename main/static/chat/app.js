const chatMessages = document.getElementById('chat-messages');
const userMessage = document.getElementById('user-message');
const sendButton = document.getElementById('send-button');

sendButton.addEventListener('click', () => {
    const message = userMessage.value;
    if (message.length === 0) {
        return;
    } else {
        displayUserMessage(message);
        userMessage.value = '';
        // Прокрутить чат в самый низ после отправки сообщения
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});

userMessage.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        event.preventDefault()
        sendButton.click(); // Отправить сообщение при нажатии Enter

    }
});



function displayUserMessage(message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('chat-message', 'user');
    messageElement.innerText = "You: " + message;
    chatMessages.appendChild(messageElement);
    // Прокрутить чат в самый низ после добавления сообщения
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function displayBotMessage(message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('chat-message', 'sent');
    messageElement.innerText = message;
    chatMessages.appendChild("ChatGPT: " + messageElement);
    // Прокрутить чат в самый низ после добавления сообщения
    chatMessages.scrollTop = chatMessages.scrollHeight;
<<<<<<< HEAD:frontend/spage/ready_html/second_page/chatpage/app.js
}

function sendMessageToServer(message) {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/send-message/');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            // это принимает ответ сервера
            displayBotMessage(response.message);
        }
    };
    const data = 'message=' + encodeURIComponent(message);
    xhr.send(data);
}
=======
}
>>>>>>> 6ea0f62acd204ec2b216fd9d99d67ce19c085305:backend/main/static/chat/app.js
