#!/django-starter bash
cd $PWD


#if [ ! -f $HOME/bin/upload.py ]
#then
#wget -O $HOME/bin/upload.py  http://codereview.appspot.com/static/upload.py
#chmod +x $HOME/bin/upload.py
#fi


echo "Installing the basics"
curl -O http://python-distribute.org/distribute_setup.py
sudo python distribute_setup.py
sudo easy_install pip
sudo pip install virtualenv
sudo pip install virtualenvwrapper


echo "Populating virtual environment"
cd ..
virtualenv env --no-site-packages -p python2.6
#source env/bin/activate
env/bin/pip install -r requirements.txt


echo "Installing apps into project"
python env/src/django-css/setup.py install
mv env/src/django-css/compressor myproject/