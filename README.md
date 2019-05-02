# -Redundant-object-storage
 Redundant object storage
yum update -y
reboot
sudo su - 
aws configure
aws configure --profile ncp
pip install flask
mkdir /uploads
vi index.py
crontab -e
30 * * * * aws s3 sync /uploads/ s3://hwangheeje/
30 * * * * aws --endpoint-url=https://kr.object.ncloudstorage.com s3 sync /uploads/ s3://hwangheeje/ --profile ncp
* * * * * find /uploads -ctime +1 -exec rm -f {} \;
