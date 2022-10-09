#Librerias
from tkinter import *  
import random
#creacion de ventana
root=Tk()
root.title("Clue")
root.geometry("1280x720")
root.resizable(0,0)
#fondos a utlizar
escuela=PhotoImage(file="Escuela.png")
azotea=PhotoImage(file="Azotea.png")
comedor=PhotoImage(file="Comedor.png")
gimnasio=PhotoImage(file="Gimnasio.png")
piscina=PhotoImage(file="Piscina.png")
salon=PhotoImage(file="Salon.png")
#personajes buenos
luffy=PhotoImage(file="DLuffy.png")
naruto=PhotoImage(file="DNaruto.png")
goku=PhotoImage(file="DGoku.png")
ichigo=PhotoImage(file="DIchigo.png")
saitama=PhotoImage(file="DSaitama.png")
#personajes sospechosos
asta=PhotoImage(file="DAsta.png")
eren=PhotoImage(file="DEren.png")
meliodas=PhotoImage(file="DMeliodas.png")
natsu=PhotoImage(file="DNatsu.png")
tanjiro=PhotoImage(file="DTanjiro.png")
#lugar donde va el dialogo
BarraDialogo=PhotoImage(file="Dialogo.png")
#listas
nombres=['Asta','Eren','Meliodas','Natsu','Tanjiro']
imagenes=[asta,eren,meliodas,natsu,tanjiro]
lugar=['Azotea','Comedor','Gimnasio','Piscina','Salon']
arma=['Espada antimagia','Acero endurecido','Espada rota','Fuego','Espada de agua']
#random del asesino
a=random.randint(0,4)
asesino=[nombres[a],lugar[random.randint(0,4)],arma[random.randint(0,4)],imagenes[a]]
#creacion de mapa
Mapa=[] 
Conclusion=[]
AccionesCount=0
for z in range(5):
    a=random.randint(0,(len(nombres)-1))
    Mapa.append([nombres[a],lugar[random.randint(0,len(lugar)-1)],arma[random.randint(0,len(arma)-1)],imagenes[a]])
    nombres.remove(Mapa[z][0])
    lugar.remove(Mapa[z][1])
    arma.remove(Mapa[z][2])
    imagenes.remove(Mapa[z][3])
#creacion del canvas
canvas=Canvas(root,width=1280,height=720)
canvas.pack(fill="both",expand=True)
canvas.pack()
canvas.create_image(0,0,image=escuela,anchor="nw")
canvas.create_text(600,660,text="Selecciona un lugar para investigar",fill="Black",font=("Helvetica",26)) 
canvas.create_text(600,700,text=f"Acciones restantes: {5-AccionesCount}", fill="Black",font=("Helvetica",26)) 
#cambiar a la azotea
def cambia_azotea():
    canvas.pack(fill="both",expand=True) 
    canvas.pack()
    canvas.create_image(0,0,image=azotea,anchor="nw")
    ocultar_botones()
    global nombre_lugar
    nombre_lugar="Azotea"
    global zmapa
    zmapa=ubicar_mapa(nombre_lugar)
    destino(nombre_lugar)
#cambiar al comedor
def cambia_comedor():
    canvas.pack(fill="both",expand=True)
    canvas.pack()
    canvas.create_image(0,0,image=comedor,anchor="nw")
    ocultar_botones()
    global nombre_lugar
    nombre_lugar="Comedor"
    global zmapa
    zmapa=ubicar_mapa(nombre_lugar)
    destino(nombre_lugar)
#cambiar al salon
def cambia_salon():
    canvas.pack(fill="both",expand=True) 
    canvas.pack()
    canvas.create_image(0,0,image=salon,anchor="nw")
    ocultar_botones()
    global nombre_lugar
    nombre_lugar="Salon"
    global zmapa
    zmapa=ubicar_mapa(nombre_lugar)
    destino(nombre_lugar)
#cambiar a la piscina
def cambia_piscina():
    canvas.pack(fill="both",expand=True)
    canvas.pack()
    canvas.create_image(0,0,image=piscina,anchor="nw")
    ocultar_botones()
    global nombre_lugar
    nombre_lugar="Piscina"
    global zmapa
    zmapa=ubicar_mapa(nombre_lugar)
    destino(nombre_lugar)
#cambiar al gimnasio
def cambia_gimnasio():
    canvas.pack(fill="both",expand=True) 
    canvas.pack()
    canvas.create_image(0,0,image=gimnasio,anchor="nw")
    ocultar_botones()
    global nombre_lugar
    nombre_lugar="Gimnasio"
    global zmapa
    zmapa=ubicar_mapa(nombre_lugar)
    destino(nombre_lugar)
#ocultar botones
def ocultar_botones():
    boton_piscina.place_forget()
    boton_comedor.place_forget()
    boton_azotea.place_forget()
    boton_gimnasio.place_forget()
    boton_salon.place_forget()
    global EnLugar
    global DialogCount
    EnLugar=1
    DialogCount=0
#mostrar botones    
def mostrar_botones():
    boton_investigar.place_forget()
    boton_preguntar.place_forget()
    boton_piscina.place(x=1050,y=200)
    boton_comedor.place(x=350,y=450)
    boton_azotea.place(x=600,y=100)
    boton_gimnasio.place(x=1050,y=450)
    boton_salon.place(x=600,y=300)
#mostrar opciones
def mostrar_opciones():
    boton_uno.place(x=600,y=280)
    boton_dos.place(x=600,y=320)
    boton_tres.place(x=600,y=360)
    boton_cuatro.place(x=600,y=400)
    boton_cinco.place(x=600,y=440)
#destino
def destino(lugar):
    texto=["Luffy\n\nListo, llegamos a "+lugar+ "\nBusquemos algo que nos diga quien es el asesino de Saitama",
           "Naruto\n\nParece ser que no somos los unicos aqui.\n*"+Mapa[zmapa][0]+" hace acto de presencia*",
           "Luffy\n\nCual sera nuestro siguiente paso?"]
    Imagen_texto=[luffy,naruto,luffy]
    global dialogo
    global Imagen
    if DialogCount>0 and DialogCount<len(texto):  
        canvas.itemconfig(Imagen,image=Imagen_texto[DialogCount])
        canvas.itemconfig(dialogo,text=texto[DialogCount])
        if DialogCount==2:
            boton_investigar.place(x=750,y=500)
            boton_preguntar.place(x=950,y=500)    
    elif DialogCount>=len(texto):
        boton_siguiente.place_forget()
    else:
        Imagen=canvas.create_image(0,0,image=luffy,anchor="nw")
        dialogo=canvas.create_text(200,440,fill="White",text=texto[DialogCount],anchor="nw",font=("Helvetica",20))
#funcion para interrogar       
def interrogar():
    boton_investigar.place_forget()
    boton_preguntar.place_forget()
    boton_siguiente.place(x=1000,y=680)
    global AccionesCount
    global DialogCount
    global EnLugar
    global num_dialogo 
    global dialogo  
    global Imagen
    canvas.delete(Imagen)
    canvas.delete(dialogo)
    AccionesCount+=1
    EnLugar=4
    DialogCount=0
    boton_menu.place_forget()
    num_dialogo=random.randint(0,2) 
    conversacion()
#funcion para observar el area
def observar():
    boton_investigar.place_forget()
    boton_preguntar.place_forget()
    boton_siguiente.place(x=1000,y=680)
    global AccionesCount
    global EnLugar
    global DialogCount
    global dialogo  
    global Imagen
    canvas.delete(Imagen)
    canvas.delete(dialogo)
    AccionesCount+=1
    EnLugar=2
    DialogCount=0
    boton_menu.place_forget()
    encontrarpista()
#funcion para conversar
def conversacion():
    global dialogo
    global Imagen
    lugar_random=random.randint(0,4)
    nombre_random=random.randint(0,4)
    if Mapa[nombre_random][0]==Mapa[zmapa][0] or Mapa[nombre_random][0]==asesino[0]:  
        nombre_random=random.randint(0,4)
    if lugar_random==zmapa:
        lugar_random=random.randint(0,4)
    dialogo1=[f"Naruto \n\nHola {Mapa[zmapa][0]}.",
             f"{Mapa[zmapa][0]} \n\nHey, que los trae por aqui chicos?",
             f"Ichigo \n\nSaitama ha muerto, y estamos buscando pistas acerca de su muerte, \nde hecho, nos preguntabamos donde has estado en las ultimas horas.",
             f"{Mapa[zmapa][0]} \n\nPues de hecho estaba en {Mapa[lugar_random][1]},\n y ahora que lo pienso, recuerdo haber visto a {Mapa[nombre_random][0]} rondando por el lugar.\nQuizas encuentren algo util....",
             f"Naruto \n\nHmmm,que curioso... iremos a echar un vistazo de cualquier manera, {Mapa[zmapa][0]}",
             f"{Mapa[zmapa][0]} \n\nNo hay problema, nos vemos chicos."]
    image=[naruto,Mapa[zmapa][3],ichigo,Mapa[zmapa][3],naruto,Mapa[zmapa][3]]
   
    dialogos=[[f"{Mapa[zmapa][0]} \n\nHola chicos, oigan, y Saitama?",
                 "Goku \n\nHa muerto, y Estamos buscando pistas sobre ello\nNos puedes decir donde has estado en las ultimas horas?",
                 f"{Mapa[zmapa][0]} \n\nDiablos, pobre Saitama, espero encuentren al responsable pronto \npues solamente estuve en el gimnasio haciendo ejercicio.",
                 "Goku \n\nNo pudo haber estado ahi, Saitama solo va al gimnasio de la escuela junto \ncon nosotros, y hoy es sabado",
                 "Luffy \n\nDe cualquier manera, gracias por la informacion",
                 f"{Mapa[zmapa][0]} \n\nNo hay de que y espero ustedes encuentren al culpable"],
            [f"Luffy \n\nQue onda, {Mapa[zmapa][0]}? \nVengan acá nakamas",
                 f"{Mapa[zmapa][0]} \n\nQue onda chicos, ¿y Saitama?",
                 f"Naruto \n\nAlguien ha matado a Saitama, y dado que ninguno de nosotros estaba con el, \ntenemos que saber quien lo mató. \nDinos donde estuviste estas ultimas horas que han pasado.",
                 f"{Mapa[zmapa][0]} \n\nEstaba bebiendo en ROSCOE. \nDe hecho tengo el recibo si no me creen.",
                 "Naruto \n\nNo pasa nada, sabemos que Saitama no bebe \npor lo que es imposible que estuviera en ese lugar",
                 f"{Mapa[zmapa][0]} \n\nOK, nos vemos luego, que tengo unos pendientes por hacer. \nEspero encuentren al asesino pronto."],
            [f"{Mapa[zmapa][0]} \n\nHola chicos, ¿puedo ayudarles en algo?",
                 f"Ichigo \n\nHola! {Mapa[zmapa][0]}, de hecho si, estamos buscando al desgraciado que mato a Saitama,\n donde has estado las ultimas horas?",
                 f"{Mapa[zmapa][0]} \n\nHmmm... no recuerdo muy bien...",
                 f"{Mapa[zmapa][0]} \n\nVale, ya recuerdo Estaba con {Mapa[nombre_random][0]} en la piscina, \ny posteriormente me dirigí al comedor",
                 f"Naruto \n\nCapisci, muchas gracias de todos modos {Mapa[zmapa][0]}"]]
    image2 =[[Mapa[zmapa][3],goku,Mapa[zmapa][3],goku,luffy,Mapa[zmapa][3]],[luffy,Mapa[zmapa][3],naruto,Mapa[zmapa][3],naruto,Mapa[zmapa][3]],[Mapa[zmapa][3],ichigo,Mapa[zmapa][3],Mapa[zmapa][3],naruto]]
    if asesino[0]==Mapa[zmapa][0]:
        if DialogCount>0 and DialogCount<len(dialogo1): 
            canvas.itemconfig(Imagen,image=image[DialogCount])
            canvas.itemconfig(dialogo,text=dialogo1[DialogCount])
        elif DialogCount>=len(dialogo1):  
            volver_menu()
        else:             
            Imagen=canvas.create_image(0,0,image=image[DialogCount],anchor="nw")
            dialogo=canvas.create_text(200,440,fill="White",text=dialogo1[DialogCount],anchor="nw",font=("Helvetica",20))
    else:  
        if DialogCount>0 and DialogCount<len(dialogos[num_dialogo]):  
            canvas.itemconfig(Imagen,image=image2[num_dialogo][DialogCount])
            canvas.itemconfig(dialogo,text=dialogos[num_dialogo][DialogCount])
        elif DialogCount>=len(dialogos[num_dialogo]): 
            volver_menu()
        else:            
            Imagen=canvas.create_image(0,0,image=image2[num_dialogo][DialogCount],anchor = "nw")
            dialogo=canvas.create_text(200,440,fill="White",text=dialogos[num_dialogo][DialogCount],anchor="nw",font=("Helvetica",20))
#encontrar objeto importante
def encontrarcapa():  
    global dialogo
    global Imagen
    dialogo1=["Goku \n\nChicos, he encontrado la capa de Saitama. Fue aqui donde lo mataron.",  
            "Ichigo \n\nMalditos desgraciados!!",
             "Goku \n\nNo parare hasta encontrar a este hijo de perra.",
             "Luffy \n\nNo te preocupes Goku, lo encontraremos"]
    ImgTex1=[goku,ichigo,goku,luffy]
    
    dialogo2=["Naruto \n\nHmmm, que raro, no hay nada por aqui, dudo que Saitama haya estado por \nesta area", 
             "Luffy \n\nProbablemente no haya estado por aqui",
             "Goku \n\nDescuida Saitama, te vengare muy pronto..."]
    ImgTex2=[naruto,luffy,goku]
    
    if asesino[1]==Mapa[zmapa][1]: 
        if DialogCount>0 and DialogCount<len(dialogo1):  
            canvas.itemconfig(Imagen,image=ImgTex1[DialogCount])
            canvas.itemconfig(dialogo,text=dialogo1[DialogCount])
        elif DialogCount>=len(dialogo1):
            volver_menu()
        else:            
            Imagen=canvas.create_image(0,0,image=ImgTex1[DialogCount],anchor="nw")
            dialogo=canvas.create_text(200,440,fill="White",text=dialogo1[DialogCount],anchor="nw",font=("Helvetica",20))
    else:  
        if DialogCount>0 and DialogCount<len(dialogo2): 
            canvas.itemconfig(Imagen,image=ImgTex2[DialogCount])
            canvas.itemconfig(dialogo,text=dialogo2[DialogCount])
        elif DialogCount>=len(dialogo2): 
            volver_menu()
        else:            
            Imagen=canvas.create_image(0,0,image=ImgTex2[DialogCount],anchor="nw")
            dialogo=canvas.create_text(200,440,fill="White",text=dialogo2[DialogCount],anchor="nw",font=("Helvetica",20))
#encontrar pista en las areas
def encontrarpista():
    global dialogo
    global EnLugar
    global DialogCount
    global Imagen
    dialogo1=["Luffy \n\nVale nakamas, hay que dividirnos y encontremos cualquier cosa que nos pueda \nllevar al asesino de Saitama.",
             "Naruto \n\nRayos! Acabo de encontrar algo...",
             "Naruto \n\nEncontre "+asesino[2]+", \npero no estoy seguro de a quien le pertenece.",
             "Ichigo \n\nQuizas el asesino de Saitama lo dejo caer accidentalmente."]
    ImgTex1=[luffy,naruto,naruto,ichigo]
    
    dialogo2=["Luffy \n\nVale nakamas, hay que dividirnos y encontremos cualquier cosa que nos pueda \nllevar al asesino de Saitama.",
             "...",
             "Goku \n\nParece ser que no hay nada por aquí que nos indique que fue aquí mismo \ndonde mataron a Saitama",
             "Naruto \n\nTenemos que seguir buscando, quizá deberíamos probar suerte en otro lugar..."]
    ImgTex2=[luffy,BarraDialogo,goku,naruto]
    
    if asesino[2]==Mapa[zmapa][2]:
        if DialogCount>0 and DialogCount<len(dialogo1):  
            canvas.itemconfig(Imagen,image=ImgTex1[DialogCount])
            canvas.itemconfig(dialogo,text=dialogo1[DialogCount])
        elif DialogCount>=len(dialogo1):
            DialogCount=0
            EnLugar=3
            canvas.delete(dialogo)
            canvas.delete(Imagen)
            encontrarcapa()
        else:             
            Imagen=canvas.create_image(0,0,image=ImgTex1[DialogCount],anchor="nw")
            dialogo=canvas.create_text(200,440,fill="White",text=dialogo1[DialogCount],anchor="nw",font=("Helvetica",20))
    else:  
        if DialogCount>0 and DialogCount<len(dialogo2): 
            canvas.itemconfig(Imagen,image =ImgTex2[DialogCount])
            canvas.itemconfig(dialogo,text=dialogo2[DialogCount])
        elif DialogCount>=len(dialogo2): 
            DialogCount=0
            EnLugar=3
            canvas.delete(dialogo)
            canvas.delete(Imagen)
            encontrarcapa()
        else:             
            Imagen=canvas.create_image(0,0,image=ImgTex2[DialogCount],anchor="nw")
            dialogo=canvas.create_text(200,440,fill="White",text=dialogo2[DialogCount],anchor="nw",font=("Helvetica",20))
#ubicar mapa
def ubicar_mapa(lugar): 
    for i in range(5):
        if lugar==Mapa[i][1]:
            return i       
#volver al menu para seleccionar los lugares
def volver_menu():
    global dialogo
    global DialogCount
    global EnLugar
    EnLugar=0
    if AccionesCount==5:
        canvas.delete(dialogo)
        DialogCount=0
        EnLugar=5
        resolvermisterio()
    else:
        canvas.pack(fill="both",expand=True) 
        canvas.pack() 
        canvas.create_image(0,0,image=escuela,anchor="nw") 
        mostrar_botones()
        boton_menu.place(x=5,y=680)
        canvas.create_text(600,660,text="Selecciona un lugar para investigar",fill="Black",font=("Helvetica",26)) 
        canvas.create_text(600,700,text=f"Acciones restantes: {5-AccionesCount}",fill="Black",font=("Helvetica",26)) 
#funcion para continuar el dialogo
def siguiente():
    global DialogCount
    global AnswerBien
    DialogCount+=1
    if EnLugar==1:
        destino(nombre_lugar)
    elif EnLugar==2: 
        encontrarpista()
    elif EnLugar==3: 
        encontrarcapa()
    elif EnLugar==4: 
        conversacion()
    elif EnLugar==5: 
        if DialogCount==1: 
            boton_siguiente.place_forget()
            mostrar_opciones()
        resolvermisterio()
    elif EnLugar==6: 
        Final(AnswerBien)
    elif EnLugar==7:
        root.destroy()
#funcion para resolver el misterio
def resolvermisterio():
    global dialogo
    global DialogCount
    global ans
    global AnswerBien
    global EnLugar
    global Imagen
    
    DialogFinal=["Luffy \n\nExcelente, ya es hora de encontrar al bastardo que mató a Saitama",
                "Luffy \n\nQuien es el asesino?",
                "Luffy \n\nEn donde fué asesinado Saitama?",
                "Luffy \n\nPor último, con que arma se realizo el asesinato?"]
    if DialogCount>0 and DialogCount<len(DialogFinal):
        canvas.itemconfig(dialogo,text=DialogFinal[DialogCount])
        boton_uno.configure(text=Mapa[0][DialogCount-1])
        boton_dos.configure(text=Mapa[1][DialogCount-1])
        boton_tres.configure(text=Mapa[2][DialogCount-1])
        boton_cuatro.configure(text=Mapa[3][DialogCount-1])
        boton_cinco.configure(text=Mapa[4][DialogCount-1])
    elif DialogCount>=len(DialogFinal): 
        DialogCount=0
        EnLugar=6
        canvas.delete(dialogo)
        canvas.delete(Imagen)
        ans=0
        for a in 'Espada antimagia','Acero endurecido','Espada rota','Fuego','Espada de agua':
            if asesino[2]==a:
                break
            ans+=1
        AnswerBien=True
        for i in range(3):
            if asesino[i]!=Conclusion[i]:
                AnswerBien=False
        boton_uno.place_forget()
        boton_dos.place_forget()
        boton_tres.place_forget()
        boton_cuatro.place_forget()
        boton_cinco.place_forget()
        boton_siguiente.place(x=1000,y=680) 
        Final(AnswerBien)
    else:             
        canvas.create_image(0,0,image=escuela,anchor="nw")
        Imagen=canvas.create_image(0,0,image=luffy,anchor="nw")
        dialogo=canvas.create_text(200,440,fill="White",text=DialogFinal[DialogCount],anchor="nw",font=("Helvetica",20))
#dfuncion para el ir al resultado   
def resultado(respuesta):
    global DialogCount
    global Conclusion
    Conclusion.append(respuesta)
    DialogCount+=1  
    resolvermisterio()
#dialogo final
def Final(r):
    global ans
    global DialogCount
    global dialogo
    global Imagen, EnLugar
    if r==True: 
        objetivos=[f"la {asesino[2]} que encontramos como pista? \nBueno, resulta que esa espada antimagia es de que Asta \nMusculo sin cerebro.",
                  f"el {asesino[2]} que encontramos como pista? \nBueno, resulta que ese acero endurecido le pertenece a Eren \nTitan descuidado.",
                  f"la {asesino[2]} que encontramos como pista? \nBueno, resulta que la espada rota le pertenece a Meliodas \nMaldito demonio.",
                  f"el {asesino[2]} que encontramos como pista? \nBueno, recorde que ese fuego es de la habilidad de Natsu \nMe sorprende que no lo haya quemado todo.",
                  f"la {asesino[2]} que encontramos como pista? \nBueno, la espada de agua es de Tanjiro \nLe encanta joder con unas posturas medio raras."]
        
        Dialogo_Final=["Naruto \n\nMuy bien chicos, finalmente hemos dado con el asesino de Saitama.\nFue..",
                     f"Goku \n\n{asesino[0]} ?!?!?",
                     f"Naruto \n\nEfectivamente, {asesino[0]} mato a Saitama porque es calvo",
                     "Ichigo \n\nTiene sentido, cuando fuimos a hablar con el, claramente \nNos mintio e intentó culpar a otra persona",
                     "Luffy \n\nLogrando así que el dejara de parecer un sospechoso para poder lograr su \ncometido y salirse con la suya",
                     "Goku \n\n¿Porque ese imbécil asesinaría a Saitama?",
                     f"Naruto \n\nRecuerdas {objetivos[ans]}",
                      "Goku \n\nPues fue gracias a ello que logramos encontrarte.Pero, donde está su cuerpo?",
                      f"{asesino[0]} \n\nNunca les diré donde está el cuerpo de su estúpido ami.....",
                      "Saitama \n\nHola chicos que estan haciendo?",
                      "Luffy \n\nSaitama? Hijo de perra, como es que sigues vivo?",
                      f"Saitama \n\nPues {asesino[0]} intento matarme pero solo consiguio \nnoquearme y penso que estaba muerto",
                      "Goku \n\nTiene que ser una broma, ¿acaso no puedes morir?",
                      "Saitama \n\nLa verdad no se, aun no conozco a una persona o monstruo capaz\nde aguantar mas de un golpe asi que de momento no puedo morir",
                      "Luffy \n\nMaldita se Saitama, estabamos tan preocupados por ti.",
                       f"{asesino[0]} \n\nMe lleva de haber sabido que eras tan fuerte \nhubiera intentado matar a otro de ustedes.",
                      "Saitama \n\nLo siento por ti, deberias entrenar y hacerte mas fuerte"]
        ImgFinal=[naruto,goku,naruto,ichigo,luffy,goku,naruto,goku,asesino[3],
                 saitama,luffy,saitama,goku,saitama,luffy,asesino[3],saitama]
        
        if DialogCount>0 and DialogCount<len(Dialogo_Final):  
            canvas.itemconfig(Imagen,image=ImgFinal[DialogCount])
            canvas.itemconfig(dialogo,text=Dialogo_Final[DialogCount])
        elif DialogCount>=len(Dialogo_Final): 
            DialogCount=0
            EnLugar=0
            canvas.delete(dialogo)
            canvas.delete(Imagen)
            boton_siguiente.place_forget()
            root.destroy()
        else:            
            Imagen=canvas.create_image(0,0,image=ImgFinal[DialogCount],anchor="nw")
            dialogo=canvas.create_text(200,440,fill="White",text=Dialogo_Final[DialogCount],anchor="nw",font=("Helvetica",20))
    else:
        Imagen=canvas.create_image(0,0,image=luffy,anchor="nw")
        dialogo=canvas.create_text(200,440,fill="White",text=f"Luffy \n\nTe falta investigar mejor.\nCulpable:{asesino[0]}\nLugar:{asesino[1]}\narma:{asesino[2]}",anchor="nw",font=("Helvetica",20)) 
        EnLugar=7
#boton piscina
boton_piscina=Button(canvas,text="Piscina",width=12,command=cambia_piscina)  
boton_piscina.place(x=1050,y=200)
#boton azotea
boton_azotea=Button(canvas,text="Azotea",width=12,command=cambia_azotea)
boton_azotea.place(x=600,y=100)
#boton comedor
boton_comedor=Button(canvas,text="Comedor",width=12,command=cambia_comedor)
boton_comedor.place(x=350,y=450)
#boton gimnasio
boton_gimnasio=Button(canvas,text="gimnasio",width=12,command=cambia_gimnasio)
boton_gimnasio.place(x=1050,y=450)
#boton salon
boton_salon=Button(canvas,text="Salon",width=12,command=cambia_salon)
boton_salon.place(x=600,y=300)
#boton menu
boton_menu=Button(canvas,text="menu",width=12,command=volver_menu)
boton_menu.place(x=5,y=680)
#botn siguiente
boton_siguiente=Button(canvas, text="siguiente", width=12, command=siguiente)
boton_siguiente.place(x=1000,y=680)
#boton para checar lugares
boton_preguntar=Button(canvas,text="Interrogar a la persona",width="20",command=interrogar,font=("Helveltica",12))
boton_investigar=Button(canvas,text="Analizar el lugar",width="20",command=observar,font=("Helveltica",12))
#botones para las respuestas del asesinato
boton_uno=Button(canvas,text="",width="28",command= lambda:resultado(Mapa[0][DialogCount-1]),font=("Helveltica",12))
boton_dos=Button(canvas,text="",width="28",command=lambda:resultado(Mapa[1][DialogCount-1]),font=("Helveltica",12))
boton_tres=Button(canvas,text="",width="28",command=lambda:resultado(Mapa[2][DialogCount-1]),font=("Helveltica",12))
boton_cuatro=Button(canvas,text="",width="28",command=lambda:resultado(Mapa[3][DialogCount-1]),font=("Helveltica",12))
boton_cinco=Button(canvas,text="",width="28",command=lambda:resultado(Mapa[4][DialogCount-1]),font=("Helveltica",12))
root.mainloop() 