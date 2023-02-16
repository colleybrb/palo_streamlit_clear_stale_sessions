# palo_streamlit_clear_stale_sessions

Need: Palo doesn't have a way to clear sessions through the gui. This program is written in python and uses: streamlit, netmiko and pandas. It connects and pulls sessions displays them in streamlit. You can select the sessions you want to clear and click clear session button to clear them. Then close the SSH session.

![image](https://user-images.githubusercontent.com/50241257/219487024-7c7e52cd-b4e7-4788-914c-6cb873caa600.png)


### Operational overview
You could add an input for regex to match the ip's your looking for. Also, change the input to all streamlit. Getpass is still cli.

* 1. Install Streamlit 
* 2. Change credentials and file locations, uncomment #pano.send_command(f"clear session id {item}")
* 3. Run script by "run streamlit stale_sessions.py"


### Contact
***If you have issues and need help reach out to colleybrb@gmail.com
