# 1. load module
module load python-2.7
# 2. create virtual environment
virtualenv --system-site-packages flask
# 3. activate virtual environment
source flask/bin/activate
# 4. install required packages in venv
pip install -r requirements.txt
# 5. locate in the web application folder
cd app
# 6. start web server
python server.py
# 7. Access the web app at: http://linserv2.cims.nyu.edu:40555/