    $(document).ready(function() {
        // Send the form on enter keypress and avoid if shift is pressed 
        $('#user-message').keypress(function(event) {
            if ((event.keyCode === 13 && !event.shiftKey)) {
                event.preventDefault();
                $('form').submit();
            }
        });
        $('#send-button').on('click', function(event) {
            event.preventDefault();
            $('form').submit();
        });

        $('form').on('submit', function(event) {
            event.preventDefault();
            // get the CSRF token from the cookie 
            var csrftoken = Cookies.get('csrftoken');

            // set the CSRF token in the AJAX headers 
            $.ajaxSetup({
                headers: {
                    'X-CSRFToken': csrftoken
                }
            });

            var prompt = $('#user-message').val();
            var dateTime = new Date();
            var time = dateTime.toLocaleTimeString();

            $('#chat-messages').append('<div class="chat-message user">' + "🧑‍💻You: " + prompt + '</div>');

            $('#user-message').val('');
            $.ajax({
                url: '/chat',
                type: 'POST',
                data: {
                    prompt: prompt
                },
                dataType: 'json',
                success: function(data) {
                    var response = "🤖Bot:" + data.response
                    $('#chat-messages').append('<div class="chat-message sent" id="sentmessage">' + "🤖Bot:" + response + '</div>');



                    var typed = new Typed('#sentmessage.sent:last-child', {
                        strings: [response],
                        typeSpeed: 50,
                        backSpeed: 0,
                        showCursor: true,
                        loop: false
                    });

                }
            });
        });
    });