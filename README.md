# palo_streamlit_clear_stale_sessions

Need: Palo doesn't have a way to clear sessions through the gui. This program is written in python and uses: streamlit, netmiko and pandas.


### Operational overview
You could add an input for regex to match the ip's your looking for. Also, change the input to all streamlit. Getpass is still cli.

* 1. Install Streamlit 
* 2. Change credentials and file locations, uncomment #pano.send_command(f"clear session id {item}")
* 3. Run script by "run streamlit app.py"


### Contact
***If you have issues and need help reach out to colleybrb@gmail.com
