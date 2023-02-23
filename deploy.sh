#!/bin/bash
echo "started"
cd app
#1
docker build -t 80XXXXXXXXXX.dkr.ecr.us-east-1.amazonaws.com/notifyme:latest . &&
#2
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 80XXXXXXXXXX.dkr.ecr.us-east-1.amazonaws.com &&
#3
docker push 80XXXXXXXXXX.dkr.ecr.us-east-1.amazonaws.com/notifyme:latest &&
#4
OLD_TASK_ID=$(aws ecs list-tasks --cluster notifymeCluster --desired-status RUNNING --family notifymetask | egrep "task/" | sed -E "s/.*task\/(.*)\"/\1/")
aws ecs stop-task --cluster notifymeCluster --task ${OLD_TASK_ID} &&
#5 start-task will actually hard pull the image again (ignore the cache)
aws ecs start-task --task-definition notifymetask:6 --cluster notifymeCluster --container-instances 82XXXXXXXXXX4f45b96655XXXXXXXXXX &


