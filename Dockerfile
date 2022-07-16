FROM osrf/ros:foxy-desktop
RUN sudo apt-get update -y && \
  sudo apt-get install -y python3 \
  python3-pip

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ./ ./
RUN pip install -r requirements.txt
SHELL ["/bin/bash", "-c"]
ENTRYPOINT [ "/ros_entrypoint.sh" ]
CMD ["bash"]