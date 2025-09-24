# build image
docker build -t basictext-app .

# run container (เชื่อม port 5000 ในเครื่องกับ container)
docker run -it --rm -p 5000:5000 basictext-app
