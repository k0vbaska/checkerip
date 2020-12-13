import requests as req
import json

def sayer():
	print("Произошла ошибка:(")
	main()

def getip(ip):
	result = req.get("http://ip-api.com/json/" + ip)
	result = result.json()
	return result

def main():
	print("[1] Информация об IP")
	menu = int(input(">>> "))
	if menu == 1:
		try:
			print("* Оставьте поле пустым, чтобы узнать информацию о своем IP")
			ip = input(">>> Введите IP ")
			res = getip(ip)
			print("Страна: " + res['country'])
			print("Город: " + res['city'])
			print("Регион: " + res['regionName'])
			print("Часовой пояс: " + res['timezone'])
			print("Провайдер: " + res['as'])
			print("IP: " + res['query'])
		except:
			sayer()
	else:
		print("Выберите пункт из меню")
		main()

main()