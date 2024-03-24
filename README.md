# **altair-vision-research**
Altair Team research repository for robot vision.

## **Usage**

### **1. Build the Docker Image**
Create the image with:

```console
sudo docker build -t altair-avr .
```

### **2. Compose the Docker Container**
After creating the image, proceed to compose the container with:

```console
sudo docker compose up -d
```

### **3. Check the Container**
Go to container's bash terminal and run an example with:

```console
# on host machine
sudo docker exec -it altair-avr bash   

# on docker container
colcon build
source install/setup.bash
ros2 launch avr_main publish_example_launch.py 
```

Open ```notebooks/subscribe_example.ipynb``` and run with Docker's Jupyter kernel. To access the Jupyter kernel (Jupyter server), go to ```<HOST_MACHINE_IP>:8888``` or if you are accessing directly from host machine, go to ```localhost:8888```. We will be asked for token to access the Jupyter server, run the following command to obtain the token:

```
# on docker container
jupyter server list
```

Copy the token from the ```?token=``` query.