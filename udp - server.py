import socket #objeto importado

HOST = '' #host não definido
PORT = 5000 #porta aberta pra receber comunicações

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #dados a serem recebidos (datagramas)
origem = (HOST, PORT) #variável recebe host e port
udp.bind(origem) #faz a comunicação

print("Serviço UDP inicializado. Aguardando mensagem. \n") #mensagem a ser exibida quando carregar udp

while True: #enquanto for verdadeiro, realizar o comando abaixo
    msg, cliente = udp.recvfrom(1024) #valor que cliente e mensagem recebem
    print(cliente, msg) #exibir cliente e mensagem

udp.close() #encerrar udp

