function SendMessage()
{
  addMessage(message.value,
    {
      email : message.value
    }
  );
  message.value = "";
}

function init()
{
  onMessageAdded(function(snapshot)
  {
    var node = document.createElement("span");
    var breakLine = document.createElement("br");
    var textnode = document.createTextNode(snapshot.val().email);
    node.appendChild(textnode);
    chatBox.appendChild(node);
    chatBox.appendChild(breakLine);
    chatBox.scrollTop=chatBox.scrollHeight
  });
}
