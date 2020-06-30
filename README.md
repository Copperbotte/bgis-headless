this is a test of a blender GIS interface to work in headless mode.

Current bugs:
- extracting the bigs repo into the addons folder does not automatically install bgis as an addon
- instead, running addon_install and addon_enable does not install bgis from a different directory
- running bgis from a new .blend properly scale
- sometimes, running bgis results in this error:
  ```python
  ValueError: Converting py args to operator properties: : 'building' not found in ()
  ```

Todo:
- build the bgis flask server
- build the interface flask server
- add zoom parameter into bgis request
- make bgis server a k8s cluster
