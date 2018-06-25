$(document).ready(function(){
	$('form').bootstrapValidator({
　　　　　　　　message: 'This value is not valid',
		　feedbackIcons: {
			　　　　　　　　valid: 'glyphicon glyphicon-ok',
			　　　　　　　　invalid: 'glyphicon glyphicon-remove',
			　　　　　　　　validating: 'glyphicon glyphicon-refresh'
		　　　　　　　　   },
		fields: {
			username: {
				message: '用户名验证失败',
				validators: {
					notEmpty: {
						message: '用户名不能为空'
					},
					emailAddress: {
						message: '邮箱格式不正确'
					}
				} 
			},
			password: {
				validators: {
					notEmpty: {
						message: '密码不能为空'
					},
					regexp: {
						regexp: /^[a-zA-Z0-9_]+$/,
						message: '密码只能包含大写、小写、数字和下划线'
					},
					stringLength: {
						min: 6,
						max: 18,
						message: '密码长度必须在6到18位之间'
					},
				}
			},
			password1: {
				validators: {
					notEmpty: {
						message: '密码不能为空'
					},
					regexp: {
						regexp: /^[a-zA-Z0-9_]+$/,
						message: '密码只能包含大写、小写、数字和下划线'
					},
					stringLength: {
						min: 6,
						max: 18,
						message: '密码长度必须在6到18位之间'
					},
				}
			},
			password2: {
				validators: {
					notEmpty: {
						message: '密码不能为空'
					},
					regexp: {
						regexp: /^[a-zA-Z0-9_]+$/,
						message: '密码只能包含大写、小写、数字和下划线'
					},
					stringLength: {
						min: 6,
						max: 18,
						message: '密码长度必须在6到18位之间'
					},
				}
			}
		}
	});
	$(".nav li").click(
		function()
		{
			console.log("hello")
			$(this).tab("show")

		}
	);
});
function validate_form()
{
	if(!check_email())
	{
		var email = $("#email input")
		email.focus();
		return false
	}
	else if(!check_password())
	{
		var password1 = $("#password1 input")
		password1.focus()
		return false
	}
	else if(!check_confirmpassword())
	{
		var password2 = $("#password2 input")
		password2.focus()
		return false
	}
	return true
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
function ChangeCode(code)
{
	code.src += "?";

}
function validate_loginform()
{
	var email = $("#email input")
	var password1 = $("#password1 input")
	if(email.val() == "")
	{
		email.focus()
		return false
	}
	if(password1.val() == "")
	{
		password1.focus()
		return false
	}
	return true;
	
}
