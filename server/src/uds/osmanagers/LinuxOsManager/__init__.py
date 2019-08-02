# -*- coding: utf-8 -*-

#
# Copyright (c) 2012 Virtual Cable S.L.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#    * Neither the name of Virtual Cable S.L. nor the names of its contributors
#      may be used to endorse or promote products derived from this software
#      without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
@author: Adolfo Gómez, dkmaster at dkmon dot com
"""
from __future__ import unicode_literals

from django.utils.translation import ugettext_noop as _
from uds.core.osmanagers.osmfactory import OSManagersFactory
from uds.core.managers.DownloadsManager import DownloadsManager
from uds.core import VERSION

from .LinuxOsManager import LinuxOsManager
from .LinuxRandomPassOsManager import LinuxRandomPassManager
import os.path
import sys

OSManagersFactory.factory().insert(LinuxOsManager)
OSManagersFactory.factory().insert(LinuxRandomPassManager)

DownloadsManager.manager().registerDownloadable('udsactor_{version}_all.deb'.format(version=VERSION),
                                                _('UDS Actor for Debian, Ubuntu, ... Linux machines <b>(Requires python >= 3.5)</b>'),
                                                os.path.dirname(sys.modules[__package__].__file__) + '/files/udsactor_{version}_all.deb'.format(version=VERSION),
                                                'application/x-debian-package')

DownloadsManager.manager().registerDownloadable('udsactor-{version}-1.noarch.rpm'.format(version=VERSION),
                                                _('UDS Actor for Centos, Fedora, RH, ... Linux machines <b>(Requires python 2.7)</b>'),
                                                os.path.dirname(sys.modules[__package__].__file__) + '/files/udsactor-{version}-1.noarch.rpm'.format(version=VERSION),
                                                'application/x-redhat-package-manager')

DownloadsManager.manager().registerDownloadable('udsactor-opensuse-{version}-1.noarch.rpm'.format(version=VERSION),
                                                _('UDS Actor for openSUSE, ... Linux machines <b>(Requires python 2.7)</b>'),
                                                os.path.dirname(sys.modules[__package__].__file__) + '/files/udsactor-opensuse-{version}-1.noarch.rpm'.format(version=VERSION),
                                                'application/x-redhat-package-manager')

DownloadsManager.manager().registerDownloadable('udsactor_2.2.0_legacy.deb'.format(version=VERSION),
                                                _('<b>Legacy</b> UDS Actor for Debian, Ubuntu, ... Linux machines <b>(Requires python 2.7)</b>'),
                                                os.path.dirname(sys.modules[__package__].__file__) + '/files/udsactor_2.2.0_legacy.deb'.format(version=VERSION),
                                                'application/x-debian-package')
