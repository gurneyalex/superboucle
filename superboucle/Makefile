
UI = gui_ui.py cell_ui.py learn_ui.py learn_cell_ui.py manage_ui.py new_song_ui.py add_clip_ui.py playlist_ui.py port_manager_ui.py add_port_ui.py

dep : $(UI)

%_ui.py : %_ui.ui
	@echo "compiling $<"
	pyuic5 $< > $@
