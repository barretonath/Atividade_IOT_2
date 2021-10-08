import socket #classe importada 
HOST = '' #não precisa de endereço, por ser servidor
PORT = 5000 #porta que receberá conexões
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #variável com constantes que abrem o protocolo
origem = (HOST, PORT) #origem (host e porta usadas)
tcp.bind(origem) #ligação à origem
tcp.listen(1) #determina quantas solicitações de conexão serão aceitas. No caso, uma.
print('Serviço iniciado. ') #exibir mensagem programada
while(True): #enquanto estiver, realizar os procedimentos abaixo
    con, cliente = tcp.accept() #espera por novas solicitações
    print('Conectado por ', cliente) #exibir mensagem programada
    while(True):#enquanto estiver, realizar os procedimentos abaixo
        mensagem = con.recv(1024) #receber dados
        print(cliente, mensagem) #exibir os valores de "cliente" e "mensagem"
    con.close() #encerrar conexão

con.close() #encerrar conexão