#!/bin/zsh

rm -rf ../nexyu/ui/**

for uifile in **/*.ui
do
	filename=`basename -s .ui ${uifile}`".py"
	folder="../nexyu/ui/"`dirname ${uifile}`
	if [ ! -d $folder ]
	then
		mkdir -p $folder
	fi
		echo "converting ${uifile} in ${folder}/${filename}"
	pyuic4 ${uifile} -o ${folder}/${filename}
done

for rcfile in **/*.qrc
do
	filename=`basename -s .qrc ${rcfile}`"_rc.py"
	folder="../nexyu/ui/"`dirname ${rcfile}`
	if [ ! -d $folder ]
	then
		mkdir -p $folder
	fi
	echo "converting ${rcfile} in ${folder}/${filename}"
	pyrcc4 ${rcfile} > ${folder}/${filename}
done

echo "Creation of the missing __init__.py"
find ../nexyu/ui/ -type d -exec touch {}/__init__.py \;
