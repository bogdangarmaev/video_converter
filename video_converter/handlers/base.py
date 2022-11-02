# -*- coding: utf-8 -*-

import ffmpeg
import tornado.web
from tornado.httputil import HTTPServerRequest

from video_converter.handlers.validators import filename_is_supported_ffmpeg


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        tonality_coefficient = self.get_body_argument("video_tonality", default=None)
        body, filename = get_file_from_request(self.request, "file")

        if not filename_is_supported_ffmpeg(filename):
            self.set_status(400)
            self.write({"file": f" format of {filename} is not supported"})
            return

        with open(filename, "wb") as out:
            out.write(body)

        clip = ffmpeg.input(filename)
        if tonality_coefficient is not None:
            audio = _change_tonality(clip.audio, int(tonality_coefficient))
            clip = ffmpeg.concat(clip, audio, v=1, a=1)

        output = clip.output(
            "output.m3u8",
            format="hls",
            start_number=0,
            hls_time=1,
            hls_list_size=0,
            g=30,
        )
        output.run()


def get_file_from_request(request: HTTPServerRequest, key: str) -> tuple[bytes, str]:
    filename = request.files[key][0].filename
    body = request.files[key][0].body
    return body, filename


def _change_tonality(audio, tonality_coefficient: float | int):
    return (
        audio.filter("asetrate", sample_rate=44100 * tonality_coefficient)
        .filter("aresample", sample_rate=44100)
        .filter("atempo", tempo=1 / tonality_coefficient)
    )
