// Функция для добавления сообщения в блок списка сообщений
function addMessageToChat(content, role) {
    const messageList = document.getElementById('message-list');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');
    messageElement.classList.add(role);
    messageElement.innerText = content;
    messageList.appendChild(messageElement);
}

// Функция обработки отправки сообщения
function sendMessage(event) {
    event.preventDefault();

    const messageInput = document.getElementById('message-input');
    const userMessage = messageInput.value;

    // Отправка сообщения пользователя на сервер через AJAX
    // и получение ответа от ChatGPT
    // Пример использования fetch():
    fetch('/process-message/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userMessage }),
        })
        .then(response => response.json())
        .then(data => {
            // Добавление ответа ChatGPT в чат
            addMessageToChat(data.message, 'chatgpt');
        })
        .catch(error => {
            console.error('Произошла ошибка:', error);
        });

    // Очистка поля ввода после отправки сообщения
    messageInput.value = '';
}

// Обработчик события отправки формы
const messageForm = document.getElementById('message-form');
messageForm.addEventListener('submit', sendMessage);