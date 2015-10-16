$('#login_submit').click(function(){

    var username = $('#username').val();
    var password = $('#password').val();

    <!--ajax.post方法请求，进行登陆验证-->
    $.post(
        '/loginReg/doLogin/',
        {username:username,password:password},
        function(data){
            if(data == 1){
                alert('login OK!');
            }else{
                alert('error');
            }
        }
    )
})