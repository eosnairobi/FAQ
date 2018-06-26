from celery import shared_task
from faq.models import Question, Answer, Mention
import re
from notifications.signals import notify
from map.models import BlockProducer
from django.contrib.auth.models import User


@shared_task
def parse_content(text, content_id):
    print(content_id)
    accounts = re.findall(r'(?:^|\s)(\@\w+)', text)
    for account in accounts:
        print(account)
        process_account.delay(account, content_id)


@shared_task
def process_account(account_name, content_id):
    if account_name.startswith('@'):
        bp = account_name.strip('@')
        print(bp)
        try:
            account = User.objects.get(username=bp)
            print('User Found')
        except Exception as e:
            print(str(e))
            try:
                account = BlockProducer.objects.get(account_name=bp)
            except Exception as e:
                print(str(e))
                account = None
        if account:
            print('account found')
            broadcast_question.delay(account.id, content_id)
        pass
    else:
        pass


@shared_task
def broadcast_question(account, content_id):
    try:

        object_ = Question.objects.get(id=content_id)
        print('Q Found')
    except Exception as e:
        print(str(e))
        object_ = Answer.objects.get(id=content_id)
        print('Answer found')
    if object_:
        deliver_message(object_, account)
    else:
        pass
    pass


@shared_task
def deliver_message(obj, account):
    print('Passed Accpint', account)
    sender = obj.author
    print('sender', sender)
    try:

        content = {'title': obj.title}
    except Exception as e:
        print(str(e))
        content = {'stuff': obj.content}
    # print(content)
    try:
        recipient = User.objects.get(id=account)
        print(recipient)
    except Exception as e:
        print(str(e))
        recipient = BlockProducer.objects.get(id=account)
        print('BP', recipient)
    Mention.objects.create(initiator=sender, mentioned=recipient, subject_url=obj.get_absolute_url())
    notify.send(sender, recipient=recipient, verb='Mentioned You At')
