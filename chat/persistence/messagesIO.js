var rootIO = new Firebase("https://blazing-torch-1750.firebaseio.com/");
var emailsIO = new Firebase("https://blazing-torch-1750.firebaseio.com/emails");

function addMessage(key, content)
{
  var emailsRef = rootIO.child("emails");
  emailsRef.child(key).set(content);
}

function onMessageAdded(refresh)
{
  emailsIO.on("child_added", function(snapshot, prevChildKey) {
  refresh(snapshot);
  }, function (errorObject) {
    console.log("The read failed: " + errorObject.code);
  });
}
