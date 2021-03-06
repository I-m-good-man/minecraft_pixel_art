from PIL import Image


def work_with_img(file_name):
    """
    Эта функция принимает на вход имя файла. Функция переводит фотографию в меньшее разрешения, чтобы получить пиксельный
    эффект. Функция возвращает объект, из которого можно получить цветовое значения каждого пикселя уменьшенной
    фотографии и разрешение этой фотографии.
    :param file_name:
    :return: img_obj, new_width, new_height
    """
    # открываем фото
    try:
        img = Image.open(f'./images/{file_name}').convert('RGB')
    except OSError:
        raise OSError
    img_obj = img.load()
    return img_obj[366, 79]

print(work_with_img('all_colors.bmp'))

dict_with_colors = {'белый': (206, 212, 213), 'оранжевый': (225, 98, 1), 'пурпурный': (169,48,159),
                    'голубой': (35,137,199), 'желтый': (242,176,21), 'зеленый': (95,170,25), 'розовый': (212,100,142),
                    'темно-серый': (54,57,61), 'светло-серый': (126,126,116), 'бирюзовый': (22,120,137),
                    'фиолетовый': (100,31,156), 'синий': (44,46,143), 'коричневый': (97,61,33),
                    'темно-зеленый': (73,91,36), 'темно-красный': (141,32,32), 'черный': (9,11,16)}