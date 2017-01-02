#!/bin/sh
':' //; exec "$(command -v nodejs || command -v node)" "$0" "$@"

// command to give the node interpreter a call

if(process.argv.length<3) {
	console.log("Enter command variables")
	}
else
	console.log("Hello World, you are ", process.argv.slice(2))
