# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 Petter Reinholdtsen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


#url-s for watching shqip-tv channels

stream1url = 'rtmp://66.55.93.204/livepkgr//stream?adbe-live-event=report'

stream2url = 'http://stream1.rtkit.com:1935/rtk2stream/rtk2.stream/playlist.m3u8'

stream3url = ''

stream4url = ''

#url-s for listening RTK radio stations
stream1radiourl = ''

stream2radiourl = ''

#iconImages for channels and radio stations

iconImageRtk1='http://rtklive.com/kodi/img/rtk1w.png'
iconImageRtk2='http://rtklive.com/kodi/img/rtk2w.png'
iconImageRtk3='http://rtklive.com/kodi/img/rtk3w.png'
iconImageRtk4='http://rtklive.com/kodi/img/rtk4w.png'

iconImageRk1='http://rtklive.com/kodi/img/rk1w.png'
iconImageRk2='http://rtklive.com/kodi/img/rk1w.png'

#fanart_image for all items
fanart='http://www.rtklive.com/kodi/img/bg.jpg'

import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'videos')

li = xbmcgui.ListItem('Report 1', iconImage=iconImageRtk1)
li.setProperty('IsPlayable', 'true')
li.setInfo('videos', {'mediatype' : 'video'})
li.setProperty('fanart_image',fanart)

xbmcplugin.addDirectoryItem(handle=addon_handle, url=stream1url, listitem=li)


li = xbmcgui.ListItem('News24', iconImage=iconImageRtk2)
li.setProperty('IsPlayable', 'true')
li.setInfo('videos', {'mediatype' : 'video'})
li.setProperty('fanart_image',fanart)

xbmcplugin.addDirectoryItem(handle=addon_handle, url=stream2url, listitem=li)

li = xbmcgui.ListItem('RTK3', iconImage=iconImageRtk3)
li.setProperty('IsPlayable', 'true')
li.setInfo('videos', {'mediatype' : 'video'})
li.setProperty('fanart_image',fanart)

xbmcplugin.addDirectoryItem(handle=addon_handle, url=stream3url, listitem=li)


li = xbmcgui.ListItem('RTK4', iconImage=iconImageRtk4)
li.setProperty('IsPlayable', 'true')
li.setInfo('videos', {'mediatype' : 'video'})
li.setProperty('fanart_image',fanart)

xbmcplugin.addDirectoryItem(handle=addon_handle, url=stream4url, listitem=li)

li = xbmcgui.ListItem('RadioKosova1', iconImage=iconImageRk1)
li.setProperty('IsPlayable', 'true')
li.setInfo('videos', {'mediatype' : 'video'})
li.setProperty('fanart_image',fanart)

xbmcplugin.addDirectoryItem(handle=addon_handle, url=stream1radiourl, listitem=li)


li = xbmcgui.ListItem('RadioKosova2', iconImage=iconImageRk2)
li.setProperty('IsPlayable', 'true')
li.setInfo('videos', {'mediatype' : 'video'})
li.setProperty('fanart_image',fanart)

xbmcplugin.addDirectoryItem(handle=addon_handle, url=stream2radiourl, listitem=li)


xbmcplugin.endOfDirectory(addon_handle)

