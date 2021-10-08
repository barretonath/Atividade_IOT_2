from http.client import HTTPConnection #classe importada

conexao = HTTPConnection('localhost:5000') #host que receberá conexões
conexao.request("GET", "/") #raiz
resposta = conexao.getresponse() #recebe resposta
pagina = resposta.read() #lê a resposta da página

print(pagina) #exibe a página