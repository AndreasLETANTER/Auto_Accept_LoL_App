from enum import auto
import pyautogui
import logging
import time
import datetime
import os
import sys

def ban_champ():
    accept = pyautogui.locateOnScreen('resources/jgl.png', confidence=0.6)
    ban = pyautogui.locateOnScreen('resources/ban.png', confidence=0.6)
    if (accept != None and ban != None):
        accept = pyautogui.center(accept)
        acceptx, accepty = accept
        pyautogui.click(acceptx, accepty + 50)
        ban = pyautogui.center(ban)
        banx, bany = ban
        time.sleep(0.5)
        pyautogui.click(banx, bany)

def auto_ban_engine(name, date_string):
    accept = pyautogui.locateOnScreen('resources/search.png', confidence=0.9)
    ban = pyautogui.locateOnScreen('resources/ban_check.png', confidence=0.9)
    if (accept != None and ban != None):
        logging.info(date_string + ' banning...')
        accept = pyautogui.center(accept)
        acceptx, accepty = accept
        pyautogui.click(acceptx + 10, accepty)
        pyautogui.typewrite(str(name))
        time.sleep(0.5)
        ban_champ()
        logging.info(date_string + name + 'banned !')

def pick_champ():
    accept = pyautogui.locateOnScreen('resources/jgl.png', confidence=0.6)
    ban = pyautogui.locateOnScreen('resources/ban.png', confidence=0.6)
    if (accept != None and ban != None):
        accept = pyautogui.center(accept)
        acceptx, accepty = accept
        pyautogui.click(acceptx, accepty + 50)
        time.sleep(0.5)
        ban = pyautogui.center(ban)
        banx, bany = ban
        pyautogui.click(banx, bany)

def auto_pick_engine(name, date_string):
    accept = pyautogui.locateOnScreen('resources/search.png', confidence=0.9)
    ban = pyautogui.locateOnScreen('resources/choose.png', confidence=0.9)
    if (accept != None and ban != None):
        logging.info(date_string + ' choosing...')
        accept = pyautogui.center(accept)
        acceptx, accepty = accept
        pyautogui.click(acceptx + 10, accepty)
        pyautogui.typewrite(str(name))
        time.sleep(0.5)
        pick_champ()
        logging.info(date_string + name + ' picked !')

def auto_accept_engine(date_string):
    accept = pyautogui.locateOnScreen('resources/accept.png')
    if (accept != None):
        logging.info(date_string + ' game found !')
        accept = pyautogui.center(accept)
        acceptx, accepty = accept
        pyautogui.click(acceptx, accepty)
        logging.info(date_string + ' game accepted !')
    return False

def control_center(ban_name, pick_name):
    logging.basicConfig(filename="log.log", level=logging.INFO)
    today = datetime.datetime.today()
    date_string = today.strftime(" %d.%m.%Y_%H;%M;%S ")
    auto_accept_engine(date_string)
    auto_ban_engine(ban_name, date_string)
    auto_pick_engine(pick_name, date_string)
