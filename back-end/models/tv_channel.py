from config import PROVIDER_CONFIG
from file_handler import get_media_files_from_server, get_subtitle_files_from_source


CHANNEL_NAME_CFG_KEY = 'channelName'
CHANNEL_CLIP_DIR_CFG_KEY = 'channelClipDirectory'
CHANNEL_SUBTITLE_DIR_CFG_KEY = 'channelSubtitleDirectory'
CHANNEL_SUBTITLE_SRC_DIR_CFG_KEY = 'channelSubtitleSourceDirectory'
CHANNEL_SUBTITLE_LANGUAGES_CFG_KEY = 'channelSubtitleLanguages'
CHANNEL_IMAGE_NAME_CFG_KEY = 'channelImageName'

class TVChannel:
    def __init__(self, channel_name, channel_clip_dir, channel_sub_dir, channel_sub_src_dir, subtitle_languages, image_name):
        self.channel_name = channel_name
        self.channel_clip_dir = channel_clip_dir
        self.channel_sub_dir = channel_sub_dir
        self.channel_sub_src_dir = channel_sub_src_dir
        self.subtitle_languages = subtitle_languages
        self.channel_image_name = image_name

        self.clips = []
        self.subtitles_on_server = []
        self.subtitles_on_source = []

    @staticmethod
    def get_tv_channels(config):
        tv_channels = []
        channel_nodes = config['tv_channels']
        for node in channel_nodes:
            cur_channel_name = node[CHANNEL_NAME_CFG_KEY]
            cur_channel_clip_dir = node[CHANNEL_CLIP_DIR_CFG_KEY]
            cur_channel_sub_dir = node[CHANNEL_SUBTITLE_DIR_CFG_KEY]
            cur_channel_sub_src_dir = node[CHANNEL_SUBTITLE_SRC_DIR_CFG_KEY]
            cur_channel_subtitle_languages = node[CHANNEL_SUBTITLE_LANGUAGES_CFG_KEY]
            cur_channel_image_name = node[CHANNEL_IMAGE_NAME_CFG_KEY]
            cur_tv_channel = TVChannel(cur_channel_name, cur_channel_clip_dir, cur_channel_sub_dir,
                                       cur_channel_sub_src_dir, cur_channel_subtitle_languages, cur_channel_image_name)
            tv_channels.append(cur_tv_channel)
        return tv_channels

    def refresh_state(self):
        self.clips = get_media_files_from_server(self.channel_clip_dir, 'clips')
        self.subtitles_on_server = get_media_files_from_server(self.channel_sub_dir, 'subtitles')
        self.subtitles_on_source = get_subtitle_files_from_source(self.channel_sub_src_dir)

TV_CHANNELS_STATE = TVChannel.get_tv_channels(PROVIDER_CONFIG)
