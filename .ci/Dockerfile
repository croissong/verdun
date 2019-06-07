FROM alpine/git

RUN apk add --no-cache python3 docker nodejs-current yarn git make curl gnupg openssh-client --repository=http://dl-cdn.alpinelinux.org/alpine/edge/main
ADD requirements.txt .
RUN pip3 install -r requirements.txt
ADD . ./
RUN wget https://github.com/roboll/helmfile/releases/download/v0.73.0/helmfile_linux_amd64 -O /usr/local/bin/helmfile
