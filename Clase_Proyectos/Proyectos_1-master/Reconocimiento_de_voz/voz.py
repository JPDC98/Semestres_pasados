#IMPORTAMOS RECURSOS NECESARIOS.
import pyaudio  
import wave  
import speech_recognition as sr 

chunk = 1024  

#FORMATO CREADO DE LA GRABACIÓN
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"

repetir = True

while repetir== True:
    try:
        #PROCEDEMOS A SELECCIÓNAR QUE QUEREMOS
        print("\n-------------------------------------------------------------------------------------")
        select = int(input("\ningrese (1) para reproducir, (2) para grabar y (3) para salir: "))
        print("\n\n")
        #REPRODUCIR AUDIO
        if select == 1:
            #ABRIMOS UBICACIÓN DEL AUDIO.  
            f = wave.open("/home/jose/Documentos/Repositorio_proyectos/file.wav","rb")
            #INICIAMOS LA LECTURA DEL AUDIO
            r = sr.Recognizer()
            #INICIAMOS PyAudio.
            p = pyaudio.PyAudio()  
            #ABRIMOS STREAM
            stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                            channels = f.getnchannels(),  
                            rate = f.getframerate(),  
                            output = True)

            #LEEMOS INFORMACIÓN  
            data = f.readframes(chunk)  

            #REPRODUCIMOS "stream"  
            while data:  
                stream.write(data)  
                data = f.readframes(chunk)  

            #PARAMOS "stream".  
            stream.stop_stream()  
            stream.close()  

            #FINALIZAMOS PyAudio  
            p.terminate() 
            with sr.AudioFile("/home/jose/Documentos/Repositorio_proyectos/file.wav") as source:
                voz = r.listen(source)
                try:
                    print("\n\nEsto es lo que dice el audio...\n\n")    
                    texto = r.recognize_google(voz, language='es-Es')
                    print(texto)
                except: 
                    print("Lo sentimos, algo salio mal")

        #GRABAR AUDIO    
        elif select == 2:
            audio = pyaudio.PyAudio()
            stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
            print("\n\ngrabando...")
            frames = []
            
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)
            print("\n\ngrabación terminada")
            
            
            # stop Recording
            stream.stop_stream()
            stream.close()
            audio.terminate()
            
            waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            waveFile.setnchannels(CHANNELS)
            waveFile.setsampwidth(audio.get_sample_size(FORMAT))
            waveFile.setframerate(RATE)
            waveFile.writeframes(b''.join(frames))
            waveFile.close()  
        elif select==3:
            repetir = False
            print("Pase buen día\n\n")     
        else:
            print("Ingreso una opcion inexistente")      
    except:
        print("El programa a tenido un error fatal")
    