$(document).ready(function(){
  $('.btn').click(function(){
      doLogin();
    });
    // $.ajax({
    //     type:"GET",
    //     url:"../user.json",
    //     dataType:"json",
    //     success:function(data){
    //         var abc = JSON.stringify(data,null," ");
    //         console.log(abc);
    //     },
    //     error:function(def){
    //         alert("json数据出错：" + def.status);
    //     }
    // });
});
function doLogin(){
  var name=$('#email').val();
  var password=$('#password').val();

  alert(name+password);

}
