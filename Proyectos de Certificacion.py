def menu():
    while True:
        print('MENU PRINCIPAL Proyectos de certificacion Python')
        print('1: Formateador aritmetico')
        print('2: Calculadora de tiempo')
        #print('3: ')
        #print('4: ')
        #print('5: ')
        print('0: Para salir')
        print('______________________________')

        opcion = input("Por favor ingrese una opcion: ")

        if opcion == '1':
            def arithmetic_arranger(problems, show_answers=False):

                if len(problems) > 5:
                    return  'Error: Too many problems.'

                # Creo un diccionario para almacenar variables
                arranged_problems = {
                    'first_line':'',
                    'second_line':'',
                    'dash_line':'',
                    'answer_line':''
                }

                # Creo un for loop para iterar sobre el problema

                for problem in problems:
                    # Esto crea un espacio entre operador1, operador y operador2
                    operador1, operador, operador2 = problem.split()
                    # print(problem.split(), operador1, operador2, operador)
                    # Otro operador que no sea + o - return error
                    if operador not in ['+' , '-'] :
                        return "Error: Operator must be '+' or '-'."

                    # Solo acepta digitos
                    if not operador1.isdigit() or not operador2.isdigit():
                        return 'Error: Numbers must only contain digits.'

                    # Cada operador no puede tener mas de 4 digitos
                    if len(operador1) > 4 or len(operador2) > 4:
                        return 'Error: Numbers cannot be more than four digits.'

                    # Create spacing
                    width = max(len(operador1), len(operador2)) + 2

                    # Agregando al diccionario los valores para hacer la cuentas
                    arranged_problems['first_line'] += operador1.rjust(width) + '    '

                    arranged_problems['second_line'] += operador + ' ' + operador2.rjust(width - 2) + '    '

                    arranged_problems['dash_line'] += '-' * width + '    '

                    # If show_answer is true show answer
                    if show_answers:
                        if operador == '+':
                            answer = str(int(operador1) + int(operador2))
                        else:
                            answer = str(int(operador1) - int(operador2))

                        # Ordenando el resultado en el lugar apropiado
                        arranged_problems['answer_line'] += answer.rjust(width) + '    ' 

                # Mostar el resultado
                arranged_output = arranged_problems['first_line'].rstrip() + '\n'
                arranged_output += arranged_problems['second_line'].rstrip() + '\n'
                arranged_output += arranged_problems['dash_line'].rstrip()

                if show_answers:
                    arranged_output += '\n' + arranged_problems['answer_line'].rstrip()

                return arranged_output
                # return problems

            print(f'\n{arithmetic_arranger(["3233 + 1698", "3801 - 2", "45 + 43", "123 + 49"], True)}')
            print('______________________________')
        elif opcion == '2':
            def add_time(start, duration, day=None):
                # Declarar variables.
                start_hours = int(start.split(':')[0])
                start_minutes = int(start.split(':')[1][:2])
                start_meridian = start.split(':')[1][3:]

                duration_hours = int(duration.split(':')[0])
                duration_minutes = int(duration.split(':')[1][:2])

                # Convertir a 24hrs.
                if start_meridian == 'PM' and start_hours != 12:
                    start_hours += 12
                elif start_meridian == 'AM' and start_hours == 12:
                    start_hours = 0

                # Agregar duration horas y minutos
                total_hours = start_hours + duration_hours
                total_minutes = start_minutes + duration_minutes

                # Minutos desbordados arreglar
                if total_minutes >= 60:
                    total_hours += 1
                    total_minutes %= 60

                # Calcular los dias
                days_later = total_hours // 24
                hours_later = total_hours % 24

                # Convertir a 12hrs.
                #meridian = 'AM'
                if hours_later == 0:
                    hours_later = 12
                    start_meridian = 'AM'
                elif hours_later < 12:
                    start_meridian = 'AM'
                elif hours_later == 12:
                    start_meridian = 'PM'
                else:
                    hours_later -= 12
                    start_meridian = 'PM'

                # Opcional dias de la semana
                if day:
                    days_of_the_week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
                    day_index = days_of_the_week.index(day.capitalize())
                    end_day_index = (day_index + days_later) % 7 
                    end_day = days_of_the_week[end_day_index]
                else:
                    end_day = None

                # Formato para return
                formatted_time = f"{hours_later}:{total_minutes:02d} {start_meridian}"
                
                if end_day:
                    formatted_time += f", {end_day}"

                # Proximos dias mensaje
                if days_later == 1:
                    formatted_time += ' (next day)'
                elif days_later > 1:
                    formatted_time += f' ({days_later} days later)'


                print(formatted_time)
                
                return formatted_time
            add_time('11:43 PM', '24:20', 'tueSday')
            add_time('11:30 AM', '2:32', 'Monday')
            add_time('3:00 PM', '3:10')
            add_time('10:10 PM', '3:30')
            add_time('11:43 AM', '00:20')
            add_time('6:30 PM', '205:12')
            add_time('11:59 PM', '24:05')
            add_time('8:16 PM', '466:02')
            add_time('11:59 PM', '24:05', 'Wednesday')
            print('______________________________')
            
        elif opcion == '0':
            print('-----PROGRAMA FINALIZADO-----')
            print('______________________________')
            break
        else:
            
            print('Por favor ingrese una opcion valida')
            print('______________________________')
            
            
menu()

