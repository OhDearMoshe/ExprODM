### Flask with python 3.4

Contains everything you need to run flask on ubunutu with python 3.4.

To Build locally
```
docker build -t flask:3.4 .
```

It even includes a test app. You can try it out by:
```
docker run -i -t -P -d flask:3.4 python -m flask run --host=0.0.0.0
```
Then grab the port from docker
```
docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                           NAMES
c1090793c344        flask:3.4           "python -m flask run "   2 seconds ago       Up 1 seconds        0.0.0.0:32779->5000/tcp
```

Then go to the correct url in your browser to try it out

```
http://127.0.0.1:32779/
```
