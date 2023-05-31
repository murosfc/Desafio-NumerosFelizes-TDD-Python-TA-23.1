# Números Felizes

# Para saber se um número é feliz, você deve obter o quadrado de cada dígito deste número, em seguida você faz a soma desses resultados. 
# A seguir o mesmo procedimento deve ser feito com o valor resultante desta soma. 
# Se ao repetir o procedimento diversas vezes obtivermos o valor 1, o número inicial é considerado feliz.

# Tomamos o 7, que é um número feliz:

# 7² = 49
# 4² + 9² = 97
# 9² + 7² = 130
# 1² + 3² + 0² = 10
# 1² + 0² = 1
# Podemos observar nesse exemplo que os números 49, 97, 130 e 10 também são felizes. Existem infinitos números felizes.

# E um número triste? Como sabemos que um número não será feliz?

# Desenvolva um programa que determine se um número é feliz ou triste.,

class NumerosFelizes:

    def verificaSeNumeroEhValido(self, numero):
        return isinstance(numero, int) and numero is not None
    
    def trataNumeroNegativo(self, numero):
        return abs(numero)
    
    def somaQuadrados(self, numero):
        numero_tratado = self.trataNumeroNegativo(numero)
        return sum([(int(i))**2 for i in str(numero_tratado )])
    
    def verifica_se_numero_eh_feliz(self, numero):
        if self.verificaSeNumeroEhValido(numero):
            if numero == 1:
                return True
            else:               
                if numero == 4:
                    return False
                else:
                    return self.verifica_se_numero_eh_feliz(self.somaQuadrados(numero))
        else:
            return False



    
    