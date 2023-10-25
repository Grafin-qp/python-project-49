install: #установка программы
	poetry install

brain-games: #запуск программы
	poetry run brain-game

build: #собирает пакет
	poetry build

publish: #публикация пакета
	poetry publish --dry-run

package-install: #установка пакета
	python3 -m pip install --user dist/*.whl


