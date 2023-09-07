from django.shortcuts import render, redirect
from django.core.mail import send_mail
from Hospital import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponse
import traceback

def inicio(request):
    return render(request, 'website/inicio.html')

def trabalhe_conosco(request):
    return render(request, 'website/trabalhe_conosco.html')

def sobre_nos(request):
    return render(request, 'website/sobre_nos.html')


def fale_conosco(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        from_email = settings.EMAIL_HOST_USER
        to_email = ['contatotht@hotmail.com']
        subject = 'Mensagens do Site '

        email_message = f"Nome: {nome}\nEmail: {email}\nTelefone: {phone}\nMensagem: {message}"
        send_mail(subject, email_message, from_email, to_email)
        messages.success(request, 'Mensagem enviada com sucesso!')
        return redirect('inicio')  # Pagina que será direcionado após enviar o form
    else:
        return HttpResponse('Algo deu errado.')


def enviar_cv(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        if not nome or not email or not phone:
            return HttpResponse('Os campos Nome, Email e Telefone são obrigatórios.')

        cv = request.FILES.get('cv')  # Aqui é FILES e não POST, pois é um arquivo.

        if not cv:
            return HttpResponse('O currículo é obrigatório.')

        from_email = settings.EMAIL_HOST_USER
        to_email = ['contatotht@hotmail.com']
        subject = 'Curriculos do Site '

        # Criar a mensagem:
        email_message = f"Nome: {nome}\nEmail: {email}\nTelefone: {phone}\nVeja o anexo para o currículo"

        mail = EmailMessage(subject, email_message, from_email, to_email)
        # anexando o cv
        mail.attach(cv.name, cv.read(), cv.content_type)

        try:
            mail.send()  # enviando o email
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            return HttpResponse('Erro ao enviar o currículo. Por favor, tente novamente.')

        messages.success(request, 'Seu currículo foi enviado com sucesso!')
        return redirect('trabalhe_conosco')  # Página que será direcionado após enviar o cv
    else:
        return HttpResponse('Método de solicitação não suportado.')
