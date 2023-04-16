import calendar
import bson
import datetime
import json
import telebot
bot = telebot.TeleBot('token')

def s(ss):
    lables, lables_check, dataset = [], [], []
    js = open('sample_collection.bson', 'rb+')

    dt_from = (ss.partition("om\": \"")[2]).partition("\", \"dt_upto")[0]
    dt_upto = ss.partition("\"dt_upto\": \"")[2].partition("\", \"group_type\"")[0]

    group_type = (ss.partition("\", \"group_type\": \"")[2])[:-2]
    
    base =0

    if group_type =='day':
        next = datetime.datetime.strptime(dt_from, '%Y-%m-%dT00:00:00')
        while True:
            dataset.append(0)
            lables.append(next.strftime('%Y-%m-%dT00:00:00'))
            next = next + datetime.timedelta(days=1)
            if  next >datetime.datetime.strptime(dt_upto, '%Y-%m-%dT%H:%M:%S'):break
        js1 =(js.read())
        while base < len(js1):
            base, d = bson.decode_document(js1, base)
            if (d['dt'].strftime('%Y-%m-%dT00:00:00')) in lables:
                dataset[(lables.index((d['dt'].strftime('%Y-%m-%dT00:00:00'))))] +=d['value']
    if group_type == 'hour':
        next = datetime.datetime.strptime(dt_from, '%Y-%m-%dT%H:00:00')
        while True:
            dataset.append(0)
            lables.append(next.strftime('%Y-%m-%dT%H:00:00'))
            next = next + datetime.timedelta(hours=1)
            if next > datetime.datetime.strptime(dt_upto, '%Y-%m-%dT%H:%M:%S'): break
        js1 = (js.read())
        while base < len(js1):
            base, d = bson.decode_document(js1, base)
            if (d['dt'].strftime('%Y-%m-%dT%H:00:00')) in lables:
                dataset[(lables.index((d['dt'].strftime('%Y-%m-%dT%H:00:00'))))] += d['value']
        dataset[-1] = 0
    if group_type == 'week':
        next = datetime.datetime.strptime(dt_from, '%Y-%m-%dT00:00:00')
        while True:
            dataset.append(0)
            lables.append(next.strftime('%Y-%m-%dT00:00:00'))
            next = next + datetime.timedelta(days=7)
            if next > datetime.datetime.strptime(dt_upto, '%Y-%m-%dT%H:%M:%S'): break
        js1 = (js.read())
        while base < len(js1):
            base, d = bson.decode_document(js1, base)
            if (d['dt'].strftime('%Y-%m-%dT00:00:00')) in lables:
                dataset[(lables.index((d['dt'].strftime('%Y-%m-%dT00:00:00'))))] += d['value']
    if group_type == 'month':
        next = datetime.datetime.strptime(dt_from, '%Y-%m-%dT%H:%M:%S')
        while True:
            dataset.append(0)
            lables.append(next.strftime('%Y-%m-01T00:00:00'))


            in_month = calendar.monthrange(int(next.strftime('%Y')),int(next.strftime('%m')))
            next= next + datetime.timedelta(days=in_month[1])

            if next >= datetime.datetime.strptime(dt_upto, '%Y-%m-%dT%H:%M:%S'): break
        js1 = (js.read())
        while base < len(js1):
            base, d = bson.decode_document(js1, base)
            if (d['dt'].strftime('%Y-%m-01T00:00:00')) in lables:
                dataset[(lables.index((d['dt'].strftime('%Y-%m-01T00:00:00'))))] += d['value']
    
    jsl = '["' + '", "'.join(lables) + '"]'
    lables = '"labels": ' + jsl+'}'
    jsl = '[' + ', '.join(map(str, dataset)) + ']'
    dataset = '{"dataset": ' + jsl
    return str(dataset)+', '+str(lables)

@bot.message_handler(content_types=['text'])

def get_input(message):
    global in_data
    in_data = message.text
    out_tex = s(in_data)
    bot.send_message(message.from_user.id, out_tex)
    bot.register_next_step_handler(message, get_input)
bot.polling(none_stop=True, interval=0)
