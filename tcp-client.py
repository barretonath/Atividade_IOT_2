import socket #classe importada

HOST = 'localhost' #host local
PORT = 5000 #porta que receberá conexões

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #variável com constantes que abrem o protocolo
destino = (HOST, PORT) #destino (host e portas usadas)

tcp.connect(destino) #extabelecer conexão ao servidor (host e portas)

while(True): #enquanto receber mensagens, realizar procedimento abaixo
    mensagem = bytes(input('Digite a mensagem: '), encoding='utf-8') #exibir mensagem programada + conversão em bytes
    tcp.send(mensagem) #enviar mensagem em bytes

tcp.close() #encerrar conexão