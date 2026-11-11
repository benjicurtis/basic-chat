function send(){
    const username = document.getElementById("username").value;
    const messageInput = document.getElementById("message")
    const message = document.getElementById("message").value
    fetch("/send", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({username, message})
    })
    messageInput.value = "";
}
async function getMsg(){
    const chatbox = document.getElementById("chatbox")
    const response = await fetch("/getMsg");
    const data = await response.json();
    chatbox.innerHTML = "";
    data.forEach( msg => {
        const newMsg = document.createElement("p")
        newMsg.innerHTML = `${msg.username}: ${msg.message}`;
        chatbox.appendChild(newMsg)
    })
} 

setInterval(getMsg, 1000)
