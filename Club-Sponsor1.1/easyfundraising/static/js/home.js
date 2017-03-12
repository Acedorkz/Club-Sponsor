
// cookie
function getCookie(cname)
{
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for(var i=0; i<ca.length; i++)
  {
    var c = ca[i].trim();
    if (c.indexOf(name)==0)
      return c.substring(name.length,c.length);
  }
  return "";
}
var username=getCookie("username");
console.log(username);


$("#hi_user").html("Good to see you "+username);
