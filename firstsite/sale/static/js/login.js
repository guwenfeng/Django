/**
 * Created by SHQT on 2017/12/18.
 */


/**
 *
 * @param len  验证码
 */
  var getCharacter = function(len){
      var character = "";
      for(var i=0;i<(len||4);i++){
          character += String.fromCharCode(Math.floor(Math.random()*26)+"A".charCodeAt(0));
      }
      document.getElementById('checkCode').innerHTML =character;
}
getCharacter(4)


document.getElementById("inputCode").addEventListener("onchange",validate)
function validate () {
    var inputCode = document.getElementById("inputCode").value;
    console.log(inputCode);
    var codeToUp=document.getElementById("checkCode").textContent;
    if(inputCode.length <=0) {
      alert("请输入验证码！");
      return false;
    }
    else if(inputCode.toUpperCase() != codeToUp.toUpperCase() ){
       alert("验证码输入错误！");
       getCharacter();
       return false;
    }
}


/**
 *
 * @param len  登录
 */
function validateLogin(e){
        var sUserName = document.frmLogin.username.value
        var sPassword = document.frmLogin.password.value ;
        var sinputCode =document.getElementById('inputCode').value ;
        if ((sUserName =="") || (sUserName=="Your name")){
             alert("请输入用户名!");
             e.preventDefault()
            return False
        }

        if ((sPassword =="") || (sPassword=="Your password")){
            alert("请输入密码!");
            e.preventDefault()
             return False
        }
        if ((sinputCode =="") || (sinputCode=="Your code")){
            alert("请输入验证码!");
            e.preventDefault()
             return False
           }

        validate()
   }


/**
 *
 * @param len  注册
 */


document.getElementsByName("repassword").addEventListener("onchange",checkpwd)
function checkpwd () {
    var sPassword = document.frmLogin.password.value ;
    var rePassword = document.frmLogin.repassword.value ;


    if ((sPassword.length >0)  && (rePassword.length >0) && (sPassword!=rePassword)) {
      alert("两次输入的密码不一致!");
      return false;
    }
}

function validateRegist(e){
        console.log(11)
        var sUserName = document.frmLogin.username.value
        var sPassword = document.frmLogin.password.value ;
         var rePassword = document.frmLogin.repassword.value ;

        if ((sUserName =="")){
             alert("请输入用户名!");
             e.preventDefault()
            return False
        }

        if ((sPassword !=rePassword)){
            alert("两次输入的密码不一致!");
            e.preventDefault()
             return False
        }
        if ((sPassword =="") || (rePassword=="")){
            alert("请输入密码!");
            e.preventDefault()
             return False
           }
   }
