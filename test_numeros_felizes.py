#casos de uso:
# 1 - entrar um numero
# 2 - tratar numeros negativos
# 3 - somar quadrados
# 4 - verificar se é feliz ou triste
from numeros_felizes import NumerosFelizes

class TestNumerosFelizes:  
    global numerosFelizes
    numerosFelizes = NumerosFelizes() 

    #testes com número de entrada
    def teste_se_numero_eh_valido(self):
        #enviando inteiro             
        numero_teste = 7
        resultado = numerosFelizes.verificaSeNumeroEhValido(numero_teste)       
        assert resultado == True
        
        #enviando float
        numero_teste = 7.5
        resultado = numerosFelizes.verificaSeNumeroEhValido(numero_teste)
        assert resultado == False

        #enviando None    
        numero_teste = None
        resultado = numerosFelizes.verificaSeNumeroEhValido(numero_teste)       
        assert resultado == False

        #enviando string         
        numero_teste = "teste"
        resultado = numerosFelizes.verificaSeNumeroEhValido(numero_teste)       
        assert resultado == False
        
    #teste tratar numeros negativos
    def teste_se_numero_eh_negativo(self):
        numero_teste = -7
        resultado = numerosFelizes.trataNumeroNegativo(numero_teste)       
        assert resultado == 7
        
        numero_teste = 7
        resultado = numerosFelizes.trataNumeroNegativo(numero_teste)       
        assert resultado == 7

    #testar soma dos quadrados
    def teste_soma_dos_quadrados(self):
        numero_teste = 7
        resultado = numerosFelizes.somaQuadrados(numero_teste)       
        assert resultado == 49

        numero_teste = 20
        resultado = numerosFelizes.somaQuadrados(numero_teste)       
        assert resultado == 4

        numero_teste = -50
        resultado = numerosFelizes.somaQuadrados(numero_teste)       
        assert resultado == 25
        

    #teste se o número é feliz
    def teste_se_numero_eh_feliz(self):                
        numero_teste = 7
        resultado = numerosFelizes.verifica_se_numero_eh_feliz(numero_teste)       
        assert resultado == True
        
        numero_teste = -7
        resultado = numerosFelizes.verifica_se_numero_eh_feliz(numero_teste)       
        assert resultado == True

        numero_teste = 20 
        resultado = numerosFelizes.verifica_se_numero_eh_feliz(numero_teste)    
        assert resultado == False
        
        numero_teste = -20 
        resultado = numerosFelizes.verifica_se_numero_eh_feliz(numero_teste)    
        assert resultado == False
        


