document.getElementById("id_message_send_button").addEventListener("click", function() {
	document.getElementById("replyDialog").style.display = "block";
});

document.getElementById("replyCancelButton").addEventListener("click", function() {
	document.getElementById("replyDialog").style.display = "none";
});

document.addEventListener("DOMContentLoaded", function(){
	var resetButton = document.getElementById("replyResetButton");
	resetButton.addEventListener("click", function(){
		var message = document.getElementById("replyMessage");
		message.value ="";
	});
});

const emojiContainer = document.getElementById('emoji-container');
const replyText = document.getElementById("replyMessage");
emojiContainer.addEventListener('click', function(event){
	if (event.target.tagName === 'SPAN') {
	const clickedEmoji = event.target.textContent;

	replyText.value +=clickedEmoji;
	}
});

const emojiContainerr= document.getElementById('emoji-containerr');
const replyTextt = document.getElementById("replyMessage");
emojiContainer.addEventListener('click',function(event){
	if (event.target.tagName === 'SPAN'){
		const clickedEmooji = event.target.textContext;
		replyText.value =+clickedEMoji;
	}
});

var replyForm = document.getElementById('replyForm');
var replyMessage = document.getElementById('replyMessage');
var replyMessageInput = document.getElementById('replyMessageInput');

replyForm.addEventListener('submit', function(event){
	event.preventDefault();
	var formData = new FormData();
	formData.append('reply_message', replyMessage.value);
	formData.append('main_message_id', "{{ id }}");
	formData.append('main_message', "{{ message }}");

	var formDataJSON = {};
	formData.forEach(function(value, key){
		formDataJSON[key] = value;
	});

	replyMessageInput.value = JSON.stringify(formDataJSON);

	this.submit();
	});