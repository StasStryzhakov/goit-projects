import shutil
import sys
from pathlib import Path
import translate_name # Модуль для перекладу назви файлу
from concurrent.futures import ThreadPoolExecutor



# MAIN_PATH = sys.argv[1] if len(sys.argv) < 3 else ' '.join(sys.argv[1:]) # Основний шлях
MAIN_PATH = input('where i must clen?: ')
TRANSLATE = translate_name.get_translate_dict() # Словник для перекладу


extensions = {  

    'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v', 
              'h264', 'flv', 'rm', 'swf', 'vob', 'm4a'],

    'data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb', 'sav', 
             'tar', 'xml', 'xlsx', 'bin'],

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
    
    sub_dir_paths = [dir_path for dir_path in Path(folder_path).iterdir() if dir_path.is_dir() and dir_path.name not in extensions]
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
    path.rmdir()
        

def sort_files(paths):
    file_path = paths
    main_path = get_main_path() 
    extension_list = extensions.items()
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
    files_path = get_file_paths(folder_path)
    dirs_path = get_sub_dir_paths(folder_path)
    
    
    if files_path:    
        with ThreadPoolExecutor(max_workers=5) as file_executor:
            print(f'sort files in: {folder_path}')
            file_executor.map(sort_files, files_path)
    else:
        print(f'no files to sort in: {folder_path}')
        
        
    if dirs_path:
        with ThreadPoolExecutor(max_workers=5) as dir_executor:    
            dir_executor.map(sort_by_dir, dirs_path)
            
    if not files_path and not dirs_path:
        print(f'directory: {folder_path} is empty') 
        print(f'directory: {folder_path} deleted')
        remove_empty_dir(folder_path)

def sort(folder_path):
    sort_by_dir(folder_path)
            
def main():
    sort(MAIN_PATH)
    
if __name__ == '__main__':
    main()        