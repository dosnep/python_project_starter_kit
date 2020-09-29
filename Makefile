help:
	@echo "dev : Init a dev environment"
	@echo "clean : Clean repo"
	@echo "format : Reformat python code" 
	@echo "package : Build a pex file of your project" 

clean:
	@if [ -d "./.venv" ]; then rm -r ./.venv; fi; if [ -d "./dist" ]; then rm -r ./dist; fi;

dev:
	@if [ ! -d "./.venv" ]; then python -m venv ./.venv && . ./.venv/bin/activate && pip install -r ./requirements/requirements.txt; fi;

format:	dev
	@black ./project/*

package: clean dev format
	@. ./.venv/bin/activate && if [ ! -d "./dist" ]; then mkdir ./dist; fi; pex . -m project -o ./dist/project.pex --disable-cache
