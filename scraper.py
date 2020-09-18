import requests

from bs4 import BeautifulSoup

import smtplib

import time

URL = "https://www.amazon.in/Mediweave-KN95-Equivalent-Respirator-certified/dp/B087N2WPLT?pf_rd_r=TNHRQMYJ6C0ZQT8VRAY6&pf_rd_p=93c03e60-301b-482c-aedb-31792d163881&pd_rd_r=9f67ec93-53ad-4d0a-bb7b-d285cd9efd30&pd_rd_w=V6XKi&pd_rd_wg=m1H6j&ref_=pd_gw_unk"

headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}

def check_price():


    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    #print(soup.prettify())
    title = soup.find(id="title").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:5])

    if(converted_price < 1,700):
        send_mail()

    print(title.strip())
    print(converted_price)

    if(converted_price < 1,700):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('chandramohancse7@gmail.com','programerwork')

    subject = 'price fell down!'
    body = 'check the amazon link  https://www.amazon.in/Mediweave-KN95-Equivalent-Respirator-certified/dp/B087N2WPLT?pf_rd_r=TNHRQMYJ6C0ZQT8VRAY6&pf_rd_p=93c03e60-301b-482c-aedb-31792d163881&pd_rd_r=9f67ec93-53ad-4d0a-bb7b-d285cd9efd30&pd_rd_w=V6XKi&pd_rd_wg=m1H6j&ref_=pd_gw_unk'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        
        'chandramohancse7@gmail.com',
        'chandrashanmugam007@gmail.com',
         msg
    )
    print('HEY CHECK OUT YOUR MAIL')
    server.quit()

while(True):
    check_price()
    time.sleep(60*60)  






