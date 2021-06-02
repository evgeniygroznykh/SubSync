from flask import Blueprint, jsonify
from config import PROVIDER_CONFIG, save_config
from file_handler import get_media_files_from_server, get_subtitle_files_from_source
from models.tv_channel import TV_CHANNELS_STATE
import os


TV_CHANNELS_CFG_KEY = 'tv_channels'
CHANNEL_NAME_CFG_KEY = 'channelName'
CHANNEL_CLIP_DIR_CFG_KEY = 'channelClipDirectory'
CHANNEL_SUBTITLE_DIR_CFG_KEY = 'channelSubtitleDirectory'
CHANNEL_SUBTITLE_SRC_DIR_CFG_KEY = 'channelSubtitleSourceDirectory'
ROOT_PY_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

ROUTE_BLUEPRINTS = []

get_channels = Blueprint("get_channels", __name__)
ROUTE_BLUEPRINTS.append(get_channels)
@get_channels.route('/get_channels')
def get_channels():
    return jsonify([{"channelName" : channel.channel_name, "channelImage" : channel.channel_image_name,
                        "channelClips": channel.clips,
                        "channelSubtitles": channel.subtitles_on_server}
                         for channel in TV_CHANNELS_STATE])
    
get_subtitles_on_src = Blueprint("get_subtitles_on_src", __name__)
ROUTE_BLUEPRINTS.append(get_subtitles_on_src)
@get_subtitles_on_src.route('/get_subtitles_on_src/<channel_name>')
def get_subtitles_on_src(channel_name):
    for channel in TV_CHANNELS_STATE:
        if channel.channel_name == channel_name:
            subtitle_src_path = channel.channel_sub_src_dir
            subtitles_on_src = get_subtitle_files_from_source(subtitle_src_path)
            return jsonify(subtitles_on_src)
    return jsonify({'Error':f'no tv channels found with given channel name ({channel_name})'})
