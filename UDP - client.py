import socket #objeto importado

HOST = 'localhost' # 127.0.0.1 #endereço host
PORT = 5000 #porta aberta para comunicações

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #dados a serem recebidos (datagramas)
destino = (HOST, PORT) #destino da mensagem

while(True): #enquanto for verdadeiro, exibir a mensagem
    mensagem = bytes(input('Digite a mensagem: '), encoding='utf-8') #mensagem a ser exibida
    udp.sendto(mensagem, destino) #enviar mensagem ao destino

udp.close() #encerrar udp