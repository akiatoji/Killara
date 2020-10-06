docker rm $(docker ps -a -q)
docker build -t threed_img . 
docker run -it -p 9888:8888 --mount src="$(pwd)",target=/app,type=bind threed_img
