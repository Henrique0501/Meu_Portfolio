from flask import render_template, request, flash, redirect
from enviar_email import mandar_email
from main import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    tel = request.form['tel']
    subject = request.form['subject']
    msg = request.form['msg']

    mandar_email('mf.henrique05@gmail.com', subject,
                 'Olá, Henrique'
                 '\nNovo email mandado a partir do seu site\n'
                 f'\nNome: {name}'
                 f'\nEmail: {email}'
                 f'\nTelefone: {tel}\n'
                 f'\nMensagem:\n{msg}')

    flash('Sua mensagem foi entregue', 'success')

    return redirect('/#contact')


@app.route('/sites')
def sites():
    return render_template('sites.html')
