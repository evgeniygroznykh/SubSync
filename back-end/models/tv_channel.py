from config import PROVIDER_CONFIG
from models.clip import Clip
from models.subtitle import Subtitle
from file_handler import get_media_files_from_server, get_subtitle_files_from_source, get_base_name_list


TV_CHANNELS_CFG_KEY = 'tv_channels'
CHANNEL_NAME_CFG_KEY = 'channelName'
CHANNEL_M_CLIP_DIR_CFG_KEY = 'channelMainClipDirectory'
CHANNEL_M_SUBTITLE_DIR_CFG_KEY = 'channelMainSubtitleDirectory'
CHANNEL_B_CLIP_DIR_CFG_KEY = 'channelBackupClipDirectory'
CHANNEL_B_SUBTITLE_DIR_CFG_KEY = 'channelBackupSubtitleDirectory'
CHANNEL_SUBTITLE_SRC_DIR_CFG_KEY = 'channelSubtitleSourceDirectory'
CHANNEL_SUBTITLE_LANGUAGES_CFG_KEY = 'channelSubtitleLanguages'
CHANNEL_IMAGE_NAME_CFG_KEY = 'channelImageName'

CLIP_QUERY_TARGET = 'clips'
SUBTITLE_QUERY_TARGET = 'subtitles'

class TVChannel:
    def __init__(self, channel_name, channel_m_clip_dir, channel_m_sub_dir,
                                        channel_b_clip_dir, channel_b_sub_dir, 
                                            channel_sub_src_dir, subtitle_languages, image_name):
        self.channel_name = channel_name
        self.channel_m_clip_dir = channel_m_clip_dir
        self.channel_m_sub_dir = channel_m_sub_dir
        self.channel_b_clip_dir = channel_b_clip_dir
        self.channel_b_sub_dir = channel_b_sub_dir
        self.channel_sub_src_dir = channel_sub_src_dir
        self.subtitle_languages = subtitle_languages
        self.channel_image_name = image_name

        self.clips = []
        self.subtitles = []

        self.subtitles_on_m_server = []
        self.subtitles_on_b_server = []
        self.subtitles_on_source = []

    @staticmethod
    def get_tv_channels(config):
        tv_channels = []
        channel_nodes = config[TV_CHANNELS_CFG_KEY]
        for node in channel_nodes:
            cur_channel_name = node[CHANNEL_NAME_CFG_KEY]
            cur_channel_m_clip_dir = node[CHANNEL_M_CLIP_DIR_CFG_KEY]
            cur_channel_m_sub_dir = node[CHANNEL_M_SUBTITLE_DIR_CFG_KEY]
            cur_channel_b_clip_dir = node[CHANNEL_B_CLIP_DIR_CFG_KEY]
            cur_channel_b_sub_dir = node[CHANNEL_B_SUBTITLE_DIR_CFG_KEY]
            cur_channel_sub_src_dir = node[CHANNEL_SUBTITLE_SRC_DIR_CFG_KEY]
            cur_channel_subtitle_languages = node[CHANNEL_SUBTITLE_LANGUAGES_CFG_KEY]
            cur_channel_image_name = node[CHANNEL_IMAGE_NAME_CFG_KEY]
            cur_tv_channel = TVChannel(cur_channel_name, cur_channel_m_clip_dir, cur_channel_m_sub_dir,
                                        cur_channel_b_clip_dir, cur_channel_b_sub_dir,
                                       cur_channel_sub_src_dir, cur_channel_subtitle_languages, 
                                       cur_channel_image_name)
            tv_channels.append(cur_tv_channel)
        return tv_channels

    def get_clip_info(self):
        m_clips = get_media_files_from_server(self.channel_m_clip_dir, CLIP_QUERY_TARGET)
        b_clips = get_media_files_from_server(self.channel_m_clip_dir, CLIP_QUERY_TARGET)
        clip_list = list(set(m_clips + b_clips))
        clip_names_no_ext = get_base_name_list(clip_list)

        m_subtitle_names = get_base_name_list(self.subtitles_on_m_server)
        b_subtitle_names = get_base_name_list(self.subtitles_on_b_server)

        clip_info = []
        for clip_base_name in clip_names_no_ext:
            for lang in self.subtitle_languages:
                has_sub_on_main = f"{clip_base_name}_{lang}" in m_subtitle_names
                has_sub_on_backup = f"{clip_base_name}_{lang}" in b_subtitle_names
                
                clip_info.append(Clip(clip_base_name, has_sub_on_main, has_sub_on_backup))
        return clip_info

    def get_subtitle_info(self):
        sub_list = list(set(self.subtitles_on_m_server + self.subtitles_on_b_server))
        sub_names_no_ext = get_base_name_list(sub_list)

        m_subtitle_names = get_base_name_list(self.subtitles_on_m_server)
        b_subtitle_names = get_base_name_list(self.subtitles_on_b_server)
 
        src_sub_names = get_base_name_list(self.subtitles_on_source)

        sub_info = []
        for sub_base_name in sub_names_no_ext:
            is_on_main = sub_base_name in m_subtitle_names
            is_on_backup = sub_base_name in b_subtitle_names
            is_on_src = sub_base_name in src_sub_names

            sub_info.append(Subtitle(sub_base_name, is_on_main, is_on_backup, is_on_src))
        return sub_info

    def refresh_state(self):
        self.subtitles_on_source = get_subtitle_files_from_source(self.channel_sub_src_dir)

        self.subtitles_on_m_server = get_media_files_from_server(self.channel_m_sub_dir, SUBTITLE_QUERY_TARGET)
        self.subtitles_on_b_server = get_media_files_from_server(self.channel_b_sub_dir, SUBTITLE_QUERY_TARGET)

        self.clips = self.get_clip_info()
        self.subtitles = self.get_subtitle_info()


TV_CHANNELS_STATE = TVChannel.get_tv_channels(PROVIDER_CONFIG)
