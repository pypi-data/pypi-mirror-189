# fabproj-manager
A CLI to help create new fabric project templates in an effort to standardize experiment structure.

## Usage
`fabproj --add --name --local <fabric project name>`
- Replace <fabric project name> with a desired name
- `--add`: required to add project
- `--name`: optional, default is myProj
- `--local`: only include if you will be running scripts on local machine as well; creates another folder for these.
Once you run the above command, you should see a new set of folders that serve as a template
for your fabric project.