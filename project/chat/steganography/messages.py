from rest_framework.decorators import api_view
from chat.models import *
import sqlite3
from django.db import connection
from random import randint
from django.shortcuts import render, redirect
import json
from django.shortcuts import get_object_or_404
from datetime import date

@api_view(['GET','POST'])
def quotes(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            data = json.loads(request.data['data'])
            html_page = 'replyPage.html'

            main_message_id = get_object_or_404(MessageTable, id=data['main_message_id'])

            RelySave = ReplyTable(
            message = data['reply_message'],
            replyTo = main_message_id,
            main_message = data['main_message'],
            repliedBy = request.user,
            message_id = main_message_id.id
            )
            RelySave.save()

            context = {'message': 'Reply sent successfully'}
        elif request.method == 'GET':
            today_date = date.today()
            # count = MessageTable.objects.filter(authorizedTo = request.user).count()
            todaymessage = MessageTable.objects.filter(authorizedTo = request.user, receivedDate=today_date).first()
            if not todaymessage:
                try:
                    selectQuery = MessageTable.objects.filter(authorizedTo = request.user, readed=False).all().order_by('?').first()
                except:
                    selectQuery = MessageTable.objects.filter(authorizedTo = request.user).all()[0]
                if not selectQuery:
                    selectQuery = MessageTable.objects.filter(authorizedTo = request.user).all()[0]

                selectQuery.readed=True
                selectQuery.readBy=request.user.username

                from datetime import datetime
                selectQuery.seenDate=datetime.now()
                selectQuery.receivedDate=today_date
                selectQuery.save()
                message = selectQuery.message
                message_id = selectQuery.id
            else:

                message = todaymessage.message
                message_id = todaymessage.id

            html_page = "message.html"
            context = {'message':message, 'id':message_id}

        return render(request, html_page, context=context)
    else:
        return redirect("login-user")

# @api_view(['GET','POST'])
# def history(request):
#     if request.user.is_authenticated():
#         if request.method == 'GET':

# @api_view(['GET','POST'])
# def authorScreen(request):
#     if request.user.is_authenticated and request.user.username == 'vengi':
#         if request.method == 'POST':
#             data = json.loads(request.data['data'])
#             userreplymessage = get_object_or_404(ReplyTable, id = data['reply_message'])

#             AuthorReply = MainMessageReply(
#                 message = data['message'],
#                 replyTo = userreplymessage,
#                 repliedBy = request.user,
#                 main_message = userreplymessage.main_message,
#                 reply_id = userreplymessage.id
#             )

#             AuthorReply.save()
#             return render(request, "authorReplyPage.html",context={'data':AuthorReply})
#         else:
            
#             data={'MessageData': MessageTable.objects.all().values(),
#                     'ReplyData':ReplyTable.objects.all().values(),
#                     'AuthorReply': MainMessageReply.objects.all().values(),
#                     'HistoryTable': HistoryTable.objects.all().values()}

#             return render(request, "authorReplyPage.html", context={'data':data})

#     else:
#         return redirect("login-user")

# # def adminget(request):