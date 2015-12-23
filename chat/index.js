function SendMessage()
{
  addMessage(
    {
      userName : signInName.value,
      dateTime : Firebase.ServerValue.TIMESTAMP,
      content : message.value
    }
  );
  message.value = "";
}

function EvaluateSendMessage(e)
{
  var charCode = (typeof e.which === "number") ? e.which : e.keyCode;
  if(charCode == 13)
   send.click();
}

function VerifyUserName()
{
  if(signInName.value)
    send.disabled = false;
  else
    send.disabled = true;
}

function init()
{
  onMessageAdded(function(snapshot)
  {
    var node = document.createElement("span");
    var breakLine = document.createElement("br");
    var textnode = document.createTextNode(time(snapshot.val().dateTime)+ " - "+ snapshot.val().userName +" : "+ snapshot.val().content);
    node.appendChild(textnode);
    chatBox.appendChild(node);
    chatBox.appendChild(breakLine);
    chatBox.scrollTop=chatBox.scrollHeight
  });
}
