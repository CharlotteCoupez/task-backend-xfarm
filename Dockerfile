FROM python:3.11
# Set the working directory inside the container
WORKDIR /app

# Install system dependencies for OpenCV and Git
RUN apt-get update && apt-get install -y \
    git \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Install MobileSAM separately from GitHub
RUN pip install git+https://github.com/dhkim2810/MobileSAM.git


COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]