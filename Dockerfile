#######################################
# Base image and common dependencies  #
#######################################
FROM ubuntu:24.04 AS base
# Install common packages and add deadsnakes PPA for multiple Python versions
RUN apt-get update && \
    apt-get install -y --no-install-recommends software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        wget \
        ca-certificates \
        && rm -rf /var/lib/apt/lists/*

# add user for building and running
RUN adduser kp

# copy files into the image
COPY . /kpindex
RUN chown kp:kp -R /kpindex

#######################################
# Stage for Python 3.10               #
#######################################
FROM base AS py310
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3.10 \
        python3.10-venv \
        python3.10-dev && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
USER kp
# Create a virtual environment, upgrade pip and install your package (editable mode)
RUN cd /app && python3.10 -m venv venv && \
    ./venv/bin/pip install --upgrade pip 
CMD ["tail", "-f", "/dev/null"]
#######################################
# Stage for Python 3.11               #
#######################################
FROM base AS py311
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3.11 \
        python3.11-venv \
        python3.11-dev && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
USER kp
# Create a virtual environment, upgrade pip and install your package (editable mode)
RUN cd /app && python3.11 -m venv venv && \
    ./venv/bin/pip install --upgrade pip 
CMD ["tail", "-f", "/dev/null"]
#######################################
# Stage for Python 3.12               #
#######################################
FROM base AS py312
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3.12 \
        python3.12-venv \
        python3.12-dev && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
USER kp
# Create a virtual environment, upgrade pip and install your package (editable mode)
RUN cd /app && python3.12 -m venv venv && \
    ./venv/bin/pip install --upgrade pip 
CMD ["tail", "-f", "/dev/null"]
#######################################
# Stage for Python 3.13               #
#######################################
FROM base AS py313
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3.13 \
        python3.13-venv \
        python3.13-dev && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
USER kp
# Create a virtual environment, upgrade pip and install your package (editable mode)
RUN cd /app && python3.13 -m venv venv && \
    ./venv/bin/pip install --upgrade pip 
CMD ["tail", "-f", "/dev/null"]

