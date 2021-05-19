from flask import Blueprint, jsonify
from config import PROVIDER_CONFIG, save_config
from file_handler import get_media_files_from_server, get_subtitle_files_from_source
from models.tv_channel import TV_CHANNELS_STATE


TV_CHANNELS_CFG_KEY = 'tv_channels'
CHANNEL_NAME_CFG_KEY = 'channelName'
CHANNEL_CLIP_DIR_CFG_KEY = 'channelClipDirectory'
CHANNEL_SUBTITLE_DIR_CFG_KEY = 'channelSubtitleDirectory'
CHANNEL_SUBTITLE_SRC_DIR_CFG_KEY = 'channelSubtitleSourceDirectory'
CLIP_QUERY_TARGET = 'clips'
SUBTITLE_QUERY_TARGET = 'subtitles'

ROUTE_BLUEPRINTS = []

get_channels = Blueprint("get_channels", __name__)
ROUTE_BLUEPRINTS.append(get_channels)
@get_channels.route('/get_channels')
def get_channels():
    return jsonify([channel.channel_name for channel in TV_CHANNELS_STATE])

get_clips = Blueprint("get_clips", __name__)
ROUTE_BLUEPRINTS.append(get_clips)
@get_clips.route('/get_clips/<channel_name>')
def get_clips(channel_name):
    for channel in TV_CHANNELS_STATE:
        if channel.channel_name == channel_name:
            clip_dir_path = channel.channel_clip_dir
            clips = get_media_files_from_server(clip_dir_path, CLIP_QUERY_TARGET)
            return jsonify(clips)
    return(jsonify({'Error':f'no tv channels found with given channel name ({channel_name})'}))

get_subtitles = Blueprint("get_subtitles", __name__)
ROUTE_BLUEPRINTS.append(get_subtitles)
@get_subtitles.route('/get_subtitles/<channel_name>')
def get_subtitles(channel_name):
    for channel in TV_CHANNELS_STATE:
        if channel.channel_name == channel_name:
            subtitle_dir_path = channel.channel_sub_dir
            subtitles = get_media_files_from_server(subtitle_dir_path, SUBTITLE_QUERY_TARGET)
            return jsonify(subtitles)
    return(jsonify({'Error':f'no tv channels found with given channel name ({channel_name})'}))

get_subtitles_on_src = Blueprint("get_subtitles_on_src", __name__)
ROUTE_BLUEPRINTS.append(get_subtitles_on_src)
@get_subtitles_on_src.route('/get_subtitles_on_src/<channel_name>')
def get_subtitles_on_src(channel_name):
    for channel in TV_CHANNELS_STATE:
        if channel.channel_name == channel_name:
            subtitle_src_path = channel.channel_sub_src_dir
            subtitles_on_src = get_subtitles_on_src(subtitle_src_path)
            return(jsonify(subtitles_on_src))
    return(jsonify({'Error':f'no tv channels found with given channel name ({channel_name})'}))

config = Blueprint("config", __name__)
ROUTE_BLUEPRINTS.append(config)
@config.route('/config', methods=['GET'])
def get_config():
    return jsonify(PROVIDER_CONFIG)

"""
save_config = Blueprint("save_config", __name__)
BLUEPRINTS.append(save_config)
@save_config.route('/save_config', methods=['POST'])
def save_config(new_config):
    save_config(new_config)
    return (jsonify({'Config was successfully saved.'}))
"""
