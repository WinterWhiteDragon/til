import socket
from time import ctime


host = 'localhost'
port = 6660
	# 0 ~ 1024번 port는 주로 내부 시스템 전용
bufsiz = 1024
	# buffer size의 단위는 byte
	# buffer size가 커질 수록 느려진다
addr = (host, port)
	# host & port을 묶어서 정의

if __name__ == "__main__":
	# Make socket, then bind, then listen, then accept
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(addr)
	server_socket.listen(5)
		# 서버가 새 접속을 받을 수 있게 활성화시킨다. 괄호 안에 backlog값을 넣어야 하는데, 0보다 큰 숫자여야 한다.
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 3)
		# SOL_SOCKET은 setsockopt가 설정을 다루도록 하는 기본 입력값 같은 것, SO_REUSEADDR는 보안을 위해

	# Python이기에 이렇게 간단하게 만들 수 있다
		# C로 socket을 정의하려면 코드 400줄을 써야한다
	
	# accept 요청이 오기 전까지 계속 listen하게 만들기 위해 무한반복문 사용
	while True:
		print("Server is listening......")
			# client로부터 접속해서 handshake이 끝날 때까지 여기까지만 실행하고 대기한다 
		client_sock, addr = server_socket.accept()
		print("Client connected from : ", addr)
			# 여기서 addr은 위에서 정의한 서버의 addr이 아니라, 바로 위 줄에서 받은 client의 addr
				# client의 addr란 client쪽에서 접속할 때 쓰는 client's port number다
					# 기본적으로 random하게 주어진다

		# accept하고 나서, receive & send를 하기까지 무한반복하게 만든다
			# recv()는 상대가 보낸 정보를 받고, send()는 상대에게 
		while True:
			data = client_sock.recv(bufsiz)
			if not data or data.decode("utf-8") == 'END':
				# client가 보낸 정보를 봤을 때, 비어있거나 (정보가 없거나) 끝까지 다 봤으면 반복문을 깨트린다
				break
			print("Data received from client : %s" % data.decode("utf-8"))
			print("Sending server time : %s" % ctime())

			try:
				client_sock.send(bytes(ctime(), 'utf-8'))
			except KeyboardInterrupt:
				print("Exited by user")
			except:
				pass
		client_sock.close()
	server_socket.close()

