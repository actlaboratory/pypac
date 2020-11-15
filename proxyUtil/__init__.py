"""
proxyUtil: Proxy auto-config for Python
===================================

Copyright 2018 Carson Lam
Copyright 2020 Hiroki Fujii

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from proxyUtil.api import get_pac, collect_pac_urls, download_pac, PACSession, pac_context_for_url, virtualProxyEnviron
from proxyUtil import __pyinstaller


__version__ = '0.1.1'


__all__ = [
    'get_pac', 'collect_pac_urls', 'download_pac', 'PACSession', 'pac_context_for_url', 'virtualProxyEnviron', '__pyinstaller'
]
