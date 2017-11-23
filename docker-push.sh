#!/usr/bin/env bash
docker build -t base -f Dockerfile.base .
docker tag base janggunhee/base
docker push janggunhee/base