#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Chris Griffith"
from pathlib import Path

import pkg_resources

name = "Copy"

video_extensions = [".mkv", ".mp4", ".ts", ".mov", ".webm", ".avi", ".mts", ".m2ts", ".m4v", ".gif", ".avif", ".webp"]
video_dimension_divisor = 1
icon = str(Path(pkg_resources.resource_filename(__name__, f"../../data/icons/black/onyx-copy.svg")).resolve())

enable_subtitles = True
enable_audio = True
enable_attachments = True


from fastflix.encoders.copy.command_builder import build
from fastflix.encoders.copy.settings_panel import Copy as settings_panel
