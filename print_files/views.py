from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from print_files.models import Print_File
from print_files.serializer import PrintFileSerializer
from user.models import User
from exercise.models import Exercise
from exam.models import Exam
from print_files.generatePdf import PDF
from file.models import File

from rest_framework import viewsets
from text_unidecode import unidecode

class PrintFileViewSet(viewsets.ModelViewSet):
    queryset = Print_File.objects.all()
    serializer_class = PrintFileSerializer




@csrf_exempt
@api_view(['POST', ])
def print_single_file(request):
    print('inside print single file')
    if request.method == 'POST':

        # Load json data from body

        user_id = request.data['user_id']
        print_type = request.data['print_type']

        new_file_name = ""

        if print_type == 'single':
            file_id = request.data['file_id']
            file_instance = File.objects.get(pk=file_id)
            user_instance = User.objects.get(username=file_instance.user.username)
            exercise_instance = Exercise.objects.get(pk=file_instance.exercise.id)
            exam_instance = Exam.objects.get(pk=exercise_instance.exam.id)

            date = str(file_instance.date_created.strftime("%d/%m/%Y %H:%M:%S"))
            exam_name = exam_instance.name
            full_name = user_instance.first_name + user_instance.last_name
            username = user_instance.username
            exercise_name = exercise_instance.name
            file_name = file_instance.name
            header_text_val = date+" "+exam_name+" "+full_name+" "+username+" "+exercise_name+" "+file_name

            bf = file_instance.file_obj.read().decode("utf_8", 'replace')
            bf = unidecode(bf)
            pdf = PDF()

            pdf.Val(header_text_val)

            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 5, bf)
            pdf.output("simple_demo.pdf").encode('latin-1')
            new_file_name = "print_"+ file_name
        else:
            file_list = request.data['file_list']
            pdf_bulk = PDF()
            tempuserObj = None
            counter = 0
            for file_item in file_list:

                file_instance = File.objects.get(pk=file_item)
                user_instance = User.objects.get(username=file_instance.user.username)
                exercise_instance = Exercise.objects.get(pk=file_instance.exercise.id)
                exam_instance = Exam.objects.get(pk=exercise_instance.exam.id)

                date = str(file_instance.date_created.strftime("%d/%m/%Y %H:%M:%S"))
                exam_name = exam_instance.name
                full_name = user_instance.first_name + user_instance.last_name
                username = user_instance.username
                exercise_name = exercise_instance.name
                file_name = file_instance.name
                header_text_val = date+" "+exam_name+" "+full_name+" "+username+" "+exercise_name+" "+file_name

                bf = file_instance.file_obj.read().decode("utf_8", 'replace')
                bf = unidecode(bf)
                new_file_name = "print_bulk_"+ exercise_instance.exam.name



                # Name, Exam, Date, Time, and loginID
                frontPage_name = "Name: " + full_name
                frontPage_exam = "Exam: " + exam_name
                frontPage_date = "Date: " + date
                frontPage_timeSlot = "Time: "+ user_instance.time_slot.start_time + "-"+ user_instance.time_slot.end_time
                frontPage_loginId = "Login ID: " + user_instance.username
                # First condition to add Head Page
                if counter == 0:
                    print("First condition")
                    tempuserObj = user_instance
                    pdf_bulk.Val(header_text_val)
                    pdf_bulk.add_page()
                    pdf_bulk.set_font("Arial", size=12)
                    pdf_bulk.cell(0, 5, txt=frontPage_name)
                    pdf_bulk.ln(10)
                    pdf_bulk.cell(0, 5, txt=frontPage_exam)
                    pdf_bulk.ln(10)
                    pdf_bulk.cell(0, 5, txt=frontPage_date)
                    pdf_bulk.ln(10)
                    pdf_bulk.cell(0, 5, txt=frontPage_timeSlot)
                    pdf_bulk.ln(10)
                    pdf_bulk.cell(0, 5, txt=frontPage_loginId)
                counter = counter + 1

                if counter !=0 and tempuserObj != user_instance:
                    print("not equal condition")
                    tempuserObj = user_instance
                    pdf_bulk.add_page()
                    pdf_bulk.set_font("Arial", size=12)
                    pdf_bulk.cell(0, 5, txt="Signature:")
                    pdf_bulk.ln(10)
                    pdf_bulk.Val(header_text_val)
                    pdf_bulk.add_page()
                    pdf_bulk.cell(0, 5, txt=frontPage_name)
                    pdf_bulk.ln(10)
                    pdf_bulk.cell(0, 5, txt=frontPage_exam)
                    pdf_bulk.ln(10)
                    pdf_bulk.cell(0, 5, txt=frontPage_date)
                    pdf_bulk.ln(10)
                    pdf_bulk.cell(0, 5, txt=frontPage_timeSlot)
                    pdf_bulk.ln(10)
                    pdf_bulk.cell(0, 5, txt=frontPage_loginId)
                pdf_bulk.Val(header_text_val)
                pdf_bulk.add_page()
                pdf_bulk.multi_cell(0, 5, bf)
                if counter == len(file_list):
                    pdf_bulk.add_page()
                    pdf_bulk.set_font("Arial", size=12)
                    pdf_bulk.cell(0, 5, txt="Signature:")
            pdf_bulk.output("simple_demo.pdf").encode('latin-1')

        f = open("simple_demo.pdf", 'rb')
        from django.core.files import File as filexx

        file_obj = filexx(f)



        user_obj = User.objects.get(username=user_id)
        new_file = Print_File(
            name=new_file_name,
            is_submitted=False,
            file_obj=file_obj,
            user=user_obj,
            subject_id=file_instance.subject.id
        )

        new_file.save()
        f.close()


        return JsonResponse({'msg': 'Successfully Assigned!', 'success': 1}, status=status.HTTP_200_OK)

    else:
        return JsonResponse({'msg': 'Method not allowed!', 'success': 0}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
