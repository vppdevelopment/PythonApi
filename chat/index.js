function SaveEmail()
{
  var emailtext = document.getElementById("email");
  addEmail(emailtext.value,
    {
      email : emailtext.value
    }
  );
  emailtext.value = "";
}

function init()
{
  var emailList = document.getElementById("emailList");
  onEmailAdded(function(snapshot)
  {
    var node = document.createElement("LI");
    var textnode = document.createTextNode(snapshot.val().email);
    node.appendChild(textnode);
    emailList.appendChild(node);
  });
}
