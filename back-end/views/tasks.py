from models.tv_channel import TVChannel, TV_CHANNELS_STATE
from file_handler import get_subtitle_filename_from_clipname, check_copy_conditions, \
    get_subtitle_server_full_path, get_subtitle_source_full_path
from shutil import copy2
import os


TASKS = []

def copy_new_subtitles():
    for channel in TV_CHANNELS_STATE:
        channel.refresh_state()
        for clip in channel.clips:
            for lang in channel.subtitle_languages:
                cur_file_to_check = get_subtitle_filename_from_clipname(clip, lang)
                if cur_file_to_check not in channel.subtitles_on_server \
                        and cur_file_to_check in channel.subtitles_on_source:
                    copy2(os.path.join(channel.channel_sub_src_dir, lang, cur_file_to_check),
                             os.path.join(channel.channel_sub_dir, cur_file_to_check))

def copy_updated_subtitles():
    for channel in TV_CHANNELS_STATE:
        channel.refresh_state()
        for clip in channel.clips:
            for lang in channel.subtitle_languages:
                cur_file_to_check = get_subtitle_filename_from_clipname(clip, lang)
                if cur_file_to_check in channel.subtitles_on_server \
                        and cur_file_to_check in channel.subtitles_on_source:
                    size_cond, mod_date_cond = check_copy_conditions(channel.channel_sub_src_dir, channel.channel_sub_dir, cur_file_to_check, lang)

                    if size_cond or mod_date_cond:
                        copy2(get_subtitle_source_full_path(channel.channel_sub_src_dir, lang, cur_file_to_check),
                                 get_subtitle_server_full_path(channel.channel_sub_dir, cur_file_to_check))

TASKS.append(copy_new_subtitles)
TASKS.append(copy_updated_subtitles)
