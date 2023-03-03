from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import Cliente


def home(request):
    
    if request.method == "POST":

        def valida_cpf(cpf):
            cpf = cpf.replace(".", "").replace("-", "")
            
            if len(cpf) != 11 or not cpf.isdigit():  # verifica se o CPF tem 11 dígitos e se todos são números
                
                return False
            
            soma =  0

            for i in range(9):
                soma += int(cpf[i]) * (10-i)

            digito1 = 11 - (soma % 11)

            if digito1 > 9:
                digito1 = 0

            soma =  0

            for i in range(10):
                soma += int(cpf[i]) * (11 - i)

            digito2 = 11 - (soma % 11)

            if digito2 > 9:
                digito2 = 0

            if cpf[-2:] == str(digito1) + str(digito2):
                return True
            
            else:
                return False
        
        cpf = request.POST.get("cpf")
        
        nome = request.POST.get('nome')

        telefone = str(request.POST.get('telefone')).replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace('.', '')
        
        mensagem = str(request.POST.get('mensagem'))

        if cpf and nome and telefone:
        

            if valida_cpf(cpf):

                cliente = Cliente.objects.create(nome_completo=nome, CPF=cpf, telefone=telefone, mensagem=mensagem)

                cliente.save()

                context = {
                    'nome':nome,
                    'telefone':telefone,
                    'cpf':cpf,
                    'mensagem':mensagem
                    }

                html_content = render_to_string('emails/novo_cliente.html', context)
                text_content = strip_tags(html_content)

                email = EmailMultiAlternatives('Novo Cliente', text_content, settings.EMAIL_HOST_USER, ['requests@bnspromotora.com'] )
                email.attach_alternative(html_content, 'text/html')
                email.send()

                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Dados enviados com sucesso'
                )
                return redirect('home')
        
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'CPF Inválido!'
                )
                return redirect('home')
        else:
            messages.add_message(
                    request,
                    messages.ERROR,
                    'Preencha todos os campos!'
                )
            return redirect('home')
        

    return render(request,'pages/home.html')




