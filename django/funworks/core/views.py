from django.shortcuts import render, redirect
from funworks.core.models import PagamentosFunworks
from funworks import settings
import ldap

def logar(request):
    user = request.POST.get("user", "")
    password = request.POST.get("pass", "")

    con = ldap.initialize(settings.LDAP_HOST)
    con.set_option(ldap.OPT_REFERRALS,0)

    con.simple_bind_s(settings.LDAP_USER, settings.LDAP_PASS)
    response = con.search_s('OU=KEYWORKS,DC=keyworks,DC=com,DC=br', ldap.SCOPE_SUBTREE, "(&(sAMAccountName={}))".format(user))

    if user=='':
        return redirect('/')

    try:
        con.simple_bind_s(response[0][0], password)
        request.session['is_logged'] = True
        usuario = response[0][1]['name'][0].decode()
        email = response[0][1]['mail'][0].decode()
        request.session['user_nome'] = usuario
        request.session['user_mail'] = email
    except Exception as e:
        pass

    return redirect('/')


def login(request):
    return  render(request, 'login.html')


# Create your views here.
def home(request):
    if request.session.get('is_logged', False) == False:
        return redirect('/login')
    nome = request.session['user_nome']
    email = request.session['user_mail']
    email_query = email
    if '@veltus.com.br' in email:
        email_query = email.replace('@veltus.com.br', '@keyworks.com.br')

    pagamentos = PagamentosFunworks\
                        .objects.using('funworks')\
                        .order_by('vencimentoConta')\
                        .filter(emailCliente=email_query)\
                        .all()

    context = {
        'nome':nome,
        'mail':email,
        'pagamentos':pagamentos
    }

    return render(request, 'home.html',context )

def loggoff(request):
    request.session['is_logged'] = False
    request.session['user_nome'] = ''
    request.session['user_mail'] = ''
    return redirect('/')


def como_pagar(request):

    nome = request.session['user_nome']
    email = request.session['user_mail']

    context = {
        'nome':nome,
        'mail':email,
    }
    
    return render(request, 'como_pagar.html', context)
    