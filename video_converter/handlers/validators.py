def filename_is_supported_ffmpeg(filename: str) -> bool:
    available_formats = (
        '.mp4',
        '.ts',
        '.mov',
        '.avi',
        '.y4m',
        '.mkv',
    )
    return filename in available_formats
