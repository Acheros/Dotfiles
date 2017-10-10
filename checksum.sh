#!/bin/bash
if [[ -n "$1" ]]; then
	filename=$1
	echo -n "md5checksum: "
	md5sum $filename
	echo -n "sha1checksum: "
	sha1sum $filename
	echo -n "sha256checksum: "
	sha256sum $filename
	echo -n "sha512checksum: "
	sha512sum $filename
	echo -n "whirlpool: "
	whirlpooldeep $filename
else
	echo "agument error"
fi
