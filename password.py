password = 'a123456'
while True:
	inputpassword = input('請輸入密碼,最多三次機會:')
	if inputpassword != password:
		print('密碼錯誤,還有兩次機會')
		inputpassword2 = input('請輸入密碼,還有兩次機會:')
		if inputpassword2 != password:
			print('密碼錯誤,還有一次機會')
			inputpassword3 = input('密碼錯誤,還有一次機會:')
			if inputpassword3 != password:
				print('密碼錯誤,登入失敗')
				break
			else:
				print('登入成功')	
				break
		else:
			print('登入成功')	
			break
	else:
		print('登入成功')	
		break
	
