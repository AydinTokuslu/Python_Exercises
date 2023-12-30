def student_credits():
    name_surname = input("please enter student name and surname: ")
    visa_note = float(input("please enter your visa note : "))
    final_note = float(input("please enter your final note : "))

    avr_note = (visa_note * 0.4) + (final_note * 0.6)
    print("Total average note : ", avr_note)

    if avr_note >= 90:
        letter_grade = "AA"
    elif avr_note >= 85:
        letter_grade = "BA"
    elif avr_note >= 80:
        letter_grade = "BB"
    elif avr_note >= 75:
        letter_grade = "CB"
    elif avr_note >= 70:
        letter_grade = "CC"
    elif avr_note >= 65:
        letter_grade = "DC"
    elif avr_note >= 60:
        letter_grade = "DD"
    else:
        letter_grade = "FF"

    print("{} named student average note {}, and achieved grade is {}".format(name_surname, avr_note, letter_grade))

    with open("grades.txt","a", encoding="utf-8") as file:
        file.write("{} named student average note {}, and achieved grade is {}\n".format(name_surname, avr_note, letter_grade))
        file.close()

num_of_students = int(input("how many students information will you enter : "))
for i in range(num_of_students):
    student_credits()