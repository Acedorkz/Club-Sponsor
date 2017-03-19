
$.ajax({
    type:"GET",
    url:"http://127.0.0.1:8000/ItemList/",
    dataType:"json",
    success:function(message){
      var len=message.length;
      console.log(len);
      console.log(message);
      // 根据ItemList遍历用户发表的内容
      //并且创建div 渲染页面
      for(var i=len-1;i>=0;i--){
        var title=message[i].title;
        var content=message[i].contents;
        var author=message[i].author;
        var pubtime=message[i].pubtime;
        var kind=message[i].kind;

        if(kind=="club"){
          var li=document.createElement("li");
          document.getElementById("thumbnails_club").appendChild(li);
          li.className="span4";
          var thumbnail=document.createElement("div");
          thumbnail.className="thumbnail";
          li.appendChild(thumbnail);

          var caption=document.createElement("div");
          caption.className="caption";
          thumbnail.appendChild(caption);

          var tit=document.createElement("div");
          tit.id="tit"+i;
          caption.appendChild(tit);

          var com=document.createElement("div");
          com.id="com"+i;
          caption.appendChild(com);

          var auth=document.createElement("div");
          auth.id="auth"+i;
          caption.appendChild(auth);

          var time=document.createElement("div");
          time.id="time"+i;
          caption.appendChild(time);

          var kin=document.createElement("div");
          kin.id="kin"+i;
          caption.appendChild(kin);

          $("#tit"+i).html("title:"+title);
          $("#com"+i).html("content:"+content);
          $("#auth"+i).html("author:"+author);
          $("#time"+i).html("pubtime:"+pubtime);
          $("#kin"+i).html("kind:"+kind);
        }

        else if(kind=="market"){
          var li=document.createElement("li");
          document.getElementById("thumbnails_merchant").appendChild(li);
          li.className="span4";
          var thumbnail=document.createElement("div");
          thumbnail.className="thumbnail";
          li.appendChild(thumbnail);

          var caption=document.createElement("div");
          caption.className="caption";
          thumbnail.appendChild(caption);

          var tit=document.createElement("div");
          tit.id="tit"+i;
          caption.appendChild(tit);

          var com=document.createElement("div");
          com.id="com"+i;
          caption.appendChild(com);

          var auth=document.createElement("div");
          auth.id="auth"+i;
          caption.appendChild(auth);

          var time=document.createElement("div");
          time.id="time"+i;
          caption.appendChild(time);

          var kin=document.createElement("div");
          kin.id="kin"+i;
          caption.appendChild(kin);

          $("#tit"+i).html("title:"+title);
          $("#com"+i).html("content:"+content);
          $("#auth"+i).html("author:"+author);
          $("#time"+i).html("pubtime:"+pubtime);
          $("#kin"+i).html("kind:"+kind);
        }
      }


      // 创建这样的结构
      // <li class="span4">
      //   <div class="thumbnail">
      //     <img alt="300x200" src="/static/pic/pic1.jpg" />
      //     <div class="caption">
      //       <div id="comment"></div>
      //       <div id="author"></div>
      //       <div id="pubtime"></div>
      //       <p>
      //         <a class="btn btn-primary" href="#">浏览</a> <a class="btn" href="#">分享</a>
      //       </p>
      //     </div>
      //   </div>
      // </li>

    }

});

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
console.log(username);1


$("#hi_user").html("Good to see you "+username);

$("#auth_input").attr("value",username);
$("#auth_input").attr("readOnly","true");
