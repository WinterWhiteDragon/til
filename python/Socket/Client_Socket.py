import socket


host = 'localhost'
port = 6660
bufsiz = 4096
addr = (host, port)

if __name__ == "__main__":
	# client socket을 만들다
	client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# 사용자에게 host & port를 바꾸 쓸 수 있는 기회를 제공
		# 만약 사용자가 host & port을 바꾸지 않을 경우, default 값으로 기존 host & port 사용하게 한다
	host = input("hostname[localhost]> ") or host
	
	port = input("port number[6660]> ") or port
	
	sock_addr = (host, int(port))
		# port number는 int이어야하지만 input은 string으로 받기 때문에 int()를 더한다
	client_sock.connect(sock_addr)

	# payload == packet 안의 실제로 상대방에게 전달하려는 데이터
	payload = 'GET TIME'

	try:
		while True:
			# payload를 보낼 때는 네트워크에 접속하기에 반드시 encoding을 해야한다
				# 네트워크는 무조건 utf-8 encoding 사용
			client_sock.send(payload.encode('utf-8'))
			data = client_sock.recv(bufsiz)
			print(repr(data))
				# "repr"은 사실 "__repr__", 파이썬의 datetime 라이브러리의 함수 중 하나
					# method를 interpreter에서 바로 사용가능한 형태로, string형태로 만들어 놓는다
						# 반면, str()을 사용하면 사용자가 보기 편한 형태로 출력한다
					# repr을 하지 않을 때랑 값은 같지만, repr은 별도 위치에 객체를 객체 그대로 저장한다
			# 여기까지만 해도 실행 가능, 하지만 
			more = input("Want more? [y / n]")
			if more.lower() == 'y':
				payload = input("Enter payload: ")
			else:
				break
	except KeyboardInterrupt:
		print("Exited")

	client_sock.close()



