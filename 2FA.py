import time 
import pyotp
import qrcode


# print(pyotp.random_base32())
# gera um código aleatório

chave_mestre = "TDYHCEJMCUNG23BQQI3RBWCEVNZC67T2"

codigo = pyotp.TOTP(chave_mestre)
# ele pega uma combinação de 6 digitos e gera um codigo aleatorio com base na chave mestre
print(codigo.now())
# gera o codigo aleatorio de 30 em 30 sec

codigo_usuario = input("Digite o codigo: ")
print(codigo.verify(codigo_usuario))
# verifica se o codigo digitado é valido comparando com chave com codigo_usuario


# QRCode
link = pyotp.TOTP(chave_mestre).provisioning_uri(name="Leo", issuer_name="Teste de 2FA")

qrcode.make(link).save("qrcode.png")
