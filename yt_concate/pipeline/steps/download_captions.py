import logging

import yt_dlp

from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        ydl_opts = {
            'writesubtitles': True,
            'writeautomaticsub': True,
            'skip_download': True,
            'subtitleslangs': ['en'],
            'outtmpl': utils.get_caption_dir() + '/%(id)s.%(ext)s',
            'encoding': 'utf-8',
        }

        for yt in data:
            logging.getLogger().info(f'dowmloading caption for {yt.id}')
            if utils.caption_file_exists(yt):
                logging.getLogger().info(f'found existing caption file')
                continue
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([yt.url])
            # break
        return data
