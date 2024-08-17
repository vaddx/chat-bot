import telebot

from telebot import types


bot = telebot.TeleBot('7405453669:AAHefuofJR-BT7z5TMu7SHfN1eXrSIYAAXI')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    butt1 = types.InlineKeyboardButton('Джйотиш', callback_data='Джйотиш')
    butt2 = types.InlineKeyboardButton('Практики', callback_data='Практики')
    butt3 = types.InlineKeyboardButton('Подкасты', callback_data='Подкасты')
    butt4 = types.InlineKeyboardButton('Записаться на консультацию', callback_data='Записаться на консультацию')
    markup.add(butt1)
    markup.row(butt2, butt3)
    markup.add(butt4)
    file = open('start.jpg', 'rb')
    bot.send_photo(message.chat.id, file, caption='''Кто Я? - как часто ты задаешь себе этот вопрос, но смогла ли ты найти на него ответ?

Для начала я отвечу на вопрос кто Я
Меня зовут Руслана и я ведический астролог Джйотиш, эксперт по предназначению!

Я несколько лет глубинно изучаю ведическую науку, которая включает в себя психологию, астрологию, философию и антропологию! Джйотиш поможет тебе заглянуть внутрь себя и откроет твое истинное предназначение! И самое главное, поможет тебе ответит на твой вопрос: Кто Я? 
Хочешь узнать больше - нажми на кнопку Джйотиш!

В разделе Практики, ты найдешь тантрические и психологические практики - они помогут тебе лучше познать свой внутренний мир, а самое главное они учат проживать каждый день в гармонии с собой! 

Я помогу тебе ответить на главный вопрос - "Кто Я?"''', reply_markup=markup)


markup = types.InlineKeyboardMarkup()
start = types.InlineKeyboardButton('Перейти в начало', callback_data='start')
@bot.callback_query_handler(func=lambda callback: True)
def callback(callback):

    # Джйотиш
    if callback.data == 'Джйотиш':
        markup = types.InlineKeyboardMarkup()
        butt1 = types.InlineKeyboardButton('Натальная карта - это', callback_data='Натальная карта - это')
        butt2 = types.InlineKeyboardButton('Урок как построить натальную карту', callback_data='Урок как построить натальную карту')
        markup.add(butt1)
        markup.add(butt2)
        markup.add(start)
        file = open('джйотиш.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file, caption='Джйотиш - в этом разделе я расскажу тебе более подробно о ведичсекой астрологии, ты сможешь понять на какие вопросы может дать ответ твоя натальная карта!', reply_markup=markup)

    elif callback.data == 'Натальная карта - это':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True)
        butt = types.KeyboardButton('Назад')
        markup.row(butt)
        bot.send_message(callback.message.chat.id, '''Хотите узнать, что скрывает ваша натальная карта в ведической астрологии? Этот древний инструмент способен пролить свет на 12 важнейших сфер вашей жизни! 

Натальная карта - это изображение расположения планет и звезд в момент вашего рождения.

в видео я подробно рассказываю про 12 сфер или 12 домов натальной карты!
https://youtu.be/NIv9z2R6OV8?si=EkhsBYHuCNCuJF1f''', reply_markup=markup)
    elif callback.data == 'Урок как построить натальную карту':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True)
        butt = types.KeyboardButton('Назад')
        markup.add(butt)
        bot.send_message(callback.message.chat.id, '''В этом видео я рассказываю как самостоятельно ты сможешь построить свою натальную карту по Джйотиш!

Что бы построить натальную карту переходи на сайт: https://saturn.love/ru/

Но обязана предупредить, без ректификации невозможно быть уверенным что это именно твой гороскоп.

Более подробно, что такое ректификация я рассказываю в разделе "Записаться на консультацию"!
https://youtu.be/6fgxlufu_8M?si=drBjcjgfRGqsJVnR''', reply_markup=markup)
    # Джйотиш


    # Практики
    if callback.data == 'Практики':
        markup = types.InlineKeyboardMarkup()
        markup.add(start)
        file = open('практики.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file, caption='''В этом разделе я для тебя собрала тантрические и психологические практики! Они помогут тебе улучшить твое эмоциональное состояние, избавят от хаоса мыслей в голове! А главная цель Тантры - это достичь гармонии с собой и проживать каждый день в удовольствие!


✔️Выбери практику с которой хочешь начать и отправь ее номер:
1. "Толкование снов" - это практика не являться сонником, это практика поможет тебе расшифровать твой сон самостоятельно! Ведь сон - это разговор с твоим подсознанием!
2. "Тратака" - это практика учит концентрации, избавляет от хаоса мыслей в твоей голове!
3. "100 Удовольствий" - она научит тебя быть счастливой здесь и сейчас!
4. "Зеркала" - это моя авторская медитация, которая позволит тебе подружиться с тем, что ты отвергаешь в себе, со своей тенью.
5. "Круг света" - это практика для женщин, для тех кто хочет взрастить в себе сексуальную энергию или наоборот снять сексуальное напряжение.''', reply_markup=markup)
    # Практики


    # Подкасты
    if callback.data == 'Подкасты':
        markup = types.InlineKeyboardMarkup()
        butt1 = types.InlineKeyboardButton('Тень личности', callback_data='Тень личности')
        butt2 = types.InlineKeyboardButton('Позитивное мышление',
                                           callback_data='Позитивное мышление')
        markup.add(butt1)
        markup.add(butt2)
        markup.add(start)
        file = open('подкасты.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file, caption='Подкасты - это разговор о сложном простыми словами, здесь я раскрываю темы без знания которых невозможно начать путь своей реализации, эти знания помогут тебе не только понять Кто Ты?, но и поменяют твое мышление, эти знания помогут тебе изменить твою реальность!', reply_markup=markup)
    elif callback.data == 'Тень личности':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True)
        butt = types.KeyboardButton('Вернуться к списку подкастов')
        markup1.add(butt)
        bot.send_message(callback.message.chat.id, '''Подкаст про ТЕНИ нашей личности - объяснить сложно, это нужно слушать, эта информация перевернет ваше представление о вас!
https://t.me/ruslana_astrolog_jyotish/26''', reply_markup=markup1)
    elif callback.data == 'Позитивное мышление':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True)
        butt = types.KeyboardButton('Вернуться к списку подкастов')
        markup1.add(butt)
        bot.send_message(callback.message.chat.id, '''Подкаст про ПОЗИТИВНОЕ мышление, позитивное мышление является ключевым фактором для достижения успеха! Это самое первое правило. которое нужно приметь в своей жизни если ты хочешь выйти на новый уровень!
https://t.me/ruslana_astrolog_jyotish/24''', reply_markup=markup1)

    # Подкасты

    # Запись
    if callback.data == 'Записаться на консультацию':
        markup = types.InlineKeyboardMarkup()
        butt1 = types.InlineKeyboardButton('WhatsApp', url='https://sblnk.ru/788371770')
        butt2 = types.InlineKeyboardButton('Telegram', url='https://t.me/AkbasovaRuslana')
        markup.row(butt1, butt2)
        markup.add(start)
        file = open('джйотиш.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file)
        bot.send_message(callback.message.chat.id, '''Для того что бы записаться на консультацию напиши мне: 
Telegram: @AkbasovaRuslana
WA: +77056605911

Консультация проходит в онлайн формате по видеосвязи в два этапа:

1 этап: Ректификация - это первый созвон с тобой, где мы будем разговаривать о твоей жизни, мои клиенты эту часть консультации называют - сеанс у тантрического психолога. Этот этап необходим для того, что бы точно определить твою натальную карту, ведь просто даты, времени и места рождения не хватает для точного определения твоего гороскопа! Без ректификации НЕВОЗМОЖНО вывести ПРЕДНАЗНАЧЕНИЕ!

2 этап: Вывод предназначения - это второй созвон с тобой через пару дней после ректификации, где я полностью раскрою тайны твоего гороскопа и отвечу на твой главный вопрос: Кто Я?
Я раскрою все 12 сфер твоего гороскопа и отвечу на все твои вопросы!

Каждый этап консультации по времени занимает от двух до трех часов!

После консультации мы остаемся на связи, и ты всегда сможешь задавать вопросы мне лично!

Остались вопросы, напиши мне и я с удовольствием отвечу на них.

С уважением твой ведичсекий астролог, Руслана!''', reply_markup=markup )
    # Запись

        # Практики
    if callback.data == 'back':
        markup = types.InlineKeyboardMarkup()
        markup.add(start)
        file = open('практики.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file, caption='''В этом разделе я для тебя собрала тантрические и психологические практики! Они помогут тебе улучшить твое эмоциональное состояние, избавят от хаоса мыслей в голове! А главная цель Тантры - это достичь гармонии с собой и проживать каждый день в удовольствие!


    ✔️Выбери практику с которой хочешь начать и отправь ее номер:
    1. "Толкование снов" - это практика не являться сонником, это практика поможет тебе расшифровать твой сон самостоятельно! Ведь сон - это разговор с твоим подсознанием!
    2. "Тратака" - это практика учит концентрации, избавляет от хаоса мыслей в твоей голове!
    3. "100 Удовольствий" - она научит тебя быть счастливой здесь и сейчас!
    4. "Зеркала" - это моя авторская медитация, которая позволит тебе подружиться с тем, что ты отвергаешь в себе, со своей тенью.
    5. "Круг света" - это практика для женщин, для тех кто хочет взрастить в себе сексуальную энергию или наоборот снять сексуальное напряжение.''',
                           reply_markup=markup)

        # Практики

    # start
    if callback.data == 'start':
        markup = types.InlineKeyboardMarkup()
        butt1 = types.InlineKeyboardButton('Джйотиш', callback_data='Джйотиш')
        butt2 = types.InlineKeyboardButton('Практики', callback_data='Практики')
        butt3 = types.InlineKeyboardButton('Подкасты', callback_data='Подкасты')
        butt4 = types.InlineKeyboardButton('Записаться на консультацию', callback_data='Записаться на консультацию')
        markup.add(butt1)
        markup.row(butt2, butt3)
        markup.add(butt4)
        file = open('start.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file, caption='''Кто Я? - как часто ты задаешь себе этот вопрос, но смогла ли ты найти на него ответ?

Для начала я отвечу на вопрос кто Я:
Меня зовут Руслана и я ведический астролог Джйотиш, эксперт по предназначению!

Я несколько лет глубинно изучаю ведическую науку, которая включает в себя психологию, астрологию, философию и антропологию! Джйотиш поможет тебе заглянуть внутрь себя и откроет твое истинное предназначение! И самое главное, поможет тебе ответит на твой вопрос: Кто Я? 
Хочешь узнать больше - нажми на кнопку Джйотиш!

В разделе Практики, ты найдешь тантрические и психологические практики - они помогут тебе лучше познать свой внутренний мир, а самое главное они учат проживать каждый день в гармонии с собой! 

Я помогу тебе ответить на главный вопрос - "Кто Я?"''', reply_markup=markup)
    # start



@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == 'Назад':
        markup = types.InlineKeyboardMarkup()
        butt1 = types.InlineKeyboardButton('Натальная карта - это', callback_data='Натальная карта - это')
        butt2 = types.InlineKeyboardButton('Урок как построить натальную карту', callback_data='Урок как построить натальную карту')
        butt3 = types.InlineKeyboardButton('Перейти в начало', callback_data='start')
        markup.add(butt1)
        markup.add(butt2)
        markup.add(butt3)
        file = open('джйотиш.jpg', 'rb')
        bot.send_photo(message.chat.id, file,
                       caption='''Джйотиш - в этом разделе я расскажу тебе более подробно о ведичсекой астрологии, ты сможешь понять на какие вопросы может дать ответ твоя натальная карта!''',
                       reply_markup=markup)
    if message.text == 'Вернуться к списку подкастов':
        markup = types.InlineKeyboardMarkup()
        butt1 = types.InlineKeyboardButton('Тень личности', callback_data='Тень личности')
        butt2 = types.InlineKeyboardButton('Позитивное мышление',
                                               callback_data='Позитивное мышление')
        butt3 = types.InlineKeyboardButton('Перейти в начало', callback_data='start')
        markup.add(butt1)
        markup.add(butt2)
        markup.add(butt3)
        file = open('подкасты.jpg', 'rb')
        bot.send_photo(message.chat.id, file, caption='Подкасты - это разговор о сложном простыми словами, здесь я раскрываю темы без знания которых невозможно начать путь своей реализации, эти знания помогут тебе не только понять Кто Ты?, но и поменяют твое мышление, эти знания помогут тебе изменить твою реальность!', reply_markup=markup)


    if message.text == '1':
            markup = types.InlineKeyboardMarkup()
            butt1 = types.InlineKeyboardButton('Вернуться к списку практик', callback_data='back')
            markup.add(butt1)

            bot.send_message(message.chat.id, '''"Толкование снов” - эта практика имеет важное значение для
понимания внутреннего мира человека и его бессознательных
процессов - это путь к самопознанию.

https://files.salebot.pro/uploads/file_item/31366151/file/438680/Толкование_снов.pdf''', reply_markup=markup)

    elif message.text == '2':
            markup = types.InlineKeyboardMarkup()
            butt1 = types.InlineKeyboardButton('Вернуться к списку практик', callback_data='back')
            markup.add(butt1)
            with open('Практика_концентрации_внимания.pdf', 'rb') as pdf:
                bot.send_document(message.chat.id, pdf , caption='''"Тратака" - эта практика помогает развить концентрацию,
усилить интуицию, успокоить ум и достичь медитативных
состояний. Это очень ценная практика для духовного роста и
самопознания.''', reply_markup=markup)

    elif message.text == '3':
            markup = types.InlineKeyboardMarkup()
            butt1 = types.InlineKeyboardButton('Вернуться к списку практик', callback_data='back')
            markup.add(butt1)
            with open('Практика_100_удовольствий.pdf.pdf', 'rb') as pdf:
                bot.send_document(message.chat.id, pdf , caption='''“100 удовольствий“ - это эффективный инструмент для
повышения осознанности, она научит получать удовольствие
от жизни и напомнит каждому, как прекрасна ваша жизнь.''', reply_markup=markup)

    elif message.text == '4':
            markup = types.InlineKeyboardMarkup()
            butt1 = types.InlineKeyboardButton('Вернуться к списку практик', callback_data='back')
            markup.add(butt1)
            bot.send_message(message.chat.id,  ''''Зеркала” - это моя авторская медитация! которая позволит тебе
подружиться с теми своими качествами, которые ты
отвергаешь в себе, она позволяет подружиться со своей тенью!
Если вы не знакомы с таким выражением, как тень, рекомендую
перед тем как слушать медитацию, прослушать мой подкаст на
тем теней.
https://youtu.be/h0X_aMFF-Ns?si=rUhGNgn-4q-0Pwe_''' ,reply_markup=markup)

    elif message.text == '5':
            markup = types.InlineKeyboardMarkup()
            butt1 = types.InlineKeyboardButton('Вернуться к списку практик', callback_data='back')
            markup.add(butt1)
            with open('Священный_храм_женщины.pdf.pdf', 'rb') as pdf:
                bot.send_document(message.chat.id, pdf , caption='''Круг света“ - эта практика помогает активировать женскую
сексуальность, так же она помогает снять сексуальное
напряжение. Очень нужная и полезная практика для женщин
которые в данный момент не состоят в отношениях!''', reply_markup=markup)

bot.infinity_polling()