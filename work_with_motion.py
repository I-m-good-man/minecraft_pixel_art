from pynput import keyboard
from pynput import mouse
import time
import pyautogui


class Player:
    """
    Это класс для работы с движением объекта.
    """
    def __init__(self):
        self.keyboard = keyboard.Controller()
        self.mouse = mouse.Controller()

    def one_block_forward(self):
        """
        Эта функция двигает персонажа вперед на один блок. Сначала проходим один блок вперед, а затем идем назад, чтобы
        прижаться к заднему блоку.
        :return:
        """
        # идем вперед
        pyautogui.keyDown('w')
        time.sleep(0.5)
        pyautogui.keyUp('w')
        # идем назад
        pyautogui.keyDown('s')
        time.sleep(1)
        pyautogui.keyUp('s')

    def one_jump(self):
        """
        Эта функция делает прыжок игрока.
        :return:
        """

        pyautogui.keyDown('space')
        time.sleep(0.07)
        pyautogui.keyUp('space')

    def one_right_button_click(self):

        self.mouse.press(mouse.Button.right)
        time.sleep(0.3)
        self.mouse.release(mouse.Button.right)

    def one_left_button_click(self):
        self.mouse.press(mouse.Button.left)
        time.sleep(0.1)
        self.mouse.release(mouse.Button.left)

    @staticmethod
    def keyboard_listener():
        """
        Эта функция нужна для того, чтобы отследить команду пользователя "бот", чтобы после нее уже можно было начинать
        строить пиксель-арт.
        :return:
        """
        # это список для трех последних символов, чтобы моэно было отследить команду "бот"
        list_with_chars = []

        def on_press(key):
            # если пользователь вводит на русском языке команду "бот", то программа перестает слушать клавитуру и начинает
            # делать пиксельарт
            try:
                if len(list_with_chars) < 3:
                    list_with_chars.append(key.char)
                else:
                    list_with_chars.pop(0)
                    list_with_chars.append(key.char)
            except AttributeError:
                pass
            # проверяет, соответсвует ли последние набранные 2 символа нашей команде
            if len(list_with_chars) == 3:
                string_of_chars = ''
                for char in list_with_chars:
                    string_of_chars += char
                if string_of_chars == ',jn':
                    return False

        def on_release(key):
            pass

        # Collect events until released
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()

    def press_e_key(self):
        pyautogui.keyDown('e')
        time.sleep(0.07)
        pyautogui.keyUp('e')

    @staticmethod
    def mouse_listener():
        """
        функция для отладки поведения мыши
        :return:
        """
        def on_move(x, y):
            print('Pointer moved to {0}'.format(
                (x, y)))

        def on_click(x, y, button, pressed):
            print('{0} at {1}'.format(
                'Pressed' if pressed else 'Released',
                (x, y)))
            if not pressed:
                # Stop listener
                return False

        def on_scroll(x, y, dx, dy):
            print('Scrolled {0} at {1}'.format(
                'down' if dy < 0 else 'up',
                (x, y)))

        # Collect events until released
        with mouse.Listener(
                on_move=on_move,
                on_click=on_click,
                on_scroll=on_scroll) as listener:
            listener.join()

    # далее идут функции для нажатия на цифры от 1 до 9
    def press_on_digit_1(self):
        last_time = time.time()
        while (time.time() - last_time) < 0.2:
            self.keyboard.press('1')
        self.keyboard.release('1')

    def press_on_digit_2(self):
        last_time = time.time()
        while (time.time() - last_time) < 0.2:
            self.keyboard.press('2')
        self.keyboard.release('2')

    def press_on_digit_3(self):
        last_time = time.time()
        while (time.time() - last_time) < 0.2:
            self.keyboard.press('3')
        self.keyboard.release('3')

    def press_on_digit_4(self):
        last_time = time.time()
        while (time.time() - last_time) < 0.2:
            self.keyboard.press('4')
        self.keyboard.release('4')

    def press_on_digit_5(self):
        last_time = time.time()
        while (time.time() - last_time) < 0.2:
            self.keyboard.press('5')
        self.keyboard.release('5')

    def press_on_digit_6(self):
        last_time = time.time()
        while (time.time() - last_time) < 0.2:
            self.keyboard.press('6')
        self.keyboard.release('6')

    def press_on_digit_7(self):
        last_time = time.time()
        while (time.time() - last_time) < 0.2:
            self.keyboard.press('7')
        self.keyboard.release('7')

    def press_on_digit_8(self):
        last_time = time.time()
        while (time.time() - last_time) < 0.2:
            self.keyboard.press('8')
        self.keyboard.release('8')

    def press_on_digit_9(self):
        last_time = time.time()
        while (time.time() - last_time) < 0.2:
            self.keyboard.press('9')
        self.keyboard.release('9')

    @staticmethod
    def replace_cursor(position):
        """
        Функция, которая перемещает курсор мыши на позцию, которую функция получает на входе
        :param position:
        :return:
        """
        pyautogui.moveTo(position[0], position[1])



"""
player = Player()
player.keyboard_listener()
for i in range(10):
    player.one_jump()
    player.one_right_button_click()
player = Player()
player.keyboard_listener()
for i in range(10):
    for j in range(10):
        player.one_jump()
        time.sleep(0.08)
        player.one_right_button_click()
    time.sleep(0.5)
    player.one_block_forward()
    time.sleep(1)"""

