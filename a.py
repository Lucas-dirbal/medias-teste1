print("**************************")
print("*******Bem-vindo(a)*******")
print("**************************")
while True:
    print("1 - Primeira serie\n2 - Segunda serie\n3 - Terceira serie")
    serie = int(input("Qual serie você está cursando ?"))

    if serie == 1:
        print("Ainda em manutenção !")
        refazerMedias = input("Deseja recalcular sua media ?")
        if refazerMedias == "sim":
            print("")
        elif refazerMedias == "não":
            break
    
    
    elif serie == 2:
        print("Vamos começar comas materia normais :")
        
        prj_de_vida1 = int(input("Qual foi sua media no 1ºTrimestre de Prjoeto de vida ?"))
        prj_de_vida2 = int(input("Qual foi sua media no 2ºTrimestre de Prjoeto de vida ?"))
        prj_de_vida3 = int(input("Qual foi sua media no 3ºTrimestre de Prjoeto de vida ?"))
        
        prj_de_vida_soma = (prj_de_vida1 + prj_de_vida2 + prj_de_vida3) 
        prj_de_vida_final = prj_de_vida_soma - 180        
        if prj_de_vida_final >= 0:
            print(f"aprovado em projeto de vida ! \nCom {prj_de_vida_final} pontos sobrando !")
        else :
            print("")
        break
    
    
    
    elif serie == 3:
        print("teste3")
        break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    else:
        print("invalido")