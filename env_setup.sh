# !/bin/bash


# Colored strings
function colored_green()      { echo "\033[0;32m${1}\033[0m"; }
function colored_cyan()       { echo "\033[0;36m${1}\033[0m"; }
function colored_light_red()  { echo "\033[1;31m${1}\033[0m"; }

# Colored echo
function echo_info()    { echo -e "$(colored_cyan "${1}")"; }
function echo_error()   { echo -e "$(colored_light_red "${1}")"; }
function echo_success() { echo -e "$(colored_green "${1}")"; }


function fail_to_cd()
{
	echo_error "Installation failed!!"
        echo_error "No such file or directory ${1} exiting"
	exit
}


function install_py_venv()
{
	ver_major=$(python3 -c"import sys; print(sys.version_info.major)")
	ver_minor=$(python3 -c"import sys; print(sys.version_info.minor)")
	if [ $ver_major -eq 3 ]; then
		echo "Python3.$ver_minor is found"
	else 
		echo "Current Python version: $ver_major.$ver_minor. Python3 is preferred. Exiting..."
		exit 1
	fi
	echo_info "Installing python virtual environment"
	sudo apt install -y python3.$ver_minor-venv
	echo_success "Python3.$ver_minor-venv is installed"
}



function create_py_venv()
{
	echo_info "Create Python Venv in ${PWD}"
	python3 -m venv env
}


function activate_py_venv()
{
	echo_info "Activate Python Venv"
	source env/bin/activate
}


function install_dependency()
{
	echo_info "Installing dependencies"
	pip install -r requirements.txt
	echo_success "Dependencies are installed"
}


function run_installer()
{
	install_py_venv
	create_py_venv
	activate_py_venv
	install_dependency
}

run_installer
