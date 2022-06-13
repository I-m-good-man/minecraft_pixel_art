from PIL import Image


def work_with_img(file_name, size_of_pixel):
    """
    Эта функция принимает на вход имя файла и размер пиксель-арта в пикселях. Функция переводит фотографию в меньшее
    разрешения, чтобы получить пиксельный
    эффект. Функция возвращает объект, из которого можно получить цветовое значения каждого пикселя уменьшенной
    фотографии и разрешение этой фотографии.
    :param file_name, size_of_pixel:
    :return: img_obj, new_width, new_height
    """
    # открываем фото
    try:
        img = Image.open(f'./images/{file_name}').convert('RGB')
    except OSError:
        raise OSError
    # получаем размеры в пикселях нашего фото
    width, height = img.size
    # создаем новые размеры фото
    new_width, new_height = width // (height // size_of_pixel), size_of_pixel

    def pixelate_for_user(image, new_width, new_height, width, height):
        """
        Эта функция пикселизирует картинку так, чтобы ее можно было показать пользователю, она имеет исходное разрешение
        и не будет очень маленькой
        :param image:
        :param pixel_size:
        :return:
        """
        image = image.resize((new_width, new_height), Image.NEAREST)
        image = image.resize((width, height), Image.NEAREST)
        return image

    def pixelate_for_programm(image, new_width, new_height):
        """
        Эта функция пикселизирует картинку, изменяя разрешение, эта функция нужна для программы, чтобы было проще
        определять цвет пикселей.
        :param image:
        :param pixel_size:
        :return:
        """
        image = image.resize((new_width, new_height), Image.NEAREST)
        return image

    # создаем пиксельное изображене для дальнейшего его использования
    reduce_img = pixelate_for_programm(img, new_width, new_height)
    img_obj = reduce_img.load()

    # создаем пиксельное изображение для пользователя и сохраняем его
    image_for_user = pixelate_for_user(img, new_width, new_height, width, height)
    image_for_user.save(f'./reduce_images/pixel_art_of_{file_name}')
    """
    # пробуем показать это изображение пользователю
    try:
        image_for_user.show()
    except:
        print(f'вы можете посмотреть изображение, пиксель арт которого будет делать в по этому пути '
              f'/reduce_images/pixel_art_of_{file_name}')
    """
    return img_obj, new_width, new_height


def determine_blocks_for_pixels(all_pixels, width, height):
    """
    Эта функция определяет, какого цвета нужно взять блок. Выборка осуществляется на основании цвета текущего пикселя.
    Функция вернет двумерный массив, список списков, каждый список - это столбец цветов, которые нужно ставить снизу-вверх.
    :return:
    """
    def determine_color(color_of_pixel):
        """
        Эта функция сверяет цвет пикслея, который она получает на входе, с цветом, которые имеют блоки в словаре
        dict_with_colors_of_blocks. Чтобы узнать, какой блок соответствует по цвету пикселю, мы будем сравнивать суммы
        значений ргб пикселя и значений ргб блока.
        :return:
        """
        dict_with_colors_of_blocks = {'белый': (206, 212, 213), 'оранжевый': (225, 98, 1), 'пурпурный': (169, 48, 159),
                                      'голубой': (35, 137, 199), 'желтый': (242, 176, 21), 'зеленый': (95, 170, 25),
                                      'розовый': (212, 100, 142), 'темно-красный': (141, 32, 32),
                                      'черный': (9, 11, 16),
                                      'темно-серый': (54, 57, 61), 'светло-серый': (126, 126, 116),
                                      'бирюзовый': (22, 120, 137),'фиолетовый': (100, 31, 156), 'синий': (44, 46, 143),
                                      'коричневый': (97, 61, 33),'темно-зеленый': (73, 91, 36)
                                      }

        # это словарь с суммами разности
        dict_with_dif = {}

        for key, value in dict_with_colors_of_blocks.items():
            # тут мы добавляем в словарь разницу в процентах меджду цветами
            r1, g1, b1 = value
            r2, g2, b2 = color_of_pixel

            dict_with_dif[key] = (abs(r1-r2) / 255 + abs(g1-g2) / 255 + abs(b1-b2) / 255) / 3 * 100

        # список с кортежами, в которых ключ и значение
        list_with_keys_and_values = list(dict_with_dif.items())

        # сортируем список, ключ находится на 0 позиции в кортеже, значение на 1
        sorted_list_with_keys_and_values = sorted(list_with_keys_and_values, key=lambda x: x[1])

        # т.к. нам нужно наименьшее значение, то мы забираем цвет первого элемента списка
        necessary_color = sorted_list_with_keys_and_values[0][0]
        return necessary_color

    # это список со списками, в котором идут столбцы по порядку снизу вверх
    list_for_colors = []

    # это словарь, в котором подсчитывается количество блоков каждого цвета, чтобы можно было найти 8 наиболее частых блоков
    dict_counter = {'белый': 0, 'оранжевый': 0, 'пурпурный': 0,
                                      'голубой': 0, 'желтый': 0, 'зеленый': 0,
                                      'розовый': 0, 'темно-красный': 0,
                                      'черный': 0,
                                      'темно-серый': 0, 'светло-серый': 0,
                                      'бирюзовый': 0,'фиолетовый': 0, 'синий': 0,
                                      'коричневый': 0,'темно-зеленый': 0}

    # тут перебираются номера столбцов
    for w in range(width):
        # это список для цветов каждой ячейки столбца
        current_column = []
        # тут перебираются значения ячейки каждого столбца снизу вверх
        for h in range(height):
            color_of_block = determine_color(all_pixels[w, h])
            # добавляем в список цвет блока, сопоставленный с цветом пикселя в функции determine_color
            current_column.append(color_of_block)
            # увеличиваем на один счетчик цветов
            dict_counter[color_of_block] += 1
        list_for_colors.append(current_column)

    # сортируем словарь с кол-вом каждого цвета и получаем отсортированный список кортежей
    dict_counter = sorted(list(dict_counter.items()), key=lambda el: el[1], reverse=True)
    # составляем список с 8 основными цветами
    main_colors = [el[0] for el in dict_counter[:8]]
    return list_for_colors, main_colors




