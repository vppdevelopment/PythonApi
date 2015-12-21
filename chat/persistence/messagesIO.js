var rootIO = new Firebase("https://blazing-torch-1750.firebaseio.com/");
var emailsIO = new Firebase("https://blazing-torch-1750.firebaseio.com/messages");

function addMessage(content)
{
  emailsIO.push(content);
}

function onMessageAdded(refresh)
{
  emailsIO.on("child_added", function(snapshot, prevChildKey) {
  refresh(snapshot);
  }, function (errorObject) {
    console.log("The read failed: " + errorObject.code);
  });
}
