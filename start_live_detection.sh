# !/bin/bash

# Colored strings
function colored_cyan()       { echo "\033[0;36m${1}\033[0m"; }

# Colored echo
function echo_info()    { echo -e "$(colored_cyan "${1}")"; }


function fail_to_cd()
{
    echo_error "No such file or directory ${1} exiting"
	exit
}


ROOT_PATH=${PWD}
SRC_PATH="${ROOT_PATH}/src/"
MAIN_FUNC="live_detection.py"

echo_info "Activating Python Virtual Environment"
source ${ROOT_PATH}/env/bin/activate
cd "${SRC_PATH}" || fail_to_cd "${SRC_PATH}"
echo_info "Starting live detection ..."
python3 ${MAIN_FUNC}