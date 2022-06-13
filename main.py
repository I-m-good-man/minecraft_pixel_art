import work_with_image
import work_with_motion
import time
import os.path


# принимаем разрешение экрана пользователя
print('привет, это бот, который делает пиксельарты в майнкрафте. в настройках игры маайнкрафт поставьте полноэкранный '
      'режим и интерфейс на авто. сюда введите разрешение вашего экрана, сначала ширину, '
      'затем высоту. пример: "1920,1080". вводить без ковычек.')
flag = True
while flag:
    try:

        user_width, user_height = tuple(map(lambda x: int(x.strip()), input('\n').strip().split(',')))
        flag = False
    except:
        print('введенные вами данные некорректны')

# это стандартные координаты меню выбора блоков
dict_with_coordinates_in_menu = {'roll_in_necessary_place': [1289, 766], 'белый': [853, 442], 'оранжевый': [923, 443],
                                 'пурпурный': [996, 442], 'коричневый': [1068, 515], 'темно-зеленый': [1141, 515],
                              'голубой': [1068, 444], 'желтый': [1139, 443], 'зеленый': [1213, 442],
                              'розовый': [635, 513], 'темно-красный': [1212, 514],'черный': [636, 585],
                              'темно-серый': [708, 515], 'светло-серый': [780, 515],
                              'бирюзовый': [853, 515], 'фиолетовый': [924, 514], 'синий': [995, 513]
                              }

# переделываем координаты меню выбора под разрешение пользователя если у него разрешение не full hd
if (user_width, user_height) != (1920, 1080):
    for key, value in dict_with_coordinates_in_menu.items():
        dict_with_coordinates_in_menu[key][0] = int((dict_with_coordinates_in_menu[key][0] / 1920) * user_width)
        dict_with_coordinates_in_menu[key][1] = int((dict_with_coordinates_in_menu[key][1] / 1080) * user_height)

# просим название картинки
flag = True
while flag:
    print('Теперь вам нужно выбрать картинку, которую вы хотите воссоздать в майнкрафте. Чтобы это сделать, перейдите в'
          'папку с этой программой, затем перейдите в папку images, туда загрузите вашу фотографию. Затем сюда введите'
          'полное имя файла изображения, например "image.png".')
    image_name = input()
    # проверяем, существует ли такой файл
    if not os.path.exists(f'./images/{image_name}'):
        print('Такого файла не существует. Возможно, вы ввели некорректные данные, или забыли указать расширение.\n')
    else:
        flag = False

flag = True
while flag:
    # получаем все пиксели картинки, ее ширину и высоту
    try:
        print(
            'Теперь введите высоту пиксель арта, в зависимости от заданной вами высоты и соотношения размеров исходного '
            'изображения, программа автоматически определит ширину пиксель-арта. Пример "64".')
        size_of_pixel = int(input())
        flag = False
    except OSError:
        print('введенные вами данные некорректны')

# пробуем открыть файл с изображением
flag = True
while flag:
    # получаем все пиксели картинки, ее ширину и высоту
    try:
        all_pixels, width, height = work_with_image.work_with_img(image_name, size_of_pixel)
        flag = False
    except OSError:
        print('Возникли проблемы при открытии вашего изображения, скорее всего, проблем возникли из-за того, что '
              'в имени изображения есть нелатинские символы, или изображение имеет неподдерживаемый формат.')

print('чтобы начать постройку пиксель арта, вам нужно зайти в майнкрафт, направить курсор полностью вниз и сделать так,'
      'чтобы горизонтальные линии креста были параллельны границам блоков. это нужно, чтобы когда персонаж строил пиксель'
      'арт и шел вперед, он никуда не свернул, а шел прямо, строя одну ровную линию блоков. Затем вам нужно просто'
      'набрать русскими буквами команду "бот", после этого начнется постройка пиксель-арта, чтобы не возникло никаких'
      'ошибок, не трогайте мышку и клавиатуру ноутбука, вы это сможете сделать после окончания постройки.')

# получаем двумерный массив с цветами блоков и список 8 главных цветов картинки
list_with_colors, main_colors = work_with_image.determine_blocks_for_pixels(all_pixels, width, height)

# создаем объект игрока и ждем команды "бот"
player = work_with_motion.Player()
player.keyboard_listener()

# заполняем ячейки основными цветами
player.press_e_key()
time.sleep(1)
print(dict_with_coordinates_in_menu['roll_in_necessary_place'])
player.replace_cursor(dict_with_coordinates_in_menu['roll_in_necessary_place'])
time.sleep(1)
player.one_left_button_click()
for counter, color in enumerate(main_colors, 1):
    time.sleep(1)
    player.replace_cursor(dict_with_coordinates_in_menu[color])
    time.sleep(1)
    if counter == 1:
        player.press_on_digit_1()
    elif counter == 2:
        player.press_on_digit_2()
    elif counter == 3:
        player.press_on_digit_3()
    elif counter == 4:
        player.press_on_digit_4()
    elif counter == 5:
        player.press_on_digit_5()
    elif counter == 6:
        player.press_on_digit_6()
    elif counter == 7:
        player.press_on_digit_7()
    elif counter == 8:
        player.press_on_digit_8()
time.sleep(1)
player.press_e_key()
time.sleep(1)

# добавляем в конец списка главных цветов пустую строку - это пустая девятая ячейка, которая дальше будет использоваться
main_colors.append('')

# начинаем строить пиксель арт
for column in list_with_colors:
    # перебираем блоки в столбце - снизу вверх
    for counter, color_of_block in enumerate(column):
        # перед тем как поставить блок, нам нужно выбрать правильно цвет блока и выбрать правильную ячейку
        # если цвет блока является основным, то мы просто меняем ячейку (постоянных ячеек с основными цветами - 8)
        if color_of_block in main_colors:

            if main_colors.index(color_of_block) + 1 == 1:
                player.press_on_digit_1()
            elif main_colors.index(color_of_block) + 1 == 2:
                player.press_on_digit_2()
            elif main_colors.index(color_of_block) + 1 == 3:
                player.press_on_digit_3()
            elif main_colors.index(color_of_block) + 1 == 4:
                player.press_on_digit_4()
            elif main_colors.index(color_of_block) + 1 == 5:
                player.press_on_digit_5()
            elif main_colors.index(color_of_block) + 1 == 6:
                player.press_on_digit_6()
            elif main_colors.index(color_of_block) + 1 == 7:
                player.press_on_digit_7()
            elif main_colors.index(color_of_block) + 1 == 8:
                player.press_on_digit_8()

        # иначе мы открываем главное меню и ставим блок нужного цвета в 9 ячейку, она постоянно меняется
        else:
            # убираем из девятой ячейки блок и ставим новый
            main_colors.pop(-1)
            main_colors.append(color_of_block)
            player.press_e_key()
            time.sleep(1)
            player.replace_cursor(dict_with_coordinates_in_menu['roll_in_necessary_place'])
            time.sleep(1)
            player.one_left_button_click()
            time.sleep(1)
            player.replace_cursor(dict_with_coordinates_in_menu[color_of_block])
            time.sleep(1)
            player.press_on_digit_9()
            player.press_e_key()
            time.sleep(1)
            player.press_on_digit_9()

        time.sleep(0.5)
        # далее мы ставим блок, подпрыгивая
        player.one_jump()
        time.sleep(0.08)
        player.one_right_button_click()

        # если мы достроили последний блок в столбце, то нам нужно спрыгнуть вниз, чтобы начать строить следущий столбец
        if counter == height-1:
            player.one_block_forward()
            time.sleep(4)


