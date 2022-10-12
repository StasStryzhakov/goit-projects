import shutil
import sys
from pathlib import Path
import clean_folder.translate_name as translate_name # Модуль для перекладу назви файлу


MAIN_PATH = sys.argv[1] # Основний шлях

TRANSLATE = translate_name.get_translate_dict() # Словник для перекладу


extensions = {  

    'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v', 
              'h264', 'flv', 'rm', 'swf', 'vob', 'm4a'],

    'data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb', 'sav', 
             'tar', 'xml'],

    'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl',
              'cda'],

    'image': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif', 
              'tiff', 'heic'],

    'archive': ['zip', 'gz', 'tar'],

    'text': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],

    '3d': ['stl', 'obj', 'fbx', 'dae', '3ds', 'iges', 'step'],

    'presentation': ['pptx', 'ppt', 'pps', 'key', 'odp'],

    'spreadsheet': ['xlsx', 'xls', 'xlsm', 'ods'],

    'font': ['otf', 'ttf', 'fon', 'fnt'],

    'gif': ['gif'],

    'exe': ['exe', 'msi'],

    'bat': ['bat'],

    'apk': ['apk'],
    
    'torrent': ['torrent']
} # Словник типів файлів


def get_sub_dir_paths(folder_path): # функція яка повертає список під шляхів папок
    
    sub_dir_paths = [dir_path for dir_path in Path(folder_path).iterdir() if dir_path.is_dir()]
    return sub_dir_paths


def get_file_paths(folder_path): # функція яка повертає список під шляхів файлів
    
    file_paths = [file_path for file_path in Path(folder_path).iterdir() if file_path.is_file()]
    return file_paths

    
def get_target_path(folder_path, *args: str): # функція яка повертає шлях назначення
    
    path = Path(folder_path)
    return path.joinpath(*args)

    
def get_main_path(): # функція яка повертає основний шлях
    
    return MAIN_PATH
        
def remove_empty_dir(folder_path): # функція яка видаляє пусті папки
    
    path = Path(folder_path)
    if not get_file_paths(path) and not get_sub_dir_paths(path):
        path.rmdir()
  
def sort_files(folder_path): # функція яка сорту файли по каталогам із словника extensions
    
    file_paths = get_file_paths(folder_path)
    if not file_paths:
        return None
    main_path = get_main_path() 
    extension_list = extensions.items()
    for file_path in file_paths:
        file_extension = file_path.suffix[1:]
        file_name = translate_name.translate_file_name(file_path.name, file_extension, TRANSLATE)
        for folder, extension in extension_list:
            if file_extension.lower() in extension:
                target_path = get_target_path(main_path, folder)
                if not target_path.exists():
                    target_path.mkdir()
                if folder == 'archive':
                    archive_new_folder_path = target_path.joinpath(file_name.removesuffix(file_extension))
                    if not archive_new_folder_path.exists():
                        shutil.unpack_archive(file_path, archive_new_folder_path)
                    file_path.unlink(missing_ok=True)
                else:
                    file_new_folder_path = target_path.joinpath(file_name)                
                    if file_new_folder_path.exists():
                        file_path.unlink(missing_ok=True) 
                    else:
                        file_path.rename(file_new_folder_path)
                      
                       
                    
              
            
                 
def sort_by_dir(folder_path): # функція яка проходить рекурсивно по папкам
    sort_files(folder_path)
    for path in Path(folder_path).iterdir():
        if path.is_dir() and path.name not in extensions:
            sort_by_dir(path)
            remove_empty_dir(path)
               

if __name__ == '__main__':
    sort_by_dir(MAIN_PATH)
 
    
    
    
    
    
