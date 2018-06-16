import xbmc
import xbmcgui
import youtube_resolver

stream = youtube_resolver.resolve("n7kYOhiMFiI")
if stream:
    xbmc.log("----------------TEST STREAM ---------------------------------")
    xbmc.log("{url}|{headers}".format(url=stream[0]["url"], headers=stream[0]["headers"]))
    xbmc.log("----------------TEST STREAM ---------------------------------")
    xbmcgui.Dialog().ok("TestStream", "Stream url printed to xbmc log. Make sure you enable debug logging.")
else:
    xbmcgui.Dialog().ok("TestStream", "Unable to resolve URL")

