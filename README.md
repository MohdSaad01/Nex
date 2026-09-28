# Nex

**Nex** is a content addressed version control system designed to track changes to files, create immutable project snapshots, and manage different versions of a software project through commits, branches, and related version control operations.

## Project status

Nex is under active, incremental development.

### Currently implemented

* `nex init` — initialize a Nex repository
* `nex add` — stage files and store their content objects
* `nex commit` — create commits from the current staging area

For the detailed development progress and implementation history, see [`docs/development/progress.md`](docs/development/progress.md).


## Project scope and philosophy

Nex as a version control system is being built to help me as a developer to improve my python proficiency and make me a better developer. The development of this project would also assist and strengthen my understanding of Version Control.
The scope of this project is to be a **real, usable command line software tool**, not a CRUD application, demonstration script, tutorial project, or toy program.  
  
As Nex is being built primarily as a learning project, the implementation of Nex will be written entirely by me through raw problem-solving, experimentation, debugging, and reading official documentation. AI may only be used as a source of documentation and knowledge; for example, to explain concepts, clarify APIs, interpret error messages, discuss design principles, or point me toward relevant documentation. Any actual implementation, code, and problem-solving will be done by me.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.