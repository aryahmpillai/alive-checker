# Alive Checker
A lightweight Python CLI tool that checks which subdomains from a list are alive. It sends HTTP/HTTPS requests to each host and reports the ones that respond, so you can quickly narrow a large subdomain list down to live targets for recon and bug bounty work.
## Features

Checks alive hosts
Saves alive domains

## Installation
git clone https://github.com/aryahmpillai/alive-checker.git

cd alive-checker

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt


python3 alive-checker -h

## For Globally run
chmod +x alive-checker

## Usage
alive-checker
 
