
document.getElementById("id_message_send_button").addEventListener("click", function() {
    document.getElementById("replyDialog").style.display = "block";
});

// JavaScript code to handle send and cancel buttons
document.getElementById("replySendButton").addEventListener("click", function() {
    // Get the message from the textarea
    var message = document.getElementById("replyMessage").value;
    // Send the message to the backend API
    // Implement your API call here
    console.log("Sending message:", message);
    document.getElementById("replyDialog").style.display = "none";
});

document.getElementById("replyCancelButton").addEventListener("click", function() {
    document.getElementById("replyDialog").style.display = "none";
});
document.getElementById("emojiButton").addEventListener("click", function() {
    document.querySelector(".emoji-options").style.display = "block"
});