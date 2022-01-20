password = 'a123456'
y = 3
while y > 0:
	y = y - 1
	ps = input('請輸入密碼：')
	if ps == password:
		print('登入成功！')
		break
	else:
		print('密碼錯誤！')
		if y > 0:
			print('還有',' ',y,' ','次機會')
		else:
			print('沒機會嘗試了！要鎖帳號了！')