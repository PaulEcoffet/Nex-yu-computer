#!/bin/zsh

for uifile in **/*.ui
do
	filename=`basename -s .ui ${uifile}`".py"
	folder="../src/ui/"`dirname ${uifile}`
	if [ ! -d $folder ]
	then
		mkdir -p $folder 
	fi
	if [ ! -f $folder/__init__.py ]
	then
		touch $folder/__init__.py
	fi
	pyuic4 ${uifile} > ${folder}/${filename}
done

for rcfile in **/*.qrc
do
	filename=`basename -s .qrc ${rcfile}`"_rc.py"
	folder="../src/ui/"`dirname ${rcfile}`
	if [ ! -d $folder ]
	then
		mkdir -p $folder 
	fi
	if [ ! -f $folder/__init__.py ]
	then
		touch $folder/__init__.py
	fi

	pyrcc4 ${rcfile} > ${folder}/${filename}
done
