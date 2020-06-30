
import bpy

#def custom_render():
#    path = "C:\\Users\\Joe\\Desktop"
#    bpy.context.scene.render.filepath = path + "\\output.png"
#    bpy.ops.render.render(write_still=True)

#custom_render()

#bgis requires the addon to be enabled every time, and to set the cache every time

def bgis(address):
    #translate address to bounding box
    bpy.ops.view3d.map_search(query=address)
    
    #generate basemap from bounding box
    bpy.ops.view3d.map_headless_export(srckey="GOOGLE", laykey="SAT", grdkey="WM")
    
    #select basemap, for srtm to work right
    
    #generate strm height from basemap
    bpy.ops.importgis.srtm_query()
    
    #generate models, offset from strm
    #these tags are found in perfs.py, and are used in the enum filter as a set
    OSM_TAGS = [
        'building',
    #    'highway',
    #    'landuse',
    #    'leisure',
    #    'natural',
    #    'railway',
    #    'waterway'
    ]
    bpy.ops.importgis.osm_query(useElevObj=True,filterTags=set(OSM_TAGS))

#bgis("1 Rocket Road, Hawthorne, California")
#bgis("LC-39A, Florida")
#bgis("432 Park Avenue, New York City, New York")

def bgis_test(address):

    OSM_TAGS = [
        'building',
    #    'highway',
    #    'landuse',
    #    'leisure',
    #    'natural',
    #    'railway',
    #    'waterway'
    ]
    bpy.ops.importgis.osm_query(useElevObj=True,filterTags=set(OSM_TAGS))

#installs BGIS into the extracted blender archive
#this is only needed because extracting into the directory isn't working.
bpy.ops.preferences.addon_install(filepath='~/BlenderGIS-master')
bpy.ops.preferences.addon_enable(module='BlenderGIS-master')

#if bgis was installed, its present in this list.
for a in bpy.context.preferences.addons:
    print(a.module)
