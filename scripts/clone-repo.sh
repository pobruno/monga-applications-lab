sudo kill -9 `sudo lsof -t -i:80`
rm -rf monga-applications-lab
git clone https://github.com/BrunoPolezaGomes/monga-applications-lab.git
sudo cp /home/monga/config.py /home/monga/monga-applications-lab/
sudo nohup python3 -u /home/monga/monga-applications-lab/app.py