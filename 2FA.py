import time
import pyotp
import qrcode

def gera_chave_mestre():
    """Gera uma chave mestre aleatória usando pyotp"""
    return pyotp.random_base32()

def gera_codigo(chave_mestre):
    """Gera um código TOTP baseado na chave mestre"""
    return pyotp.TOTP(chave_mestre).now()

def verifica_codigo(chave_mestre, codigo_usuario):
    """Verifica se o código TOTP fornecido pelo usuário é válido"""
    return pyotp.TOTP(chave_mestre).verify(codigo_usuario)

def gera_qrcode(chave_mestre, name, issuer_name):
    """Gera um QRCode contendo o link de provisionamento para aplicativos de autenticação"""
    link = pyotp.TOTP(chave_mestre).provisioning_uri(name=name, issuer_name=issuer_name)
    qrcode.make(link).save("qrcode.png")

if __name__ == "__main__":
    # Gera uma nova chave mestre
    chave_mestre = gera_chave_mestre()
    print("Chave Mestre:", chave_mestre)

    # Gera um código TOTP baseado na chave mestre
    codigo = gera_codigo(chave_mestre)
    print("Código TOTP:", codigo)

    # Solicita ao usuário que insira o código TOTP para verificação
    codigo_usuario = input("Digite o código: ")
    if verifica_codigo(chave_mestre, codigo_usuario):
        print("Código verificado com sucesso!")
    else:
        print("Código inválido!")

    # Gera um QRCode para o link de provisionamento
    gera_qrcode(chave_mestre, name="Leo", issuer_name="Teste de 2FA")
    print("QRCode gerado e salvo como 'qrcode.png'.")