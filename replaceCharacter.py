texto = "opinando como leiga em relação a marketing: a foto está absurdamente linda tbm, eu achei de um bom gosto extremo."

'''for caractere in "!@#$%*()<>:|/?":
    texto = texto.replace(caractere, "")'''

for caractere in "aeiou":
    texto = texto.replace(caractere, "*")

print(texto.lower())
