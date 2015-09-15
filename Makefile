dep : gui_rc.py
	cd superboucle; $(MAKE) dep

run : dep
	python3 launch.py

gui_rc.py : gui.qrc icons/*
	pyrcc5 gui.qrc > gui_rc.py
