sudo kill -9 `sudo lsof -t -i:80`
sudo kill -9 `sudo lsof -t -i:3000`
rm -rf monga-applications-lab
rm -rf mgpt
git clone https://github.com/BrunoPolezaGomes/monga-applications-lab.git
git clone https://github.com/robjunior/mgpt.git
sudo cp /home/monga/config.py /home/monga/monga-applications-lab/
sudo nohup python3 -u /home/monga/monga-applications-lab/app.py
#sudo nohup python3 -u /home/monga/monga-applications-lab/bot.py
sudo nohup python3 -u /home/monga/monga-applications-lab/app.py

#sudo python3 /home/monga/monga-applications-lab/bot.py