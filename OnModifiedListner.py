import os
import shutil
import datetime
import time
from watchdog.events import FileSystemEventHandler

default_download_folder = '/home/roman/Загрузки'

class OnModifiedListner(FileSystemEventHandler):
        def on_modified(self, event):
                current_year = str(datetime.date.today().year)
                username = os.getlogin() #get current working username
                #check if directory for downloads exist and make if it doesnt
                if not(os.path.isdir('/home/' + username + '/Downloads')):
                        os.makedirs('/home/' + username + '/Downloads')
                #check if directory of current year exist and if it doesnt make it and inner files
                if not(os.path.isdir('/home/' + username + '/Downloads/' + current_year)):
                        os.makedirs('/home/' + username + '/Downloads/' + current_year)
                        os.makedirs('/home/' + username + '/Downloads/' + current_year + '/Images')
                        os.makedirs('/home/' + username + '/Downloads/' + current_year + '/Videos')
                        os.makedirs('/home/' + username + '/Downloads/' + current_year + '/Documents')
                        os.makedirs('/home/' + username + '/Downloads/' + current_year + '/Music')
                        os.makedirs('/home/' + username + '/Downloads/' + current_year + '/Archives')
                        os.makedirs('/home/' + username + '/Downloads/' + current_year + '/Code')
                        os.makedirs('/home/' + username + '/Downloads/' + current_year + '/Other_Files')

                images_path = '/home/' + username + '/Downloads/' + current_year + '/Images'
                documents_path = '/home/' + username + '/Downloads/' + current_year + '/Documents'
                music_path = '/home/' + username + '/Downloads/' + current_year + '/Music'
                others_path = '/home/' + username + '/Downloads/' + current_year + '/Other_Files'
                videos_path = '/home/' + username + '/Downloads/' + current_year + '/Videos'
                archives_path = '/home/' + username + '/Downloads/' + current_year + '/Archives'
                code_path = '/home/' + username + '/Downloads/' + current_year + '/Code'
                with os.scandir(default_download_folder) as entries:
                        for entry in entries:
                                file = entry.name
                                if file[-3:] == 'png' or file[-3:] == 'jpg' \
                                    or file[-4:] == 'jpeg' or file[-3:] == 'gif' \
                                        or  file[-4:] == 'webp' or file[-3:] == 'bmp' or file[-3:] == 'ico':
                                            move(file, images_path)
                                elif file[-3:] == 'doc' or file[-4:] == 'docx' \
                                    or file[-3:] == 'odt' or file[-3:] == 'pdf' \
                                        or file[-3:] == 'xls' or file[-4:] == 'xlsx' \
                                            or file[-3:] == 'ods' or file[-3:] == 'rtf' \
                                                or file[-3:] == 'ppt' or file[-4:] == 'pptx' \
                                                    or file[-3:] == 'txt' or file[-3:] == 'csv' \
                                                        or file[-3:] == 'ott' or file[-3:] == 'odt' \
                                                            or file[-3:] == 'ods' or file[-3:] == 'odp':
                                                                move(file, documents_path)
                                elif file[-3:] == 'wmv' or file[-4:] == 'webm' \
                                    or file[-3:] == 'vob' or file[-2:] == 'ts' \
                                        or file[-3:] == 'swf' or file[-2:] == 'rm' \
                                            or file[-3:] == 'ogv' or file[-3:] == 'mxf' \
                                                or file[-3:] == 'mts' or file[-3:] == 'mpg' \
                                                    or file[-4:] == 'mpeg' or file[-3:] == 'mp4' \
                                                        or file[-3:] == 'mov' or file[-3:] == 'mkv' \
                                                            or file[-5:] == 'mjpeg' or file[-3:] == 'm4v' \
                                                                or file[-3:] == 'm2v' or file[-4:] == 'm2ts' \
                                                                    or file[-4:] == 'hevc' or file[-3] == 'flv' \
                                                                        or file[-3] == 'f4v' or file[-3] == 'asf' \
                                                                            or file[-3] == 'avi' or file[-3] == '3gp':
                                                                                move(file, videos_path)
                                elif file[-3:] == 'mp3' or file[-3:] == 'aac' \
                                    or file[-3:] == 'ogg' or file[-4:] == 'flac' \
                                        or file[-4:] == 'alac' or file[-3:] == 'pcm' \
                                            or file[-3:] == 'wav' or file[-4:] == 'aiff':
                                                move(file, music_path)
                                elif file[-3:] == 'zip' or file[-3:] == 'tgz' \
                                    or file[-3:] == 'tar' or file[-3:] == 'rar' \
                                        or file[-2:] == '7z':
                                            move(file, archives_path)
                                elif file[-4:] == 'yaml' or file[-2:] == 'vb' \
                                    or file[-5:] == 'swift' or file[-3:] == 'sql' \
                                        or file[-2:] == 'sh' or file[-2:] == 'rb' \
                                            or file[-2:] == 'py' or file[-2:] == 'pl' \
                                                or file[-3:] == 'php' or file[-3:] == 'kml' \
                                                    or file[-4:] == 'json' or file[-2:] == 'js' \
                                                        or file[-4:] == 'java' or file[-4:] == 'html' \
                                                            or file[-8:] == 'htaccess' or file[-1:] == 'h' \
                                                                or file[-2:] == 'go' or file[-3:] == 'css' \
                                                                    or file[-2:] == 'cs' or file[-3:] == 'cpp' \
                                                                        or file[-5:] == 'class' or file[-1:] == 'c' \
                                                                            or file[-3:] == 'bat':
                                                                                move(file, code_path)
                                else: 
                                    move(file, others_path)

def move(file, path):
        try:
            shutil.move(default_download_folder + '/' + file, path)
        except:
                shutil.Error
                file_array = file.split('.')
                file = file_array[0] + '(1)' + '.' + file_array[1]