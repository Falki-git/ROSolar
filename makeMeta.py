import os, argparse, sys, json, glob

class DefaultHelpParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

HELP_DESC = "Creates neccesary metadata files"
parser = DefaultHelpParser(description=HELP_DESC)
parser.add_argument('tag', metavar='tag', type=str, nargs=1,
                   help='tag of release (e.g. 0.4.6.0')

args = parser.parse_args()

if not args.tag or len(args.tag) < 1:
    print("ERROR: git tag must be specified and must be in the format major.minor.patch.build-configuration.e.g. 0.4.6.0")
    sys.exit(2)

version = args.tag[0]

if version.startswith('v'):
    version = version.split('v')[1]

major = int(version.split(".")[0])
minor = int(version.split(".")[1])
patch = int(version.split(".")[2])
build = int(version.split(".")[3])
# create AVC .version file
avc = {
	"NAME":"ROSolar",
	"URL":"https://github.com/KSP-RO/ROSolar/tree/master/GameData/ROSolar/ROSolar.version",
	"DOWNLOAD":"https://github.com/KSP-RO/ROSolar/releases",
	"GITHUB": {
		"USERNAME":"KSP-RO",
		"REPOSITORY":"ROSolar",
		"ALLOW_PRE_RELEASE":False
	},
	"VERSION": {
		"MAJOR": major,
		"MINOR": minor,
		"PATCH": patch,
		"BUILD": build
	},
	"KSP_VERSION_MIN": {
		"MAJOR": "1",
		"MINOR": "10",
		"PATCH": "1"
	},
	"KSP_VERSION_MAX": {
		"MAJOR": "1",
		"MINOR": "12",
		"PATCH": "99"
	}
}
with open("ROSolar.version", "w") as f:
	f.write(json.dumps(avc, indent=4))
