FROM ubuntu:16.04
RUN apt-get update -y && \
	apt-get install -y python3-pip python3-dev curl tar blender

RUN mkdir /app
WORKDIR /app

COPY . .

RUN curl -fsSL https://ftp.nluug.nl/pub/graphics/blender/release/Blender2.83/blender-2.83.0-linux64.tar.xz | tar xJ
RUN git clone https://github.com/domlysz/BlenderGIS.git ./blender-2.83.0-linux64/2.83/scripts/addons/BlenderGIS-master
RUN cp view3d_mapviewer.py ./blender-2.83.0-linux64/2.82/scripts/addons/BlenderGIS-master/operators
RUN mkdir ./blender-2.83.0-linux64/2.83/config
RUN cp userpref.blend ./blender-2.83.0-linux64/2.83/config

#flask server stuff
#RUN pip3 install -r requirements.txt
#ENTRYPOINT ["python3"]
#CMD ["test.py"]

#addon via command line
#RUN blender -b bgis.blend -o bgis_ --addons BlenderGIS-master --python blenderscript.py

#addon via script
#RUN blender -b bgis.blend -o bgis_ --python blenderscript.py