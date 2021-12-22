# coding: utf8

import os
import pyautogui
import time

# BASE_DIR = os.path.realpath(os.path.dirname(__file__))

class AutoClick:
    def __init__(self):
        # 配置文件名字和图片文件夹名字
        self.TXT_PATH = r'config.txt'
        self.IMAGE_DIR = r'img'
        # 置信度
        self.CONFIDENCE = 0.95
        # 识别图片和执行动作的间隔时间
        self.SLEEP_TIME = 0.5

        self.KEY_ACTION = None
        self.MOUSE_ACTION = None
        self.init_action_dict()

    def init_action_dict(self):
        self.MOUSE_ACTION = {
            '~l': pyautogui.click,
            '~r': pyautogui.rightClick,
            '~dl': pyautogui.doubleClick,
        }
        self.KEY_ACTION = {
            'winleft': pyautogui.press,
            'enter': pyautogui.press,
            'esc': pyautogui.press,
            'backspace': pyautogui.press,
            'space': pyautogui.press,
            'up': pyautogui.press,
            'down': pyautogui.press,
            'left': pyautogui.press,
            'right': pyautogui.press,
        }

        for char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.;/"':
            self.KEY_ACTION[char] = pyautogui.press

    def do_actions(self, action_list, point):
        for action in action_list:
            action = action.strip()
            # 鼠标动作
            if action in self.MOUSE_ACTION:
                print('mouse', action)
                time.sleep(self.SLEEP_TIME)
                action_func = self.MOUSE_ACTION[action]
                action_func(point)

            # 键盘动作
            elif action in self.KEY_ACTION:
                print('key', action)
                time.sleep(self.SLEEP_TIME)
                action_func = self.KEY_ACTION[action]
                print(action_func)
                # pyautogui.press('winleft')
                action_func(action)

            # 连续按键
            else:
                print('type', action)
                time.sleep(self.SLEEP_TIME)
                for each in action:
                    time.sleep(self.SLEEP_TIME)
                    pyautogui.press(each)

    def run(self):
        # with open(os.path.join(BASE_DIR, self.TXT_PATH), 'r', encoding='utf-8') as fr:
        with open(self.TXT_PATH, 'r', encoding='utf-8') as fr:
            line_list = fr.readlines()

        for line in line_list:
            if not line.strip() or line.lstrip().startswith('#'):
                continue
            content_list = line.split("|")
            if len(content_list) == 3:
                pre_action, img_path, actions = content_list
            else:
                pre_action = None
                img_path, actions = content_list
            action_list = actions.split(',')
            print(line, action_list)
            while True:
                point = pyautogui.Point(0, 0)
                # 没有输入图片则不需要找图片
                if img_path:
                    # 有pre_action则做pre_action直到找到图片为止
                    if pre_action:
                        self.do_actions(action_list=pre_action.split(','), point=None)
                        # point = pyautogui.locateCenterOnScreen(os.path.join(BASE_DIR, self.IMAGE_DIR, img_path),
                        point = pyautogui.locateCenterOnScreen(os.path.join(self.IMAGE_DIR, img_path),
                                                               confidence=self.CONFIDENCE)
                    else:
                        # point = pyautogui.locateCenterOnScreen(os.path.join(BASE_DIR, self.IMAGE_DIR, img_path),
                        point = pyautogui.locateCenterOnScreen(os.path.join(self.IMAGE_DIR, img_path),
                                                               confidence=self.CONFIDENCE)
                    if not point:
                        continue
                    point = pyautogui.Point(x=point.x, y=point.y - 8)

                time.sleep(self.SLEEP_TIME)
                self.do_actions(action_list=action_list, point=point)

                break


class AutoLianLianKan(AutoClick):
    def __init__(self):
        super(AutoLianLianKan, self).__init__()
        self.TXT_PATH = r'lianliankan.txt'
        self.SLEEP_TIME = 0
        self.CONFIDENCE = None
        # 连连看的图片都以llk开头
        self.PNG_START = 'llk'

    def gen_txt(self):
        with open(self.TXT_PATH, 'w', encoding='utf-8') as fw:
            for png in os.listdir(self.IMAGE_DIR):
                if png.startswith(self.PNG_START):
                    fw.write('{}|~l\n'.format(png))

    def run(self):
        self.gen_txt()
        with open(self.TXT_PATH, 'r', encoding='utf-8') as fr:
            line_list = fr.readlines()

        while True:
            for line in line_list:
                if not line.strip() or line.lstrip().startswith('#'):
                    continue
                content_list = line.split("|")
                img_path, actions = content_list
                action_list = actions.split(',')
                print(line, action_list)

                if self.CONFIDENCE:
                    point_list = pyautogui.locateAllOnScreen(os.path.join(self.IMAGE_DIR, img_path),
                                                            confidence=self.CONFIDENCE)
                else:
                    point_list = pyautogui.locateAllOnScreen(os.path.join(self.IMAGE_DIR, img_path))
                point_list = list(point_list)
                if img_path == 'llk_kaishi.png' and point_list:
                    point = point_list[0]
                    self.do_actions(action_list=action_list,
                                    point=pyautogui.Point(x=point.left + point.width // 2,
                                                          y=point.top + point.height // 2))
                for i in range(1, len(point_list)):
                    for j in range(i):
                        point = point_list[i]
                        point = pyautogui.Point(x=point.left + point.width // 2, y=point.top + point.height // 2)
                        self.SLEEP_TIME and time.sleep(self.SLEEP_TIME)
                        self.do_actions(action_list=action_list, point=point)

                        point = point_list[j]
                        point = pyautogui.Point(x=point.left + point.width//2, y=point.top + point.height//2)
                        self.SLEEP_TIME and time.sleep(self.SLEEP_TIME)
                        self.do_actions(action_list=action_list, point=point)
