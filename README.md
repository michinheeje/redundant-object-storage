# Redundant-object-storage
 Redundant object storage</br>
`yum update -y`</br>
`reboot`</br>
`sudo su -`</br>
`aws configure`</br>
`aws configure --profile ncp`</br>
`pip install flask`</br>
`mkdir /uploads`</br>
`cd`</br>
`vi index.py`</br>
`crontab -e`</br>
`30 * * * * aws s3 sync /uploads/ s3://hwangheeje/`</br>
`30 * * * * aws --endpoint-url=https://kr.object.ncloudstorage.com s3 sync /uploads/ s3://hwangheeje/ --profile ncp`</br>
`* * * * * find /uploads -ctime +1 -exec rm -f {} \;`</br>
