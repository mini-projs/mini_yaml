REPO_URL := git@github.com:pokerLL/mini_yaml.git

init:
	# poetry init
	git init
	git remote add origin $(REPO_URL)

commit:
	git add .
	git commit -a -m 'update'

push: commit
	git push

clean:
	echo "clean ..."