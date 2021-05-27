import os
import pathlib


def get_media_files_from_server(file_path, query_target):
    try:
        if query_target == 'clips':
            file_extension = '.mxf'
        elif query_target == 'subtitles':
            file_extension = '.stl'
        else:
            raise ValueError

        media_files = [x for x in os.listdir(file_path) if x.endswith(file_extension)]
        return media_files
    except:
        return f"Error: can't get {query_target[0:-1]} list with given {query_target[0:-1]} directory path. {file_path}"

def get_subtitle_files_from_source(file_path):
    try:
        subtitles_files_from_src = [name
                            for _, _, files in os.walk(file_path)
                            for name in files
                            if name.endswith(".stl")]
        return subtitles_files_from_src
    except:
        return f"Error: can't get subtitle list with given subtitle source directory path. {file_path}"

def get_clip_filename_from_subtitlename(subtitle_name):
    return f"{subtitle_name.split('_')[0]}.mxf"

def get_subtitle_filename_from_clipname(clip_name, language):
    return f"{clip_name.split('.')[0]}_{language}.stl"

def get_subtitle_source_full_path(channel_sub_src_dir, lang, file_name_with_ext):
    return os.path.join(channel_sub_src_dir, lang, file_name_with_ext)

def get_subtitle_server_full_path(channel_sub_dir, file_name_with_ext):
    return os.path.join(channel_sub_dir, file_name_with_ext)

def check_copy_conditions(channel_sub_src_dir, channel_sub_dir, cur_file_to_check, lang):
    subtitle_source_full_path = get_subtitle_source_full_path(channel_sub_src_dir, lang, cur_file_to_check)
    subtitle_server_full_path = get_subtitle_server_full_path(channel_sub_dir, cur_file_to_check)
    return (os.path.getsize(subtitle_source_full_path) != os.path.getsize(subtitle_server_full_path),
            pathlib.Path(subtitle_source_full_path).stat().st_mtime != pathlib.Path(subtitle_server_full_path).stat().st_mtime)

