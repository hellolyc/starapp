$(document).ready(function(){
   $("#email input").blur(check_email);
   $("#password1 input").blur(check_password);
   $("#password2 input").blur(check_confirmpassword);
});
function validate_form()
{
	return check_email() && check_password() && check_confirmpassword();
	
}
function check_email()
{
	var email = $("#email input")
	var font = $('#email font')
	 var myreg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
	if(email.val() == "")
	{
		font.text("不能为空!")
		return false
	}
	else if(!myreg.test(email.val()))
	{
		font.text("邮箱格式不正确")
		return false
	}
	else
	{
		font.text("")
		return true
	}
}
function check_password()
{
	var password1 = $("#password1 input")
	var font = $('#password1 font')
	var number = /[0-9]/i;
	var chars =  /[a-z]/i;	
	if(password1.val() == "")
	{
		font.text("不能为空!")
		return false
	}
	else if(!number.test(password1.val()) || !chars.test(password1.val()))
	{
		font.text("密码格式不正确")
		return false
	}
	else if(password1.val().length > 16 || password1.val() < 8)
	{
		font.text("密码8-16位")
		return false
		
	}
	else{font.text("") 
	return true}
}
function check_confirmpassword()
{
	var password1 = $("#password1 input")
	var password2 = $("#password2 input")
	var font = $('#password2 font')
	if(password1.val() != password2.val())
	{
		font.text("密码不一致")
		return false
	}
	else{font.text("") 
	return true}
	
}
