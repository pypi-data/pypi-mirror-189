FROM python:3.9-alpine

RUN apk update

# AWS CLI
RUN apk add aws-cli

# TERRAFORM
RUN apk add terraform 

# TERRAFORM PLUGINS
COPY providers /providers
ENV TF_PLUGIN_CACHE_DIR /providers
RUN terraform -chdir=/providers init

# OTHER PACKAGES
RUN apk add vim ncurses
RUN pip install pyyaml simple-term-menu yaspin

COPY projects /projects
COPY scripts /scripts
COPY templates /templates

ENTRYPOINT ["python3", "scripts/entrypoint.py"]