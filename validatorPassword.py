#Reto desarrollado con python
#Entrada de la contraseña
password=input("Ingrese su contraseña: ")
#Validacion de la contraseña
def validarPassword(password):
    #Condicione para comprobar que tiene mas de 8 caracteres
    if len(password)>8:
        #Contador de las minusculas mayusculas y caracteres especiales 
        contadorMayuscula=0
        contadorMinuscula=0
        contadorCaracteres=0
        #Lista de caracteres especiales en otros lenguajes se conoce como arreglos
        caracterEspeciales=["/", "$", "#", "%", "&","(", ")", "*", "-", "+", "[", "]", "{", "}", "?","¿"]
        #Iterador para la contraseña
        for i in password:
            print(i)
            #Iterador de carateres especiales
            for caracterEspecial in caracterEspeciales:
                #Si cumple la conidicion incrementa el contador de carateres
                if i ==caracterEspecial:
                    contadorCaracteres+=1
            #Si cumple la conidicion incrementa el contador de carateres
            if i.isupper():
                contadorMayuscula+=1
            #Si cumple la conidicion incrementa el contador de carateres
            elif i.islower():
              contadorMinuscula+=1  
        #Si los contadores no cuentan con ningun cero responde un mensaje
        if (contadorMayuscula !=0 and contadorCaracteres!=0 and contadorMinuscula!=0):      
            return f"La contraseña {password} es valida"
    #Si no cumple con la cantidad de carateres
    else:
        return "La contraseña debe tener al menos 8 caracteres"
#llamado de funcion de validación
print(validarPassword(password))

#Documentacion oficial => https://docs.python.org/3/
#Para ejecutarlo se escribre: "python ./validatorPassword.py"