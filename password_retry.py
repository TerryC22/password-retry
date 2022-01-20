password = 'a123456'
x = 0
y = 3
while x < 3:
	ps = input('請輸入密碼：')
	x = x + 1
	z = y - x
	if ps == 'a123456':
		print('登入成功！')
		break
	elif ps != 'a123456':
		print('密碼錯誤！還有',' ',z,' ','次機會')
