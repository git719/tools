#!/bin/bash
#@echo off
#rem 0. Assumes cdrecord/mkisofs are in the PATH
#rem 1. Create the image.iso using isomake.cmd script
#rem 2. Run cdrecord -scanbus to get the dev number

echo "cdrecord dev=4,0,0 image.iso"
echo ""
cdrecord dev=4,0,0 image.iso
