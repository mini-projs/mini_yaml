REPO_URL := git@github.com:pokerLL/mini_yaml.git

init:
	# poetry init
	git init
	git remote add origin $(REPO_URL)

test: 
	poetry run pytest -s -v tests

commit:
	git add .
	git commit -a -m 'update'

push: test commit
	git push

clean:
	echo "clean ..."