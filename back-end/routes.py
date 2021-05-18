import os
from flask import Blueprint, jsonify
from config import PROVIDER_CONFIG


BLUEPRINTS = []

get_channels = Blueprint("get_channels", __name__)
BLUEPRINTS.append(get_channels)
@get_channels.route('/get_channels')
def get_channels():
    return jsonify([channel['channelName'] for channel in PROVIDER_CONFIG['tv_channels']])

get_clips = Blueprint("get_clips", __name__)
BLUEPRINTS.append(get_clips)
@get_clips.route('/get_clips/<channel_name>')
def get_clips(channel_name):
    if channel_name.lower() in PROVIDER_CONFIG['clip_directories'].keys():
        try:
            clip_dir_path = PROVIDER_CONFIG['clip_directories'][channel_name.lower()]
            clips = [x for x in os.listdir(clip_dir_path) if x.endswith('mxf')]
            return(jsonify(clips))
        except:
            return(jsonify(f"Error: can't get clip list with given clip directory path. {clip_dir_path}"))
    else:
        return(jsonify({'Error':f'no tv channels found with given channel name ({channel_name})'}))

get_subtitles = Blueprint("get_subtitles", __name__)
BLUEPRINTS.append(get_subtitles)
@get_subtitles.route('/get_subtitles/<channel_name>')
def get_subtitles(channel_name):
    if channel_name.lower() in PROVIDER_CONFIG['subtitle_directories'].keys():
        try:
            subtitle_dir_path = PROVIDER_CONFIG['subtitle_directories'][channel_name.lower()]
            subtitles = [x for x in os.listdir(subtitle_dir_path) if x.endswith('stl')]
            return(jsonify(subtitles))
        except:
            return(jsonify(f"Error: can't get subtitle list with given clip directory path. {subtitle_dir_path}"))
    else:
        return(jsonify({'Error':f'no tv channels found with given channel name ({channel_name})'}))

config = Blueprint("config", __name__)
BLUEPRINTS.append(config)
@config.route('/config', methods=['GET'])
def get_config():
    return jsonify(PROVIDER_CONFIG)