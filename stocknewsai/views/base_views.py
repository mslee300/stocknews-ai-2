from django.shortcuts import render, get_object_or_404, redirect
from stocknewsai.models import Email
from stocknewsai.forms import EmailForm
from django.utils import timezone
from django.template.loader import render_to_string
# from django.core.mail import EmailMessage
from django.contrib import messages
from django.utils.html import strip_tags
# from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail


def send_confirm_email(request, to_email):
    subject = '🗞️ Welcome to Stocknews AI!'
    html_message = render_to_string('confirm_email.html')
    plain_message = strip_tags(html_message)
    from_email = 'stocknewsai@gmail.com'
    to = to_email
    if send_mail(subject, plain_message, from_email, [to], html_message=html_message):
      pass
    else:
      messages.error(request, f'Problem sending email to {to_email}, please check if you typed it correctly.')


def send_stocknews_email(request, to_email):
    subject = '🗞️ Apple savings accounts, iOS 17 app sideloading, end of giant AI models'
    html_message = render_to_string('stocknews_email.html')
    plain_message = strip_tags(html_message)
    from_email = 'stocknewsai@gmail.com'
    to = to_email
    if send_mail(subject, plain_message, from_email, [to], html_message=html_message):
      pass
    else:
      messages.error(request, f'Problem sending email to {to_email}, please check if you typed it correctly.')
      

def index(request):
  if request.method == 'POST':
      form = EmailForm(request.POST)
      if form.is_valid():
          email = form.save(commit=False)
          email.create_date = timezone.now()
          email.save()
          # Send a confirmation email
          user_email = form['email'].value()
          # send_confirm_email(request, user_email)
          send_stocknews_email(request, user_email)
        
          return redirect('/stocknewsai/subscribed')
  else:
      form = EmailForm()
  context = {'form': form}
  return render(request, 'stocknewsai/index.html', context)