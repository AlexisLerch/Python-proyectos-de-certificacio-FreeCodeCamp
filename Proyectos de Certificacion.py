def menu():
    while True:
        #print('______________________________')
        print('MENU PRINCIPAL Proyectos de certificacion Python')
        print('1: Formateador aritmetico')
        #print('2: Luhn')
        #print('3: Expenses tracker')
        #print('4: Case converter')
        #print('5: Square root')
        print('0: Para salir')
        print('______________________________')

        opcion = input("Por favor ingrese una opcion: ")

        if opcion == '1':
            print('______________________________')
            pass
        elif opcion == '0':
            print('-----PROGRAMA FINALIZADO-----')
            print('______________________________')
            break
        else:
            
            print('Por favor ingrese una opcion valida')
            print('______________________________')
            
            
menu()

