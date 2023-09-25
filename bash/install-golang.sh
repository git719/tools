#!/bin/bash
# install-golang.sh
# Install GoLang in RHEL Linux or GitBash environment
# Notes
#   - RHEL 'shasum' command is in package perl-Digest-SHA

GOVER="1.21.1"
set -euo pipefail
if [[ "$OSTYPE" = "linux-gnu"* ]]; then
    Filename="go${GOVER}.linux-amd64.tar.gz"
elif [[ "$OSTYPE" = "darwin"* ]]; then
    Filename="go${GOVER}.darwin-amd64.tar.gz"
elif [[ "$OSTYPE" = "msys"* ]]; then
    Filename="go${GOVER}.windows-amd64.zip"
else
    printf "=> Unsupported OSTYPE = '$OSTYPE'\n" && exit 1
fi

check_binary() {
    printf "==> Checking for '$1' ... "
    if [[ -z "$(which $1 2>/dev/null)" ]]; then
        printf "missing!\n" && exit 1
    else
        printf "found\n"
    fi
}
for B in curl jq awk grep shasum ; do check_binary $B ; done

cd
[[ -d "go" ]] && printf "==> Directory 'go' already exists. Aborting!\n" && exit 1

Files=$(curl -sk "https://go.dev/dl/?mode=json")
printf "==> Downloading https://go.dev/dl/${Filename}\n\n"
curl -# -kLO https://go.dev/dl/${Filename}
if [[ -e ${Filename} ]]; then
    DigestLocal=$(shasum -a 256 ${Filename} | awk '{print $1}')
else
    printf "==> Error downloanding ${Filename}\n" && exit 1
fi
if [[ -n ${Files} ]]; then
    DigestRemote=$(echo "$Files" | jq -r '.[] | .files[] | "\(.filename) \(.sha256)"' | grep "$Filename" | awk '{print $2}')
else
    printf "==> Error getting JSON string with all digests\n" && exit 1
fi

printf "\n%-24s = %s\n" "SHA DIGEST REMOTE" "$DigestRemote"
printf "%-24s = %s\n" "SHA DIGEST DOWNLOADED" "$DigestLocal"
[[ "$DigestLocal" != "$DigestRemote" ]] && printf "\n==> SHA digest do NOT match. Aborting!\n" && exit 1
printf "\n==> SHA digests do match. Installing ... \n"

if [[ "${Filename}" == *.tar.gz ]]; then
    tar xzf $Filename
elif [[ "${Filename}" == *.zip ]]; then
    unzip -q $Filename
else
    printf "==> Unknown ${Filename} extension\n" && exit 1
fi

exit 0

