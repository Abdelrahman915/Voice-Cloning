############################ Original Image #############################
# FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime
# RUN ["apt", "update"]
# RUN ["apt", "install", "-y", "build-essential"]
# RUN ["pip", "install", "-U", "pip", "setuptools", "wheel"]
# RUN ["pip", "install", "-U", "so-vits-svc-fork"]
#######################################################################
FROM abdelrahman915/imageprefinal:Thelastdance

WORKDIR /app

COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt 

EXPOSE 8080

# Run the FastAPI app using Uvicorn server
CMD ["python", "app.py"]
