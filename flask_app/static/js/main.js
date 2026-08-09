document.addEventListener("DOMContentLoaded", () => {
    const chatWindow = document.getElementById("chat-window");
    const userInput = document.getElementById("user-input");
    const sendBtn = document.getElementById("send-btn");
    const historyList = document.getElementById("chat-history");
    const sidebarToggle = document.getElementById("sidebar-toggle");
    const sidebar = document.querySelector(".sidebar");

    // Toggle the collapsed class on click
    sidebarToggle.addEventListener("click", () => {
        sidebar.classList.toggle("collapsed");
    });

    // Auto-resize textarea as user types
    userInput.addEventListener("input", function() {
        this.style.height = "auto";
        this.style.height = (this.scrollHeight) + "px";
    });

    // Handle Enter key (Shift+Enter for new line)
    userInput.addEventListener("keydown", function(e) {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    sendBtn.addEventListener("click", sendMessage);

    async function sendMessage() {
        const text = userInput.value.trim();
        if (!text) return;
        appendMessage("user", text);
        sendBtn.disabled = true;

        // 1. Add User Message to Chat
        // const result = await response.json();
        // addToHistory(text, result.label);
        // addToHistory(text);
        
        // Reset input
        userInput.value = "";
        userInput.style.height = "auto";

        // 2. Add Loading Indicator
        const loadingId = appendLoading();

        // 3. TODO: Fetch from Flask Backend (Placeholder logic for now)
        // We will connect this to your Python API shortly!
        try {
            const response = await fetch("/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    text: text
                })
            });
            if (!response.ok) {
                throw new Error("Prediction request failed.");
            }
            const result = await response.json();
            removeElement(loadingId);
            sendBtn.disabled = false;
            const botMessage = `
                <b>Prediction</b><br><br>
                Sentiment:
                <span class="${
                    result.label === "Positive"
                        ? "sentiment-positive"
                        : "sentiment-negative"
                }">
                    ${result.label}
                </span>
                <br><br>
                Confidence:
                ${result.confidence}%
                <br><br>
                <small style="color:#a0a0a0;">
                    Processed by BERT
                </small>
            `;
            appendMessage("bot", botMessage);
            addToHistory(text, result.label);
        }
        catch(error){
            removeElement(loadingId);
            sendBtn.disabled = false;
            appendMessage(
                "bot",
                `<span style="color:#ff3366;">
                Error: Unable to connect to the server.
                </span>`
            );
            console.error(error);
        }
    }
    function appendMessage(sender, htmlContent) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", sender === "user" ? "user-message" : "bot-message");

        const bubbleDiv = document.createElement("div");
        bubbleDiv.classList.add("bubble");
        bubbleDiv.innerHTML = htmlContent; // Using innerHTML to render bold/colored span tags

        messageDiv.appendChild(bubbleDiv);
        chatWindow.appendChild(messageDiv);
        scrollToBottom();
    }

    function addToHistory(text, label) {
        const li = document.createElement("li");
        li.classList.add("history-item");
        li.innerHTML = `
            <strong>${label}</strong><br>
            ${text}
        `;
        if (historyList.firstChild) {
            historyList.insertBefore(li, historyList.firstChild);
        } else {
            historyList.appendChild(li);
        }
    }

    function appendLoading() {
        const id = "loading-" + Date.now();
        const messageDiv = document.createElement("div");
        messageDiv.id = id;
        messageDiv.classList.add("message", "bot-message");

        const bubbleDiv = document.createElement("div");
        bubbleDiv.classList.add("bubble");
        bubbleDiv.innerHTML = `<span style="color: var(--accent-blue)">Analyzing Your Input...</span>`;

        messageDiv.appendChild(bubbleDiv);
        chatWindow.appendChild(messageDiv);
        scrollToBottom();
        return id;
    }

    function removeElement(id) {
        const el = document.getElementById(id);
        if (el) el.remove();
    }

    function scrollToBottom() {
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }
});