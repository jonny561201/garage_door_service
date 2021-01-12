#!/usr/bin/env bash

YELLOW='\033[1;33m'
WHITE='\033[0m'
RED='\033[0;31m'

GARAGE_DOOR_SERVICE_FILE=garageDoorStatus.service


function cloneServiceFiles {
    if [[ -d "/home/pi/garage_door_service" ]]; then
        echo -e "${YELLOW}---------------Service Folder Exists---------------${WHITE}"
        cd /home/pi/garage_door_service
        git pull
    else
        echo -e "${YELLOW}---------------Cloning Service---------------${WHITE}"
        cd /home/pi/
        git clone https://github.com/jonny561201/garage_door_service.git /home/pi/garage_door_service
    fi
}

function installDependencies {
    echo -e "${YELLOW}---------------Installing Dependencies---------------${WHITE}"
    pip3 install -Ur requirements.txt
}

function stopService {
    echo -e "${YELLOW}---------------Stopping Service---------------${WHITE}"
    sudo systemctl stop ${GARAGE_DOOR_SERVICE_FILE}
    sudo rm /lib/systemd/system/${GARAGE_DOOR_SERVICE_FILE}
}

function copyServiceFile {
    echo  -e "${YELLOW}---------------Creating SystemD---------------${WHITE}"
    sudo chmod 666 ./deployment/${GARAGE_DOOR_SERVICE_FILE}
    sudo yes | sudo cp ./deployment/${GARAGE_DOOR_SERVICE_FILE} /lib/systemd/system/${GARAGE_DOOR_SERVICE_FILE}
}

function configureSystemD {
    echo  -e "${YELLOW}---------------Configuring SystemD---------------${WHITE}"
    sudo systemctl daemon-reload
    sudo systemctl enable ${GARAGE_DOOR_SERVICE_FILE}
}

function restartDevice {
    echo  -e "${YELLOW}---------------Rebooting Device---------------${WHITE}"
    sudo reboot
}

function createEnvironmentVariableFile {
    if [[ ! -f "/home/pi/garage_door_service/serviceEnvVariables" ]]; then
        echo -e "${YELLOW}---------------Creating Environment Variable File---------------${WHITE}"
        createFile
    else
        echo -e "${YELLOW}---------------Environment Variable File Already Exists---------------${WHITE}"
        echo 'Would you like to recreate serviceEnvVariables file? (y/n)'
        read USER_RESPONSE
        if [[ ${USER_RESPONSE} == "y" ]]; then
            createFile
        fi
    fi
    echo -e "${YELLOW}---------------Exporting Environment Variables---------------${WHITE}"
    set -o allexport; source serviceEnvVariables; set +o allexport
}

function createFile {
    echo -e "Enter FILE_NAME:${WHITE}"
    read FILE_NAME

    echo "FILE_NAME=${FILE_NAME}" > serviceEnvVariables
}


stopService
cloneServiceFiles
installDependencies
createEnvironmentVariableFile
copyServiceFile
configureSystemD
restartDevice